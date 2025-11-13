# PhysicsForge Documentation

Welcome to the PhysicsForge documentation directory. This directory contains comprehensive guides, references, and specifications for the project.

## Quick Links

- **[INDEX.md](INDEX.md)** - Complete documentation index with all available resources
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - Repository structure and organization
- **[INSTALLATION_REQUIREMENTS.md](INSTALLATION_REQUIREMENTS.md)** - Setup and installation guide
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Contribution guidelines

## Documentation Structure

### Core Documentation
Files in this directory provide essential project information:

- **Agent Integration**: Guides for AI agents (CLAUDE.md, COPILOT.md, AGENTS.md)
- **Setup & Installation**: Comprehensive environment setup (INSTALLATION_REQUIREMENTS.md)
- **Architecture**: Repository structure and data flow (ARCHITECTURE.md)
- **Contributing**: How to contribute effectively (CONTRIBUTING.md)
- **CI/CD**: Build and deployment pipelines (CI_CD_GUIDE.md)
- **GitHub**: Version control workflows (GITHUB_PUSH_INSTRUCTIONS.md)

### Research Frameworks
Documentation specific to physics and mathematics frameworks:

- **Superforce Framework**: README_SUPERFORCE.md, SUPERFORCE_README.md
- **Integration Status**: INTEGRATION_COMPLETE.md

### Technical References
JSON schemas and technical specifications:

- **metrics.schema.json**: Extraction metrics specification
- **plan.schema.json**: Extraction plan specification

### Release Information
Version history and release notes:

- **RELEASE_NOTES_v1.0.md**: Version 1.0 release documentation

## Navigation

### For New Users
1. Start with the main [README.md](../README.md) in the repository root
2. Follow [INSTALLATION_REQUIREMENTS.md](INSTALLATION_REQUIREMENTS.md) to set up your environment
3. Read [ARCHITECTURE.md](ARCHITECTURE.md) to understand the structure
4. Review [CONTRIBUTING.md](CONTRIBUTING.md) before making changes

### For AI Agents
- **Gemini**: See [../GEMINI.md](../GEMINI.md) (root level)
- **Claude**: See [CLAUDE.md](CLAUDE.md)
- **GitHub Copilot**: See [COPILOT.md](COPILOT.md)
- **All Agents**: Follow [AGENTS.md](AGENTS.md) for universal guidelines

### For Developers
- [ARCHITECTURE.md](ARCHITECTURE.md) - System design and structure
- [CI_CD_GUIDE.md](CI_CD_GUIDE.md) - Build and test workflows
- [CONTRIBUTING.md](CONTRIBUTING.md) - Development practices
- [examples/](examples/) - Code examples and patterns

## Standards and Conventions

All documentation in this repository follows these standards:

### ASCII-Only Policy
- All documentation files use ASCII characters only
- LaTeX macros or ASCII transliterations for special characters
- Enforced by `make ascii_guard`
- Exceptions: data artifacts in `data/`, `extracted_data/`, `source_materials/`

### Markdown Format
- Level-one title at the beginning
- Clear section hierarchy
- Relative path cross-references
- Code blocks with language specification

### File Organization
- Core docs in `docs/` directory
- Agent-specific files clearly labeled
- Schemas in JSON format with validation
- Examples in `docs/examples/` subdirectory

## Updating Documentation

When adding or modifying documentation:

1. **Follow Standards**: Maintain ASCII-only policy and markdown conventions
2. **Update Index**: Add new documents to [INDEX.md](INDEX.md)
3. **Cross-Reference**: Update related documents with links
4. **Test**: Run `make ascii_guard` to validate
5. **Commit**: Use scoped commit messages (e.g., "docs: add new guide")

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## Finding Information

Use the [INDEX.md](INDEX.md) file to quickly locate documentation on specific topics:

- **Getting started**: Installation and setup guides
- **Building**: Make targets and build systems
- **Testing**: Test frameworks and validation
- **Contributing**: Development workflows
- **Frameworks**: Research-specific documentation
- **Technical**: Schemas and specifications

## Additional Resources

### Repository Root
- [../README.md](../README.md) - Project overview
- [../GEMINI.md](../GEMINI.md) - Gemini integration guide
- [../Makefile](../Makefile) - Build system (`make help` for commands)

### Scripts Directory
- [../scripts/](../scripts/) - Python automation tools
- Documentation within scripts using docstrings

### Archive
- [../archive/](../archive/) - Historical documentation and legacy materials
- See [../archive/README.md](../archive/README.md) for archive contents

## Help and Support

If you cannot find what you need:

1. Check [INDEX.md](INDEX.md) for complete documentation list
2. Review [ARCHITECTURE.md](ARCHITECTURE.md) for structural questions
3. Consult agent-specific guides for integration questions
4. Run `make help` for available build commands
5. See [CONTRIBUTING.md](CONTRIBUTING.md) for development workflows

## Contributing to These Docs

We welcome documentation improvements! To contribute:

1. Follow the standards outlined above
2. Update cross-references as needed
3. Test with `make ascii_guard`
4. Submit a pull request with clear description

Thank you for helping improve PhysicsForge documentation!
