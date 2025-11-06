@echo off
echo === MiKTeX Final Sync (Admin Update) ===
echo.
echo User was ahead of admin - running admin update again...
echo.

echo [1/3] Updating packages (admin mode)...
mpm --admin --verbose --update
if errorlevel 1 (
    echo WARNING: No new updates or update failed
)

echo.
echo [2/3] Refreshing database (admin)...
initexmf --admin --update-fndb
if errorlevel 1 goto error

echo.
echo [3/3] Rebuilding format (admin)...
initexmf --admin --dump=pdflatex
if errorlevel 1 goto error

echo.
echo === Verification ===
pdflatex --version
echo.

if errorlevel 1 (
    echo SYNC ERROR REMAINS
    pause
    exit /b 1
) else (
    echo.
    echo === CHECK OUTPUT ABOVE ===
    echo If "out-of-sync" message is GONE, we are fixed!
    echo.
    pause
    exit /b 0
)

:error
echo.
echo === FAILED ===
pause
exit /b 1
