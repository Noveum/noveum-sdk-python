# Integration Tests

End-to-end integration tests for the Noveum SDK.

## Test Types

### 🧪 Unit Tests (Fast - Mocked)
- **Location**: `../unit/`
- **45 tests** in 3 files
- **No API key needed**
- **< 1 second** execution
- Tests SDK logic with mocked responses

### 🌐 Integration Tests (Real API)
- **Location**: `.` (current directory)
- **14 test files**
- **API key required**
- Tests real API integration

## Quick Start

### Unit Tests (Recommended for Development)
```bash
cd /Users/mramanindia/work/noveum-sdk-python/tests/unit
pytest -v                     # All unit tests
pytest test_models.py -v      # Specific file
```

### Integration Tests
```bash
# Setup
export NOVEUM_API_KEY="your_api_key_here"
cd /Users/mramanindia/work/noveum-sdk-python/tests/integration

# Run tests (choose one method)
./run_test.sh datasets        # Helper script
./run_test.sh traces          # Helper script
pytest test_datasets.py -v    # Pytest
python test_datasets.py       # Standalone
```

## Test Files

| File | Tests | Status |
|------|-------|--------|
| `test_datasets.py` | 10 | Dataset CRUD + items |
| `test_traces.py` | 10 | Trace creation + retrieval |
| `test_scorers.py` | 9 | Scorer workflow |
| `test_auth.py` | 11 | Authentication |
| `test_api_keys.py` | 1 | API key management |
| `test_scorer_results.py` | 2 | Scorer results |
| `test_credentials.py` | 1 | Credentials |
| `test_projects.py` | 1 | Projects |
| `test_etl_jobs.py` | 1 | ETL jobs |
| `test_telemetry.py` | 10 | Telemetry |
| `test_telemetry_plugins.py` | 1 | Telemetry plugins |
| `test_webhooks.py` | 1 | Webhooks |
| `test_ai_chats.py` | 1 | AI chats |
| `test_other_apis.py` | 3 | Health/Status/Orgs |

## Requirements

- `NOVEUM_API_KEY` environment variable
- SDK installed: `pip install -e ../..`
- (Optional) `pytest` for advanced testing

## Pytest Commands

```bash
# Run all tests
pytest -v

# Run specific file
pytest test_datasets.py -v

# Run specific test
pytest test_datasets.py::test_create_dataset -v

# Verbose with print output
pytest test_datasets.py -vv -s

# Stop on first failure
pytest test_datasets.py -x
```

## Configuration Files

- `conftest.py` - Pytest fixtures and configuration
- `pytest.ini` - Pytest settings
- `run_test.sh` - Convenient test runner
- `test_data/` - Test data files (JSON datasets)

