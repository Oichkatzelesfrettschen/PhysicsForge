# Comprehensive LaTeX Compilation Test Suite
# Tests each foundation chapter individually, then all together

$chapters = @("ch01", "ch02", "ch03", "ch04", "ch05", "ch06")
$results = @()

Write-Host "=== LaTeX Compilation Test Suite ===" -ForegroundColor Cyan
Write-Host "Testing 6 individual chapters + 1 full Part I compilation" -ForegroundColor Cyan
Write-Host ""

# Test individual chapters
foreach ($ch in $chapters) {
    Write-Host "Testing $ch..." -NoNewline
    $output = pdflatex -interaction=nonstopmode "test_$ch.tex" 2>&1

    if ($LASTEXITCODE -eq 0 -and (Test-Path "test_$ch.pdf")) {
        Write-Host " SUCCESS" -ForegroundColor Green
        $results += "$ch : SUCCESS"
    } else {
        Write-Host " FAILED" -ForegroundColor Red
        $results += "$ch : FAILED"
        # Extract error from log
        $errorLine = Get-Content "test_$ch.log" | Select-String "^!" | Select-Object -First 1
        if ($errorLine) {
            Write-Host "  Error: $errorLine" -ForegroundColor Yellow
        }
    }
}

# Test full Part I
Write-Host ""
Write-Host "Testing full Part I (all 6 chapters)..." -NoNewline
$output = pdflatex -interaction=nonstopmode "test_part1_foundations.tex" 2>&1

if ($LASTEXITCODE -eq 0 -and (Test-Path "test_part1_foundations.pdf")) {
    Write-Host " SUCCESS" -ForegroundColor Green
    $results += "Part I Full : SUCCESS"
} else {
    Write-Host " FAILED" -ForegroundColor Red
    $results += "Part I Full : FAILED"
}

# Summary
Write-Host ""
Write-Host "=== Test Summary ===" -ForegroundColor Cyan
$results | ForEach-Object { Write-Host $_ }

# Count successes
$successCount = ($results | Select-String "SUCCESS").Count
Write-Host ""
Write-Host "$successCount / 7 tests passed" -ForegroundColor $(if ($successCount -eq 7) { "Green" } else { "Yellow" })
