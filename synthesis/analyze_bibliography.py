#!/usr/bin/env python3
"""
Comprehensive bibliography analysis script
Analyzes bibliography.bib for duplicates, undefined citations, format issues, and usage
"""

import re
from pathlib import Path
from collections import defaultdict, Counter
import os

SYNTHESIS_DIR = Path(r"C:\Users\ericj\Git-Projects\Math_Science\synthesis")
BIB_FILE = SYNTHESIS_DIR / "bibliography.bib"

def parse_bibtex(bib_file):
    """Parse BibTeX file and extract all entries"""
    entries = {}
    current_entry = None
    current_key = None
    in_entry = False

    with open(bib_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Find all entries using regex
    pattern = r'@(\w+)\{([^,]+),\s*\n(.*?)\n\}'
    matches = re.finditer(pattern, content, re.DOTALL)

    for match in matches:
        entry_type = match.group(1)
        key = match.group(2).strip()
        fields_text = match.group(3)

        # Parse fields
        fields = {}
        field_pattern = r'(\w+)\s*=\s*[{"](.*?)["}](?=,\s*\w+\s*=|$)'
        for field_match in re.finditer(field_pattern, fields_text, re.DOTALL):
            field_name = field_match.group(1).lower()
            field_value = field_match.group(2).strip()
            fields[field_name] = field_value

        entries[key] = {
            'type': entry_type,
            'key': key,
            'fields': fields
        }

    return entries

def find_duplicates(entries):
    """Find duplicate entries based on DOI, title, or author+year"""
    duplicates = []

    # Group by DOI
    doi_groups = defaultdict(list)
    title_groups = defaultdict(list)
    author_year_groups = defaultdict(list)

    for key, entry in entries.items():
        fields = entry['fields']

        # Group by DOI
        if 'doi' in fields:
            doi = fields['doi'].strip().lower()
            doi_groups[doi].append(key)

        # Group by title (normalized)
        if 'title' in fields:
            title = re.sub(r'\W+', '', fields['title'].lower())
            title_groups[title].append(key)

        # Group by author+year
        if 'author' in fields and 'year' in fields:
            author_key = re.sub(r'\W+', '', fields['author'].lower()[:50])
            year = fields['year']
            author_year_groups[f"{author_key}_{year}"].append(key)

    # Report duplicates
    for doi, keys in doi_groups.items():
        if len(keys) > 1:
            duplicates.append(('DOI', doi, keys))

    for title, keys in title_groups.items():
        if len(keys) > 1:
            duplicates.append(('Title', title[:50], keys))

    for ay, keys in author_year_groups.items():
        if len(keys) > 1:
            duplicates.append(('Author+Year', ay, keys))

    return duplicates

def extract_citations(tex_files):
    """Extract all \cite{} commands from TeX files"""
    citations = []

    for tex_file in tex_files:
        try:
            with open(tex_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # Find all citations
            cite_pattern = r'\\(?:cite|citep|citet|nocite)\{([^}]+)\}'
            matches = re.finditer(cite_pattern, content)

            for match in matches:
                cite_keys = match.group(1).split(',')
                for key in cite_keys:
                    citations.append(key.strip())

        except Exception as e:
            print(f"Warning: Could not read {tex_file}: {e}")

    return citations

def check_citation_validity(citations, entries):
    """Check if all citations exist in bibliography"""
    undefined = []
    citation_counts = Counter(citations)

    for cite_key in citation_counts:
        if cite_key not in entries:
            undefined.append(cite_key)

    return undefined, citation_counts

def check_format_consistency(entries):
    """Check format consistency of bibliography entries"""
    issues = []

    for key, entry in entries.items():
        fields = entry['fields']

        # Check required fields
        if 'author' not in fields and 'editor' not in fields:
            issues.append((key, 'Missing author/editor'))

        if 'title' not in fields:
            issues.append((key, 'Missing title'))

        if 'year' not in fields:
            issues.append((key, 'Missing year'))

        # Check DOI format
        if 'doi' in fields:
            doi = fields['doi']
            if not re.match(r'10\.\d+/', doi):
                issues.append((key, f'Malformed DOI: {doi}'))

    return issues

def main():
    print("=" * 80)
    print("BIBLIOGRAPHY ANALYSIS")
    print("=" * 80)
    print()

    # Parse bibliography
    print(f"Parsing {BIB_FILE}...")
    entries = parse_bibtex(BIB_FILE)
    print(f"Found {len(entries)} bibliography entries")
    print()

    # Find duplicates
    print("=" * 80)
    print("DUPLICATE DETECTION")
    print("=" * 80)
    duplicates = find_duplicates(entries)
    if duplicates:
        print(f"Found {len(duplicates)} potential duplicate groups:")
        for dup_type, dup_id, keys in duplicates[:20]:  # Show first 20
            print(f"  {dup_type}: {keys}")
    else:
        print("No duplicates found")
    print()

    # Extract citations from all chapter files
    print("=" * 80)
    print("CITATION EXTRACTION")
    print("=" * 80)
    chapter_files = list((SYNTHESIS_DIR / "chapters").rglob("*.tex"))
    print(f"Scanning {len(chapter_files)} chapter files...")
    citations = extract_citations(chapter_files)
    print(f"Found {len(citations)} total citations ({len(set(citations))} unique)")
    print()

    # Check citation validity
    print("=" * 80)
    print("CITATION VALIDATION")
    print("=" * 80)
    undefined, citation_counts = check_citation_validity(citations, entries)
    if undefined:
        print(f"Found {len(undefined)} undefined citations:")
        for cite_key in undefined[:20]:  # Show first 20
            print(f"  {cite_key}")
    else:
        print("All citations are defined in bibliography")
    print()

    # Format consistency
    print("=" * 80)
    print("FORMAT CONSISTENCY")
    print("=" * 80)
    issues = check_format_consistency(entries)
    if issues:
        print(f"Found {len(issues)} format issues:")
        for key, issue in issues[:20]:  # Show first 20
            print(f"  {key}: {issue}")
    else:
        print("All entries have consistent formatting")
    print()

    # Usage analysis
    print("=" * 80)
    print("USAGE ANALYSIS")
    print("=" * 80)

    # Count unused entries
    unused = []
    for key in entries:
        if citation_counts[key] == 0:
            unused.append(key)

    print(f"Unused entries: {len(unused)} ({len(unused)/len(entries)*100:.1f}%)")

    # Top 10 most cited
    print("\nTop 10 most cited works:")
    for cite_key, count in citation_counts.most_common(10):
        if cite_key in entries:
            title = entries[cite_key]['fields'].get('title', 'Unknown')[:60]
            print(f"  {count:3d}x {cite_key:30s} {title}")
    print()

    # Summary statistics
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total bibliography entries:  {len(entries)}")
    print(f"Unique citations in text:    {len(set(citations))}")
    print(f"Undefined citations:         {len(undefined)}")
    print(f"Unused entries:              {len(unused)} ({len(unused)/len(entries)*100:.1f}%)")
    print(f"Potential duplicates:        {len(duplicates)}")
    print(f"Format issues:               {len(issues)}")
    print()

    # Save results
    with open(SYNTHESIS_DIR / 'bibliography_analysis.txt', 'w') as f:
        f.write("BIBLIOGRAPHY ANALYSIS REPORT\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Total entries: {len(entries)}\n")
        f.write(f"Undefined citations: {len(undefined)}\n")
        if undefined:
            f.write("\nUndefined citations:\n")
            for cite_key in undefined:
                f.write(f"  {cite_key}\n")
        f.write(f"\nUnused entries: {len(unused)}\n")
        if unused[:50]:
            f.write("\nFirst 50 unused entries:\n")
            for key in unused[:50]:
                f.write(f"  {key}\n")

    print("Results saved to bibliography_analysis.txt")

if __name__ == '__main__':
    main()
