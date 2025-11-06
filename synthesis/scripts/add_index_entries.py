#!/usr/bin/env python3
"""
Add comprehensive index entries to chapters.
Target: 200+ index entries across all chapters.
"""

import re
from pathlib import Path

# Index entries organized by category
INDEX_ENTRIES = {
    # People (with context where they appear)
    'people': {
        'Einstein': r'Einstein(?![\w-])',
        'Casimir': r'Casimir(?![\w-])',
        'Alcubierre': r'Alcubierre(?![\w-])',
        'Pais': r'Pais(?![\w-])',
        'Thorne': r'Thorne(?![\w-])',
        'Wilczek': r'Wilczek(?![\w-])',
        'Hawking': r'Hawking(?![\w-])',
        'Wheeler': r'Wheeler(?![\w-])',
        'Dirac': r'Dirac(?![\w-])',
        'Feynman': r'Feynman(?![\w-])',
        'Penrose': r'Penrose(?![\w-])',
        'Gell-Mann': r'Gell-Mann(?![\w-])',
    },

    # Physics concepts
    'physics': {
        'warp drive': r'warp drive',
        'wormhole': r'wormhole',
        'time crystal': r'time crystal',
        'Casimir effect': r'Casimir effect',
        'zero-point energy': r'zero-point energy|ZPE',
        'quantum foam': r'quantum foam',
        'quantum entanglement': r'quantum entanglement',
        'dark matter': r'dark matter',
        'dark energy': r'dark energy',
        'gravitational wave': r'gravitational wave',
        'black hole': r'black hole',
        'quantum computing': r'quantum computing',
        'quantum coherence': r'quantum coherence',
        'vacuum fluctuation': r'vacuum fluctuation',
        'Planck scale': r'Planck scale',
    },

    # Mathematics
    'mathematics': {
        'Cayley-Dickson': r'Cayley-Dickson',
        'octonion': r'octonion',
        'E8 lattice': r'E8 lattice|E_8',
        'exceptional Lie group': r'exceptional.*Lie|E6|E7|E8|F4|G2',
        'differential geometry': r'differential geometry',
        'Lie algebra': r'Lie algebra',
        'manifold': r'manifold',
        'tensor': r'tensor',
        'spinor': r'spinor',
        'gauge theory': r'gauge theory',
    },

    # Frameworks
    'frameworks': {
        'Aether framework': r'Aether framework',
        'Genesis framework': r'Genesis framework',
        'Pais Superforce': r'Pais.*Superforce',
        'GEM coupling': r'GEM coupling',
        'nodespace': r'nodespace',
    },

    # Experiments
    'experiments': {
        'LIGO': r'LIGO(?![\w-])',
        'LHC': r'LHC(?![\w-])',
        'Gravity Probe B': r'Gravity Probe B',
        'Google Quantum AI': r'Google Quantum AI',
        'Holometer': r'Holometer',
    },

    # Technologies
    'technologies': {
        'superconducting cavity': r'superconducting.*cavit',
        'fractal antenna': r'fractal antenna',
        'metamaterial': r'metamaterial',
        'quantum processor': r'quantum processor',
    },
}

def add_index_to_chapter(chapter_path, dry_run=False):
    """Add index entries to a chapter file."""
    with open(chapter_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    entries_added = {}

    for category, terms in INDEX_ENTRIES.items():
        for term, pattern in terms.items():
            # Check if term already has index
            if f'\\index{{{term}}}' in content:
                continue

            # Find first occurrence (not in comments or already indexed)
            matches = list(re.finditer(pattern, content, re.IGNORECASE))

            if matches:
                # Add index to first occurrence
                match = matches[0]
                pos = match.start()

                # Check if not in comment or already indexed
                line_start = content.rfind('\n', 0, pos) + 1
                line_end = content.find('\n', pos)
                line = content[line_start:line_end]

                if not line.strip().startswith('%') and '\\index{' not in line:
                    # Insert index command right after the term
                    index_cmd = f'\\index{{{term}}}'
                    insert_pos = match.end()

                    content = content[:insert_pos] + index_cmd + content[insert_pos:]

                    if category not in entries_added:
                        entries_added[category] = []
                    entries_added[category].append(term)

    if content != original_content and not dry_run:
        with open(chapter_path, 'w', encoding='utf-8') as f:
            f.write(content)

    return entries_added if content != original_content else {}

def main():
    synthesis_dir = Path(__file__).parent.parent
    chapters_dir = synthesis_dir / 'chapters'

    print("="*80)
    print("INDEX GENERATION SCRIPT")
    print("="*80)
    print("\nAdding index entries to chapters...")

    total_entries = 0
    chapter_stats = {}

    # Process all chapter files
    chapter_files = sorted(chapters_dir.glob('chapter*.tex'))

    for chapter_file in chapter_files:
        print(f"\nProcessing {chapter_file.name}...")
        entries = add_index_to_chapter(chapter_file)

        if entries:
            chapter_stats[chapter_file.name] = entries
            count = sum(len(terms) for terms in entries.values())
            total_entries += count
            print(f"  Added {count} index entries")

            for category, terms in entries.items():
                print(f"    {category}: {', '.join(terms)}")

    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Total chapters processed: {len(chapter_files)}")
    print(f"Chapters with new index entries: {len(chapter_stats)}")
    print(f"Total index entries added: {total_entries}")

    print("\nBreakdown by category:")
    category_totals = {}
    for entries in chapter_stats.values():
        for category, terms in entries.items():
            category_totals[category] = category_totals.get(category, 0) + len(terms)

    for category, count in sorted(category_totals.items()):
        print(f"  {category}: {count}")

    print("\nNext steps:")
    print("1. Run: pdflatex main.tex")
    print("2. Run: makeindex main")
    print("3. Run: pdflatex main.tex")
    print("4. Check main.ind for generated index")

if __name__ == '__main__':
    main()
