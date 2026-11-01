"""Publish local plugin artifacts beside the generated well-known catalog."""

import argparse
import json
from pathlib import Path
import shutil
from urllib.parse import quote, urlsplit


def local_path(root, value):
    """Resolve a marketplace path without escaping its declared root."""
    if not isinstance(value, str) or not value or urlsplit(value).scheme:
        raise ValueError(f"Expected a local marketplace path, got {value!r}")
    if "\\" in value or urlsplit(value).query or urlsplit(value).fragment:
        raise ValueError(f"Invalid marketplace path: {value!r}")
    candidate = root / value
    if candidate.is_symlink() or any(parent.is_symlink() for parent in candidate.parents):
        raise ValueError(f"Marketplace path contains a symlink: {value!r}")
    path = candidate.resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError(f"Marketplace path escapes its root: {value!r}")
    return path


def normalize_types(catalog):
    for entry in catalog["entries"]:
        if "mediaType" in entry:
            if "type" in entry and entry["type"] != entry["mediaType"]:
                raise ValueError(f"Conflicting entry types: {entry['identifier']}")
            entry["type"] = entry.pop("mediaType")
        if entry.get("type") == "application/ai-catalog+json" and "data" in entry:
            normalize_types(entry["data"])


def publish(catalog_path, marketplace_path, source_root, site_root, site_url):
    base = urlsplit(site_url)
    if base.scheme not in ("http", "https") or not base.netloc or base.query or base.fragment:
        raise ValueError("Site URL must be an absolute HTTP(S) URL without query or fragment")
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    marketplace = json.loads(marketplace_path.read_text(encoding="utf-8"))
    normalize_types(catalog)
    entries = {entry["identifier"]: entry for entry in catalog["entries"]}
    well_known = site_root / ".well-known"
    if catalog_path.resolve().parent != well_known.resolve():
        raise ValueError("Catalog must be published in the site's .well-known directory")

    publications = []
    for plugin in marketplace["plugins"]:
        identifier = f"urn:marketplace:{marketplace['name']}:{plugin['name']}"
        entry = entries[identifier]
        plugin_root = local_path(source_root, plugin["source"])
        if not plugin_root.is_dir():
            raise FileNotFoundError(f"Missing plugin directory: {plugin_root}")
        # Reject symlinks instead of copying files outside the published feed.
        if plugin_root.is_symlink() or any(p.is_symlink() for p in plugin_root.rglob("*")):
            raise ValueError(f"Plugin contains a symlink: {plugin_root}")
        destination = well_known / plugin_root.relative_to(source_root.resolve())
        if not entry.get("data", {}).get("entries"):
            raise ValueError(f"Plugin has no inline artifact catalog: {identifier}")
        children = {child["identifier"]: child for child in entry["data"]["entries"]}
        for skill in plugin["skills"]:
            skill_root = local_path(plugin_root, skill)
            skill_file = skill_root / "SKILL.md"
            if not skill_file.is_file():
                raise FileNotFoundError(f"Missing skill document: {skill_file}")
            child = children[f"{identifier}:{skill_root.name}"]
            child["type"] = "application/agent-skills+md"
            artifact_path = quote(skill_file.relative_to(source_root.resolve()).as_posix(), safe="/")
            child["url"] = f"{site_url.rstrip('/')}/.well-known/{artifact_path}"
            child.pop("data", None)
        if len(children) != len(plugin["skills"]):
            raise ValueError(f"Unexpected artifact entries for plugin: {identifier}")
        publications.append((plugin_root, destination))

    if len(entries) != len(marketplace["plugins"]):
        raise ValueError("Catalog and marketplace plugin counts differ")
    for source, destination in publications:
        shutil.copytree(source, destination, dirs_exist_ok=True)
    catalog_path.write_text(json.dumps(catalog, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("catalog", type=Path)
    parser.add_argument("marketplace", type=Path)
    parser.add_argument("source_root", type=Path)
    parser.add_argument("site_root", type=Path)
    parser.add_argument("--site-url", required=True)
    args = parser.parse_args()
    publish(args.catalog, args.marketplace, args.source_root, args.site_root, args.site_url)
