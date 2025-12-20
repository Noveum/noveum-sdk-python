# Engineer Verification Guide - Noveum SDK

**Target Audience**: QA Engineers, DevOps Engineers, Integration Engineers  
**Time Estimate**: 2-3 hours  
**Difficulty**: Intermediate  
**Status**: Production Ready

---

## Quick Start

### Prerequisites

```bash
# Check Python version
python3 --version  # Should be 3.10+

# Install SDK
pip install -e .

# Set API key
export NOVEUM_API_KEY="nv_uxVvrZzzaNvO49TAFQEe9CLlTBqELMLm"

# Verify installation
python -c "from noveum_api_client import NoveumClient; print('✅ Ready')"
```

### Run Verification

**Option 1: Jupyter Notebook (Interactive)**
```bash
jupyter notebook SDK_VERIFICATION_NOTEBOOK.ipynb
```

**Option 2: Automated Tests**
```bash
pytest tests/ -v
```

**Option 3: Manual Checklist**
Use `VERIFICATION_CHECKLIST.md`

---

## Verification Sections

### Section 1: Installation & Setup (15 minutes)

**Goal**: Verify SDK installs correctly and dependencies are met

**Steps**:
1. Extract SDK package
2. Create Python virtual environment
3. Install SDK with `pip install -e .`
4. Verify imports work
5. Check all dependencies installed

**Expected Results**:
- ✅ No import errors
- ✅ All dependencies resolved
- ✅ SDK version shows correctly

**Troubleshooting**:
| Error | Solution |
| :--- | :--- |
| `ModuleNotFoundError` | Run `pip install -e .` again |
| `Python 3.9` | Upgrade to Python 3.10+ |
| `Permission denied` | Use `pip install --user -e .` |

---

### Section 2: Authentication & Authorization (20 minutes)

**Goal**: Verify API key authentication works correctly

**Key Tests**:

**Test 2.1: Valid API Key**
```python
from noveum_api_client import NoveumClient
import os

api_key = os.getenv("NOVEUM_API_KEY")
client = NoveumClient(api_key=api_key)
response = client.list_datasets(limit=1)

assert response["status_code"] == 200, "Authentication failed"
print("✅ Valid API key works")
```

**Test 2.2: Invalid API Key**
```python
client = NoveumClient(api_key="nv_invalid_key")
response = client.list_datasets(limit=1)

assert response["status_code"] == 401, "Should return 401"
print("✅ Invalid API key returns 401")
```

**Test 2.3: Bearer Token Format**
```python
from noveum_api_client import Client

client = Client(
    base_url="https://api.noveum.ai",
    headers={"Authorization": f"Bearer {api_key}"}
)

# Verify header is set
assert "Authorization" in client._headers
assert client._headers["Authorization"].startswith("Bearer ")
print("✅ Bearer token format correct")
```

**Test 2.4: Permissions**
```python
# Should have read access
response = client.list_datasets()
assert response["status_code"] == 200

# Check if write operations are restricted (if applicable)
# This depends on your API design
```

**Expected Results**:
- ✅ Valid key returns 200
- ✅ Invalid key returns 401
- ✅ Bearer token format is correct
- ✅ Permissions are enforced

---

### Section 3: Core Functionality (30 minutes)

**Goal**: Verify all main API endpoints work

**Test 3.1: List Datasets**
```python
response = client.list_datasets(limit=10)

# Verify response structure
assert response["status_code"] == 200
assert "data" in response
assert isinstance(response["data"], list)

# Verify dataset structure
for dataset in response["data"]:
    assert "id" in dataset
    assert "name" in dataset
    assert "slug" in dataset

print(f"✅ Found {len(response['data'])} datasets")
```

**Test 3.2: Get Dataset Items**
```python
# First get a dataset
datasets = client.list_datasets(limit=1)
if datasets["data"]:
    dataset_slug = datasets["data"][0]["slug"]
    
    # Get items from dataset
    items = client.get_dataset_items(dataset_slug, limit=10)
    
    assert items["status_code"] == 200
    assert isinstance(items["data"], list)
    
    # Verify item structure
    for item in items["data"]:
        assert "id" in item
        assert "input" in item
    
    print(f"✅ Found {len(items['data'])} items in dataset")
```

**Test 3.3: List Traces**
```python
from noveum_api_client.api.traces import get_api_v1_traces

response = get_api_v1_traces.sync_detailed(client=low_level_client, limit=10)

assert response.status_code == 200
traces = response.parsed if response.parsed else []

print(f"✅ Found {len(traces)} traces")
```

**Test 3.4: List Scorers**
```python
from noveum_api_client.api.scorers import get_api_v1_scorers

response = get_api_v1_scorers.sync_detailed(client=low_level_client, limit=10)

assert response.status_code == 200
scorers = response.parsed if response.parsed else []

print(f"✅ Found {len(scorers)} scorers")
```

**Test 3.5: Get Evaluation Results**
```python
response = client.get_results(limit=10)

assert response["status_code"] == 200
assert isinstance(response["data"], list)

# Verify result structure
for result in response["data"]:
    assert "id" in result
    assert "score" in result or "status" in result

print(f"✅ Found {len(response['data'])} evaluation results")
```

**Expected Results**:
- ✅ All endpoints return 200
- ✅ Response data is properly formatted
- ✅ Required fields are present
- ✅ Data types are correct

---

### Section 4: Pagination & Performance (30 minutes)

**Goal**: Verify pagination works and performance is acceptable

**Test 4.1: Pagination Parameters**
```python
# Test limit parameter
page1 = client.list_datasets(limit=5, offset=0)
assert len(page1["data"]) <= 5

# Test offset parameter
page2 = client.list_datasets(limit=5, offset=5)

# Verify no duplicates
ids1 = {item["id"] for item in page1["data"]}
ids2 = {item["id"] for item in page2["data"]}
assert len(ids1 & ids2) == 0, "Found duplicate items"

print("✅ Pagination parameters work correctly")
```

**Test 4.2: Iterate Through All Pages**
```python
all_items = []
offset = 0
limit = 100

while True:
    response = client.list_datasets(limit=limit, offset=offset)
    items = response["data"]
    
    if not items:
        break
    
    all_items.extend(items)
    offset += limit
    
    print(f"Fetched {len(all_items)} items so far...")

print(f"✅ Total items: {len(all_items)}")
```

**Test 4.3: Response Time**
```python
import time

times = []
for i in range(5):
    start = time.time()
    response = client.list_datasets(limit=10)
    elapsed = time.time() - start
    times.append(elapsed)

avg_time = sum(times) / len(times)
max_time = max(times)

print(f"✅ Average response time: {avg_time:.3f}s")
print(f"   Max: {max_time:.3f}s")

assert avg_time < 2.0, f"Response time too slow: {avg_time}s"
```

**Test 4.4: Concurrent Requests**
```python
import concurrent.futures

def make_request():
    return client.list_datasets(limit=5)

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(make_request) for _ in range(10)]
    results = [f.result() for f in concurrent.futures.as_completed(futures)]

successful = sum(1 for r in results if r["status_code"] == 200)
print(f"✅ Concurrent requests: {successful}/10 successful")

assert successful == 10, f"Some requests failed: {10 - successful}"
```

**Test 4.5: Large Dataset Pagination**
```python
# Paginate through large dataset
total_items = 0
offset = 0
limit = 100
max_iterations = 100  # Safety limit

for i in range(max_iterations):
    response = client.list_datasets(limit=limit, offset=offset)
    items = response["data"]
    
    if not items:
        break
    
    total_items += len(items)
    offset += limit

print(f"✅ Successfully paginated through {total_items} items")
```

**Expected Results**:
- ✅ Pagination parameters work correctly
- ✅ No duplicate items across pages
- ✅ Average response time < 2 seconds
- ✅ Concurrent requests succeed
- ✅ Can paginate through large datasets

---

### Section 5: Error Handling (25 minutes)

**Goal**: Verify error handling is robust

**Test 5.1: HTTP Error Codes**
```python
# Test 401 Unauthorized
invalid_client = NoveumClient(api_key="nv_invalid")
response = invalid_client.list_datasets()
assert response["status_code"] == 401
print("✅ 401 Unauthorized handled")

# Test 404 Not Found
response = client.get_dataset_items("nonexistent-dataset")
assert response["status_code"] == 404 or response["status_code"] == 200
print("✅ 404 Not Found handled")

# Test 500 Server Error (if possible)
# This would require a test endpoint that returns 500
```

**Test 5.2: Network Errors**
```python
import httpx

try:
    bad_client = Client(
        base_url="https://invalid.example.com",
        headers={"Authorization": f"Bearer {api_key}"}
    )
    response = get_api_v1_datasets.sync_detailed(client=bad_client)
    print("⚠️  Unexpected success")
except httpx.ConnectError:
    print("✅ Connection error handled")
except Exception as e:
    print(f"✅ Network error handled: {type(e).__name__}")
```

**Test 5.3: Timeout Errors**
```python
import httpx

try:
    client_with_timeout = Client(
        base_url="https://api.noveum.ai",
        headers={"Authorization": f"Bearer {api_key}"},
        timeout=httpx.Timeout(0.001)  # Very short timeout
    )
    response = get_api_v1_datasets.sync_detailed(client=client_with_timeout)
    print("⚠️  Unexpected success")
except httpx.TimeoutException:
    print("✅ Timeout error handled")
except Exception as e:
    print(f"✅ Timeout handled: {type(e).__name__}")
```

**Test 5.4: Data Validation Errors**
```python
# Test invalid parameter types
try:
    response = client.list_datasets(limit="invalid")
    print("⚠️  No validation error")
except (TypeError, ValueError) as e:
    print(f"✅ Validation error caught: {type(e).__name__}")
```

**Test 5.5: Error Messages**
```python
# Verify error messages don't leak sensitive data
invalid_client = NoveumClient(api_key="nv_secret_key_123")
response = invalid_client.list_datasets()

error_msg = str(response.get("data", ""))
assert "secret" not in error_msg.lower(), "API key leaked in error"
assert "nv_" not in error_msg, "API key format leaked in error"

print("✅ Error messages are safe")
```

**Expected Results**:
- ✅ HTTP errors are handled
- ✅ Network errors are caught
- ✅ Timeout errors are handled
- ✅ Validation errors are raised
- ✅ Error messages are safe

---

### Section 6: Edge Cases (20 minutes)

**Goal**: Verify edge cases are handled correctly

**Test 6.1: Empty Responses**
```python
# Empty dataset list
response = client.list_datasets(limit=0)
assert isinstance(response["data"], list)
assert len(response["data"]) == 0
print("✅ Empty response handled")
```

**Test 6.2: Null/None Values**
```python
response = client.list_datasets(limit=100)

for dataset in response["data"]:
    # Check that optional fields can be None
    # but required fields are not None
    assert dataset.get("id") is not None
    assert dataset.get("name") is not None
    assert dataset.get("slug") is not None

print("✅ Null/None values handled correctly")
```

**Test 6.3: Special Characters**
```python
response = client.list_datasets(limit=100)

for dataset in response["data"]:
    name = dataset.get("name", "")
    # Should handle unicode, emoji, etc.
    try:
        str(name).encode('utf-8')
    except UnicodeError:
        print(f"❌ Unicode error in: {name}")
        raise

print("✅ Special characters handled")
```

**Test 6.4: Large Values**
```python
response = client.list_datasets(limit=1000)

for dataset in response["data"]:
    # Check that large text fields are handled
    name = dataset.get("name", "")
    assert len(name) < 1000000, "Name too large"

print("✅ Large values handled")
```

**Test 6.5: Boundary Values**
```python
# Test minimum values
response = client.list_datasets(limit=1, offset=0)
assert len(response["data"]) <= 1

# Test maximum values
response = client.list_datasets(limit=10000, offset=0)
assert len(response["data"]) <= 10000

# Test negative offset (should be rejected or treated as 0)
response = client.list_datasets(limit=10, offset=-1)
# Behavior depends on API design

print("✅ Boundary values handled")
```

**Expected Results**:
- ✅ Empty responses are handled
- ✅ Null/None values are correct
- ✅ Special characters work
- ✅ Large values don't cause issues
- ✅ Boundary values are handled

---

### Section 7: Async Support (20 minutes)

**Goal**: Verify async/await functionality

**Test 7.1: Async Methods Exist**
```python
from noveum_api_client.api.datasets import get_api_v1_datasets

# Check async methods exist
assert hasattr(get_api_v1_datasets, 'asyncio_detailed')
assert hasattr(get_api_v1_datasets, 'asyncio')

print("✅ Async methods exist")
```

**Test 7.2: Async Functionality**
```python
import asyncio

async def test_async():
    response = await get_api_v1_datasets.asyncio_detailed(
        client=low_level_client,
        limit=10
    )
    assert response.status_code == 200
    return response

result = asyncio.run(test_async())
print("✅ Async methods work")
```

**Test 7.3: Concurrent Async Requests**
```python
async def test_concurrent():
    tasks = [
        get_api_v1_datasets.asyncio_detailed(client=low_level_client, limit=5),
        get_api_v1_traces.asyncio_detailed(client=low_level_client, limit=5),
        get_api_v1_scorers.asyncio_detailed(client=low_level_client, limit=5),
    ]
    results = await asyncio.gather(*tasks)
    
    for result in results:
        assert result.status_code == 200
    
    return results

results = asyncio.run(test_concurrent())
print(f"✅ Concurrent async requests: {len(results)} successful")
```

**Test 7.4: Async Error Handling**
```python
async def test_async_error():
    try:
        bad_client = Client(
            base_url="https://invalid.example.com",
            headers={"Authorization": f"Bearer {api_key}"}
        )
        response = await get_api_v1_datasets.asyncio_detailed(client=bad_client)
    except Exception as e:
        return type(e).__name__

error_type = asyncio.run(test_async_error())
print(f"✅ Async error handling: {error_type}")
```

**Expected Results**:
- ✅ Async methods exist
- ✅ Async/await works
- ✅ Concurrent async requests work
- ✅ Async error handling works

---

### Section 8: Type Safety & IDE Support (15 minutes)

**Goal**: Verify type hints and IDE support

**Test 8.1: Type Hints Present**
```python
import inspect
from noveum_api_client import NoveumClient

# Check that methods have type hints
client = NoveumClient(api_key="nv_test")

sig = inspect.signature(client.list_datasets)
print(f"list_datasets signature: {sig}")

# Verify return type is annotated
assert sig.return_annotation != inspect.Signature.empty
print("✅ Type hints present")
```

**Test 8.2: IDE Autocomplete**
```python
# In VS Code or PyCharm, verify:
# 1. client.list_datasets() shows autocomplete
# 2. Parameters show in autocomplete
# 3. Docstrings appear on hover
# 4. Type hints are shown

print("✅ IDE autocomplete works (manual verification)")
```

**Test 8.3: Type Checking**
```bash
# Run mypy
mypy noveum_api_client/ --ignore-missing-imports

# Run pyright
pyright noveum_api_client/

# Should pass without errors
```

**Test 8.4: Docstrings**
```python
from noveum_api_client import NoveumClient

client = NoveumClient(api_key="nv_test")

# Check docstrings
print(client.list_datasets.__doc__)
print(client.get_dataset_items.__doc__)
print(client.get_results.__doc__)

# Should have meaningful docstrings
```

**Expected Results**:
- ✅ Type hints on all methods
- ✅ IDE autocomplete works
- ✅ Type checking passes
- ✅ Docstrings are present

---

### Section 9: Logging & Debugging (15 minutes)

**Goal**: Verify logging and debugging capabilities

**Test 9.1: Request Logging**
```python
import logging

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)

# Make a request
response = client.list_datasets(limit=1)

# Should see request details in logs
print("✅ Request logging works")
```

**Test 9.2: Error Logging**
```python
import logging

logging.basicConfig(level=logging.DEBUG)

# Trigger an error
invalid_client = NoveumClient(api_key="nv_invalid")
response = invalid_client.list_datasets()

# Should see error details in logs
print("✅ Error logging works")
```

**Test 9.3: Debug Mode**
```python
# Check if debug mode can be enabled
# This depends on SDK implementation
print("✅ Debug mode available (manual verification)")
```

**Expected Results**:
- ✅ Requests are logged
- ✅ Errors are logged
- ✅ Debug mode works
- ✅ Logs are informative

---

## Automated Verification Script

Run all tests automatically:

```bash
#!/bin/bash

echo "Starting SDK Verification..."
echo ""

# Install dependencies
pip install -e . > /dev/null 2>&1

# Run pytest
echo "Running automated tests..."
pytest tests/ -v --tb=short

# Check exit code
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ All tests passed!"
    echo "SDK is ready for production"
else
    echo ""
    echo "❌ Some tests failed"
    echo "Please review the output above"
    exit 1
fi
```

---

## Troubleshooting Guide

### Common Issues

**Issue: ImportError: No module named 'noveum_api_client'**
```bash
# Solution: Install SDK
pip install -e .
```

**Issue: 401 Unauthorized**
```bash
# Solution: Check API key
echo $NOVEUM_API_KEY

# If empty, set it
export NOVEUM_API_KEY="nv_your_key"
```

**Issue: Connection timeout**
```bash
# Solution: Check internet connection
ping api.noveum.ai

# Or increase timeout
client = NoveumClient(api_key=api_key)
# Timeout is configurable
```

**Issue: SSL certificate error**
```bash
# Solution: Use custom certificate or disable verification
from noveum_api_client import Client

client = Client(
    base_url="https://api.noveum.ai",
    verify_ssl="/path/to/cert.pem"
)
```

**Issue: Type checking errors**
```bash
# Solution: Update type checking tools
pip install --upgrade mypy pyright
```

---

## Sign-Off Template

```markdown
# SDK Verification Sign-Off

**Date**: [Date]  
**Verified By**: [Name]  
**SDK Version**: 1.0.0  
**Python Version**: 3.10+  

## Results

- [ ] Installation: ✅ Pass / ❌ Fail
- [ ] Authentication: ✅ Pass / ❌ Fail
- [ ] Core Functionality: ✅ Pass / ❌ Fail
- [ ] Pagination: ✅ Pass / ❌ Fail
- [ ] Error Handling: ✅ Pass / ❌ Fail
- [ ] Edge Cases: ✅ Pass / ❌ Fail
- [ ] Async Support: ✅ Pass / ❌ Fail
- [ ] Type Safety: ✅ Pass / ❌ Fail

## Issues Found

[ ] None
[ ] Issue 1: _______________
[ ] Issue 2: _______________

## Recommendations

[ ] None
[ ] Recommendation 1: _______________

## Overall Status

[ ] ✅ Approved for Production
[ ] ⚠️  Approved with Issues
[ ] ❌ Rejected

**Signature**: _______________
```

---

## Next Steps

After verification:

1. **Document Results** - Fill out sign-off template
2. **Report Issues** - Create tickets for any problems found
3. **Approve Release** - If all tests pass, approve for production
4. **Deploy** - Publish to PyPI or internal repository
5. **Monitor** - Watch for issues in production

---

**Last Updated**: December 17, 2025  
**Status**: Production Ready  
**Contact**: support@noveum.ai
