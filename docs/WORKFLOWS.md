# PhysicsForge Paper Build Workflows

This document describes the GitHub Actions workflows for building and releasing the PhysicsForge papers.

## Overview

PhysicsForge produces **six research papers** plus a complete monograph. The workflows automate the LaTeX compilation and distribution of these documents.

## Papers

1. **Paper 1**: Scalar Field Theory and Zero-Point Energy Coupling
2. **Paper 2**: Exceptional Algebras and Crystalline Lattice Structures
3. **Paper 3**: Fractal Geometry and Hyperdimensional Field Structures
4. **Paper 4**: Gravitational-Electromagnetic Unification via Scalar Intermediaries
5. **Paper 5**: Experimental Protocols for Exotic Quantum States
6. **Paper 6**: Applications to Quantum Computing and Energy Technologies

## Workflows

### 1. Papers Build Workflow (`papers_build.yml`)

**Triggers:**
- Push to `main` branch (when paper files change)
- Pull requests to `main` branch (when paper files change)
- Manual trigger via `workflow_dispatch`

**Purpose:**
- Builds all 6 papers on every relevant commit
- Validates that papers compile successfully
- Uploads PDFs as workflow artifacts (retained for 30 days)

**Matrix Strategy:**
The workflow uses a matrix strategy to build all papers in parallel, significantly reducing build time.

**Artifacts:**
- `paper1_scalar_field_zpe.pdf`
- `paper2_exceptional_algebras.pdf`
- `paper3_fractal_geometry.pdf`
- `paper4_em_gravity_unification.pdf`
- `paper5_experimental_protocols.pdf`
- `paper6_applications.pdf`

### 2. Release Workflow (`release.yml`)

**Triggers:**
- GitHub Release is published

**Purpose:**
- Builds all 6 papers with versioned filenames
- Builds the complete monograph (legacy document)
- Attaches all PDFs to the GitHub Release

**Jobs:**

1. **build-papers**: Builds each of the 6 papers in parallel
2. **build-monograph**: Builds the complete monograph document
3. **release-all-pdfs**: Collects all PDFs and uploads them to the release

**Release Artifacts:**
- `PhysicsForge-Paper1-vX.Y.Z.pdf`
- `PhysicsForge-Paper2-vX.Y.Z.pdf`
- `PhysicsForge-Paper3-vX.Y.Z.pdf`
- `PhysicsForge-Paper4-vX.Y.Z.pdf`
- `PhysicsForge-Paper5-vX.Y.Z.pdf`
- `PhysicsForge-Paper6-vX.Y.Z.pdf`
- `PhysicsForge-Monograph-vX.Y.Z.pdf`

## LaTeX Compilation

All papers are compiled using:
- **Tool**: `xu-cheng/latex-action@v3`
- **Engine**: pdfLaTeX (via latexmk)
- **Mode**: Non-interactive with error halting
- **Shell escape**: Enabled (for TikZ and other packages)

## Caching

Both workflows implement TeX Live package caching to speed up subsequent builds:
- Cache key based on shared LaTeX infrastructure
- Significantly reduces build time after first run

## Local Building

To build papers locally, use the Makefile:

```bash
# Build individual papers
make paper1-new  # Paper 1: Scalar Field Theory
make paper2      # Paper 2: Exceptional Algebras
make paper3      # Paper 3: Fractal Geometry
make paper4      # Paper 4: EM-Gravity Unification
make paper5      # Paper 5: Experimental Protocols
make paper6      # Paper 6: Applications

# Build all papers
make papers_all

# Clean build artifacts
make papers_clean
```

## File Locations

- **Source Files**: `synthesis/papers/paper{1-6}_*/paper{1-6}_main.tex`
- **Shared Infrastructure**: `synthesis/shared/`
  - `common_preamble.tex`
  - `common_macros.tex`
  - `marginal_notes_system.tex`
  - `glossary.tex`
  - `notation.tex`
  - `bibliography_shared.bib`
- **Build Outputs**: `synthesis/build/` (local builds)

## Creating a Release

To create a new release with all papers:

1. Ensure all changes are committed and pushed to `main`
2. Create a new tag: `git tag -a vX.Y.Z -m "Release vX.Y.Z"`
3. Push the tag: `git push origin vX.Y.Z`
4. Go to GitHub → Releases → Draft a new release
5. Select the tag you just created
6. Add release notes
7. Click "Publish release"

The workflow will automatically build all papers and attach them to the release.

## Troubleshooting

### Paper Build Fails

1. Check the workflow logs for LaTeX errors
2. Look for undefined references, missing packages, or syntax errors
3. Test locally: `cd synthesis/papers/paper{N}_*/ && pdflatex paper{N}_main.tex`

### Missing Dependencies

If a LaTeX package is missing, it will be automatically installed by the `latex-action`. However, very obscure packages might need to be added to the TeX Live installation step.

### Artifacts Not Appearing

- Workflow artifacts are retained for 30 days
- Release artifacts are permanent (attached to the release)
- Check that the workflow completed successfully

## Continuous Integration

The papers build workflow integrates with PhysicsForge's CI system:
- Validates LaTeX compilation on every change
- Prevents broken papers from being merged
- Provides early feedback to contributors

## Future Enhancements

Potential improvements to consider:
- PDF metadata injection (title, author, keywords)
- Automatic changelog generation from commits
- Cross-reference validation between papers
- Build time optimization
- Conditional builds (only build changed papers)
