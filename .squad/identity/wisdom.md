---
last_updated: 2026-03-21T11:54:10.181Z
---

# Team Wisdom

Reusable patterns and heuristics learned through work. NOT transcripts — each entry is a distilled, actionable insight.

## Patterns

**Pattern:** Always validate registry JSON after edits. **Context:** `registry/index.json` is a complex xRegistry document. A missing comma or misplaced field breaks the catalog. Validate structure before committing.

**Pattern:** Rebuild the landing page from registry data, never edit the Parts table by hand. **Context:** The Available Parts table in `docs/index.md` must stay in sync with the registry. Regenerating it eliminates drift.

**Pattern:** Check `repository` URLs before accepting a registry entry. **Context:** Stale or incorrect URLs make the catalog unreliable. The Auditor should verify each Part's repository is accessible and public.

**Pattern:** Increment `epoch` on every registry mutation. **Context:** xRegistry uses epoch for optimistic concurrency. Consumers can detect changes by comparing epoch values.

**Pattern:** Use `componentscount` as a sanity check. **Context:** After adding or removing a component, verify that `componentscount` matches the actual number of entries in the `components` object.

**Pattern:** The problem-space index (`Find Parts By Problem Space`) is high-value. **Context:** Users discover SpecWorks by problem, not language. Keep this section accurate and well-organized — it's the main differentiator.

**Pattern:** docfx builds locally with `docfx docs/docfx.json`. **Context:** Always preview the site locally before pushing. The custom template in `docs/template/` and styles in `docs/styles/` affect rendering.
