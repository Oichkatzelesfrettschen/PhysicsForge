# synthesis/scripts/ Directory Guide

**Location:** `/home/eirikr/Playground/PhysicsForge/synthesis/scripts/`

## Purpose

LaTeX build automation scripts. These scripts handle document compilation, cleaning, and output management.

## ⚠️ CRITICAL: Never Call Directly

**DO NOT run these scripts manually. Always use root Makefile:**

```bash
# WRONG - Do NOT do this
cd ~/Playground/PhysicsForge/synthesis/scripts
bash compile.sh

# CORRECT - Always do this
cd ~/Playground/PhysicsForge
make latex
```

The Makefile handles:
- Setting correct working directories
- Managing build artifacts
- Log file placement
- Error handling

## Scripts

### compile.sh
**Purpose:** Main LaTeX compilation script

**What it does:**
1. Changes to synthesis/ directory
2. Runs latexmk with pdflatex
3. Processes bibliography with bibtex
4. Multiple passes for cross-references
5. Writes logs to `../logs/latexmk_compile.log`

**Called by:** `make latex` from project root

**Internal workflow:**
```bash
cd "$(dirname "$0")/.."  # Changes to synthesis/
latexmk -pdf main.tex
# On failure: clean aux files and retry
```

**Never call directly** - use `make latex` instead.

### Other Scripts (if present)
- **clean.sh** - Remove build artifacts (use `make clean`)
- **test_compile.sh** - Test individual chapters (use `pdflatex synthesis/test_chNN.tex`)

## Build Workflow (How It Actually Works)

### User Command
```bash
cd ~/Playground/PhysicsForge
make latex
```

### Makefile Target
```makefile
latex:
    bash synthesis/scripts/compile.sh
```

### compile.sh Execution
1. **cd to synthesis/** - Script changes directory internally
2. **Run latexmk** - Compiles main.tex with pdflatex
3. **Process bibtex** - Resolves bibliography references
4. **Multiple passes** - Resolves cross-references
5. **Write logs** - Outputs to `../logs/latexmk_compile.log`

### Outputs
- **PDF:** `synthesis/main.pdf`
- **Logs:** `logs/latexmk_compile.log` (project root)
- **Auxiliary:** `synthesis/main.aux`, `.toc`, `.lof`, `.lot`, etc.

## Why This Structure?

### Problem: Path Confusion
If you run `compile.sh` directly from synthesis/scripts/:
- Script expects to be in synthesis/
- Paths break (can't find main.tex)
- Log files go to wrong location

### Solution: Makefile Orchestration
Makefile ensures:
- **Consistent entry point** - Always project root
- **Correct paths** - Script handles directory changes
- **Proper logging** - Logs go to project root logs/
- **Error handling** - Makefile catches failures

## Modifying Build Scripts

### Adding New Build Step

1. **Edit compile.sh:**
```bash
# Add after latexmk call
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
# Your new step here
makeindex main.idx
```

2. **Test from root:**
```bash
cd ~/Playground/PhysicsForge
make latex
```

3. **Never test by calling compile.sh directly**

### Creating New Build Script

1. **Create in synthesis/scripts/**
```bash
#!/bin/bash
cd "$(dirname "$0")/.."  # Navigate to synthesis/
# Your build logic here
```

2. **Add to root Makefile:**
```makefile
my_target:
	bash synthesis/scripts/my_script.sh
```

3. **Test:**
```bash
cd ~/Playground/PhysicsForge
make my_target
```

## Build Targets Available

From project root:
```bash
make latex         # Full compilation (uses compile.sh)
make clean         # Clean build artifacts
make latex_strict  # Strict mode with error checking
```

## Troubleshooting

### "File not found" errors
**Cause:** Running script from wrong directory

**Fix:** Always use `make latex` from project root

### Compilation fails
**Check log:**
```bash
cat ~/Playground/PhysicsForge/logs/latexmk_compile.log
```

**Common issues:**
- Missing packages (check preamble.tex)
- Syntax errors in .tex files
- Undefined references (need multiple passes)
- Unicode characters (check for non-ASCII)

### Log file not created
**Cause:** Script not finding correct output directory

**Fix:** Verify you're using `make latex` from project root

### Script hangs
**Cause:** LaTeX waiting for input (error prompt)

**Fix:**
1. Kill process: `Ctrl+C`
2. Check log for error
3. Fix error in source
4. Run `make clean && make latex`

## Script Structure

### Standard Template
```bash
#!/bin/bash
set -e  # Exit on error

SCRIPT_DIR="$(dirname "$0")"
cd "$SCRIPT_DIR/.."  # Navigate to synthesis/

# Build logic here

# Always return explicit exit code
exit 0
```

### Best Practices
1. **Navigate to synthesis/** at script start
2. **Set -e** to exit on first error
3. **Use explicit paths** for log files
4. **Return proper exit codes**
5. **Add error messages** for debugging
6. **Never assume working directory**

## Integration with Makefile

The root Makefile is the **single source of truth** for all builds:

```makefile
latex:
	bash synthesis/scripts/compile.sh

clean:
	rm -f synthesis/*.aux synthesis/*.log synthesis/*.pdf
	rm -f synthesis/*.toc synthesis/*.lof synthesis/*.lot
	rm -f synthesis/*.out synthesis/*.bbl synthesis/*.blg
```

**Never modify synthesis/scripts/ without updating Makefile.**

## Common Modifications

### Add BibTeX Processing
Already included in compile.sh via latexmk.

### Add Index Generation
```bash
# In compile.sh
latexmk -pdf main.tex
makeindex main.idx
pdflatex main.tex
```

### Change Compilation Engine
```bash
# In compile.sh
# Replace latexmk -pdf with:
lualatex main.tex  # or xelatex main.tex
```

### Add Glossary Processing
```bash
# In compile.sh
makeglossaries main
pdflatex main.tex
```

## See Also

- `/home/eirikr/Playground/PhysicsForge/CLAUDE.md` - Project root guidelines
- `/home/eirikr/Playground/PhysicsForge/synthesis/CLAUDE.md` - LaTeX source guidelines
- `/home/eirikr/Playground/PhysicsForge/scripts/CLAUDE.md` - Python utilities (different directory!)
- `/home/eirikr/Playground/PhysicsForge/Makefile` - All available make targets
