# PhysicsForge Paper Series: Build Instructions

## Quick Start

```bash
# Clone repository
git clone https://github.com/Oichkatzelesfrettschen/PhysicsForge.git
cd PhysicsForge

# Build all 6 papers
make papers_all

# Build individual paper
make paper1-new  # or paper2, paper3, paper4, paper5, paper6

# Clean build artifacts
make papers_clean
```

**Output location**: `synthesis/build/paper{1-6}_{name}.pdf`

---

## System Requirements

### Required Software

1. **TeX Live 2020 or Later** (Full installation recommended)
   ```bash
   # Ubuntu/Debian
   sudo apt-get install texlive-full

   # macOS (via Homebrew)
   brew install --cask mactex

   # Windows
   # Download from: https://www.tug.org/texlive/windows.html
   ```

2. **Make** (build automation)
   ```bash
   # Usually pre-installed on Linux/macOS
   # Windows: Install via WSL or MinGW
   ```

### Required LaTeX Packages

The following packages must be available (included in texlive-full):

**Core Packages**:
- `book` documentclass
- `amsmath`, `amssymb`, `amsthm` (mathematics)
- `geometry` (page layout)
- `hyperref` (PDF metadata and links)
- `natbib` (bibliography)

**Graphics Packages**:
- `tikz` (vector graphics)
- `pgfplots` (data plotting)
- `graphicx` (image inclusion)
- `xcolor` (color support)

**Typography Packages**:
- `fontenc`, `inputenc` (character encoding)
- `microtype` (typography enhancement)
- `fancyhdr` (headers/footers)

**Specialized Packages**:
- `marginnote` (marginal annotations)
- `tcolorbox` (colored boxes)
- `listings` (code listings)
- `booktabs` (professional tables)

**Check Installation**:
```bash
kpsewhich amsmath.sty
kpsewhich tikz.sty
kpsewhich pgfplots.sty
# Should return package paths if installed
```

---

## Build Process

### Individual Paper Build

```bash
cd /path/to/PhysicsForge
make paper1-new  # Builds Paper 1
```

**Build steps executed**:
1. `pdflatex paper1_main.tex` (first pass - resolve structure)
2. `bibtex paper1_main` (generate bibliography)
3. `pdflatex paper1_main.tex` (second pass - resolve citations)
4. `pdflatex paper1_main.tex` (third pass - finalize cross-references)
5. Move `paper1_main.pdf` → `synthesis/build/paper1_scalar_field_zpe.pdf`

**Build time**: ~30-60 seconds per paper (depending on system)

### All Papers Build

```bash
make papers_all
```

Builds all 6 papers sequentially:
- Paper 1: Scalar Field Theory and ZPE
- Paper 2: Exceptional Algebras
- Paper 3: Fractal Geometry
- Paper 4: EM-Gravity Unification
- Paper 5: Experimental Protocols
- Paper 6: Applications and Future

**Total build time**: ~5-10 minutes

### Clean Build Artifacts

```bash
make papers_clean
```

Removes intermediate files:
- `*.aux` (auxiliary files)
- `*.log` (compilation logs)
- `*.out` (outline files)
- `*.toc` (table of contents)
- `*.bbl` (bibliography processing)
- `*.blg` (bibliography logs)
- `*.fls` (file list)

**PDFs are preserved** in `synthesis/build/`

---

## Manual Build (Advanced)

If you prefer to build manually without make:

```bash
cd synthesis/papers/paper1_scalar_field_zpe

# First pass
pdflatex -interaction=nonstopmode paper1_main.tex

# Bibliography
bibtex paper1_main

# Second pass (resolve citations)
pdflatex -interaction=nonstopmode paper1_main.tex

# Third pass (finalize cross-refs)
pdflatex -interaction=nonstopmode paper1_main.tex

# Output: paper1_main.pdf
```

**Repeat for each paper** (paper2, paper3, ..., paper6)

---

## Troubleshooting

### Common Errors and Solutions

#### 1. **Package Not Found**

**Error**:
```
! LaTeX Error: File `tikz.sty' not found.
```

**Solution**:
```bash
# Install missing package (example for tikz)
sudo tlmgr install pgf tikz

# Or install full TeX Live
sudo apt-get install texlive-full
```

#### 2. **Bibliography Errors**

**Error**:
```
Warning: Citation 'Einstein1915' on page 5 undefined
```

**Solution**:
- Ensure `bibliography_shared.bib` symlink exists in `synthesis/shared/`
- Run build process completely (3 pdflatex passes + bibtex)
- Check that `.bib` files are in correct directories

**Verify symlink**:
```bash
ls -la synthesis/shared/bibliography_shared.bib
# Should show: bibliography_shared.bib -> ../bibliography.bib
```

**Recreate if missing**:
```bash
cd synthesis/shared
ln -s ../bibliography.bib bibliography_shared.bib
```

#### 3. **TikZ Dimension Too Large**

**Error**:
```
! Dimension too large.
```

**Solution**:
- This occurs with very large or very small coordinates in TikZ
- Add `[scale=0.5]` to the problematic `\begin{tikzpicture}` line
- Or use `x=1cm, y=1cm` to explicitly set unit sizes

**Example fix**:
```latex
% Before
\begin{tikzpicture}
  \draw (0,0) -- (1000000,0);  % Too large!
\end{tikzpicture}

% After
\begin{tikzpicture}[scale=0.001]
  \draw (0,0) -- (1000000,0);  % Now 1000 cm → 1 cm
\end{tikzpicture}
```

#### 4. **Compilation Hangs**

**Symptom**: pdflatex stops responding during compilation

**Solution**:
1. **Interrupt**: Press `Ctrl+C`
2. **Check for errors in source**: Look for `\input{missing_file.tex}`
3. **Use halt-on-error**:
   ```bash
   pdflatex -interaction=nonstopmode -halt-on-error paper1_main.tex
   ```
4. **Check log file**: `less paper1_main.log` (look for last operation)

#### 5. **Missing Cross-References**

**Warning**:
```
LaTeX Warning: Reference `eq:einstein' on page 12 undefined.
```

**Solution**:
- Run pdflatex **3 times** (cross-references resolved in passes 2-3)
- If persists, check that referenced label exists (e.g., `\label{eq:einstein}`)

#### 6. **Font Encoding Warnings**

**Warning**:
```
Package inputenc Warning: inputenc package ignored with utf8 based engines.
```

**Solution**:
- This is **informational only** (not an error)
- Modern LaTeX engines handle UTF-8 automatically
- Safe to ignore

---

## Build Optimization

### Faster Incremental Builds

When editing a single chapter:

```bash
cd synthesis/papers/paper1_scalar_field_zpe

# Quick compile (skip bibliography)
pdflatex -interaction=batchmode paper1_main.tex

# Only if citations changed
bibtex paper1_main
pdflatex paper1_main.tex
```

**Build time**: ~10-15 seconds (vs. 30-60s for full build)

### Parallel Builds

Build multiple papers simultaneously (multi-core systems):

```bash
# GNU Make parallel execution
make -j 4 papers_all  # Use 4 cores

# Or manually
make paper1-new & make paper2 & make paper3 & wait
```

**Caution**: Requires sufficient RAM (~2GB per concurrent build)

### Draft Mode

For faster preview during editing:

```latex
% In paper*_main.tex, add to \documentclass options:
\documentclass[11pt,letterpaper,oneside,draft]{book}
%                                         ^^^^^
% Disables: figure rendering, hyperlinks, complex graphics
```

**Speedup**: ~50-70% faster compilation

---

## Continuous Integration

### Automated Testing

Set up CI/CD to build papers on every commit:

**.github/workflows/build-papers.yml** (example):
```yaml
name: Build PhysicsForge Papers

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Install TeX Live
        run: |
          sudo apt-get update
          sudo apt-get install -y texlive-full

      - name: Build all papers
        run: make papers_all

      - name: Upload PDFs
        uses: actions/upload-artifact@v2
        with:
          name: papers
          path: synthesis/build/*.pdf
```

### Pre-commit Hooks

Validate LaTeX syntax before committing:

**.git/hooks/pre-commit**:
```bash
#!/bin/bash
# Check for common LaTeX errors

for file in $(git diff --cached --name-only | grep '\.tex$'); do
  # Check for unmatched braces
  python3 -c "
import sys
with open('$file') as f:
    text = f.read()
    if text.count('{') != text.count('}'):
        print(f'Unmatched braces in $file')
        sys.exit(1)
  " || exit 1
done

echo "LaTeX syntax check passed"
```

---

## Output Specifications

### PDF Metadata

Each generated PDF includes:

**Paper 1 Example**:
- **Title**: Scalar Field Theory and Zero-Point Energy Coupling
- **Author**: PhysicsForge Collaboration
- **Subject**: Quantum Vacuum Physics and Scalar Field Dynamics
- **Keywords**: scalar fields, zero-point energy, Casimir effect, quantum vacuum
- **Creator**: pdfLaTeX
- **PDF Version**: 1.5

### File Sizes

Expected PDF sizes (with all TikZ figures):

| Paper | Chapters | Approx. Size |
|-------|----------|--------------|
| Paper 1 | 4 | 2.5-3.5 MB |
| Paper 2 | 5 | 3.5-4.5 MB |
| Paper 3 | 4 | 2.5-3.5 MB |
| Paper 4 | 4 | 3.0-4.0 MB |
| Paper 5 | 5 | 3.5-4.5 MB |
| Paper 6 | 4 | 4.0-5.0 MB |

**Total**: ~18-25 MB for all 6 papers

### Page Counts

| Paper | Chapters | Pages |
|-------|----------|-------|
| Paper 1 | 4 | 25-30 |
| Paper 2 | 5 | 30-35 |
| Paper 3 | 4 | 28-32 |
| Paper 4 | 4 | 30-35 |
| Paper 5 | 5 | 32-38 |
| Paper 6 | 4 | 35-40 |

**Total**: ~180-210 pages across series

---

## Advanced Customization

### Custom Build Locations

Modify Makefile to change output directory:

```makefile
# Change this line in Makefile
BUILD_DIR := synthesis/custom_build

# Then rebuild
make papers_all
```

### Include/Exclude Chapters

Comment out chapters in `paper*_main.tex`:

```latex
% Chapter 1: Mathematical Preliminaries
\input{chapters/ch01_mathematical_preliminaries}

% Chapter 2: Scalar Field Lagrangian Formulation
% \input{chapters/ch02_scalar_lagrangian}  % COMMENTED OUT

% Chapter 3: Zero-Point Energy and Quantum Vacuum
\input{chapters/ch03_quantum_vacuum}
```

### Custom Paper Subsets

Build only Papers 1, 4, and 6:

```bash
make paper1-new paper4 paper6
```

Or create custom Makefile target:

```makefile
papers_core: paper1-new paper2 paper4
	@echo "Core theory papers built"
```

---

## Platform-Specific Notes

### Linux

**Recommended Distribution**: Ubuntu 20.04+ or Debian 11+

```bash
# Install dependencies
sudo apt-get update
sudo apt-get install texlive-full make git

# Build
cd PhysicsForge
make papers_all
```

**Note**: On minimal installations, use `texlive-latex-extra` instead of `texlive-full` to save space

### macOS

**Recommended Version**: macOS 11 (Big Sur) or later

```bash
# Install MacTeX (large download ~4GB)
brew install --cask mactex

# Or BasicTeX (smaller, ~100MB) + manual packages
brew install --cask basictex
sudo tlmgr update --self
sudo tlmgr install collection-fontsrecommended collection-latexextra

# Build
cd PhysicsForge
make papers_all
```

### Windows

**Option 1: WSL (Recommended)**

```powershell
# Install WSL2 with Ubuntu
wsl --install

# Then follow Linux instructions
```

**Option 2: Native Windows**

```powershell
# Install MiKTeX from https://miktex.org/
# Install Make from http://gnuwin32.sourceforge.net/packages/make.htm

# Build (in PowerShell or CMD)
cd PhysicsForge
make papers_all
```

**Option 3: Docker**

```bash
# Use containerized TeX Live
docker run --rm -v ${PWD}:/workspace texlive/texlive \
  make -C /workspace papers_all
```

---

## Performance Benchmarks

### Build Times (Sample System: i7-10700K, 32GB RAM, NVMe SSD)

| Paper | Lines | TikZ Diagrams | Build Time |
|-------|-------|---------------|------------|
| Paper 1 | ~1,800 | 15 | 35s |
| Paper 2 | ~2,600 | 15 | 48s |
| Paper 3 | ~1,770 | 23 | 42s |
| Paper 4 | ~2,010 | 15 | 38s |
| Paper 5 | ~2,590 | 16 | 45s |
| Paper 6 | ~2,570 | 20 | 52s |

**Total sequential**: ~4m 20s
**Total parallel (-j6)**: ~1m 30s

### Resource Usage

- **RAM**: 500-800 MB per paper compilation
- **Disk Space**:
  - Source files: ~15 MB
  - Build artifacts (intermediate): ~50 MB
  - Final PDFs: ~20 MB
  - TeX Live installation: ~4-6 GB

---

## Quality Checks

### Post-Build Verification

**1. Check for LaTeX Warnings**

```bash
grep -i warning synthesis/papers/paper1_scalar_field_zpe/paper1_main.log
```

**Common acceptable warnings**:
- `Package inputenc Warning: inputenc package ignored` (UTF-8 handled automatically)
- `LaTeX Font Warning: Font shape ... not available` (if using substitutes)

**2. Verify PDF Metadata**

```bash
pdfinfo synthesis/build/paper1_scalar_field_zpe.pdf
```

Expected output includes:
- Title, Author, Subject, Keywords
- PDF version: 1.5 or higher
- Page count matches expectations

**3. Check for Broken Cross-References**

```bash
grep -i "undefined" synthesis/papers/paper1_scalar_field_zpe/paper1_main.log
```

Should return **no results** after successful build

**4. Validate Bibliography**

```bash
grep -c "bibitem" synthesis/papers/paper1_scalar_field_zpe/paper1_main.bbl
```

Should match number of citations in `bibliography_p1.bib`

### Visual Inspection Checklist

- [ ] Title page renders correctly
- [ ] Table of contents shows all chapters
- [ ] All TikZ diagrams display properly
- [ ] Marginal notes appear in correct locations
- [ ] Equations are numbered consistently
- [ ] Bibliography entries are formatted correctly
- [ ] Hyperlinks work (test in PDF viewer)
- [ ] No overflow boxes (black rectangles)

---

## Troubleshooting Resources

### Log File Analysis

**Find errors in log file**:
```bash
grep -A 5 "^!" synthesis/papers/paper1_scalar_field_zpe/paper1_main.log
```

**Find overfull boxes** (text overflowing margins):
```bash
grep "Overfull" synthesis/papers/paper1_scalar_field_zpe/paper1_main.log
```

### Online Resources

- **TeX Stack Exchange**: https://tex.stackexchange.com/
- **LaTeX Wikibook**: https://en.wikibooks.org/wiki/LaTeX
- **TikZ/PGF Manual**: http://mirrors.ctan.org/graphics/pgf/base/doc/pgfmanual.pdf
- **CTAN Package Search**: https://www.ctan.org/

### Community Support

- **GitHub Issues**: https://github.com/Oichkatzelesfrettschen/PhysicsForge/issues
- **Email**: [via GitHub profile]

---

## License and Attribution

**License**: [Specify repository license]

**Citation**:
```
PhysicsForge Collaboration, "Unified Field Theories and Advanced Physics:
Build Instructions and Developer Guide," PhysicsForge Paper Series (2025),
https://github.com/Oichkatzelesfrettschen/PhysicsForge
```

---

**Last Updated**: 2025-11-17
**Document Version**: 1.0
**Compatible with**: Papers 1-6 (v1.0)
