@echo off
echo === MiKTeX Admin Repair ===
echo.

echo [1/4] Synchronizing links...
initexmf --admin --mklinks
if errorlevel 1 goto error

echo [2/4] Updating database (admin)...
initexmf --admin --update-fndb
if errorlevel 1 goto error

echo [3/4] Updating database (user)...
initexmf --update-fndb
if errorlevel 1 goto error

echo [4/4] Rebuilding format...
initexmf --admin --dump=pdflatex
if errorlevel 1 goto error

echo.
echo === SUCCESS ===
pdflatex --version
echo.
pause
exit /b 0

:error
echo.
echo === FAILED ===
pause
exit /b 1
