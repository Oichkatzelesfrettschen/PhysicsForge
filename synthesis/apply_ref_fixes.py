"""
Script to apply all undefined reference fixes
"""
import re
from pathlib import Path

# Comprehensive mapping of undefined -> correct references
REF_REPLACEMENTS = {
    # Chapter references
    'ch:zpe_coherence': 'ch:scalar_zpe_protocols',
    'ch:aether:overview': 'ch:aether-scalar-fields',
    'ch:aether:experiments': 'ch:scalar_zpe_protocols',
    'ch:genesis:overview': 'ch:genesis-overview',
    'ch:genesis:experiments': 'ch:scalar_zpe_protocols',
    'ch:pais:overview': 'ch:pais_superforce',
    'ch:pais:experiments': 'ch:scalar_zpe_protocols',
    'ch:exceptional-lie': 'ch:exceptional-lie-groups',
    'ch:genesis:origami': 'ch:origami-dimensions',
    'ch:modular': 'ch:genesis-monster',  # modular forms are in ch06
    'ch:aether:kernels': 'ch:aether-kernel',
    'ch:unified:dimensional-map': 'ch:dimensional_mapping',
    'ch:fractal': 'ch:fractal-calculus',
    'ch:unified:symmetries': 'ch:unified_framework',
    'ch:aether-scalar': 'ch:aether-scalar-fields',
    'ch:aether-kernels': 'ch:aether-kernel',
    'ch:genesis-foundations': 'ch:genesis-overview',
    'ch:genesis-origami': 'ch:origami-dimensions',
    'ch:unified-symmetries': 'ch:unified_framework',
    'ch:experiments-e8': 'ch:scalar_zpe_protocols',
    'ch:experiments-casimir': 'ch:scalar_zpe_protocols',
    'ch:experiments-time-crystals': 'ch:time_crystal_protocols',
    'ch:aether-zpe': 'ch:aether-zpe-coupling',
    'ch:experiments-lattice': 'ch:scalar_zpe_protocols',
    'ch:app-propulsion': 'ch:app_propulsion',
    'ch:app-quantum-computing': 'ch:app_quantum_computing',
    'ch:app-energy': 'ch:energy-technologies',
    'ch:unify-cosmology': 'ch:unified_framework',
    'ch:exp-zpe-coherence': 'ch:scalar_zpe_protocols',
    'ch:exp-casimir': 'ch:scalar_zpe_protocols',
    'ch:advanced-topics': 'ch:genesis-monster',
    'ch:exp-tourmaline': 'ch:scalar_zpe_protocols',
    'ch:unify-emergent-gravity': 'ch:unified_framework',
    'ch:genesis-nodespace': 'ch:nodespace-theory',
    'ch:unify-reconciliation': 'ch:conflict_resolution',
    'ch:exp-numerical': 'ch:scalar_zpe_protocols',
    'ch:aether-kernel-equations': 'ch:aether-kernel',
    'ch:unified-kernels': 'ch:unified_kernels',
    'ch:aether_scalar_dynamics': 'ch:aether-scalar-fields',
    'ch:aether_foam': 'ch:aether-scalar-fields',
    'ch:unified_field_kernel': 'ch:unified_kernels',
    'ch:genesis_kernel_intro': 'ch:genesis-overview',
    'ch:aether_crystalline': 'ch:aether-lattice',
    'ch:genesis_nodespace': 'ch:nodespace-theory',
    'ch:fifth_force_protocol': 'ch:scalar_zpe_protocols',
    'ch:unified_validation': 'ch:scalar_zpe_protocols',

    # Section references
    'sec:pais_superforce:summary': 'sec:pais-summary',
}

def replace_refs_in_file(filepath):
    """Replace undefined references in a single file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        replacements_made = []

        for old_ref, new_ref in REF_REPLACEMENTS.items():
            # Pattern to match \ref{old_ref} or \eqref{old_ref}
            pattern = rf'\\(ref|eqref)\{{{re.escape(old_ref)}\}}'

            def replacement(match):
                cmd = match.group(1)
                replacements_made.append(f"{old_ref} -> {new_ref}")
                return f'\\{cmd}{{{new_ref}}}'

            content = re.sub(pattern, replacement, content)

        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return len(set(replacements_made))

        return 0
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return 0

def main():
    """Process all .tex files in chapters/"""
    total_files_changed = 0
    total_replacements = 0

    for tex_file in Path('chapters').rglob('*.tex'):
        # Skip backup and test files
        if any(x in str(tex_file) for x in ['.OLD', '_test', '_NEW', 'backup']):
            continue

        num_replacements = replace_refs_in_file(tex_file)
        if num_replacements > 0:
            total_files_changed += 1
            total_replacements += num_replacements
            print(f"Fixed {num_replacements} reference(s) in {tex_file}")

    print(f"\n=== Summary ===")
    print(f"Files modified: {total_files_changed}")
    print(f"Total reference types fixed: {total_replacements}")

if __name__ == "__main__":
    main()
