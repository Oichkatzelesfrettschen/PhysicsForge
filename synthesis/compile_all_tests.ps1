# Comprehensive test compilation script for Windows PowerShell
# Compiles all 35 test files and generates report

$SynthesisDir = "C:\Users\ericj\Git-Projects\Math_Science\synthesis"
Set-Location $SynthesisDir

# List of all test files
$TestFiles = @(
    'test_ch01.tex', 'test_ch02.tex', 'test_ch03.tex', 'test_ch04.tex', 'test_ch05.tex',
    'test_ch06.tex', 'test_ch07.tex', 'test_ch08.tex', 'test_ch09.tex', 'test_ch10.tex',
    'test_ch11.tex', 'test_ch12.tex', 'test_ch13.tex', 'test_ch14.tex', 'test_ch15.tex',
    'test_ch16.tex', 'test_ch17.tex', 'test_ch18.tex', 'test_ch19.tex', 'test_ch20.tex',
    'test_ch21.tex', 'test_ch22.tex', 'test_ch23.tex', 'test_ch24.tex', 'test_ch25.tex',
    'test_ch26.tex', 'test_ch27.tex', 'test_ch28.tex', 'test_ch29.tex', 'test_ch30.tex',
    'test_part1_foundations.tex', 'test_part2_frameworks.tex', 'test_part3.tex',
    'test_part4.tex', 'test_part5.tex'
)

$Results = @()
$SuccessCount = 0
$FailedCount = 0

foreach ($TestFile in $TestFiles) {
    Write-Host "Compiling $TestFile..." -ForegroundColor Cyan

    $BaseName = [System.IO.Path]::GetFileNameWithoutExtension($TestFile)

    # Clean previous outputs
    Remove-Item -Path "$BaseName.aux", "$BaseName.log", "$BaseName.pdf", "$BaseName.bbl", "$BaseName.blg" -ErrorAction SilentlyContinue

    # Compile (3 passes for cross-references and bibliography)
    $null = & pdflatex -interaction=nonstopmode $TestFile 2>&1
    if (Test-Path "$BaseName.aux") {
        $null = & bibtex $BaseName 2>&1
    }
    $null = & pdflatex -interaction=nonstopmode $TestFile 2>&1
    $null = & pdflatex -interaction=nonstopmode $TestFile 2>&1

    # Check results
    if (Test-Path "$BaseName.pdf") {
        $PdfFile = Get-Item "$BaseName.pdf"
        $SizeKB = [math]::Round($PdfFile.Length / 1KB, 1)

        # Count pages - extract from log file
        $Pages = "?"
        if (Test-Path "$BaseName.log") {
            $LogContent = Get-Content "$BaseName.log" -Raw
            if ($LogContent -match "Output written.*\((\d+) page") {
                $Pages = $Matches[1]
            }
        }

        # Count errors
        $Errors = 0
        if (Test-Path "$BaseName.log") {
            $Errors = (Select-String -Path "$BaseName.log" -Pattern "^!" -AllMatches).Matches.Count
        }

        $Results += [PSCustomObject]@{
            File = $TestFile
            Status = "SUCCESS"
            Pages = $Pages
            Size = "$SizeKB KB"
            Errors = $Errors
        }
        $SuccessCount++
        Write-Host "  SUCCESS: $Pages pages, $SizeKB KB" -ForegroundColor Green
    } else {
        $Results += [PSCustomObject]@{
            File = $TestFile
            Status = "FAILED"
            Pages = 0
            Size = "0 KB"
            Errors = "N/A"
        }
        $FailedCount++
        Write-Host "  FAILED" -ForegroundColor Red
    }
}

# Output results
Write-Host "`n=== COMPILATION RESULTS ===" -ForegroundColor Yellow
$Results | Format-Table -AutoSize

Write-Host "`n=== SUMMARY ===" -ForegroundColor Yellow
Write-Host "Total tests: $($TestFiles.Count)"
Write-Host "Successful: $SuccessCount" -ForegroundColor Green
Write-Host "Failed: $FailedCount" -ForegroundColor Red
$SuccessRate = [math]::Round(($SuccessCount / $TestFiles.Count) * 100, 1)
Write-Host "Success rate: $SuccessRate%"

# Save results to CSV
$Results | Export-Csv -Path "test_compilation_results.csv" -NoTypeInformation
Write-Host "`nResults saved to test_compilation_results.csv"
