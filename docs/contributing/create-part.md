# Creating a New Part

This guide walks you through the complete process of creating a new Part for the SpecWorks Factory.

## Overview

A **Part** is a software component that implements one or more public specifications. Creating a new Part involves 12 key steps.

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
| 12 | Documentation | Optional |

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

Create a new repository in the `spec-works` organization:

```bash
git clone https://github.com/spec-works/PartName.git
cd PartName
```

**Standard structure:**

```
PartName/
├── README.md
├── specs.json
├── LICENSE (MIT)
├── testcases/
│   ├── valid/
│   └── invalid/
└── dotnet/ (or python/, rust/, etc.)
    ├── src/
    ├── tests/
    └── PartName.sln
```

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

Create `.github/workflows/dotnet-test.yml`:

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

Registry updates automatically weekly, or trigger manually:

```bash
gh workflow run update-registry.yml
```

Verify:
```bash
curl https://spec-works.github.io/registry/parts/partname/ | jq .
```

### Step 12: Documentation (Optional)

Add DocFX documentation and deploy to GitHub Pages.

## Checklist

**Repository Setup**
- [ ] Repository created
- [ ] Standard structure
- [ ] MIT License
- [ ] .gitignore

**Documentation**
- [ ] README.md
- [ ] specs.json
- [ ] Registry badge

**Implementation**
- [ ] Test cases added
- [ ] Core functionality
- [ ] Unit tests
- [ ] All tests passing

**Publishing**
- [ ] CI/CD workflow
- [ ] Package published
- [ ] Registry updated

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
