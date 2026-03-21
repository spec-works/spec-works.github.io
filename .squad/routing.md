# Work Routing

How to decide who handles what in the SpecWorks Factory landing page squad.

## Routing Table

| Work Type | Route To | Examples |
|-----------|----------|----------|
| Part registration | Registrar | New Part submits specs.json, add component to registry/index.json |
| Registry updates | Registrar | Update component version, language, status, maturity |
| Registry validation | Registrar | Validate index.json against xRegistry model, check URLs |
| Landing page content | Publisher | Rebuild Available Parts table, update problem-space index |
| Site structure | Publisher | docfx config, navigation, styles, template changes |
| Part compliance | Auditor | Check Part repos for required files, naming, test structure |
| Stale entry detection | Auditor | Find registry entries pointing to archived/deleted repos |
| Convention drift | Auditor | Compare Part structure against factory-spec conventions |
| Session logging | Scribe | Automatic — never needs routing |

## Registry Operations

The registry at `registry/index.json` is the single source of truth for the factory catalog.

**Adding a Part:**
1. Registrar receives specs.json from the Part (pushed by Part's Publisher agent)
2. Registrar validates the entry against xRegistry model and factory-spec §7
3. Registrar adds the component to `registry/componentgroups/specification-libs/components/`
4. Publisher rebuilds `docs/index.md` Available Parts table from registry data

**Updating a Part:**
1. Part pushes updated specs.json (new version, new language, status change)
2. Registrar validates and updates the registry entry
3. Publisher rebuilds the landing page

**Auditing:**
1. Auditor reads registry, visits each Part's repository URL
2. Checks for required files (specs.json, README, testcases/, LICENSE)
3. Reports stale entries, missing test cases, convention drift

## Rules

1. **Registrar owns registry/index.json** — no other agent writes to it.
2. **Publisher owns docs/index.md** — rebuilds from registry data, never hand-edits the Parts table.
3. **Auditor is read-only on Part repos** — reports findings, never modifies Part repositories.
4. **Registry is append-only** — entries are updated or marked deprecated, never deleted.
5. **Scribe always runs** after substantial work, always as `mode: "background"`. Never blocks.
