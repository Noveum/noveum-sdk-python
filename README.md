# Noveum Trace Python SDK

[![PyPI version](https://badge.fury.io/py/noveum-sdk-python.svg)](https://badge.fury.io/py/noveum-sdk-python)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**The official Python SDK for the Noveum.ai AI/ML evaluation platform.**

---

The Noveum SDK provides a powerful and developer-friendly Python interface for interacting with the Noveum API. It is designed for seamless integration into your CI/CD pipeline, enabling real-time evaluation of AI/ML models, robust dataset management, and comprehensive performance tracing.

This SDK is built with a focus on modern Python practices, including full `async` support, Pydantic data validation, and a clean, intuitive API.

## ✨ Key Features

- **Real-Time Evaluation**: Score agent and model outputs instantly during tests, not after.
- **CI/CD Optimized**: Built from the ground up for regression testing and test automation.
- **Sync + Async Support**: Use `NoveumClient` for synchronous code or `AsyncNoveumClient` for modern async applications.
- **Simple & Secure Auth**: API key authentication only. No complex login flows.
- **Transparent Pagination**: Iterate through large datasets effortlessly without managing `limit` or `offset`.
- **Automatic Retries**: Built-in exponential backoff for handling transient network errors.
- **Rich Data Models**: Pydantic v2 models for all API objects, providing type safety and autocompletion.
- **Granular Error Handling**: A comprehensive exception hierarchy for robust error management.
- **Helper Utilities**: Fluent builders and aggregators to simplify common tasks.

## 🚀 Quick Start

Get up and running with the Noveum SDK in minutes.

### 1. Installation

```bash
# Install from PyPI
pip install noveum-sdk-python
```

### 2. Authentication

Set your Noveum API key as an environment variable. You can find your key at [noveum.ai/settings/api-keys](https://noveum.ai/settings/api-keys).

```bash
export NOVEUM_API_KEY="nv_..."
```

The client will automatically pick it up. Alternatively, you can pass it directly:

```python
from noveum import NoveumClient

client = NoveumClient(api_key="nv_...")
```

### 3. Your First Evaluation

Here’s a complete example of how to evaluate a model's output against a dataset item.

```python
from noveum import NoveumClient, ScorerConfig

# 1. Initialize the client
client = NoveumClient()

# 2. Define a dummy agent to test
def my_agent(prompt: str) -> str:
    if "hello" in prompt.lower():
        return "Hello there! How can I help you today?"
    return "I am not sure how to respond to that."

# 3. Load a dataset item
# (Assumes a dataset with slug 'chatbot-greetings' exists)
try:
    item = client.datasets.get_item("chatbot-greetings", "greeting-1")
except Exception as e:
    print(f"Could not load dataset item. Please create it first. Error: {e}")
    exit()

# 4. Run your agent with the item's input
agent_output = my_agent(item.input_text)

# 5. Evaluate the output in real-time
result = client.evals.score(
    dataset_item=item,
    agent_output=agent_output,
    scorers=[ScorerConfig(scorer_id="factuality_scorer")]
)

# 6. Print the results
print(f"Item ID: {result.item_id}")
print(f"Agent Output: {result.agent_output}")
print(f"Overall Score: {result.overall_score}/10")
print(f"Passed: {result.overall_passed}")

for score in result.scores:
    print(f"  - Scorer: {score.scorer_name}")
    print(f"    Score: {score.score}")
    print(f"    Reasoning: {score.reasoning}")
```

## 📚 Usage Examples

### Datasets

```python
# List all datasets
for dataset in client.datasets.list():
    print(f"- {dataset.name} ({dataset.slug}) has {dataset.item_count} items")

# Get a specific dataset
dataset = client.datasets.get("regression-tests")

# Iterate through all items in a dataset (with automatic pagination)
for item in client.datasets.items("regression-tests"):
    print(f"  - Item ID: {item.item_id}, Input: {item.input_text[:30]}...")
```

### Evals (for CI/CD)

```python
from noveum import EvalAggregator

# Load test items
items = list(client.datasets.items("regression-tests"))
scorers = [ScorerConfig(scorer_id="factuality_scorer")]

# Run evaluations
results = []
for item in items:
    output = my_agent.run(item.input_text)
    result = client.evals.score(item, output, scorers)
    results.append(result)

# Aggregate results and assert
aggregator = EvalAggregator(results)

print(f"Passing Rate: {aggregator.passing_rate:.1f}%")
print(f"Average Score: {aggregator.average_score:.1f}")

# Assert a minimum passing rate for your CI test
aggregator.assert_passing_rate(80.0) # Fails if < 80%
```

### Async Usage

The SDK provides an async client for modern Python applications.

```python
import asyncio
from noveum import AsyncNoveumClient

async def main():
    async with AsyncNoveumClient() as client:
        # List datasets asynchronously
        async for dataset in client.datasets.list():
            print(dataset.name)
        
        # Run evaluations in parallel
        tasks = []
        async for item in client.datasets.items("regression-tests"):
            output = await my_async_agent.run(item.input_text)
            task = client.evals.score(item, output, scorers)
            tasks.append(task)
        
        results = await asyncio.gather(*tasks)
        print(f"Evaluated {len(results)} items.")

asyncio.run(main())
```

### Error Handling

Catch specific exceptions to handle API errors gracefully.

```python
from noveum.exceptions import NoveumNotFoundError, NoveumRateLimitError

try:
    item = client.datasets.get_item("non-existent-dataset", "item-1")
except NoveumNotFoundError:
    print("Dataset or item not found!")
except NoveumRateLimitError as e:
    print(f"Rate limited. Retry after {e.retry_after} seconds.")
```

## 🔧 Configuration

You can configure the client via environment variables or directly in code.

| Environment Variable | Code Parameter | Default | Description |
| :--- | :--- | :--- | :--- |
| `NOVEUM_API_KEY` | `api_key` | `None` | Your Noveum API key. **(Required)** |
| `NOVEUM_BASE_URL` | `base_url` | `https://api.noveum.ai/api/v1` | The API base URL. |
| `NOVEUM_TIMEOUT` | `timeout` | `30.0` | Request timeout in seconds. |
| `NOVEUM_MAX_RETRIES` | `max_retries` | `3` | Max retries on transient errors. |

## 🤝 Contributing

Contributions are welcome! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to submit pull requests.

## 📜 License

This SDK is licensed under the [MIT License](LICENSE).
