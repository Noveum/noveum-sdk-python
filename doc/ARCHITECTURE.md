# Noveum SDK - Architecture Documentation

## Overview

The Noveum SDK is a professional Python client for the Noveum.ai API, built with a two-layer architecture:

1. **Generated API Layer** - Auto-generated from OpenAPI schema (low-level)
2. **Wrapper Layer** - Hand-crafted convenience methods (high-level)

This hybrid approach combines the best of both worlds: automatic API coverage with optimized developer experience.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    User Application                         │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│              High-Level Wrapper (NoveumClient)              │
│  • list_datasets()                                          │
│  • get_dataset_items()                                      │
│  • get_results()                                            │
│  • Simplified API for common operations                     │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│           Generated API Client (Client)                     │
│  • 37 v1 endpoints                                          │
│  • Full OpenAPI coverage                                    │
│  • Both sync and async                                      │
│  • Type-safe with Pydantic                                  │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│              HTTP Transport Layer (httpx)                   │
│  • Connection pooling                                       │
│  • Async/await support                                      │
│  • SSL verification                                         │
│  • Timeout handling                                         │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                  Noveum API (api.noveum.ai)                 │
└─────────────────────────────────────────────────────────────┘
```

## Layer 1: Generated API Client

### Purpose
Provides low-level access to all API endpoints with full type safety and IDE support.

### Key Components

**Client Class** (`noveum_api_client/client.py`)
- Manages HTTP connections
- Handles authentication headers
- Configures timeouts and SSL
- Supports both sync and async

**API Modules** (`noveum_api_client/api/`)
- One module per API endpoint
- Each module has 4 functions:
  - `sync()` - Blocking request, returns parsed data
  - `sync_detailed()` - Blocking request, returns full response
  - `asyncio()` - Async request, returns parsed data
  - `asyncio_detailed()` - Async request, returns full response

**Pydantic Models** (`noveum_api_client/models/`)
- Type-safe data validation
- Automatic serialization/deserialization
- IDE autocomplete support

### Example: Low-Level Usage

```python
from noveum_api_client import Client
from noveum_api_client.api.datasets import get_api_v1_datasets

# Create client
client = Client(
    base_url="https://api.noveum.ai",
    headers={"Authorization": f"Bearer {api_key}"}
)

# Call API directly
response = get_api_v1_datasets.sync_detailed(
    client=client,
    limit=20,
    offset=0
)

# Access response
print(f"Status: {response.status_code}")
print(f"Data: {response.parsed}")
print(f"Headers: {response.headers}")
```

### Advantages
- ✅ Full API coverage (all 37 endpoints)
- ✅ Complete type safety
- ✅ IDE autocomplete
- ✅ Both sync and async
- ✅ Full control over parameters

### Disadvantages
- ❌ More verbose
- ❌ Requires knowledge of endpoint structure
- ❌ Manual error handling

## Layer 2: High-Level Wrapper

### Purpose
Provides convenient methods for common operations with simplified API.

### Key Components

**NoveumClient Class** (`noveum_api_client/noveum_client.py`)
- Wraps the generated Client
- Provides convenience methods
- Handles common use cases
- Simplified return format

### Convenience Methods

| Method | Purpose | Example |
| :--- | :--- | :--- |
| `list_datasets()` | List all datasets | `client.list_datasets(limit=10)` |
| `get_dataset_items()` | Get items from dataset | `client.get_dataset_items("slug")` |
| `get_results()` | Get evaluation results | `client.get_results(dataset_slug="x")` |

### Example: High-Level Usage

```python
from noveum_api_client import NoveumClient

# Create client
client = NoveumClient(api_key="nv_...")

# Use convenience methods
datasets = client.list_datasets()
items = client.get_dataset_items("my-dataset")
results = client.get_results()

# Simple response format
print(f"Status: {datasets['status_code']}")
print(f"Data: {datasets['data']}")
```

### Advantages
- ✅ Simple, intuitive API
- ✅ Covers 90% of use cases
- ✅ Automatic error handling
- ✅ Consistent response format
- ✅ Less code to write

### Disadvantages
- ❌ Limited to common operations
- ❌ Less control over parameters
- ❌ Not all endpoints exposed

## Design Decisions

### 1. Why Two Layers?

**Generated Layer**
- Ensures 100% API coverage
- Automatically stays in sync with API changes
- Provides full control when needed

**Wrapper Layer**
- Improves developer experience
- Reduces boilerplate code
- Makes common tasks simple

### 2. Why Auto-Generation?

**Advantages**
- ✅ Never out of sync with API
- ✅ 100% endpoint coverage
- ✅ Automatic type safety
- ✅ Consistent patterns

**Implementation**
- Uses `openapi-python-client`
- Regenerates when API changes
- Can be automated in CI/CD

### 3. Why Pydantic Models?

**Advantages**
- ✅ Type validation
- ✅ IDE support
- ✅ Serialization/deserialization
- ✅ Clear data contracts

### 4. Why httpx?

**Advantages**
- ✅ Modern HTTP client
- ✅ Async/await support
- ✅ HTTP/2 support
- ✅ Connection pooling
- ✅ Type hints

## Data Flow

### Request Flow

```
User Code
   ↓
NoveumClient.list_datasets()
   ↓
get_api_v1_datasets.sync_detailed()
   ↓
Client.get_httpx_client()
   ↓
httpx.Client.request()
   ↓
HTTPS → api.noveum.ai
```

### Response Flow

```
api.noveum.ai
   ↓
httpx.Client receives response
   ↓
Response parsing (JSON → Pydantic)
   ↓
get_api_v1_datasets returns Response
   ↓
NoveumClient wraps in dict
   ↓
User receives: {"status_code": 200, "data": {...}}
```

## Error Handling

### Hierarchy

```
Exception
├── httpx.HTTPError
│   ├── httpx.ConnectError
│   ├── httpx.TimeoutException
│   └── ...
├── ValidationError (Pydantic)
└── Other exceptions
```

### Handling Strategy

```python
try:
    response = client.list_datasets()
except httpx.ConnectError:
    # Network error
except httpx.TimeoutException:
    # Timeout
except Exception as e:
    # Other error
```

## Configuration

### Client Configuration

```python
from noveum_api_client import Client

client = Client(
    base_url="https://api.noveum.ai",        # API endpoint
    headers={"Authorization": "Bearer ..."},  # Auth headers
    timeout=30.0,                            # Request timeout
    verify_ssl=True,                         # SSL verification
    follow_redirects=False,                  # Redirect handling
)
```

### High-Level Client Configuration

```python
from noveum_api_client import NoveumClient

client = NoveumClient(
    api_key="nv_...",                        # API key
    base_url="https://api.noveum.ai",        # Custom endpoint
)
```

## Authentication

### Bearer Token

The SDK uses Bearer token authentication:

```
Authorization: Bearer nv_your_api_key
```

### Implementation

```python
# Low-level
client = Client(
    base_url="https://api.noveum.ai",
    headers={"Authorization": f"Bearer {api_key}"}
)

# High-level
client = NoveumClient(api_key=api_key)
# Automatically adds Bearer token
```

## Type System

### Pydantic Models

All request/response data is validated with Pydantic:

```python
from noveum_api_client.models import Dataset

# Type-safe
dataset: Dataset = response.parsed

# IDE knows the structure
print(dataset.name)
print(dataset.slug)
```

### Type Hints

All methods have complete type hints:

```python
def list_datasets(
    self,
    limit: int = 20,
    offset: int = 0,
) -> Dict[str, Any]:
    """..."""
```

## Testing Architecture

### Test Structure

```
tests/
└── test_integration_complete.py
    ├── TestDatasets
    ├── TestTraces
    ├── TestScorers
    ├── TestScorerResults
    ├── TestHighLevelClient
    └── TestClientConfiguration
```

### Test Categories

| Category | Purpose | Count |
| :--- | :--- | :--- |
| Unit Tests | Test individual methods | - |
| Integration Tests | Test with real API | 10 |
| Configuration Tests | Test client setup | 3 |

## Performance Considerations

### Connection Pooling

httpx automatically manages connection pools:

```python
# Reuses connections
client = Client(base_url="https://api.noveum.ai")
response1 = get_api_v1_datasets.sync_detailed(client=client)
response2 = get_api_v1_datasets.sync_detailed(client=client)
# Both requests reuse same connection
```

### Async for Concurrency

```python
import asyncio

async def fetch_all():
    tasks = [
        get_api_v1_datasets.asyncio_detailed(client=client),
        get_api_v1_traces.asyncio_detailed(client=client),
        get_api_v1_scorers.asyncio_detailed(client=client),
    ]
    return await asyncio.gather(*tasks)
```

### Pagination

```python
# Efficient pagination
offset = 0
while True:
    response = client.list_datasets(limit=100, offset=offset)
    if not response["data"]:
        break
    # Process response
    offset += 100
```

## Security

### API Key Management

- ✅ Never hardcode API keys
- ✅ Use environment variables
- ✅ Use .env files in development
- ✅ Rotate keys regularly

### HTTPS Only

- ✅ All requests use HTTPS
- ✅ SSL verification enabled by default
- ✅ Certificate validation enforced

### Data Validation

- ✅ Pydantic validates all data
- ✅ Type checking prevents injection
- ✅ No sensitive data in logs

## Extensibility

### Adding New Convenience Methods

```python
# In noveum_api_client/noveum_client.py

def get_dataset_by_name(self, name: str) -> Dict[str, Any]:
    """Get dataset by name."""
    datasets = self.list_datasets(limit=1000)
    for dataset in datasets["data"]:
        if dataset["name"] == name:
            return dataset
    return None
```

### Custom Client

```python
from noveum_api_client import Client

class MyClient(Client):
    def custom_method(self):
        """Custom functionality."""
        pass
```

### Middleware/Hooks

```python
from noveum_api_client import Client

def log_request(request):
    print(f"Request: {request.method} {request.url}")

def log_response(response):
    print(f"Response: {response.status_code}")

client = Client(
    base_url="https://api.noveum.ai",
    httpx_args={
        "event_hooks": {
            "request": [log_request],
            "response": [log_response],
        }
    }
)
```

## Maintenance

### Regenerating from OpenAPI

When the API changes:

```bash
# 1. Get new OpenAPI spec
cp new-openapi.json noveum-openapi.json

# 2. Fix any schema issues
python3 scripts/fix_openapi.py

# 3. Regenerate SDK
openapi-python-client generate \
    --path noveum-openapi-fixed.json \
    --output-path noveum-sdk-autogen \
    --overwrite

# 4. Test
pytest tests/

# 5. Update wrapper if needed
# Edit noveum_api_client/noveum_client.py

# 6. Commit
git add .
git commit -m "Regenerate SDK from updated OpenAPI spec"
```

### Version Management

Update version in `pyproject.toml`:

```toml
[tool.poetry]
name = "noveum-api-client"
version = "1.0.1"  # Bump version
```

## Best Practices

### For Users

1. **Use high-level client** for common operations
2. **Use low-level client** for advanced use cases
3. **Handle errors gracefully**
4. **Use environment variables** for API keys
5. **Paginate** through large result sets

### For Maintainers

1. **Keep wrapper simple** - add methods only for common patterns
2. **Regenerate regularly** - stay in sync with API
3. **Update tests** - add tests for new endpoints
4. **Update documentation** - keep docs in sync
5. **Version carefully** - follow semantic versioning

## Summary

The Noveum SDK provides a professional, well-architected Python client with:

- ✅ Complete API coverage (37+ endpoints)
- ✅ Two-layer architecture (generated + wrapper)
- ✅ Full type safety with Pydantic
- ✅ Both sync and async support
- ✅ Excellent developer experience
- ✅ Production-ready code quality

The hybrid approach ensures both automatic API coverage and optimized developer experience.
