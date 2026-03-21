# Squad Team

> SpecWorks Factory — Landing Page & Registry

This squad manages the SpecWorks Factory landing page and the xRegistry component catalog. It does NOT implement Parts — that work happens in individual Part repos with their own squads. This squad's job is factory-level: maintaining the catalog, rebuilding the landing page, and auditing Part compliance.

## Coordinator

| Name | Role | Notes |
|------|------|-------|
| Squad | Coordinator | Routes work, enforces handoffs and reviewer gates. |

## Members

| Name | Role | Charter | Status |
|------|------|---------|--------|
| Registrar | Registry Maintainer | [charter](agents/registrar/charter.md) | Active |
| Publisher | Landing Page Builder | [charter](agents/publisher/charter.md) | Active |
| Auditor | Compliance Checker | [charter](agents/auditor/charter.md) | Active |
| Scribe | Session Logger | [charter](agents/scribe/charter.md) | Active |

## Upstream

This squad inherits shared factory knowledge from `factory-squad`:
- Convention enforcement, spec-reading, language patterns
- Factory decisions (D001–D012)
- Factory wisdom patterns

## Project Context

- **Project:** spec-works.github.io (landing page + xRegistry catalog)
- **Registry:** `registry/index.json` — xRegistry format, 11 components in `specification-libs` group
- **Site:** docfx-generated, deployed to GitHub Pages
- **Created:** 2026-03-21
