#!/usr/bin/env python3
"""
Merge duplicate bibliography entries and update citations in chapters.
"""

import re
import sys
import os
from pathlib import Path

# Duplicate mappings: OLD_KEY -> NEW_KEY
DUPLICATES = {
    # Group 1
    'Mi2022GoogleTC': 'Mi2022TimeCrystal',
    # Group 2
    'MarraniEtAl2021G2Extension': 'Marrani2021G2Extension',
    # Group 3
    'Perlman2014QuantumGravityConstraints': 'Perlman2014QuantumGravity',
    # Group 4
    'Vasileiou2015LorentzFuzziness': 'Vasileiou2015Lorentz',
    # Group 5
    'Bartlett2021PhotonMassConstraints': 'Bartlett2021PhotonMass',
    # Group 6, 7 - same keys, pick one
    # Group 8 - same keys, pick one
    # Group 9
    'QuantumEnhancedDarkEnergy2023': 'QuantumEnhancedScreening2023',
    # Group 10, 11, 12 - same keys, pick one
    # Group 13
    'SolarSystemScalarTensor2020': 'Deng2020SolarSystemScalar',
    # Group 14
    'GWScalarTensor2018': 'OdintsovOikonomou2018GWST',
    # Group 15
    'FifthForce2020': 'Zhou2020FifthForce',
    # Group 16
    'OSIRIS2024': 'OSIRIS2024Bennu',
    # Group 17
    'TorsionBalance2024': 'TorsionBalance2024Scalar',
    # Group 18
    'Else2016FloqTC': 'Else2016Floquet',
    'ElseBauerNayak2016Floquet': 'Else2016Floquet',
    # Group 19
    'Zhang2017IonDTC': 'Zhang2017TrappedIons',
    # Group 20
    'Kyprianidis2021PreThermalDTC': 'Kyprianidis2021Prethermal',
    # Group 21
    'Polariton2024TC': 'Polariton2024TCCQC',
    # Group 22
    'RydbergDissipative2024': 'RydbergDissipative2024TC',
    # Group 23
    'SmitsEtAl2018SpacetimeTC': 'SuperfluidSpaceTime2018',
    # Group 24
    'Autti2018HeliumTimeQuasicrystal': 'Autti2018Helium3',
    # Group 25
    'Lamoreaux1997CasimirMeasurement': 'Lamoreaux1997',
    # Group 26 - same keys
    # Group 27
    'Ciufolini2004LAGEOS': 'Ciufolini1998LenseThirring',
    # Group 28
    'Capasso2007CasimirForce': 'Munday2009RepulsiveCasimir',
    # Group 29
    'Alcubierre1994': 'Alcubierre1994WarpDrive',
    # Group 30
    'PfenningFord1997': 'Pfenning1997WarpOptimization',
    # Group 31
    'MorrisThorne1988': 'MorrisThorne1988Wormholes',
    # Group 32
    'DESI2024BAO': 'DESI2024',
    # Group 33
    'GarciaEtxebarria2022E9': 'GarciaEtxebarriaEtAl2022E9',
    # Group 34
    'Basile2025NonSUSY': 'BasileEtAl2025NonSUSY',
    # Group 35
    'Zamolodchikov1989': 'Zamolodchikov1989Integrable',
    # Group 36
    'Forestano2023MachineLearning': 'ForesranoEtAl2023MachineLearningE6',
    # Group 37
    'Todorov2018Jordan': 'TodorovDrenska2018F4JordanAlgebra',
    # Group 38
    'Todorov2022Octonions': 'Todorov2023OctonionSM',
    # Group 39 - same keys
    # Group 40
    'Jackson2019OctonionsProperTime': 'Jackson2019Octonions',
    # Group 41
    'Dixon1994DivisionAlgebrasBook': 'Dixon1994DivisionAlgebras',
    # Group 42
    'Dixon2010SpinorsIdempotents': 'Dixon2010Spinors',
    # Group 43
    'LustEtAl2010NonassociativeGravity': 'Lust2010Nonassociative',
    # Group 44
    'Mylonas2018Nonassociative': 'MylonasEtAl2018NonassociativeDiffGeom',
    # Group 45
    'Perlman2016QuasarConstraints': 'Perlman2016Extended',
    # Group 46
    'Ofengeim2025CurvatureQG': 'Ofengeim2025Curvature',
    # Group 47
    'NgPerlman2022SpacetimeFoamReview': 'Ng2022Review',
    # Group 48
    'DESI2024PhysicsConstraints': 'DESI2024Physics',
    # Group 49, 50, 51, 52 - same keys
    # Group 53
    'MICROSCOPE2021': 'MICROSCOPE2021FifthForce',
    # Group 54
    'NobleGas2024TCCQC': 'NobleGas2024TC',
    # Group 55
    'GravityAtomInterferometry2019': 'AtomInterferometry2019Gravimetry',
    # Group 56
    'CasimirEffect1948': 'Casimir1948Original',
    'Casimir1948': 'Casimir1948Original',
    'Casimir1948Force': 'Casimir1948Original',
}

def update_citations_in_file(filepath, replacements):
    """Update citations in a LaTeX file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    changes = []

    for old_key, new_key in replacements.items():
        # Match \cite{old_key} and \cite{...old_key...}
        patterns = [
            (rf'\\cite\{{{old_key}\}}', rf'\\cite{{{new_key}}}'),
            (rf'\\cite\{{([^}}]*,\s*){old_key}(,\s*[^}}]*)\}}', rf'\\cite{{\1{new_key}\2}}'),
            (rf'\\cite\{{{old_key}(,\s*[^}}]*)\}}', rf'\\cite{{{new_key}\1}}'),
            (rf'\\cite\{{([^}}]*,\s*){old_key}\}}', rf'\\cite{{\1{new_key}}}'),
        ]

        for pattern, replacement in patterns:
            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content)
                changes.append(f"  {old_key} -> {new_key}")

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return changes
    return []

def remove_bibtex_entry(bib_content, key):
    """Remove a BibTeX entry by key."""
    # Match @type{key, ... }
    pattern = rf'@\w+\{{{key},\s*\n.*?\n\}}'
    match = re.search(pattern, bib_content, re.DOTALL)
    if match:
        return bib_content.replace(match.group(0), '')
    return bib_content

def main():
    repo_root = Path(__file__).parent.parent.parent
    synthesis_dir = repo_root / 'synthesis'
    chapters_dir = synthesis_dir / 'chapters'
    bib_file = synthesis_dir / 'bibliography.bib'

    print("="*80)
    print("BIBLIOGRAPHY MERGE SCRIPT")
    print("="*80)

    # Step 1: Update citations in chapter files
    print("\n[1] Updating citations in chapter files...")
    chapter_files = sorted(chapters_dir.glob('chapter*.tex'))

    total_changes = 0
    for chapter_file in chapter_files:
        changes = update_citations_in_file(chapter_file, DUPLICATES)
        if changes:
            print(f"\n{chapter_file.name}:")
            for change in set(changes):
                print(change)
                total_changes += 1

    print(f"\nTotal citation updates: {total_changes}")

    # Step 2: Remove duplicate entries from bibliography
    print("\n[2] Removing duplicate entries from bibliography...")

    with open(bib_file, 'r', encoding='utf-8') as f:
        bib_content = f.read()

    original_count = len(re.findall(r'@\w+\{', bib_content))
    print(f"Original entries: {original_count}")

    removed_keys = []
    for old_key in DUPLICATES.keys():
        new_content = remove_bibtex_entry(bib_content, old_key)
        if new_content != bib_content:
            removed_keys.append(old_key)
            bib_content = new_content

    with open(bib_file, 'w', encoding='utf-8') as f:
        f.write(bib_content)

    final_count = len(re.findall(r'@\w+\{', bib_content))
    print(f"Entries removed: {len(removed_keys)}")
    print(f"Final entries: {final_count}")

    # Step 3: Verify
    print("\n[3] Verification...")
    print(f"Expected final count: {original_count - len(removed_keys)}")
    print(f"Actual final count: {final_count}")

    if final_count == original_count - len(removed_keys):
        print("SUCCESS: Counts match!")
    else:
        print("WARNING: Count mismatch!")

    # Step 4: Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Duplicate entries merged: {len(DUPLICATES)}")
    print(f"Bibliography entries removed: {len(removed_keys)}")
    print(f"Chapter files updated: {len([f for f in chapter_files if update_citations_in_file(f, DUPLICATES)])}")
    print(f"New bibliography size: {final_count} entries")
    print(f"Line count: {len(bib_content.splitlines())} lines")

    return 0

if __name__ == '__main__':
    sys.exit(main())
