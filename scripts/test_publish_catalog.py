import json
from pathlib import Path
import tempfile
import unittest
from urllib.parse import unquote, urljoin, urlsplit

from publish_catalog import publish


class PublishCatalogTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "feed"
        self.site = self.root / "site"
        self.skill = self.source / "plugins" / "example" / "skills" / "example skill"
        self.skill.mkdir(parents=True)
        (self.skill / "SKILL.md").write_text("# Example skill\n", encoding="utf-8")
        (self.skill.parent.parent / ".mcp.json").write_text("{}", encoding="utf-8")
        self.marketplace = self.source / "marketplace.json"
        self.marketplace.write_text(json.dumps({
            "name": "feed",
            "plugins": [{"name": "example", "source": "plugins/example",
                         "skills": ["./skills/example skill"]}],
        }), encoding="utf-8")
        self.catalog = self.site / ".well-known" / "ai-catalog.json"
        self.catalog.parent.mkdir(parents=True)
        self.catalog.write_text(json.dumps({
            "specVersion": "1.0",
            "entries": [{
                "identifier": "urn:marketplace:feed:example",
                "displayName": "example",
                "mediaType": "application/ai-catalog+json",
                "data": {"specVersion": "1.0", "entries": [{
                    "identifier": "urn:marketplace:feed:example:example skill",
                    "displayName": "example skill",
                    "mediaType": "application/json",
                    "url": "./skills/example skill",
                }]},
            }],
        }), encoding="utf-8")

    def run_publish(self):
        publish(self.catalog, self.marketplace, self.source, self.site, "https://example.org")

    def test_skill_urls_resolve_to_published_documents(self):
        self.run_publish()
        result = json.loads(self.catalog.read_text(encoding="utf-8"))
        plugin = result["entries"][0]
        self.assertNotIn("mediaType", plugin)
        child = plugin["data"]["entries"][0]
        self.assertEqual("application/agent-skills+md", child["type"])
        self.assertNotIn("mediaType", child)
        url = urljoin("https://example.org/.well-known/ai-catalog.json", child["url"])
        self.assertEqual(
            "/.well-known/plugins/example/skills/example%20skill/SKILL.md",
            urlsplit(url).path,
        )
        artifact = self.site / unquote(urlsplit(url).path).lstrip("/")
        self.assertEqual("# Example skill\n", artifact.read_text(encoding="utf-8"))
        self.assertTrue((self.site / ".well-known/plugins/example/.mcp.json").is_file())
        self.run_publish()  # Already normalized catalogs are supported.

    def test_missing_skill_fails_without_rewriting_catalog(self):
        original = self.catalog.read_bytes()
        (self.skill / "SKILL.md").unlink()
        with self.assertRaisesRegex(FileNotFoundError, "Missing skill document"):
            self.run_publish()
        self.assertEqual(original, self.catalog.read_bytes())

    def test_plugin_cannot_escape_feed(self):
        data = json.loads(self.marketplace.read_text(encoding="utf-8"))
        data["plugins"][0]["source"] = "../outside"
        self.marketplace.write_text(json.dumps(data), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "escapes"):
            self.run_publish()

    def test_conflicting_types_are_rejected(self):
        data = json.loads(self.catalog.read_text(encoding="utf-8"))
        data["entries"][0]["type"] = "application/json"
        self.catalog.write_text(json.dumps(data), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Conflicting"):
            self.run_publish()


if __name__ == "__main__":
    unittest.main()
