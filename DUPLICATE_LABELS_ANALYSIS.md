# DUPLICATE LABELS ANALYSIS

## Executive Summary

- **Total .tex files analyzed:** 443
- **Total label definitions found:** 1933
- **Unique labels:** 1933
- **Duplicate labels:** 0

### Duplicates by Category

| Category | Count | Percentage |
|----------|-------|------------|
| Equation | 0 | 0.0% |
| Figure | 0 | 0.0% |
| Table | 0 | 0.0% |
| Chapter | 0 | 0.0% |
| Section | 0 | 0.0% |
| Part | 0 | 0.0% |
| Other | 0 | 0.0% |

## Detailed Duplicate Analysis

## Resolution Strategy

### Priority Order (Most Impactful First)

1. **Fix Multiple Labels in Single File** (0 labels)
   - These are likely from multi-line align environments with repeated labels
   - Resolution: Keep only first label in align block

2. **Module Reuse Issues** (0 labels)
   - Resolution: Labels should be unique in modules, no action needed if properly used
   - Verify modules are not defining duplicate labels internally

3. **Framework Collisions** (0 labels)
   - Resolution: Add chapter prefix: `eq:chNN:framework:descriptor`

4. **Auto-Manual Conflicts** (0 labels)
   - Resolution: Rename auto labels with `:auto:` prefix

5. **Copy-Paste Errors** (0 labels)
   - Resolution: Remove duplicate, keep first occurrence

## Quick Fix Commands

### Find and review specific duplicates:
```bash
# Example: Fix eq:prelim:commutator-xx
grep -rn "\\label{eq:prelim:commutator-xx}" synthesis/
```

### Check for labels in backup files:
```bash
find synthesis -name "*.bak" -exec grep -l "\\label{" {} \;
```

### Verify no duplicate labels after fixes:
```bash
grep -r "\\label{" synthesis --include="*.tex" | 
  grep -o "\\label{[^}]*}" | sort | uniq -d
```

## Statistics Summary

| Metric | Value |
|--------|-------|
| Total Labels | 1933 |
| Unique Labels | 1933 |
| Duplicate Labels | 0 |
| Duplication Rate | 0.0% |
| Most Duplicated | 0 times |