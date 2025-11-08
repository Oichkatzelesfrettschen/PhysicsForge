# PhysicsForge CI/CD Bug Fix Plan

**Date**: 2025-11-08
**Status**: Planning complete, ready for parallel agent deployment

---

## Issues Identified by Quality Gates

### Issue 1: build-catalog - Missing Python Dependencies ⚠️ **HIGH PRIORITY**

**Root Cause**: Workflow installs dependencies from non-existent `requirements.txt`, but dependencies are in `requirements-optional.txt`

**Evidence**:
```
ModuleNotFoundError: No module named 'lark'
ModuleNotFoundError: No module named 'fitz' (PyMuPDF)
ModuleNotFoundError: No module named 'pix2tex'
```

**Dependencies Required** (from requirements-optional.txt):
- `pymupdf>=1.22,<2.0`
- `Pillow>=10,<12`
- `pix2tex>=0.1,<1.0`
- `jsonschema>=4.19,<5`
- `bibtexparser>=1.4.0,<2.0.0`
- `lark>=1.1.2`

**Scripts That Need These**:
1. `equation_extractor.py` → needs `lark`
2. `pdf_equation_extractor.py` → needs `fitz` (pymupdf)
3. `pdf_image_equation_extractor.py` → needs `pix2tex`
4. `build_catalog_pipeline.py` → orchestrates all the above

**Fix Strategy**:
1. Create `requirements.txt` in root combining test and optional dependencies
2. Update `.github/workflows/build.yml` build-catalog job to install requirements
3. Update `.github/workflows/test.yml` validate-catalog job to install requirements

**Files to Modify**:
- `requirements.txt` (CREATE)
- `.github/workflows/build.yml` (line ~160: add pip install step)
- `.github/workflows/test.yml` (line ~120: add pip install step)

**Agent Assignment**: **Agent 1 - dependency-fixer**
**Tools**: Edit, Write
**MCP**: filesystem

---

### Issue 2: ASCII Encoding Violations ⚠️ **MEDIUM PRIORITY**

**Root Cause**: Python files contain Unicode characters (quotes, arrows, Greek letters) violating ASCII-only policy

**Violations Found**:

**File 1: `scripts/equation_extractor.py` (18 violations)**
- Line 41:33-60: Smart quotes " " (U+201C, U+201D)
- Line 42:33-44: Math symbols ≈≃≅≡∈≤≥↦→←÷× (U+2248, U+2243, U+2245, U+2261, U+2208, U+2264, U+2265, U+21A6, U+2192, U+2190, U+00F7, U+00D7)
- Line 82:27-32: Greek letters αωΑΩ (U+03B1, U+03C9, U+0391, U+03A9)

**File 2: `scripts/rename_equation_modules.py` (10 violations)**
- Lines 174-221: Arrow → characters (U+2192) in print statements

**File 3: `scripts/superforce/modular_forms.py` (5 violations)**
- Line 13:3: τ (U+03C4) in comment
- Line 15:15,17: π, τ (U+03C0, U+03C4) in formula comment
- Line 79:28,30,44: η, τ, ∏ (U+03B7, U+03C4, U+220F) in docstring

**File 4: `scripts/CLAUDE.md` (2 violations)**
- Line 9:4-5: Warning emoji ⚠️ (U+26A0, U+FE0F)

**Fix Strategy**:
1. Replace smart quotes with straight quotes: " → "
2. Replace arrows with ASCII: → → ->
3. Replace Greek letters with names: τ → tau, π → pi, η → eta, α → alpha, ω → omega
4. Replace math symbols with ASCII equivalents or spelled out
5. Replace emoji with text: ⚠️ → WARNING:

**Files to Modify**:
- `scripts/equation_extractor.py`
- `scripts/rename_equation_modules.py`
- `scripts/superforce/modular_forms.py`
- `scripts/CLAUDE.md`

**Agent Assignment**: **Agent 2 - ascii-enforcer**
**Tools**: Edit, Read
**MCP**: filesystem

---

### Issue 3: pytest - Missing Coverage Plugin ⚠️ **LOW PRIORITY**

**Root Cause**: Workflow runs `pytest --cov` but `pytest-cov` plugin not installed

**Evidence**:
```
ERROR: usage: pytest [options] [file_or_dir] [file_or_dir] [...]
pytest: error: unrecognized arguments: --cov --cov-report=xml
```

**Current**: `requirements-test.txt` only has `pytest==7.4.3`

**Fix Strategy**:
1. Add `pytest-cov` to `requirements-test.txt`
2. Update `.github/workflows/test.yml` to install test requirements

**Files to Modify**:
- `requirements-test.txt` (add line: pytest-cov>=4.1,<5)
- `.github/workflows/test.yml` (ensure test requirements installed)

**Agent Assignment**: **Agent 1 - dependency-fixer** (same agent as Issue 1)
**Tools**: Edit, Write
**MCP**: filesystem

---

### Issue 4: LaTeX Strict Mode - Expected Failure ✅ **NO FIX NEEDED**

**Status**: Working as designed

**Evidence**:
```
Error: latexmk strict compilation failed
WARNINGS_AS_ERRORS=1
```

**Root Cause**: Document has 87+ undefined references and 20+ undefined citations (expected for incomplete work)

**Assessment**: This is **correct behavior**. The strict mode job is designed to fail when warnings exist. Once the document is complete, this will pass.

**Action**: None - this validates that strict mode is working

---

## Fix Plan Summary

| Issue | Priority | Agent | Estimated Time | Blocker |
|-------|----------|-------|----------------|---------|
| Missing Dependencies | HIGH | dependency-fixer | 5 min | YES (Pages deployment) |
| ASCII Violations | MEDIUM | ascii-enforcer | 10 min | YES (validate-code) |
| pytest-cov Missing | LOW | dependency-fixer | 2 min | YES (test-python) |
| LaTeX Strict | N/A | None | N/A | NO (expected) |

**Total Agents**: 2 (parallel deployment)
**Total Estimated Time**: ~10-15 minutes
**Blocking Deployment**: Issues 1, 2, 3

---

## Agent Deployment Plan

### Agent 1: dependency-fixer
**Role**: Fix all dependency-related issues
**Tools**: Read, Edit, Write
**MCP**: filesystem
**Tasks**:
1. Create `requirements.txt` combining test and optional deps
2. Update build.yml to install requirements for build-catalog
3. Update test.yml to install requirements for validate-catalog and test-python
4. Add pytest-cov to requirements-test.txt

**Expected Output**:
- `requirements.txt` (new file)
- `.github/workflows/build.yml` (modified)
- `.github/workflows/test.yml` (modified)
- `requirements-test.txt` (modified)

---

### Agent 2: ascii-enforcer
**Role**: Replace all Unicode characters with ASCII equivalents
**Tools**: Read, Edit
**MCP**: filesystem
**Tasks**:
1. Fix `scripts/equation_extractor.py` (18 replacements)
2. Fix `scripts/rename_equation_modules.py` (10 replacements)
3. Fix `scripts/superforce/modular_forms.py` (5 replacements)
4. Fix `scripts/CLAUDE.md` (2 replacements)

**Expected Output**:
- 4 files modified with all Unicode → ASCII replacements

---

## Verification Plan

### Step 1: Commit and Push
```bash
git add requirements.txt requirements-test.txt .github/workflows/*.yml scripts/
git commit -m "Fix CI/CD quality gate failures: dependencies + ASCII violations"
git push origin main
```

### Step 2: Monitor Workflows
- build.yml: Should complete successfully (build-catalog will pass)
- test.yml: Should complete successfully (ASCII guard, pytest will pass)
- Validate GitHub Pages deployment works

### Step 3: Success Criteria
- ✅ build-catalog job succeeds
- ✅ Equation catalog artifacts generated
- ✅ GitHub Pages deployed with catalog
- ✅ validate-code (ASCII guard) passes
- ✅ test-python passes on all 4 matrix combinations
- ✅ validate-catalog passes

---

## Rollback Plan

If any agent fails or introduces new issues:

```bash
# Revert specific file
git checkout HEAD~1 -- <file-path>

# Or revert entire commit
git revert HEAD
git push origin main
```

---

**Plan Status**: ✅ Ready for execution
**Next Step**: Deploy agents in parallel using Task tool
**Expected Completion**: ~15 minutes from deployment to verified workflows
