# PhysicsForge GitHub Actions Workflows

**Last Updated**: 2025-11-17
**Architecture Version**: 2.1 (Papers Build Added)

---

## Overview

The PhysicsForge CI/CD pipeline includes workflows for building research papers, validating code, and deploying documentation.

**Current Workflows**:
- **papers_build.yml** - Builds all 6 research papers (NEW)
- **release.yml** - Builds and publishes papers + monograph on release (UPDATED)
- **test.yml** - Tests and validation
- **performance.yml** - Performance monitoring
- **test-coverage.yml** - Code coverage
- Legacy workflows (disabled)

---

## Active Workflows

### 1. papers_build.yml - Build All Research Papers (NEW)

**Purpose**: Build all 6 PhysicsForge research papers on every commit to validate LaTeX compilation

**Triggers**:
- `push` to main branch (when paper files change)
- `pull_request` to main branch (when paper files change)  
- `workflow_dispatch` (manual)

**Papers Built**:
1. Paper 1: Scalar Field Theory and Zero-Point Energy
2. Paper 2: Exceptional Algebras and Crystalline Lattices
3. Paper 3: Fractal Geometry and Hyperdimensional Fields
4. Paper 4: Gravitational-EM Unification
5. Paper 5: Experimental Protocols for Exotic Quantum States
6. Paper 6: Applications to Quantum Computing and Energy Technologies

**Jobs**:
- **build-papers**: Matrix job building all 6 papers in parallel
  - Uses pdfLaTeX via xu-cheng/latex-action@v3
  - Caches TeX Live packages
  - Uploads each paper as individual artifact (30-day retention)
- **build-all-papers-summary**: Generates summary table of build results

**Key Features**:
- ✅ Parallel paper builds (6 papers built simultaneously)
- ✅ Individual paper artifacts for download
- ✅ TeX Live package caching
- ✅ Build status summary

**Artifact Flow**:
```
build-papers (matrix) → [paper1, paper2, paper3, paper4, paper5, paper6]
                        ↓
build-all-papers-summary → Downloads all → Generates summary
```

---

### 2. release.yml - Release All PDFs (UPDATED)

**Purpose**: Build and publish all papers and monograph when a GitHub Release is created

**Triggers**:
- `release:published` (when git tag is published)

**Jobs**:

#### build-papers
- **Matrix**: Builds all 6 papers in parallel
- Uses pdfLaTeX via xu-cheng/latex-action@v3
- Creates versioned PDFs (e.g., `PhysicsForge-Paper1-v1.0.0.pdf`)
- Uploads each paper as artifact

#### build-monograph
- Builds complete monograph (legacy document)
- **Primary Path**: Downloads PDF artifact from build.yml if available
- **Fallback Path**: Rebuilds PDF with LuaLaTeX if artifact unavailable
- Creates versioned monograph (e.g., `PhysicsForge-Monograph-v1.0.0.pdf`)

#### release-all-pdfs
- Downloads all paper and monograph artifacts
- Uploads all PDFs to the GitHub Release
- Generates release summary with file sizes

**Release Artifacts**:
- `PhysicsForge-Paper1-vX.Y.Z.pdf`
- `PhysicsForge-Paper2-vX.Y.Z.pdf`
- `PhysicsForge-Paper3-vX.Y.Z.pdf`
- `PhysicsForge-Paper4-vX.Y.Z.pdf`
- `PhysicsForge-Paper5-vX.Y.Z.pdf`
- `PhysicsForge-Paper6-vX.Y.Z.pdf`
- `PhysicsForge-Monograph-vX.Y.Z.pdf`

**Key Features**:
- ✅ All 7 PDFs attached to release
- ✅ Versioned filenames
- ✅ Parallel paper builds
- ✅ Artifact reuse for monograph (fast)
- ✅ Fallback rebuild for monograph (reliable)

---

### 3. test.yml - Test and Validate

**Purpose**: Quality gates for pull requests and commits

**Triggers**:
- `push` (all branches)
- `pull_request` (all branches)

**Jobs** (4):

#### test-python
- **Matrix**: 2 OS × 2 Python versions = 4 combinations
  - ubuntu-latest, windows-latest (macOS removed)
  - Python 3.11, 3.12
- Runs pytest with coverage
- Uploads coverage to Codecov
- Cache: Pip packages per OS/Python version

#### validate-code
- flake8 (syntax + complexity)
- mypy (type checking, non-blocking)
- ASCII guard (encoding validation)
- Metrics and plan schema validation
- Cache: Validation tool dependencies

#### validate-latex
- LaTeX compilation in strict mode
- WARNINGS_AS_ERRORS=1
- Uses synthesis/scripts/compile_strict.sh
- Cache: apt metadata + TeX Live user tree

#### validate-catalog
- Build equation catalog pipeline
- Validate catalog integrity
- Check coverage gaps
- Superforce validation (if exists)
- RG running plots (if exists)
- Cache: Scientific Python libraries

**Consolidation**:
- **From ci.yml (8 jobs)**: tests, windows_tests, ascii_guard, latex_strict → merged/removed
- **From test.yml (3 jobs)**: test, superforce_validation, equation_catalog → merged
- **Removed duplicates**: All report generation moved to build.yml

Note: python_tests.yml was consolidated into test.yml in Nov 2025

**Why Consolidated**:
- Testing and validation are distinct from building and deployment
- Eliminates double-testing on PRs
- Faster feedback loops (no report generation delays)
- Clear separation: test.yml validates code, build.yml generates artifacts

---

### 3. release.yml - Release PDF

**Purpose**: Attach versioned PDF to GitHub Releases

**Triggers**:
- `release:published` (when git tag is published)

**Jobs** (1):

#### build-and-release
- **Primary Path**: Downloads PDF artifact from build.yml run matching release tag
  - Fast: ~3-5 seconds download
  - Validates: file size > 0, existence check
- **Fallback Path**: Rebuilds PDF if artifact unavailable
  - Slow: ~2-3 minutes compilation
  - Safety: ensures release always has PDF
- Renames PDF with version tag (e.g., `PhysicsForge-v1.0.0.pdf`)
- Uploads both versioned and `main.pdf` to release

**Time Savings**: 85-90% reduction (2-3 min → 3-5 sec) when artifact reuse works

**Why Updated**:
- Original workflow rebuilt PDF from scratch (duplicate work)
- Risk of version drift (release PDF ≠ Pages PDF)
- Artifact reuse guarantees consistency

---

## Disabled Workflows (5)

| Workflow | Reason | Superseded By |
|----------|--------|---------------|
| ci.yml.disabled | Consolidated into test.yml | test.yml |
| test.yml.disabled | Consolidated into test.yml | test.yml |
| latex_build.yml.disabled | Legacy implementation | build.yml |
| main.yml.disabled | Prototype CI | test.yml |
| pages.yml.disabled | Manual deployment only | build.yml |

**Preservation**:
- Disabled workflows kept for historical reference
- Document evolution of CI/CD architecture
- Can be restored if specific feature needed

---

## Workflow Dependency Graph

```
push to main (paper files change)
├─ papers_build.yml
│  ├─ build-papers (matrix: 6 papers in parallel)
│  │  ├─ paper1_scalar_field_zpe → [paper1 artifact]
│  │  ├─ paper2_exceptional_algebras → [paper2 artifact]
│  │  ├─ paper3_fractal_geometry → [paper3 artifact]
│  │  ├─ paper4_em_gravity_unification → [paper4 artifact]
│  │  ├─ paper5_experimental_protocols → [paper5 artifact]
│  │  └─ paper6_applications → [paper6 artifact]
│  └─ build-all-papers-summary
│     └─ downloads all papers → generates summary

push to main
├─ build.yml
│  ├─ build-pdf (LuaLaTeX) → [pdf]
│  ├─ build-chapters (parallel) → [chapter-pdfs]
│  ├─ build-catalog (Python) → [catalog]
│  ├─ build-web (depends: build-pdf, build-catalog)
│  │  ├─ downloads: [pdf] + [catalog]
│  │  ├─ generates: SVG figures
│  │  └─ uploads: [github-pages]
│  └─ deploy (depends: build-pdf, build-web)
│     └─ deploys: GitHub Pages
│
└─ test.yml
   ├─ test-python (matrix: 4 combinations)
   ├─ validate-code (flake8, mypy, ASCII)
   ├─ validate-latex (strict mode)
   └─ validate-catalog (integrity, superforce)

release:published
└─ release.yml (UPDATED)
   ├─ build-papers (matrix: 6 papers)
   │  ├─ paper1 → PhysicsForge-Paper1-vX.Y.Z.pdf
   │  ├─ paper2 → PhysicsForge-Paper2-vX.Y.Z.pdf
   │  ├─ paper3 → PhysicsForge-Paper3-vX.Y.Z.pdf
   │  ├─ paper4 → PhysicsForge-Paper4-vX.Y.Z.pdf
   │  ├─ paper5 → PhysicsForge-Paper5-vX.Y.Z.pdf
   │  └─ paper6 → PhysicsForge-Paper6-vX.Y.Z.pdf
   ├─ build-monograph
   │  ├─ try: download artifact from build.yml
   │  ├─ fallback: rebuild PDF
   │  └─ output: PhysicsForge-Monograph-vX.Y.Z.pdf
   └─ release-all-pdfs
      ├─ downloads: all paper + monograph artifacts
      ├─ generates: release summary
      └─ uploads: all 7 PDFs to GitHub Release
```

---

## Caching Strategy

### TeXLive Packages (build.yml, papers_build.yml, release.yml)
- **Jobs**: build-pdf, build-chapters, build-papers (all workflows)
- **Key**: `${{ runner.os }}-texlive-papers-${{ hashFiles('synthesis/shared/**') }}`
- **Path**: `~/.texlive`, `~/.texmf-var`, `~/.cache/texmf`
- **Size**: ~500 MB
- **Invalidation**: When shared LaTeX infrastructure changes

### TeXLive SVG (build.yml)
- **Job**: build-web
- **Key**: `${{ runner.os }}-texlive-svg-${{ hashFiles('figures/tikz/*.tex') }}`
- **Path**: `/tmp/texlive`, `~/.texlive`
- **Invalidation**: When TikZ figure sources change

### Python Packages (build.yml, test.yml)
- **Jobs**: build-catalog, validate-catalog
- **Key**: `${{ runner.os }}-pip-${{ hashFiles('scripts/*.py') }}`
- **Path**: `~/.cache/pip`
- **Invalidation**: When Python scripts change

### Python Matrix (test.yml)
- **Job**: test-python
- **Key**: `${{ runner.os }}-${{ matrix.python-version }}-pip-${{ hashFiles('requirements*.txt') }}`
- **Fallback**: OS-level and generic pip caches
- **Invalidation**: When requirements or Python version changes

---

## Artifact Management

| Artifact | Produced By | Used By | Retention |
|----------|-------------|---------|-----------|
| paper1-paper6 | papers_build.yml, release.yml | - (download only) | 30 days / release |
| pdf | build-pdf | build-web, release.yml | 1 day |
| chapter-pdfs | build-chapters | - (download only) | 1 day |
| catalog | build-catalog | build-web | 7 days |
| github-pages | build-web | deploy | Per GH policy |
| build-logs | build-pdf (on failure) | - (debug) | 3 days |

**Retention Policy Rationale**:
- **1 day**: Temporary build artifacts (PDFs) - only needed for current deployment
- **3 days**: Debug logs - useful for recent failures
- **7 days**: Analysis artifacts (catalog) - useful across multiple builds
- **GitHub Pages**: Managed by GitHub Actions automatically

---

## Common Tasks

### Build All Papers Manually
```bash
gh workflow run papers_build.yml
```

### View Latest Papers Build Status
```bash
gh run list --workflow=papers_build.yml --limit 5
```

### Download Individual Paper
```bash
# Download specific paper
gh run download --name paper1_scalar_field_zpe

# Download all papers
gh run download --name paper1_scalar_field_zpe
gh run download --name paper2_exceptional_algebras
gh run download --name paper3_fractal_geometry
gh run download --name paper4_em_gravity_unification
gh run download --name paper5_experimental_protocols
gh run download --name paper6_applications
```

### Build Papers Locally
```bash
# Build individual papers
make paper1-new
make paper2
make paper3
make paper4
make paper5
make paper6

# Build all papers
make papers_all

# Clean build artifacts
make papers_clean
```

### Trigger Manual Build
```bash
gh workflow run build.yml
```

### View Latest Build Status
```bash
gh run list --workflow=build.yml --limit 5
```

### Download PDF from Latest Build
```bash
gh run download --name pdf
```

### Download Equation Catalog
```bash
gh run download --name catalog
```

### Trigger Release (creates tag, triggers release.yml)
```bash
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
gh release create v1.0.0 --title "Version 1.0.0" --notes "Release notes here"
```

### Debug Failed Build
```bash
# View failed run
gh run view <run-id>

# Download build logs
gh run download <run-id> --name build-logs
```

---

## Troubleshooting

### build.yml Fails with "PDF not found"

**Symptom**: "Check PDF exists and analyze warnings" step fails

**Diagnosis**:
```bash
gh run view <run-id> --log-failed | grep "PDF"
```

**Common Causes**:
1. LaTeX errors (not warnings) - check log for "! " errors
2. Missing package - check log for "File ... not found"
3. Syntax error in .tex files - check specific line in error message

**Fix**:
- Review build log artifact
- Fix LaTeX errors in synthesis/
- Test locally: `cd synthesis && pdflatex main.tex`

### test.yml Fails on "validate-latex"

**Symptom**: LaTeX strict mode fails

**Diagnosis**: This job treats warnings as errors

**Fix**:
- Review LaTeX warnings in log
- Fix warnings or adjust tolerance in compile_strict.sh
- Validate locally: `WARNINGS_AS_ERRORS=1 make latex`

### release.yml Uses Fallback (Slow)

**Symptom**: Release takes 2-3 minutes instead of 3-5 seconds

**Diagnosis**: Artifact download failed, rebuild triggered

**Common Causes**:
1. Release tag doesn't match recent build.yml run
2. Artifact expired (1-day retention)
3. build.yml failed on tagged commit

**Fix**:
- Ensure build.yml succeeds before creating release
- Create release within 24 hours of merge to main
- Manually trigger build.yml if needed: `gh workflow run build.yml`

### Workflow Not Triggering

**Check**:
```bash
# Verify workflow is active (not .disabled)
ls -la .github/workflows/*.yml

# Check recent runs
gh run list --workflow=<workflow-name> --limit 10
```

**Common Issues**:
- Workflow file has .disabled extension
- Trigger conditions don't match (e.g., wrong branch)
- Syntax error in YAML (check for tabs vs spaces)

---

## Performance Benchmarks

### Before Consolidation (7 workflows, 14 jobs)

**Typical PR**:
- ci.yml: 8 jobs, ~6-8 minutes
- test.yml: 3 jobs (matrix), ~4-6 minutes
- Total: ~8-12 minutes (some jobs parallel)
- Actions minutes consumed: ~40-60 min

Note: test.yml consolidated python_tests.yml and ci.yml workflows

**Typical Release**:
- build.yml: 3 jobs, ~3-4 minutes
- release.yml: 1 job (rebuild), ~2-3 minutes
- Total: ~5-7 minutes

### After Consolidation (3 workflows, 9 jobs)

**Typical PR**:
- test.yml: 4 jobs, ~5-7 minutes (caching helps)
- Total: ~5-7 minutes
- Actions minutes consumed: ~25-35 min

**Typical Release**:
- build.yml: 5 jobs, ~4-6 minutes (more jobs, but cached)
- release.yml: 1 job (artifact reuse), ~3-5 seconds
- Total: ~4-6 minutes

**Improvements**:
- PR time: 40% faster (8-12 min → 5-7 min)
- Release time: 30% faster (5-7 min → 4-6 min)
- Actions minutes: 40% reduction
- Duplicate work: eliminated

---

## Migration Notes

### From ci.yml → test.yml

**What changed**:
- Report generation jobs removed (moved to build.yml)
- macOS testing removed from matrix
- Python 3.10 removed from matrix
- Windows quick reports removed (duplicate)

**What stayed**:
- All validation jobs (code quality, LaTeX, catalog)
- Test coverage with Codecov
- ASCII enforcement

### From test.yml → test.yml (Consolidated)

**What changed** (consolidation of python_tests.yml):
- macOS removed from matrix (OS: 3 → 2)
- Matrix testing consolidated with ci.yml tests

**What stayed**:
- Python version matrix (3.11, 3.12)
- Superforce validation
- Equation catalog validation

Note: python_tests.yml was consolidated into test.yml in Nov 2025

### From latex_build.yml.disabled → build.yml

**Restored features**:
- ✅ Individual chapter compilation (build-chapters job)
- ✅ Equation catalog generation (build-catalog job)
- ✅ Custom landing page (build-web creates index.html)

**Improvements**:
- Docker-based LaTeX (xu-cheng/latex-action@v4) instead of apt-get
- LuaLaTeX instead of pdfLaTeX (better Unicode support)
- Triple caching layer (TeXLive, Python, SVG)
- Intelligent error handling (warnings vs errors)

---

## Future Enhancements

**Potential Additions** (not currently implemented):

1. **Incremental Builds**
   - Cache LaTeX auxiliary files (.aux, .toc, .bbl)
   - Only recompile changed chapters
   - Significant speed improvements for large documents

2. **Preview Deployments**
   - Deploy PR previews to separate GitHub Pages URLs
   - Useful for reviewing changes before merge

3. **Notification System**
   - Slack/Discord notifications on build failures
   - Email digest of weekly build statistics

4. **Security Scanning**
   - Dependabot for GitHub Actions versions
   - CodeQL analysis for Python scripts

5. **Performance Monitoring**
   - Track build time trends over time
   - Alert on performance regressions

---

## References

- **docs/WORKFLOWS.md**: Comprehensive documentation for paper build workflows
- **WORKFLOW_ANALYSIS.md**: Detailed analysis of consolidation rationale
- **GitHub Actions Documentation**: https://docs.github.com/en/actions
- **xu-cheng/latex-action**: https://github.com/xu-cheng/latex-action
- **actions/cache**: https://github.com/actions/cache
- **PhysicsForge Documentation**: /docs/

---

**Questions or Issues?**
- Check troubleshooting section above
- Review workflow run logs: `gh run list`
- See docs/WORKFLOWS.md for paper build documentation
- Consult WORKFLOW_ANALYSIS.md for historical context
- Open GitHub issue with workflow run ID and error details
