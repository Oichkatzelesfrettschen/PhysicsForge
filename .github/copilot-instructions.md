# GitHub Copilot Instructions for PhysicsForge

**Last Updated**: November 16, 2025
**Repository**: PhysicsForge - Unified Field Theories and Advanced Physics Research Hub

---

## Project Overview

PhysicsForge is a comprehensive theoretical physics research repository that has been restructured from a single 500+ page monograph into **six focused, peer-reviewable papers** using **standard scientific nomenclature**.

### Series Title
**"Unified Field Theories and Advanced Physics: A Mathematical Synthesis"**

###Six Papers
1. **Paper 1**: Scalar Field Theory and Zero-Point Energy Coupling (25-30 pages)
2. **Paper 2**: Exceptional Lie Algebras and Crystalline Lattice Structures (30-35 pages)
3. **Paper 3**: Fractal Geometry and Hyperdimensional Field Structures (25-30 pages)
4. **Paper 4**: Gravitational-Electromagnetic Unification via Scalar Intermediaries (28-33 pages)
5. **Paper 5**: Experimental Protocols for Exotic Quantum States (30-35 pages)
6. **Paper 6**: Applications to Quantum Computing and Energy Technologies (25-30 pages)

---

## Critical Standards

### 1. Terminology - STRICT ENFORCEMENT

**NEVER USE** deprecated terms:
- ❌ "Aether Framework"
- ❌ "Aether Scalar Fields"
- ❌ "Genesis Framework"
- ❌ "Pais Superforce"

**ALWAYS USE** standard physics terminology:
- ✓ "Scalar Field Theory"
- ✓ "Quantum Vacuum"
- ✓ "Zero-Point Energy"
- ✓ "Exceptional Lie Groups"
- ✓ "E8 Lattice"
- ✓ "Time Crystals"
- ✓ "Casimir Effect"
- ✓ "Gravitational-Electromagnetic Unification"

**Reference**: `synthesis/shared/glossary.tex` for complete approved terminology

---

## Repository Structure

```
PhysicsForge/
├── synthesis/
│   ├── shared/                         # SHARED INFRASTRUCTURE
│   │   ├── common_preamble.tex         # LaTeX packages & settings
│   │   ├── common_macros.tex           # Standard physics macros
│   │   ├── glossary.tex                # 80+ approved terms
│   │   ├── notation.tex                # Symbol conventions
│   │   └── marginal_notes_system.tex   # Lions commentary macros
│   │
│   ├── papers/                         # SIX MODULAR PAPERS
│   │   ├── paper1_scalar_field_zpe/
│   │   │   ├── paper1_main.tex         # Main compilation file
│   │   │   ├── chapters/               # Chapters 1-4 (sequential)
│   │   │   ├── figures/                # TikZ/PGFPlots
│   │   │   └── bibliography_p1.bib     # Paper-specific refs
│   │   ├── paper2_exceptional_algebras/
│   │   ├── paper3_fractal_geometry/
│   │   ├── paper4_em_gravity_unification/
│   │   ├── paper5_experimental_protocols/
│   │   └── paper6_applications/
│   │
│   ├── build/                          # Compiled PDFs
│   ├── chapters/                       # Original monograph (being migrated)
│   └── modules/                        # Reusable components
│
├── scripts/                            # Python automation
├── docs/                               # Comprehensive documentation
├── figures/                            # Figure sources
└── tests/                              # Validation tests
```

---

## Coding Standards

### LaTeX

**File Naming**:
- Papers: `paperN_main.tex` (N=1..6)
- Chapters: `chNN_descriptive_name.tex` (sequential per paper)
- Equations: `eq_domain_descriptor.tex`
- Figures: `fig_domain_descriptor.tex`

**Required Headers**:
```latex
%==============================================================================
% CHAPTER N: Title Using Standard Terminology
% Paper X of PhysicsForge Series
% Purpose: Clear description
%==============================================================================
```

**Shared Infrastructure Usage**:
```latex
% ALWAYS include in paper main files:
\input{../../shared/common_preamble}
\input{../../shared/common_macros}
\input{../../shared/marginal_notes_system}
```

**Marginal Notes (Lions Commentary)**:
- Use 8 specialized macros: `\mnote`, `\mphys`, `\mcomp`, `\mdim`, `\mxref`, `\mcaution`, `\mhist`, `\mex`
- Target: 150+ marginal notes per paper
- Example: `\mphys{Time dilation: $\Delta t/t \sim GM/rc^2$}`

**Visualizations**:
- 4-6 TikZ diagrams per chapter
- 3-5 pgfplots per chapter
- 2-3 multidimensional visualizations per chapter
- All figures must have captions and labels

### Python

**Style**:
- Python 3.10+ (type hints required)
- Four-space indents
- Snake_case for files and functions
- Docstrings for all functions
- Use `pathlib.Path` for cross-platform compatibility

**Required**:
```python
#!/usr/bin/env python3
"""
Module description
"""
from __future__ import annotations
from pathlib import Path
import argparse
```

**Common Imports**:
- Use `scripts/common.py` for `resolve_base_dir()` and PDF helpers
- Accept `--base-dir` argument (default: repository root)

---

## Build System

### Makefile Targets (To Be Implemented)

```makefile
# Individual papers
make paper1  # Build Paper 1 (Scalar Field Theory)
make paper2  # Build Paper 2 (Exceptional Algebras)
make paper3  # Build Paper 3 (Fractal Geometry)
make paper4  # Build Paper 4 (EM-Gravity Unification)
make paper5  # Build Paper 5 (Experimental Protocols)
make paper6  # Build Paper 6 (Applications)

# Collective
make papers_all    # Build all 6 papers
make papers_clean  # Clean build artifacts

# Legacy
make latex         # Build original monograph
make test          # Run pytest
make ci            # Full CI pipeline
```

### Python Build Script (To Be Implemented)
```bash
python scripts/build_all_papers.py        # Build all papers
python scripts/build_all_papers.py 1      # Build Paper 1 only
```

---

## Quality Standards

### Per Chapter Requirements
- [x] Standard terminology only (no deprecated terms)
- [x] Sequential numbering within paper
- [x] 150+ marginal notes (Lions Commentary style)
- [x] 20-30 high-quality visualizations (TikZ/PGFPlots)
- [x] 3-5 worked numerical examples
- [x] Physical interpretation for every equation
- [x] Dimensional analysis throughout
- [x] Complete cross-references

### Chapter 1 as Template
The existing `ch01_mathematical_preliminaries.tex` with its 22 visualizations and comprehensive marginal notes serves as the **quality standard** for all future chapters.

---

## Common Tasks for Copilot

### Adding a New Equation
```latex
% File: synthesis/modules/equations/eq_casimir_force.tex
%==============================================================================
% Equation: Casimir Force Between Parallel Plates
% Source: Paper 1, Chapter 3 (Quantum Vacuum)
% Domain: Quantum Electrodynamics
%==============================================================================
\begin{equation}
F_{\mathrm{Cas}} = -\frac{\pi^2 \hbar c}{240 d^4} A
\label{eq:casimir:force}
\end{equation}
% Physical Interpretation: Attractive force between conducting plates
% Units: [Force] = [Energy]/[Length]
% Dimensions: F ~ hbar c / d^4
%==============================================================================
```

### Adding a TikZ Figure
```latex
\begin{figure}[htbp]
\centering
\begin{tikzpicture}
  % Casimir plates configuration
  \draw[thick, fill=gray!20] (0,0) rectangle (0.2,3);
  \draw[thick, fill=gray!20] (4,0) rectangle (4.2,3);
  \draw[<->] (0.2,1.5) -- node[above] {$d$} (4,1.5);
  % Vacuum fluctuations
  \foreach \x in {0.5,1,...,3.5} {
    \draw[blue!50,decorate,decoration={snake}] (\x,0.5) -- (\x,2.5);
  }
  \node at (2.1,-0.5) {Quantum Vacuum};
\end{tikzpicture}
\caption{Casimir effect: parallel conducting plates with vacuum fluctuations}
\label{fig:casimir_plates}
\end{figure}

\mphys{Boundary conditions modify vacuum modes, leading to net attractive force}
\mdim{Force scales as $1/d^4$ for perfect conductors}
```

### Adding Marginal Notes
```latex
The Casimir effect
\mnote{H. Casimir, 1948}
arises from boundary condition modifications of the electromagnetic vacuum.
\mphys{Vacuum fluctuations have measurable consequences}
Between two parallel conducting plates separated by distance $d$,
\mdim{[$d$] = length}
the force per unit area is
\begin{equation}
P_{\mathrm{Cas}} = -\frac{\pi^2 \hbar c}{240 d^4}
\end{equation}
\mcaution{Negative sign indicates attraction}
\mcomp{Use $\hbar c \approx 197$ eV·nm for numerical estimates}
```

---

## Prohibited Actions

### NEVER:
1. Use deprecated terminology ("Aether", "Genesis", "Pais")
2. Create chapters with non-sequential numbering
3. Skip dimensional analysis in equations
4. Omit marginal notes in pedagogical sections
5. Use hardcoded equations (always modularize to `modules/equations/`)
6. Create visualizations without proper captions and labels
7. Add TODO/FIXME comments without immediate resolution
8. Commit without clean LaTeX compilation (zero warnings)
9. Use Unicode in Python identifiers or comments
10. Bypass shared infrastructure (always use `synthesis/shared/`)

---

## Testing and Validation

### Before Committing:
```bash
# Test individual chapter
cd synthesis/papers/paper1_scalar_field_zpe
pdflatex paper1_main.tex

# Check for errors
grep -i "error\|warning\|undefined" paper1_main.log

# Verify cross-references resolved
grep "??" paper1_main.log  # Should be empty

# Run full test suite
make test

# ASCII enforcement
make ascii_guard
```

---

## Documentation References

- **Paper Structure**: See `PAPER_STRUCTURE_NORMALIZED.md`
- **Progress Report**: See `RESTRUCTURE_PROGRESS_REPORT.md`
- **Glossary**: See `synthesis/shared/glossary.tex`
- **Build Guide**: See `docs/BUILD_SYSTEM_GUIDE.md`
- **Agent Guidelines**: See `docs/AGENTS.md`, `docs/CLAUDE.md`, `GEMINI.md`

---

## Current Status (November 2025)

**Phase 1 Complete**: Infrastructure established
- ✓ Shared components created (preamble, macros, glossary, notation)
- ✓ All 6 paper directories structured
- ✓ Paper 1 template ready
- ✓ Standard terminology enforced

**Phase 2 In Progress**: Content migration
- Migrating chapters to new paper structure
- Building Makefile targets
- Updating configuration files

---

## Key Principles

1. **Standard Nomenclature**: Use established physics terminology exclusively
2. **Modularity**: Each paper is self-contained, using shared infrastructure
3. **Quality**: Chapter 1 sets the standard (Lions Commentary + visualizations)
4. **Reproducibility**: Zero warnings, complete cross-references, clean builds
5. **Pedagogy**: Physical interpretation and dimensional analysis throughout

---

**For Questions**: See `docs/CLAUDE.md`, `GEMINI.md`, or repository README.md
