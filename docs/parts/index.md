# Parts Catalog

Browse all available SpecWorks components. Each Part implements one or more public specifications to solve a specific problem space.

## Active Parts

### vCard - Contact Information Representation

**Specification**: [RFC 6350 - vCard Format Specification](https://www.rfc-editor.org/rfc/rfc6350)

Parse, validate, and serialize vCard (electronic business card) data.

**Available Implementations**:
- **.NET**: [SpecWorks.vCard](https://www.nuget.org/packages/VCard.Net) on NuGet
- **Python**: [vcard](https://pypi.org/project/vcard/) on PyPI
- **Rust**: [vcard](https://crates.io/crates/vcard) on crates.io

**Documentation**: [https://spec-works.github.io/vCard/](https://spec-works.github.io/vCard/)

**Repository**: [github.com/spec-works/vCard](https://github.com/spec-works/vCard)

---

### JsonDiff - JSON Patch Generator

**Specification**: [RFC 6902 - JavaScript Object Notation (JSON) Patch](https://www.rfc-editor.org/rfc/rfc6902)

Generate JSON Patch documents by comparing two JSON objects.

**Available Implementations**:
- **.NET**: [SpecWorks.JsonDiff](https://www.nuget.org/packages/SpecWorks.JsonDiff) on NuGet
- **CLI Tool**: [SpecWorks.JsonDiff.Cli](https://www.nuget.org/packages/SpecWorks.JsonDiff.Cli) on NuGet

**Documentation**: [https://spec-works.github.io/JsonDiff/](https://spec-works.github.io/JsonDiff/)

**Repository**: [github.com/spec-works/JsonDiff](https://github.com/spec-works/JsonDiff)

---

### iCalendar - Calendar Data Parser

**Specification**: [RFC 5545 - Internet Calendaring and Scheduling Core Object Specification (iCalendar)](https://www.rfc-editor.org/rfc/rfc5545)

Parse, validate, and serialize iCalendar data for events, to-dos, and calendar information.

**Available Implementations**:
- **.NET**: [ICalendar.Net](https://www.nuget.org/packages/ICalendar.Net) on NuGet

**Documentation**: [https://spec-works.github.io/iCalendar/](https://spec-works.github.io/iCalendar/)

**Repository**: [github.com/spec-works/iCalendar](https://github.com/spec-works/iCalendar)

---

### RateLimiter - HTTP Rate Limit Client

**Specification**: [draft-ietf-httpapi-ratelimit-headers - RateLimit header fields for HTTP](https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/)

Client-side rate limiting based on standardized HTTP RateLimit headers.

**Available Implementations**:
- **.NET**: [RateLimitClient](https://www.nuget.org/packages/RateLimitClient) on NuGet

**Documentation**: [https://spec-works.github.io/RateLimiter/](https://spec-works.github.io/RateLimiter/)

**Repository**: [github.com/spec-works/RateLimiter](https://github.com/spec-works/RateLimiter)

---

### linkset - Linkset Document Parser

**Specification**:
- [RFC 9264 - Linkset: Media Types and a Link Relation Type for Link Sets](https://www.rfc-editor.org/rfc/rfc9264)
- [RFC 8288 - Web Linking](https://www.rfc-editor.org/rfc/rfc8288)

Parse and serialize linkset documents (`application/linkset+json`).

**Available Implementations**:
- **.NET**: [SpecWorks.Linkset](https://www.nuget.org/packages/SpecWorks.Linkset) on NuGet

**Documentation**: [https://spec-works.github.io/linkset/](https://spec-works.github.io/linkset/)

**Repository**: [github.com/spec-works/linkset](https://github.com/spec-works/linkset)

---

### MarkMyWord - Markdown ↔ Word Converter

**Specification**:
- [CommonMark 0.31.2](https://spec.commonmark.org/0.31.2/)
- [ECMA-376 - Office Open XML File Formats](https://www.ecma-international.org/publications-and-standards/standards/ecma-376/)

Bidirectional conversion between Markdown and Microsoft Word (.docx) documents.

**Available Implementations**:
- **.NET**: [SpecWorks.MarkMyWord](https://www.nuget.org/packages/SpecWorks.MarkMyWord) on NuGet
- **CLI Tool**: [SpecWorks.MarkMyWord.Cli](https://www.nuget.org/packages/SpecWorks.MarkMyWord.Cli) on NuGet

**Documentation**: [https://spec-works.github.io/MarkMyWord/](https://spec-works.github.io/MarkMyWord/)

**Repository**: [github.com/spec-works/MarkMyWord](https://github.com/spec-works/MarkMyWord)

---

## Finding the Right Part

### By Problem Space

- **Contact/Address Book Data** → vCard
- **Calendar/Event Data** → iCalendar
- **JSON Comparison/Diff** → JsonDiff
- **HTTP Rate Limiting** → RateLimiter
- **Web Linking/Link Relations** → linkset
- **Document Conversion (Markdown/Word)** → MarkMyWord

### By Specification

Use the table below to find Parts by their implementing specification:

| Specification | Part | Status |
|---------------|------|--------|
| RFC 6350 | [vCard](#vcard---contact-information-representation) | Active |
| RFC 5545 | [iCalendar](#icalendar---calendar-data-parser) | Active |
| RFC 6902 | [JsonDiff](#jsondiff---json-patch-generator) | Active |
| RFC 9264 | [linkset](#linkset---linkset-document-parser) | Active |
| RFC 8288 | [linkset](#linkset---linkset-document-parser) | Active |
| draft-ietf-httpapi-ratelimit-headers | [RateLimiter](#ratelimiter---http-rate-limit-client) | Active |
| CommonMark 0.31.2 | [MarkMyWord](#markMyword---markdown--word-converter) | Active |
| ECMA-376 | [MarkMyWord](#markMyword---markdown--word-converter) | Active |

### By Language

| Language | Available Parts |
|----------|----------------|
| **.NET** | All parts (vCard, JsonDiff, iCalendar, RateLimiter, linkset, MarkMyWord) |
| **Python** | vCard |
| **Rust** | vCard |

---

## Installation Examples

### .NET (NuGet)

```bash
# Library packages
dotnet add package SpecWorks.JsonDiff
dotnet add package SpecWorks.Linkset
dotnet add package VCard.Net
dotnet add package ICalendar.Net
dotnet add package RateLimitClient

# CLI tools (install globally)
dotnet tool install --global SpecWorks.JsonDiff.Cli
dotnet tool install --global SpecWorks.MarkMyWord.Cli
```

### Python (PyPI)

```bash
pip install vcard
```

### Rust (Cargo)

```toml
[dependencies]
vcard = "*"
```

---

## Quality Standards

All SpecWorks Parts meet these quality standards:

- ✅ **Comprehensive Testing** - Typically 20+ tests per implementation
- ✅ **Specification Compliance** - Documented mapping to specification sections
- ✅ **Real-World Validation** - Tested with actual payloads from specifications
- ✅ **CI/CD** - Automated testing and deployment
- ✅ **Documentation** - API reference and usage examples
- ✅ **Open Source** - MIT licensed

---

## Contributing

Each Part repository accepts contributions:

1. Find the Part repository on [GitHub](https://github.com/spec-works)
2. Review the Part's README and conventions
3. Open issues for bugs or feature requests
4. Submit pull requests with tests

See the [SpecWorks Conventions](../specification/conventions.md) for development standards.

---

## Creating New Parts

Interested in creating your own SpecWorks-compliant component? See:

- [Factory Specification](../specification/factory-spec.md) - Complete pattern specification
- [Conventions](../specification/conventions.md) - Development standards
- [Creating Your Own Factory](../specification/factory-spec.md#appendix-a-creating-your-own-factory) - Step-by-step guide
