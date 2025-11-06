#!/usr/bin/env python3
"""
Find duplicate bibliography entries by DOI and title.
"""

import re
import sys
from collections import defaultdict

def parse_bibtex(filename):
    """Parse BibTeX file and extract entries."""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all BibTeX entries
    entry_pattern = r'@(\w+)\{([^,]+),\s*\n(.*?)\n\}'
    entries = []

    for match in re.finditer(entry_pattern, content, re.DOTALL):
        entry_type = match.group(1)
        key = match.group(2)
        fields_text = match.group(3)

        # Parse fields
        fields = {}
        field_pattern = r'(\w+)\s*=\s*[{"](.*?)[}"](?:,|\s*$)'
        for field_match in re.finditer(field_pattern, fields_text, re.DOTALL):
            field_name = field_match.group(1).lower()
            field_value = field_match.group(2).strip()
            fields[field_name] = field_value

        entries.append({
            'type': entry_type,
            'key': key,
            'fields': fields,
            'full_text': match.group(0)
        })

    return entries

def normalize_title(title):
    """Normalize title for comparison."""
    # Remove LaTeX commands, punctuation, whitespace
    title = re.sub(r'\\[a-zA-Z]+\{([^}]*)\}', r'\1', title)
    title = re.sub(r'[^a-zA-Z0-9\s]', '', title)
    title = re.sub(r'\s+', ' ', title)
    return title.lower().strip()

def normalize_authors(authors):
    """Normalize author names for comparison."""
    if not authors:
        return ""
    # Remove 'and', extra spaces
    authors = re.sub(r'\s+and\s+', ' ', authors)
    authors = re.sub(r'[^a-zA-Z\s]', '', authors)
    authors = re.sub(r'\s+', ' ', authors)
    return authors.lower().strip()

def find_duplicates(entries):
    """Find duplicate entries by DOI and title."""
    doi_map = defaultdict(list)
    title_map = defaultdict(list)

    for entry in entries:
        # Group by DOI
        doi = entry['fields'].get('doi', '').strip()
        if doi:
            doi_map[doi.lower()].append(entry)

        # Group by normalized title
        title = entry['fields'].get('title', '')
        if title:
            norm_title = normalize_title(title)
            if norm_title:
                title_map[norm_title].append(entry)

    # Find duplicates
    duplicates = []

    # DOI duplicates
    for doi, dup_entries in doi_map.items():
        if len(dup_entries) > 1:
            duplicates.append({
                'type': 'doi',
                'value': doi,
                'entries': dup_entries
            })

    # Title duplicates (exclude those already found by DOI)
    seen_keys = set()
    for doi_dup in duplicates:
        for entry in doi_dup['entries']:
            seen_keys.add(entry['key'])

    for norm_title, dup_entries in title_map.items():
        if len(dup_entries) > 1:
            # Check if not already in DOI duplicates
            keys = [e['key'] for e in dup_entries]
            if not any(k in seen_keys for k in keys):
                duplicates.append({
                    'type': 'title',
                    'value': norm_title,
                    'entries': dup_entries
                })

    return duplicates

def select_canonical(entries):
    """Select canonical entry from duplicates."""
    # Scoring criteria:
    # 1. Has DOI: +10
    # 2. Has journal (not arXiv): +5
    # 3. Has year: +2
    # 4. Has volume/pages: +2
    # 5. Shorter key: +1
    # 6. Complete author list: +1

    scores = []
    for entry in entries:
        score = 0
        fields = entry['fields']

        if fields.get('doi'):
            score += 10

        journal = fields.get('journal', '').lower()
        if journal and 'arxiv' not in journal:
            score += 5

        if fields.get('year'):
            score += 2

        if fields.get('volume') and fields.get('pages'):
            score += 2

        if len(entry['key']) < 30:
            score += 1

        author = fields.get('author', '')
        if 'et al' not in author.lower() and len(author) > 20:
            score += 1

        scores.append((score, entry))

    # Return highest scored entry
    scores.sort(key=lambda x: x[0], reverse=True)
    return scores[0][1]

def main():
    if len(sys.argv) < 2:
        print("Usage: python find_duplicates.py bibliography.bib")
        sys.exit(1)

    filename = sys.argv[1]

    print(f"Parsing {filename}...")
    entries = parse_bibtex(filename)
    print(f"Found {len(entries)} entries")

    print("\nSearching for duplicates...")
    duplicates = find_duplicates(entries)
    print(f"Found {len(duplicates)} duplicate groups")

    # Report duplicates
    print("\n" + "="*80)
    print("DUPLICATE REPORT")
    print("="*80)

    for i, dup in enumerate(duplicates, 1):
        print(f"\n--- Duplicate Group {i} ({dup['type'].upper()}) ---")
        if dup['type'] == 'doi':
            print(f"DOI: {dup['value']}")

        canonical = select_canonical(dup['entries'])

        for entry in dup['entries']:
            is_canonical = (entry['key'] == canonical['key'])
            marker = "[KEEP]" if is_canonical else "[REMOVE]"

            print(f"\n{marker} @{entry['type']}{{{entry['key']},")
            print(f"  Title: {entry['fields'].get('title', 'N/A')[:80]}")
            print(f"  Author: {entry['fields'].get('author', 'N/A')[:80]}")
            print(f"  Year: {entry['fields'].get('year', 'N/A')}")
            print(f"  DOI: {entry['fields'].get('doi', 'N/A')}")
            print(f"  Journal: {entry['fields'].get('journal', 'N/A')[:80]}")

    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Total duplicate groups: {len(duplicates)}")
    total_to_remove = sum(len(d['entries']) - 1 for d in duplicates)
    print(f"Entries to remove: {total_to_remove}")
    print(f"Entries to keep: {len(duplicates)}")
    print(f"New total: {len(entries)} - {total_to_remove} = {len(entries) - total_to_remove}")

    # Generate merge script
    merge_script = "merge_duplicates.txt"
    with open(merge_script, 'w', encoding='utf-8') as f:
        for i, dup in enumerate(duplicates, 1):
            canonical = select_canonical(dup['entries'])
            f.write(f"\n# Duplicate Group {i}\n")
            f.write(f"KEEP: {canonical['key']}\n")
            for entry in dup['entries']:
                if entry['key'] != canonical['key']:
                    f.write(f"REMOVE: {entry['key']}\n")

    print(f"\nMerge instructions written to: {merge_script}")

if __name__ == '__main__':
    main()
