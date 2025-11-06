# Maintainer: Your Name <youremail@example.com>

pkgname=physicsforge
pkgver=1.0.0
pkgrel=1
pkgdesc="A Math & Science Research Hub for data extraction, analysis, and LaTeX synthesis."
arch=('any')
url=""
license=('MIT')
depends=('python' 'python-pip' 'make' 'texlive-core' 'texlive-bin' 'texlive-latexextra')
makedepends=('git')
optdepends=('python-pymupdf: for PDF text extraction'
           'python-pix2tex: for PDF image OCR to LaTeX (from AUR)'
           'python-pytorch: for machine learning backend for pix2tex'
           'python-torchvision: for machine learning backend for pix2tex'
           'python-torchaudio: for machine learning backend for pix2tex'
           'python-pytest: for running tests'
           'ollama-cli: for running ollama batch scripts')
source=("$pkgname-$pkgver.tar.gz")
sha256sums=('1686630b012bce47789eb0c73bdb3fd0917e1150640ac16773fa99a3d0011a3e')

build() {
    # Do not run make, as it requires optional dependencies
    return 0
}

package() {
    cp -r . "$pkgdir/"
    find "$pkgdir" -name ".*" -exec rm -rf {} +
}