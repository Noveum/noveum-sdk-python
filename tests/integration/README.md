# Integration Tests

Complete end-to-end integration tests for the Noveum SDK.

## Overview

These tests verify the complete lifecycle of all Noveum SDK APIs with real API calls. Each test file covers a specific API domain and tests the full CRUD workflow.

## Test Structure

| Test File | API Coverage | Tests | Flow |
|-----------|-------------|-------|------|
| `test_traces.py` | Traces API | 12 | Send → Verify → Query → Get Spans |
| `test_datasets.py` | Datasets API | 15 | Create → Items → Version → Publish → Delete |
| `test_scorers.py` | Scorers + Results API | 13 | Create Scorer → Add Results → Query → Delete |
| `test_scorer_results.py` | Scorer Results API | 13 | Create → Get → Update → Batch → Delete |
| `test_etl_jobs.py` | ETL Jobs API | 12 | Create → Configure → Trigger → Monitor → Delete |
| `test_projects.py` | Projects API | 12 | Create → Associate Datasets → Health → Delete |
| `test_audio.py` | Audio API | 14 | List → Upload → Get → Serve → Delete |
| `test_complete_flow.py` | All APIs | 12 | Full Journey: Traces → Datasets → Scorers → Projects |

**Total: 103 tests covering 55+ API endpoints**

## Quick Start

### 1. Set Environment Variables

```bash
export NOVEUM_API_KEY="nv_your_api_key_here"

# Optional (have sensible defaults)
export NOVEUM_BASE_URL="https://api.noveum.ai"
export NOVEUM_PROJECT="SDK_Integration_Test"
export NOVEUM_ENVIRONMENT="test"
export NOVEUM_ORG_SLUG="noveum-inc"
```

### 2. Run Tests

```bash
# Navigate to integration tests directory
cd tests/integration

# Run all tests
pytest -v

# Run specific test file
pytest test_traces.py -v

# Run specific test class
pytest test_datasets.py::TestDatasetsE2EFlow -v

# Run specific test
pytest test_datasets.py::TestDatasetsE2EFlow::test_01_list_datasets -v

# Run with output (shows print statements)
pytest test_complete_flow.py -v -s

# Run only fast tests (skip slow E2E)
pytest -v -m "not slow"

# Run tests for specific API
pytest -v -m traces
pytest -v -m datasets
pytest -v -m scorers
pytest -v -m etl
pytest -v -m projects
pytest -v -m audio
```

## Test Markers

Tests are organized with the following pytest markers:

| Marker | Description |
|--------|-------------|
| `integration` | All integration tests (auto-applied) |
| `slow` | Long-running tests |
| `serial` | Tests that must run in sequence |
| `traces` | Traces API tests |
| `datasets` | Datasets API tests |
| `scorers` | Scorers API tests |
| `etl` | ETL Jobs API tests |
| `projects` | Projects API tests |
| `audio` | Audio API tests |

## Test Flow Examples

### Traces E2E Flow
```
1. Check connection status
2. Send single trace
3. Verify trace ingestion (with retry)
4. Send batch traces
5. Verify batch ingestion
6. List traces with pagination
7. Get trace IDs
8. Get trace by ID
9. Get trace spans
10. Get filter values
11. Get directory tree
12. Get environments by projects
```

### Datasets E2E Flow
```
1. List existing datasets
2. Create new dataset
3. Get dataset by slug
4. Update dataset
5. Add items to dataset
6. List dataset items
7. Get single item
8. Create version
9. List versions
10. Get specific version
11. Get version diff
12. Publish version
13. Delete single item
14. Bulk delete items
15. Delete dataset
```

### Audio E2E Flow
```
1. List existing audio files
2. Test pagination parameters
3. Upload audio file (if supported)
4. Get audio by ID
5. Serve/stream audio content
6. Delete audio file
7. Verify deletion
```

### Complete Flow (Golden Path)
```
1. Verify API connection
2. Send traces → Verify ingestion → Query
3. Create dataset → Add items → Version & publish
4. Create scorer → Add evaluation results
5. Create project → Associate dataset
6. Verify all resources exist
7. Cleanup all resources
```

## Configuration Files

- `conftest.py` - Shared fixtures, markers, and utilities
- `pytest.ini` - Pytest configuration
- `test_data/` - Test data files (JSON datasets)

## Fixtures Available

| Fixture | Scope | Description |
|---------|-------|-------------|
| `api_key` | session | API key from environment |
| `api_config` | session | Full API configuration dict |
| `session_client` | session | Session-scoped low-level client |
| `session_noveum_client` | session | Session-scoped high-level client |
| `low_level_client` | function | Test-scoped low-level client |
| `noveum_client` | function | Test-scoped high-level client |
| `unique_id` | function | Unique ID for test resources |
| `unique_slug` | function | Unique slug for datasets |
| `sample_trace_data` | function | Sample trace for testing |
| `sample_traces_batch` | function | Batch of sample traces |
| `sample_dataset_items` | function | Sample dataset items |
| `sample_scorer_results` | function | Sample scorer results |
| `test_context` | class | Shared context within a test class |

## Troubleshooting

### API Key Issues
```
❌ NOVEUM_API_KEY not set
Fix: export NOVEUM_API_KEY='nv_your_key_here'
```

### Connection Issues
```
❌ Connection timeout / refused
Fix: Check NOVEUM_BASE_URL is correct
     Check network connectivity
```

### Known Backend Issues
Some delete operations may return HTTP 500 - this is a known backend issue. Tests handle this gracefully with `pytest.xfail()`.

### Test Data Files Missing
```
❌ Test data file not found
Fix: Ensure test_data/ directory contains required JSON files
```

## Writing New Tests

Follow this pattern for new E2E tests:

```python
@pytest.mark.integration
@pytest.mark.serial  # If tests must run in order
class TestNewAPIE2EFlow:
    """E2E tests for New API."""

    @pytest.fixture(scope="class")
    def context(self) -> dict[str, Any]:
        """Shared context for tests."""
        return {}

    def test_01_setup(self, low_level_client, context):
        """Setup prerequisites."""
        # Create required resources
        context["resource_id"] = "created_id"

    def test_02_main_operation(self, low_level_client, context):
        """Test main operation."""
        assert context.get("resource_id")
        # Perform operation

    def test_03_verify(self, low_level_client, context):
        """Verify results."""
        # Verify operation succeeded

    def test_04_cleanup(self, low_level_client, context):
        """Clean up resources."""
        # Delete created resources
```

## CI/CD Integration

For CI/CD pipelines:

```bash
# Run all integration tests with JUnit output
pytest --junitxml=test-results.xml -v

# Run with coverage
pytest --cov=noveum_api_client --cov-report=xml

# Run only smoke tests (fast)
pytest -v -m "integration and not slow"

# Run full E2E suite
pytest -v -m "integration"
```
