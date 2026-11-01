# SpecWorks Factory Documentation

This repository contains the landing site and documentation for the SpecWorks Factory.

## Site URL

https://spec-works.github.io/

## Contents

- **Landing Page** - Overview of SpecWorks Factory and Parts catalog
- **Factory Specification** - Complete specification for the SpecWorks Factory pattern
- **Conventions** - Standards and patterns used across all components
- **Architecture Decision Records** - Design decisions and rationale

## Building Locally

### Prerequisites

- [.NET SDK 10.0](https://dotnet.microsoft.com/download)
- [DocFX](https://dotnet.github.io/docfx/)

### Build Steps

1. Install DocFX:
   ```bash
   dotnet tool install -g docfx
   ```

2. Build the documentation:
   ```bash
   docfx docs/docfx.json
   ```

3. Serve locally:
   ```bash
   docfx docs/docfx.json --serve
   ```

4. Open browser to `http://localhost:8080`

## Deployment

Documentation is automatically built and deployed to GitHub Pages when changes are pushed to the `main` branch.

The GitHub Actions workflow:
1. Installs DocFX
2. Builds the documentation site
3. Generates the AI Catalog from the `spec-works/plugins` marketplace
4. Publishes plugin files under `.well-known/plugins/` and resolves skill entries to
   their `SKILL.md` documents using absolute HTTPS URLs
5. Deploys to GitHub Pages

`scripts/publish_catalog.py` normalizes catalog entry types and checks every
declared skill exists before publishing. Missing artifacts fail the build instead
of producing a catalog containing broken directory URLs. Hidden plugin files such
as `.mcp.json` are copied along with skill content.

Run the publisher regression checks with:

```bash
python -m unittest discover -s scripts -p "test_*.py"
```

## Contributing

To contribute to the documentation:

1. Fork this repository
2. Make your changes in the `docs/` directory
3. Test locally using DocFX
4. Submit a pull request

## Structure

```
spec-works.github.io/
├── docs/
│   ├── docfx.json              # DocFX configuration
│   ├── index.md                # Landing page
│   ├── toc.yml                 # Main table of contents
│   ├── parts/
│   │   └── index.md            # Parts catalog
│   └── specification/
│       ├── factory-spec.md     # Factory specification
│       ├── conventions.md      # Conventions
│       ├── adr/
│       │   └── index.md        # ADR index
│       └── toc.yml
├── .github/
│   └── workflows/
│       └── docs.yml            # GitHub Actions workflow
└── README.md
```

## License

This documentation is licensed under the [MIT License](LICENSE).

## Links

- **GitHub Organization**: [github.com/spec-works](https://github.com/spec-works)
- **Specification Repository**: [github.com/spec-works/specification](https://github.com/spec-works/specification)
- **Documentation Site**: [spec-works.github.io](https://spec-works.github.io)
