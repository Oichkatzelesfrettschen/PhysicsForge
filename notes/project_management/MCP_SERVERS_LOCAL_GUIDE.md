# Local MCP Servers Guide - No External Accounts Required

**Purpose**: Comprehensive guide to Model Context Protocol (MCP) servers that run entirely locally without requiring API keys or external accounts.

**Platform**: Windows 11, PowerShell
**Date**: 2025-10-19

---

## What is MCP?

Model Context Protocol (MCP) is an open standard introduced by Anthropic (November 2024) that allows AI to communicate with external data sources, tools, and services securely and flexibly. Think of it as "database connectors for AI" - standardized interfaces that let Claude Code access local tools, files, databases, and computational engines.

## Why Local-Only Servers?

**Advantages**:
- No API costs or rate limits
- Complete privacy (data never leaves your machine)
- Works offline
- No account creation or authentication hassles
- Full control over data and computation

**Trade-offs**:
- Requires local installation and configuration
- Computational resources limited to your machine
- Some features (web search, cloud APIs) require internet

---

## Tier 1: Essential Local MCP Servers

### 1. Filesystem Server (Anthropic Official)

**Purpose**: Secure file operations - read, write, search, create directories, move files

**Why Essential**: Core functionality for any file-based project (like LaTeX synthesis)

**Installation**:
```powershell
# Via npm (Node.js required)
npm install -g @modelcontextprotocol/server-filesystem

# Via npx (no global install)
npx @modelcontextprotocol/server-filesystem <allowed-directory>
```

**Configuration** (in Claude Code MCP settings):
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "@modelcontextprotocol/server-filesystem",
        "C:\\Users\\ericj\\Git-Projects\\Math_Science"
      ]
    }
  }
}
```

**Security Features**:
- Path validation (no escaping allowed directories)
- Gitignore-style exclusion patterns
- Explicit directory allowlisting
- Operations require user approval

**Capabilities**:
- `read_file`: Read file contents
- `write_file`: Write/overwrite files
- `edit_file`: In-place edits
- `create_directory`: Make directories
- `list_directory`: List contents
- `move_file`: Rename/move files
- `search_files`: Grep-like search
- `get_file_info`: Metadata (size, modified time)

**Use Cases for This Project**:
- Read source markdown documents
- Create LaTeX chapter files
- Update equation modules
- Search for specific equations or sections

---

### 2. SymPy-MCP (Symbolic Mathematics)

**Purpose**: Symbolic algebra, calculus, differential equations, tensor calculus

**Why Essential**: Mathematical derivations, equation verification, dimensional analysis

**Installation**:
```powershell
# Requires Python 3.12+
pip install sympy-mcp

# Optional: General relativity calculations
pip install einsteinpy
```

**Repository**: https://github.com/sdiehl/sympy-mcp

**Configuration**:
```json
{
  "mcpServers": {
    "sympy": {
      "command": "python",
      "args": ["-m", "sympy_mcp"]
    }
  }
}
```

**Capabilities**:
- **Algebraic Equations**: Solve polynomial, transcendental, systems of equations
- **Calculus**: Differentiate, integrate (definite/indefinite), series expansions
- **Differential Equations**: Solve ODEs, PDEs
- **Linear Algebra**: Matrix operations, eigenvalues, diagonalization
- **Vector Calculus**: Gradient, divergence, curl, line/surface integrals
- **Tensor Calculus**: Christoffel symbols, Riemann tensor, Einstein tensor
- **Number Theory**: Prime factorization, modular arithmetic
- **Simplification**: Algebraic simplification, trigonometric identities

**Use Cases for This Project**:
- Derive Cayley-Dickson multiplication rules
- Verify Riemann curvature tensor expressions
- Simplify Genesis kernel equations
- Compute Christoffel symbols for metric perturbations
- Validate dimensional consistency

**Security Note**: Uses `parse_expr()` which internally uses `eval()` - trust the code you generate.

---

### 3. SQLite MCP Server (Local Database)

**Purpose**: Structured data storage, query execution, knowledge management

**Why Useful**: Equation catalog, reference database, build metadata

**Installation**:
```powershell
# Option A: jparkerweb implementation (comprehensive)
npm install -g mcp-sqlite

# Option B: Community version
npm install -g @modelcontextprotocol/server-sqlite
```

**Repository**: https://github.com/jparkerweb/mcp-sqlite

**Configuration**:
```json
{
  "mcpServers": {
    "sqlite": {
      "command": "npx",
      "args": [
        "mcp-sqlite",
        "--db-path", "C:\\Users\\ericj\\Git-Projects\\Math_Science\\notes\\synthesis\\synthesis.db"
      ]
    }
  }
}
```

**Capabilities**:
- Execute SELECT queries
- Create/modify tables
- Insert/update/delete records
- Database introspection (schema, tables, indexes)
- Transaction support
- Query result formatting

**Features**:
- Uses WAL (Write-Ahead Logging) for concurrent access
- Parameterized queries (SQL injection prevention)
- Single-file database (no server process)

**Use Cases for This Project**:
- Store equation catalog as database (better than CSV)
- Track chapter completion status
- Reference management (bibliography database)
- Cross-reference index
- Build statistics and analytics

---

### 4. Git MCP Server (Local Repository Operations)

**Purpose**: Git operations from within Claude Code

**Why Useful**: Automated commits, branch management, history analysis

**Installation**:
```powershell
# Option A: cyanheads implementation (comprehensive)
npm install -g git-mcp-server

# Option B: Local git server
npm install -g local-git-mcp-server
```

**Repository**: https://github.com/cyanheads/git-mcp-server

**Configuration**:
```json
{
  "mcpServers": {
    "git": {
      "command": "npx",
      "args": [
        "git-mcp-server",
        "--working-dir", "C:\\Users\\ericj\\Git-Projects\\Math_Science"
      ]
    }
  }
}
```

**Capabilities**:
- `git_status`: Check working tree status
- `git_diff`: View changes
- `git_log`: Commit history
- `git_commit`: Create commits
- `git_branch`: Branch operations
- `git_checkout`: Switch branches
- `git_merge`: Merge branches
- `git_rebase`: Rebase operations
- `git_tag`: Tag management
- `git_clone`: Clone repositories
- `git_pull` / `git_push`: Remote sync

**Use Cases for This Project**:
- Automated chapter completion commits
- Track equation additions
- Branch per chapter for safe work
- Generate detailed commit messages with provenance

---

## Tier 2: Highly Recommended Local Servers

### 5. Sequential Thinking MCP

**Purpose**: Break complex tasks into logical steps, multi-phase planning

**Why Useful**: Architectural design, system decomposition, large-scale refactors

**Installation**:
```powershell
npm install -g sequential-thinking-mcp
```

**Capabilities**:
- Decompose complex problems
- Generate step-by-step plans
- Track progress through phases
- Validate logical dependencies

**Use Cases for This Project**:
- Plan complex chapter structures
- Decompose kernel equation derivations
- Multi-step conflict resolution analysis

---

### 6. Memory MCP Server (Anthropic Official)

**Purpose**: Persistent knowledge graph, long-term context retention

**Why Useful**: Remember project decisions, equation definitions, framework details across sessions

**Installation**:
```powershell
npm install -g @modelcontextprotocol/server-memory
```

**Configuration**:
```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": [
        "@modelcontextprotocol/server-memory",
        "--store-path", "C:\\Users\\ericj\\Git-Projects\\Math_Science\\notes\\.memory"
      ]
    }
  }
}
```

**Capabilities**:
- Store key-value pairs
- Create entity relationships (knowledge graph)
- Query by concept or relationship
- Persistent across sessions

**Use Cases for This Project**:
- Remember: "E₇ has 126 roots, not 127"
- Store: Framework conflict resolutions
- Track: Equation dependencies and derivations
- Link: Concepts across multiple documents

---

### 7. DuckDuckGo Search MCP (No API Key)

**Purpose**: Real-time web search for documentation, error resolution, concept exploration

**Why Useful**: Find LaTeX package docs, mathematical definitions, reference papers

**Installation**:
```powershell
npm install -g duckduckgo-mcp
```

**Configuration**:
```json
{
  "mcpServers": {
    "ddg-search": {
      "command": "npx",
      "args": ["duckduckgo-mcp"]
    }
  }
}
```

**Capabilities**:
- Text search (web results)
- Instant answers (Wikipedia, Wolfram)
- No rate limits
- No API key required

**Use Cases for This Project**:
- Find LaTeX package documentation
- Look up mathematical definitions
- Resolve compilation errors
- Find academic references

---

## Tier 3: Specialized Local Servers

### 8. Selenium MCP (Web Automation)

**Purpose**: Automated browser control (screenshot docs, interact with web tools)

**Installation**:
```powershell
pip install selenium-mcp-server
# Requires: Chrome/Firefox + WebDriver
```

**Use Cases**:
- Screenshot arXiv papers for reference
- Automate PDF downloads
- Test web-based equation renderers

---

### 9. Jupyter MCP (Computational Notebooks)

**Purpose**: Execute Python code in notebooks, generate plots, numerical analysis

**Installation**:
```powershell
pip install jupyter-mcp
```

**Repository**: Part of https://github.com/pathintegral-institute/mcp.science

**Use Cases for This Project**:
- Generate numerical datasets for pgfplots
- Visualize E₈ root system projections
- Compute Cayley-Dickson products in high dimensions
- Validate kernel equations numerically

---

## Configuration Strategy for This Project

### Recommended MCP Server Stack

**Minimal (start here)**:
1. **Filesystem** - Read/write project files
2. **SymPy** - Mathematical derivations
3. **Git** - Version control automation

**Optimal (full workflow)**:
Add:
4. **SQLite** - Equation database
5. **Memory** - Persistent knowledge
6. **DuckDuckGo** - Documentation lookup

**Advanced (if needed)**:
7. **Sequential Thinking** - Complex planning
8. **Jupyter** - Numerical computation

### Master Configuration File

Create: `C:\Users\ericj\.claude\mcp_config.json`

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "@modelcontextprotocol/server-filesystem",
        "C:\\Users\\ericj\\Git-Projects\\Math_Science"
      ]
    },
    "sympy": {
      "command": "python",
      "args": ["-m", "sympy_mcp"]
    },
    "git": {
      "command": "npx",
      "args": [
        "git-mcp-server",
        "--working-dir", "C:\\Users\\ericj\\Git-Projects\\Math_Science"
      ]
    },
    "sqlite": {
      "command": "npx",
      "args": [
        "mcp-sqlite",
        "--db-path", "C:\\Users\\ericj\\Git-Projects\\Math_Science\\notes\\synthesis\\synthesis.db"
      ]
    },
    "memory": {
      "command": "npx",
      "args": [
        "@modelcontextprotocol/server-memory",
        "--store-path", "C:\\Users\\ericj\\Git-Projects\\Math_Science\\notes\\.memory"
      ]
    },
    "ddg-search": {
      "command": "npx",
      "args": ["duckduckgo-mcp"]
    }
  }
}
```

### Installation Script

Create: `notes\synthesis\scripts\install_mcp_servers.ps1`

```powershell
#requires -version 7.0
# Install all local MCP servers for Math_Science project

Write-Host "Installing MCP Servers..." -ForegroundColor Green

# Node.js based servers
Write-Host "`n[1/6] Installing Filesystem server..."
npm install -g @modelcontextprotocol/server-filesystem

Write-Host "`n[2/6] Installing Git server..."
npm install -g git-mcp-server

Write-Host "`n[3/6] Installing SQLite server..."
npm install -g mcp-sqlite

Write-Host "`n[4/6] Installing Memory server..."
npm install -g @modelcontextprotocol/server-memory

Write-Host "`n[5/6] Installing DuckDuckGo search..."
npm install -g duckduckgo-mcp

# Python based servers
Write-Host "`n[6/6] Installing SymPy server..."
pip install sympy-mcp

# Optional: einsteinpy for general relativity
pip install einsteinpy

Write-Host "`n✓ All MCP servers installed!" -ForegroundColor Green
Write-Host "Configure in Claude Code settings: MCP Servers section"
```

---

## Usage Examples

### Example 1: Extract Equation from Source Document

**With Filesystem + SymPy**:
```
User: "Extract the Riemann curvature tensor equation from Alpha001.06
      around line 5000, simplify it, and create eq_riemann_curvature.tex"

Claude:
1. [Filesystem] Read Alpha001.06 lines 4900-5100
2. [SymPy] Parse and simplify the tensor expression
3. [Filesystem] Write modules/equations/eq_riemann_curvature.tex
4. [Git] Commit with message "[Equations] Add Riemann curvature tensor"
```

### Example 2: Database-Driven Equation Catalog

**With SQLite**:
```sql
-- Create equation catalog table
CREATE TABLE equations (
    id INTEGER PRIMARY KEY,
    label TEXT UNIQUE NOT NULL,
    source_doc TEXT,
    source_lines TEXT,
    framework TEXT,
    domain TEXT,
    status TEXT,
    file_path TEXT,
    description TEXT,
    chapter TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Query all Aether framework equations
SELECT label, description, chapter
FROM equations
WHERE framework = 'A'
ORDER BY chapter;
```

### Example 3: Persistent Memory Across Sessions

**With Memory server**:
```
User: "Remember: E₇ has 126 roots, not 127. The confusion comes from
      the number of E₇-symmetric uniform polytopes."

Claude: [Memory] Stores entity:
  - Concept: "E7_root_count"
  - Value: 126
  - Note: "NOT 127 - that's the polytope count"
  - Relations: [E6_root_count: 72, E8_root_count: 240]

[Next session]
User: "How many roots does E₇ have?"
Claude: [Memory] Retrieves → "E₇ has 126 roots (stored from previous session)"
```

---

## Troubleshooting

### Node.js Not Found
```powershell
# Install Node.js from https://nodejs.org/
# Verify:
node --version
npm --version
```

### Python Module Not Found
```powershell
# Ensure Python 3.12+
python --version

# Check pip
pip --version

# Install in virtual environment if needed
python -m venv venv_mcp
.\venv_mcp\Scripts\activate
pip install sympy-mcp
```

### Permission Errors
```powershell
# Run PowerShell as Administrator
# OR use --prefix for local install:
npm install --prefix C:\LocalMCP @modelcontextprotocol/server-filesystem
```

### MCP Servers Not Appearing in Claude Code
1. Restart Claude Code after configuration changes
2. Check MCP settings: Settings → MCP Servers
3. Verify JSON syntax in config file
4. Check server installation: `npx <server-name> --version`

---

## Performance Considerations

**Fast (< 100ms latency)**:
- Filesystem operations
- SQLite queries
- Memory lookups

**Medium (100ms - 1s)**:
- Git operations (status, diff, log)
- SymPy simple operations (simplify, solve linear equations)

**Slow (1s - 10s)**:
- SymPy complex operations (tensor calculus, PDEs)
- Large file searches
- Git operations on large repos

**Very Slow (10s+)**:
- SymPy very complex operations (high-dimensional tensors)
- Database operations on large datasets
- Web searches (network dependent)

**Optimization Tips**:
- Use caching for repeated operations
- Index SQLite database for frequent queries
- Batch filesystem operations when possible
- Use incremental git operations (status before full diff)

---

## Security Best Practices

1. **Filesystem Server**:
   - Only allow access to project directory
   - Use .gitignore-style exclusions for sensitive files
   - Regularly review allowed directories

2. **SymPy Server**:
   - Trust the mathematical expressions generated
   - Avoid arbitrary string-to-code conversion
   - Use in sandboxed environments for untrusted input

3. **Git Server**:
   - Don't auto-push without review
   - Use branches for experimental work
   - Verify commit messages before execution

4. **SQLite Server**:
   - Use parameterized queries
   - Regular backups of database files
   - Validate schema migrations

5. **Memory Server**:
   - Review stored knowledge periodically
   - Clear outdated/incorrect information
   - Backup .memory directory

---

## Next Steps

### Immediate (Now)
1. Install minimal MCP stack (Filesystem, SymPy, Git)
2. Test each server with simple operations
3. Configure in Claude Code settings

### Short-term (This Week)
1. Add SQLite for equation database
2. Populate Memory with framework definitions
3. Create MCP-powered workflow scripts

### Long-term (This Month)
1. Integrate MCP servers into build pipeline
2. Automate equation extraction with SymPy validation
3. Create custom MCP servers for project-specific needs

---

**References**:
- MCP Specification: https://modelcontextprotocol.io/
- Awesome MCP Servers: https://github.com/punkpeye/awesome-mcp-servers
- Anthropic Official Servers: https://github.com/modelcontextprotocol/servers
- SymPy-MCP: https://github.com/sdiehl/sympy-mcp

**Last Updated**: 2025-10-19
**Author**: Claude Code + ericj
**Project**: Math_Science Synthesis
