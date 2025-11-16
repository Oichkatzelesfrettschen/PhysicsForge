# CI/CD Infrastructure Guide

## Overview

PhysicsForge uses a comprehensive CI/CD pipeline built on GitHub Actions with local development tools for fast iteration.

## Workflows

### Active Workflows

#### 1. **ci.yml** - Continuous Integration
- **Triggers**: All pushes and PRs
- **Purpose**: Quality gates and validation
- **Jobs**:
  - `tests`: Run pytest suite with linting
  - `windows_tests`: Cross-platform validation
- **Duration**: ~5-7 minutes
- **Key Features**:
  - Dependency caching
  - ASCII guard validation
  - Plan and metrics validation

#### 2. **test-coverage.yml** - Coverage Reporting
- **Triggers**: Pushes to main, PRs
- **Purpose**: Track test coverage metrics
- **Jobs**:
  - `coverage`: Generate and upload coverage reports
- **Duration**: ~3-5 minutes
- **Outputs**: Coverage XML and term reports

#### 3. **performance.yml** - Performance Monitoring
- **Triggers**: Pushes to main, PRs, manual
- **Purpose**: Track CI/CD performance metrics
- **Jobs**:
  - `performance-metrics`: Measure test and lint timing
- **Duration**: ~5-7 minutes
- **Outputs**: Timing metrics in job summary

#### 4. **python_tests.yml** - Cross-Platform Testing
- **Triggers**: All pushes and PRs
- **Purpose**: Ensure compatibility across platforms
- **Matrix**: Ubuntu, Windows, macOS
- **Duration**: ~10-15 minutes

#### 5. **build.yml** - PDF and Web Deployment
- **Triggers**: Pushes to main, manual
- **Purpose**: Build PDFs and deploy to GitHub Pages
- **Jobs**:
  - `build-pdf`: LaTeX compilation
  - `build-chapters`: Individual chapter builds
  - `build-catalog`: Equation catalog generation
  - `build-web`: SVG generation and site preparation
  - `deploy`: GitHub Pages deployment
- **Duration**: ~15-25 minutes

#### 6. **release.yml** - Release Automation
- **Triggers**: Version tags (v*.*.*)
- **Purpose**: Create GitHub Releases with PDFs
- **Jobs**: Similar to build.yml plus release creation
- **Duration**: ~20-30 minutes

## Local Development Commands

### Quick Commands

```bash
# Fast validation before committing
make smoke # Quick tests + ASCII check (~10 seconds)
make pre-commit # Full pre-commit validation (~30 seconds)

# Testing
make test # Full test suite (~2 minutes)
make test-parallel # Parallel test execution (faster)
make test-coverage # Tests with coverage report
make test-timing # Show slowest tests

# Quality checks
make lint # ASCII guard + plan + metrics (~1 minute)
make ascii_guard # Just ASCII validation (~5 seconds)
make security-check # Security scan with bandit

# Comprehensive validation
make ci-check # What runs in CI (~3 minutes)
make full-check # All checks including coverage
```

### Development Workflow

1. **Before starting work:**
   ```bash
   git pull origin main
   pip install -r requirements-test.txt
   ```

2. **During development:**
   ```bash
   # Quick validation after each change
   make smoke
   
   # Before committing
   make pre-commit
   ```

3. **Before pushing:**
   ```bash
   # Full CI check
   make ci-check
   
   # Optional: Run coverage
   make test-coverage
   ```

4. **Pre-commit hooks:**
   ```bash
   # Install hooks (one-time)
   pip install pre-commit
   pre-commit install
   
   # Hooks run automatically on commit
   # Or run manually:
   pre-commit run --all-files
   ```

## Performance Optimizations

### Test Execution
- **Parallel testing**: Use `pytest -n auto` for multi-core execution
- **Test caching**: pytest caches results for unchanged files
- **Selective testing**: Run specific test files during development

### CI Caching
- **pip cache**: ~500MB Python packages cached
- **LaTeX cache**: ~2GB TeXLive packages cached
- **Test results**: pytest cache persisted between runs

### Timing Benchmarks
- Smoke tests: ~10 seconds
- Full test suite: ~2 minutes (sequential), ~45 seconds (parallel)
- Lint checks: ~1 minute
- PDF build: ~10-15 minutes

## Troubleshooting

### Common Issues

#### "ModuleNotFoundError: No module named 'lark'"
```bash
pip install -r requirements-test.txt
```

#### "make: *** missing separator"
- Makefile requires tabs, not spaces
- Check that recipe lines start with tabs

#### Tests hang or timeout
- Some tests are I/O intensive
- Use `pytest -x` to stop on first failure
- Use `pytest tests/test_specific.py` for single test file

#### ASCII guard failures
```bash
# Check violations
python scripts/ascii_guard.py --base-dir .

# Fix automatically (for supported files)
python scripts/fix_ascii_violations.py
```

#### Regex pattern errors after ASCII normalization
- Check for invalid character class ranges
- Move special chars outside `[ ]` or escape them
- Example: `[a-z->]` -> `[a-z]|->|`

## Continuous Improvement

### Adding New Tests
1. Create `tests/test_feature.py`
2. Follow existing test patterns
3. Use pytest fixtures from `conftest.py`
4. Run: `pytest tests/test_feature.py -v`

### Adding New Workflows
1. Create `.github/workflows/new-workflow.yml`
2. Follow existing workflow structure
3. Test with `workflow_dispatch` trigger first
4. Add to this documentation

### Performance Tuning
- Monitor workflow timing in GitHub Actions
- Use caching for expensive operations
- Consider parallel execution for independent jobs
- Profile slow tests with `pytest --durations=20`

## Monitoring and Metrics

### GitHub Actions Insights
- Navigate to repository -> Actions tab
- View workflow run history and timing
- Check failure rates and trends
- Download artifacts for debugging

### Coverage Reports
- Available in test-coverage workflow artifacts
- HTML report at `htmlcov/index.html`
- Track coverage trends over time
- Aim for >80% coverage on critical code

### Performance Metrics
- Test execution time tracked in performance workflow
- Lint timing measured automatically
- Repository metrics (LOC, file counts) tracked
- Build artifact sizes monitored

## Best Practices

### For Contributors
1. [x] Run `make smoke` frequently during development
2. [x] Run `make pre-commit` before committing
3. [x] Write tests for new features
4. [x] Keep commits small and focused
5. [x] Use ASCII-only characters in code/docs

### For Maintainers
1. [x] Monitor CI failure rates
2. [x] Review coverage reports regularly
3. [x] Update dependencies periodically
4. [x] Document workflow changes
5. [x] Optimize slow tests and builds

### For Releases
1. [x] Ensure all CI checks pass
2. [x] Update version numbers
3. [x] Create annotated tags: `git tag -a v1.0.0 -m "Release v1.0.0"`
4. [x] Push tags: `git push origin v1.0.0`
5. [x] Verify release workflow succeeds
6. [x] Check PDF attached to GitHub Release

## Support

For issues with CI/CD infrastructure:
1. Check this documentation first
2. Review recent workflow runs for patterns
3. Search existing issues
4. Create new issue with workflow run URL
5. Tag with `ci/cd` label
