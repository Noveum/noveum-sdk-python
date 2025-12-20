# Noveum SDK - Complete Usage Guide

## Quick Start

### Installation

```bash
pip install -e .
```

### Basic Usage

```python
from noveum_api_client import NoveumClient

# Initialize client
client = NoveumClient(api_key="nv_...")

# List datasets
datasets = client.list_datasets()

# Get dataset items
items = client.get_dataset_items("my-dataset")

# Get evaluation results
results = client.get_results()
```

## API Reference

### High-Level Client (NoveumClient)

The `NoveumClient` class provides convenient methods for common operations.

#### Methods

**`list_datasets(limit=20, offset=0)`**
- List all datasets
- Returns: `Dict[str, Any]` with status_code, data, headers

```python
response = client.list_datasets(limit=10)
print(f"Status: {response['status_code']}")
print(f"Datasets: {response['data']}")
```

**`get_dataset_items(dataset_slug, limit=20, offset=0)`**
- Get items from a dataset
- Returns: `Dict[str, Any]` with status_code, data, headers

```python
items = client.get_dataset_items("my-dataset", limit=50)
for item in items['data']:
    print(item)
```

**`get_results(dataset_slug=None, item_id=None, scorer_id=None, limit=100, offset=0)`**
- Get evaluation results
- Returns: `Dict[str, Any]` with status_code, data, headers

```python
results = client.get_results(dataset_slug="my-dataset")
for result in results['data']:
    print(f"Item {result['item_id']}: {result['score']}")
```

### Low-Level API Access

For advanced use cases, access the generated API directly:

```python
from noveum_api_client import Client
from noveum_api_client.api.datasets import get_api_v1_datasets

client = Client(base_url="https://api.noveum.ai")
response = get_api_v1_datasets.sync_detailed(
    client=client,
    limit=20,
    offset=0
)

print(f"Status: {response.status_code}")
print(f"Data: {response.parsed}")
print(f"Headers: {response.headers}")
```

## Common Use Cases

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
        
        # Get evaluation results
        results = client.get_results(item_id=item["id"])
        
        # Assert quality
        for result in results["data"]:
            assert result["score"] > 0.8, f"Low score: {result['score']}"
```

### Batch Processing

```python
client = NoveumClient(api_key="nv_...")

# Process all items in a dataset
items = client.get_dataset_items("my-dataset", limit=1000)

for item in items["data"]:
    # Process each item
    output = process_item(item)
    
    # Store or evaluate
    results = client.get_results(item_id=item["id"])
```

### Result Analysis

```python
client = NoveumClient(api_key="nv_...")

# Get all results
results = client.get_results(limit=1000)

# Analyze
total = len(results["data"])
passed = sum(1 for r in results["data"] if r.get("passed"))
avg_score = sum(r.get("score", 0) for r in results["data"]) / total

print(f"Total: {total}")
print(f"Passed: {passed} ({passed/total*100:.1f}%)")
print(f"Avg Score: {avg_score:.2f}")
```

## Advanced Usage

### Using the Low-Level Client

The low-level `Client` class gives you direct access to all API endpoints:

```python
from noveum_api_client import Client
from noveum_api_client.api import datasets, traces, scorers

client = Client(base_url="https://api.noveum.ai")

# Datasets
response = datasets.get_api_v1_datasets.sync_detailed(client=client)

# Traces
response = traces.get_api_v1_traces.sync_detailed(client=client)

# Scorers
response = scorers.get_api_v1_scorers.sync_detailed(client=client)
```

### Async Operations

All endpoints support async:

```python
import asyncio
from noveum_api_client import Client
from noveum_api_client.api.datasets import get_api_v1_datasets

async def main():
    client = Client(base_url="https://api.noveum.ai")
    
    # Async call
    response = await get_api_v1_datasets.asyncio_detailed(client=client)
    print(f"Status: {response.status_code}")

asyncio.run(main())
```

### Error Handling

```python
from noveum_api_client import NoveumClient
from noveum_api_client.errors import UnexpectedStatus

client = NoveumClient(api_key="nv_...")

try:
    results = client.get_results()
except UnexpectedStatus as e:
    print(f"API Error: {e.status_code}")
    print(f"Response: {e.content}")
```

### Context Manager

```python
from noveum_api_client import NoveumClient

with NoveumClient(api_key="nv_...") as client:
    datasets = client.list_datasets()
    # Client automatically closes when exiting context
```

## Configuration

### Custom Base URL

```python
client = NoveumClient(
    api_key="nv_...",
    base_url="https://custom.api.noveum.ai"
)
```

### API Key from Environment

```python
import os
from noveum_api_client import NoveumClient

api_key = os.getenv("NOVEUM_API_KEY")
client = NoveumClient(api_key=api_key)
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

## Best Practices

1. **Use environment variables for API keys**
   ```python
   api_key = os.getenv("NOVEUM_API_KEY")
   client = NoveumClient(api_key=api_key)
   ```

2. **Handle errors gracefully**
   ```python
   try:
       response = client.list_datasets()
   except Exception as e:
       print(f"Error: {e}")
   ```

3. **Use context managers for resource cleanup**
   ```python
   with NoveumClient(api_key="nv_...") as client:
       # Use client
       pass
   ```

4. **Paginate through large result sets**
   ```python
   offset = 0
   while True:
       response = client.list_datasets(offset=offset, limit=100)
       if not response['data']:
           break
       # Process response
       offset += 100
   ```

5. **Cache results when appropriate**
   ```python
   datasets = client.list_datasets()
   # Use datasets multiple times
   ```

## Troubleshooting

### ImportError: No module named 'noveum_api_client'

Install the SDK:
```bash
pip install -e .
```

### AttributeError: 'NoneType' object has no attribute 'value'

Ensure you're passing valid parameters. Check the API documentation for required fields.

### 401 Unauthorized

Check your API key:
```bash
export NOVEUM_API_KEY="nv_..."
```

### Connection Timeout

Check your network connection and base URL:
```python
client = NoveumClient(
    api_key="nv_...",
    base_url="https://api.noveum.ai"
)
```

## Examples

### Example 1: List All Datasets

```python
from noveum_api_client import NoveumClient

client = NoveumClient(api_key="nv_...")
response = client.list_datasets(limit=100)

for dataset in response['data']:
    print(f"Dataset: {dataset['name']} ({dataset['slug']})")
```

### Example 2: Get Dataset Items

```python
from noveum_api_client import NoveumClient

client = NoveumClient(api_key="nv_...")
items = client.get_dataset_items("my-dataset")

for item in items['data']:
    print(f"Item {item['id']}: {item['content']}")
```

### Example 3: Evaluate Results

```python
from noveum_api_client import NoveumClient

client = NoveumClient(api_key="nv_...")
results = client.get_results(dataset_slug="my-dataset")

for result in results['data']:
    print(f"Item {result['item_id']}: Score {result['score']}")
```

## Support

- **API Docs**: https://api.noveum.ai/docs
- **Issues**: Open on GitHub
- **Email**: support@noveum.ai
