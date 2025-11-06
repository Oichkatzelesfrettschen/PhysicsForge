
import os
import hashlib
import argparse
from collections import defaultdict

def hash_file(path):
    """Calculate the SHA256 hash of a file."""
    h = hashlib.sha256()
    try:
        with open(path, 'rb') as f:
            while True:
                data = f.read(65536)  # 64k chunks
                if not data:
                    break
                h.update(data)
        return h.hexdigest()
    except IOError as e:
        print(f"Error reading file {path}: {e}")
        return None

def find_duplicate_files(base_dir):
    """Find duplicate files in a directory tree."""
    hashes = defaultdict(list)
    had_errors_local = False
    try:
        for dirpath, _, filenames in os.walk(base_dir):
            for filename in filenames:
                path = os.path.join(dirpath, filename)
                if os.path.isfile(path):
                    file_hash = hash_file(path)
                    if file_hash is not None:
                        hashes[file_hash].append(path)
                    else:
                        had_errors_local = True
    except PermissionError as e:
        print(f"Error accessing directory {base_dir}: {e}")
        had_errors_local = True
    return {hash_val: paths for hash_val, paths in hashes.items() if len(paths) > 1}, had_errors_local

def main():
    parser = argparse.ArgumentParser(description="Find duplicate files in a directory tree.")
    parser.add_argument('--base-dir', default='.', help='The base directory to scan.')
    args = parser.parse_args()

    had_errors = False
    duplicates, func_had_errors = find_duplicate_files(args.base_dir)
    if func_had_errors:
        had_errors = True

    if not duplicates:
        print("No duplicate files found.")
        return

    print("Duplicate files found:")
    for hash_val, paths in duplicates.items():
        print(f"\nHash: {hash_val}")
        for path in paths:
            print(f"  - {path}")

    if had_errors:
        raise SystemExit(1)

if __name__ == '__main__':
    main()
