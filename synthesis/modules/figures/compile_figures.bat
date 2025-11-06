@echo off
REM Compilation script for Chapter 28 figures
REM Author: Dr. Computernonymouse

echo Compiling Chapter 28 ZPE Technology Figures...
echo ============================================

echo.
echo Compiling Figure 1: Spherical Cavity...
pdflatex -interaction=nonstopmode fig_ch28_spherical_cavity.tex > nul 2>&1
if %errorlevel% equ 0 (
    echo [SUCCESS] Figure 1 compiled
) else (
    echo [ERROR] Figure 1 compilation failed
)

echo.
echo Compiling Figure 2: Cylindrical Cavity...
pdflatex -interaction=nonstopmode fig_ch28_cylindrical_cavity.tex > nul 2>&1
if %errorlevel% equ 0 (
    echo [SUCCESS] Figure 2 compiled
) else (
    echo [ERROR] Figure 2 compilation failed
)

echo.
echo Compiling Figure 3: Sierpinski Antenna...
pdflatex -interaction=nonstopmode fig_ch28_sierpinski_antenna.tex > nul 2>&1
if %errorlevel% equ 0 (
    echo [SUCCESS] Figure 3 compiled
) else (
    echo [ERROR] Figure 3 compilation failed
)

echo.
echo Compiling Figure 4: Extraction Schematic...
pdflatex -interaction=nonstopmode fig_ch28_extraction_schematic.tex > nul 2>&1
if %errorlevel% equ 0 (
    echo [SUCCESS] Figure 4 compiled
) else (
    echo [ERROR] Figure 4 compilation failed
)

echo.
echo Compiling Figure 5: Power vs Frequency...
pdflatex -interaction=nonstopmode fig_ch28_power_vs_frequency.tex > nul 2>&1
if %errorlevel% equ 0 (
    echo [SUCCESS] Figure 5 compiled
) else (
    echo [ERROR] Figure 5 compilation failed
)

echo.
echo Compiling Figure 6: TRL Timeline...
pdflatex -interaction=nonstopmode fig_ch28_trl_timeline.tex > nul 2>&1
if %errorlevel% equ 0 (
    echo [SUCCESS] Figure 6 compiled
) else (
    echo [ERROR] Figure 6 compilation failed
)

echo.
echo Compiling Figure 7: Efficiency Comparison...
pdflatex -interaction=nonstopmode fig_ch28_efficiency_comparison.tex > nul 2>&1
if %errorlevel% equ 0 (
    echo [SUCCESS] Figure 7 compiled
) else (
    echo [ERROR] Figure 7 compilation failed
)

echo.
echo ============================================
echo Compilation complete. Check PDFs for output.
echo.

REM Clean up auxiliary files
del *.aux *.log *.out 2>nul

pause