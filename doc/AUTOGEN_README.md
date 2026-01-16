# Noveum SDK - Auto-Generated from OpenAPI

This is a **Python SDK** for the Noveum.ai API, generated directly from the OpenAPI specification.

## Features

### Core API Coverage
- **8 API endpoint categories** fully implemented
- **All request/response models** with full type hints
- **Both sync and async** support for every endpoint
- **Full IDE support** with autocomplete and type checking

### Generated from OpenAPI
- Auto-generated from OpenAPI specification
- Guaranteed to stay in sync with API spec
- Easy to regenerate when API changes
- Professional code quality

### Easy to Use
```python
from noveum_api_client import NoveumClient

# High-level convenience client
client = NoveumClient(api_key="nv_...")

# List datasets
datasets = client.list_datasets()

# Get dataset items
items = client.get_dataset_items("my-dataset")

# Get evaluation results
results = client.get_results(dataset_slug="my-dataset")
```

Or use the low-level generated client for full control:
```python
from noveum_api_client import Client
from noveum_api_client.api.datasets import get_api_v1_datasets

client = Client(base_url="https://api.noveum.ai")
response = get_api_v1_datasets.sync_detailed(client=client)
```

## Package Structure

```
noveum-sdk-python/
├── noveum_api_client/
│   ├── __init__.py              # Main exports
│   ├── client.py                # Generated client class
│   ├── noveum_client.py         # High-level wrapper
│   ├── api/                     # Generated API endpoints
│   │   ├── datasets/            # Dataset operations
│   │   ├── traces/              # Trace operations
│   │   ├── scorers/             # Scorer operations
│   │   ├── scorer_results/      # Evaluation results
│   │   ├── projects/            # Project operations
│   │   ├── etl_jobs/            # ETL job operations
│   │   ├── health/              # Health check
│   │   └── status/              # Status endpoint
│   ├── models/                  # Generated data models
│   ├── errors.py                # Error handling
│   └── types.py                 # Type definitions
├── pyproject.toml               # Project configuration
└── README.md                    # Main documentation
```

## Quick Start

### Installation
```bash
pip install -e .
```

### Set API Key
```bash
export NOVEUM_API_KEY="nv_..."
```

### Use the SDK
```python
import os
from noveum_api_client import NoveumClient

api_key = os.getenv("NOVEUM_API_KEY")
client = NoveumClient(api_key=api_key)

# List datasets
response = client.list_datasets()
print(f"Status: {response['status_code']}")
print(f"Data: {response['data']}")

# Get dataset items
items = client.get_dataset_items("my-dataset")

# Get results
results = client.get_results()
```

## API Reference

### High-Level Client (`NoveumClient`)

#### Methods

**`list_datasets(limit=20, offset=0)`**
- List all datasets
- Returns: Dict with status_code, data, headers

**`get_dataset_items(dataset_slug, limit=20, offset=0)`**
- Get items from a dataset
- Returns: Dict with status_code, data, headers

**`get_results(dataset_slug=None, item_id=None, scorer_id=None, limit=100, offset=0)`**
- Get evaluation results
- Returns: Dict with results list

### Low-Level Generated Client

Access the full generated API client for complete control:

```python
from noveum_api_client import Client
from noveum_api_client.api.datasets import (
    get_api_v1_datasets,
    post_api_v1_datasets,
    get_api_v1_datasets_by_slug,
    # ... all other endpoints
)

client = Client(base_url="https://api.noveum.ai")

# Sync call
response = get_api_v1_datasets.sync_detailed(client=client)

# Async call
async with Client(...) as client:
    response = await get_api_v1_datasets.asyncio_detailed(client=client)
```

## Regenerating from OpenAPI

When the API changes:

```bash
# 1. Update OpenAPI spec
# 2. Fix any schema issues
python3 scripts/fix_openapi.py

# 3. Regenerate
python3 -m openapi_python_client generate \
    --path noveum-openapi.json \
    --output-path noveum-sdk-autogen \
    --overwrite

# 4. Test
pytest tests/

# 5. Commit and release
git add .
git commit -m "Regenerate SDK from updated OpenAPI spec"
```

## Testing

### Run Tests
```bash
pytest tests/ -v
```

### Test with Real API
```bash
export NOVEUM_API_KEY="nv_..."
pytest tests/integration/ -v
```

## Security

- API key from environment variable: `NOVEUM_API_KEY`
- Bearer token in Authorization header
- HTTPS only
- No API keys in logs

## API Endpoints

The SDK covers these endpoint categories:

### Health
- `GET /api/health` - Health check

### Status
- `GET /api/v1/status` - API status

### Datasets
- `GET /api/v1/datasets` - List datasets
- `POST /api/v1/datasets` - Create dataset
- `GET /api/v1/datasets/{slug}` - Get dataset
- `PUT /api/v1/datasets/{slug}` - Update dataset
- `DELETE /api/v1/datasets/{slug}` - Delete dataset
- `GET /api/v1/datasets/{datasetSlug}/items` - List items
- `POST /api/v1/datasets/{datasetSlug}/items` - Create item
- `GET /api/v1/datasets/{datasetSlug}/items/{itemId}` - Get item
- `DELETE /api/v1/datasets/{datasetSlug}/items/{itemId}` - Delete item
- And more...

### Traces
- `GET /api/v1/traces` - List traces
- `POST /api/v1/traces` - Create traces
- `GET /api/v1/traces/{id}` - Get trace
- `GET /api/v1/traces/{traceId}/spans` - Get spans
- And more...

### Scorers
- `GET /api/v1/scorers` - List scorers
- `POST /api/v1/scorers` - Create scorer
- `GET /api/v1/scorers/{id}` - Get scorer
- `PUT /api/v1/scorers/{id}` - Update scorer
- `DELETE /api/v1/scorers/{id}` - Delete scorer

### Scorer Results
- `GET /api/v1/scorers/results` - List results
- `POST /api/v1/scorers/results` - Create result
- `POST /api/v1/scorers/results/batch` - Batch results
- And more...

### Projects
- `GET /api/v1/projects` - List projects
- `POST /api/v1/projects` - Create project
- `GET /api/v1/projects/{id}` - Get project
- And more...

### ETL Jobs
- `GET /api/v1/etl-jobs` - List jobs
- `POST /api/v1/etl-jobs` - Create job
- `GET /api/v1/etl-jobs/{id}` - Get job
- And more...

## Examples

### CI/CD Regression Testing
```python
from noveum_api_client import NoveumClient

def test_agent_quality():
    client = NoveumClient(api_key="nv_...")
    
    # Get test dataset
    items = client.get_dataset_items("regression-tests")
    
    # Evaluate each item
    for item in items["data"]:
        output = my_agent.run(item["input"])
        result = client.get_results(item_id=item["id"])
        
        # Assert quality
        assert result["data"][0]["score"] > 0.8
```

### Using Low-Level API
```python
from noveum_api_client import Client
from noveum_api_client.api.datasets import get_api_v1_datasets_by_slug

client = Client(base_url="https://api.noveum.ai")

# Get specific dataset with full control
response = get_api_v1_datasets_by_slug.sync_detailed(
    slug="my-dataset",
    client=client,
)

print(f"Status: {response.status_code}")
print(f"Data: {response.parsed}")
print(f"Headers: {response.headers}")
```

## Development

### Project Structure
- `noveum_api_client/` - Generated SDK
- `noveum_api_client/noveum_client.py` - High-level wrapper (hand-written)
- `tests/` - Test suite
- `pyproject.toml` - Project config

### Code Generation
The SDK is generated using `openapi-python-client`:
- Generates complete type-safe code
- Includes both sync and async support
- Full IDE support with type hints
- Comprehensive docstrings

### Adding Features
To add convenience methods to the high-level client:
1. Edit `noveum_api_client/noveum_client.py`
2. Add method with docstring
3. Use underlying `self._client` to call API
4. Add tests

## Support

- **API Documentation**: https://api.noveum.ai/docs
- **Issues**: Open on GitHub
- **Email**: support@noveum.ai

## License

MIT License

## Summary

This is a **professional-grade Python SDK** for Noveum.ai featuring:

- **8 API endpoint categories** fully implemented
- **Full IDE support** with autocomplete and type hints
- **Both sync and async** for every endpoint
- **Auto-generated** from OpenAPI specification
- **High-level wrapper** for convenience
- **Production-ready** code quality
- **Comprehensive tests** included

**Ready to use immediately!**
