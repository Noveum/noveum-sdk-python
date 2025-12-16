# Contributing to Noveum SDK

Thank you for your interest in contributing to the Noveum SDK! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

Please be respectful and professional in all interactions. We are committed to providing a welcoming and inclusive environment for all contributors.

## Getting Started

### 1. Fork and Clone

```bash
# Fork the repository on GitHub
# Clone your fork
git clone https://github.com/YOUR_USERNAME/noveum-sdk-python.git
cd noveum-sdk-python
```

### 2. Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

### 3. Make Your Changes

Create a new branch for your feature or fix:

```bash
git checkout -b feature/your-feature-name
```

## Development Workflow

### Running Tests

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=noveum --cov-report=html

# Run specific test file
pytest tests/unit/test_client.py

# Run with verbose output
pytest tests/ -v
```

### Code Quality

```bash
# Format code with black
black noveum tests

# Lint with ruff
ruff check noveum tests

# Type check with mypy
mypy noveum

# Run all checks
pre-commit run --all-files
```

### Documentation

- Add docstrings to all public functions and classes
- Use Google-style docstrings
- Update README.md if adding new features
- Add examples for new functionality

## Submission Guidelines

### Before Submitting

1. **Write Tests**: Add tests for new functionality. Aim for 80%+ coverage.
2. **Update Documentation**: Update README.md and docstrings as needed.
3. **Follow Code Style**: Run `black` and `ruff` to ensure consistency.
4. **Test Locally**: Run the full test suite locally before submitting.

### Pull Request Process

1. Ensure all tests pass: `pytest tests/`
2. Ensure code is formatted: `black noveum tests`
3. Ensure no linting issues: `ruff check noveum tests`
4. Update CHANGELOG.md with your changes
5. Push to your fork and submit a pull request

### Pull Request Template

```markdown
## Description
Brief description of your changes.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Testing
Describe how you tested your changes.

## Checklist
- [ ] Tests pass locally
- [ ] Code is formatted with black
- [ ] No linting issues with ruff
- [ ] Documentation is updated
- [ ] CHANGELOG.md is updated
```

## Coding Standards

### Style Guide

- Follow PEP 8
- Use type hints for all function parameters and return types
- Maximum line length: 100 characters
- Use meaningful variable names

### Example

```python
from typing import Optional, List
from noveum.models import DatasetItem

def process_items(
    items: List[DatasetItem],
    batch_size: int = 10,
    timeout: Optional[float] = None,
) -> List[dict]:
    """
    Process dataset items in batches.
    
    Args:
        items: List of dataset items to process
        batch_size: Number of items per batch
        timeout: Optional timeout in seconds
        
    Returns:
        List of processed results
    """
    results = []
    for i in range(0, len(items), batch_size):
        batch = items[i : i + batch_size]
        # Process batch
        results.extend(batch)
    return results
```

## Commit Messages

Write clear, descriptive commit messages:

```
feat: add batch evaluation support
fix: handle rate limit errors correctly
docs: update README with async examples
test: add tests for pagination
refactor: simplify error handling
```

## Release Process

Maintainers follow this process for releases:

1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md`
3. Create a git tag: `git tag v0.2.0`
4. Push to GitHub: `git push origin main --tags`
5. GitHub Actions builds and publishes to PyPI

## Questions or Issues?

- Open an issue on GitHub for bugs or feature requests
- Check existing issues before opening a new one
- Provide clear reproduction steps for bugs
- Include your Python version and OS

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

Thank you for contributing! 🎉
