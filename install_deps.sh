#!/bin/bash

# This script installs the essential dependencies for the PhysicsForge project.

# Set the SUDO_ASKPASS environment variable
export SUDO_ASKPASS="/usr/bin/sudo-askpass-oaich"

# Install dependencies from the official repositories
echo "Installing essential dependencies from the official repositories..."
sudo -A pacman -S --noconfirm --needed python python-pip make texlive-core texlive-bin texlive-latexextra python-bibtexparser
