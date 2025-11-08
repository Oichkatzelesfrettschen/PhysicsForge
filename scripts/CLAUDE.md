# scripts/ Directory Guide

**Location:** `/home/eirikr/Playground/PhysicsForge/scripts/`

## Purpose

Root-level Python utilities for equation extraction, catalog management, repository auditing, and validation. These scripts operate on the entire repository.

## WARNING: CRITICAL - Execution Context

**Always run from project root:**

```bash
# CORRECT
cd ~/Playground/PhysicsForge
python scripts/build_catalog_pipeline.py --base-dir .

# WRONG
cd ~/Playground/PhysicsForge/scripts
python build_catalog_pipeline.py --base-dir ..
```

## Script Inventory

### Equation Extraction
- **equation_extractor.py** - Extract equations from text/markdown sources
- **pdf_equation_extractor.py** - Extract equations from PDF files
- **merge_and_analyze_equations.py** - Build master catalog from extractions

### Catalog Management
- **build_catalog_pipeline.py** - Run full extraction pipeline (calls above scripts)
- **catalog_parity.py** - Check catalog vs modules coverage
- **validate_catalog.py** - Validate catalog integrity
- **link_modules.py** - Cross-link equations by ID
- **gap_todo.py** - Generate TODO list for missing content

### Repository Auditing
- **repo_audit.py** - Repository structure audit
- **tex_audit.py** - LaTeX package/label audit
- **benchmark_extraction.py** - Performance benchmarking

## Common Usage Patterns

### Full Catalog Pipeline
```bash
cd ~/Playground/PhysicsForge
python scripts/build_catalog_pipeline.py --base-dir . --scan-dir notes --scan-dir synthesis
```

**Outputs:**
- `equation_catalog.csv` - Master catalog
- `equation_summary.txt` - Statistics
- `notation_conflicts.txt` - Symbol conflicts
- `top_equations.txt` - Most referenced equations

### Check Coverage
```bash
cd ~/Playground/PhysicsForge
python scripts/catalog_parity.py --base-dir .
# Output: CATALOG_PARITY.md
```

### Validate Integrity
```bash
cd ~/Playground/PhysicsForge
python scripts/validate_catalog.py --base-dir .
# Output: VALIDATION_REPORT.md
# Exit code: 0 = valid, non-zero = errors
```

### Repository Audit
```bash
cd ~/Playground/PhysicsForge
python scripts/repo_audit.py --base-dir .
# Output: REPO_AUDIT.md
```

### LaTeX Audit
```bash
cd ~/Playground/PhysicsForge
python scripts/tex_audit.py --base-dir .
# Output: TEX_AUDIT.md
```

## Script Conventions

### Command-Line Arguments

All scripts accept:
- **--base-dir** - Repository root (default: `.` or `MATH_SCIENCE_BASE_DIR` env var)
- **--scan-dir** - Directories to scan (repeatable)

Example:
```bash
python scripts/equation_extractor.py --base-dir . --scan-dir notes --scan-dir synthesis
```

### Return Codes
- **0** = Success, no errors
- **Non-zero** = Errors found (check stderr)

### Output Files
- Written to repository root unless specified
- Markdown reports: `*.md`
- Data files: `*.csv`, `*.txt`

### Path Handling
- Use `pathlib.Path` for cross-platform compatibility
- Accept both absolute and relative paths
- Normalize paths internally

## Python Environment

### Requirements
- **Python:** 3.10+ required
- **Dependencies:** Standard library only (no pip install needed)
- **Type Hints:** Encouraged (Python 3.10+ syntax)

### Standard Imports
```python
from __future__ import annotations
import argparse
from pathlib import Path
import csv
import re
```

### Naming Conventions
- **Script names:** `snake_case.py`
- **Function names:** `snake_case()`
- **Class names:** `PascalCase`
- **Constants:** `UPPER_SNAKE_CASE`

## Makefile Integration

These scripts are integrated into the root Makefile:

```bash
make pipeline      # Run full catalog pipeline
make audit         # Repository audit
make parity        # Catalog coverage check
make gaps          # Generate gap TODO list
make validate      # Validate catalog
make bench         # Benchmark extraction
make smoke         # Quick smoke test
make test          # Run pytest
make ci            # Full CI suite
```

## Creating New Scripts

### Template
```python
#!/usr/bin/env python3
"""
Script: [name]
Purpose: [description]
Usage: python scripts/[name].py --base-dir . [options]
"""

from __future__ import annotations
import argparse
from pathlib import Path

def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(description="[description]")
    parser.add_argument("--base-dir", type=Path, default=Path("."),
                        help="Repository root (default: current directory)")
    args = parser.parse_args()

    base_dir = args.base_dir.resolve()

    # Script logic here

    return 0  # Success

if __name__ == "__main__":
    exit(main())
```

### Best Practices
1. **Accept --base-dir** for repository root
2. **Use pathlib.Path** for all file operations
3. **Return proper exit codes** (0 = success)
4. **Write outputs to repository root** unless specified
5. **Document in docstrings** (what, why, how)
6. **Add type hints** for function signatures
7. **Handle errors gracefully** with try/except
8. **Use argparse** for command-line parsing

## Integration with LaTeX Build

These scripts are **separate** from the LaTeX build process:
- LaTeX build: `make latex` (uses `synthesis/scripts/compile.sh`)
- Catalog build: `make pipeline` (uses Python scripts here)
- Full CI: `make ci` (runs both + tests + validation)

## Common Tasks

### Add New Script to Makefile
1. Create script in `scripts/[name].py`
2. Make executable: `chmod +x scripts/[name].py`
3. Add target to root `Makefile`:
```makefile
[name]:
	python scripts/[name].py --base-dir .
```
4. Document in Makefile comments
5. Test: `make [name]`

### Debug Script Errors
```bash
cd ~/Playground/PhysicsForge

# Run with verbose output
python -v scripts/[script].py --base-dir .

# Check exit code
echo $?

# Redirect stderr to file
python scripts/[script].py --base-dir . 2> error.log
```

### Benchmark Performance
```bash
cd ~/Playground/PhysicsForge
python scripts/benchmark_extraction.py --base-dir . --scan-dir notes
```

## Troubleshooting

### "Module not found"
- Verify Python 3.10+: `python --version`
- Scripts use only standard library
- Check for typos in imports

### "File not found"
- Verify --base-dir is correct
- Use absolute paths: `--base-dir /home/eirikr/Playground/PhysicsForge`
- Check working directory: `pwd`

### "Permission denied"
- Make script executable: `chmod +x scripts/[name].py`
- Check file ownership: `ls -la scripts/[name].py`

### Script runs but no output
- Check exit code: `echo $?`
- Non-zero = errors occurred
- Redirect stderr: `2> error.log`
- Verify write permissions in target directory

## See Also

- `/home/eirikr/Playground/PhysicsForge/CLAUDE.md` - Project root guidelines
- `/home/eirikr/Playground/PhysicsForge/synthesis/scripts/CLAUDE.md` - Build scripts (LaTeX-specific)
- `/home/eirikr/Playground/PhysicsForge/Makefile` - All available make targets
