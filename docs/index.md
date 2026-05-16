# SpecWorks Factory

## Welcome

The SpecWorks Factory uses AI tooling to materialize software components directly from their specifications. This is a specification-centric ecosystem where components are discovered by problem space, not programming language.

## What is SpecWorks?

SpecWorks is a **Factory pattern system** for creating, cataloging, and distributing software components that implement publicly available specifications. Components are:

- **Specification-Compliant** - Implement RFCs, W3C standards, ISO specifications, and other public standards
- **Multi-Language** - Available in .NET, Python, Rust, and other languages
- **Discoverable** - Find components by problem space, not language
- **Quality-Focused** - Comprehensive test suites demonstrate compliance
- **Open Source** - MIT licensed, hosted on GitHub

## Available Parts

| Part | Specification | Languages | Test Cases | Status |
|------|---------------|-----------|------------|--------|
| [vCard](https://spec-works.github.io/vCard/) | [RFC 6350](https://www.rfc-editor.org/rfc/rfc6350) - Contact Information | .NET, Python, Rust | [testcases/](https://github.com/spec-works/vCard/tree/main/testcases) | ✅ Active |
| [JsonDiff](https://spec-works.github.io/JsonDiff/) | [RFC 6902](https://www.rfc-editor.org/rfc/rfc6902) - JSON Patch | .NET | [TestCases/](https://github.com/spec-works/JsonDiff/tree/main/TestCases) | ✅ Active |
| [iCalendar](https://spec-works.github.io/iCalendar/) | [RFC 5545](https://www.rfc-editor.org/rfc/rfc5545) - Calendar Data | .NET | [testcases/](https://github.com/spec-works/iCalendar/tree/main/testcases) | ✅ Active |
| [RateLimiter](https://spec-works.github.io/RateLimiter/) | [IETF Draft](https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/) - HTTP Rate Limits | .NET | [testcases/](https://github.com/spec-works/RateLimiter/tree/main/testcases) | ✅ Active |
| [linkset](https://spec-works.github.io/linkset/) | [RFC 9264](https://www.rfc-editor.org/rfc/rfc9264) - Web Link Sets | .NET | [testcases/](https://github.com/spec-works/linkset/tree/main/testcases) | ✅ Active |
| [MarkMyWord](https://spec-works.github.io/MarkMyWord/) | CommonMark 0.31.2 + ECMA-376 - Markdown/Word Conversion | .NET | — | ✅ Active |
| [MarkMyDeck](https://spec-works.github.io/MarkMyDeck/) | CommonMark 0.31.2 + ECMA-376 - Markdown/PowerPoint Conversion | .NET | [testcases/](https://github.com/spec-works/MarkMyDeck/tree/main/testcases) | ✅ Active |
| [Message](https://spec-works.github.io/message/) | [RFC 5322](https://www.rfc-editor.org/rfc/rfc5322) + [MIME](https://www.rfc-editor.org/rfc/rfc2045) - Email Messages | .NET | [testcases/](https://github.com/spec-works/message/tree/main/testcases) | ✅ Active |
| [Sidemark](https://spec-works.github.io/Sidemark/) | [MRSF v1.0](https://sidemark.org/specification.html) - Markdown Review Sidecar Format | .NET | [testcases/](https://github.com/spec-works/Sidemark/tree/main/testcases) | ✅ Active |
| [OfficeTalk](https://spec-works.github.io/OfficeTalk/) | [OfficeTalk/1.0](https://github.com/spec-works/OfficeTalk/blob/main/officetalk-spec.md) - Deterministic Office Document Operations | .NET | [testcases/](https://github.com/spec-works/OfficeTalk/tree/main/testcases) | ✅ Active |
| [OfficeTalkEngine](https://spec-works.github.io/OfficeTalkEngine/) | [OfficeTalk/1.0](https://github.com/spec-works/OfficeTalk/blob/main/officetalk-spec.md) - Execution Engine + CLI | .NET | [testcases/](https://github.com/spec-works/OfficeTalkEngine/tree/main/testcases) | ✅ Active |
| [A2A-Ask](https://spec-works.github.io/A2A-Ask/) | [A2A Protocol](https://a2a-protocol.org/latest/specification/) - Agent-to-Agent Communication CLI | .NET | — | ✅ Active |
| [AI Catalog](https://spec-works.github.io/ai-catalog/) | [AI Card](https://agent-card.github.io/ai-card/) - AI Artifact Catalog Format | .NET, Python | [testcases/](https://github.com/spec-works/ai-catalog/tree/main/testcases) | ✅ Active |

[Explore the full xRegistry catalog →](https://spec-works.github.io/registry/)

## Find Parts By Problem Space

- **Contact/Address Book Data** → [vCard](https://spec-works.github.io/vCard/)
- **Calendar/Event Data** → [iCalendar](https://spec-works.github.io/iCalendar/)
- **JSON Comparison/Diff** → [JsonDiff](https://spec-works.github.io/JsonDiff/)
- **HTTP Rate Limiting** → [RateLimiter](https://spec-works.github.io/RateLimiter/)
- **Web Linking/Link Relations** → [linkset](https://spec-works.github.io/linkset/)
- **Document Conversion (Markdown/Word)** → [MarkMyWord](https://spec-works.github.io/MarkMyWord/)
- **Presentation Generation (Markdown/PowerPoint)** → [MarkMyDeck](https://spec-works.github.io/MarkMyDeck/)
- **Email/Internet Messages** → [Message](https://spec-works.github.io/message/)
- **Markdown Review Comments** → [Sidemark](https://spec-works.github.io/Sidemark/)
- **Office Document Operations (Word/Excel/PowerPoint)** → [OfficeTalk](https://spec-works.github.io/OfficeTalk/) + [OfficeTalkEngine](https://spec-works.github.io/OfficeTalkEngine/)
- **Agent-to-Agent Communication (A2A Protocol)** → [A2A-Ask](https://spec-works.github.io/A2A-Ask/)
- **AI Artifact Catalogs** → [AI Catalog](https://spec-works.github.io/ai-catalog/)

## Quick Start

### AI Agent Skills & Plugins

SpecWorks provides **AI agent skills** that teach coding assistants (GitHub Copilot CLI, Claude Code, VS Code Copilot, Cursor) how to use SpecWorks tools. Install from the [SpecWorks Plugins Repository](https://github.com/spec-works/plugins):

| Plugin | Type | Description | Install |
|--------|------|-------------|---------|
| [a2a-ask](https://github.com/spec-works/plugins/tree/main/plugins/a2a-ask) | Skill | Interact with remote A2A protocol agents | `dotnet tool install --global SpecWorks.A2A-Ask` |
| [markmyword](https://github.com/spec-works/plugins/tree/main/plugins/markmyword) | Skill | Markdown ↔ Word (.docx) conversion | `dotnet tool install --global SpecWorks.MarkMyWord.CLI` |
| [markmydeck](https://github.com/spec-works/plugins/tree/main/plugins/markmydeck) | Skill | Markdown → PowerPoint (.pptx) conversion | `dotnet tool install --global SpecWorks.MarkMyDeck.CLI` |
| [officetalk](https://github.com/spec-works/plugins/tree/main/plugins/officetalk) | Skill | Deterministic Office document operations | `dotnet tool install --global SpecWorks.OfficeTalkEngine.CLI` |
| [xregistry-mcp](https://github.com/spec-works/plugins/tree/main/plugins/xregistry-mcp) | MCP Server | xRegistry specification discovery | See [README](https://github.com/spec-works/xRegistry-MCP-Server) |

**To install a skill** into your AI coding assistant, copy the SKILL.md from the plugin folder into your skills directory:

```bash
# GitHub Copilot CLI (personal)
mkdir -p ~/.copilot/skills/<plugin-name>
cp SKILL.md ~/.copilot/skills/<plugin-name>/SKILL.md

# Claude Code (personal)
mkdir -p ~/.claude/skills/<plugin-name>
cp SKILL.md ~/.claude/skills/<plugin-name>/SKILL.md
```

[Browse all plugins →](https://github.com/spec-works/plugins)

### Finding a Component

Browse the [Available Parts](#available-parts) table above, or search the [xRegistry catalog](https://spec-works.github.io/registry/) to find components by specification or problem space:

- Need to parse contact information? → **vCard** (RFC 6350)
- Need JSON Patch operations? → **JsonDiff** (RFC 6902)
- Need calendar/event parsing? → **iCalendar** (RFC 5545)
- Need email message parsing? → **Message** (RFC 5322 + MIME)
- Need Markdown review comments? → **Sidemark** (MRSF v1.0)

### Installing a Component

Each Part provides packages for standard package managers:

**.NET (NuGet):**
```bash
dotnet add package SpecWorks.JsonDiff
```

**Python (PyPI):**
```bash
pip install vcard
```

**Rust (crates.io):**
```toml
[dependencies]
vcard = "*"
```

### Using a Component

Each Part includes comprehensive documentation with examples:

```csharp
// Example: Using JsonDiff (.NET)
using SpecWorks.JsonDiff;

var original = JsonDocument.Parse("{\"name\":\"John\"}");
var modified = JsonDocument.Parse("{\"name\":\"Jane\"}");
var patch = JsonDiffer.Diff(original, modified);
```

## Documentation

- [Factory Specification](specification/factory-spec.md) - Complete specification for the SpecWorks Factory pattern
- [Conventions](specification/conventions.md) - Standards and patterns used across all components
- [Architecture Decision Records](specification/adr/index.md) - Design decisions and rationale

## Contributing

- **[Creating a New Part](contributing/create-part.md)** - Step-by-step guide to adding a new component to the factory
- [Creating Your Own Factory](specification/factory-spec.md#appendix-a-creating-your-own-factory) - Build your own specification factory

## Goals

- Operationalize the theory of an AI-powered software factory
- Provide a place to learn and improve AI-assisted developer tooling
- Produce high-quality software components that conform to publicly available specifications
- Demonstrate the viability of LLM-generated software components

## Why SpecWorks?

### Specification-Centric Discovery

Traditional package search:
> "I need a JSON library for .NET"

SpecWorks approach:
> "I need to implement RFC 6902 (JSON Patch)"

Find solutions by **problem space** and **specification**, not by programming language.

### Multi-Language Implementations

A single Part (like vCard) can have implementations in multiple languages, all implementing the same specification. Choose the language that fits your stack.

### Quality and Compliance

Every component includes:
- ✅ Comprehensive test suites (typically 20+ tests)
- ✅ Specification compliance documentation
- ✅ Real-world payload examples
- ✅ CI/CD automated testing

### Open and Reproducible

The SpecWorks Factory pattern is:
- 📖 **Fully documented** - Complete specification available
- 🔓 **Open source** - All code MIT licensed
- 🔄 **Reproducible** - Create your own factory following the pattern
- 🤖 **AI-friendly** - Designed for AI-assisted development

## Repository Organization

The SpecWorks organization uses a **multi-repository pattern**:

- Each Part has its own repository (e.g., `github.com/spec-works/vCard`)
- Factory specifications and conventions in the `specification` repository
- Shared workflows and documentation in `.github` repository

This enables:
- Parallel AI-agent operations on different Parts
- Independent version control and release cycles
- Specification-centric organization

## Community

- **GitHub Organization**: [github.com/spec-works](https://github.com/spec-works)
- **Contributing**: [Create a new Part](contributing/create-part.md) or improve existing ones
- **Issues and Discussions**: Use each Part's repository for specific issues
- **Factory Specification**: [specification repository](https://github.com/spec-works/specification)

## License

All SpecWorks components are licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

Ready to explore? [Browse the xRegistry catalog →](https://spec-works.github.io/registry/)
