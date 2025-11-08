# synthesis/modules/ Directory Guide

**Location:** `/home/eirikr/Playground/PhysicsForge/synthesis/modules/`

## Purpose

Reusable LaTeX components that are included across multiple chapters. This modular approach ensures:
- **Single source of truth** for equations/figures
- **Consistent formatting** across document
- **Easy maintenance** - fix once, applies everywhere
- **Provenance tracking** - each module documents its source

## ⚠️ CRITICAL: Build Workflow

**Never build from this directory:**

```bash
# WRONG
cd ~/Playground/PhysicsForge/synthesis/modules
# (no build commands should run here)

# CORRECT
cd ~/Playground/PhysicsForge
make latex
```

## Directory Structure

```
modules/
├── equations/       # 163+ equation modules (eq_*.tex)
├── figures/         # TikZ/pgfplots visualizations (fig_*.tex)
├── tables/          # Data tables (tab_*.tex, table_*.tex)
├── derivations/     # Multi-step mathematical proofs
├── algorithms/      # Computational procedures
└── narrative/       # Reusable text sections
```

## Module Types

### equations/
**Purpose:** One equation per file with full provenance

**Naming:** `eq_[framework]_[descriptor].tex`
- Examples: `eq_aether_scalar_wave.tex`, `eq_genesis_e8_projection.tex`

**Standard format:**
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

**Tag system:**
- Framework: A (Aether), G (Genesis), P (Pais), M (Math), U (Unified)
- Domain: QM, GR, EM, MATH, COSMO, EXP
- Status: T (Theoretical), E (Experimental), S (Speculative), V (Validated)

**Usage in chapters:**
```latex
\input{modules/equations/eq_aether_scalar_wave}
```

### figures/
**Purpose:** TikZ/pgfplots visualizations

**Naming:** `fig_[descriptor].tex`
- Examples: `fig_e8_roots_2d.tex`, `fig_scalar_field_potential.tex`

**Standard format:**
```latex
%==============================================================================
% Figure: [Descriptive name]
% Source: [Document/chapter]
% Purpose: [What this figure illustrates]
%==============================================================================
\begin{figure}[ht]
  \centering
  \begin{tikzpicture}
    % TikZ code here
  \end{tikzpicture}
  \caption{[Caption text]}
  \label{fig:descriptor}
\end{figure}
%==============================================================================
```

**Usage in chapters:**
```latex
\input{modules/figures/fig_e8_roots_2d}
```

### tables/
**Purpose:** Data tables with consistent formatting

**Naming:** `tab_[descriptor].tex` or `table_[descriptor].tex`

**Standard format:**
```latex
%==============================================================================
% Table: [Descriptive name]
% Source: [Data source or calculation]
%==============================================================================
\begin{table}[ht]
  \centering
  \begin{tabular}{lcc}
    \toprule
    Header1 & Header2 & Header3 \\
    \midrule
    Data1 & Data2 & Data3 \\
    \bottomrule
  \end{tabular}
  \caption{[Caption text]}
  \label{tab:descriptor}
\end{table}
%==============================================================================
```

### derivations/
**Purpose:** Multi-step mathematical proofs

**Format:** Detailed calculation steps with intermediate results.

### algorithms/
**Purpose:** Computational procedures (pseudocode or actual code)

**Format:** Algorithm environment or listings.

### narrative/
**Purpose:** Reusable text sections that appear in multiple chapters

**Usage:** Common introductions, standard disclaimers, framework descriptions.

## Creating New Modules

### New Equation Module

1. **Create file:**
```bash
cd ~/Playground/PhysicsForge
touch synthesis/modules/equations/eq_framework_descriptor.tex
```

2. **Add content:** Use standard format (see above)

3. **Include in chapter:**
```latex
% In synthesis/chapters/frameworks/ch07_aether.tex
\input{modules/equations/eq_framework_descriptor}
```

4. **Test compilation:**
```bash
cd ~/Playground/PhysicsForge
make latex
```

5. **Update catalog:**
```bash
cd ~/Playground/PhysicsForge
python scripts/build_catalog_pipeline.py --base-dir .
```

### New Figure Module

1. **Create file:**
```bash
cd ~/Playground/PhysicsForge
touch synthesis/modules/figures/fig_descriptor.tex
```

2. **Add TikZ/pgfplots code** with standard header

3. **Test standalone** (optional):
```latex
\documentclass{article}
\usepackage{tikz}
\begin{document}
\input{synthesis/modules/figures/fig_descriptor}
\end{document}
```

4. **Include in chapter** and test full build

### New Table Module

1. **Prepare data** (CSV or manual entry)

2. **Create file** with tabular environment

3. **Use booktabs** for professional appearance:
```latex
\toprule, \midrule, \bottomrule
```

4. **Include in chapter** and test

## Module Best Practices

### Equations
1. **One equation per file** - No exceptions
2. **Full provenance** - Document source file + line numbers
3. **Physical interpretation** - Explain what it means
4. **Unique labels** - Follow `eq:framework:descriptor` pattern
5. **Framework attribution** - Use `\eqtag{F}{D}{S}`

### Figures
1. **Standalone compilation** - Figure should work in isolation
2. **Relative sizing** - Use `\textwidth` not absolute measurements
3. **Consistent style** - Match colors/fonts to preamble definitions
4. **Descriptive captions** - Explain what's shown
5. **pgfplots version** - Respect `compat=1.18` in preamble

### Tables
1. **booktabs package** - Professional rules
2. **Numeric alignment** - Use `S` column type (siunitx)
3. **Units in headers** - Document units clearly
4. **Data source** - Document where data came from
5. **Significant figures** - Consistent precision

## Common Tasks

### Find an Equation Module
```bash
cd ~/Playground/PhysicsForge
grep -l "scalar.*wave" synthesis/modules/equations/*.tex
```

### Count Equation Modules
```bash
cd ~/Playground/PhysicsForge
ls synthesis/modules/equations/eq_*.tex | wc -l
```

### Check for Duplicate Labels
```bash
cd ~/Playground/PhysicsForge
grep -h "\\label{" synthesis/modules/equations/*.tex | sort | uniq -d
```

### List All Figures
```bash
cd ~/Playground/PhysicsForge
ls synthesis/modules/figures/fig_*.tex
```

### Verify Module is Used
```bash
cd ~/Playground/PhysicsForge
grep -r "eq_aether_scalar_wave" synthesis/chapters/
```

## Integration with Catalog System

Modules are tracked in the master equation catalog:
- **Location:** `/home/eirikr/Playground/PhysicsForge/equation_catalog.csv`
- **Generated by:** `python scripts/build_catalog_pipeline.py`

To update catalog after adding modules:
```bash
cd ~/Playground/PhysicsForge
python scripts/build_catalog_pipeline.py --base-dir .
python scripts/catalog_parity.py --base-dir .  # Check coverage
```

## Module Naming Conventions

### Equations
- **Framework prefix:** `eq_aether_`, `eq_genesis_`, `eq_pais_`, `eq_unified_`
- **Descriptor:** Short name (e.g., `scalar_wave`, `e8_projection`)
- **Auto-generated:** `eq_ae001_auto.tex` (from extraction)

### Figures
- **Descriptive:** `fig_e8_roots_2d.tex`, `fig_scalar_potential.tex`
- **Concept-based:** `fig_dimensional_folding.tex`

### Tables
- **Content-based:** `tab_scalar_constraints.tex`, `tab_notation_tensor.tex`

## Troubleshooting

### "File not found" when including module
**Cause:** Wrong path or file doesn't exist

**Check:**
```bash
ls synthesis/modules/equations/eq_framework_descriptor.tex
```

**Fix:** Verify filename and use correct path in `\input{}`

### Module compiles alone but not in document
**Cause:** Missing packages or conflicting macros

**Fix:**
1. Check preamble.tex for required packages
2. Verify no command redefinitions
3. Test in minimal document

### Duplicate label warnings
**Cause:** Same `\label{}` in multiple modules

**Fix:**
```bash
cd ~/Playground/PhysicsForge
grep -rn "label{eq:problematic:label}" synthesis/
# Rename one of them to make unique
```

### Figure positioning issues
**Cause:** Float placement parameters

**Fix:** Use `[ht]` or `[htbp]`, avoid `[h]` alone

## See Also

- `/home/eirikr/Playground/PhysicsForge/CLAUDE.md` - Project root guidelines
- `/home/eirikr/Playground/PhysicsForge/synthesis/CLAUDE.md` - LaTeX source guidelines
- `/home/eirikr/Playground/PhysicsForge/synthesis/preamble.tex` - Package definitions and macros
- `equation_catalog.csv` - Master catalog of all equations
