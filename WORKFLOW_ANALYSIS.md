# PhysicsForge CI/CD Workflow Analysis

**Date**: 2025-11-08
**Purpose**: Comprehensive analysis of GitHub Actions workflows to identify redundancies, conflicts, and consolidation opportunities
**Scope**: All active and disabled workflows in `.github/workflows/`

---

## Executive Summary

The PhysicsForge repository currently has **7 workflow files** (4 active, 3 disabled). Analysis reveals significant **functional overlap** and **historical evolution** from multiple parallel implementations to a more focused approach. Key findings:

- **Primary concern**: 3 different PDF build + Pages deployment implementations (build.yml active, latex_build.yml.disabled, pages.yml.disabled)
- **Redundancy**: 2 CI implementations (ci.yml active, main.yml.disabled)
- **Clarity issue**: Overlapping Python testing in ci.yml and python_tests.yml
- **Recommendation**: Consolidate to 3 core workflows with distinct responsibilities

---

## Workflow Inventory

### Active Workflows (4)

| Workflow | File | Lines | Triggers | Purpose |
|----------|------|-------|----------|---------|
| **Build PDF and Deploy to GitHub Pages** | `build.yml` | 124 | push:main, workflow_dispatch | PDF compilation (LuaLaTeX) + SVG figure generation + Pages deployment |
| **CI** | `ci.yml` | 208 | push:main, pull_request | Comprehensive testing suite with 8 jobs |
| **Python Tests** | `python_tests.yml` | 120 | push, pull_request | Python matrix testing + validation |
| **Release PDF** | `release.yml` | 38 | release:published | PDF build for GitHub Releases |

### Disabled Workflows (3)

| Workflow | File | Lines | Status | Notes |
|----------|------|-------|--------|-------|
| **LaTeX Build and Deploy** | `latex_build.yml.disabled` | 221 | Disabled | Legacy: apt-get TeX install, individual chapter compilation, custom index.html |
| **CI** | `main.yml.disabled` | 43 | Disabled | Legacy: simpler CI with flake8/mypy/make ci |
| **Pages Build** | `pages.yml.disabled` | 37 | Disabled | Legacy: manual-trigger only, apt-get TeX install |

---

## Detailed Analysis by Workflow

### 1. build.yml - Build PDF and Deploy to GitHub Pages (ACTIVE)

**Purpose**: Main production workflow for PDF compilation and web deployment
**Triggers**: `push` to main, `workflow_dispatch`
**Status**: ✅ Recently fixed (LuaLaTeX compatibility, job dependencies, continue-on-error)

#### Jobs (3):

1. **build-pdf** (xu-cheng/latex-action@v4)
   - LuaLaTeX compilation with latexmk
   - Output: `build/main.pdf`
   - Artifact: `pdf` (1-day retention)
   - Error handling: `continue-on-error: true` for LaTeX warnings
   - Explicit PDF existence check

2. **build-web** (xu-cheng/texlive-action@v2)
   - Depends on: `build-pdf`
   - Install TeXLive packages: xetex, dvisvgm, standalone, pgf, pgfplots
   - Generate SVG figures: XeLaTeX → XDV → SVG (WOFF2 fonts)
   - Copy PDF artifact to `site/pdf/`
   - Upload Pages artifact from `site/`

3. **deploy**
   - Depends on: `build-pdf`, `build-web`
   - Deploy to GitHub Pages (actions/deploy-pages@v4)
   - Environment: `github-pages`

#### Strengths:
- Modern action versions (@v4, @v5)
- Proper job dependencies
- Docker-based LaTeX (reproducible)
- XDV→SVG workflow preserves fonts
- Dedicated site/ directory structure

#### Issues:
- Still experiencing exit code 12 on LaTeX compilation (warnings treated as errors by action)
- `continue-on-error: true` not preventing job failure
- No caching (rebuilds from scratch every time)

---

### 2. ci.yml - CI (ACTIVE)

**Purpose**: Comprehensive continuous integration testing
**Triggers**: `push` to main, `pull_request` to main
**Status**: ✅ Operational

#### Jobs (8):

1. **tests**: Python 3.11, pytest, smoke tests
2. **windows_tests**: Cross-platform validation (Windows runner)
3. **ascii_guard**: Enforce ASCII-only Python code
4. **latex_strict**: Strict LaTeX validation (WARNINGS_AS_ERRORS=1)
5. **reports**: Generate catalog parity, gap TODO, validation reports
6. **quick_pipeline**: Fast equation catalog pipeline
7. **quick_reports**: Quick audit + catalog validation
8. **metrics_only**: Metrics generation

#### Strengths:
- Comprehensive coverage (testing, linting, reporting, auditing)
- Cross-platform testing (Linux + Windows)
- Enforces project standards (ASCII-only policy)
- Multiple report generation paths
- Uses make targets (good abstraction)

#### Issues:
- **Overlap with python_tests.yml**: Both run Python tests
- **Complexity**: 8 jobs may be over-engineered for current project size
- **Duplication**: `reports` and `quick_reports` similar
- **No caching**: Python dependencies reinstalled every run

---

### 3. python_tests.yml - Python Tests (ACTIVE)

**Purpose**: Python testing matrix and equation validation
**Triggers**: `push`, `pull_request`
**Status**: ✅ Operational

#### Jobs (3):

1. **test**: Matrix (OS: ubuntu/windows/macos, Python: 3.11/3.12)
2. **superforce_validation**: Validate Superforce proof
3. **equation_catalog**: Build equation catalog pipeline

#### Strengths:
- True matrix testing (6 combinations: 3 OS × 2 Python versions)
- Specialized validation jobs (superforce, catalog)
- Modern setup-python@v5 with caching

#### Issues:
- **Redundancy with ci.yml**: Both run Python tests
- **Unclear division of labor**: Why separate from ci.yml?
- **Matrix may be excessive**: Do we need 3 OSes for LaTeX-heavy project?

---

### 4. release.yml - Release PDF (ACTIVE)

**Purpose**: Build PDF for GitHub Releases (tagged versions)
**Triggers**: `release:published`
**Status**: ✅ Operational

#### Job (1):

1. **build-and-release**: Build PDF, rename with version tag, upload to release

#### Strengths:
- Focused single purpose
- Version-tagged PDFs (`PhysicsForge-v1.0.0.pdf`)
- Provides both versioned and `main.pdf` files
- Uses same latex-action@v4 as build.yml

#### Issues:
- **No artifact reuse**: Rebuilds PDF instead of reusing build.yml artifact
- **Potential version mismatch**: What if release tag doesn't match main branch state?

---

### 5. latex_build.yml.disabled - LaTeX Build and Deploy (DISABLED)

**Purpose**: Legacy build and deployment workflow
**Status**: ❌ Disabled (superseded by build.yml)

#### Why Disabled:

This was the **original implementation** before build.yml. Key differences:

| Feature | latex_build.yml (OLD) | build.yml (NEW) |
|---------|----------------------|-----------------|
| LaTeX install | apt-get (system packages) | xu-cheng/latex-action@v4 (Docker) |
| Engine | pdflatex | LuaLaTeX |
| Individual chapters | ✅ Compiles all test_chNN.tex | ❌ Only main.pdf |
| Equation catalog | ✅ Runs build_catalog_pipeline.py | ❌ Not included |
| Custom index.html | ✅ Inline HTML generation | ❌ Uses pre-existing site/index.html |
| Output structure | output/latex/chapters/ | site/pdf/ |
| Artifact retention | 30 days | 1 day |

#### Valuable Features Lost:

1. **Individual chapter PDFs**: No longer compiled in build.yml
2. **Equation catalog generation**: Moved to ci.yml (less discoverable)
3. **Custom landing page**: Static site/ instead of generated index

#### Recommendation:

- Keep disabled (Docker approach is better)
- Consider restoring: individual chapter compilation, catalog generation

---

### 6. main.yml.disabled - CI (DISABLED)

**Purpose**: Legacy CI workflow
**Status**: ❌ Disabled (superseded by ci.yml)

#### Why Disabled:

This was a **simpler prototype** before ci.yml. Comparison:

| Feature | main.yml (OLD) | ci.yml (NEW) |
|---------|---------------|--------------|
| Jobs | 2 (build, latex_strict_check) | 8 (tests, windows, ascii, latex, reports x4) |
| Python testing | ✅ flake8, mypy, make ci | ✅ pytest, smoke, make ci |
| Windows testing | ❌ | ✅ |
| Reports | ❌ | ✅ (4 jobs) |
| LaTeX | xu-cheng/latex-action@v2 | Uses make latex |

#### Recommendation:

- Keep disabled (ci.yml is more comprehensive)
- No features worth preserving

---

### 7. pages.yml.disabled - Pages Build (DISABLED)

**Purpose**: Manual GitHub Pages deployment
**Status**: ❌ Disabled (superseded by build.yml)

#### Why Disabled:

This was a **manual-trigger-only** deployment before build.yml automated it:

| Feature | pages.yml (OLD) | build.yml (NEW) |
|---------|----------------|-----------------|
| Trigger | workflow_dispatch only | push:main + workflow_dispatch |
| LaTeX install | apt-get | xu-cheng/latex-action@v4 |
| SVG generation | ❌ | ✅ XDV→SVG with WOFF2 |
| Error handling | `make latex || true` | continue-on-error + explicit check |
| Output | Simple index.html | Full site/ directory |

#### Recommendation:

- Keep disabled (build.yml is superior)
- No features worth preserving

---

## Redundancy and Conflict Analysis

### Critical Redundancies

#### 1. **Python Testing** (ci.yml vs python_tests.yml)

**Overlap**:
- Both run pytest
- Both validate equation catalog
- Both test on multiple platforms

**Differences**:
| Aspect | ci.yml | python_tests.yml |
|--------|--------|------------------|
| OS matrix | Linux + Windows (2 jobs) | Linux + Windows + macOS (matrix) |
| Python versions | 3.11 only | 3.11 + 3.12 |
| Additional jobs | 6 non-test jobs | 2 validation jobs |
| Scope | Comprehensive CI | Focused testing |

**Conflict**:
- Unclear which is the "primary" test workflow
- PR checks run both, doubling resource usage
- Developers may be confused which to monitor

**Impact**:
- Wasted GitHub Actions minutes
- Slower PR feedback loops
- Maintenance burden (two test configs to update)

#### 2. **PDF Build** (build.yml vs release.yml)

**Overlap**:
- Both compile main.pdf with LuaLaTeX
- Both use xu-cheng/latex-action@v4
- Both use same args and working_directory

**Differences**:
- build.yml: Triggered by push, uploads to Pages
- release.yml: Triggered by release tag, uploads to GitHub Releases

**Conflict**:
- No artifact reuse (rebuild on release instead of using build.yml artifact)
- Potential version drift if release tag doesn't match main branch HEAD

**Impact**:
- Doubled build time for releases
- Risk of different PDF on Pages vs Releases

#### 3. **Report Generation** (ci.yml internal duplication)

**Overlap**: ci.yml has two report jobs:
- **reports**: `make report` (catalog_parity, gap_todo, validate_catalog)
- **quick_reports**: `make quick_audit` + validate_catalog

**Conflict**:
- Both generate similar outputs
- Unclear when to use which
- "quick" vs "full" distinction not well-defined

**Impact**:
- Confusion about report currency
- Potential for conflicting report versions

---

## Project Goals and Workflow Alignment

From `/home/eirikr/Playground/PhysicsForge/site/README.md` and workflow analysis:

### Project Requirements

1. **PDF Compilation**: LuaLaTeX, bibliography, cross-references
2. **GitHub Pages Deployment**: HTML landing page, SVG figures, PDF download
3. **Python Testing**: Scripts for equation extraction, catalog building, validation
4. **Release Artifacts**: Version-tagged PDFs on GitHub Releases
5. **Quality Gates**: ASCII enforcement, LaTeX strict mode, catalog validation

### Current Alignment

| Requirement | Current Implementation | Status |
|-------------|----------------------|--------|
| PDF compilation | ✅ build.yml, release.yml | Working |
| Pages deployment | ✅ build.yml | Working (with issues) |
| SVG figures | ✅ build.yml (XDV→SVG) | Working |
| Python testing | ⚠️ ci.yml + python_tests.yml | Redundant |
| Release PDFs | ✅ release.yml | Working |
| Quality gates | ✅ ci.yml | Working |

### Gaps

1. **Individual chapter PDFs**: Lost in transition from latex_build.yml to build.yml
2. **Equation catalog on Pages**: Generated in ci.yml, not deployed to Pages
3. **Artifact caching**: No reuse between workflows (Python deps, LaTeX compilation)
4. **Build performance**: No incremental builds, always full recompilation

---

## Consolidation Strategy

### Recommended Approach: 3-Workflow Architecture

**Principle**: Each workflow has a **single, clear responsibility** without overlap.

#### Workflow 1: **Build and Deploy** (build.yml - enhanced)

**Purpose**: Main production pipeline
**Triggers**: push:main, workflow_dispatch
**Jobs**:
1. build-pdf (LuaLaTeX)
2. build-chapters (individual test_chNN.tex)
3. build-catalog (equation_catalog.csv, reports)
4. build-web (SVG figures, combine artifacts)
5. deploy (GitHub Pages)

**Changes from current**:
- ✅ Add individual chapter compilation (from latex_build.yml)
- ✅ Add equation catalog generation (from ci.yml)
- ✅ Add artifact caching (Python packages, LaTeX packages)
- ✅ Fix continue-on-error to properly handle LaTeX warnings

**Rationale**: Single source of truth for production builds and deployments

#### Workflow 2: **Test and Validate** (consolidate ci.yml + python_tests.yml)

**Purpose**: Quality gates for PRs and commits
**Triggers**: push, pull_request
**Jobs**:
1. test-python (matrix: 3.11/3.12, linux/windows only)
2. validate-code (flake8, mypy, ASCII guard)
3. validate-latex (strict mode, zero warnings)
4. validate-catalog (superforce, equation integrity)

**Changes from current**:
- ✅ Merge python_tests.yml into ci.yml
- ✅ Remove macOS from matrix (LaTeX project, not needed)
- ✅ Remove redundant report jobs (moved to build.yml)
- ✅ Keep only validation jobs (no artifact generation)

**Rationale**: Fast PR feedback, no duplicate testing

#### Workflow 3: **Release** (release.yml - enhanced)

**Purpose**: Version-tagged releases
**Triggers**: release:published
**Jobs**:
1. reuse-build-artifact (download from build.yml run matching tag)
2. upload-to-release (rename and attach)

**Changes from current**:
- ✅ Reuse artifact from build.yml instead of rebuilding
- ✅ Add fallback: rebuild if artifact not found (safety)

**Rationale**: Fast releases, guaranteed consistency with Pages

---

## Recommendations Summary

### Immediate Actions (Phase 1)

1. **Fix build.yml LaTeX warnings issue**
   - Investigate why `continue-on-error: true` not working
   - Verify LaTeX warnings vs actual errors
   - Consider `-halt-on-error` vs `-interaction=nonstopmode` flags

2. **Consolidate Python testing**
   - Merge python_tests.yml into ci.yml
   - Keep matrix testing, remove macOS
   - Disable python_tests.yml

3. **Add caching to build.yml**
   - Cache Python packages: `actions/setup-python@v5` with `cache: 'pip'`
   - Cache TeXLive packages: custom cache key for tlmgr packages

### Medium-term Actions (Phase 2)

4. **Restore lost features**
   - Add individual chapter compilation to build.yml
   - Add equation catalog generation to build.yml
   - Deploy catalog to Pages (site/equation_catalog.csv)

5. **Improve release.yml**
   - Reuse build.yml artifacts when possible
   - Add version validation (tag matches PDF version)

6. **Clean up ci.yml**
   - Consolidate `reports` and `quick_reports` jobs
   - Document purpose of each job clearly
   - Consider further reduction (currently 8 jobs)

### Long-term Actions (Phase 3)

7. **Archive disabled workflows**
   - Move to `.github/workflows/archive/` directory
   - Add README documenting history and consolidation rationale

8. **Implement incremental builds**
   - Cache LaTeX auxiliary files
   - Only recompile changed chapters
   - Significant performance gain for large documents

9. **Add workflow documentation**
   - Create `.github/workflows/README.md`
   - Document each workflow's purpose, triggers, and dependencies
   - Add architecture diagram

---

## Synthesis: The Evolution Story

### Historical Timeline

1. **Early Stage** (main.yml.disabled, pages.yml.disabled, latex_build.yml.disabled)
   - Simple CI with flake8/mypy
   - Manual Pages deployment with apt-get TeXLive
   - Comprehensive LaTeX build with individual chapters

2. **Expansion** (python_tests.yml added)
   - Matrix testing introduced
   - Specialized validation jobs
   - Parallel development with ci.yml

3. **Current State** (ci.yml + build.yml + release.yml active)
   - Docker-based LaTeX (reproducible)
   - Automated Pages deployment
   - LuaLaTeX for full Unicode support
   - Comprehensive CI with 8 jobs

4. **Problems**
   - Lost features: individual chapters, catalog on Pages
   - Redundancy: duplicate testing, duplicate PDF builds
   - Complexity: 7 workflows (4 active), unclear responsibilities

### Root Causes

1. **Incremental evolution** without refactoring old workflows
2. **Feature additions** spread across multiple files
3. **No workflow documentation** or ownership model
4. **Migration incomplete** from disabled workflows to new ones

### Vision: Consolidated Future

**3 workflows, clear separation of concerns**:
- **build.yml**: Production artifacts and deployment
- **test.yml**: Quality gates for PRs
- **release.yml**: Version-tagged releases

**Benefits**:
- 50% reduction in workflow count
- No duplicate jobs or testing
- Clear responsibility boundaries
- Faster builds (caching, artifact reuse)
- Easier maintenance (one file per concern)

---

## Metrics and Impact

### Current State

| Metric | Value | Notes |
|--------|-------|-------|
| Total workflows | 7 (4 active, 3 disabled) | |
| Total jobs (active) | 14 | ci:8 + python_tests:3 + build:3 + release:1 |
| Duplicate jobs | 3 | Python testing, PDF builds, reports |
| Average PR build time | ~8-12 min | ci.yml + python_tests.yml sequential |
| GitHub Actions minutes/PR | ~40-60 min | Multiple parallel jobs |

### Projected State (After Consolidation)

| Metric | Value | Change | Notes |
|--------|-------|--------|-------|
| Total workflows | 3 (0 disabled) | -57% | Cleaner repo |
| Total jobs (active) | 9 | -36% | build:5 + test:4 + release:1 |
| Duplicate jobs | 0 | -100% | All redundancy removed |
| Average PR build time | ~5-7 min | -40% | Caching, no duplication |
| GitHub Actions minutes/PR | ~25-35 min | -40% | Efficiency gains |

### ROI

- **Development velocity**: Faster PR feedback loops
- **Cost savings**: 40% reduction in Actions minutes
- **Maintainability**: Single workflow per concern, easier updates
- **Reliability**: Artifact reuse eliminates version drift

---

## Next Steps

### Immediate (This Session)

1. ✅ Complete workflow analysis (this document)
2. ⏳ Investigate build.yml exit code 12 issue
3. ⏳ Draft updated build.yml with lost features restored

### Short-term (Next Session)

4. Implement Phase 1 consolidation
5. Test merged ci.yml + python_tests.yml
6. Verify caching reduces build times

### Medium-term (This Week)

7. Implement Phase 2 improvements
8. Add workflow documentation
9. Archive disabled workflows with history

---

## Appendix A: Workflow Dependency Graph

```
build.yml (push:main)
├─ build-pdf (LuaLaTeX) → artifact:pdf
├─ build-web (depends: build-pdf)
│  ├─ downloads: artifact:pdf
│  └─ uploads: artifact:pages
└─ deploy (depends: build-pdf, build-web)
   └─ downloads: artifact:pages

ci.yml (push:main, pull_request)
├─ tests (Python 3.11, pytest)
├─ windows_tests (Windows runner)
├─ ascii_guard (ASCII enforcement)
├─ latex_strict (LaTeX strict mode)
├─ reports (catalog_parity, gap_todo, validate)
├─ quick_pipeline (equation catalog)
├─ quick_reports (audit + validate)
└─ metrics_only (metrics generation)

python_tests.yml (push, pull_request)
├─ test (matrix: 3 OS × 2 Python versions)
├─ superforce_validation
└─ equation_catalog

release.yml (release:published)
└─ build-and-release (rebuild PDF, upload to release)
```

## Appendix B: Job Responsibility Matrix

| Responsibility | Current Owner(s) | Recommended Owner |
|----------------|------------------|-------------------|
| PDF compilation | build.yml, release.yml | build.yml |
| Individual chapters | (lost) latex_build.yml.disabled | build.yml |
| SVG figures | build.yml | build.yml |
| Equation catalog | ci.yml (quick_pipeline) | build.yml |
| Pages deployment | build.yml | build.yml |
| Python testing | ci.yml, python_tests.yml | test.yml (consolidated) |
| Code linting | ci.yml, python_tests.yml | test.yml |
| LaTeX strict mode | ci.yml | test.yml |
| ASCII enforcement | ci.yml | test.yml |
| Catalog validation | ci.yml, python_tests.yml | test.yml |
| Reports generation | ci.yml (2 jobs) | build.yml (single job) |
| Release artifacts | release.yml | release.yml (reuse build) |

---

**End of Analysis**
