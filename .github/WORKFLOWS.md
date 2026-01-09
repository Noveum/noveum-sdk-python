# GitHub Workflows Documentation

This document describes the GitHub Actions workflows and their test execution strategy for the Noveum SDK.

## Workflow Overview

### 1. **ci.yml** - Comprehensive CI Pipeline
- **Triggers**: Push to main, Pull Requests to main, Daily cron schedule
- **Jobs**:
  - `lint`: Code formatting, linting, and type checking
  - `security`: Security scanning with bandit and safety
  - `unit-test`: Unit tests on multiple OS/Python versions (all branches)
  - `integration-test`: Integration tests **only on main branch**
  - `build`: Package building and validation

### 2. **tests.yml** - Basic Test Runner
- **Triggers**: Push to main, Pull Requests to main
- **Jobs**:
  - `unit-test`: Unit tests on multiple Python versions (all branches)
  - `integration-test`: Integration tests **only on main branch**
  - `lint`: Code quality checks

### 3. **release.yml** - Release Pipeline
- **Triggers**: Tag pushes (v*)
- **Jobs**:
  - `test`: Runs both unit and integration tests
  - `build`: Package building
  - `publish-to-pypi`: PyPI publication via Trusted Publishing
  - `github-release`: GitHub release creation with artifacts

## Test Execution Strategy

### Unit Tests (`tests/unit/`)
- **When**: On every PR and main branch push
- **Where**: All workflows (ci.yml, tests.yml, release.yml)
- **Coverage**: Fast, isolated tests covering core components
- **Purpose**: Quick feedback, no external dependencies
- **Characteristics**:
  - No API key required
  - Mocked responses
  - < 5 seconds execution time
  - Tests SDK logic in isolation

### Integration Tests (`tests/integration/`)
- **When**: Only on main branch pushes and releases
- **Where**: ci.yml (main only), tests.yml (main only), release.yml
- **Coverage**: End-to-end tests with real API calls
- **Purpose**: Comprehensive testing with actual API interactions
- **Characteristics**:
  - Requires `NOVEUM_API_KEY`
  - Real API calls
  - Minutes execution time
  - Tests full integration flow

## Benefits

1. **Faster PR Feedback**: PRs only run unit tests (faster, no API costs)
2. **Comprehensive Main Testing**: Main branch gets full test coverage
3. **Cost Optimization**: Integration tests with API calls only when necessary
4. **Multi-Platform Coverage**: Unit tests run on Ubuntu, Windows, MacOS
5. **Release Safety**: Full test suite runs before any release

## Test Directory Structure

```text
tests/
├── unit/                      # Fast, isolated tests
│   ├── conftest.py           # Unit test fixtures
│   ├── pytest.ini            # Unit test configuration
│   ├── test_client_wrapper.py
│   ├── test_api_wrappers.py
│   ├── test_models.py
│   ├── test_datasets_wrappers.py
│   ├── test_traces_wrappers.py
│   ├── test_scorers_wrappers.py
│   ├── test_scorer_results_wrappers.py
│   ├── test_auth_wrappers.py
│   ├── test_api_keys_wrappers.py
│   ├── test_telemetry_wrappers.py
│   └── test_webhooks_projects_other_wrappers.py
├── integration/               # Real API tests
│   ├── conftest.py           # Integration test fixtures
│   ├── pytest.ini            # Integration test configuration
│   ├── test_datasets.py
│   ├── test_traces.py
│   ├── test_scorers.py
│   ├── test_scorer_results.py
│   ├── test_auth.py
│   ├── test_api_keys.py
│   ├── test_credentials.py
│   ├── test_projects.py
│   ├── test_etl_jobs.py
│   ├── test_telemetry.py
│   ├── test_telemetry_plugins.py
│   ├── test_webhooks.py
│   ├── test_ai_chats.py
│   └── test_other_apis.py
└── test_config.py            # Shared test configuration
```

## Workflow Conditions

### Pull Requests
- ✅ Unit tests run on all PRs
- ❌ Integration tests skipped on PRs
- ✅ Lint and security checks run

### Main Branch
- ✅ Unit tests run
- ✅ Integration tests run
- ✅ Full coverage reports
- ✅ Security scanning

### Releases (Tags)
- ✅ Complete test suite (unit + integration)
- ✅ Multi-platform validation
- ✅ Security scanning
- ✅ Package building
- ✅ PyPI publication
- ✅ GitHub release creation

## CI/CD Pipeline Details

### Linting and Code Quality
```yaml
- Black: Code formatting (120 char line length)
- isort: Import sorting
- Ruff: Fast Python linter
- Mypy: Type checking (optional, continue-on-error)
```

### Security Scanning
```yaml
- Bandit: Security issue detection
- Safety: Dependency vulnerability scanning
```

### Test Matrix
```yaml
Unit Tests:
  - OS: [Ubuntu, Windows, MacOS]
  - Python: [3.10, 3.11, 3.12]
  - Total: 9 combinations (excluding problematic ones)

Integration Tests:
  - OS: Ubuntu only
  - Python: 3.11 or 3.12
  - Main branch only
```

### Coverage Tracking
- Codecov integration for coverage reports
- Test results uploaded to Codecov
- Coverage badges in README

## PyPI Publishing (Trusted Publishing)

The release workflow uses PyPI's Trusted Publishing (OIDC) for secure, token-less publishing:

1. **Setup**: Configure Trusted Publisher on PyPI
   - Project: `noveum-sdk-python`
   - Repository: `Noveum/noveum-sdk-python`
   - Workflow: `release.yml`
   - Environment: `pypi`

2. **Process**:
   - Tag pushed: `v1.0.0`
   - Tests run (unit + integration)
   - Package built and validated
   - Published to PyPI automatically
   - GitHub release created

3. **Security**:
   - No PyPI tokens in repository
   - OIDC authentication
   - Short-lived credentials
   - Audit trail

## Required GitHub Secrets

- `CODECOV_TOKEN` - For coverage reporting
- `NOVEUM_API_KEY` - For integration tests
- No PyPI token needed (using Trusted Publishing)

## Running Workflows Locally

### Unit Tests
```bash
cd /Users/mramanindia/work/noveum-sdk-python
pytest tests/unit/ -v --cov=noveum_api_client
```

### Integration Tests
```bash
export NOVEUM_API_KEY="your_api_key"
pytest tests/integration/ -v
```

### Linting
```bash
black --check noveum_api_client/ tests/
isort --check-only noveum_api_client/ tests/
ruff check noveum_api_client/ tests/
mypy noveum_api_client/
```

### Security Scans
```bash
bandit -r noveum_api_client/
safety check
```

### Build Package
```bash
pip install build twine
python -m build
twine check dist/*
```

## Troubleshooting

### Tests Failing in CI but Passing Locally
- Check Python version consistency
- Verify dependencies are installed
- Check for environment-specific issues

### Integration Tests Timing Out
- Verify API key is valid
- Check API endpoint availability
- Increase timeout in pytest.ini

### Build Failing
- Update version in pyproject.toml
- Ensure all dependencies are specified
- Check for syntax errors in configuration files

## Best Practices

1. **Always run unit tests locally before pushing**
2. **Let CI run integration tests on main branch**
3. **Use meaningful commit messages**
4. **Keep PRs focused and small**
5. **Update CHANGELOG.md for significant changes**
6. **Tag releases with semantic versioning**

## Monitoring

- **GitHub Actions**: Check workflow runs
- **Codecov**: Monitor test coverage
- **PyPI**: Verify package uploads
- **Dependabot**: Review dependency updates

---

**Last Updated**: January 9, 2026  
**Package**: noveum-sdk-python  
**Repository**: https://github.com/Noveum/noveum-sdk-python
