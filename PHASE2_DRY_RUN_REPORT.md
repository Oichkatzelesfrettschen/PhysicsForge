# Phase 2: Equation Module Renaming - Dry Run Report

## Summary

The rename script has identified **174 equation module files** that need to be renamed from branded terms to standard physics terms, along with **38 references** in **8 chapter files** that need to be updated.

## Files to Rename by Category

| From | To | Count |
|------|----|-------|
| Aether → Scalar | `eq_aether_*` → `eq_scalar_*` | 71 files |
| Genesis → Symmetry | `eq_genesis_*` → `eq_symm_*` | 22 files |
| Pais → GEM | `eq_pais_*` → `eq_gem_*` | 24 files |
| Unified → PhysicsForge | `eq_unified_*` → `eq_physforge_*` | 2 files |
| Auto AE → SC | `eq_ae###_auto` → `eq_sc###_auto` | 48 files |
| Auto GE → SX | `eq_ge###_auto` → `eq_sx###_auto` | 0 files |
| Auto PE → GM | `eq_pe###_auto` → `eq_gm###_auto` | 3 files |
| Auto UE → PF | `eq_ue###_auto` → `eq_pf###_auto` | 4 files |
| **TOTAL** | | **174 files** |

## Chapter References to Update

| Chapter File | Reference Count |
|--------------|-----------------|
| `ch29_advanced_propulsion.tex` | 1 |
| `ch07_aether_scalar_fields.tex` | 6 |
| `ch08_aether_zpe_coupling.tex` | 5 |
| `ch11_genesis_overview.tex` | 6 |
| `ch12_nodespace_theory.tex` | 8 |
| `ch14_genesis_superforce.tex` | 2 |
| `ch16_pais_gem_formalism.tex` | 6 |
| `ch21_unified_framework.tex` | 4 |
| **TOTAL** | **38 references** |

## Sample Renames

### Aether → Scalar Examples
- `eq_aether_scalar_wave.tex` → `eq_scalar_scalar_wave.tex`
- `eq_aether_zpe_coherence.tex` → `eq_scalar_zpe_coherence.tex`
- `eq_aether_casimir_modification.tex` → `eq_scalar_casimir_modification.tex`

### Genesis → Symmetry Examples
- `eq_genesis_dimensional_folding.tex` → `eq_symm_dimensional_folding.tex`
- `eq_genesis_superforce.tex` → `eq_symm_superforce.tex`

### Pais → GEM Examples
- `eq_pais_gem_coupling.tex` → `eq_gem_gem_coupling.tex`
- `eq_pais_gravitoelectric_field.tex` → `eq_gem_gravitoelectric_field.tex`

### Auto-generated Examples
- `eq_ae001_auto.tex` → `eq_sc001_auto.tex`
- `eq_pe001_auto.tex` → `eq_gm001_auto.tex`
- `eq_ue001_auto.tex` → `eq_pf001_auto.tex`

## Impact Assessment

### Low Risk
- File renames are straightforward pattern replacements
- Reference updates are simple string replacements
- No content changes within files (labels remain unchanged)
- Build can be tested immediately after execution

### Medium Considerations
- 174 files is substantial but manageable
- Only 8 chapter files affected (limited scope)
- Auto-generated files follow clear numbering pattern

### High Importance
- This is more than the 10-file threshold mentioned
- Backup recommended before execution
- Full build test required after changes

## Execution Command

To proceed with the renaming (after approval):

```bash
cd ~/Playground/PhysicsForge
python scripts/rename_equation_modules.py --execute
```

## Test Command

After execution:

```bash
cd ~/Playground/PhysicsForge
make clean && make latex
```

## Recommendation

**REQUEST APPROVAL**: With 174 files to rename (significantly more than 10), I recommend getting your explicit approval before proceeding with the execution.

The changes are systematic and reversible (via git), but the scope is substantial. The dry-run shows no conflicts and the patterns are clean.

---

Generated: 2024-11-07
Script: `scripts/rename_equation_modules.py`
Status: DRY RUN COMPLETE - AWAITING APPROVAL