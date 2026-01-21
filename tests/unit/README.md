# Unit Tests

Fast, mocked unit tests for SDK wrapper functionality.

## Purpose

- ✅ **Fast**: No real API calls, runs in seconds
- ✅ **Isolated**: Tests SDK logic without network dependencies
- ✅ **Comprehensive**: Tests all wrapper methods, models, and error handling
- ✅ **Mocked**: Uses `unittest.mock` to simulate API responses

## Test Files

### Core SDK Tests
| File | Tests | Focus |
|------|-------|-------|
| `test_client_wrapper.py` | 11 | High-level `NoveumClient` methods |
| `test_api_wrappers.py` | 15 | Low-level API endpoint wrappers |
| `test_models.py` | 19 | `attrs` models serialization/validation |

### API Category Tests
| File | Tests | Focus |
|------|-------|-------|
| `test_datasets_wrappers.py` | 20+ | Dataset API wrappers |
| `test_traces_wrappers.py` | 30+ | Traces API wrappers |
| `test_scorers_wrappers.py` | 20+ | Scorers API wrappers |
| `test_scorer_results_wrappers.py` | 15+ | Scorer results API wrappers |
| `test_auth_wrappers.py` | 25+ | Authentication API wrappers |
| `test_api_keys_wrappers.py` | 15+ | API keys management wrappers |
| `test_telemetry_wrappers.py` | 25+ | Telemetry stats wrappers |
| `test_webhooks_projects_other_wrappers.py` | 20+ | Webhooks, projects, and misc wrappers |

## Quick Start

```bash
# Install pytest if needed
pip install pytest pytest-mock

# Run all unit tests
cd /Users/mramanindia/work/noveum-sdk-python/tests/unit
pytest -v

# Run specific test file
pytest test_client_wrapper.py -v

# Run specific test
pytest test_client_wrapper.py::TestNoveumClientInit::test_client_initialization -v

# Run with coverage
pytest --cov=noveum_api_client --cov-report=html
```

## What's Tested

### Client Wrapper (`test_client_wrapper.py`)
- ✅ Client initialization
- ✅ `list_datasets()` method
- ✅ `get_dataset_items()` method
- ✅ `get_results()` method
- ✅ Authentication handling (401, 403)
- ✅ Error handling (network, timeout, invalid responses)
- ✅ Response formatting consistency

### API Wrappers (`test_api_wrappers.py`)
- ✅ Request building (headers, params, body)
- ✅ Response parsing (JSON, empty, malformed)
- ✅ HTTP status codes (200, 400, 401, 403, 404, 500)
- ✅ Rate limiting (429)
- ✅ Pagination parameters
- ✅ Client configuration (base URL, timeout, headers)
- ✅ Data serialization

### Models (`test_models.py`)
- ✅ Model creation and initialization
- ✅ `to_dict()` serialization
- ✅ `from_dict()` deserialization
- ✅ Required vs optional fields
- ✅ Complex nested data structures
- ✅ JSON serialization
- ✅ Edge cases (empty dicts, large payloads, special characters)
- ✅ Model equality

## Key Features

### Mocking
All tests use mocked HTTP responses:
```python
mock_response = Mock(spec=httpx.Response)
mock_response.status_code = 200
mock_response.json.return_value = {"data": "test"}
```

### No Real API Calls
- ✅ No API key needed
- ✅ No network connection needed
- ✅ Fast execution (< 5 seconds)

### Comprehensive Coverage
- ✅ Success cases
- ✅ Error cases
- ✅ Edge cases
- ✅ Boundary conditions

## Running Tests

### All Tests
```bash
pytest -v
```

### By Category
```bash
pytest test_client_wrapper.py -v    # Client wrapper tests
pytest test_api_wrappers.py -v      # API wrapper tests
pytest test_models.py -v            # Model tests
```

### By Marker
```bash
pytest -m models -v    # Only model tests
pytest -m wrappers -v  # Only wrapper tests
pytest -m client -v    # Only client tests
```

### With Output
```bash
pytest -v -s           # Show print statements
pytest -vv             # Very verbose
pytest -x              # Stop on first failure
```

## Expected Results

All tests should **PASS** ✅:

```
======================== test session starts ========================
test_client_wrapper.py ................ [ XX%]
test_api_wrappers.py .................. [ XX%]
test_models.py ....................... [100%]

======================== XX passed in X.XXs ========================
```

## Difference from Integration Tests

| Aspect | Unit Tests | Integration Tests |
|--------|-----------|-----------|
| **Speed** | < 5 seconds | Minutes |
| **API Calls** | Mocked | Real |
| **API Key** | Not needed | Required |
| **Network** | Not needed | Required |
| **Purpose** | Test SDK logic | Test API integration |
| **When to Run** | Every code change | Before release |

## Adding New Tests

1. Create test file: `test_<feature>.py`
2. Import necessary modules and fixtures
3. Use `mock_client` or `mock_noveum_client` fixtures
4. Mock HTTP responses as needed
5. Assert expected behavior

Example:
```python
def test_my_feature(mock_noveum_client):
    """Test my new feature"""
    with patch('noveum_api_client.api...') as mock_api:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_api.sync_detailed.return_value = mock_response
        
        result = mock_noveum_client.my_method()
        
        assert result["status_code"] == 200
```

## Fixtures Available

From `conftest.py`:
- `mock_response` - Generic mock HTTP response
- `mock_client` - Mocked low-level `Client`
- `mock_noveum_client` - Mocked high-level `NoveumClient`
- `sample_dataset_response` - Sample dataset data
- `sample_dataset_items` - Sample dataset items
- `sample_trace_response` - Sample trace data
- `mock_api_error_response` - Mock 500 error
- `mock_auth_error_response` - Mock 401 error

## CI/CD Integration

These unit tests are perfect for CI/CD pipelines:

```yaml
# .github/workflows/test.yml
- name: Run Unit Tests
  run: |
    cd tests/unit
    pytest -v --junitxml=report.xml
```

Fast, reliable, no external dependencies needed!

