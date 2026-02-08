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

| Part | Specification | Languages | Status |
|------|---------------|-----------|--------|
| [vCard](https://spec-works.github.io/vCard/) | [RFC 6350](https://www.rfc-editor.org/rfc/rfc6350) - Contact Information | .NET, Python, Rust | ✅ Active |
| [JsonDiff](https://spec-works.github.io/JsonDiff/) | [RFC 6902](https://www.rfc-editor.org/rfc/rfc6902) - JSON Patch | .NET | ✅ Active |
| [iCalendar](https://spec-works.github.io/iCalendar/) | [RFC 5545](https://www.rfc-editor.org/rfc/rfc5545) - Calendar Data | .NET | ✅ Active |
| [RateLimiter](https://spec-works.github.io/RateLimiter/) | [IETF Draft](https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/) - HTTP Rate Limits | .NET | ✅ Active |
| [linkset](https://spec-works.github.io/linkset/) | [RFC 9264](https://www.rfc-editor.org/rfc/rfc9264) - Web Link Sets | .NET | ✅ Active |
| [MarkMyWord](https://spec-works.github.io/MarkMyWord/) | CommonMark 0.31.2 + ECMA-376 - Markdown/Word Conversion | .NET | ✅ Active |
| [MarkMyDeck](https://spec-works.github.io/MarkMyDeck/) | CommonMark 0.31.2 + ECMA-376 - Markdown/PowerPoint Conversion | .NET | ✅ Active |
| [Message](https://spec-works.github.io/message/) | [RFC 5322](https://www.rfc-editor.org/rfc/rfc5322) + [MIME](https://www.rfc-editor.org/rfc/rfc2045) - Email Messages | .NET | ✅ Active |

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

## Quick Start

### Finding a Component

Browse the [Available Parts](#available-parts) table above, or search the [xRegistry catalog](https://spec-works.github.io/registry/) to find components by specification or problem space:

- Need to parse contact information? → **vCard** (RFC 6350)
- Need JSON Patch operations? → **JsonDiff** (RFC 6902)
- Need calendar/event parsing? → **iCalendar** (RFC 5545)
- Need email message parsing? → **Message** (RFC 5322 + MIME)

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
