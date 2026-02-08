# Creating a New Part

This guide walks you through the complete process of creating a new Part for the SpecWorks Factory.

## Overview

A **Part** is a software component that implements one or more public specifications. Creating a new Part involves 13 key steps.

## Quick Reference

| Step | Task | Required |
|------|------|----------|
| 1 | Choose Specification | ✅ |
| 2 | Plan Your Part | ✅ |
| 3 | Create Repository | ✅ |
| 4 | Create specs.json | ✅ |
| 5 | Write README.md | ✅ |
| 6 | Add Test Cases | ✅ |
| 7 | Implement Specification | ✅ |
| 8 | Add Tests | ✅ |
| 9 | Add CI/CD | ✅ |
| 10 | Publish Packages | ✅ |
| 11 | Register in xRegistry | ✅ |
| 12 | Add to Landing Page | ✅ |
| 13 | Documentation & GitHub Pages | ✅ |

[View detailed step-by-step guide →](#step-by-step-guide)

## Prerequisites

- ✅ Public specification (RFC, W3C, ISO, etc.)
- ✅ Git and GitHub access
- ✅ Development environment for target language
- ✅ Optional: AI coding assistant (GitHub Copilot, Claude)

## Step-by-Step Guide

### Step 1: Choose a Specification

Select a publicly available specification to implement.

**Good candidates:**
- IETF RFCs ([rfc-editor.org](https://www.rfc-editor.org/))
- W3C Standards ([w3.org/TR](https://www.w3.org/TR/))
- IANA Registries ([iana.org/protocols](https://www.iana.org/protocols))

**Requirements:**
- Must be publicly accessible
- Should have test vectors or examples
- Solves a specific problem space

**Examples:** RFC 6350 (vCard), RFC 6902 (JSON Patch), RFC 5545 (iCalendar)

### Step 2: Plan Your Part

**Name**: Use specification name (PascalCase: `vCard`, `JsonPatch`)  
**Language**: Start with one (.NET recommended), add more later  
**Scope**: Define which version and features to implement

### Step 3: Create Repository

Create a new **public** repository in the `spec-works` organization (must be public for GitHub Pages):

```bash
gh repo create spec-works/PartName --public --clone
cd PartName
```

**Standard structure:**

```
PartName/
├── README.md
├── specs.json
├── LICENSE (MIT)
├── docs/
│   ├── docfx.json
│   ├── index.md
│   ├── toc.yml
│   ├── filterConfig.yml
│   ├── .gitignore
│   ├── api/
│   │   └── index.md
│   └── images/
├── testcases/
│   ├── README.md
│   ├── *.md / *.json (positive test cases)
│   └── negative/
│       └── *.json
└── dotnet/ (or python/, rust/, etc.)
    ├── src/
    ├── tests/
    └── PartName.sln
```

**Required files from the start:**
- `LICENSE` — MIT license (copy from any existing Part)
- `README.md` — see Step 5
- `specs.json` — see Step 4

### Step 4: Create specs.json

Create a linkset descriptor:

```json
{
  "linkset": [
    {
      "href": "https://www.rfc-editor.org/rfc/rfcXXXX.html",
      "rel": "describedby",
      "title": "Specification Name"
    },
    {
      "href": "https://spec-works.github.io/registry/parts/partname/",
      "rel": "registry",
      "title": "Part registry entry"
    }
  ]
}
```

### Step 5: Write README.md

Include:
- Registry badge
- Brief description
- Specification links
- Installation instructions
- Usage examples
- Testing information

See [vCard README](https://github.com/spec-works/vCard) for example.

### Step 6: Add Test Cases

Create shared, language-independent test cases:

```
testcases/
├── valid/
│   ├── example1.txt    # From spec
│   └── real-world-1.txt
└── invalid/
    └── malformed-1.txt
```

Extract examples directly from the specification.

### Step 7: Implement the Specification

**With AI assistance:**
- Provide specification text as context
- Reference test cases
- Use test-driven development

**Manual implementation:**
- Read specification thoroughly
- Follow SpecWorks [conventions](../specification/conventions.md)
- Use namespace: `SpecWorks.PartName`
- Keep dependencies minimal

### Step 8: Add Tests

**Test all MUST requirements** from specification

Example (.NET):

```csharp
[Theory]
[FilesData("../../../../testcases/valid/*.txt")]
public void ParseValid_Succeeds(string file)
{
    var result = Parser.Parse(File.ReadAllText(file));
    Assert.NotNull(result);
}
```

**Coverage goals:**
- All specification examples
- Edge cases
- Error conditions

### Step 9: Add CI/CD

Create **two** workflows in `.github/workflows/`:

**`.github/workflows/dotnet-test.yml`** — runs tests on push/PR:

```yaml
name: .NET Test
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-dotnet@v4
      - run: dotnet test dotnet/
```

**`.github/workflows/docs.yml`** — builds and deploys DocFX documentation to GitHub Pages:

```yaml
name: Deploy Documentation

on:
  push:
    branches: [main]
    paths:
      - 'docs/**'
      - 'dotnet/src/**'
      - '.github/workflows/docs.yml'
  workflow_dispatch:

permissions:
  contents: write

jobs:
  build-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Download shared template
        run: |
          curl -L -o template.zip https://github.com/spec-works/spec-works.github.io/archive/refs/heads/main.zip
          unzip -q template.zip
          mkdir -p docs/template
          cp -r spec-works.github.io-main/docs/template/* docs/template/
          rm -rf spec-works.github.io-main template.zip

      - name: Setup .NET
        uses: actions/setup-dotnet@v4
        with:
          dotnet-version: '10.0.x'

      - name: Restore dependencies
        run: dotnet restore dotnet/PartName.sln

      - name: Install DocFX
        run: dotnet tool install -g docfx

      - name: Build documentation
        run: docfx docs/docfx.json

      - name: Deploy to gh-pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: docs/_site
          force_orphan: true
```

> **Important:** The `dotnet restore` step is required so DocFX can resolve project dependencies when extracting API metadata.

Add status badge to README.

### Step 10: Publish Packages

**.NET:**
```bash
dotnet pack -c Release
dotnet nuget push *.nupkg
```

**Python:**
```bash
python -m build
twine upload dist/*
```

Update `specs.json` with package links.

### Step 11: Register in xRegistry

Add your Part to the registry in the [spec-works.github.io](https://github.com/spec-works/spec-works.github.io) repository:

1. **Create registry entry** at `registry/parts/partname/`:
   - `index.json` — Part metadata (id, name, description, version info)
   - `versions/1.0.0/part.json` — Linkset with specification references

2. **Update `registry/parts/index.json`** — add your Part entry and increment the `count`

Use an existing Part (e.g., `registry/parts/markmydeck/`) as a template.

Verify:
```bash
curl https://spec-works.github.io/registry/parts/partname/ | jq .
```

### Step 12: Add to Landing Page

Update the [spec-works.github.io](https://github.com/spec-works/spec-works.github.io) documentation to include your new Part:

1. **`docs/index.md`** — Add row to the "Available Parts" table and entry to the "Find Parts By Problem Space" list

### Step 13: Documentation & GitHub Pages

Documentation is required for all Parts. Set up DocFX and GitHub Pages:

**1. Create `docs/` folder** with these files (copy from an existing Part and adapt):

| File | Purpose |
|------|---------|
| `docfx.json` | DocFX configuration — update project references and metadata |
| `index.md` | Documentation home page — features, installation, usage examples |
| `toc.yml` | Navigation bar — links to home, API reference, GitHub |
| `filterConfig.yml` | API filter — excludes System/Microsoft types |
| `.gitignore` | Excludes build outputs (`_site/`, `obj/`, `api/*.yml`, `api/.manifest`) |
| `api/index.md` | API reference landing page — list of namespaces with descriptions |
| `images/` | Directory for documentation images (logo, screenshots) |

> **Important:** The `docs/.gitignore` must exclude generated files (`api/*.yml`, `api/.manifest`) but **must track `api/index.md`** — this is the landing page for `/api/`. Without it, the API Reference link returns a 404.

**2. Trigger the docs workflow** to create the `gh-pages` branch:

```bash
gh workflow run docs.yml --repo spec-works/PartName
gh run watch  # wait for completion
```

**3. Enable GitHub Pages** on the repository:

```bash
gh api repos/spec-works/PartName/pages -X POST \
  -f "source[branch]=gh-pages" -f "source[path]=/"
```

**4. Verify** the documentation site is live:

```bash
curl -s -o /dev/null -w "%{http_code}" https://spec-works.github.io/PartName/
# Should return 200

curl -s -o /dev/null -w "%{http_code}" https://spec-works.github.io/PartName/api/
# Should return 200 (API reference index page)
```

## Checklist

**Repository Setup**
- [ ] Public repository created
- [ ] Standard directory structure
- [ ] MIT License file
- [ ] .gitignore

**Documentation**
- [ ] README.md with badge, description, installation, usage
- [ ] specs.json (linkset descriptor)
- [ ] `docs/` folder with DocFX configuration
- [ ] `docs/api/index.md` (API reference landing page)
- [ ] `docs/index.md` (documentation home page)

**Implementation**
- [ ] Test case data files added (`testcases/`)
- [ ] Core functionality implemented
- [ ] Unit tests
- [ ] Integration tests (data-driven from test cases)
- [ ] All tests passing

**CI/CD & Deployment**
- [ ] `dotnet-test.yml` workflow (tests on push/PR)
- [ ] `docs.yml` workflow (DocFX build and deploy to gh-pages)
- [ ] GitHub Pages enabled (source: `gh-pages` branch)
- [ ] Documentation site live and API reference accessible
- [ ] Package published (NuGet, PyPI, etc.)

**Registration**
- [ ] xRegistry entry added (`registry/parts/partname/`)
- [ ] `registry/parts/index.json` updated (entry + count)
- [ ] Landing page updated (`docs/index.md` — Available Parts table + problem space)

## Examples

Study existing Parts:
- [vCard](https://github.com/spec-works/vCard) - Multi-language (RFC 6350)
- [JsonDiff](https://github.com/spec-works/JsonDiff) - .NET (RFC 6902)
- [iCalendar](https://github.com/spec-works/iCalendar) - .NET (RFC 5545)

## AI-Assisted Development

SpecWorks works great with AI coding assistants:

**GitHub Copilot:**
- Use specification as context
- Reference test cases in prompts

**Claude:**
- Share specification document
- Provide test cases as examples

**Best practices:**
- Validate AI output against specification
- Run comprehensive tests
- Review for security and maintainability

## Getting Help

- **Questions**: [GitHub Discussions](https://github.com/orgs/spec-works/discussions)
- **Issues**: [Specification repo](https://github.com/spec-works/specification/issues)
- **Examples**: Review existing Parts

---

Welcome to the SpecWorks Factory! 🏭
