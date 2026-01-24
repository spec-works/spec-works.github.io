# Architecture Decision Records

Architecture Decision Records (ADRs) document important architectural and design decisions made in the SpecWorks Factory.

## Organization-Level ADRs

ADRs at the organization level affect all Parts and define factory-wide standards.

For organization-level ADRs, see the [specification repository](https://github.com/spec-works/specification/tree/main/adr).

## Part-Level ADRs

Each Part repository contains its own ADRs documenting project-specific decisions:

- **[vCard ADRs](https://github.com/spec-works/vCard/tree/main/adr)** - Multi-language implementation decisions
- **[JsonDiff ADRs](https://github.com/spec-works/JsonDiff/tree/main/adr)** - JSON Patch generation approaches
- **[iCalendar ADRs](https://github.com/spec-works/iCalendar/tree/main/adr)** - Calendar parsing decisions
- **[RateLimiter ADRs](https://github.com/spec-works/RateLimiter/tree/main/adr)** - Rate limiting strategies
- **[linkset ADRs](https://github.com/spec-works/linkset/tree/main/adr)** - Linkset parsing decisions
- **[MarkMyWord ADRs](https://github.com/spec-works/MarkMyWord/tree/main/adr)** - Document conversion approaches

## ADR Format

All ADRs follow a standard format:

```markdown
# ADR NNNN: <Title>

## Status
Accepted | Proposed | Deprecated | Superseded

## Context
<Problem description, background, constraints>

## Decision
<The decision made>

## Consequences

### Positive
- Benefit 1
- Benefit 2

### Negative
- Trade-off 1
- Trade-off 2

### Mitigation
- How to address negative consequences

## References
- [RFC XXXX](url)
- [Related ADR](url)

## Date
YYYY-MM-DD
```

## Creating ADRs

### When to Create an ADR

**Organization-level** (in specification repository):
- Framework/language version policies
- Organization-wide patterns
- Naming conventions
- Cross-project architectural choices

**Part-level** (in Part repositories):
- API design choices
- Specification version support
- Implementation trade-offs
- Library dependencies
- Feature inclusion/exclusion

### ADR Numbering

- Four digits with leading zeros: `0001`, `0002`, etc.
- Sequential within repository
- Never reuse numbers

## Common ADR Topics

- Specification version support decisions
- API design patterns and rationale
- Type safety vs. flexibility trade-offs
- Performance vs. specification purity
- Migration paths for breaking changes
- Multi-language implementation strategies
- Testing approach and coverage goals

## Questions?

For questions about ADRs:
- Review the [Conventions](../conventions.md#architecture-decision-records) for detailed guidelines
- Open an issue in the relevant repository
- Propose new ADRs via pull request using the standard format
