#!/usr/bin/env python3
"""
Strategically add index entries to key chapters.
Target: 200+ entries across 30 chapters.
"""

import re
from pathlib import Path

# Strategic index entries by chapter
CHAPTER_INDEX_MAP = {
    'chapter01': [
        ('Einstein', 'general relativity'),
        ('quantum mechanics', 'quantum mechanics'),
        ('unified field theory', 'unification'),
        ('gauge theory', 'gauge'),
        ('Planck scale', 'Planck'),
    ],
    'chapter02': [
        ('differential geometry', 'differential.*geometry'),
        ('Riemannian manifold', 'Riemannian'),
        ('Lie group', 'Lie group'),
        ('tensor', 'tensor'),
        ('spinor', 'spinor'),
    ],
    'chapter03': [
        ('Cayley-Dickson', 'Cayley-Dickson'),
        ('octonion', 'octonion'),
        ('quaternion', 'quaternion'),
        ('complex number', 'complex number'),
        ('division algebra', 'division algebra'),
    ],
    'chapter04': [
        ('E8 lattice', 'E_?8|E8 lattice'),
        ('exceptional Lie group', 'exceptional'),
        ('E6', 'E_?6'),
        ('E7', 'E_?7'),
        ('F4', 'F_?4'),
        ('G2', 'G_?2'),
    ],
    'chapter05': [
        ('fractal', 'fractal'),
        ('Hausdorff dimension', 'Hausdorff'),
        ('self-similarity', 'self-similar'),
    ],
    'chapter07': [
        ('Aether framework', '[Aa]ether framework'),
        ('scalar field', 'scalar field'),
        ('zero-point energy', 'zero-point|ZPE'),
    ],
    'chapter08': [
        ('vacuum energy', 'vacuum energy'),
        ('quantum fluctuation', 'quantum fluctuation'),
        ('Casimir effect', 'Casimir effect'),
    ],
    'chapter09': [
        ('quantum foam', 'quantum foam'),
        ('spacetime foam', 'spacetime foam'),
        ('Planck length', 'Planck length'),
    ],
    'chapter11': [
        ('Genesis framework', '[Gg]enesis framework'),
        ('nodespace', 'nodespace'),
        ('origami folding', 'origami'),
    ],
    'chapter15': [
        ('Pais', '[Pp]ais'),
        ('Superforce', '[Ss]uperforce'),
        ('GEM', 'GEM'),
        ('Wilczek', 'Wilczek'),
    ],
    'chapter17': [
        ('framework comparison', 'comparison'),
        ('unified kernel', 'unified kernel|master kernel'),
    ],
    'chapter22': [
        ('time crystal', 'time crystal'),
        ('Floquet', 'Floquet'),
        ('discrete time crystal', 'discrete time crystal|DTC'),
    ],
    'chapter23': [
        ('Casimir', 'Casimir'),
        ('Lamoreaux', 'Lamoreaux'),
    ],
    'chapter24': [
        ('LIGO', 'LIGO'),
        ('gravitational wave', 'gravitational wave'),
        ('Gravity Probe B', 'Gravity Probe B'),
    ],
    'chapter25': [
        ('quantum entanglement', 'quantum entanglement'),
        ('Bell inequality', 'Bell'),
    ],
    'chapter26': [
        ('dark matter', 'dark matter'),
        ('dark energy', 'dark energy'),
        ('DESI', 'DESI'),
    ],
    'chapter27': [
        ('quantum computing', 'quantum computing'),
        ('quantum processor', 'quantum processor'),
        ('Google Quantum AI', 'Google.*Quantum'),
    ],
    'chapter28': [
        ('energy harvesting', 'energy harvesting'),
        ('superconducting cavity', 'superconducting'),
    ],
    'chapter29': [
        ('propulsion', 'propulsion'),
        ('inertia reduction', 'inertia'),
    ],
    'chapter30': [
        ('warp drive', 'warp drive'),
        ('Alcubierre', 'Alcubierre'),
        ('wormhole', 'wormhole'),
        ('Morris', 'Morris'),
        ('Thorne', 'Thorne'),
    ],
}

def add_index_entry(content, term, pattern, max_occurrences=3):
    """Add index entry after first few occurrences of a term."""
    added = 0
    matches = list(re.finditer(rf'\b{pattern}\b', content, re.IGNORECASE))

    for match in matches[:max_occurrences]:
        pos = match.end()

        # Check if already indexed
        check_region = content[max(0, pos-100):pos+100]
        if f'\\index{{{term}}}' in check_region:
            continue

        # Check not in comment
        line_start = content.rfind('\n', 0, pos)
        line_end = content.find('\n', pos)
        line = content[line_start:line_end]

        if line.strip().startswith('%'):
            continue

        # Insert index command
        content = content[:pos] + f'\\index{{{term}}}' + content[pos:]
        added += 1

    return content, added

def process_chapter(chapter_path, index_entries):
    """Add strategic index entries to a chapter."""
    with open(chapter_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    stats = {}

    for term, pattern in index_entries:
        content, added = add_index_entry(content, term, pattern)
        if added > 0:
            stats[term] = added

    if content != original_content:
        with open(chapter_path, 'w', encoding='utf-8') as f:
            f.write(content)

    return stats

def main():
    synthesis_dir = Path(__file__).parent.parent
    chapters_dir = synthesis_dir / 'chapters'

    print("="*80)
    print("STRATEGIC INDEX GENERATION")
    print("="*80)

    total_entries = 0
    chapter_stats = {}

    for chapter_name, index_entries in CHAPTER_INDEX_MAP.items():
        chapter_file = chapters_dir / f'{chapter_name}.tex'

        if not chapter_file.exists():
            print(f"\nWarning: {chapter_file.name} not found, skipping...")
            continue

        print(f"\nProcessing {chapter_file.name}...")
        stats = process_chapter(chapter_file, index_entries)

        if stats:
            chapter_stats[chapter_name] = stats
            count = sum(stats.values())
            total_entries += count
            print(f"  Added {count} index entries:")
            for term, num in stats.items():
                print(f"    - {term}: {num}")

    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Chapters processed: {len(CHAPTER_INDEX_MAP)}")
    print(f"Chapters with new entries: {len(chapter_stats)}")
    print(f"Total index entries added: {total_entries}")

    print("\nTo generate the index:")
    print("1. cd synthesis")
    print("2. pdflatex main.tex")
    print("3. makeindex main")
    print("4. pdflatex main.tex")

if __name__ == '__main__':
    main()
