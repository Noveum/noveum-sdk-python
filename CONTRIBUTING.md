# Contributing to Noveum SDK

Thank you for your interest in contributing to the Noveum SDK! This document provides guidelines and instructions for contributing.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Testing](#testing)
- [Code Style](#code-style)
- [Submitting Changes](#submitting-changes)
- [Release Process](#release-process)

## Code of Conduct

This project adheres to a code of conduct. By participating, you are expected to uphold this code. Please be respectful and constructive in all interactions.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/noveum-sdk-python.git
   cd noveum-sdk-python
   ```
3. Add the upstream repository:
   ```bash
   git remote add upstream https://github.com/Noveum/noveum-sdk-python.git
   ```

## Development Setup

### Prerequisites

- Python 3.10 or higher
- pip and virtualenv
- Git

### Installation

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install the package in development mode with dev dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

3. Verify installation:
   ```bash
   python -c "from noveum_api_client import NoveumClient; print('Success!')"
   ```

## Making Changes

### Branching Strategy

- `main` - Production-ready code
- `feature/*` - New features
- `bugfix/*` - Bug fixes
- `docs/*` - Documentation updates

### Creating a Branch

```bash
git checkout -b feature/your-feature-name
```

### Commit Messages

Use clear and descriptive commit messages:

```
feat: Add support for new API endpoint
fix: Handle timeout errors in client wrapper
docs: Update README with new examples
test: Add tests for dataset pagination
chore: Update dependencies
```

Prefix conventions:
- `feat:` - New features
- `fix:` - Bug fixes
- `docs:` - Documentation changes
- `test:` - Test additions/changes
- `chore:` - Maintenance tasks
- `refactor:` - Code refactoring

## Testing

### Running Tests

```bash
# Run all unit tests (fast, no API key needed)
pytest tests/unit/ -v

# Run integration tests (requires API key)
export NOVEUM_API_KEY="your_api_key"
pytest tests/integration/ -v

# Run with coverage
pytest tests/unit/ --cov=noveum_api_client --cov-report=html

# Run specific test file
pytest tests/unit/test_client_wrapper.py -v
```

### Writing Tests

- **Unit tests**: Mock all external dependencies, test logic in isolation
- **Integration tests**: Test actual API interactions (use test API key)
- Aim for >80% code coverage
- Test both success and error cases

Example unit test:
```python
def test_my_feature(mock_noveum_client):
    """Test my new feature"""
    result = mock_noveum_client.my_method()
    assert result["status_code"] == 200
```

## Code Style

We use automated code formatting and linting tools:

### Black (Code Formatting)
```bash
black noveum_api_client/ tests/
```

### isort (Import Sorting)
```bash
isort noveum_api_client/ tests/
```

### Ruff (Linting)
```bash
ruff check noveum_api_client/ tests/
```

### Mypy (Type Checking)
```bash
mypy noveum_api_client/
```

### Run All Checks
```bash
# Format code
black noveum_api_client/ tests/
isort noveum_api_client/ tests/

# Check for issues
ruff check noveum_api_client/ tests/
mypy noveum_api_client/
```

### Style Guidelines

- Line length: 120 characters
- Use type hints for function parameters and return values
- Write docstrings for all public functions and classes
- Follow PEP 8 conventions

## Submitting Changes

### Before Submitting

1. Run all tests and ensure they pass:
   ```bash
   pytest tests/unit/ -v
   ```

2. Run code quality checks:
   ```bash
   black --check noveum_api_client/ tests/
   isort --check-only noveum_api_client/ tests/
   ruff check noveum_api_client/ tests/
   ```

3. Update documentation if needed

4. Add tests for new features

### Pull Request Process

1. Update your branch with the latest upstream changes:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

3. Open a Pull Request on GitHub with:
   - Clear title and description
   - Reference any related issues
   - List of changes made
   - Screenshots (if UI-related)

4. Wait for CI checks to pass

5. Address any review comments

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests pass
- [ ] Integration tests pass (if applicable)
- [ ] Added new tests

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No new warnings generated
```

## Release Process

Releases are automated via GitHub Actions when a version tag is pushed.

### For Maintainers

1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md` with release notes
3. Commit changes:
   ```bash
   git commit -am "chore: Bump version to X.Y.Z"
   ```
4. Create and push tag:
   ```bash
   git tag vX.Y.Z
   git push origin main --tags
   ```
5. GitHub Actions will automatically:
   - Run full test suite
   - Build package
   - Publish to PyPI
   - Create GitHub release

## Questions?

- Open an issue for bug reports or feature requests
- Check existing issues and pull requests first
- Contact: team@noveum.ai

## License

By contributing, you agree that your contributions will be licensed under the Apache 2.0 License.

---

Thank you for contributing to Noveum SDK! 🎉

