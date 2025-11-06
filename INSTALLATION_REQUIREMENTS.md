# INSTALLATION REQUIREMENTS

**Math & Science Research Repository**
**Unified Field Theory - Aether, Genesis, Pais Frameworks**
**Last Updated:** 2025-10-22

---

## Table of Contents

1. [System Requirements](#system-requirements)
2. [Core Dependencies](#core-dependencies)
3. [LaTeX Package Requirements](#latex-package-requirements)
4. [Optional Dependencies](#optional-dependencies)
5. [Installation Steps](#installation-steps)
6. [Verification & Testing](#verification--testing)
7. [Post-Installation Configuration](#post-installation-configuration)
8. [Troubleshooting Guide](#troubleshooting-guide)

---

## 1. System Requirements

### Windows 11 Specifications

**Minimum Requirements:**
- **Operating System:** Windows 11 (64-bit)
- **RAM:** 8 GB minimum, 16 GB recommended
- **Disk Space:** 10 GB minimum (5 GB for chosen LaTeX distribution, 2 GB for Python, 3 GB for workspace)
- **CPU:** Dual-core processor, quad-core recommended
- **Display:** 1920x1080 or higher recommended for LaTeX editing

**PowerShell Requirements:**
- **Version:** PowerShell 5.1 or higher (comes with Windows 11)
- **Execution Policy:** RemoteSigned or Unrestricted (for script execution)

**Verify PowerShell Version:**
```powershell
$PSVersionTable.PSVersion
```

Expected output: Major version 5 or higher

---

## 2. Core Dependencies

### 2.0 LaTeX Distribution Options

This project supports both MiKTeX and TeX Live distributions for LaTeX compilation. Please choose one of the following options based on your preference and system setup. The instructions below will guide you through the installation and configuration for your chosen distribution.

---

### Option A: MiKTeX Complete Installation

**MiKTeX** is a comprehensive LaTeX distribution for Windows that provides all necessary tools for compiling LaTeX documents.

#### Download
- **URL:** https://miktex.org/download
- **Version:** Latest stable release (2.9.x or higher)
- **Installer:** Download the 64-bit Basic Installer or Complete Installer

#### Installation Options

**Option A: User Installation (Recommended for single user)**
1. Download MiKTeX installer
2. Run the installer executable
3. Choose "Install MiKTeX for: You only"
4. Select installation directory (default: `C:\Users\<username>\AppData\Local\Programs\MiKTeX`)
5. Preferred paper: Letter or A4
6. Install missing packages: **Yes (on-the-fly)** - CRITICAL SETTING
7. Complete installation (may take 10-30 minutes)

**Option B: Admin Installation (For multi-user systems)**
1. Run installer as Administrator
2. Choose "Install MiKTeX for: All Users"
3. Select installation directory (default: `C:\Program Files\MiKTeX`)
4. Configure on-the-fly package installation: **Yes**
5. Complete installation

#### Required MiKTeX Configuration

After installation, configure MiKTeX Console:

```powershell
# Open MiKTeX Console
Start-Process "miktex-console"
```

In MiKTeX Console:
1. **Updates Tab:** Check for updates and install all available updates
2. **Settings Tab:**
   - Package installation: **Install missing packages on-the-fly: Yes**
   - Package repository: Select nearest CTAN mirror
   - Automatic update check: **Daily**
3. **Packages Tab:** Verify installation of critical packages (see Section 3)

#### Package Repository Configuration

```powershell
# Set default package repository (use nearest mirror)
mpm --set-repository="https://ctan.org/tex-archive/systems/win32/miktex"

# Update package database
mpm --update-db

# Verify repository connection
mpm --list-repositories
```

#### Format File Generation

MiKTeX automatically generates format files (.fmt) on first use. To pre-generate:

```powershell
# Generate LaTeX format files
initexmf --dump=latex

# Generate pdfLaTeX format files
initexmf --dump=pdflatex

# Refresh filename database
initexmf --update-fndb
```

### Option B: TeX Live Complete Installation

**TeX Live** is a comprehensive, cross-platform LaTeX distribution that provides all necessary tools for compiling LaTeX documents.

#### Download
- **URL:** https://www.tug.org/texlive/acquire-netinstall.html
- **Version:** Latest stable release (e.g., TeX Live 2025)
- **Installer:** Download `install-tl-windows.exe` (network installer)

#### Installation Steps

1. Download the `install-tl-windows.exe` installer.
2. **Run the installer as Administrator** (right-click -> Run as administrator). This is crucial for proper system-wide installation and PATH configuration.
3. In the TeX Live installer GUI:
   - Click "Advanced" to customize.
   - **Installation scheme:** Select "full" (recommended for comprehensive package set).
   - **Installation directory:** Default `C:\texlive\<YEAR>` (e.g., `C:\texlive\2025`) is recommended.
   - **Options:**
     - Ensure "Add TeX Live to system PATH" is checked (CRITICAL).
     - Check "Install font maps"
     - Check "Create desktop icons" (optional)
   - Click "Install TeX Live".
4. Installation may take a significant amount of time (30-90 minutes or more) due to downloading all packages. Ensure a stable internet connection.
5. Complete installation.

#### Required TeX Live Configuration

After installation, ensure TeX Live is in your system PATH. You can verify this by opening a new PowerShell window and typing `tex --version`.

To update TeX Live packages:

```powershell
# Open TeX Live Manager GUI
tlmgr gui

# In the GUI:
# 1. Click "Load default repositories"
# 2. Click "Update all installed packages"
# 3. Click "Install missing packages" (if any are reported)
```

Alternatively, from the command line:

```powershell
# Update package database
tlmgr update --self --all

# Verify repository connection
tlmgr repository list
```

#### Format File Generation

TeX Live automatically generates format files during installation and updates. To manually regenerate (rarely needed):

```powershell
# Regenerate all format files
fmtutil-sys --all

# Refresh filename database
mktexlsr
```

---

### 2.2 Python 3.10+ Installation

**Python** is required for the equation extraction and catalog pipeline scripts.

#### Download
- **URL:** https://www.python.org/downloads/
- **Version:** Python 3.10 or higher (currently tested with 3.13.9)
- **Installer:** Download Windows installer (64-bit)

#### Installation Steps

1. Run the Python installer
2. **CRITICAL:** Check "Add Python to PATH" checkbox at bottom
3. Click "Install Now" (installs to `C:\Users\<username>\AppData\Local\Programs\Python\Python3XX`)
4. Wait for installation to complete
5. Click "Disable path length limit" if prompted (recommended)

#### PATH Configuration

If you forgot to check "Add to PATH" during installation:

```powershell
# Manual PATH configuration
# 1. Open System Properties > Environment Variables
# 2. Edit PATH variable, add:
#    C:\Users\<username>\AppData\Local\Programs\Python\Python3XX
#    C:\Users\<username>\AppData\Local\Programs\Python\Python3XX\Scripts

# OR use PowerShell to modify PATH (run as Administrator)
$pythonPath = "C:\Users\$env:USERNAME\AppData\Local\Programs\Python\Python313"
[Environment]::SetEnvironmentVariable("PATH", "$env:PATH;$pythonPath;$pythonPath\Scripts", "User")
```

#### Verification Commands

```powershell
# Verify Python installation
python --version
# Expected: Python 3.10.x or higher

# Verify pip installation
pip --version
# Expected: pip 24.x or higher

# Verify Python can import stdlib modules
python -c "import re, os, csv, argparse, pathlib, collections, subprocess, sys; print('Python stdlib modules: OK')"
```

Important: Core smoke tests run on the Python standard library only; however, several advanced extraction pipelines are optional and require additional packages. See the next section for details.

### 2.3 Python Optional Packages (for PDF/OCR pipelines)

These are only needed if you plan to run PDF text or image OCR extraction and related workflows.

- PyMuPDF for text extraction from PDFs
  - Install: `pip install pymupdf`
- Pillow (PIL) for basic image pre/post-processing
  - Install: `pip install Pillow`
- pix2tex (LaTeX OCR) for equation OCR from images
  - Install: `pip install pix2tex`
  - Note: pix2tex depends on machine-learning frameworks (PyTorch et al.). For CPU-only installs of PyTorch:
    - Windows (CPU): `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu`
    - Verify: `python -c "import torch; print(torch.__version__)"`

Recommended optional constraints file: `requirements-optional.txt` at the repository root captures these extras.

---

## 3. LaTeX Package Requirements

The following LaTeX packages are required by `synthesis/preamble.tex`. MiKTeX should install these automatically on first compilation if "on-the-fly installation" is enabled.

### 3.1 Encoding and Fonts

| Package | Purpose | MiKTeX Installation | TeX Live Installation |
|---------|---------|---------------------|-----------------------|
| `inputenc` | UTF-8 input encoding support | Auto-installed with MiKTeX | `tlmgr install inputenc` |
| `fontenc` | Font encoding (T1) | Auto-installed with MiKTeX | `tlmgr install fontenc` |
| `lmodern` | Latin Modern fonts | `mpm --install=lm` | `tlmgr install lmodern` |

### 3.2 Mathematics

| Package | Purpose | MiKTeX Installation | TeX Live Installation |
|---------|---------|---------------------|-----------------------|
| `amsmath` | AMS mathematical facilities | `mpm --install=amsmath` | `tlmgr install amsmath` |
| `amssymb` | AMS mathematical symbols | `mpm --install=amsfonts` | `tlmgr install amssymb` |
| `amsthm` | AMS theorem environments | `mpm --install=amscls` | `tlmgr install amsthm` |
| `mathtools` | Enhanced math typesetting | `mpm --install=mathtools` | `tlmgr install mathtools` |
| `physics` | Dirac notation, derivatives, physics notation | `mpm --install=physics` | `tlmgr install physics` |

### 3.3 Graphics and Figures

| Package | Purpose | MiKTeX Installation | TeX Live Installation |
|---------|---------|---------------------|-----------------------|
| `graphicx` | Include graphics (PNG, JPG, PDF) | `mpm --install=graphics` | `tlmgr install graphics` |
| `tikz` | Programmatic graphics and diagrams | `mpm --install=pgf` | `tlmgr install pgf` |
| `pgfplots` | Plot mathematical functions | `mpm --install=pgfplots` | `tlmgr install pgfplots` |

**TikZ Libraries Used:**
- `arrows.meta` - Advanced arrow styles
- `positioning` - Relative positioning
- `calc` - Coordinate calculations
- `decorations.pathmorphing` - Decorative path effects
- `shapes.geometric` - Geometric shapes

### 3.4 Tables

| Package | Purpose | MiKTeX Installation | TeX Live Installation |
|---------|---------|---------------------|-----------------------|
| `booktabs` | Professional quality tables | `mpm --install=booktabs` | `tlmgr install booktabs` |
| `longtable` | Multi-page tables | `mpm --install=tools` | `tlmgr install longtable` |
| `multirow` | Multi-row table cells | `mpm --install=multirow` | `tlmgr install multirow` |
| `array` | Enhanced array/tabular environments | `mpm --install=tools` | `tlmgr install array` |

### 3.5 Colors

| Package | Purpose | MiKTeX Installation | TeX Live Installation |
|---------|---------|---------------------|-----------------------|
| `xcolor` | Color support with RGB definitions | `mpm --install=xcolor` | `tlmgr install xcolor` |

**Custom Colors Defined:**
- `aetherblue` - RGB(0,102,204) - Aether framework
- `genesisgreen` - RGB(34,139,34) - Genesis framework
- `paisred` - RGB(204,0,0) - Pais framework
- `unifiedpurple` - RGB(128,0,128) - Unified framework

### 3.6 Units and Formatting

| Package | Purpose | MiKTeX Installation | TeX Live Installation |
|---------|---------|---------------------|-----------------------|
| `siunitx` | SI units typesetting and number formatting | `mpm --install=siunitx` | `tlmgr install siunitx` |

### 3.7 Cross-Referencing and Hyperlinks

| Package | Purpose | MiKTeX Installation | TeX Live Installation |
|---------|---------|---------------------|-----------------------|
| `hyperref` | Hyperlinks and PDF metadata | `mpm --install=hyperref` | `tlmgr install hyperref` |
| `cleveref` | Intelligent cross-referencing | `mpm --install=cleveref` | `tlmgr install cleveref` |

### 3.8 Bibliography

| Package | Purpose | MiKTeX Installation | TeX Live Installation |
|---------|---------|---------------------|-----------------------|
| `natbib` | Natural sciences bibliography | `mpm --install=natbib` | `tlmgr install natbib` |

### 3.9 Code Listings

| Package | Purpose | MiKTeX Installation | TeX Live Installation |
|---------|---------|---------------------|-----------------------|
| `listings` | Source code syntax highlighting | `mpm --install=listings` | `tlmgr install listings` |

### 3.10 Page Layout

| Package | Purpose | MiKTeX Installation | TeX Live Installation |
|---------|---------|---------------------|-----------------------|
| `geometry` | Page dimensions and margins | `mpm --install=geometry` | `tlmgr install geometry` |
| `fancyhdr` | Custom headers and footers | `mpm --install=fancyhdr` | `tlmgr install fancyhdr` |
| `titlesec` | Custom section/chapter formatting | `mpm --install=titlesec` | `tlmgr install titlesec` |

### 3.11 Miscellaneous

| Package | Purpose | MiKTeX Installation | TeX Live Installation |
|---------|---------|---------------------|-----------------------|
| `tcolorbox` | Colored boxes for examples/highlights | `mpm --install=tcolorbox` | `tlmgr install tcolorbox` |
| `lipsum` | Placeholder text generation | `mpm --install=lipsum` | `tlmgr install lipsum` |
| `enumitem` | Enhanced list control | `mpm --install=enumitem` | `tlmgr install enumitem` |
| `caption` | Caption formatting | `mpm --install=caption` | `tlmgr install caption` |
| `subcaption` | Subfigure support | `mpm --install=caption` | `tlmgr install subcaption` |

### 3.12 Batch Installation

Install all required packages at once:

```powershell
# MiKTeX Core packages batch install
Write-Host "Installing MiKTeX packages..."
$miktex_packages = @(
    "lm",
    "amsmath",
    "amsfonts",
    "amscls",
    "mathtools",
    "physics",
    "graphics",
    "pgf",
    "pgfplots",
    "booktabs",
    "tools",
    "multirow",
    "xcolor",
    "siunitx",
    "hyperref",
    "cleveref",
    "natbib",
    "listings",
    "geometry",
    "fancyhdr",
    "titlesec",
    "tcolorbox",
    "lipsum",
    "enumitem",
    "caption"
)

foreach ($pkg in $miktex_packages) {
    Write-Host "Installing $pkg for MiKTeX..."
    mpm --install=$pkg
}
Write-Host "MiKTeX package installation complete!"

# TeX Live Core packages batch install
Write-Host "Installing TeX Live packages..."
$texlive_packages = @(
    "lmodern",
    "amsmath",
    "amsfonts",
    "amsthm",
    "mathtools",
    "physics",
    "graphics",
    "pgf",
    "pgfplots",
    "booktabs",
    "longtable",
    "multirow",
    "array",
    "xcolor",
    "siunitx",
    "hyperref",
    "cleveref",
    "natbib",
    "listings",
    "geometry",
    "fancyhdr",
    "titlesec",
    "tcolorbox",
    "lipsum",
    "enumitem",
    "caption",
    "subcaption",
    "inputenc",
    "fontenc"
)

foreach ($pkg in $texlive_packages) {
    Write-Host "Installing $pkg for TeX Live..."
    tlmgr install $pkg
}
Write-Host "TeX Live package installation complete!"
```

---

## 4. Optional Dependencies

### 4.1 Chocolatey Package Manager

**Chocolatey** simplifies Windows package management for development tools.

#### Installation

```powershell
# Run PowerShell as Administrator
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

#### Usage Examples

```powershell
# Install Python via Chocolatey (alternative method)
choco install python --version=3.13.9 -y

# Install MiKTeX via Chocolatey (alternative method)
choco install miktex -y

# Install TeX Live via Chocolatey (alternative method)
choco install texlive -y

# Install Git
choco install git -y
```

### 4.2 Git for Version Control

**Git** is essential for repository management and collaboration.

#### Installation Options

**Option A: Via Chocolatey**
```powershell
choco install git -y
```

**Option B: Manual Install**
1. Download from https://git-scm.com/download/win
2. Run installer with default settings
3. Select "Use Git from Windows Command Prompt"
4. Configure line endings: "Checkout Windows-style, commit Unix-style"

#### Configuration

```powershell
# Configure Git user identity
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Configure line endings for Windows
git config --global core.autocrlf true

# Verify configuration
git config --list
```

#### Initialize Repository

```powershell
# Navigate to repository root
cd C:\Users\ericj\Git-Projects\Math_Science

# Initialize Git repository
git init

# Create .gitignore
@"
# LaTeX build artifacts
*.aux
*.log
*.out
*.toc
*.synctex.gz
*.fdb_latexmk
*.fls
*.pdf

# Python artifacts
__pycache__/
*.pyc
*.pyo
.pytest_cache/

# OS files
.DS_Store
Thumbs.db

# Editor files
.vscode/
.idea/
*.swp
*~
"@ | Out-File -FilePath .gitignore -Encoding utf8

# Initial commit
git add .
git commit -m "Initial commit: Math & Science research repository"
```

### 4.3 Visual Studio Code with LaTeX Workshop

**VS Code** provides excellent LaTeX editing and compilation support.

#### Installation

```powershell
# Via Chocolatey
choco install vscode -y

# Manual: Download from https://code.visualstudio.com/
```

#### LaTeX Workshop Extension

1. Open VS Code
2. Press `Ctrl+Shift+X` (Extensions)
3. Search "LaTeX Workshop"
4. Install "LaTeX Workshop" by James Yu
5. Reload VS Code

#### VS Code Configuration

Create `.vscode/settings.json`:

```json
{
  "latex-workshop.latex.tools": [
    {
      "name": "pdflatex",
      "command": "pdflatex",
      "args": [
        "-synctex=1",
        "-interaction=nonstopmode",
        "-file-line-error",
        "%DOC%"
      ]
    }
  ],
  "latex-workshop.latex.recipes": [
    {
      "name": "pdflatex",
      "tools": ["pdflatex"]
    }
  ],
  "latex-workshop.view.pdf.viewer": "tab",
  "files.encoding": "utf8"
}
```

### 4.4 Python Virtual Environment (Optional)

Although this repository uses Python stdlib only, virtual environments are best practice.

```powershell
# Navigate to repository root
cd C:\Users\ericj\Git-Projects\Math_Science

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Deactivate when done
deactivate
```

**Note:** If you encounter execution policy errors:

```powershell
# Allow script execution (run as Administrator)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 5. Installation Steps

Follow these steps for a complete installation from scratch.

### Step 1: Install MiKTeX

**Description:** Install the complete LaTeX distribution for Windows.

1. **Download MiKTeX installer:**
   - Navigate to https://miktex.org/download
   - Download "Basic MiKTeX 64-bit Installer" (miktex-setup-x64.exe)
   - File size: ~300 MB

2. **Run installer:**
   ```powershell
   # Navigate to Downloads folder
   cd $env:USERPROFILE\Downloads

   # Run installer (may prompt for elevation)
   .\miktex-setup-x64.exe
   ```

3. **Installer wizard steps:**
   - **Welcome Screen:** Click "Next"
   - **License Agreement:** Accept terms, click "Next"
   - **Installation Scope:** Select "Install MiKTeX for: You only", click "Next"
   - **Installation Directory:** Use default or choose custom path, click "Next"
   - **Settings:**
     - Preferred paper size: Letter (US) or A4 (International)
     - **Install missing packages on-the-fly: Yes** (CRITICAL!)
     - Click "Next"
   - **Review:** Verify settings, click "Start"
   - **Installation:** Wait 10-30 minutes
   - **Completion:** Click "Close"

4. **Verify installation:**
   ```powershell
   # Check pdflatex version
   pdflatex --version
   # Expected: pdfTeX 3.141592653-2.6-1.40.x (MiKTeX)

   # Check MiKTeX package manager
   mpm --version
   # Expected: MiKTeX Package Manager x.x.x
   ```

### Step 2: Configure MiKTeX Console

**Description:** Configure package management and update settings.

1. **Open MiKTeX Console:**
   ```powershell
   Start-Process "miktex-console"
   ```

2. **Update package database:**
   - Navigate to **Updates** tab
   - Click "Check for updates"
   - If updates available, click "Update now"
   - Wait for updates to complete

3. **Configure settings:**
   - Navigate to **Settings** tab
   - Under "Package installation":
     - Set to: **Always install missing packages on-the-fly**
   - Under "Package repository":
     - Click "Change..."
     - Select nearest CTAN mirror or use "Random package repository on the Internet"
     - Click "OK"

4. **Verify critical packages (optional):**
   - Navigate to **Packages** tab
   - Search for: `amsmath`, `pgf`, `hyperref`, `physics`
   - Verify installation status (green checkmark = installed)

### Step 3: Install Python

**Description:** Install Python 3.10 or higher with pip.

1. **Download Python installer:**
   - Navigate to https://www.python.org/downloads/
   - Click "Download Python 3.13.9" (or latest 3.10+)
   - File size: ~25 MB

2. **Run installer:**
   ```powershell
   # Navigate to Downloads folder
   cd $env:USERPROFILE\Downloads

   # Run installer
   .\python-3.13.9-amd64.exe
   ```

3. **Installer wizard steps:**
   - **CRITICAL:** Check "Add Python to PATH" (bottom checkbox)
   - Click "Install Now"
   - Wait for installation (3-5 minutes)
   - If prompted, click "Disable path length limit" (recommended)
   - Click "Close"

4. **Verify installation:**
   ```powershell
   # Restart PowerShell to refresh PATH

   # Check Python version
   python --version
   # Expected: Python 3.13.9

   # Check pip version
   pip --version
   # Expected: pip 24.x from C:\Users\...\Python313\lib\site-packages\pip

   # Test Python stdlib imports
   python -c "import re, os, csv, argparse, pathlib, collections, subprocess, sys; print('All stdlib modules loaded successfully')"
   ```

### Step 4: Clone/Download Repository

**Description:** Obtain the Math & Science research repository.

**Option A: If Git is installed:**
```powershell
# Navigate to desired parent directory
cd C:\Users\ericj\Git-Projects

# Clone repository (if remote exists)
git clone https://github.com/username/Math_Science.git
cd Math_Science
```

**Option B: If working with existing local directory:**
```powershell
# Verify repository structure
cd C:\Users\ericj\Git-Projects\Math_Science
ls
# Should see: synthesis/, scripts/, tests/, notes/, etc.
```

**Option C: Initialize new Git repository:**
```powershell
cd C:\Users\ericj\Git-Projects\Math_Science

# Initialize Git
git init

# Create .gitignore (see Section 4.2)
```

### Step 5: Verify Installation

**Description:** Comprehensive verification of all components.

```powershell
# Navigate to repository root
cd C:\Users\ericj\Git-Projects\Math_Science

# Create verification script
@"
Write-Host "=== Math & Science Installation Verification ===" -ForegroundColor Cyan

# Check PowerShell version
Write-Host "`n[1/7] PowerShell Version:" -ForegroundColor Yellow
`$PSVersionTable.PSVersion

# Check MiKTeX
Write-Host "`n[2/7] MiKTeX Installation:" -ForegroundColor Yellow
pdflatex --version | Select-String "pdfTeX"
mpm --version

# Check Python
Write-Host "`n[3/7] Python Installation:" -ForegroundColor Yellow
python --version
pip --version

# Check repository structure
Write-Host "`n[4/7] Repository Structure:" -ForegroundColor Yellow
if (Test-Path ".\synthesis") { Write-Host "  synthesis/ - OK" -ForegroundColor Green } else { Write-Host "  synthesis/ - MISSING" -ForegroundColor Red }
if (Test-Path ".\scripts") { Write-Host "  scripts/ - OK" -ForegroundColor Green } else { Write-Host "  scripts/ - MISSING" -ForegroundColor Red }
if (Test-Path ".\tests") { Write-Host "  tests/ - OK" -ForegroundColor Green } else { Write-Host "  tests/ - MISSING" -ForegroundColor Red }
if (Test-Path ".\notes") { Write-Host "  notes/ - OK" -ForegroundColor Green } else { Write-Host "  notes/ - MISSING" -ForegroundColor Red }

# Check critical LaTeX files
Write-Host "`n[5/7] LaTeX Project Files:" -ForegroundColor Yellow
if (Test-Path ".\synthesis\preamble.tex") { Write-Host "  preamble.tex - OK" -ForegroundColor Green } else { Write-Host "  preamble.tex - MISSING" -ForegroundColor Red }
if (Test-Path ".\synthesis\main.tex") { Write-Host "  main.tex - OK" -ForegroundColor Green } else { Write-Host "  main.tex - MISSING" -ForegroundColor Red }

# Check Python scripts
Write-Host "`n[6/7] Python Scripts:" -ForegroundColor Yellow
`$scripts = @("equation_extractor.py", "build_catalog_pipeline.py", "merge_and_analyze_equations.py")
foreach (`$script in `$scripts) {
    if (Test-Path ".\scripts\`$script") {
        Write-Host "  `$script - OK" -ForegroundColor Green
    } else {
        Write-Host "  `$script - MISSING" -ForegroundColor Red
    }
}

# Test Python stdlib imports
Write-Host "`n[7/7] Python Standard Library:" -ForegroundColor Yellow
python -c "import re, os, csv, argparse, pathlib, collections, subprocess, sys; print('  All stdlib modules - OK')"

Write-Host "`n=== Verification Complete ===" -ForegroundColor Cyan
"@ | Out-File -FilePath verify_install.ps1 -Encoding utf8

# Run verification script
.\verify_install.ps1
```

### Step 6: Test LaTeX Compilation

**Description:** Verify LaTeX compilation pipeline works correctly.

```powershell
# Navigate to synthesis directory
cd C:\Users\ericj\Git-Projects\Math_Science\synthesis

# Test preamble syntax (compile minimal document)
@"
\documentclass{book}
\input{preamble}
\begin{document}
\chapter{Test Chapter}
This is a test document to verify preamble compilation.

Test equation with framework attribution:
\begin{equation}
E = mc^2 \aetherattr
\end{equation}

Test custom macros:
\begin{equation}
\nabla^2 \phiscalar = \rho \eqtag{A}{EM}{T}
\end{equation}

\end{document}
"@ | Out-File -FilePath test_compilation.tex -Encoding utf8

# Compile test document
pdflatex -interaction=nonstopmode test_compilation.tex

# Check for successful compilation
if (Test-Path "test_compilation.pdf") {
    Write-Host "LaTeX compilation: SUCCESS" -ForegroundColor Green
    Write-Host "PDF generated: test_compilation.pdf" -ForegroundColor Cyan

    # Open PDF
    Start-Process test_compilation.pdf
} else {
    Write-Host "LaTeX compilation: FAILED" -ForegroundColor Red
    Write-Host "Check test_compilation.log for errors" -ForegroundColor Yellow
}

# Cleanup auxiliary files
Remove-Item test_compilation.aux, test_compilation.log, test_compilation.out -ErrorAction SilentlyContinue
```

### Step 7: Test Python Scripts

**Description:** Verify Python equation extraction pipeline.

```powershell
# Navigate to repository root
cd C:\Users\ericj\Git-Projects\Math_Science

# Test equation extractor
Write-Host "Testing equation_extractor.py..." -ForegroundColor Cyan
python scripts\equation_extractor.py --base-dir . --scan-dir notes

# Verify output catalog
if (Test-Path "output\equations_catalog.csv") {
    Write-Host "Equation extraction: SUCCESS" -ForegroundColor Green
    Write-Host "Catalog generated: output\equations_catalog.csv" -ForegroundColor Cyan

    # Display first 10 lines
    Get-Content output\equations_catalog.csv | Select-Object -First 10
} else {
    Write-Host "Equation extraction: FAILED" -ForegroundColor Red
}

# Test full pipeline (if time permits)
Write-Host "`nTesting full catalog pipeline..." -ForegroundColor Cyan
python scripts\build_catalog_pipeline.py --base-dir . --scan-dir notes

# Verify pipeline outputs
$outputs = @(
    "output\equations_catalog.csv",
    "output\pdf_equations_catalog.csv",
    "output\merged_equations_catalog.csv"
)

foreach ($output in $outputs) {
    if (Test-Path $output) {
        Write-Host "  $output - OK" -ForegroundColor Green
    } else {
        Write-Host "  $output - MISSING" -ForegroundColor Red
    }
}
```

---

## 6. Verification & Testing

### 6.1 Component Verification

#### LaTeX Distribution Verification

**For MiKTeX:**
```powershell
# Check pdflatex executable
pdflatex --version
# Expected output:
# pdfTeX 3.141592653-2.6-1.40.25 (MiKTeX 24.1)
# kpathsea version 6.4.0

# Check package manager
mpm --version
# Expected: MiKTeX Package Manager x.x.x

# List installed packages (sample)
mpm --list | Select-String "amsmath|hyperref|pgf"
# Should show installed versions

# Check format files
initexmf --report
# Should show format files in: C:\Users\...\MiKTeX\miktex\data\le
```

**For TeX Live:**
```powershell
# Check pdflatex executable
pdflatex --version
# Expected output:
# pdfTeX 3.141592653-2.6-1.40.x (TeX Live)

# Check package manager
tlmgr --version
# Expected: TeX Live Manager x.x.x

# List installed packages (sample)
tlmgr list --only-installed | Select-String "amsmath|hyperref|pgf"
# Should show installed versions

# Check format files (TeX Live handles this automatically)
# No direct equivalent to initexmf --report for TeX Live format files
```

#### Python Verification

```powershell
# Verify Python installation
python --version
# Expected: Python 3.10.x or higher

# Verify pip
pip --version
# Expected: pip 24.x from ...

# Test Python stdlib modules used in scripts
python -c @"
import re
import os
import csv
import argparse
from pathlib import Path
from collections import defaultdict
import subprocess
import sys

print('Module tests:')
print(f'  re version: {re.__version__}')
print(f'  pathlib: {Path.cwd()}')
print(f'  collections.defaultdict: {defaultdict}')
print(f'  sys.version: {sys.version}')
print('All required stdlib modules loaded successfully!')
"@
```

#### Repository Structure Verification

```powershell
# Verify directory structure
$requiredDirs = @(
    "synthesis",
    "synthesis\chapters",
    "synthesis\equations",
    "scripts",
    "tests",
    "notes",
    "output"
)

Write-Host "Directory Structure Verification:" -ForegroundColor Cyan
foreach ($dir in $requiredDirs) {
    if (Test-Path $dir) {
        $count = (Get-ChildItem $dir -File).Count
        Write-Host "  $dir - OK ($count files)" -ForegroundColor Green
    } else {
        Write-Host "  $dir - MISSING" -ForegroundColor Red
    }
}
```

### 6.2 Expected Output Examples

#### Successful pdflatex Compilation

**For MiKTeX:**
```
This is pdfTeX, Version 3.141592653-2.6-1.40.25 (MiKTeX 24.1)
entering extended mode
(./test_compilation.tex
LaTeX2e <2023-11-01> patch level 1
...
[1] (./test_compilation.aux) )
Output written on test_compilation.pdf (1 page, 25678 bytes).
Transcript written on test_compilation.log.
```

**For TeX Live:**
```
This is pdfTeX, Version 3.141592653-2.6-1.40.25 (TeX Live 2025/W32TeX)
entering extended mode
(./test_compilation.tex
LaTeX2e <2023-11-01> patch level 1
...
[1] (./test_compilation.aux) )
Output written on test_compilation.pdf (1 page, 25678 bytes).
Transcript written on test_compilation.log.
```

#### Successful Python Script Execution

```
> python scripts\equation_extractor.py --base-dir . --scan-dir notes
Extracting equations from text files...
Found 237 equations in notes/
Writing catalog to output\equations_catalog.csv...
Extraction complete: 237 equations extracted
```

#### Successful Package Installation

```
> mpm --install=physics
installing physics 1.3...
extracting files from physics.tar.xz...
physics: 1.3 installed
```

### 6.3 Troubleshooting Common Installation Issues

#### Issue 1: pdflatex not found

**Symptoms:**
```
pdflatex : The term 'pdflatex' is not recognized...
```

**Solutions:**
```powershell
# Solution A: Refresh PATH (close and reopen PowerShell)

# Solution B: Add TeX Live to PATH manually (replace <YEAR> with your TeX Live version, e.g., 2025)
$texlivePath = "C:\texlive\<YEAR>\bin\windows"
[Environment]::SetEnvironmentVariable("PATH", "$env:PATH;$texlivePath", "User")

# Solution C: Verify TeX Live installation directory
Get-ChildItem "C:\texlive" -Recurse -Filter "pdflatex.exe"
```

#### Issue 2: Python not found

**Symptoms:**
```
python : The term 'python' is not recognized...
```

**Solutions:**
```powershell
# Solution A: Reinstall Python with "Add to PATH" checked

# Solution B: Add Python to PATH manually
$pythonPath = "C:\Users\$env:USERNAME\AppData\Local\Programs\Python\Python313"
[Environment]::SetEnvironmentVariable("PATH", "$env:PATH;$pythonPath;$pythonPath\Scripts", "User")

# Solution C: Use py launcher instead
py --version
py -m pip --version
```

#### Issue 3: Missing LaTeX packages during compilation

**Symptoms:**
```
! LaTeX Error: File 'physics.sty' not found.
```

**Solutions:**
```powershell
# Solution A: Manually install missing package
tlmgr install physics

# Solution B: Update TeX Live (ensures all packages are up-to-date)
tlmgr update --self --all

# Solution C: Verify package repository connection
tlmgr repository list
```

---

## 7. Post-Installation Configuration

### 7.1 LaTeX Package Repository Configuration

**For MiKTeX:**
```powershell
# Set default package repository to random CTAN mirror
mpm --set-repository="https://ctan.org/tex-archive/systems/win32/miktex"

# Update package database
mpm --update-db

# Refresh filename database
initexmf --update-fndb

# Verify repository connection
mpm --list-repositories
# Should show active repository
```
**For TeX Live:**
```powershell
# Update package database and all installed packages
tlmgr update --self --all

# Verify repository connection
tlmgr repository list
# Should show active repository
```

### 7.2 Python PATH Setup

Verify Python is in PATH:

```powershell
# Check Python executable location
Get-Command python | Select-Object Source
# Should show: C:\Users\...\Python313\python.exe

# Check Scripts directory (for pip-installed tools)
Get-Command pip | Select-Object Source
# Should show: C:\Users\...\Python313\Scripts\pip.exe

# If missing, add to PATH
$pythonRoot = "C:\Users\$env:USERNAME\AppData\Local\Programs\Python\Python313"
$currentPath = [Environment]::GetEnvironmentVariable("PATH", "User")
if ($currentPath -notlike "*$pythonRoot*") {
    [Environment]::SetEnvironmentVariable("PATH", "$currentPath;$pythonRoot;$pythonRoot\Scripts", "User")
    Write-Host "Python added to PATH. Restart PowerShell." -ForegroundColor Green
}
```

### 7.3 PowerShell Execution Policy

Allow local script execution:

```powershell
# Check current execution policy
Get-ExecutionPolicy -Scope CurrentUser

# If Restricted, change to RemoteSigned
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Verify change
Get-ExecutionPolicy -Scope CurrentUser
# Should show: RemoteSigned
```

**Execution Policy Levels:**
- **Restricted:** No scripts allowed (default on some systems)
- **RemoteSigned:** Local scripts allowed, remote scripts require signature (recommended)
- **Unrestricted:** All scripts allowed (not recommended for security)

### 7.4 Directory Structure Validation

Create output directory if missing:

```powershell
# Navigate to repository root
cd C:\Users\ericj\Git-Projects\Math_Science

# Create required directories
$requiredDirs = @(
    "output",
    "output\logs",
    "synthesis\build",
    "docs"
)

foreach ($dir in $requiredDirs) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir
        Write-Host "Created directory: $dir" -ForegroundColor Green
    }
}
```

### 7.5 Environment Variables (Optional)

Set project-specific environment variables:

```powershell
# Set base directory environment variable
[Environment]::SetEnvironmentVariable("MATH_SCIENCE_BASE_DIR", "C:\Users\ericj\Git-Projects\Math_Science", "User")

# Set LaTeX output directory
[Environment]::SetEnvironmentVariable("MATH_SCIENCE_OUTPUT", "C:\Users\ericj\Git-Projects\Math_Science\output", "User")

# Verify
$env:MATH_SCIENCE_BASE_DIR
$env:MATH_SCIENCE_OUTPUT

# Note: Restart PowerShell to apply changes
```

---

## 8. Troubleshooting Guide



### 8.1 LaTeX Format File Issues

**Problem:** Format file errors or "I can't find the format file `pdflatex.fmt`!"

**Diagnosis:**
**For MiKTeX:**
```powershell
# Check format file location
initexmf --report | Select-String "format"

# List existing format files
Get-ChildItem -Path "C:\Users\$env:USERNAME\AppData\Local\MiKTeX" -Recurse -Filter "*.fmt"
```
**For TeX Live:**
```powershell
# TeX Live handles format files automatically during installation and updates.
# If issues persist, try updating TeX Live:
tlmgr update --self --all
# Or manually regenerate:
fmtutil-sys --all
```

**Solutions:**
**For MiKTeX:**
```powershell
# Solution 1: Regenerate format files
initexmf --dump=pdflatex
initexmf --dump=latex

# Solution 2: Update filename database
initexmf --update-fndb

# Solution 3: Rebuild format database
initexmf --force --mkfmt=pdflatex

# Solution 4: Refresh MiKTeX (run as Administrator if needed)
initexmf --admin --update-fndb
initexmf --admin --mkfmt
```
**For TeX Live:**
```powershell
# Solution 1: Update TeX Live
tlmgr update --self --all

# Solution 2: Manually regenerate format files
fmtutil-sys --all

# Solution 3: Refresh filename database
mktexlsr
```

### 8.2 LaTeX Package Installation Failures

**Problem:** Packages fail to install or "Unknown archive file size"

**Diagnosis:**
**For MiKTeX:**
```powershell
# Check repository connection
mpm --list-repositories

# Verify internet connectivity
Test-NetConnection ctan.org -Port 443

# Check MiKTeX Console logs
# Open MiKTeX Console > Settings > Directories > Show logs
```
**For TeX Live:**
```powershell
# Check repository connection
tlmgr repository list

# Verify internet connectivity
Test-NetConnection ctan.org -Port 443
```

**Solutions:**
**For MiKTeX:**
```powershell
# Solution 1: Change package repository
mpm --pick-repository
# Select different CTAN mirror

# Solution 2: Update package database
mpm --update-db
mpm --verify

# Solution 3: Clear package cache
Remove-Item -Path "C:\Users\$env:USERNAME\AppData\Local\MiKTeX\miktex\data\mpm\cache" -Recurse -Force
mpm --update-db

# Solution 4: Manual package download
# Visit https://ctan.org/pkg/<package-name>
# Download .tar.xz file
# Install via MiKTeX Console > Packages > + (Add package)
```
**For TeX Live:**
```powershell
# Solution 1: Update TeX Live
tlmgr update --self --all

# Solution 2: Change package repository (if default is problematic)
tlmgr option repository ctan
# Or choose a specific mirror: tlmgr option repository http://mirror.ctan.org/systems/texlive/tlnet

# Solution 3: Manual package download
# Visit https://ctan.org/pkg/<package-name>
# Download .zip or .tar.gz file
# Manually place files in TEXMF tree (advanced)
```

### 8.3 LaTeX Installation Permission/UAC Errors

**Problem:** Access denied or UAC prompts during installation

**Diagnosis:**
**For MiKTeX:**
```powershell
# Check if running as Administrator
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
Write-Host "Running as Administrator: $isAdmin"

# Check MiKTeX installation scope
mpm --admin --version
# If error: User installation
# If success: Admin installation
```
**For TeX Live:**
```powershell
# Check if running as Administrator
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
Write-Host "Running as Administrator: $isAdmin"

# TeX Live is typically installed system-wide, so UAC prompts are expected during initial install.
# Verify installation directory permissions if issues persist.
```

**Solutions:**
**For MiKTeX:**
```powershell
# Solution 1: Run PowerShell as Administrator
# Right-click PowerShell > Run as Administrator

# Solution 2: For user installations, avoid --admin flag
# Use: mpm --install=<package>
# Not: mpm --admin --install=<package>

# Solution 3: Reinstall MiKTeX with correct scope
# Uninstall via Control Panel > Programs
# Reinstall choosing "You only" or "All users" consistently

# Solution 4: Fix file permissions
# Right-click MiKTeX directory > Properties > Security
# Grant Full Control to your user account
```
**For TeX Live:**
```powershell
# Solution 1: Ensure installer was run as Administrator
# Re-run install-tl-windows.exe as Administrator if not done previously.

# Solution 2: Fix file permissions for TeX Live installation directory
# Right-click C:\texlive\<YEAR> directory > Properties > Security
# Grant Full Control to your user account
```

### 8.4 Python Module Import Errors

**Problem:** ImportError or ModuleNotFoundError when running scripts

**Diagnosis:**
```powershell
# Test Python import path
python -c "import sys; print('\n'.join(sys.path))"

# Verify script location
Get-ChildItem scripts\equation_extractor.py

# Check for __pycache__ conflicts
Get-ChildItem -Recurse -Filter "__pycache__" | Remove-Item -Recurse -Force
```

**Solutions:**
```powershell
# Solution 1: Run scripts from repository root
cd C:\Users\ericj\Git-Projects\Math_Science
python scripts\equation_extractor.py --base-dir .

# Solution 2: Set PYTHONPATH environment variable
$env:PYTHONPATH = "C:\Users\ericj\Git-Projects\Math_Science"

# Solution 3: Use absolute paths
python C:\Users\ericj\Git-Projects\Math_Science\scripts\equation_extractor.py

# Solution 4: Create __init__.py in scripts directory
New-Item -ItemType File -Path scripts\__init__.py
```

### 8.5 LaTeX Compilation Errors

**Problem:** Compilation fails with cryptic errors

**Common Errors and Solutions:**

#### Error: "Undefined control sequence"

```
! Undefined control sequence.
l.42 \aetherattr
```

**Solution:** Missing custom macro definition from preamble.tex

```powershell
# Verify preamble is included
Get-Content synthesis\main.tex | Select-String "preamble"
# Should show: \input{preamble}

# Ensure preamble.tex is in same directory
Test-Path synthesis\preamble.tex
```

#### Error: "Missing $ inserted"

```
! Missing $ inserted.
```

**Solution:** Math mode required for equation

```latex
% Incorrect
E = mc^2

% Correct
$E = mc^2$  % inline
\[ E = mc^2 \]  % display
```

#### Error: "Package babel Error: Unknown option 'english'"

**Solution:** Missing or conflicting babel package

**For MiKTeX:**
```powershell
# Install babel
mpm --install=babel
```
**For TeX Live:**
```powershell
# Install babel
tlmgr install babel
```

# Update preamble if needed
# Add: \usepackage[english]{babel}


#### Error: "File '*.tex' not found"

**Solution:** Incorrect file path or missing file

```powershell
# Verify chapter files exist
Get-ChildItem synthesis\chapters\*.tex

# Check \input or \include paths in main.tex
Get-Content synthesis\main.tex | Select-String "input|include"
```

### 8.6 General Debugging Tips

```powershell
# Enable verbose LaTeX output
pdflatex -interaction=errorstopmode document.tex

# Check LaTeX log file for detailed errors
Get-Content document.log | Select-String "Error|Warning" -Context 2

# Test minimal working example
@"
\documentclass{article}
\begin{document}
Hello World
\end{document}
"@ | Out-File -FilePath minimal.tex -Encoding utf8
pdflatex minimal.tex

# Clear LaTeX auxiliary files
Remove-Item *.aux, *.log, *.out, *.toc, *.synctex.gz -Force

# Update all MiKTeX packages
mpm --update

# Update all TeX Live packages
tlmgr update --self --all
```

---

## Additional Resources

### Official Documentation

- **MiKTeX Documentation:** https://miktex.org/docs
- **TeX Live Documentation:** https://www.tug.org/texlive/doc.html
- **Python Documentation:** https://docs.python.org/3/
- **LaTeX Project:** https://www.latex-project.org/
- **CTAN (Comprehensive TeX Archive Network):** https://ctan.org/

### Community Support

- **TeX Stack Exchange:** https://tex.stackexchange.com/
- **MiKTeX Issues:** https://github.com/MiKTeX/miktex/issues
- **TeX Live Issues:** https://www.tug.org/texlive/bugs.html
- **Python Community:** https://www.python.org/community/

### LaTeX Packages Documentation

- **amsmath:** https://ctan.org/pkg/amsmath
- **physics:** https://ctan.org/pkg/physics
- **tikz/pgf:** https://ctan.org/pkg/pgf
- **hyperref:** https://ctan.org/pkg/hyperref
- **cleveref:** https://ctan.org/pkg/cleveref

---

## Revision History

| Date | Version | Changes |
|------|---------|---------|
| 2025-10-22 | 1.0 | Initial comprehensive installation guide |

---

**Document Status:** Production
**Maintained By:** Repository Owner
**Last Verified:** 2025-10-22

For installation issues or questions, please refer to the troubleshooting section or consult the official documentation links above.

---

## Strict LaTeX Checks

Treat warnings as errors to ensure reproducible, high-quality builds.

- Bash (Git Bash/WSL): `bash synthesis/scripts/compile_strict.sh`
- PowerShell: `pwsh synthesis/scripts/compile_strict.ps1`
- Makefile target: `make latex_strict`

These scripts compile the main synthesis document and then scan the LaTeX log for warnings. Any warning triggers a non-zero exit code.

## PDF Sources Directory

PDF extractors default to `source_materials/pdfs/` and fall back to `papers/`. Override with:

- `--papers-dir <dir>` to specify a directory
- `--pdf <file>` (repeatable) to target specific files

Examples:

```
python scripts/pdf_equation_extractor.py --base-dir . --papers-dir source_materials/pdfs
python scripts/pdf_image_equation_extractor.py --base-dir . --pdf "Comment on the Pais Superforce Theory.pdf"
```

---

## ASCII-Only Policy

This repository enforces an ASCII-only policy for code and documentation:

- Verify: `make ascii_guard`
- Normalize (docs/summaries): `make ascii_normalize`

The guard checks `.py`, `.md`, `.tex`, `.yml`, `.ps1`, `.sh`, and top-level docs for non-ASCII. Data and external source folders are excluded.


