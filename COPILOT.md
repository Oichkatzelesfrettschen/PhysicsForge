# COPILOT.md

This file provides guidance to GitHub Copilot (github.com/features/copilot) when working with code in this repository.

## Project Overview

This is a theoretical physics and advanced mathematics research repository synthesizing unified field theories, quantum-gravitational models, and crystalline spacetime engineering. The work integrates:

- **Aether Framework**: Scalar field dynamics, zero-point energy (ZPE), quantum foam, time crystals
- **Genesis Framework**: Exceptional Lie groups (E8, E7, E6, F4, G2), Cayley-Dickson algebras, fractal geometries, modular symmetries
- **Pais Framework**: Gravitational-electromagnetic unification with scalar-ZPE interactions
- **Mathematical Foundations**: Non-associative algebras, hyperdimensional constructs (up to 2048D), Monster Group modular invariants

**Platform**: Cross-platform (Windows 11 / Linux CachyOS)
**Shell**: PowerShell (Windows) / Bash (Linux)
**LaTeX Distribution**: MiKTeX (Windows) / TeX Live (Linux recommended)
**Python**: 3.10+ (standard library only for current tools)

## Repository Structure

The repository structure is detailed in `CLAUDE.md`. Please refer to that file for a complete overview.

## Build Commands

The build commands for both LaTeX and the Python-based equation catalog are detailed in `CLAUDE.md`. Please refer to that file for a complete overview.

## Agentic Workflows with GitHub Copilot

GitHub Copilot's agent-like capabilities can be leveraged to automate complex tasks within this repository. The following workflows are recommended:

### 1. Using the GitHub Copilot CLI

The GitHub Copilot CLI provides a powerful way to interact with the repository from the command line. You can use it to:

*   **Ask questions about the codebase:** `gh copilot explain "How does the equation extractor work?"`
*   **Get suggestions for commands:** `gh copilot suggest "run all tests"`
*   **Create and execute complex commands:** `gh copilot run "build the full LaTeX document and then run the repository audit"`

### 2. Creating Custom Copilot Agents

For recurring tasks, you can create custom Copilot agents. These agents can be tailored to specific workflows and can be triggered from GitHub Actions or the command line. Here are some examples of custom agents that would be useful for this repository:

*   **`new-equation-agent`**: An agent that automates the process of adding a new equation module. It would:
    1.  Prompt the user for the equation's descriptive name, source, framework, domain, and status.
    2.  Create the `eq_*.tex` file in `synthesis/modules/equations/` with the correct header.
    3.  Run the `equation_extractor.py` script to update the catalog.
    4.  Prompt the user for the chapter to link the equation in.
    5.  Add the `\input{}` command to the chapter file.
    6.  Run the test compilation for the chapter.

*   **`chapter-transformation-agent`**: An agent that transforms a chapter to the whitepaper style, as described in `CLAUDE.md`. It would:
    1.  Prompt the user for the chapter to transform.
    2.  Add an opening story.
    3.  Add worked examples.
    4.  Add physical interpretations.
    5.  Modularize equations.
    6.  Add framework attribution.
    7.  Run the test compilation for the chapter.

*   **`verification-agent`**: An agent that automatically verifies the output of other agents. It would:
    1.  Take a file path as input.
    2.  Run `wc -l`, `ls -lh`, and `grep` to check the file's line count, timestamp, and content.
    3.  Report any discrepancies.

### 3. Parallel Agent Execution

As recommended in `CLAUDE.md`, you can use multiple Copilot agents in parallel to speed up development. For example, you could use three instances of the `chapter-transformation-agent` to transform three chapters simultaneously.

## Verification Protocol

**The verification protocol outlined in `CLAUDE.md` is critical and must be followed for all agentic workflows.**

*   **NEVER** trust agent claims without verification.
*   Use `wc -l`, `ls -lh`, `grep`, and `head` to verify that files have been changed as expected.
*   Check line counts, timestamps, and content spot-checks.
*   Previous sessions with other agents have shown that they can claim success even when files are unchanged.
*   A 100% verification rate has been achieved in recent sessions by adhering to this strict checking protocol.

## Key Principles

The key principles of Quality Standards, Modularity, Validation, and Collaboration outlined in `CLAUDE.md` apply to all work done with GitHub Copilot in this repository. Please refer to that file for a complete overview.
