Param(
  [string]$Engine = "pdflatex",
  [string]$Main = "../main.tex"
)

Push-Location $PSScriptRoot
try {
  if ($Engine -ieq "latexmk") {
    latexmk -pdf $Main
  } else {
    pdflatex $Main
    pdflatex $Main
  }
} finally {
  Pop-Location
}

