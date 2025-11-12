import re
import os
from pathlib import Path

def validate_custom_links(notes_dir):
    notes_path = Path(notes_dir)
    all_md_files = list(notes_path.rglob("*.md"))

    found_links = set()
    broken_links = set()

    # Regex to find patterns like [A1] filename.md or [M1] filename.md
    # It captures the filename part
    link_pattern = re.compile(r'\[[A-Z][0-9]\]\s+([a-zA-Z0-9_.-]+\.md)')

    for md_file in all_md_files:
        content = md_file.read_text(encoding='utf-8', errors='ignore')
        matches = link_pattern.findall(content)
        
        for linked_filename in matches:
            found_links.add(linked_filename)
            # Check if the linked file exists relative to the project root
            # This assumes linked files are also in the notes directory or its subdirectories
            # For a more robust check, one might need a mapping of prefixes (A1, M1) to actual paths
            
            # For now, let's assume they are relative to the notes directory
            linked_file_path = notes_path / linked_filename
            if not linked_file_path.exists():
                # If not found directly in notes/, try searching the whole notes/ tree
                # This is a simplified check, a real system would need more context
                found_in_notes_tree = False
                for potential_path in notes_path.rglob(linked_filename):
                    if potential_path.is_file():
                        found_in_notes_tree = True
                        break
                if not found_in_notes_tree:
                    broken_links.add(f"{linked_filename} (referenced in {md_file.relative_to(notes_path)})")

    print(f"Found {len(found_links)} unique custom links.")
    if broken_links:
        print("\n--- BROKEN CUSTOM LINKS ---")
        for link in sorted(broken_links):
            print(f"- {link}")
        return False
    else:
        print("\nAll custom links appear to resolve within the notes directory.")
        return True

if __name__ == "__main__":
    project_root = Path(os.getcwd())
    notes_directory = project_root / "notes"
    
    if not notes_directory.is_dir():
        print(f"Error: Notes directory not found at {notes_directory}")
        exit(1)

    print(f"Validating custom links in {notes_directory}...")
    success = validate_custom_links(notes_directory)
    exit(0 if success else 1)
