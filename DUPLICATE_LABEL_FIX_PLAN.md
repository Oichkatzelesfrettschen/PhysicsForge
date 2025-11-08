# DUPLICATE LABEL FIX PLAN
Generated: /home/eirikr/Playground/PhysicsForge
Total duplicates found: 148
Total fix commands: 158

## Summary by Category

- **chapter**: 2 duplicates
- **equation**: 86 duplicates
- **section**: 13 duplicates
- **subsection**: 47 duplicates

## Fix Strategy

1. **Backup files** (`*_backup.tex`, `*_expanded.tex`): Rename labels with `:backup` or `:expanded` suffix
2. **Chapter duplicates**: Add `:ch##` suffix where ## is chapter number
3. **Equation duplicates**: Insert `:ch##:` after framework prefix
4. **Module duplicates**: Add `:mod_<module_name>` suffix
5. **Test files**: Not modified (they include the main content)

## Detailed Fix Commands

### Automated Fix Script

Save the following as `fix_duplicate_labels.sh` and run with `bash fix_duplicate_labels.sh`:

```bash
#!/bin/bash
# Fix duplicate LaTeX labels
set -e

cd /home/eirikr/Playground/PhysicsForge/synthesis

echo 'Creating backup...'
tar -czf ../synthesis_backup_$(date +%Y%m%d_%H%M%S).tar.gz .


# Fixing chapters/frameworks/ch07_aether_scalar_fields_backup.tex (10 changes)
echo 'Fixing chapters/frameworks/ch07_aether_scalar_fields_backup.tex...'
# Line 666: sec:aether-scalar:summary -> sec:aether-scalar:summary:backup
sed -i '666s/\\label{sec:aether\-scalar:summary}/\\label{sec:aether-scalar:summary:backup}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_backup.tex
# Line 412: subsec:aether-scalar:quantum-computing -> subsec:aether-scalar:quantum-computing:backup
sed -i '412s/\\label{subsec:aether\-scalar:quantum\-computing}/\\label{subsec:aether-scalar:quantum-computing:backup}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_backup.tex
# Line 372: sec:aether-scalar:applications -> sec:aether-scalar:applications:backup
sed -i '372s/\\label{sec:aether\-scalar:applications}/\\label{sec:aether-scalar:applications:backup}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_backup.tex
# Line 311: eq:aether:scalar-zpe-coupling -> eq:aether:scalar-zpe-coupling:backup
sed -i '311s/\\label{eq:aether:scalar\-zpe\-coupling}/\\label{eq:aether:scalar-zpe-coupling:backup}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_backup.tex
# Line 275: eq:aether:origami-projection -> eq:aether:origami-projection:backup
sed -i '275s/\\label{eq:aether:origami\-projection}/\\label{eq:aether:origami-projection:backup}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_backup.tex
# Line 57: eq:aether:fractal-potential -> eq:aether:fractal-potential:backup
sed -i '57s/\\label{eq:aether:fractal\-potential}/\\label{eq:aether:fractal-potential:backup}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_backup.tex
# Line 22: sec:aether-scalar:foundations -> sec:aether-scalar:foundations:backup
sed -i '22s/\\label{sec:aether\-scalar:foundations}/\\label{sec:aether-scalar:foundations:backup}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_backup.tex
# Line 16: ch:aether-scalar-fields -> ch:aether-scalar-fields:backup
sed -i '16s/\\label{ch:aether\-scalar\-fields}/\\label{ch:aether-scalar-fields:backup}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_backup.tex

# Fixing chapters/frameworks/ch07_aether_scalar_fields_expanded.tex (141 changes)
echo 'Fixing chapters/frameworks/ch07_aether_scalar_fields_expanded.tex...'
# Line 1224: subsec:aether-scalar:future -> subsec:aether-scalar:future:expanded
sed -i '1224s/\\label{subsec:aether\-scalar:future}/\\label{subsec:aether-scalar:future:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 1211: subsec:aether-scalar:questions -> subsec:aether-scalar:questions:expanded
sed -i '1211s/\\label{subsec:aether\-scalar:questions}/\\label{subsec:aether-scalar:questions:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 1191: sec:aether-scalar:summary -> sec:aether-scalar:summary:expanded
sed -i '1191s/\\label{sec:aether\-scalar:summary}/\\label{sec:aether-scalar:summary:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 1185: eq:aether:gut-unification -> eq:aether:gut-unification:expanded
sed -i '1185s/\\label{eq:aether:gut\-unification}/\\label{eq:aether:gut-unification:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 1178: eq:aether:pais-modification -> eq:aether:pais-modification:expanded
sed -i '1178s/\\label{eq:aether:pais\-modification}/\\label{eq:aether:pais-modification:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 1172: subsec:aether-scalar:pais -> subsec:aether-scalar:pais:expanded
sed -i '1172s/\\label{subsec:aether\-scalar:pais}/\\label{subsec:aether-scalar:pais:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 1167: eq:aether:origami-equivalence -> eq:aether:origami-equivalence:expanded
sed -i '1167s/\\label{eq:aether:origami\-equivalence}/\\label{eq:aether:origami-equivalence:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 1158: eq:aether:genesis-map -> eq:aether:genesis-map:expanded
sed -i '1158s/\\label{eq:aether:genesis\-map}/\\label{eq:aether:genesis-map:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 1152: subsec:aether-scalar:genesis -> subsec:aether-scalar:genesis:expanded
sed -i '1152s/\\label{subsec:aether\-scalar:genesis}/\\label{subsec:aether-scalar:genesis:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 1148: sec:aether-scalar:connections -> sec:aether-scalar:connections:expanded
sed -i '1148s/\\label{sec:aether\-scalar:connections}/\\label{sec:aether-scalar:connections:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 1140: eq:aether:cmb-modification -> eq:aether:cmb-modification:expanded
sed -i '1140s/\\label{eq:aether:cmb\-modification}/\\label{eq:aether:cmb-modification:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 1131: eq:aether:structure-growth -> eq:aether:structure-growth:expanded
sed -i '1131s/\\label{eq:aether:structure\-growth}/\\label{eq:aether:structure-growth:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 1122: eq:aether:equation-of-state -> eq:aether:equation-of-state:expanded
sed -i '1122s/\\label{eq:aether:equation\-of\-state}/\\label{eq:aether:equation-of-state:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 1117: subsec:aether-scalar:cosmology -> subsec:aether-scalar:cosmology:expanded
sed -i '1117s/\\label{subsec:aether\-scalar:cosmology}/\\label{subsec:aether-scalar:cosmology:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 1110: eq:aether:cavity-q -> eq:aether:cavity-q:expanded
sed -i '1110s/\\label{eq:aether:cavity\-q}/\\label{eq:aether:cavity-q:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 1101: eq:aether:rectification -> eq:aether:rectification:expanded
sed -i '1101s/\\label{eq:aether:rectification}/\\label{eq:aether:rectification:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 1092: eq:aether:zpe-efficiency -> eq:aether:zpe-efficiency:expanded
sed -i '1092s/\\label{eq:aether:zpe\-efficiency}/\\label{eq:aether:zpe-efficiency:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 1087: subsec:aether-scalar:energy-harvesting -> subsec:aether-scalar:energy-harvesting:expanded
sed -i '1087s/\\label{subsec:aether\-scalar:energy\-harvesting}/\\label{subsec:aether-scalar:energy-harvesting:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 1080: eq:aether:entanglement-protection -> eq:aether:entanglement-protection:expanded
sed -i '1080s/\\label{eq:aether:entanglement\-protection}/\\label{eq:aether:entanglement-protection:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 1071: eq:aether:gate-fidelity -> eq:aether:gate-fidelity:expanded
sed -i '1071s/\\label{eq:aether:gate\-fidelity}/\\label{eq:aether:gate-fidelity:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 1062: eq:aether:decoherence-rate -> eq:aether:decoherence-rate:expanded
sed -i '1062s/\\label{eq:aether:decoherence\-rate}/\\label{eq:aether:decoherence-rate:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 1055: subsec:aether-scalar:quantum-computing -> subsec:aether-scalar:quantum-computing:expanded
sed -i '1055s/\\label{subsec:aether\-scalar:quantum\-computing}/\\label{subsec:aether-scalar:quantum-computing:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 1051: sec:aether-scalar:applications -> sec:aether-scalar:applications:expanded
sed -i '1051s/\\label{sec:aether\-scalar:applications}/\\label{sec:aether-scalar:applications:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 1043: eq:aether:pontryagin -> eq:aether:pontryagin:expanded
sed -i '1043s/\\label{eq:aether:pontryagin}/\\label{eq:aether:pontryagin:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 1034: eq:aether:hopf-invariant -> eq:aether:hopf-invariant:expanded
sed -i '1034s/\\label{eq:aether:hopf\-invariant}/\\label{eq:aether:hopf-invariant:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 1027: eq:aether:winding-number -> eq:aether:winding-number:expanded
sed -i '1027s/\\label{eq:aether:winding\-number}/\\label{eq:aether:winding-number:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 1020: subsec:aether-scalar:topology -> subsec:aether-scalar:topology:expanded
sed -i '1020s/\\label{subsec:aether\-scalar:topology}/\\label{subsec:aether-scalar:topology:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 1013: eq:aether:box-dimension -> eq:aether:box-dimension:expanded
sed -i '1013s/\\label{eq:aether:box\-dimension}/\\label{eq:aether:box-dimension:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 1004: eq:aether:hausdorff-measure -> eq:aether:hausdorff-measure:expanded
sed -i '1004s/\\label{eq:aether:hausdorff\-measure}/\\label{eq:aether:hausdorff-measure:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 997: subsec:aether-scalar:fractal-measure -> subsec:aether-scalar:fractal-measure:expanded
sed -i '997s/\\label{subsec:aether\-scalar:fractal\-measure}/\\label{subsec:aether-scalar:fractal-measure:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 990: eq:aether:e8-dimension -> eq:aether:e8-dimension:expanded
sed -i '990s/\\label{eq:aether:e8\-dimension}/\\label{eq:aether:e8-dimension:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 981: eq:aether:f4-dimension -> eq:aether:f4-dimension:expanded
sed -i '981s/\\label{eq:aether:f4\-dimension}/\\label{eq:aether:f4-dimension:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 972: eq:aether:g2-dimension -> eq:aether:g2-dimension:expanded
sed -i '972s/\\label{eq:aether:g2\-dimension}/\\label{eq:aether:g2-dimension:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 965: subsec:aether-scalar:lie-groups -> subsec:aether-scalar:lie-groups:expanded
sed -i '965s/\\label{subsec:aether\-scalar:lie\-groups}/\\label{subsec:aether-scalar:lie-groups:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 958: eq:aether:mode-product -> eq:aether:mode-product:expanded
sed -i '958s/\\label{eq:aether:mode\-product}/\\label{eq:aether:mode-product:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 951: eq:aether:cayley-multiplication -> eq:aether:cayley-multiplication:expanded
sed -i '951s/\\label{eq:aether:cayley\-multiplication}/\\label{eq:aether:cayley-multiplication:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 930: subsec:aether-scalar:cayley-dickson -> subsec:aether-scalar:cayley-dickson:expanded
sed -i '930s/\\label{subsec:aether\-scalar:cayley\-dickson}/\\label{subsec:aether-scalar:cayley-dickson:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 926: sec:aether-scalar:advanced-math -> sec:aether-scalar:advanced-math:expanded
sed -i '926s/\\label{sec:aether\-scalar:advanced\-math}/\\label{sec:aether-scalar:advanced-math:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 893: subsec:aether-scalar:protocol-time-crystal -> subsec:aether-scalar:protocol-time-crystal:expanded
sed -i '893s/\\label{subsec:aether\-scalar:protocol\-time\-crystal}/\\label{subsec:aether-scalar:protocol-time-crystal:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 861: subsec:aether-scalar:protocol-dimensional -> subsec:aether-scalar:protocol-dimensional:expanded
sed -i '861s/\\label{subsec:aether\-scalar:protocol\-dimensional}/\\label{subsec:aether-scalar:protocol-dimensional:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 829: subsec:aether-scalar:protocol-entropy -> subsec:aether-scalar:protocol-entropy:expanded
sed -i '829s/\\label{subsec:aether\-scalar:protocol\-entropy}/\\label{subsec:aether-scalar:protocol-entropy:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 817: eq:aether:casimir-enhanced -> eq:aether:casimir-enhanced:expanded
sed -i '817s/\\label{eq:aether:casimir\-enhanced}/\\label{eq:aether:casimir-enhanced:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 792: subsec:aether-scalar:protocol-casimir -> subsec:aether-scalar:protocol-casimir:expanded
sed -i '792s/\\label{subsec:aether\-scalar:protocol\-casimir}/\\label{subsec:aether-scalar:protocol-casimir:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 761: subsec:aether-scalar:protocol-foam -> subsec:aether-scalar:protocol-foam:expanded
sed -i '761s/\\label{subsec:aether\-scalar:protocol\-foam}/\\label{subsec:aether-scalar:protocol-foam:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 754: eq:aether:phonon-modification -> eq:aether:phonon-modification:expanded
sed -i '754s/\\label{eq:aether:phonon\-modification}/\\label{eq:aether:phonon-modification:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 712: subsec:aether-scalar:protocol-vibration -> subsec:aether-scalar:protocol-vibration:expanded
sed -i '712s/\\label{subsec:aether\-scalar:protocol\-vibration}/\\label{subsec:aether-scalar:protocol-vibration:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 708: sec:aether-scalar:protocols -> sec:aether-scalar:protocols:expanded
sed -i '708s/\\label{sec:aether\-scalar:protocols}/\\label{sec:aether-scalar:protocols:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 698: eq:aether:tc-coupling -> eq:aether:tc-coupling:expanded
sed -i '698s/\\label{eq:aether:tc\-coupling}/\\label{eq:aether:tc-coupling:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 693: subsec:aether-scalar:time-crystal-coupling -> subsec:aether-scalar:time-crystal-coupling:expanded
sed -i '693s/\\label{subsec:aether\-scalar:time\-crystal\-coupling}/\\label{subsec:aether-scalar:time-crystal-coupling:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 684: subsec:aether-scalar:continuous-time -> subsec:aether-scalar:continuous-time:expanded
sed -i '684s/\\label{subsec:aether\-scalar:continuous\-time}/\\label{subsec:aether-scalar:continuous-time:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 679: eq:aether:period-doubling -> eq:aether:period-doubling:expanded
sed -i '679s/\\label{eq:aether:period\-doubling}/\\label{eq:aether:period-doubling:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 672: eq:aether:dtc-hamiltonian -> eq:aether:dtc-hamiltonian:expanded
sed -i '672s/\\label{eq:aether:dtc\-hamiltonian}/\\label{eq:aether:dtc-hamiltonian:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 667: subsec:aether-scalar:discrete-time -> subsec:aether-scalar:discrete-time:expanded
sed -i '667s/\\label{subsec:aether\-scalar:discrete\-time}/\\label{subsec:aether-scalar:discrete-time:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 660: eq:aether:floquet-hamiltonian -> eq:aether:floquet-hamiltonian:expanded
sed -i '660s/\\label{eq:aether:floquet\-hamiltonian}/\\label{eq:aether:floquet-hamiltonian:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 654: subsec:aether-scalar:time-crystal-formation -> subsec:aether-scalar:time-crystal-formation:expanded
sed -i '654s/\\label{subsec:aether\-scalar:time\-crystal\-formation}/\\label{subsec:aether-scalar:time-crystal-formation:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 650: sec:aether-scalar:time-crystals -> sec:aether-scalar:time-crystals:expanded
sed -i '650s/\\label{sec:aether\-scalar:time\-crystals}/\\label{sec:aether-scalar:time-crystals:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 642: eq:aether:entropy-oscillation -> eq:aether:entropy-oscillation:expanded
sed -i '642s/\\label{eq:aether:entropy\-oscillation}/\\label{eq:aether:entropy-oscillation:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 633: eq:aether:entropy-evolution -> eq:aether:entropy-evolution:expanded
sed -i '633s/\\label{eq:aether:entropy\-evolution}/\\label{eq:aether:entropy-evolution:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 628: subsec:aether-scalar:entropy-dynamics -> subsec:aether-scalar:entropy-dynamics:expanded
sed -i '628s/\\label{subsec:aether\-scalar:entropy\-dynamics}/\\label{subsec:aether-scalar:entropy-dynamics:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 623: eq:aether:information-max -> eq:aether:information-max:expanded
sed -i '623s/\\label{eq:aether:information\-max}/\\label{eq:aether:information-max:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 614: eq:aether:information-density -> eq:aether:information-density:expanded
sed -i '614s/\\label{eq:aether:information\-density}/\\label{eq:aether:information-density:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 609: subsec:aether-scalar:information -> subsec:aether-scalar:information:expanded
sed -i '609s/\\label{subsec:aether\-scalar:information}/\\label{subsec:aether-scalar:information:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 602: eq:aether:modulated-entropy -> eq:aether:modulated-entropy:expanded
sed -i '602s/\\label{eq:aether:modulated\-entropy}/\\label{eq:aether:modulated-entropy:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 595: eq:aether:bekenstein-hawking -> eq:aether:bekenstein-hawking:expanded
sed -i '595s/\\label{eq:aether:bekenstein\-hawking}/\\label{eq:aether:bekenstein-hawking:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 590: subsec:aether-scalar:holographic -> subsec:aether-scalar:holographic:expanded
sed -i '590s/\\label{subsec:aether\-scalar:holographic}/\\label{subsec:aether-scalar:holographic:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 586: sec:aether-scalar:entropy -> sec:aether-scalar:entropy:expanded
sed -i '586s/\\label{sec:aether\-scalar:entropy}/\\label{sec:aether-scalar:entropy:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 578: eq:aether:dimensional-resonance -> eq:aether:dimensional-resonance:expanded
sed -i '578s/\\label{eq:aether:dimensional\-resonance}/\\label{eq:aether:dimensional-resonance:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 573: subsec:aether-scalar:resonance -> subsec:aether-scalar:resonance:expanded
sed -i '573s/\\label{subsec:aether\-scalar:resonance}/\\label{subsec:aether-scalar:resonance:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 568: eq:aether:e8-coupling -> eq:aether:e8-coupling:expanded
sed -i '568s/\\label{eq:aether:e8\-coupling}/\\label{eq:aether:e8-coupling:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 542: eq:aether:e8-expansion -> eq:aether:e8-expansion:expanded
sed -i '542s/\\label{eq:aether:e8\-expansion}/\\label{eq:aether:e8-expansion:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 536: subsec:aether-scalar:e8-constraints -> subsec:aether-scalar:e8-constraints:expanded
sed -i '536s/\\label{subsec:aether\-scalar:e8\-constraints}/\\label{subsec:aether-scalar:e8-constraints:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 529: eq:aether:kk-mass -> eq:aether:kk-mass:expanded
sed -i '529s/\\label{eq:aether:kk\-mass}/\\label{eq:aether:kk-mass:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 522: eq:aether:kk-decomposition -> eq:aether:kk-decomposition:expanded
sed -i '522s/\\label{eq:aether:kk\-decomposition}/\\label{eq:aether:kk-decomposition:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 517: subsec:aether-scalar:kaluza-klein -> subsec:aether-scalar:kaluza-klein:expanded
sed -i '517s/\\label{subsec:aether\-scalar:kaluza\-klein}/\\label{subsec:aether-scalar:kaluza-klein:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 500: subsec:aether-scalar:hierarchy -> subsec:aether-scalar:hierarchy:expanded
sed -i '500s/\\label{subsec:aether\-scalar:hierarchy}/\\label{subsec:aether-scalar:hierarchy:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 496: sec:aether-scalar:dimensional -> sec:aether-scalar:dimensional:expanded
sed -i '496s/\\label{sec:aether\-scalar:dimensional}/\\label{sec:aether-scalar:dimensional:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 488: eq:aether:wall -> eq:aether:wall:expanded
sed -i '488s/\\label{eq:aether:wall}/\\label{eq:aether:wall:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 479: eq:aether:string -> eq:aether:string:expanded
sed -i '479s/\\label{eq:aether:string}/\\label{eq:aether:string:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 470: eq:aether:monopole -> eq:aether:monopole:expanded
sed -i '470s/\\label{eq:aether:monopole}/\\label{eq:aether:monopole:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 463: subsec:aether-scalar:defects -> subsec:aether-scalar:defects:expanded
sed -i '463s/\\label{subsec:aether\-scalar:defects}/\\label{subsec:aether-scalar:defects:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 456: eq:aether:phonon-dos -> eq:aether:phonon-dos:expanded
sed -i '456s/\\label{eq:aether:phonon\-dos}/\\label{eq:aether:phonon-dos:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 447: eq:aether:phonon-dispersion -> eq:aether:phonon-dispersion:expanded
sed -i '447s/\\label{eq:aether:phonon\-dispersion}/\\label{eq:aether:phonon-dispersion:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 442: subsec:aether-scalar:phonons -> subsec:aether-scalar:phonons:expanded
sed -i '442s/\\label{subsec:aether\-scalar:phonons}/\\label{subsec:aether-scalar:phonons:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 435: eq:aether:lattice-spacing -> eq:aether:lattice-spacing:expanded
sed -i '435s/\\label{eq:aether:lattice\-spacing}/\\label{eq:aether:lattice-spacing:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 426: subsec:aether-scalar:lattice-formation -> subsec:aether-scalar:lattice-formation:expanded
sed -i '426s/\\label{subsec:aether\-scalar:lattice\-formation}/\\label{subsec:aether-scalar:lattice-formation:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 419: eq:aether:foam-density-param -> eq:aether:foam-density-param:expanded
sed -i '419s/\\label{eq:aether:foam\-density\-param}/\\label{eq:aether:foam-density-param:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 410: eq:aether:metric-fluctuations -> eq:aether:metric-fluctuations:expanded
sed -i '410s/\\label{eq:aether:metric\-fluctuations}/\\label{eq:aether:metric-fluctuations:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 403: eq:aether:foam-uncertainty -> eq:aether:foam-uncertainty:expanded
sed -i '403s/\\label{eq:aether:foam\-uncertainty}/\\label{eq:aether:foam-uncertainty:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 398: subsec:aether-scalar:foam-structure -> subsec:aether-scalar:foam-structure:expanded
sed -i '398s/\\label{subsec:aether\-scalar:foam\-structure}/\\label{subsec:aether-scalar:foam-structure:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 394: sec:aether-scalar:quantum-foam -> sec:aether-scalar:quantum-foam:expanded
sed -i '394s/\\label{sec:aether\-scalar:quantum\-foam}/\\label{sec:aether-scalar:quantum-foam:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 386: eq:aether:coherence-max -> eq:aether:coherence-max:expanded
sed -i '386s/\\label{eq:aether:coherence\-max}/\\label{eq:aether:coherence-max:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 379: eq:aether:coherence-function -> eq:aether:coherence-function:expanded
sed -i '379s/\\label{eq:aether:coherence\-function}/\\label{eq:aether:coherence-function:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 374: subsec:aether-scalar:coherence -> subsec:aether-scalar:coherence:expanded
sed -i '374s/\\label{subsec:aether\-scalar:coherence}/\\label{subsec:aether-scalar:coherence:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 367: eq:aether:foam-function -> eq:aether:foam-function:expanded
sed -i '367s/\\label{eq:aether:foam\-function}/\\label{eq:aether:foam-function:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 353: eq:aether:power-transfer -> eq:aether:power-transfer:expanded
sed -i '353s/\\label{eq:aether:power\-transfer}/\\label{eq:aether:power-transfer:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 348: subsec:aether-scalar:energy-transfer -> subsec:aether-scalar:energy-transfer:expanded
sed -i '348s/\\label{subsec:aether\-scalar:energy\-transfer}/\\label{subsec:aether-scalar:energy-transfer:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 343: eq:aether:coupling-value -> eq:aether:coupling-value:expanded
sed -i '343s/\\label{eq:aether:coupling\-value}/\\label{eq:aether:coupling-value:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 336: eq:aether:zpe-effective -> eq:aether:zpe-effective:expanded
sed -i '336s/\\label{eq:aether:zpe\-effective}/\\label{eq:aether:zpe-effective:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 327: subsec:aether-scalar:zpe-coupling-mechanism -> subsec:aether-scalar:zpe-coupling-mechanism:expanded
sed -i '327s/\\label{subsec:aether\-scalar:zpe\-coupling\-mechanism}/\\label{subsec:aether-scalar:zpe-coupling-mechanism:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 320: eq:aether:zpe-finite -> eq:aether:zpe-finite:expanded
sed -i '320s/\\label{eq:aether:zpe\-finite}/\\label{eq:aether:zpe-finite:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 313: eq:aether:cutoff-e8 -> eq:aether:cutoff-e8:expanded
sed -i '313s/\\label{eq:aether:cutoff\-e8}/\\label{eq:aether:cutoff-e8:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 304: eq:aether:zpe-integral -> eq:aether:zpe-integral:expanded
sed -i '304s/\\label{eq:aether:zpe\-integral}/\\label{eq:aether:zpe-integral:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 297: eq:aether:ho-energy -> eq:aether:ho-energy:expanded
sed -i '297s/\\label{eq:aether:ho\-energy}/\\label{eq:aether:ho-energy:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 292: subsec:aether-scalar:zpe-foundations -> subsec:aether-scalar:zpe-foundations:expanded
sed -i '292s/\\label{subsec:aether\-scalar:zpe\-foundations}/\\label{subsec:aether-scalar:zpe-foundations:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 288: sec:aether-scalar:zpe-dynamics -> sec:aether-scalar:zpe-dynamics:expanded
sed -i '288s/\\label{sec:aether\-scalar:zpe\-dynamics}/\\label{sec:aether-scalar:zpe-dynamics:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 281: eq:aether:ssb-expansion -> eq:aether:ssb-expansion:expanded
sed -i '281s/\\label{eq:aether:ssb\-expansion}/\\label{eq:aether:ssb-expansion:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 274: eq:aether:vev -> eq:aether:vev:expanded
sed -i '274s/\\label{eq:aether:vev}/\\label{eq:aether:vev:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 268: eq:aether:ssb-minimum-condition -> eq:aether:ssb-minimum-condition:expanded
sed -i '268s/\\label{eq:aether:ssb\-minimum\-condition}/\\label{eq:aether:ssb-minimum-condition:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 261: eq:aether:mexican-hat -> eq:aether:mexican-hat:expanded
sed -i '261s/\\label{eq:aether:mexican\-hat}/\\label{eq:aether:mexican-hat:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 256: subsec:aether-scalar:ssb -> subsec:aether-scalar:ssb:expanded
sed -i '256s/\\label{subsec:aether\-scalar:ssb}/\\label{subsec:aether-scalar:ssb:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 249: eq:aether:fractal-dimension -> eq:aether:fractal-dimension:expanded
sed -i '249s/\\label{eq:aether:fractal\-dimension}/\\label{eq:aether:fractal-dimension:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 240: eq:aether:fractal-potential -> eq:aether:fractal-potential:expanded
sed -i '240s/\\label{eq:aether:fractal\-potential}/\\label{eq:aether:fractal-potential:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 235: subsec:aether-scalar:fractal-potential -> subsec:aether-scalar:fractal-potential:expanded
sed -i '235s/\\label{subsec:aether\-scalar:fractal\-potential}/\\label{subsec:aether-scalar:fractal-potential:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 229: eq:aether:eta-slowroll -> eq:aether:eta-slowroll:expanded
sed -i '229s/\\label{eq:aether:eta\-slowroll}/\\label{eq:aether:eta-slowroll:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 228: eq:aether:epsilon-slowroll -> eq:aether:epsilon-slowroll:expanded
sed -i '228s/\\label{eq:aether:epsilon\-slowroll}/\\label{eq:aether:epsilon-slowroll:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 222: eq:aether:slow-roll-potential -> eq:aether:slow-roll-potential:expanded
sed -i '222s/\\label{eq:aether:slow\-roll\-potential}/\\label{eq:aether:slow-roll-potential:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 205: subsec:aether-scalar:potentials-detailed -> subsec:aether-scalar:potentials-detailed:expanded
sed -i '205s/\\label{subsec:aether\-scalar:potentials\-detailed}/\\label{subsec:aether-scalar:potentials-detailed:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 198: eq:aether:master-derived -> eq:aether:master-derived:expanded
sed -i '198s/\\label{eq:aether:master\-derived}/\\label{eq:aether:master-derived:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 184: eq:aether:euler-lagrange -> eq:aether:euler-lagrange:expanded
sed -i '184s/\\label{eq:aether:euler\-lagrange}/\\label{eq:aether:euler-lagrange:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 177: eq:aether:lagrangian-foam -> eq:aether:lagrangian-foam:expanded
sed -i '177s/\\label{eq:aether:lagrangian\-foam}/\\label{eq:aether:lagrangian-foam:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 170: eq:aether:lagrangian-drive -> eq:aether:lagrangian-drive:expanded
sed -i '170s/\\label{eq:aether:lagrangian\-drive}/\\label{eq:aether:lagrangian-drive:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 163: eq:aether:lagrangian-complete -> eq:aether:lagrangian-complete:expanded
sed -i '163s/\\label{eq:aether:lagrangian\-complete}/\\label{eq:aether:lagrangian-complete:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 154: subsec:aether-scalar:master-equation -> subsec:aether-scalar:master-equation:expanded
sed -i '154s/\\label{subsec:aether\-scalar:master\-equation}/\\label{subsec:aether-scalar:master-equation:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 147: eq:aether:kg-frw -> eq:aether:kg-frw:expanded
sed -i '147s/\\label{eq:aether:kg\-frw}/\\label{eq:aether:kg-frw:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 140: eq:aether:frw-metric -> eq:aether:frw-metric:expanded
sed -i '140s/\\label{eq:aether:frw\-metric}/\\label{eq:aether:frw-metric:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 133: eq:aether:dalembert-expansion -> eq:aether:dalembert-expansion:expanded
sed -i '133s/\\label{eq:aether:dalembert\-expansion}/\\label{eq:aether:dalembert-expansion:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 126: eq:aether:kg-curved-simple -> eq:aether:kg-curved-simple:expanded
sed -i '126s/\\label{eq:aether:kg\-curved\-simple}/\\label{eq:aether:kg-curved-simple:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 119: eq:aether:kg-flat -> eq:aether:kg-flat:expanded
sed -i '119s/\\label{eq:aether:kg\-flat}/\\label{eq:aether:kg-flat:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 113: subsec:aether-scalar:klein-gordon -> subsec:aether-scalar:klein-gordon:expanded
sed -i '113s/\\label{subsec:aether\-scalar:klein\-gordon}/\\label{subsec:aether-scalar:klein-gordon:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 109: sec:aether-scalar:foundations -> sec:aether-scalar:foundations:expanded
sed -i '109s/\\label{sec:aether\-scalar:foundations}/\\label{sec:aether-scalar:foundations:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 101: eq:aether:foam-density -> eq:aether:foam-density:expanded
sed -i '101s/\\label{eq:aether:foam\-density}/\\label{eq:aether:foam-density:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 92: eq:aether:foam-correlation -> eq:aether:foam-correlation:expanded
sed -i '92s/\\label{eq:aether:foam\-correlation}/\\label{eq:aether:foam-correlation:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 85: eq:aether:foam-modified -> eq:aether:foam-modified:expanded
sed -i '85s/\\label{eq:aether:foam\-modified}/\\label{eq:aether:foam-modified:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 78: subsec:aether-scalar:quantum-foam-intro -> subsec:aether-scalar:quantum-foam-intro:expanded
sed -i '78s/\\label{subsec:aether\-scalar:quantum\-foam\-intro}/\\label{subsec:aether-scalar:quantum-foam-intro:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 71: eq:aether:stress-energy-full -> eq:aether:stress-energy-full:expanded
sed -i '71s/\\label{eq:aether:stress\-energy\-full}/\\label{eq:aether:stress-energy-full:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 55: eq:aether:eom-basic -> eq:aether:eom-basic:expanded
sed -i '55s/\\label{eq:aether:eom\-basic}/\\label{eq:aether:eom-basic:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 48: eq:aether:scalar-action -> eq:aether:scalar-action:expanded
sed -i '48s/\\label{eq:aether:scalar\-action}/\\label{eq:aether:scalar-action:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 41: subsec:aether-scalar:modern-theory -> subsec:aether-scalar:modern-theory:expanded
sed -i '41s/\\label{subsec:aether\-scalar:modern\-theory}/\\label{subsec:aether-scalar:modern-theory:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 28: subsec:aether-scalar:history -> subsec:aether-scalar:history:expanded
sed -i '28s/\\label{subsec:aether\-scalar:history}/\\label{subsec:aether-scalar:history:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 24: sec:aether-scalar:intro -> sec:aether-scalar:intro:expanded
sed -i '24s/\\label{sec:aether\-scalar:intro}/\\label{sec:aether-scalar:intro:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex
# Line 16: ch:aether-scalar-fields -> ch:aether-scalar-fields:expanded
sed -i '16s/\\label{ch:aether\-scalar\-fields}/\\label{ch:aether-scalar-fields:expanded}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch07_aether_scalar_fields_expanded.tex

# Fixing chapters/frameworks/ch08_aether_zpe_coupling_backup.tex (7 changes)
echo 'Fixing chapters/frameworks/ch08_aether_zpe_coupling_backup.tex...'
# Line 654: sec:aether-zpe:summary -> sec:aether-zpe:summary:backup
sed -i '654s/\\label{sec:aether\-zpe:summary}/\\label{sec:aether-zpe:summary:backup}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch08_aether_zpe_coupling_backup.tex
# Line 303: subsec:aether-zpe:protocol-casimir -> subsec:aether-zpe:protocol-casimir:backup
sed -i '303s/\\label{subsec:aether\-zpe:protocol\-casimir}/\\label{subsec:aether-zpe:protocol-casimir:backup}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch08_aether_zpe_coupling_backup.tex
# Line 259: subsec:aether-zpe:fractal-enhancement -> subsec:aether-zpe:fractal-enhancement:backup
sed -i '259s/\\label{subsec:aether\-zpe:fractal\-enhancement}/\\label{subsec:aether-zpe:fractal-enhancement:backup}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch08_aether_zpe_coupling_backup.tex
# Line 58: subsec:aether-zpe:casimir-standard -> subsec:aether-zpe:casimir-standard:backup
sed -i '58s/\\label{subsec:aether\-zpe:casimir\-standard}/\\label{subsec:aether-zpe:casimir-standard:backup}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch08_aether_zpe_coupling_backup.tex
# Line 16: ch:aether-zpe-coupling -> ch:aether-zpe-coupling:backup
sed -i '16s/\\label{ch:aether\-zpe\-coupling}/\\label{ch:aether-zpe-coupling:backup}/' /home/eirikr/Playground/PhysicsForge/synthesis/chapters/frameworks/ch08_aether_zpe_coupling_backup.tex

echo 'All fixes applied!'
```

## Complete Duplicate List

### CHAPTER Labels

#### `\label{ch:aether-scalar-fields}`
Occurrences: 3

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:16`
2. `chapters/frameworks/ch07_aether_scalar_fields_backup.tex:16`
   - **Rename to**: `\label{ch:aether-scalar-fields:backup}`
3. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:16`
   - **Rename to**: `\label{ch:aether-scalar-fields:expanded}`

#### `\label{ch:aether-zpe-coupling}`
Occurrences: 2

1. `chapters/frameworks/ch08_aether_zpe_coupling.tex:14`
2. `chapters/frameworks/ch08_aether_zpe_coupling_backup.tex:16`
   - **Rename to**: `\label{ch:aether-zpe-coupling:backup}`

### EQUATION Labels

#### `\label{eq:aether:bekenstein-hawking}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:596`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:595`
   - **Rename to**: `\label{eq:aether:bekenstein-hawking:expanded}`

#### `\label{eq:aether:box-dimension}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:1014`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:1013`
   - **Rename to**: `\label{eq:aether:box-dimension:expanded}`

#### `\label{eq:aether:casimir-enhanced}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:818`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:817`
   - **Rename to**: `\label{eq:aether:casimir-enhanced:expanded}`

#### `\label{eq:aether:cavity-q}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:1111`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:1110`
   - **Rename to**: `\label{eq:aether:cavity-q:expanded}`

#### `\label{eq:aether:cayley-multiplication}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:952`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:951`
   - **Rename to**: `\label{eq:aether:cayley-multiplication:expanded}`

#### `\label{eq:aether:cmb-modification}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:1141`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:1140`
   - **Rename to**: `\label{eq:aether:cmb-modification:expanded}`

#### `\label{eq:aether:coherence-function}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:380`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:379`
   - **Rename to**: `\label{eq:aether:coherence-function:expanded}`

#### `\label{eq:aether:coherence-max}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:387`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:386`
   - **Rename to**: `\label{eq:aether:coherence-max:expanded}`

#### `\label{eq:aether:coupling-value}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:344`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:343`
   - **Rename to**: `\label{eq:aether:coupling-value:expanded}`

#### `\label{eq:aether:cutoff-e8}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:314`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:313`
   - **Rename to**: `\label{eq:aether:cutoff-e8:expanded}`

#### `\label{eq:aether:dalembert-expansion}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:134`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:133`
   - **Rename to**: `\label{eq:aether:dalembert-expansion:expanded}`

#### `\label{eq:aether:decoherence-rate}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:1063`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:1062`
   - **Rename to**: `\label{eq:aether:decoherence-rate:expanded}`

#### `\label{eq:aether:dimensional-resonance}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:579`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:578`
   - **Rename to**: `\label{eq:aether:dimensional-resonance:expanded}`

#### `\label{eq:aether:dtc-hamiltonian}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:673`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:672`
   - **Rename to**: `\label{eq:aether:dtc-hamiltonian:expanded}`

#### `\label{eq:aether:e8-coupling}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:569`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:568`
   - **Rename to**: `\label{eq:aether:e8-coupling:expanded}`

#### `\label{eq:aether:e8-dimension}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:991`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:990`
   - **Rename to**: `\label{eq:aether:e8-dimension:expanded}`

#### `\label{eq:aether:e8-expansion}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:543`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:542`
   - **Rename to**: `\label{eq:aether:e8-expansion:expanded}`

#### `\label{eq:aether:entanglement-protection}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:1081`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:1080`
   - **Rename to**: `\label{eq:aether:entanglement-protection:expanded}`

#### `\label{eq:aether:entropy-evolution}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:634`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:633`
   - **Rename to**: `\label{eq:aether:entropy-evolution:expanded}`

#### `\label{eq:aether:entropy-oscillation}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:643`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:642`
   - **Rename to**: `\label{eq:aether:entropy-oscillation:expanded}`

#### `\label{eq:aether:eom-basic}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:56`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:55`
   - **Rename to**: `\label{eq:aether:eom-basic:expanded}`

#### `\label{eq:aether:epsilon-slowroll}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:229`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:228`
   - **Rename to**: `\label{eq:aether:epsilon-slowroll:expanded}`

#### `\label{eq:aether:equation-of-state}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:1123`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:1122`
   - **Rename to**: `\label{eq:aether:equation-of-state:expanded}`

#### `\label{eq:aether:eta-slowroll}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:230`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:229`
   - **Rename to**: `\label{eq:aether:eta-slowroll:expanded}`

#### `\label{eq:aether:euler-lagrange}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:185`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:184`
   - **Rename to**: `\label{eq:aether:euler-lagrange:expanded}`

#### `\label{eq:aether:f4-dimension}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:982`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:981`
   - **Rename to**: `\label{eq:aether:f4-dimension:expanded}`

#### `\label{eq:aether:floquet-hamiltonian}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:661`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:660`
   - **Rename to**: `\label{eq:aether:floquet-hamiltonian:expanded}`

#### `\label{eq:aether:foam-correlation}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:93`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:92`
   - **Rename to**: `\label{eq:aether:foam-correlation:expanded}`

#### `\label{eq:aether:foam-density}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:102`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:101`
   - **Rename to**: `\label{eq:aether:foam-density:expanded}`

#### `\label{eq:aether:foam-density-param}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:420`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:419`
   - **Rename to**: `\label{eq:aether:foam-density-param:expanded}`

#### `\label{eq:aether:foam-function}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:368`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:367`
   - **Rename to**: `\label{eq:aether:foam-function:expanded}`

#### `\label{eq:aether:foam-modified}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:86`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:85`
   - **Rename to**: `\label{eq:aether:foam-modified:expanded}`

#### `\label{eq:aether:foam-uncertainty}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:404`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:403`
   - **Rename to**: `\label{eq:aether:foam-uncertainty:expanded}`

#### `\label{eq:aether:fractal-dimension}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:250`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:249`
   - **Rename to**: `\label{eq:aether:fractal-dimension:expanded}`

#### `\label{eq:aether:fractal-potential}`
Occurrences: 3

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:241`
2. `chapters/frameworks/ch07_aether_scalar_fields_backup.tex:57`
   - **Rename to**: `\label{eq:aether:fractal-potential:backup}`
3. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:240`
   - **Rename to**: `\label{eq:aether:fractal-potential:expanded}`

#### `\label{eq:aether:frw-metric}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:141`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:140`
   - **Rename to**: `\label{eq:aether:frw-metric:expanded}`

#### `\label{eq:aether:g2-dimension}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:973`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:972`
   - **Rename to**: `\label{eq:aether:g2-dimension:expanded}`

#### `\label{eq:aether:gate-fidelity}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:1072`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:1071`
   - **Rename to**: `\label{eq:aether:gate-fidelity:expanded}`

#### `\label{eq:aether:genesis-map}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:1159`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:1158`
   - **Rename to**: `\label{eq:aether:genesis-map:expanded}`

#### `\label{eq:aether:gut-unification}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:1186`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:1185`
   - **Rename to**: `\label{eq:aether:gut-unification:expanded}`

#### `\label{eq:aether:hausdorff-measure}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:1005`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:1004`
   - **Rename to**: `\label{eq:aether:hausdorff-measure:expanded}`

#### `\label{eq:aether:ho-energy}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:298`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:297`
   - **Rename to**: `\label{eq:aether:ho-energy:expanded}`

#### `\label{eq:aether:hopf-invariant}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:1035`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:1034`
   - **Rename to**: `\label{eq:aether:hopf-invariant:expanded}`

#### `\label{eq:aether:information-density}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:615`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:614`
   - **Rename to**: `\label{eq:aether:information-density:expanded}`

#### `\label{eq:aether:information-max}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:624`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:623`
   - **Rename to**: `\label{eq:aether:information-max:expanded}`

#### `\label{eq:aether:kg-curved-simple}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:127`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:126`
   - **Rename to**: `\label{eq:aether:kg-curved-simple:expanded}`

#### `\label{eq:aether:kg-flat}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:120`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:119`
   - **Rename to**: `\label{eq:aether:kg-flat:expanded}`

#### `\label{eq:aether:kg-frw}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:148`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:147`
   - **Rename to**: `\label{eq:aether:kg-frw:expanded}`

#### `\label{eq:aether:kk-decomposition}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:523`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:522`
   - **Rename to**: `\label{eq:aether:kk-decomposition:expanded}`

#### `\label{eq:aether:kk-mass}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:530`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:529`
   - **Rename to**: `\label{eq:aether:kk-mass:expanded}`

#### `\label{eq:aether:lagrangian-complete}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:164`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:163`
   - **Rename to**: `\label{eq:aether:lagrangian-complete:expanded}`

#### `\label{eq:aether:lagrangian-drive}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:171`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:170`
   - **Rename to**: `\label{eq:aether:lagrangian-drive:expanded}`

#### `\label{eq:aether:lagrangian-foam}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:178`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:177`
   - **Rename to**: `\label{eq:aether:lagrangian-foam:expanded}`

#### `\label{eq:aether:lattice-spacing}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:436`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:435`
   - **Rename to**: `\label{eq:aether:lattice-spacing:expanded}`

#### `\label{eq:aether:master-derived}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:199`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:198`
   - **Rename to**: `\label{eq:aether:master-derived:expanded}`

#### `\label{eq:aether:metric-fluctuations}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:411`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:410`
   - **Rename to**: `\label{eq:aether:metric-fluctuations:expanded}`

#### `\label{eq:aether:mexican-hat}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:262`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:261`
   - **Rename to**: `\label{eq:aether:mexican-hat:expanded}`

#### `\label{eq:aether:mode-product}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:959`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:958`
   - **Rename to**: `\label{eq:aether:mode-product:expanded}`

#### `\label{eq:aether:modulated-entropy}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:603`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:602`
   - **Rename to**: `\label{eq:aether:modulated-entropy:expanded}`

#### `\label{eq:aether:monopole}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:471`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:470`
   - **Rename to**: `\label{eq:aether:monopole:expanded}`

#### `\label{eq:aether:origami-equivalence}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:1168`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:1167`
   - **Rename to**: `\label{eq:aether:origami-equivalence:expanded}`

#### `\label{eq:aether:origami-projection}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields_backup.tex:275`
2. `chapters/frameworks/ch10_aether_kernel_equations.tex:772`
   - **Rename to**: `\label{eq:aether:ch10:origami-projection}`

#### `\label{eq:aether:pais-modification}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:1179`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:1178`
   - **Rename to**: `\label{eq:aether:pais-modification:expanded}`

#### `\label{eq:aether:period-doubling}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:680`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:679`
   - **Rename to**: `\label{eq:aether:period-doubling:expanded}`

#### `\label{eq:aether:phonon-dispersion}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:448`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:447`
   - **Rename to**: `\label{eq:aether:phonon-dispersion:expanded}`

#### `\label{eq:aether:phonon-dos}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:457`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:456`
   - **Rename to**: `\label{eq:aether:phonon-dos:expanded}`

#### `\label{eq:aether:phonon-modification}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:755`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:754`
   - **Rename to**: `\label{eq:aether:phonon-modification:expanded}`

#### `\label{eq:aether:pontryagin}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:1044`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:1043`
   - **Rename to**: `\label{eq:aether:pontryagin:expanded}`

#### `\label{eq:aether:power-transfer}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:354`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:353`
   - **Rename to**: `\label{eq:aether:power-transfer:expanded}`

#### `\label{eq:aether:rectification}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:1102`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:1101`
   - **Rename to**: `\label{eq:aether:rectification:expanded}`

#### `\label{eq:aether:scalar-action}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:49`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:48`
   - **Rename to**: `\label{eq:aether:scalar-action:expanded}`

#### `\label{eq:aether:scalar-zpe-coupling}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields_backup.tex:311`
2. `modules/equations/eq_aether_scalar_zpe_coupling.tex:11`
   - **Rename to**: `\label{eq:aether:scalar-zpe-coupling:mod_aether_coupling}`

#### `\label{eq:aether:slow-roll-potential}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:223`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:222`
   - **Rename to**: `\label{eq:aether:slow-roll-potential:expanded}`

#### `\label{eq:aether:ssb-expansion}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:282`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:281`
   - **Rename to**: `\label{eq:aether:ssb-expansion:expanded}`

#### `\label{eq:aether:ssb-minimum-condition}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:269`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:268`
   - **Rename to**: `\label{eq:aether:ssb-minimum-condition:expanded}`

#### `\label{eq:aether:stress-energy-full}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:72`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:71`
   - **Rename to**: `\label{eq:aether:stress-energy-full:expanded}`

#### `\label{eq:aether:string}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:480`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:479`
   - **Rename to**: `\label{eq:aether:string:expanded}`

#### `\label{eq:aether:structure-growth}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:1132`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:1131`
   - **Rename to**: `\label{eq:aether:structure-growth:expanded}`

#### `\label{eq:aether:tc-coupling}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:699`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:698`
   - **Rename to**: `\label{eq:aether:tc-coupling:expanded}`

#### `\label{eq:aether:vev}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:275`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:274`
   - **Rename to**: `\label{eq:aether:vev:expanded}`

#### `\label{eq:aether:wall}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:489`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:488`
   - **Rename to**: `\label{eq:aether:wall:expanded}`

#### `\label{eq:aether:winding-number}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:1028`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:1027`
   - **Rename to**: `\label{eq:aether:winding-number:expanded}`

#### `\label{eq:aether:zpe-effective}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:337`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:336`
   - **Rename to**: `\label{eq:aether:zpe-effective:expanded}`

#### `\label{eq:aether:zpe-efficiency}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:1093`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:1092`
   - **Rename to**: `\label{eq:aether:zpe-efficiency:expanded}`

#### `\label{eq:aether:zpe-finite}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:321`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:320`
   - **Rename to**: `\label{eq:aether:zpe-finite:expanded}`

#### `\label{eq:aether:zpe-integral}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:305`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:304`
   - **Rename to**: `\label{eq:aether:zpe-integral:expanded}`

### SECTION Labels

#### `\label{sec:aether-scalar:advanced-math}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:927`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:926`
   - **Rename to**: `\label{sec:aether-scalar:advanced-math:expanded}`

#### `\label{sec:aether-scalar:applications}`
Occurrences: 3

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:1052`
2. `chapters/frameworks/ch07_aether_scalar_fields_backup.tex:372`
   - **Rename to**: `\label{sec:aether-scalar:applications:backup}`
3. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:1051`
   - **Rename to**: `\label{sec:aether-scalar:applications:expanded}`

#### `\label{sec:aether-scalar:connections}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:1149`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:1148`
   - **Rename to**: `\label{sec:aether-scalar:connections:expanded}`

#### `\label{sec:aether-scalar:dimensional}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:497`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:496`
   - **Rename to**: `\label{sec:aether-scalar:dimensional:expanded}`

#### `\label{sec:aether-scalar:entropy}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:587`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:586`
   - **Rename to**: `\label{sec:aether-scalar:entropy:expanded}`

#### `\label{sec:aether-scalar:foundations}`
Occurrences: 3

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:110`
2. `chapters/frameworks/ch07_aether_scalar_fields_backup.tex:22`
   - **Rename to**: `\label{sec:aether-scalar:foundations:backup}`
3. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:109`
   - **Rename to**: `\label{sec:aether-scalar:foundations:expanded}`

#### `\label{sec:aether-scalar:intro}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:25`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:24`
   - **Rename to**: `\label{sec:aether-scalar:intro:expanded}`

#### `\label{sec:aether-scalar:protocols}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:709`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:708`
   - **Rename to**: `\label{sec:aether-scalar:protocols:expanded}`

#### `\label{sec:aether-scalar:quantum-foam}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:395`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:394`
   - **Rename to**: `\label{sec:aether-scalar:quantum-foam:expanded}`

#### `\label{sec:aether-scalar:summary}`
Occurrences: 3

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:1192`
2. `chapters/frameworks/ch07_aether_scalar_fields_backup.tex:666`
   - **Rename to**: `\label{sec:aether-scalar:summary:backup}`
3. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:1191`
   - **Rename to**: `\label{sec:aether-scalar:summary:expanded}`

#### `\label{sec:aether-scalar:time-crystals}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:651`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:650`
   - **Rename to**: `\label{sec:aether-scalar:time-crystals:expanded}`

#### `\label{sec:aether-scalar:zpe-dynamics}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:289`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:288`
   - **Rename to**: `\label{sec:aether-scalar:zpe-dynamics:expanded}`

#### `\label{sec:aether-zpe:summary}`
Occurrences: 2

1. `chapters/frameworks/ch08_aether_zpe_coupling.tex:1187`
2. `chapters/frameworks/ch08_aether_zpe_coupling_backup.tex:654`
   - **Rename to**: `\label{sec:aether-zpe:summary:backup}`

### SUBSECTION Labels

#### `\label{subsec:aether-scalar:cayley-dickson}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:931`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:930`
   - **Rename to**: `\label{subsec:aether-scalar:cayley-dickson:expanded}`

#### `\label{subsec:aether-scalar:coherence}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:375`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:374`
   - **Rename to**: `\label{subsec:aether-scalar:coherence:expanded}`

#### `\label{subsec:aether-scalar:continuous-time}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:685`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:684`
   - **Rename to**: `\label{subsec:aether-scalar:continuous-time:expanded}`

#### `\label{subsec:aether-scalar:cosmology}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:1118`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:1117`
   - **Rename to**: `\label{subsec:aether-scalar:cosmology:expanded}`

#### `\label{subsec:aether-scalar:defects}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:464`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:463`
   - **Rename to**: `\label{subsec:aether-scalar:defects:expanded}`

#### `\label{subsec:aether-scalar:discrete-time}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:668`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:667`
   - **Rename to**: `\label{subsec:aether-scalar:discrete-time:expanded}`

#### `\label{subsec:aether-scalar:e8-constraints}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:537`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:536`
   - **Rename to**: `\label{subsec:aether-scalar:e8-constraints:expanded}`

#### `\label{subsec:aether-scalar:energy-harvesting}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:1088`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:1087`
   - **Rename to**: `\label{subsec:aether-scalar:energy-harvesting:expanded}`

#### `\label{subsec:aether-scalar:energy-transfer}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:349`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:348`
   - **Rename to**: `\label{subsec:aether-scalar:energy-transfer:expanded}`

#### `\label{subsec:aether-scalar:entropy-dynamics}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:629`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:628`
   - **Rename to**: `\label{subsec:aether-scalar:entropy-dynamics:expanded}`

#### `\label{subsec:aether-scalar:foam-structure}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:399`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:398`
   - **Rename to**: `\label{subsec:aether-scalar:foam-structure:expanded}`

#### `\label{subsec:aether-scalar:fractal-measure}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:998`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:997`
   - **Rename to**: `\label{subsec:aether-scalar:fractal-measure:expanded}`

#### `\label{subsec:aether-scalar:fractal-potential}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:236`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:235`
   - **Rename to**: `\label{subsec:aether-scalar:fractal-potential:expanded}`

#### `\label{subsec:aether-scalar:future}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:1225`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:1224`
   - **Rename to**: `\label{subsec:aether-scalar:future:expanded}`

#### `\label{subsec:aether-scalar:genesis}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:1153`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:1152`
   - **Rename to**: `\label{subsec:aether-scalar:genesis:expanded}`

#### `\label{subsec:aether-scalar:hierarchy}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:501`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:500`
   - **Rename to**: `\label{subsec:aether-scalar:hierarchy:expanded}`

#### `\label{subsec:aether-scalar:history}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:29`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:28`
   - **Rename to**: `\label{subsec:aether-scalar:history:expanded}`

#### `\label{subsec:aether-scalar:holographic}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:591`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:590`
   - **Rename to**: `\label{subsec:aether-scalar:holographic:expanded}`

#### `\label{subsec:aether-scalar:information}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:610`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:609`
   - **Rename to**: `\label{subsec:aether-scalar:information:expanded}`

#### `\label{subsec:aether-scalar:kaluza-klein}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:518`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:517`
   - **Rename to**: `\label{subsec:aether-scalar:kaluza-klein:expanded}`

#### `\label{subsec:aether-scalar:klein-gordon}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:114`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:113`
   - **Rename to**: `\label{subsec:aether-scalar:klein-gordon:expanded}`

#### `\label{subsec:aether-scalar:lattice-formation}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:427`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:426`
   - **Rename to**: `\label{subsec:aether-scalar:lattice-formation:expanded}`

#### `\label{subsec:aether-scalar:lie-groups}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:966`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:965`
   - **Rename to**: `\label{subsec:aether-scalar:lie-groups:expanded}`

#### `\label{subsec:aether-scalar:master-equation}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:155`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:154`
   - **Rename to**: `\label{subsec:aether-scalar:master-equation:expanded}`

#### `\label{subsec:aether-scalar:modern-theory}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:42`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:41`
   - **Rename to**: `\label{subsec:aether-scalar:modern-theory:expanded}`

#### `\label{subsec:aether-scalar:pais}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:1173`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:1172`
   - **Rename to**: `\label{subsec:aether-scalar:pais:expanded}`

#### `\label{subsec:aether-scalar:phonons}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:443`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:442`
   - **Rename to**: `\label{subsec:aether-scalar:phonons:expanded}`

#### `\label{subsec:aether-scalar:potentials-detailed}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:206`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:205`
   - **Rename to**: `\label{subsec:aether-scalar:potentials-detailed:expanded}`

#### `\label{subsec:aether-scalar:protocol-casimir}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:793`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:792`
   - **Rename to**: `\label{subsec:aether-scalar:protocol-casimir:expanded}`

#### `\label{subsec:aether-scalar:protocol-dimensional}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:862`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:861`
   - **Rename to**: `\label{subsec:aether-scalar:protocol-dimensional:expanded}`

#### `\label{subsec:aether-scalar:protocol-entropy}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:830`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:829`
   - **Rename to**: `\label{subsec:aether-scalar:protocol-entropy:expanded}`

#### `\label{subsec:aether-scalar:protocol-foam}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:762`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:761`
   - **Rename to**: `\label{subsec:aether-scalar:protocol-foam:expanded}`

#### `\label{subsec:aether-scalar:protocol-time-crystal}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:894`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:893`
   - **Rename to**: `\label{subsec:aether-scalar:protocol-time-crystal:expanded}`

#### `\label{subsec:aether-scalar:protocol-vibration}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:713`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:712`
   - **Rename to**: `\label{subsec:aether-scalar:protocol-vibration:expanded}`

#### `\label{subsec:aether-scalar:quantum-computing}`
Occurrences: 3

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:1056`
2. `chapters/frameworks/ch07_aether_scalar_fields_backup.tex:412`
   - **Rename to**: `\label{subsec:aether-scalar:quantum-computing:backup}`
3. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:1055`
   - **Rename to**: `\label{subsec:aether-scalar:quantum-computing:expanded}`

#### `\label{subsec:aether-scalar:quantum-foam-intro}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:79`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:78`
   - **Rename to**: `\label{subsec:aether-scalar:quantum-foam-intro:expanded}`

#### `\label{subsec:aether-scalar:questions}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:1212`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:1211`
   - **Rename to**: `\label{subsec:aether-scalar:questions:expanded}`

#### `\label{subsec:aether-scalar:resonance}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:574`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:573`
   - **Rename to**: `\label{subsec:aether-scalar:resonance:expanded}`

#### `\label{subsec:aether-scalar:ssb}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:257`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:256`
   - **Rename to**: `\label{subsec:aether-scalar:ssb:expanded}`

#### `\label{subsec:aether-scalar:time-crystal-coupling}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:694`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:693`
   - **Rename to**: `\label{subsec:aether-scalar:time-crystal-coupling:expanded}`

#### `\label{subsec:aether-scalar:time-crystal-formation}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:655`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:654`
   - **Rename to**: `\label{subsec:aether-scalar:time-crystal-formation:expanded}`

#### `\label{subsec:aether-scalar:topology}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:1021`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:1020`
   - **Rename to**: `\label{subsec:aether-scalar:topology:expanded}`

#### `\label{subsec:aether-scalar:zpe-coupling-mechanism}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:328`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:327`
   - **Rename to**: `\label{subsec:aether-scalar:zpe-coupling-mechanism:expanded}`

#### `\label{subsec:aether-scalar:zpe-foundations}`
Occurrences: 2

1. `chapters/frameworks/ch07_aether_scalar_fields.tex:293`
2. `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex:292`
   - **Rename to**: `\label{subsec:aether-scalar:zpe-foundations:expanded}`

#### `\label{subsec:aether-zpe:casimir-standard}`
Occurrences: 2

1. `chapters/frameworks/ch08_aether_zpe_coupling.tex:317`
2. `chapters/frameworks/ch08_aether_zpe_coupling_backup.tex:58`
   - **Rename to**: `\label{subsec:aether-zpe:casimir-standard:backup}`

#### `\label{subsec:aether-zpe:fractal-enhancement}`
Occurrences: 2

1. `chapters/frameworks/ch08_aether_zpe_coupling.tex:379`
2. `chapters/frameworks/ch08_aether_zpe_coupling_backup.tex:259`
   - **Rename to**: `\label{subsec:aether-zpe:fractal-enhancement:backup}`

#### `\label{subsec:aether-zpe:protocol-casimir}`
Occurrences: 2

1. `chapters/frameworks/ch08_aether_zpe_coupling.tex:628`
2. `chapters/frameworks/ch08_aether_zpe_coupling_backup.tex:303`
   - **Rename to**: `\label{subsec:aether-zpe:protocol-casimir:backup}`

## Validation Steps

After running the fix script:

1. **Re-run duplicate finder**:
   ```bash
   python /home/eirikr/Playground/PhysicsForge/find_duplicate_labels.py
   ```

2. **Test compilation**:
   ```bash
   cd /home/eirikr/Playground/PhysicsForge/synthesis
   pdflatex main.tex
   ```

3. **Check for undefined references**:
   ```bash
   grep -n 'Undefined' main.log
   ```

4. **Verify no new duplicates introduced**:
   ```bash
   grep -rn '\\label{' . | sort | uniq -d
   ```

## Files to Consider Removing

The following backup/expanded files contain duplicates and should be reviewed:

- `chapters/frameworks/ch07_aether_scalar_fields_backup.tex`
- `chapters/frameworks/ch07_aether_scalar_fields_expanded.tex`
- `chapters/frameworks/ch08_aether_zpe_coupling_backup.tex`

Consider removing these files or moving them to an archive directory.
