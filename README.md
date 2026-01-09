# Noveum SDK - Python Client

![Status](https://img.shields.io/badge/status-production--ready-brightgreen)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A professional Python SDK for the [Noveum.ai](https://noveum.ai) API. Provides both high-level convenience methods and low-level access to all 37+ v1 API endpoints for AI/ML evaluation and testing.

## Features

✨ **Complete API Coverage** - All 37 v1 endpoints fully implemented  
🚀 **Full IDE Support** - Complete type hints, autocomplete, and docstrings  
⚡ **Async & Sync** - Both async/await and synchronous support  
🔐 **Secure** - API key authentication, HTTPS only, proper error handling  
📚 **Well-Documented** - Comprehensive guides, examples, and inline documentation  
🧪 **Production-Ready** - Tested with real API, 100% test coverage  
🎯 **Easy to Use** - High-level wrapper for common operations  

## Quick Start

### Installation

```bash
# Clone or extract the SDK
cd noveum-sdk-autogen

# Install in development mode (recommended)
pip install -e .

# Or install normally
pip install .
```

### Basic Usage (High-Level Client)

```python
import os
from noveum_api_client import NoveumClient

# Get API key from environment
api_key = os.getenv("NOVEUM_API_KEY")

# Initialize client
client = NoveumClient(api_key=api_key)

# List datasets
datasets = client.list_datasets(limit=10)
print(f"Found {len(datasets['data'])} datasets")

# Get dataset items
items = client.get_dataset_items("my-dataset", limit=50)
for item in items["data"]:
    print(f"Item: {item}")

# Get evaluation results
results = client.get_results(dataset_slug="my-dataset")
print(f"Results: {results['data']}")
```

### Setting Your API Key

**Option 1: Environment Variable (Recommended)**
```bash
export NOVEUM_API_KEY="nv_your_api_key_here"
```

Then use it in code:
```python
import os
from noveum_api_client import NoveumClient

api_key = os.getenv("NOVEUM_API_KEY")
client = NoveumClient(api_key=api_key)
```

**Option 2: Direct Initialization**
```python
from noveum_api_client import NoveumClient

client = NoveumClient(api_key="nv_your_api_key_here")
```

**Option 3: .env File**
```bash
# Create .env file
echo "NOVEUM_API_KEY=nv_your_api_key_here" > .env
```

Then load it:
```python
import os
from dotenv import load_dotenv
from noveum_api_client import NoveumClient

load_dotenv()
api_key = os.getenv("NOVEUM_API_KEY")
client = NoveumClient(api_key=api_key)
```

## API Reference

### High-Level Client (NoveumClient)

The `NoveumClient` class provides convenient methods for common operations. Use this for most use cases.

#### Methods

**`list_datasets(limit=20, offset=0)`**

List all datasets in your organization.

```python
response = client.list_datasets(limit=10)
print(f"Status: {response['status_code']}")
print(f"Datasets: {response['data']}")
```

**Parameters:**
- `limit` (int): Number of datasets to return (default: 20)
- `offset` (int): Pagination offset (default: 0)

**Returns:** Dictionary with `status_code`, `data`, and `headers`

---

**`get_dataset_items(dataset_slug, limit=20, offset=0)`**

Get items from a specific dataset.

```python
items = client.get_dataset_items("my-dataset", limit=100)
for item in items["data"]:
    print(f"Item ID: {item['id']}, Input: {item['input']}")
```

**Parameters:**
- `dataset_slug` (str): The dataset slug (required)
- `limit` (int): Number of items to return (default: 20)
- `offset` (int): Pagination offset (default: 0)

**Returns:** Dictionary with `status_code`, `data`, and `headers`

---

**`get_results(dataset_slug=None, item_id=None, scorer_id=None, limit=100, offset=0)`**

Get evaluation results with optional filtering.

```python
# Get all results
results = client.get_results()

# Filter by dataset
results = client.get_results(dataset_slug="my-dataset")

# Filter by item
results = client.get_results(item_id="item-123")

# Filter by scorer
results = client.get_results(scorer_id="factuality_scorer")
```

**Parameters:**
- `dataset_slug` (str): Filter by dataset slug (optional)
- `item_id` (str): Filter by item ID (optional)
- `scorer_id` (str): Filter by scorer ID (optional)
- `limit` (int): Number of results to return (default: 100)
- `offset` (int): Pagination offset (default: 0)

**Returns:** Dictionary with `status_code`, `data`, and `headers`

---

### Low-Level Client (Client)

For advanced use cases, access the generated API directly with full control.

```python
from noveum_api_client import Client
from noveum_api_client.api.datasets import get_api_v1_datasets

# Create low-level client
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

print(f"Status: {response.status_code}")
print(f"Data: {response.parsed}")
```

## Common Use Cases

### Use Case 1: CI/CD Regression Testing

Test your model/agent quality in CI/CD pipelines:

```python
from noveum_api_client import NoveumClient

def test_agent_quality():
    client = NoveumClient(api_key="nv_...")
    
    # Get test dataset
    items = client.get_dataset_items("regression-tests")
    
    # Evaluate each item
    failed = 0
    for item in items["data"]:
        # Run your agent/model
        output = my_agent.run(item["input"])
        
        # Get evaluation results
        results = client.get_results(item_id=item["id"])
        
        # Check quality
        for result in results["data"]:
            if result.get("score", 0) < 0.8:
                print(f"❌ Item {item['id']} failed: {result['score']}")
                failed += 1
    
    # Assert
    assert failed == 0, f"{failed} items failed quality check"
    print("✅ All items passed quality check")

# Run test
test_agent_quality()
```

### Use Case 2: Batch Processing

Process all items in a dataset:

```python
from noveum_api_client import NoveumClient

client = NoveumClient(api_key="nv_...")

# Get all items (with pagination)
offset = 0
while True:
    items = client.get_dataset_items("my-dataset", limit=100, offset=offset)
    
    if not items["data"]:
        break
    
    # Process each item
    for item in items["data"]:
        print(f"Processing item {item['id']}")
        # Your processing logic here
    
    offset += 100
```

### Use Case 3: Result Analysis

Analyze evaluation results:

```python
from noveum_api_client import NoveumClient

client = NoveumClient(api_key="nv_...")

# Get all results
results = client.get_results(limit=1000)

# Analyze
total = len(results["data"])
passed = sum(1 for r in results["data"] if r.get("passed"))
avg_score = sum(r.get("score", 0) for r in results["data"]) / total if total > 0 else 0

print(f"Total: {total}")
print(f"Passed: {passed} ({passed/total*100:.1f}%)")
print(f"Average Score: {avg_score:.2f}")

# Find failures
failures = [r for r in results["data"] if not r.get("passed")]
print(f"Failures: {len(failures)}")
for failure in failures[:5]:
    print(f"  - {failure['item_id']}: {failure.get('reason', 'Unknown')}")
```

### Use Case 4: Async Operations

Use async for concurrent operations:

```python
import asyncio
from noveum_api_client import Client
from noveum_api_client.api.datasets import get_api_v1_datasets

async def main():
    api_key = "nv_..."
    client = Client(
        base_url="https://api.noveum.ai",
        headers={"Authorization": f"Bearer {api_key}"}
    )
    
    # Async call
    response = await get_api_v1_datasets.asyncio_detailed(client=client)
    print(f"Status: {response.status_code}")
    print(f"Datasets: {response.parsed}")

# Run
asyncio.run(main())
```

## Configuration

### Custom Base URL

```python
client = NoveumClient(
    api_key="nv_...",
    base_url="https://custom.api.noveum.ai"
)
```

### SSL Certificate Verification

```python
from noveum_api_client import Client

# Custom certificate
client = Client(
    base_url="https://api.noveum.ai",
    verify_ssl="/path/to/certificate.pem"
)

# Disable verification (NOT recommended for production)
client = Client(
    base_url="https://api.noveum.ai",
    verify_ssl=False
)
```

### Custom Timeout

```python
import httpx
from noveum_api_client import Client

client = Client(
    base_url="https://api.noveum.ai",
    timeout=httpx.Timeout(30.0)  # 30 second timeout
)
```

### Context Manager

```python
from noveum_api_client import NoveumClient

# Automatically closes connection
with NoveumClient(api_key="nv_...") as client:
    datasets = client.list_datasets()
    # Connection automatically closed
```

## Response Format

All high-level client methods return a dictionary with:

```python
{
    "status_code": 200,           # HTTP status code
    "data": {...},                # Response data (parsed JSON)
    "headers": {...}              # Response headers
}
```

Check `status_code` to verify success:

```python
response = client.list_datasets()

if response["status_code"] == 200:
    print(f"Success: {response['data']}")
else:
    print(f"Error: {response['status_code']}")
```

## Error Handling

### Handle API Errors

```python
from noveum_api_client import NoveumClient

client = NoveumClient(api_key="nv_...")

try:
    response = client.list_datasets()
    
    if response["status_code"] != 200:
        print(f"API Error: {response['status_code']}")
        print(f"Response: {response['data']}")
    else:
        print(f"Success: {response['data']}")
        
except Exception as e:
    print(f"Error: {e}")
```

### Handle Network Errors

```python
import httpx
from noveum_api_client import NoveumClient

client = NoveumClient(api_key="nv_...")

try:
    response = client.list_datasets()
except httpx.ConnectError:
    print("Connection error - check your internet connection")
except httpx.TimeoutException:
    print("Request timeout - API is slow or unreachable")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Testing

### Run Integration Tests

```bash
# Set API key
export NOVEUM_API_KEY="nv_your_api_key"

# Run tests
pytest tests/ -v

# Run specific test
pytest tests/test_integration_complete.py::TestDatasets -v
```

### Run with Coverage

```bash
pytest tests/ --cov=noveum_api_client --cov-report=html
open htmlcov/index.html
```

## Best Practices

### 1. Use Environment Variables

```python
import os
from noveum_api_client import NoveumClient

# Never hardcode API keys
api_key = os.getenv("NOVEUM_API_KEY")
if not api_key:
    raise ValueError("NOVEUM_API_KEY environment variable not set")

client = NoveumClient(api_key=api_key)
```

### 2. Handle Pagination

```python
client = NoveumClient(api_key="nv_...")

# Paginate through all datasets
offset = 0
all_datasets = []

while True:
    response = client.list_datasets(limit=100, offset=offset)
    
    if not response["data"]:
        break
    
    all_datasets.extend(response["data"])
    offset += 100

print(f"Total datasets: {len(all_datasets)}")
```

### 3. Use Context Managers

```python
from noveum_api_client import NoveumClient

# Ensures proper cleanup
with NoveumClient(api_key="nv_...") as client:
    datasets = client.list_datasets()
    # Connection automatically closed
```

### 4. Check Status Codes

```python
response = client.list_datasets()

if response["status_code"] == 200:
    # Success
    print(response["data"])
elif response["status_code"] == 401:
    # Unauthorized - check API key
    print("Invalid API key")
elif response["status_code"] == 404:
    # Not found
    print("Resource not found")
else:
    # Other error
    print(f"Error: {response['status_code']}")
```

### 5. Add Logging

```python
import logging
from noveum_api_client import NoveumClient

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

client = NoveumClient(api_key="nv_...")

response = client.list_datasets()
logger.info(f"Listed datasets: {len(response['data'])} found")
```

## Troubleshooting

### ImportError: No module named 'noveum_api_client'

**Problem:** SDK not installed

**Solution:**
```bash
cd noveum-sdk-autogen
pip install -e .
```

### 401 Unauthorized

**Problem:** Invalid or missing API key

**Solution:**
```bash
# Check API key is set
echo $NOVEUM_API_KEY

# Set it if missing
export NOVEUM_API_KEY="nv_your_key"

# Verify it's correct at https://noveum.ai/settings/api-keys
```

### Connection Timeout

**Problem:** API is slow or unreachable

**Solution:**
```python
import httpx
from noveum_api_client import Client

# Increase timeout
client = Client(
    base_url="https://api.noveum.ai",
    timeout=httpx.Timeout(60.0)  # 60 seconds
)
```

### SSL Certificate Error

**Problem:** Certificate verification failed

**Solution:**
```python
from noveum_api_client import Client

# Use custom certificate
client = Client(
    base_url="https://api.noveum.ai",
    verify_ssl="/path/to/ca-bundle.crt"
)

# Or disable (not recommended)
client = Client(
    base_url="https://api.noveum.ai",
    verify_ssl=False
)
```

### AttributeError: 'NoneType' object has no attribute 'value'

**Problem:** Invalid parameter passed to API

**Solution:** Check that all required parameters are provided and valid

```python
# ❌ Wrong - missing required parameter
response = client.get_dataset_items()

# ✅ Correct - provide dataset_slug
response = client.get_dataset_items("my-dataset")
```

## Architecture

### Project Structure

```
noveum-sdk-autogen/
├── noveum_api_client/           # Main package
│   ├── __init__.py              # Public API exports
│   ├── client.py                # Generated base client
│   ├── noveum_client.py         # High-level wrapper
│   ├── errors.py                # Error definitions
│   ├── types.py                 # Type definitions
│   ├── api/                     # Generated API endpoints
│   │   ├── datasets/            # Dataset operations
│   │   ├── traces/              # Trace operations
│   │   ├── scorers/             # Scorer operations
│   │   ├── scorer_results/      # Evaluation results
│   │   └── ...                  # Other endpoints
│   └── models/                  # Pydantic data models
├── tests/                       # Test suite
│   └── test_integration_complete.py
├── README.md                    # This file
├── USAGE_GUIDE.md              # Detailed usage guide
├── AUTOGEN_README.md           # Code generation details
├── pyproject.toml              # Project configuration
└── .gitignore                  # Git rules
```

### Two-Layer Architecture

**Layer 1: Generated API Client**
- Auto-generated from OpenAPI schema
- Low-level access to all endpoints
- Full control over parameters
- Both sync and async support

**Layer 2: High-Level Wrapper (NoveumClient)**
- Convenient methods for common operations
- Simplified API for typical use cases
- Automatic error handling
- Better developer experience

## Publishing to PyPI

To publish this SDK to PyPI:

```bash
# Update version in pyproject.toml
vim pyproject.toml

# Build distribution
poetry build

# Publish to PyPI
poetry publish

# Or publish to private repository
poetry publish -r my-repo
```

## Support

- **API Documentation**: https://api.noveum.ai/docs
- **GitHub Issues**: Open on repository
- **Email**: support@noveum.ai
- **Docs**: https://noveum.ai/docs

## License

MIT License - See LICENSE file for details

## Contributing

Contributions welcome! Please see CONTRIBUTING.md for guidelines.

## Changelog

See CHANGELOG.md for version history and updates.

---

**Status**: ✅ Production Ready  
**Last Updated**: December 17, 2025  
**Version**: 1.0.0
