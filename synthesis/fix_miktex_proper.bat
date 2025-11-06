@echo off
echo === MiKTeX Sync Fix (Proper Method) ===
echo.

echo [Step 1/5] Updating in ADMIN mode...
echo (This syncs admin-side packages and databases)
mpm --admin --verbose --update
if errorlevel 1 (
    echo WARNING: Admin update had issues, continuing...
)

echo.
echo [Step 2/5] Refreshing admin database...
initexmf --admin --update-fndb
if errorlevel 1 goto error

echo.
echo [Step 3/5] Updating admin font maps...
updmap --admin
if errorlevel 1 (
    echo WARNING: Admin updmap had issues, continuing...
)

echo.
echo [Step 4/5] Updating in USER mode...
mpm --verbose --update
if errorlevel 1 (
    echo WARNING: User update had issues, continuing...
)

echo.
echo [Step 5/5] Refreshing user database...
initexmf --update-fndb
if errorlevel 1 goto error

echo.
echo === Rebuilding Formats ===
echo.
echo Building pdflatex format (admin)...
initexmf --admin --dump=pdflatex
if errorlevel 1 goto error

echo.
echo === Final Verification ===
pdflatex --version
echo.

if errorlevel 1 (
    echo FAILED - pdflatex still has issues
    pause
    exit /b 1
) else (
    echo.
    echo === SUCCESS - MiKTeX is synchronized ===
    echo.
    pause
    exit /b 0
)

:error
echo.
echo === FAILED at step above ===
pause
exit /b 1
