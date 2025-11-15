# Build System Guide for PhysicsForge

## Overview

Complete build system for generating PDF artifacts from LaTeX source with Lions Commentary pedagogical enhancements.

---

## Quick Start

### Build Chapter 1 Standalone Paper

```bash
make paper1
```

This compiles `synthesis/papers/paper1_chapter1_demo.tex` to PDF with all 22 visualizations integrated.

### Build Full Monograph (30 Chapters)

```bash
make latex_strict
```

This compiles `synthesis/main.tex` with all chapters.

---

## Makefile Targets

### Paper Compilation

- `make paper1` - Compile Chapter 1 standalone paper
- `make paper2` - Compile Paper 2 (Aether Foundations, Ch 1-3,7-8) [Future]
- `make paper3` - Compile Paper 3 (Genesis Kernel, Ch 4-6,9-10) [Future]
- `make papers` - Compile all 6 papers [Future]

### Monograph Compilation

- `make latex` - Standard LaTeX compilation (warnings OK)
- `make latex_strict` - Strict compilation (warnings are errors)

### Validation

- `make test` - Run Python test suite
- `make ascii_guard` - Check ASCII compliance
- `make validate` - Validate catalog files

### Reporting

- `make reports` - Generate all repository reports
- `make todo` - Update TODO tracker

---

## Directory Structure

```
synthesis/
├── main.tex                    # Main monograph document
├── preamble.tex                # Shared LaTeX preamble
├── bibliography.bib            # BibTeX references
├── chapters/
│   └── foundations/
│       └── ch01_mathematical_preliminaries.tex
├── modules/
│   ├── figures/                # TikZ diagrams (13 files)
│   ├── tables/                 # LaTeX tables (7 files)
│   └── marginal_notes_system.tex
└── papers/
    ├── paper1_chapter1_demo.tex    # Standalone Chapter 1
    ├── paper2_aether.tex           # [Future] Aether Foundations
    ├── paper3_genesis.tex          # [Future] Genesis Kernel
    ├── paper4_superforce.tex       # [Future] Pais Superforce
    ├── paper5_exceptional.tex      # [Future] Exceptional Math
    └── paper6_applications.tex     # [Future] Applications
```

---

## LaTeX Requirements

### Required Packages

```latex
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{graphicx}
\usepackage{tikz}
\usetikzlibrary{calc,arrows.meta,patterns,shapes,decorations}
\usepackage{booktabs}
\usepackage{xcolor}
\usepackage{hyperref}
\usepackage{geometry}
\usepackage{marginnote}
\usepackage{biblatex}  % or \usepackage{natbib}
```

### LaTeX Distribution

Install one of:
- **TeX Live** (Linux/macOS/Windows): https://www.tug.org/texlive/
- **MiKTeX** (Windows): https://miktex.org/
- **MacTeX** (macOS): https://www.tug.org/mactex/

---

## Compilation Process

### Standard Compilation

```bash
cd synthesis/papers
pdflatex paper1_chapter1_demo.tex
bibtex paper1_chapter1_demo
pdflatex paper1_chapter1_demo.tex
pdflatex paper1_chapter1_demo.tex
```

### Using Make

```bash
make paper1
```

This runs:
1. `pdflatex` (first pass)
2. `bibtex` (bibliography)
3. `pdflatex` (resolve citations)
4. `pdflatex` (final pass)

---

## Visualization Modules

### TikZ Diagrams (13 files)

Located in `synthesis/modules/figures/`:

1. `tikz_gps_orbit_detailed.tex` - GPS satellite orbit
2. `tikz_metric_structure.tex` - 4x4 metric tensor
3. `tikz_christoffel_computation.tex` - Computation flowchart
4. `tikz_parallel_transport_sphere.tex` - Path-dependence
5. `tikz_riemann_holonomy.tex` - Closed loop transport
6. `tikz_einstein_equations.tex` - Field equations
7. `tikz_quantum_structure.tex` - QM formalism
8. `tikz_geodesic_equation.tex` - Geodesic equation
9. `tikz_lightcone_curved.tex` - Light cone structure
10. `tikz_dimensional_analysis.tex` - Dimensional workflow
11. `tikz_historical_timeline.tex` - 200-year GR timeline
12. `tikz_schwarzschild_coordinates.tex` - 3 coordinate systems
13. `tikz_gr_to_qft.tex` - GR to quantum gravity pathway
14. `tikz_tidal_forces.tex` - Geodesic deviation

### Tables (7 files, 19 tables)

Located in `synthesis/modules/tables/`:

1. `tab_time_dilation_budget.tex` (2 tables)
2. `tab_covariant_vs_ordinary.tex` (2 tables)
3. `tab_riemann_properties.tex` (2 tables)
4. `tab_special_cases_gr.tex` (3 tables)
5. `tab_computational_complexity.tex` (3 tables)
6. `tab_tensor_comparison_matrices.tex` (4 tables)
7. `tab_curvature_scales.tex` (3 tables)

---

## Marginal Notes System

### 8 Specialized Macros

```latex
\mnote{General note}              % Blue
\mphys{Physical interpretation}   % Purple
\mcomp{Computational guidance}    % Green
\mdim{Dimensional analysis}       % Orange
\mxref{Cross-reference}          % Cyan
\mcaution{Pitfall warning}       % Red
\mhist{Historical context}       % Brown
\mex{Example system}             % Magenta
```

### Usage Example

```latex
\section{Metric Tensor}
\label{sec:metric}

The metric tensor defines the geometry of spacetime:
\begin{equation}
ds^2 = g_{\mu\nu} dx^\mu dx^\nu
\label{eq:metric:line-element}
\end{equation}
\mphys{Metric determines proper time and invariant intervals}
\mdim{$[g_{\mu\nu}] = \text{dimensionless}$, signature $(-,+,+,+)$}
\mxref{See geodesic equation \ref{eq:geodesic}}

For Schwarzschild spacetime:
\begin{equation}
ds^2 = -\left(1-\frac{2GM}{r}\right)dt^2 + \left(1-\frac{2GM}{r}\right)^{-1}dr^2 + r^2 d\Omega^2
\end{equation}
\mcaution{Coordinate singularity at $r=2GM$ (event horizon) - not physical!}
\mex{Solar mass black hole: $2GM/c^2 = 3$ km}
```

---

## Troubleshooting

### Missing Packages

If compilation fails with "package not found":

**TeX Live**:
```bash
tlmgr install <package-name>
```

**MiKTeX**:
Packages auto-install on first use (requires internet)

### Common Issues

**Error: "Undefined control sequence \mnote"**
- Solution: Ensure `\input{modules/marginal_notes_system}` before first use

**Error: "File tikz_*.tex not found"**
- Solution: Compile from `synthesis/papers/` directory or set `\graphicspath`

**Error: "Bibliography not found"**
- Solution: Run `bibtex` step between `pdflatex` runs

---

## PDF Output Locations

After successful compilation:

- `synthesis/papers/paper1_chapter1_demo.pdf` - Chapter 1 standalone
- `synthesis/output/main.pdf` - Full monograph (when implemented)
- `output/` - Release artifacts directory

---

## GitHub Pages Deployment

### Automatic Deployment

PDFs automatically deploy to GitHub Pages on push to `main`:

1. LaTeX compilation runs in GitHub Actions
2. PDF artifacts stored
3. Deployed to `https://Oichkatzelesfrettschen.github.io/PhysicsForge/`

### Manual Deployment

```bash
# Build PDFs locally
make papers

# Copy to docs/ for GitHub Pages
cp synthesis/papers/*.pdf docs/pdfs/

# Commit and push
git add docs/pdfs/
git commit -m "docs: update PDF artifacts"
git push
```

---

## Future Enhancements

### Stream 2: Chapters 2-30

Each chapter will receive:
- 10-15 TikZ diagrams
- 5-10 comprehensive tables
- 100-150 marginal notes
- Complete Lions Commentary treatment

**Timeline**: Systematic rollout, ~1 chapter/week

### Paper Modularization

6 focused papers from 30 chapters:
1. Aether Foundations (Ch 1-3,7-8)
2. Genesis Kernel (Ch 4-6,9-10)
3. Pais Superforce (Ch 11-15)
4. Exceptional Math (Ch 16-20)
5. Experimental Predictions (Ch 21-25)
6. Applications (Ch 26-30)

### Content Extraction

Automated pipeline for .md/.txt → .tex conversion:
- Extract equations → eq_*.tex modules
- Generate TikZ diagrams from descriptions
- Create pgfplots from data tables

---

## References

- **LaTeX Documentation**: https://www.latex-project.org/help/documentation/
- **TikZ Manual**: https://tikz.dev/
- **PGFPlots Manual**: https://ctan.org/pkg/pgfplots
- **BibLaTeX Manual**: https://ctan.org/pkg/biblatex

---

**Status**: Build system ready for Chapter 1 PDF generation. Stream 1 complete.
