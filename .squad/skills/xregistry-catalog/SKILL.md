# Skill: xRegistry Catalog Management

## Purpose

This skill covers the structure and manipulation of the xRegistry component catalog used by the SpecWorks Factory. The registry at `registry/index.json` follows the xRegistry specification.

## Registry Structure

```
registry/
├── index.json          # Full xRegistry document
└── componentgroups/    # (future) per-group split files
```

## xRegistry Document Layout

```json
{
  "specversion": "1.0-rc2",
  "registryid": "specworks-factory",
  "epoch": <integer>,           // Increment on every mutation
  "model": { ... },             // Schema for groups and resources
  "componentgroups": {
    "specification-libs": {
      "componentscount": <integer>,   // Must match actual count
      "components": {
        "<componentid>": {
          "componentid": "<kebab-case>",
          "versionid": "<semver>",
          "name": "<Human Readable>",
          "description": "...",
          "componenttype": "library|tool|template",
          "language": "csharp|python|rust|typescript|...",
          "framework": "dotnet|...",
          "license": "<SPDX>",
          "repository": "<github-url>",
          "homepage": "<docs-url>",
          "keywords": ["..."],
          "status": "active|deprecated|experimental",
          "maturity": "stable|beta|alpha"
        }
      }
    }
  }
}
```

## Required Fields Per Component

| Field | Type | Constraint |
|-------|------|------------|
| componentid | string | Lowercase kebab-case, unique within group |
| name | string | Human-readable display name |
| description | string | One-sentence summary |
| componenttype | string | One of: library, tool, template |
| language | string | Primary language |
| license | string | SPDX identifier (e.g., MIT) |
| repository | url | Must be accessible |
| status | string | One of: active, deprecated, experimental |

## Mutation Rules

1. **Always increment `epoch`** after any change
2. **Always update `componentscount`** after adding/removing components
3. **Always update `modifiedat`** with ISO 8601 timestamp
4. **Never delete components** — mark as `"status": "deprecated"`
5. **Preserve existing fields** — don't drop optional fields during updates

## Adding a New Component

```json
{
  "componentid": "new-part",
  "versionid": "1.0.0",
  "name": "New Part",
  "description": "Software component for ...",
  "documentation": "https://github.com/spec-works/new-part",
  "epoch": 1,
  "self": "https://spec-works.github.io/registry/componentgroups/specification-libs/components/new-part",
  "xid": "/componentgroups/specification-libs/components/new-part",
  "createdat": "<ISO-8601>",
  "modifiedat": "<ISO-8601>",
  "componenttype": "library",
  "language": "csharp",
  "framework": "dotnet",
  "license": "MIT",
  "repository": "https://github.com/spec-works/new-part",
  "homepage": "https://spec-works.github.io/new-part/",
  "keywords": ["..."],
  "status": "active",
  "maturity": "beta",
  "versionsurl": "https://spec-works.github.io/registry/componentgroups/specification-libs/components/new-part/versions",
  "versionscount": 1
}
```
