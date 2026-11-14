# Testing Guide

Comprehensive guide for testing the Noveum SDK Python client.

## Overview

The SDK includes two types of tests:

| Test Type | Purpose | Speed | API Key | Network |
|-----------|---------|-------|---------|---------|
| **Unit Tests** | Test SDK logic with mocked responses | < 5 seconds | Not needed | Not needed |
| **Integration Tests** | Test real API integration end-to-end | Minutes | Required | Required |

## Quick Start

### Prerequisites

```bash
# Install SDK with dev dependencies (run from the repository root)
pip install --upgrade pip setuptools wheel
pip install -e ".[dev]"

# Verify pytest is installed
pytest --version
```

### Run All Tests

```bash
# Unit tests only (fast, no API key needed)
pytest tests/unit/ -v

# Integration tests only (requires API key)
export NOVEUM_API_KEY="nv_your_api_key_here"
pytest tests/integration/ -v

# All tests with coverage
pytest tests/ -v --cov=noveum_api_client --cov-report=term-missing
```

## Unit Tests (Recommended for Development)

Fast, isolated tests with mocked API responses.

### Characteristics

- **Fast**: Runs in < 5 seconds
- **Isolated**: No network dependencies
- **No API key needed**
- **Comprehensive**: Tests all SDK logic, wrappers, and models
- **CI/CD friendly**: Perfect for continuous integration

### Test Files

#### Core SDK Tests

| File | Focus |
|------|-------|
| `test_client_wrapper.py` | High-level `NoveumClient` methods |
| `test_models.py` | Model serialization/validation |

#### API Category Tests

| File | Focus |
|------|-------|
| `test_audio_wrappers.py` | Audio API wrappers |
| `test_datasets_wrappers.py` | Dataset API wrappers |
| `test_etl_jobs_wrappers.py` | ETL job API wrappers |
| `test_projects_wrappers.py` | Project API wrappers |
| `test_scorers_wrappers.py` | Scorers API wrappers |
| `test_scorer_results_wrappers.py` | Scorer results API wrappers |
| `test_traces_wrappers.py` | Traces API wrappers |

### Running Unit Tests

```bash
# Navigate to unit tests
cd tests/unit

# Run all unit tests
pytest -v

# Run specific test file
pytest test_client_wrapper.py -v

# Run specific test
pytest test_client_wrapper.py::TestNoveumClientInit::test_client_initialization -v

# Run with coverage
pytest --cov=noveum_api_client --cov-report=html

# Show print statements
pytest -v -s

# Stop on first failure
pytest -x
```

### What's Tested

**Client Wrapper** (`test_client_wrapper.py`)
- Client initialization and configuration
- High-level convenience methods (`list_datasets`, `get_dataset_items`, `get_results`)
- Authentication handling (401, 403 errors)
- Error handling (network errors, timeouts, invalid responses)
- Response formatting consistency

**Models** (`test_models.py`)
- Model creation and initialization
- `to_dict()` serialization
- `from_dict()` deserialization
- Required vs optional fields
- Complex nested data structures
- JSON serialization
- Edge cases (empty dicts, large payloads, special characters)
- Model equality

### Example: Running Unit Tests

```bash
$ cd tests/unit
$ pytest -v

======================== test session starts ========================
test_client_wrapper.py::TestNoveumClientInit::test_client_initialization PASSED
test_client_wrapper.py::TestNoveumClientInit::test_client_with_custom_base_url PASSED
test_client_wrapper.py::TestListDatasets::test_list_datasets_success PASSED
...
test_models.py::test_model_to_dict PASSED
test_models.py::test_model_from_dict PASSED

======================== passed in 4.23s ========================
```

## Integration Tests

End-to-end tests with real API calls.

### Characteristics

- **Real API**: Tests actual API integration
- **API key required**: Uses `NOVEUM_API_KEY` environment variable
- **Network required**: Makes actual HTTP requests
- **Slower**: Takes several minutes to complete
- **Production validation**: Ensures SDK works with live API

### Test Files

| File | Focus |
|------|-------|
| `test_audio.py` | Audio file upload, retrieval, and management |
| `test_complete_flow.py` | End-to-end workflow tests |
| `test_datasets.py` | Dataset CRUD operations + items |
| `test_etl_jobs.py` | ETL job management |
| `test_projects.py` | Project operations |
| `test_scorers.py` | Scorer workflow |
| `test_scorer_results.py` | Scorer results retrieval |
| `test_traces.py` | Trace creation and retrieval |

### Running Integration Tests

```bash
# Set API key
export NOVEUM_API_KEY="nv_your_api_key_here"

# Navigate to integration tests
cd tests/integration

# Run all integration tests
pytest -v

# Run specific test file
pytest test_datasets.py -v

# Run specific test
pytest test_datasets.py::test_create_dataset -v

# Verbose with print output
pytest -vv -s

# Stop on first failure
pytest -x
```

### Example: Running Integration Tests

```bash
$ export NOVEUM_API_KEY="nv_..."
$ cd tests/integration
$ pytest test_datasets.py -v

======================== test session starts ========================
test_datasets.py::test_list_datasets PASSED
test_datasets.py::test_create_dataset PASSED
test_datasets.py::test_get_dataset PASSED
test_datasets.py::test_update_dataset PASSED
test_datasets.py::test_delete_dataset PASSED
test_datasets.py::test_list_dataset_items PASSED
test_datasets.py::test_create_dataset_item PASSED
test_datasets.py::test_get_dataset_item PASSED
test_datasets.py::test_update_dataset_item PASSED
test_datasets.py::test_delete_dataset_item PASSED

======================== 10 passed in 12.45s ========================
```

## Test Configuration

### Configuration Files

- `tests/unit/conftest.py` - Unit test fixtures (mocks)
- `tests/integration/conftest.py` - Integration test fixtures (API client)
- `tests/test_config.py` - Shared test configuration
- `pyproject.toml` - Pytest configuration and settings
- `codecov.yml` - Code coverage configuration

### Environment Variables

```bash
# Required for integration tests
export NOVEUM_API_KEY="nv_your_api_key_here"

# Optional: Custom API base URL
export NOVEUM_API_BASE_URL="https://custom.api.noveum.ai"

# Optional: Enable verbose logging
export PYTEST_VERBOSE=1
```

## Coverage Reports

### Generate Coverage Report

```bash
# Terminal report
pytest tests/ -v --cov=noveum_api_client --cov-report=term-missing

# HTML report (opens in browser)
pytest tests/ -v --cov=noveum_api_client --cov-report=html
open htmlcov/index.html

# XML report (for CI/CD)
pytest tests/ -v --cov=noveum_api_client --cov-report=xml

# Coverage summary
coverage report -m
```

### Expected Coverage

- **Target**: > 80% code coverage
- **Unit tests**: Cover SDK logic and wrappers
- **Integration tests**: Cover API integration paths

### Example Coverage Report

```bash
$ pytest tests/ --cov=noveum_api_client --cov-report=term-missing

----------- coverage: platform darwin, python 3.11.0 -----------
Name                                   Stmts   Miss  Cover   Missing
--------------------------------------------------------------------
noveum_api_client/__init__.py             10      0   100%
noveum_api_client/client.py              45      2    96%   123-124
noveum_api_client/noveum_client.py       78      5    94%   45, 67, 89, 102, 115
noveum_api_client/errors.py              12      0   100%
noveum_api_client/types.py               15      1    93%   42
--------------------------------------------------------------------
TOTAL                                   160      8    95%
```

## Troubleshooting

### ModuleNotFoundError: No module named 'pytest'

**Problem**: Pytest not installed

**Solution**:
```bash
# Upgrade pip and setuptools (required for PEP 621)
pip install --upgrade pip setuptools wheel

# Reinstall with dev dependencies
pip install -e ".[dev]"

# Verify pytest is installed
pytest --version
```

### Integration Tests Fail: 401 Unauthorized

**Problem**: Invalid or missing API key

**Solution**:
```bash
# Check if API key is set
echo $NOVEUM_API_KEY

# Set API key
export NOVEUM_API_KEY="nv_your_actual_api_key"

# Verify API key at https://noveum.ai/settings/api-keys

# Run tests again
pytest tests/integration/ -v
```

### Tests Take Too Long

**Problem**: Integration tests are slow

**Solution**:
```bash
# Run only unit tests for development (< 5 seconds)
pytest tests/unit/ -v

# Run specific integration test file
pytest tests/integration/test_datasets.py -v

# Stop on first failure to save time
pytest tests/integration/ -x
```

### Import Errors

**Problem**: SDK not installed properly

**Solution**:
```bash
# Reinstall SDK in development mode (run from the repository root)
pip install -e .

# Verify installation
python -c "from noveum_api_client import NoveumClient; print('SDK installed')"
```

### Connection Timeout in Integration Tests

**Problem**: Network or API is slow

**Solution**:
```bash
# Increase pytest timeout (in pytest.ini or command line)
pytest tests/integration/ -v --timeout=120

# Or skip integration tests temporarily
pytest tests/unit/ -v
```

## CI/CD Integration

### GitHub Actions

The SDK uses GitHub Actions for automated testing:

- **Workflow**: `.github/workflows/ci.yml`
- **Triggers**: Push, pull request
- **Tests**: Unit tests (fast)
- **Coverage**: Uploads to codecov.io

### Local CI Simulation

```bash
# Run the same tests as CI
pytest tests/unit/ -v --cov=noveum_api_client --cov-report=xml

# Check if ready for CI
pytest tests/unit/ -v -x --tb=short
```

## Best Practices

### 1. Run Unit Tests During Development

```bash
# Fast feedback loop
pytest tests/unit/ -v

# Watch mode (with pytest-watch)
pip install pytest-watch
ptw tests/unit/ -- -v
```

### 2. Run Integration Tests Before Commits

```bash
# Ensure changes work with real API
export NOVEUM_API_KEY="nv_..."
pytest tests/integration/test_datasets.py -v
```

### 3. Check Coverage Regularly

```bash
# Ensure new code is tested
pytest tests/ --cov=noveum_api_client --cov-report=term-missing
```

### 4. Use Markers for Selective Testing

```python
# In test file
@pytest.mark.slow
def test_large_dataset():
    # Slow test
    pass

@pytest.mark.fast
def test_quick_check():
    # Fast test
    pass
```

```bash
# Run only fast tests
pytest -m fast -v

# Skip slow tests
pytest -m "not slow" -v
```

### 5. Test in Clean Environment

```bash
# Use virtual environment
python -m venv venv
source venv/bin/activate
pip install -e ".[dev]"
pytest tests/ -v
```

## Adding New Tests

### Unit Test Template

```python
# tests/unit/test_my_feature.py
from unittest.mock import Mock, patch
import pytest
from noveum_api_client import NoveumClient

def test_my_feature(mock_noveum_client):
    """Test my new feature"""
    with patch('noveum_api_client.api.my_module.my_function') as mock_api:
        # Setup mock
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test"}
        mock_api.sync_detailed.return_value = mock_response
        
        # Test
        result = mock_noveum_client.my_method()
        
        # Assert
        assert result["status_code"] == 200
        assert result["data"] == "test"
```

### Integration Test Template

```python
# tests/integration/test_my_feature.py
import os
import pytest
from noveum_api_client import NoveumClient

@pytest.fixture(scope="module")
def client():
    api_key = os.getenv("NOVEUM_API_KEY")
    if not api_key:
        pytest.skip("NOVEUM_API_KEY not set")
    return NoveumClient(api_key=api_key)

def test_my_feature(client):
    """Test my feature with real API"""
    # Create test data
    response = client.my_method(param="value")
    
    # Assert
    assert response["status_code"] == 200
    assert "data" in response
    
    # Cleanup if needed
    # client.cleanup_method(...)
```

## Related Documentation

- [README.md](README.md) - Main SDK documentation
- [tests/unit/README.md](tests/unit/README.md) - Detailed unit test documentation
- [tests/integration/README.md](tests/integration/README.md) - Detailed integration test documentation
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines

## Support

For testing issues:
- **GitHub Issues**: https://github.com/Noveum/noveum-sdk-python/issues
- **Email**: support@noveum.ai
- **Documentation**: https://noveum.ai/docs

---

**Last Updated**: January 16, 2026
