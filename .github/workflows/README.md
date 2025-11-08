# PhysicsForge GitHub Actions Workflows

**Last Updated**: 2025-11-08
**Architecture Version**: 2.0 (Consolidated)

---

## Overview

The PhysicsForge CI/CD pipeline has been **consolidated from 7 workflows to 3 focused workflows**, eliminating redundancy and improving efficiency.

**Key Metrics**:
- Workflows: 7 → 3 (57% reduction)
- Total jobs: 14 → 9 (36% reduction)
- PR build time: ~8-12 min → ~5-7 min (40% faster)
- GitHub Actions minutes/PR: ~40-60 min → ~25-35 min (40% reduction)

---

## Active Workflows (3)

### 1. build.yml - Build PDF and Deploy to GitHub Pages

**Purpose**: Production pipeline for PDF compilation, web assets, and GitHub Pages deployment

**Triggers**:
- `push` to main branch
- `workflow_dispatch` (manual)

**Jobs** (5):

#### build-pdf
- Compiles main.pdf with LuaLaTeX
- Handles expected LaTeX warnings (up to 200)
- Output: `build/main.pdf`
- Artifact: `pdf` (1-day retention)
- Cache: TeXLive packages (~500 MB)

#### build-chapters (NEW)
- Matrix compilation of individual chapters (Ch01-30)
- Parallel execution for speed
- Output: `test_chNN.pdf` for each chapter
- Artifact: `chapter-pdfs` (1-day retention)
- Useful for: Testing individual chapters, debugging LaTeX issues

#### build-catalog (NEW)
- Runs equation catalog pipeline
- Generates 7 analysis reports:
  - equation_catalog.csv
  - equation_summary.txt
  - notation_conflicts.txt
  - top_equations.txt
  - CATALOG_PARITY.md
  - CATALOG_GAPS_TODO.md
  - VALIDATION_REPORT.md
- Artifact: `catalog` (7-day retention)
- Cache: Python packages

#### build-web
- Generates SVG figures (XDV→SVG with WOFF2 fonts)
- Downloads PDF and catalog artifacts
- Combines into site/ directory structure
- Creates landing page index.html
- Artifact: `github-pages` (deployment)

#### deploy
- Deploys to GitHub Pages
- Environment: github-pages
- URL: Published in deployment output

**Key Features**:
- ✅ Intelligent LaTeX error handling (warnings allowed, errors caught)
- ✅ Triple caching layer (TeXLive, Python, figures)
- ✅ Individual chapter compilation (lost feature restored)
- ✅ Equation catalog deployed to Pages (lost feature restored)
- ✅ Comprehensive build logs on failure

**Artifact Flow**:
```
build-pdf → [pdf artifact]
             ↓
build-chapters → [chapter-pdfs artifact]
                  ↓
build-catalog → [catalog artifact]
                 ↓
build-web → [github-pages artifact] (downloads: pdf + catalog)
            ↓
deploy → GitHub Pages
```

---

### 2. test.yml - Test and Validate (NEW - Consolidated)

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
- **From python_tests.yml (3 jobs)**: test, superforce_validation, equation_catalog → merged
- **Removed duplicates**: All report generation moved to build.yml

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
| python_tests.yml.disabled | Consolidated into test.yml | test.yml |
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
└─ release.yml
   └─ build-and-release
      ├─ try: download artifact from build.yml
      ├─ fallback: rebuild PDF
      └─ upload: versioned + main.pdf to release
```

---

## Caching Strategy

### TeXLive Packages (build.yml)
- **Jobs**: build-pdf, build-chapters
- **Key**: `${{ runner.os }}-texlive-${{ hashFiles('synthesis/main.tex', 'synthesis/preamble.tex') }}`
- **Path**: `/tmp/texlive`, `~/.texlive`
- **Size**: ~500 MB
- **Invalidation**: When main.tex or preamble.tex changes

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
- python_tests.yml: 3 jobs (matrix), ~4-6 minutes
- Total: ~8-12 minutes (some jobs parallel)
- Actions minutes consumed: ~40-60 min

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

### From python_tests.yml → test.yml

**What changed**:
- macOS removed from matrix (OS: 3 → 2)
- Matrix testing consolidated with ci.yml tests

**What stayed**:
- Python version matrix (3.11, 3.12)
- Superforce validation
- Equation catalog validation

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

- **WORKFLOW_ANALYSIS.md**: Detailed analysis of consolidation rationale
- **GitHub Actions Documentation**: https://docs.github.com/en/actions
- **xu-cheng/latex-action**: https://github.com/xu-cheng/latex-action
- **actions/cache**: https://github.com/actions/cache
- **PhysicsForge Documentation**: /docs/

---

**Questions or Issues?**
- Check troubleshooting section above
- Review workflow run logs: `gh run list`
- Consult WORKFLOW_ANALYSIS.md for historical context
- Open GitHub issue with workflow run ID and error details
