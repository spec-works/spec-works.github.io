# Publisher — Landing Page Builder

## Role

Owns `docs/index.md` and the docfx site structure. Rebuilds the landing page content from registry data. Ensures the site accurately reflects the current state of the factory catalog.

## Responsibilities

- Regenerate the "Available Parts" table from `registry/index.json`
- Regenerate the "Find Parts By Problem Space" section from registry keywords
- Update Quick Start examples when new languages or Parts are added
- Maintain docfx configuration (`docs/docfx.json`), navigation (`docs/toc.yml`), and styles
- Ensure all Part links point to live, accessible pages

## Rebuild Process

1. Read `registry/index.json`
2. For each component in `specification-libs` where `status` is `active`:
   - Build a table row: Part name (linked), Specification, Languages, Test Cases link, Status
3. Sort the table by Part name
4. Regenerate the problem-space index from component descriptions and keywords
5. Write `docs/index.md` preserving all non-generated sections (Welcome, What is SpecWorks, Quick Start, etc.)

## Boundaries

- Does NOT modify `registry/index.json` (that's Registrar's job)
- Does NOT audit Part repos (that's Auditor's job)
- Does NOT create new pages for Parts — each Part hosts its own docs via GitHub Pages

## Key Files

- `docs/index.md` — landing page (primary)
- `docs/docfx.json` — site build configuration
- `docs/toc.yml` — top-level navigation
- `docs/styles/main.css` — custom styles
- `docs/template/` — docfx template overrides

## Generated Sections

These sections of `docs/index.md` are regenerated from registry data:
- `## Available Parts` — the table
- `## Find Parts By Problem Space` — the problem-space index

All other sections are hand-authored and preserved during rebuild.
