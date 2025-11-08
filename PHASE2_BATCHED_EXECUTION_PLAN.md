# Phase 2: Batched Equation Module Renaming - Execution Plan

**Created:** 2025-11-07
**Strategy:** Execute in 4 well-scoped batches with full validation at each step
**Total:** 174 files across 8 chapters

---

## Execution Strategy

Instead of renaming all 174 files at once, we'll execute in **4 logical batches** based on framework groupings. Each batch includes:

1. **Pre-batch sanity check** - Verify current state
2. **Execute rename** - Run script for specific batch
3. **Post-rename verification** - Confirm all files renamed
4. **Test compilation** - Build LaTeX to catch errors early
5. **Git commit** - Checkpoint progress

---

## Batch Breakdown

### Batch 1: Aether → Scalar
**Scope:** 119 files (71 manual + 48 auto-generated AE→SC)
**Chapters affected:** 3 files with 12 references
- `ch07_aether_scalar_fields.tex` (6 references)
- `ch08_aether_zpe_coupling.tex` (5 references)
- `ch29_advanced_propulsion.tex` (1 reference)

**Rationale:** Largest batch but logically cohesive (all scalar-vacuum sector)

### Batch 2: Genesis → Symmetry
**Scope:** 22 files (all manual, 0 auto-generated GE→SX)
**Chapters affected:** 3 files with 16 references
- `ch11_genesis_overview.tex` (6 references)
- `ch12_nodespace_theory.tex` (8 references)
- `ch14_genesis_superforce.tex` (2 references)

**Rationale:** Medium batch, exceptional symmetries sector

### Batch 3: Pais → GEM
**Scope:** 27 files (24 manual + 3 auto-generated PE→GM)
**Chapters affected:** 1 file with 6 references
- `ch16_pais_gem_formalism.tex` (6 references)

**Rationale:** Medium batch, GEM formalism sector

### Batch 4: Unified → PhysicsForge
**Scope:** 6 files (2 manual + 4 auto-generated UE→PF)
**Chapters affected:** 1 file with 4 references
- `ch21_unified_framework.tex` (4 references)

**Rationale:** Smallest batch, finalization

---

## Detailed Execution Steps

### Batch 1: Aether → Scalar (119 files)

#### 1. Pre-batch Sanity Check
```bash
cd ~/Playground/PhysicsForge

# Verify current state
ls -1 synthesis/modules/equations/eq_aether_* | wc -l
# Expected: 71 files

ls -1 synthesis/modules/equations/eq_ae*_auto.tex | wc -l
# Expected: 48 files

# Check chapter references
grep -n "\\input{modules/equations/eq_aether_" synthesis/chapters/frameworks/ch07*.tex | wc -l
# Expected: 6 matches

grep -n "\\input{modules/equations/eq_aether_" synthesis/chapters/frameworks/ch08*.tex | wc -l
# Expected: 5 matches

grep -n "\\input{modules/equations/eq_aether_" synthesis/chapters/applications/ch29*.tex | wc -l
# Expected: 1 match

# Verify LaTeX builds before changes
make clean && make latex
# Expected: 577-page PDF builds successfully
```

#### 2. Execute Batch 1 Rename
```bash
# Create batch-specific script or modify rename_equation_modules.py with --batch flag
# For now, we can manually specify patterns

# Rename manual Aether files
cd synthesis/modules/equations
for f in eq_aether_*.tex; do
    new="${f/eq_aether_/eq_scalar_}"
    git mv "$f" "$new"
done

# Rename auto-generated AE files
for f in eq_ae*_auto.tex; do
    new="${f/eq_ae/eq_sc}"
    git mv "$f" "$new"
done

# Update chapter references
cd ~/Playground/PhysicsForge
sed -i 's/eq_aether_/eq_scalar_/g' synthesis/chapters/frameworks/ch07*.tex
sed -i 's/eq_aether_/eq_scalar_/g' synthesis/chapters/frameworks/ch08*.tex
sed -i 's/eq_aether_/eq_scalar_/g' synthesis/chapters/applications/ch29*.tex
sed -i 's/eq_ae\([0-9]\+\)_auto/eq_sc\1_auto/g' synthesis/chapters/frameworks/ch07*.tex
sed -i 's/eq_ae\([0-9]\+\)_auto/eq_sc\1_auto/g' synthesis/chapters/frameworks/ch08*.tex
sed -i 's/eq_ae\([0-9]\+\)_auto/eq_sc\1_auto/g' synthesis/chapters/applications/ch29*.tex
```

#### 3. Post-rename Verification
```bash
cd ~/Playground/PhysicsForge

# Verify new files exist
ls -1 synthesis/modules/equations/eq_scalar_* | wc -l
# Expected: 71 files

ls -1 synthesis/modules/equations/eq_sc*_auto.tex | wc -l
# Expected: 48 files

# Verify old files gone
ls -1 synthesis/modules/equations/eq_aether_* 2>/dev/null | wc -l
# Expected: 0 files

ls -1 synthesis/modules/equations/eq_ae*_auto.tex 2>/dev/null | wc -l
# Expected: 0 files

# Check references updated
grep -n "eq_aether_" synthesis/chapters/frameworks/ch07*.tex
# Expected: No matches (exit code 1)

grep -n "eq_aether_" synthesis/chapters/frameworks/ch08*.tex
# Expected: No matches (exit code 1)

grep -n "eq_aether_" synthesis/chapters/applications/ch29*.tex
# Expected: No matches (exit code 1)

# Verify new references present
grep -c "eq_scalar_" synthesis/chapters/frameworks/ch07*.tex
# Expected: 6 matches

grep -c "eq_scalar_" synthesis/chapters/frameworks/ch08*.tex
# Expected: 5 matches

grep -c "eq_scalar_" synthesis/chapters/applications/ch29*.tex
# Expected: 1 match
```

#### 4. Test Compilation
```bash
cd ~/Playground/PhysicsForge
make clean && make latex
# Expected: PDF builds successfully (may have different page count due to renames)
```

#### 5. Git Commit
```bash
cd ~/Playground/PhysicsForge
git add synthesis/modules/equations/eq_scalar_*.tex
git add synthesis/modules/equations/eq_sc*_auto.tex
git add synthesis/chapters/frameworks/ch07*.tex
git add synthesis/chapters/frameworks/ch08*.tex
git add synthesis/chapters/applications/ch29*.tex

git commit -m "Phase 2 Batch 1: Rename Aether→Scalar (119 files, 3 chapters)

- Renamed 71 eq_aether_*.tex → eq_scalar_*.tex
- Renamed 48 eq_ae###_auto.tex → eq_sc###_auto.tex
- Updated 12 references across ch07, ch08, ch29
- LaTeX build verified: PDF compiles successfully

Framework unification step 1 of 4: Scalar-vacuum sector nomenclature"
```

---

### Batch 2: Genesis → Symmetry (22 files)

#### 1. Pre-batch Sanity Check
```bash
cd ~/Playground/PhysicsForge

# Verify current state
ls -1 synthesis/modules/equations/eq_genesis_* | wc -l
# Expected: 22 files

# Note: 0 auto-generated GE files expected

# Check chapter references
grep -n "\\input{modules/equations/eq_genesis_" synthesis/chapters/frameworks/ch11*.tex | wc -l
# Expected: 6 matches

grep -n "\\input{modules/equations/eq_genesis_" synthesis/chapters/frameworks/ch12*.tex | wc -l
# Expected: 8 matches

grep -n "\\input{modules/equations/eq_genesis_" synthesis/chapters/frameworks/ch14*.tex | wc -l
# Expected: 2 matches

# Verify LaTeX still builds after Batch 1
make clean && make latex
```

#### 2. Execute Batch 2 Rename
```bash
cd ~/Playground/PhysicsForge/synthesis/modules/equations

# Rename Genesis files
for f in eq_genesis_*.tex; do
    new="${f/eq_genesis_/eq_symm_}"
    git mv "$f" "$new"
done

# Update chapter references
cd ~/Playground/PhysicsForge
sed -i 's/eq_genesis_/eq_symm_/g' synthesis/chapters/frameworks/ch11*.tex
sed -i 's/eq_genesis_/eq_symm_/g' synthesis/chapters/frameworks/ch12*.tex
sed -i 's/eq_genesis_/eq_symm_/g' synthesis/chapters/frameworks/ch14*.tex
```

#### 3. Post-rename Verification
```bash
cd ~/Playground/PhysicsForge

# Verify new files exist
ls -1 synthesis/modules/equations/eq_symm_* | wc -l
# Expected: 22 files

# Verify old files gone
ls -1 synthesis/modules/equations/eq_genesis_* 2>/dev/null | wc -l
# Expected: 0 files

# Verify references updated
grep -n "eq_genesis_" synthesis/chapters/frameworks/ch11*.tex
# Expected: No matches

grep -n "eq_genesis_" synthesis/chapters/frameworks/ch12*.tex
# Expected: No matches

grep -n "eq_genesis_" synthesis/chapters/frameworks/ch14*.tex
# Expected: No matches

# Verify new references present
grep -c "eq_symm_" synthesis/chapters/frameworks/ch11*.tex
# Expected: 6 matches

grep -c "eq_symm_" synthesis/chapters/frameworks/ch12*.tex
# Expected: 8 matches

grep -c "eq_symm_" synthesis/chapters/frameworks/ch14*.tex
# Expected: 2 matches
```

#### 4. Test Compilation
```bash
cd ~/Playground/PhysicsForge
make clean && make latex
```

#### 5. Git Commit
```bash
cd ~/Playground/PhysicsForge
git add synthesis/modules/equations/eq_symm_*.tex
git add synthesis/chapters/frameworks/ch11*.tex
git add synthesis/chapters/frameworks/ch12*.tex
git add synthesis/chapters/frameworks/ch14*.tex

git commit -m "Phase 2 Batch 2: Rename Genesis→Symmetry (22 files, 3 chapters)

- Renamed 22 eq_genesis_*.tex → eq_symm_*.tex
- Updated 16 references across ch11, ch12, ch14
- LaTeX build verified: PDF compiles successfully

Framework unification step 2 of 4: Exceptional symmetries nomenclature"
```

---

### Batch 3: Pais → GEM (27 files)

#### 1. Pre-batch Sanity Check
```bash
cd ~/Playground/PhysicsForge

# Verify current state
ls -1 synthesis/modules/equations/eq_pais_* | wc -l
# Expected: 24 files

ls -1 synthesis/modules/equations/eq_pe*_auto.tex | wc -l
# Expected: 3 files

# Check chapter references
grep -n "\\input{modules/equations/eq_pais_" synthesis/chapters/frameworks/ch16*.tex | wc -l
# Expected: 6 matches

# Verify LaTeX still builds after Batch 2
make clean && make latex
```

#### 2. Execute Batch 3 Rename
```bash
cd ~/Playground/PhysicsForge/synthesis/modules/equations

# Rename manual Pais files
for f in eq_pais_*.tex; do
    new="${f/eq_pais_/eq_gem_}"
    git mv "$f" "$new"
done

# Rename auto-generated PE files
for f in eq_pe*_auto.tex; do
    new="${f/eq_pe/eq_gm}"
    git mv "$f" "$new"
done

# Update chapter references
cd ~/Playground/PhysicsForge
sed -i 's/eq_pais_/eq_gem_/g' synthesis/chapters/frameworks/ch16*.tex
sed -i 's/eq_pe\([0-9]\+\)_auto/eq_gm\1_auto/g' synthesis/chapters/frameworks/ch16*.tex
```

#### 3. Post-rename Verification
```bash
cd ~/Playground/PhysicsForge

# Verify new files exist
ls -1 synthesis/modules/equations/eq_gem_* | wc -l
# Expected: 24 files (excluding eq_gem_gem_coupling.tex if already exists)

ls -1 synthesis/modules/equations/eq_gm*_auto.tex | wc -l
# Expected: 3 files

# Verify old files gone
ls -1 synthesis/modules/equations/eq_pais_* 2>/dev/null | wc -l
# Expected: 0 files

ls -1 synthesis/modules/equations/eq_pe*_auto.tex 2>/dev/null | wc -l
# Expected: 0 files

# Verify references updated
grep -n "eq_pais_" synthesis/chapters/frameworks/ch16*.tex
# Expected: No matches

# Verify new references present
grep -c "eq_gem_" synthesis/chapters/frameworks/ch16*.tex
# Expected: 6 matches
```

#### 4. Test Compilation
```bash
cd ~/Playground/PhysicsForge
make clean && make latex
```

#### 5. Git Commit
```bash
cd ~/Playground/PhysicsForge
git add synthesis/modules/equations/eq_gem_*.tex
git add synthesis/modules/equations/eq_gm*_auto.tex
git add synthesis/chapters/frameworks/ch16*.tex

git commit -m "Phase 2 Batch 3: Rename Pais→GEM (27 files, 1 chapter)

- Renamed 24 eq_pais_*.tex → eq_gem_*.tex
- Renamed 3 eq_pe###_auto.tex → eq_gm###_auto.tex
- Updated 6 references in ch16
- LaTeX build verified: PDF compiles successfully

Framework unification step 3 of 4: Gravitoelectromagnetism nomenclature"
```

---

### Batch 4: Unified → PhysicsForge (6 files)

#### 1. Pre-batch Sanity Check
```bash
cd ~/Playground/PhysicsForge

# Verify current state
ls -1 synthesis/modules/equations/eq_unified_* | wc -l
# Expected: 2 files

ls -1 synthesis/modules/equations/eq_ue*_auto.tex | wc -l
# Expected: 4 files

# Check chapter references
grep -n "\\input{modules/equations/eq_unified_" synthesis/chapters/unification/ch21*.tex | wc -l
# Expected: 4 matches

# Verify LaTeX still builds after Batch 3
make clean && make latex
```

#### 2. Execute Batch 4 Rename
```bash
cd ~/Playground/PhysicsForge/synthesis/modules/equations

# Rename manual Unified files
for f in eq_unified_*.tex; do
    new="${f/eq_unified_/eq_physforge_}"
    git mv "$f" "$new"
done

# Rename auto-generated UE files
for f in eq_ue*_auto.tex; do
    new="${f/eq_ue/eq_pf}"
    git mv "$f" "$new"
done

# Update chapter references
cd ~/Playground/PhysicsForge
sed -i 's/eq_unified_/eq_physforge_/g' synthesis/chapters/unification/ch21*.tex
sed -i 's/eq_ue\([0-9]\+\)_auto/eq_pf\1_auto/g' synthesis/chapters/unification/ch21*.tex
```

#### 3. Post-rename Verification
```bash
cd ~/Playground/PhysicsForge

# Verify new files exist
ls -1 synthesis/modules/equations/eq_physforge_* | wc -l
# Expected: 2 files

ls -1 synthesis/modules/equations/eq_pf*_auto.tex | wc -l
# Expected: 4 files

# Verify old files gone
ls -1 synthesis/modules/equations/eq_unified_* 2>/dev/null | wc -l
# Expected: 0 files

ls -1 synthesis/modules/equations/eq_ue*_auto.tex 2>/dev/null | wc -l
# Expected: 0 files

# Verify references updated
grep -n "eq_unified_" synthesis/chapters/unification/ch21*.tex
# Expected: No matches

# Verify new references present
grep -c "eq_physforge_" synthesis/chapters/unification/ch21*.tex
# Expected: 4 matches
```

#### 4. Test Compilation
```bash
cd ~/Playground/PhysicsForge
make clean && make latex
```

#### 5. Git Commit
```bash
cd ~/Playground/PhysicsForge
git add synthesis/modules/equations/eq_physforge_*.tex
git add synthesis/modules/equations/eq_pf*_auto.tex
git add synthesis/chapters/unification/ch21*.tex

git commit -m "Phase 2 Batch 4: Rename Unified→PhysicsForge (6 files, 1 chapter)

- Renamed 2 eq_unified_*.tex → eq_physforge_*.tex
- Renamed 4 eq_ue###_auto.tex → eq_pf###_auto.tex
- Updated 4 references in ch21
- LaTeX build verified: PDF compiles successfully

Framework unification step 4 of 4: PhysicsForge unified nomenclature complete"
```

---

## Final Batch Completion Report

After Batch 4 completes, create summary document:

```bash
cd ~/Playground/PhysicsForge

cat > PHASE2_EQUATION_RENAME_COMPLETE.md <<'EOF'
# Phase 2: Equation Module Renaming - COMPLETE

**Completed:** 2025-11-07
**Total Files Renamed:** 174
**Total References Updated:** 38 across 8 chapters

## Batch Summary

| Batch | Framework | Files | Chapters | Status |
|-------|-----------|-------|----------|--------|
| 1 | Aether → Scalar | 119 | 3 | ✅ COMPLETE |
| 2 | Genesis → Symmetry | 22 | 3 | ✅ COMPLETE |
| 3 | Pais → GEM | 27 | 1 | ✅ COMPLETE |
| 4 | Unified → PhysicsForge | 6 | 1 | ✅ COMPLETE |

## Verification

Final build test:
```bash
cd ~/Playground/PhysicsForge
make clean && make latex
```

**Result:** [PAGE COUNT]-page PDF builds successfully

## Git History

All changes committed across 4 batches:
```bash
git log --oneline --grep="Phase 2 Batch" -4
```

## Next Steps

- [ ] Phase 3: Update equation tags (\eqtag{F}{D}{S} system)
- [ ] Phase 4: Fix chapter titles and references
- [ ] Phase 5: Validate unified build
- [ ] Run full CI pipeline

EOF
```

---

## Rollback Plan (If Needed)

If any batch fails catastrophically:

```bash
cd ~/Playground/PhysicsForge

# Option 1: Revert last commit
git reset --hard HEAD~1

# Option 2: Revert to before Phase 2 started
git log --oneline --grep="Phase 2 Batch" -1
# Note the commit hash BEFORE first batch
git reset --hard <commit-hash>

# Option 3: Cherry-pick successful batches only
git cherry-pick <batch1-commit>
git cherry-pick <batch2-commit>
# Skip failed batch
```

---

## Success Criteria (Per Batch)

Each batch is considered successful when:

1. ✅ All expected files renamed (verified with ls/wc)
2. ✅ No old files remain (verified with ls exit code)
3. ✅ All references updated in chapters (verified with grep)
4. ✅ LaTeX builds successfully (make latex exits 0)
5. ✅ Git commit created with detailed message

---

**Document Status:** READY FOR EXECUTION
**Recommended Start:** Batch 1 (Aether → Scalar)
