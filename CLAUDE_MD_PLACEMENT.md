# CLAUDE.md File Placement Guide

**Date:** November 7, 2025
**Purpose:** Document all CLAUDE.md files in the PhysicsForge repository

## Overview

The PhysicsForge repository uses a hierarchical CLAUDE.md system:
- **Root CLAUDE.md** - Project-wide guidelines and build workflow
- **Directory CLAUDE.md files** - Context-specific guidance for each major area

## File Locations

### 1. Project Root
**Path:** `/home/eirikr/Playground/PhysicsForge/CLAUDE.md`
**Size:** 609 lines
**Purpose:** Master guidance document

**Contents:**
- ⚠️ **CRITICAL: MANDATORY BUILD WORKFLOW** (top section)
- Project overview and structure
- Build commands and workflows
- LaTeX compilation instructions
- Python catalog pipeline
- Repository audits
- Common tasks and troubleshooting

**Key Emphasis:**
- **ALWAYS operate from project root:** `/home/eirikr/Playground/PhysicsForge`
- **ALL builds use:** `make latex`
- **Applies to:** Manual commands, agent tasks, all operations

### 2. LaTeX Source Directory
**Path:** `/home/eirikr/Playground/PhysicsForge/synthesis/CLAUDE.md`
**Created:** November 7, 2025
**Purpose:** LaTeX document workspace guidance

**Contents:**
- Directory structure (chapters, modules, parts, etc.)
- Key files (main.tex, preamble.tex, bibliography.bib)
- Working with chapters and equation modules
- Package management
- Equation tagging system
- Troubleshooting LaTeX errors
- Build output locations

**Key Emphasis:**
- **NEVER build from synthesis/** - Always return to project root
- **Use `\input{}`** not `\include{}` for equation modules
- **One equation per file** in modules/equations/
- **UTF-8 encoding** for all .tex files

### 3. Python Utilities Directory
**Path:** `/home/eirikr/Playground/PhysicsForge/scripts/CLAUDE.md`
**Created:** November 7, 2025
**Purpose:** Root-level Python scripts guidance

**Contents:**
- Script inventory (extraction, catalog, audit)
- Common usage patterns
- Command-line conventions
- Python environment requirements
- Makefile integration
- Script creation templates
- Troubleshooting

**Key Emphasis:**
- **Always run from project root:** `python scripts/[name].py --base-dir .`
- **Standard library only** - No external dependencies
- **Proper exit codes** - 0 = success
- **pathlib.Path** for cross-platform compatibility

### 4. Build Scripts Directory
**Path:** `/home/eirikr/Playground/PhysicsForge/synthesis/scripts/CLAUDE.md`
**Created:** November 7, 2025
**Purpose:** LaTeX build automation guidance

**Contents:**
- Build script descriptions (compile.sh)
- Why Makefile orchestration is required
- Build workflow explanation
- Modifying build scripts
- Available build targets
- Script structure best practices
- Integration with Makefile

**Key Emphasis:**
- **NEVER call compile.sh directly** - Use `make latex`
- **Makefile is single source of truth** for builds
- **Scripts change directories internally** - Don't assume location
- **Logs go to project root** logs/ directory

### 5. Reusable Components Directory
**Path:** `/home/eirikr/Playground/PhysicsForge/synthesis/modules/CLAUDE.md`
**Created:** November 7, 2025
**Purpose:** LaTeX modules (equations, figures, tables) guidance

**Contents:**
- Module types (equations, figures, tables, derivations, etc.)
- Standard formats for each module type
- Creating new modules
- Module best practices
- Naming conventions
- Integration with catalog system
- Troubleshooting module issues

**Key Emphasis:**
- **One equation per file** - No exceptions
- **Full provenance** - Document source + line numbers
- **Unique labels** - Follow naming patterns
- **Framework attribution** - Use `\eqtag{F}{D}{S}`
- **Test standalone** - Modules should work in isolation

## Hierarchy and Inheritance

```
Project Root CLAUDE.md (master guidelines)
├── synthesis/CLAUDE.md (LaTeX workspace)
│   ├── synthesis/scripts/CLAUDE.md (build automation)
│   └── synthesis/modules/CLAUDE.md (reusable components)
└── scripts/CLAUDE.md (Python utilities)
```

## Common Themes Across All Files

### 1. Build Workflow Mandate
**Every CLAUDE.md emphasizes:**
- Always work from project root: `/home/eirikr/Playground/PhysicsForge`
- Use Makefile for all builds: `make latex`, `make clean`, `make ci`
- Never execute scripts directly from subdirectories

### 2. Path Conventions
- **Absolute paths** from project root
- **pathlib.Path** for Python scripts
- **Never assume working directory**

### 3. Testing Requirements
- **Test from root** after any changes
- **Verify outputs** before committing
- **Check logs** for errors

## Usage by Claude Code Agents

### When to Consult Which CLAUDE.md

**Working on LaTeX source?**
1. Read `/home/eirikr/Playground/PhysicsForge/CLAUDE.md` (workflow)
2. Read `/home/eirikr/Playground/PhysicsForge/synthesis/CLAUDE.md` (specifics)

**Creating/modifying equation modules?**
1. Read `/home/eirikr/Playground/PhysicsForge/CLAUDE.md` (workflow)
2. Read `/home/eirikr/Playground/PhysicsForge/synthesis/modules/CLAUDE.md` (module format)

**Working on Python utilities?**
1. Read `/home/eirikr/Playground/PhysicsForge/CLAUDE.md` (workflow)
2. Read `/home/eirikr/Playground/PhysicsForge/scripts/CLAUDE.md` (script conventions)

**Modifying build process?**
1. Read `/home/eirikr/Playground/PhysicsForge/CLAUDE.md` (workflow)
2. Read `/home/eirikr/Playground/PhysicsForge/synthesis/scripts/CLAUDE.md` (build details)

### Agent Deployment Checklist

Before deploying any agent:
- [ ] Agent knows project root: `/home/eirikr/Playground/PhysicsForge`
- [ ] Agent will use `make latex` not direct script calls
- [ ] Agent understands directory context
- [ ] Agent has read appropriate CLAUDE.md file(s)

## Maintenance

### Updating CLAUDE.md Files

When project structure changes:
1. Update root CLAUDE.md first (master)
2. Update affected directory CLAUDE.md files
3. Ensure consistency across all files
4. Update this placement guide

### Adding New CLAUDE.md Files

For new major directories:
1. Create CLAUDE.md in that directory
2. Follow established format and emphasis
3. Add entry to this placement guide
4. Update root CLAUDE.md to reference it

## Quick Reference

| Directory | CLAUDE.md Purpose | Key Mandate |
|-----------|-------------------|-------------|
| `/home/eirikr/Playground/PhysicsForge/` | Master guidelines | Use Makefile from root |
| `synthesis/` | LaTeX workspace | Never build from here |
| `synthesis/scripts/` | Build automation | Never call compile.sh directly |
| `synthesis/modules/` | Reusable components | One equation per file |
| `scripts/` | Python utilities | Always run from root |

## See Also

- **Root Makefile** - All available build targets
- **equation_catalog.csv** - Master equation catalog
- **LATEX_PACKAGE_ANALYSIS.md** - LaTeX package audit
- **UNICODE_FIX_COMPLETE.md** - Recent unicode fix report

---

**Last Updated:** November 7, 2025
**Status:** Complete - 5 CLAUDE.md files in place
