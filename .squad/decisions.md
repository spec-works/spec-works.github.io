# Squad Decisions

## Active Decisions

### FD001: Registry is the single source of truth
The xRegistry catalog at `registry/index.json` is the authoritative record of all factory Parts. The landing page (`docs/index.md`) is generated from it, not maintained independently.

### FD002: xRegistry model compliance
All registry entries must conform to the xRegistry model defined in the `model` section of `index.json`. Required fields: componentid, name, description, componenttype, language, license, repository, status.

### FD003: Parts push, factory pulls
Part repos push their specs.json / linkset to the factory (via PR or API). The factory's Registrar validates and integrates. The factory never writes to Part repos.

### FD004: Landing page is generated
The Available Parts table in `docs/index.md` is regenerated from `registry/index.json` by the Publisher agent. Manual edits to the Parts table will be overwritten.

### FD005: Auditor is non-destructive
The Auditor reads Part repos and the registry. It reports findings (stale URLs, missing files, convention drift) but never modifies Part repos or the registry directly. Fixes are routed to the Registrar or the Part's own squad.

### FD006: Version tracking
Each component in the registry carries `versionid`, `versionsurl`, and `versionscount`. When a Part publishes a new version, the Registrar updates these fields and increments the registry `epoch`.

### FD007: Deprecation over deletion
Registry entries are never deleted. Parts that are retired are marked `"status": "deprecated"`. The Publisher excludes deprecated Parts from the Active table but keeps them in the full catalog.

### FD008: Component group structure
All specification-based libraries go in the `specification-libs` component group. New component groups may be added for different categories (e.g., tools, templates) but require a decision record.

## Governance

- All meaningful changes require team consensus
- Document architectural decisions here
- Keep history focused on work, decisions focused on direction
