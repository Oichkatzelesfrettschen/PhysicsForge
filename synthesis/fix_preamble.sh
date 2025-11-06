#!/bin/bash
# Fix physics package conflicts by commenting out duplicate definitions

# Commands provided by physics package that we should NOT redefine:
# \Tr, \rank, \ket, \bra, \braket, \expval, \dv, \pdv, \grad, \div, \curl, \laplacian

cp preamble.tex preamble.tex.before_fix

# Comment out lines that define commands physics already provides
sed -i '/^\DeclareMathOperator{\Tr}{Tr}/s/^/% /' preamble.tex
sed -i '/^\DeclareMathOperator{\rank}{rank}/s/^/% /' preamble.tex
sed -i '/^\newcommand{\ket}\[1\]/s/^/% /' preamble.tex
sed -i '/^\newcommand{\bra}\[1\]/s/^/% /' preamble.tex  
sed -i '/^\newcommand{\braket}\[2\]/s/^/% /' preamble.tex
sed -i '/^\newcommand{\expval}\[1\]/s/^/% /' preamble.tex
sed -i '/^\newcommand{\pdv}\[2\]/s/^/% /' preamble.tex
sed -i '/^\newcommand{\dv}\[2\]/s/^/% /' preamble.tex
sed -i '/^\newcommand{\pdvsq}\[2\]/s/^/% /' preamble.tex
sed -i '/^\renewcommand{\div}/s/^/% /' preamble.tex
sed -i '/^\newcommand{\curl}/s/^/% /' preamble.tex
sed -i '/^\newcommand{\grad}/s/^/% /' preamble.tex
sed -i '/^\newcommand{\laplacian}/s/^/% /' preamble.tex

echo "Fixed preamble.tex - commented out physics package conflicts"
