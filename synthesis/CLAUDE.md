# synthesis/ Directory Guide

**Location:** `/home/eirikr/Playground/PhysicsForge/synthesis/`

## Purpose

This is the **PRIMARY WORK AREA** for the LaTeX book project. All LaTeX source files, compiled outputs, and build artifacts live here.

## ⚠️ CRITICAL: Build Workflow

**NEVER build from this directory.** Always return to project root:

```bash
# WRONG - Do NOT do this
cd ~/Playground/PhysicsForge/synthesis
pdflatex main.tex

# CORRECT - Always do this
cd ~/Playground/PhysicsForge
make latex
```

## Directory Structure

```
synthesis/
├── main.tex                 # Master document file
├── preamble.tex            # Packages, macros, custom commands
├── bibliography.bib        # BibTeX references
├── chapters/               # 30 chapters (Ch01-Ch30)
│   ├── foundations/        # Part I: Ch01-06
│   ├── frameworks/         # Part II: Ch07-16
│   ├── unification/        # Part III: Ch17-21
│   ├── experiments/        # Part IV: Ch22-26
│   └── applications/       # Part V: Ch27-30
├── modules/                # Reusable LaTeX components
│   ├── equations/          # 163+ equation modules (eq_*.tex)
│   ├── figures/            # TikZ/pgfplots visualizations
│   ├── tables/             # Data tables
│   ├── derivations/        # Multi-step proofs
│   └── narrative/          # Reusable text sections
├── parts/                  # Part opener files (part1.tex - part5.tex)
├── frontmatter/            # Title, abstract, notation, acknowledgments
├── backmatter/             # Appendices, glossary, index
├── scripts/                # Build scripts (compile.sh)
├── build/                  # Build artifacts (auto-generated)
└── logs/                   # Compilation logs
```

## Key Files

### main.tex
Master document that includes all parts, chapters, and modules.

### preamble.tex
Contains:
- Package declarations (amsmath, tikz, hyperref, etc.)
- Custom macros (`\aetherattr`, `\genesisattr`, `\paisattr`)
- Equation tagging system (`\eqtag{F}{D}{S}`)
- Framework attribution commands

### bibliography.bib
210+ BibTeX entries for citations.

## Working with This Directory

### Reading Files
```bash
# Always use absolute paths from project root
cat ~/Playground/PhysicsForge/synthesis/preamble.tex
grep "equation" ~/Playground/PhysicsForge/synthesis/chapters/foundations/ch01*.tex
```

### Editing Files
Edit files directly but **always test with root Makefile**:
```bash
# Edit a chapter
vim ~/Playground/PhysicsForge/synthesis/chapters/foundations/ch01_mathematical_preliminaries.tex

# Test compilation from ROOT
cd ~/Playground/PhysicsForge
make latex
```

### Testing Individual Chapters
Test files are in synthesis/ root:
```bash
cd ~/Playground/PhysicsForge
pdflatex synthesis/test_ch01.tex              # Single chapter
pdflatex synthesis/test_part1_foundations.tex  # Entire part
```

## Build Outputs

All outputs go to synthesis/ subdirectories:
- **PDF:** `synthesis/main.pdf` (final document)
- **Logs:** `synthesis/main.log`, `synthesis/logs/`
- **Auxiliary:** `synthesis/main.aux`, `synthesis/main.toc`, etc.

## Common Tasks

### Add a New Equation Module
1. Create file: `synthesis/modules/equations/eq_framework_descriptor.tex`
2. Use standard format:
```latex
%==============================================================================
% Equation: [Name]
% Source: [File] (Section X.Y, lines A-B)
% Framework: [A|G|P] | Domain: [QM|GR|EM] | Status: [T|E|S|V]
%==============================================================================
\begin{equation}
  [LaTeX content]
  \eqtag{F}{D}{S}
  \label{eq:framework:descriptor}
\end{equation}
```
3. Include in chapter: `\input{modules/equations/eq_framework_descriptor}`
4. Test from root: `cd ~/Playground/PhysicsForge && make latex`

### Add a New Chapter
1. Create file: `synthesis/chapters/[part]/chNN_title.tex`
2. Create test file: `synthesis/test_chNN.tex`
3. Include in appropriate part file: `synthesis/parts/partN.tex`
4. Test from root: `cd ~/Playground/PhysicsForge && pdflatex synthesis/test_chNN.tex`

### Update Bibliography
1. Edit: `synthesis/bibliography.bib`
2. Rebuild with BibTeX from root:
```bash
cd ~/Playground/PhysicsForge
make latex    # Runs pdflatex + bibtex automatically
```

## Package Management

All packages are declared in `preamble.tex`. **Never** add `\usepackage{}` to individual chapters.

To add a new package:
1. Edit `synthesis/preamble.tex`
2. Add package in appropriate section (see comments)
3. Test compilation from root
4. Check for package conflicts in logs

## Equation Tagging System

Framework codes:
- **A** = Aether
- **G** = Genesis
- **P** = Pais
- **M** = Math/Generic
- **U** = Unified

Domain codes:
- **QM** = Quantum Mechanics
- **GR** = General Relativity
- **EM** = Electromagnetism
- **MATH** = Pure Mathematics
- **COSMO** = Cosmology
- **EXP** = Experimental

Status codes:
- **T** = Theoretical
- **E** = Experimental support
- **S** = Speculative
- **V** = Validated

Example: `\eqtag{A}{QM}{T}` = Aether framework, quantum mechanics, theoretical

## Troubleshooting

### Compilation Errors
**Always compile from project root:**
```bash
cd ~/Playground/PhysicsForge
make latex
# Check logs/latexmk_compile.log for errors
```

### Missing References
Run full BibTeX cycle:
```bash
cd ~/Playground/PhysicsForge
make latex  # Handles pdflatex + bibtex automatically
```

### Unicode Errors
Check for non-ASCII characters:
```bash
cd ~/Playground/PhysicsForge
grep -rn '[^ -~]' synthesis/chapters synthesis/modules --include="*.tex"
```

### Package Not Found
1. Check preamble.tex for typos
2. Ensure package is installed (TeX Live or MiKTeX)
3. Update package database: `tlmgr update --self --all` (TeX Live)

## Best Practices

1. **One equation per file** in modules/equations/
2. **Document provenance** in equation headers (source file + lines)
3. **Test individual chapters** before full document build
4. **Use \input{}** not \include{} for equation modules
5. **Absolute paths** when referencing from root scripts
6. **Always return to root** for builds and tests
7. **UTF-8 encoding** for all .tex files

## See Also

- `/home/eirikr/Playground/PhysicsForge/CLAUDE.md` - Project root guidelines
- `/home/eirikr/Playground/PhysicsForge/docs/` - Extended documentation
- `synthesis/scripts/CLAUDE.md` - Build script guidelines (if exists)
