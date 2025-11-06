"""
Script to systematically fix undefined cross-references
Handles mapping of old references to correct labels
"""
import re
import os
from pathlib import Path

# Mapping of undefined references to their correct labels (or actions)
# Format: 'undefined_ref': ('action', 'correct_ref_or_chapter_path')

CHAPTER_LABEL_MAPPING = {
    # Chapter references - map old style to correct style
    'ch:zpe_coherence': ('replace', 'ch:zpe-coherence'),
    'ch:aether:overview': ('replace', 'ch:aether-scalar-fields'),
    'ch:aether:experiments': ('replace', 'ch:experimental-setup'),
    'ch:genesis:overview': ('replace', 'ch:genesis-overview'),
    'ch:genesis:experiments': ('replace', 'ch:experimental-setup'),
    'ch:pais:overview': ('replace', 'ch:pais-superforce'),
    'ch:pais:experiments': ('replace', 'ch:experimental-setup'),
    'ch:exceptional-lie': ('replace', 'ch:e8-lattice'),
    'ch:genesis:origami': ('replace', 'ch:origami-folding'),
    'ch:modular': ('replace', 'ch:modular-forms'),
    'ch:aether:kernels': ('replace', 'ch:aether-field-kernels'),
    'ch:unified:dimensional-map': ('replace', 'ch:dimensional-mapping'),
    'ch:fractal': ('replace', 'ch:fractal-geometry'),
    'ch:unified:symmetries': ('replace', 'ch:unified-framework'),
    'ch:aether-scalar': ('replace', 'ch:aether-scalar-fields'),
    'ch:aether-kernels': ('replace', 'ch:aether-field-kernels'),
    'ch:genesis-foundations': ('replace', 'ch:genesis-foundations'),
    'ch:genesis-origami': ('replace', 'ch:origami-folding'),
    'ch:unified-symmetries': ('replace', 'ch:unified-framework'),
    'ch:experiments-e8': ('replace', 'ch:experimental-setup'),
    'ch:experiments-casimir': ('replace', 'ch:experimental-setup'),
    'ch:experiments-time-crystals': ('replace', 'ch:time-crystal-protocols'),
    'ch:aether-zpe': ('replace', 'ch:aether-zpe-coherence'),
    'ch:experiments-lattice': ('replace', 'ch:experimental-setup'),
    'ch:app-propulsion': ('replace', 'ch:advanced-propulsion'),
    'ch:app-quantum-computing': ('replace', 'ch:app-quantum-computing'),
    'ch:app-energy': ('replace', 'ch:energy-harvesting'),
    'ch:unify-cosmology': ('replace', 'ch:cosmology-inflation'),
    'ch:exp-zpe-coherence': ('replace', 'ch:zpe-coherence'),
    'ch:exp-casimir': ('replace', 'ch:experimental-setup'),
    'ch:advanced-topics': ('replace', 'ch:advanced-topics'),
    'ch:exp-tourmaline': ('replace', 'ch:tourmaline-protocol'),
    'ch:unify-emergent-gravity': ('replace', 'ch:emergent-phenomena'),
    'ch:genesis-nodespace': ('replace', 'ch:genesis-foundations'),
    'ch:unify-reconciliation': ('replace', 'ch:conflict-resolution'),
    'ch:exp-numerical': ('replace', 'ch:experimental-setup'),
    'ch:aether-kernel-equations': ('replace', 'ch:aether-field-kernels'),
    'ch:unified-kernels': ('replace', 'ch:unified-kernels'),
    'ch:aether_scalar_dynamics': ('replace', 'ch:aether-scalar-fields'),
    'ch:aether_foam': ('replace', 'ch:aether-scalar-fields'),
    'ch:unified_field_kernel': ('replace', 'ch:unified-kernels'),
    'ch:genesis_kernel_intro': ('replace', 'ch:genesis-foundations'),
    'ch:aether_crystalline': ('replace', 'ch:aether-scalar-fields'),
    'ch:genesis_nodespace': ('replace', 'ch:genesis-foundations'),
    'ch:fifth_force_protocol': ('replace', 'ch:experimental-setup'),
    'ch:unified_validation': ('replace', 'ch:experimental-validation'),
}

SECTION_LABEL_MAPPING = {
    'sec:pais_superforce:summary': ('replace', 'sec:pais-summary'),
}

EQUATION_LABEL_MAPPING = {
    # Ch21 equations that need to be added
    'eq:ch21:cd-to-fractal': ('add_label', 'chapters/unification/ch21_unified_framework.tex'),
    'eq:ch21:fractal-to-negative': ('add_label', 'chapters/unification/ch21_unified_framework.tex'),
    'eq:ch21:lie-cd-correspondence': ('add_label', 'chapters/unification/ch21_unified_framework.tex'),
    'eq:ch21:origami-folding': ('add_label', 'chapters/unification/ch21_unified_framework.tex'),
    'eq:ch21:dimension-energy-hierarchy': ('add_label', 'chapters/unification/ch21_unified_framework.tex'),
}

FIGURE_LABEL_MAPPING = {
    'fig:e8-spectrum': ('add_label', 'chapters/foundations/ch04_e8_lattice.tex'),
    'fig:fractal-potential': ('add_label', 'chapters/foundations/ch05_fractal_geometry.tex'),
    'fig:scalar-evolution': ('add_label', 'chapters/frameworks/ch07_aether_scalar_fields.tex'),
    'fig:casimir-enhancement': ('add_label', 'chapters/experiments/ch22_casimir_force_measurement.tex'),
    'fig:zpe-coherence': ('add_label', 'chapters/experiments/ch24_zpe_coherence.tex'),
    'fig:vibrational-spectroscopy': ('add_label', 'chapters/experiments/ch25_tourmaline_protocol.tex'),
    'fig:dimensional-folding': ('exists', 'modules/figures/fig_dimensional_folding.tex'),  # duplicate
}

def find_undefined_refs():
    """Find all files with undefined references and their locations"""
    undefined_refs = {}

    for tex_file in Path('chapters').rglob('*.tex'):
        try:
            with open(tex_file, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')

                for line_num, line in enumerate(lines, 1):
                    # Find all \ref{} and \eqref{} commands
                    refs = re.findall(r'\\(?:ref|eqref)\{([^}]+)\}', line)
                    for ref in refs:
                        # Check if it's in our undefined list
                        all_undefined = list(CHAPTER_LABEL_MAPPING.keys()) + \
                                      list(SECTION_LABEL_MAPPING.keys()) + \
                                      list(EQUATION_LABEL_MAPPING.keys()) + \
                                      list(FIGURE_LABEL_MAPPING.keys())

                        if ref in all_undefined:
                            if ref not in undefined_refs:
                                undefined_refs[ref] = []
                            undefined_refs[ref].append((str(tex_file), line_num, line.strip()[:100]))
        except Exception as e:
            print(f"Error reading {tex_file}: {e}")

    return undefined_refs

if __name__ == "__main__":
    refs = find_undefined_refs()
    print(f"Found {len(refs)} undefined references to fix:\n")
    for ref, locations in sorted(refs.items()):
        print(f"\n{ref}: ({len(locations)} occurrences)")
        for loc in locations[:3]:  # Show first 3
            print(f"  {loc[0]}:{loc[1]}")
