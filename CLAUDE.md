# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a theoretical physics and advanced mathematics research repository synthesizing unified field theories, quantum-gravitational models, and crystalline spacetime engineering. The work integrates:

- **Aether Framework**: Scalar field dynamics, zero-point energy (ZPE), quantum foam, time crystals
- **Genesis Framework**: Exceptional Lie groups (E8, E7, E6, F4, G2), Cayley-Dickson algebras, fractal geometries, modular symmetries
- **Pais Framework**: Gravitational-electromagnetic unification with scalar-ZPE interactions
- **Mathematical Foundations**: Non-associative algebras, hyperdimensional constructs (up to 2048D), Monster Group modular invariants

**Platform**: Cross-platform (Windows 11 / Linux CachyOS)
**Shell**: PowerShell (Windows) / Bash (Linux)
**LaTeX Distribution**: MiKTeX (Windows) / TeX Live (Linux recommended)
**Python**: 3.10+ (standard library only for current tools)

## Repository Structure

```
Math_Science/
|-- synthesis/                    # PRIMARY WORK AREA - LaTeX book project
|   |-- main.tex                  # Master file (book class, 5 parts, 30 chapters)
|   |-- preamble.tex              # Packages, macros, equation tags (262 lines)
|   |-- bibliography.bib          # BibTeX references (210 entries)
|   |-- chapters/                 # 30 chapters organized by part
|   |   |-- foundations/          # Ch01-06 (Phase 1 - COMPLETE)
|   |   |-- frameworks/           # Ch07-16 (Aether + Genesis + Pais)
|   |   |-- unification/          # Ch17-21 (Framework synthesis)
|   |   |-- experiments/          # Ch22-26 (Validation protocols)
|   |   `-- applications/         # Ch27-30 (Technology applications)
|   |-- modules/                  # Reusable LaTeX components
|   |   |-- equations/            # 163 equation modules (eq_*.tex)
|   |   |-- figures/              # TikZ/pgfplots visualizations
|   |   |-- tables/               # Data tables
|   |   |-- derivations/          # Multi-step proofs
|   |   |-- algorithms/           # Computational procedures
|   |   `-- narrative/            # Reusable text sections
|   |-- parts/                    # 5 part files
|   |-- frontmatter/              # Title, abstract, notation, acknowledgments
|   |-- backmatter/               # Appendices, glossary, index
|   |-- scripts/                  # Build automation (PowerShell/Bash/Python)
|   `-- data/                     # Generated datasets for figures
|
|-- scripts/                      # Root-level Python utilities
|   |-- equation_extractor.py     # Extract equations from text/markdown
|   |-- pdf_equation_extractor.py # Extract equations from PDFs
|   |-- merge_and_analyze_equations.py  # Build master catalog
|   |-- build_catalog_pipeline.py # Run full extraction pipeline
|   |-- catalog_parity.py         # Check catalog vs modules coverage
|   |-- validate_catalog.py       # Validate catalog integrity
|   |-- link_modules.py           # Cross-link equations by ID
|   |-- gap_todo.py               # Generate TODO list for missing content
|   |-- repo_audit.py             # Repository structure audit
|   `-- tex_audit.py              # LaTeX package/label audit
|
|-- notes/                        # Working documents, drafts, architecture
|-- papers/                       # Source PDFs and references
|-- data/                         # Temporary data staging
|-- docs/                         # Project documentation
|   |-- CLAUDE_GUIDE.md           # Detailed technical guide (superseded by this file)
|   |-- PROJECT_ROADMAP.md        # Phase timeline and milestones
|   |-- REPOSITORY_INFO.md        # Build commands and guidelines
|   `-- NOTATION_GLOSSARY.md      # Symbol definitions
|
|-- equation_catalog.csv          # Master equation catalog (generated)
|-- equation_summary.txt          # Catalog statistics (generated)
|-- notation_conflicts.txt        # Symbol conflicts to resolve (generated)
|-- top_equations.txt             # Most referenced equations (generated)
|-- CATALOG_GAPS_TODO.md          # Missing content checklist (generated)
|-- CATALOG_PARITY.md             # Coverage analysis (generated)
|-- VALIDATION_REPORT.md          # Catalog validation results (generated)
|-- Makefile                      # Linux/WSL build targets
`-- README.md                     # Repository overview
```

## Build Commands

### LaTeX Compilation (synthesis/ directory)

**Full document build** (primary method):
```powershell
cd synthesis
.\scripts\compile.ps1                      # Standard build (pdflatex x2)
.\scripts\compile.ps1 -Engine latexmk      # Alternative engine
```

**Manual compilation** (with bibliography):
```powershell
cd synthesis
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

**Individual chapter testing**:
```powershell
cd synthesis
pdflatex test_ch01.tex                     # Test single chapter
pdflatex test_part1_foundations.tex        # Test entire part
.\test_compilation.ps1                     # Run full test suite (7 tests)
```

**Common issues**:
- "Memory dump file not found" = MiKTeX format files corrupted
  - Fix: Open MiKTeX Console as Admin -> Tasks -> Update formats
  - Or: `initexmf --admin --mklinks && initexmf --admin --dump=pdflatex`

### Equation Catalog Pipeline (root directory)

**Full pipeline** (extracts equations, builds catalog, analyzes):
```powershell
python scripts/build_catalog_pipeline.py --base-dir . --scan-dir notes --scan-dir .
```

**Individual steps**:
```powershell
# Extract from text/markdown sources
python scripts/equation_extractor.py --base-dir . --scan-dir notes --scan-dir .

# Extract from PDFs
python scripts/pdf_equation_extractor.py --base-dir .

# Merge and analyze
python scripts/merge_and_analyze_equations.py --base-dir .

# Check coverage gaps
python scripts/catalog_parity.py --base-dir .

# Generate TODO list
python scripts/gap_todo.py --base-dir .

# Validate catalog integrity
python scripts/validate_catalog.py --base-dir .

# Cross-link modules
python scripts/link_modules.py --base-dir .
```

**Outputs**:
- `equation_catalog.csv` - Master catalog with provenance
- `equation_summary.txt` - Statistics (count by framework/domain)
- `notation_conflicts.txt` - Symbols with multiple definitions
- `top_equations.txt` - Most frequently referenced equations
- `CATALOG_PARITY.md` - Coverage analysis (catalog vs modules)
- `CATALOG_GAPS_TODO.md` - Missing content action items
- `VALIDATION_REPORT.md` - Integrity check results

### Repository Audits

```powershell
# Structure audit
python scripts/repo_audit.py --base-dir .         # -> REPO_AUDIT.md

# LaTeX audit (packages, labels, includes)
python scripts/tex_audit.py --base-dir .          # -> TEX_AUDIT.md

# Benchmark extraction performance
python scripts/benchmark_extraction.py --base-dir . --scan-dir notes
```

### Make Targets (Linux/WSL)

```bash
make pipeline      # Run full catalog pipeline
make audit         # Repository audit
make parity        # Catalog coverage check
make gaps          # Generate gap TODO list
make validate      # Validate catalog
make bench         # Benchmark extraction
make smoke         # Quick smoke test
make test          # Run pytest
make ci            # Full CI suite (smoke + test + validate + audit + parity + gaps)
make latex         # Compile LaTeX (synthesis/scripts/compile.sh)
```

## LaTeX Document Architecture

### Book Structure (5 Parts, 30 Chapters)

**Part I: Mathematical Foundations** (Ch01-06) - COMPLETE
- Ch01: Mathematical Preliminaries (744 lines)
- Ch02: Cayley-Dickson Algebras (682 lines)
- Ch03: Exceptional Lie Groups (789 lines)
- Ch04: E8 Lattice Theory (690 lines)
- Ch05: Fractal Calculus (721 lines)
- Ch06: Monster Group & Moonshine (606 lines)

**Part II: Theoretical Frameworks** (Ch07-16)
- Ch07-10: Aether Framework (scalar fields, ZPE, crystalline lattice, time crystals)
- Ch11-14: Genesis Framework (meta-principles, nodespace, phase transitions, emergent geometry)
- Ch15-16: Pais Framework (EM-gravity coupling, superforce reconciliation)

**Part III: Unified Synthesis** (Ch17-21)
- Ch17: Framework Comparison
- Ch18: Nodal Geometry Unification
- Ch19: Field Dynamics Integration
- Ch20: Hyperdimensional Structures
- Ch21: Emergent Phenomena

**Part IV: Experimental Validation** (Ch22-26)
- Ch22-23: Scalar-ZPE + Time Crystal Protocols
- Ch24: Quantum Foam Measurements
- Ch25: Holographic Entropy Tests
- Ch26: Dimensional Spectroscopy

**Part V: Applications and Outlook** (Ch27-30)
- Ch27: Quantum Computing
- Ch28: Energy Technologies
- Ch29: Advanced Propulsion
- Ch30: Spacetime Engineering

### Equation Modularization System

**Critical principle**: One equation per file in `modules/equations/eq_*.tex` with full provenance.

**Standard equation module format**:
```latex
%==============================================================================
% Equation: [Descriptive name]
% Source: [Document name] (Section X.Y, lines A-B)
% Framework: [Aether|Genesis|Pais] | Domain: [QM|GR|EM|MATH|COSMO|EXP] | Status: [T|E|S|V]
%==============================================================================
\begin{equation}
  [LaTeX equation content]
  \eqtag{FRAMEWORK}{DOMAIN}{STATUS}
  \label{eq:framework:descriptor}
\end{equation}
% Notes: [Physical interpretation, units, conditions]
% Dependencies: [Related chapters/equations]
%==============================================================================
```

**Equation tag system**: `\eqtag{F}{D}{S}`
- Framework: A (Aether), G (Genesis), P (Pais), M (Math/generic), U (Unified)
- Domain: QM, GR, EM, MATH, COSMO, EXP
- Status: T (Theoretical), E (Experimental support), S (Speculative), V (Validated)

**Framework attribution macros** (defined in preamble.tex):
```latex
\aetherattr{content}      % Blue box with "Aether Framework"
\genesisattr{content}     % Green box with "Genesis Framework"
\paisattr{content}        % Orange box with "Pais Framework"
```

**Usage in chapters**:
```latex
\input{modules/equations/eq_aether_scalar_wave}
\input{modules/equations/eq_genesis_e8_projection}
\input{modules/equations/eq_pais_em_gravity_coupling}
```

### preamble.tex Key Components

**Required packages** (all included):
- Mathematics: amsmath, amssymb, amsthm, mathtools, physics
- Graphics: tikz, pgfplots (compat=1.18), graphicx
- Cross-references: hyperref, cleveref
- Tables: booktabs, longtable, multirow
- Units: siunitx
- Bibliography: natbib

**Custom environments**: theorem, lemma, proposition, corollary, definition, remark, example

**Custom macros**:
- Framework attribution: `\aetherattr`, `\genesisattr`, `\paisattr`
- Equation tagging: `\eqtag{F}{D}{S}`
- Common physics: Defined via `physics` package (\ket, \bra, \braket, etc.)

## Critical Technical Details

### Encoding: UTF-8 for LaTeX, ASCII for Code

**UTF-8 REQUIRED** (LaTeX mathematical content):
- Greek letters in equations: α, β, γ, φ, ψ, ω, ∇, ∂, ∫, ∑, ∏
- Mathematical symbols: ℝ, ℂ, ℍ, 𝕆, ∞, ≈, ≤, ≥
- Special characters in narrative text
- `\usepackage[utf8]{inputenc}` in preamble.tex is correct and required

**ASCII ONLY** (Python/PowerShell):
- Variable names and function identifiers
- Code comments
- Markdown documentation (when possible)

### LaTeX Best Practices

**DO**:
- ✓ Create one equation per file in `modules/equations/` with full header
- ✓ Document source (file + line numbers) in equation header comments
- ✓ Use `\input{}` for equations (not `\include{}` which adds page breaks)
- ✓ Add framework attribution with `\aetherattr`, `\genesisattr`, `\paisattr`
- ✓ Use proper `\label{eq:framework:descriptor}` for all equations
- ✓ Test compile chapters individually before full document build
- ✓ Verify cross-references after adding new equations
- ✓ Add physical interpretation in equation header comments

**DON'T**:
- ✗ Hardcode equations directly in chapter files (defeats modularity)
- ✗ Create duplicate equation content across chapters
- ✗ Use Unicode in Python/PowerShell identifiers or comments
- ✗ Commit without clean compilation (zero errors)
- ✗ Skip cross-reference validation before merge
- ✗ Use `\include{}` for equation modules (causes unwanted page breaks)
- ✗ Forget to update equation_catalog.csv when adding modules

### Python Script Conventions

**Common patterns**:
- All scripts accept `--base-dir` (default: `.`) or `MATH_SCIENCE_BASE_DIR` env var
- Multiple scan directories: `--scan-dir notes --scan-dir .` (repeatable)
- Return codes: 0 = success, non-zero = errors found
- Output files written to repository root (unless specified)
- Use `pathlib.Path` for cross-platform compatibility
- Type hints encouraged (Python 3.10+ syntax)

**Standard imports**:
```python
from __future__ import annotations
import argparse
from pathlib import Path
```

**Script naming**: `snake_case.py` for all Python scripts

## Workflow for Adding Content

### Adding a New Equation Module

1. **Create module file**: `synthesis/modules/equations/eq_[framework]_[descriptor].tex`
2. **Add full provenance header** (see format above)
3. **Add to catalog**: Run `python scripts/equation_extractor.py` or manually update `equation_catalog.csv`
4. **Link in chapter**: Add `\input{modules/equations/eq_...}` in appropriate chapter
5. **Test compile**: `cd synthesis && pdflatex test_chNN.tex`
6. **Verify references**: Check that `\label{}` works and `\ref{}` resolves correctly
7. **Cross-link**: Run `python scripts/link_modules.py` to update related equations

### Transforming a Chapter to Whitepaper Style

**Target**: 50-65% narrative, 35-50% equations (currently Ch01-06 meet this standard)

**Process**:
1. **Add opening story** (200-250 words): Historical context or experimental motivation
2. **Add worked examples** (3 per chapter): Numerical calculations with intermediate steps
3. **Add physical interpretations**: Explain what each equation means physically
4. **Add framework attribution**: Use `\aetherattr{}`, `\genesisattr{}`, `\paisattr{}` boxes
5. **Modularize equations**: Move inline equations to `modules/equations/` and `\input{}` them
6. **Test compile**: Verify PDF generation with `pdflatex test_chNN.tex`
7. **Verify agent output**: ALWAYS use bash commands to verify line counts and timestamps
   ```powershell
   wc -l chapters/*/chNN*.tex              # Line count
   ls -lh chapters/*/chNN*.tex             # Timestamp
   grep "keyword" chapters/*/chNN*.tex     # Content spot-check
   ```

### Running Agents in Parallel

**Recommended**: Use 2-3 agents maximum for parallel work (user-validated best practice)

**Example usage**:
```
User: "Complete Ch07-09 transformation using 3 parallel agents"
Claude: I'll deploy 3 agents in parallel to transform Ch07-09 to whitepaper style.
[Launch 3 Task tools in single message]
[After completion, VERIFY each agent's output with bash commands]
```

**Verification protocol** (CRITICAL):
- NEVER trust agent claims without verification
- Use `wc -l`, `ls -lh`, `grep`, `head` to verify files changed
- Check line counts, timestamps, and content spot-checks
- Previous sessions showed agents claiming success but files unchanged
- 100% verification rate achieved in recent sessions by strict checking

## Common Tasks

### Test Individual Chapter Compilation

```powershell
cd synthesis
pdflatex test_ch01.tex     # Compile Ch01 standalone
# Check for errors in test_ch01.log
# Verify test_ch01.pdf generated
```

### Test Part Compilation (All Chapters in Part)

```powershell
cd synthesis
pdflatex test_part1_foundations.tex    # Part I (Ch01-06)
pdflatex test_part2_frameworks.tex     # Part II (Ch07-16) - when created
```

### Run Full Test Suite

```powershell
cd synthesis
.\test_compilation.ps1
# Expected output: "PASSED: 7 / 7" (after MiKTeX repair)
```

### Build Full Document

```powershell
cd synthesis
pdflatex main.tex
bibtex main          # Process bibliography
pdflatex main.tex    # Resolve references (run 1)
pdflatex main.tex    # Resolve references (run 2)
# Output: main.pdf (full book)
```

### Update Equation Catalog After Adding Modules

```powershell
# Re-extract from all sources
python scripts/build_catalog_pipeline.py --base-dir . --scan-dir notes --scan-dir synthesis

# Check coverage
python scripts/catalog_parity.py --base-dir .
# Output: CATALOG_PARITY.md

# Generate TODO list for gaps
python scripts/gap_todo.py --base-dir .
# Output: CATALOG_GAPS_TODO.md
```

### Check for Notation Conflicts

```powershell
python scripts/merge_and_analyze_equations.py --base-dir .
# Check notation_conflicts.txt for symbols with multiple definitions
# Resolve conflicts by adding disambiguation in chapters
```

### Validate Catalog Integrity

```powershell
python scripts/validate_catalog.py --base-dir .
# Output: VALIDATION_REPORT.md
# Exit code 0 = all valid, non-zero = errors found
```

### Repository Audit (Structure Check)

```powershell
python scripts/repo_audit.py --base-dir .
# Output: REPO_AUDIT.md (file structure, sizes, organization)
```

### LaTeX Audit (Packages/Labels/Includes)

```powershell
python scripts/tex_audit.py --base-dir .
# Output: TEX_AUDIT.md (package usage, label definitions, \input/\include stats)
```

## Troubleshooting

### LaTeX Compilation Errors

**"Memory dump file not found" / "pdflatex.fmt not found"**
- Cause: MiKTeX format files corrupted or user/admin mode mismatch
- Fix (RECOMMENDED): Open MiKTeX Console as Administrator -> Tasks -> Update formats
- Fix (CLI): `initexmf --admin --mklinks && initexmf --admin --dump=pdflatex`
- This is NOT a LaTeX syntax error in your files

**"Undefined control sequence"**
- Check that package is loaded in preamble.tex
- Verify command spelling and syntax
- Search preamble.tex for custom macro definitions

**"Missing \begin{document}"**
- Verify preamble.tex exists and is loaded with `\input{preamble}`
- Check for stray text before `\begin{document}` in main.tex

**"Undefined references" / "Citation ... undefined"**
- Normal on first compile
- Run: `pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex`
- Check that `\label{}` and `\cite{}` keys are spelled correctly

**Orphaned `\end{figure}` or `\end{equation}`**
- Search for matching `\begin{}`
- Comment out with: `% \end{figure} % REMOVED - no matching \begin`
- Document reason for commenting

### Python Script Errors

**"Module not found"**
- Current scripts use only standard library (no external dependencies)
- Verify Python 3.10+ installed: `python --version`
- If adding new scripts with dependencies, document in requirements.txt

**"File not found"**
- Check that `--base-dir` points to repository root
- Use absolute paths or ensure working directory is correct
- Windows: Use forward slashes or raw strings for paths

**Script runs but no output files**
- Check exit code: `echo $LASTEXITCODE` (PowerShell) or `echo $?` (Bash)
- Non-zero = errors occurred, check stderr output
- Verify write permissions in target directory

### Verification Failures

**Agent claimed to modify file but line count unchanged**
- CRITICAL: Verify with `wc -l [file]` and `ls -lh [file]`
- Check timestamp to confirm file actually changed
- Re-run agent task with explicit instructions
- This happened in previous sessions - strict verification prevents this

**Test suite shows all failures but content compiles manually**
- MiKTeX issue (see "Memory dump file not found" above)
- Content is correct, system configuration needs repair

## Project Status (as of 2025-10-22)

### Completed
- ✓ Phase 1: Foundations (Ch01-06) - 4,232 total lines
- ✓ All 6 chapters meet whitepaper standards (50-65% narrative)
- ✓ 163 equation modules created in `modules/equations/`
- ✓ preamble.tex with all required packages and macros
- ✓ Test suite infrastructure (8 test files)
- ✓ Frontmatter (title, abstract, notation, acknowledgments)
- ✓ Backmatter scaffolding (appendices, glossary, index)
- ✓ Bibliography (210 entries)
- ✓ Python extraction/catalog pipeline
- ✓ Equation catalog system (CSV + analytics)

### In Progress
- Phase 2: Frameworks (Ch07-16)
  - Ch07-10: Aether Framework (partial)
  - Ch11-14: Genesis Framework (partial)
  - Ch15-16: Pais Framework (partial)

### Planned
- Phase 3: Unification (Ch17-21)
- Phase 4: Experiments (Ch22-26)
- Phase 5: Applications (Ch27-30)

## Key Principles

### Quality Standards
- **Zero warnings policy**: Treat all warnings as errors during build
- **Full implementations only**: No TODOs, FIXMEs, placeholders, or stubs in committed code
- **Documented provenance**: Every equation must cite source file + line numbers
- **Reproducible builds**: Document all dependencies and installation steps
- **Verify agent output**: ALWAYS confirm file changes with bash commands

### Modularity
- Equations live in `modules/equations/`, not inline in chapters
- Figures generated by Python scripts in `synthesis/scripts/`
- Derivations extracted to `modules/derivations/` for reuse
- Tables in `modules/tables/` with CSV data sources
- Narrative snippets in `modules/narrative/` when reused across chapters

### Validation
- Individual chapter compilation must pass before full document build
- Cross-references must resolve (no "Undefined reference" in final PDF)
- Bibliography citations must resolve (run bibtex)
- Equation catalog must match modules (run `catalog_parity.py`)
- Test suite must pass (run `test_compilation.ps1`)

### Collaboration
- Use TodoWrite tool for task management (granular, immediate updates)
- Mark tasks in_progress BEFORE starting work
- Mark completed IMMEDIATELY after finishing (never batch)
- Deploy 2-3 agents maximum for parallel work (user-validated best practice)
- Verify ALL agent outputs with bash commands (line counts, timestamps, content)

## Additional Resources

- **docs/CLAUDE_GUIDE.md**: Detailed technical guidance (legacy, superseded by this file)
- **docs/PROJECT_ROADMAP.md**: 12-week phase timeline and visual workflows
- **docs/REPOSITORY_INFO.md**: Build command reference
- **docs/NOTATION_GLOSSARY.md**: Symbol definitions and conventions
- **synthesis/PHASE1_COMPLETION_REPORT_2025-10-22.md**: Phase 1 results and lessons learned
- **CATALOG_PARITY.md**: Coverage analysis (generated by catalog_parity.py)
- **CATALOG_GAPS_TODO.md**: Missing content action items (generated by gap_todo.py)
- **VALIDATION_REPORT.md**: Catalog integrity check (generated by validate_catalog.py)

## Notes for Future Sessions

1. **MiKTeX repair may be needed**: If compilation fails with "memory dump file not found", use MiKTeX Console GUI to update formats (2-3 minutes, see Troubleshooting section)

2. **Agent deployment**: Use 2-3 parallel agents max. Always verify output with bash commands. Previous sessions showed 100% agent accuracy with strict verification protocol.

3. **Chapter transformation workflow**: Add opening story (200-250 words) -> Add 3 worked examples -> Add physical interpretations -> Modularize equations -> Framework attribution -> Test compile -> Verify

4. **Equation catalog maintenance**: Run `build_catalog_pipeline.py` after adding new modules. Check `catalog_parity.py` for coverage gaps. Use `gap_todo.py` to generate action items.

5. **UTF-8 vs ASCII**: LaTeX mathematical content MUST use UTF-8. Python/PowerShell code MUST use ASCII identifiers and comments.

6. **Test before commit**: Individual chapters (`pdflatex test_chNN.tex`), then parts (`test_part1_foundations.tex`), then full document (`main.tex`). All must compile cleanly.

7. **Cross-platform notes**: Scripts designed for Windows PowerShell but work in WSL/Linux via Makefile. Use forward slashes in paths for portability.

8. **Package conflicts**: preamble.tex has resolved conflicts between `physics`, `siunitx`, and other packages. Do not add conflicting package options without testing.

9. **Label naming convention**: `\label{eq:framework:descriptor}` for equations, `\label{ch:name}` for chapters, `\label{sec:name}` for sections, `\label{fig:name}` for figures, `\label{tab:name}` for tables.

10. **Framework consistency**: Use framework attribution macros consistently. Every major equation should have `\aetherattr{}`, `\genesisattr{}`, or `\paisattr{}` designation.

---

**File created**: 2025-10-22
**Based on**: docs/CLAUDE_GUIDE.md, docs/REPOSITORY_INFO.md, docs/PROJECT_ROADMAP.md, synthesis/PHASE1_COMPLETION_REPORT_2025-10-22.md, README.md
**Status**: Complete and comprehensive for current repository state