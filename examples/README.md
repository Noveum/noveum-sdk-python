# Noveum SDK Examples

This directory contains practical examples demonstrating how to use the Noveum SDK.

## Examples

### 1. Basic Evaluation (`basic_evaluation.py`)

Demonstrates the simplest use case: loading a dataset item, running an agent, and evaluating the output.

```bash
python examples/basic_evaluation.py
```

**What it shows:**
- Initializing the Noveum client
- Loading a dataset item
- Running an agent/model
- Evaluating output with scorers
- Displaying results

### 2. Regression Test (`regression_test.py`)

Shows how to use the SDK in a pytest test for regression testing.

```bash
pytest examples/regression_test.py -v
```

**What it shows:**
- Using pytest fixtures with Noveum client
- Loading multiple dataset items
- Running batch evaluations
- Aggregating results
- Asserting quality metrics

### 3. Async Evaluation (`async_evaluation.py`)

Demonstrates async/await usage for parallel evaluations.

```bash
python examples/async_evaluation.py
```

**What it shows:**
- Using `AsyncNoveumClient`
- Async iteration over datasets
- Parallel evaluation execution
- Async error handling

## Prerequisites

Before running the examples, ensure you have:

1. **Installed the SDK**:
   ```bash
   pip install noveum-sdk-python
   ```

2. **Set your API key**:
   ```bash
   export NOVEUM_API_KEY="your-api-key"
   ```

3. **Created test data** (for some examples):
   - Create a dataset with slug `test-dataset` or `regression-tests`
   - Add items to the dataset

## Running Examples

### From the project root:

```bash
# Run basic example
python examples/basic_evaluation.py

# Run regression test
pytest examples/regression_test.py -v

# Run async example
python examples/async_evaluation.py
```

### From the examples directory:

```bash
cd examples

# Run basic example
python basic_evaluation.py

# Run regression test
pytest regression_test.py -v

# Run async example
python async_evaluation.py
```

## Customizing Examples

Each example is designed to be easily customizable:

1. **Change the agent**: Replace the `my_agent()` function with your actual model
2. **Change the dataset**: Modify the dataset slug in the examples
3. **Change the scorers**: Add or remove scorers as needed
4. **Add more logic**: Extend the examples with your own functionality

## Common Patterns

### Pattern 1: Simple Evaluation

```python
from noveum import NoveumClient, ScorerConfig

client = NoveumClient()
item = client.datasets.get_item("dataset-slug", "item-id")
output = my_agent(item.input_text)
result = client.evals.score(item, output, [ScorerConfig("scorer_id")])
```

### Pattern 2: Batch Evaluation

```python
from noveum import EvalAggregator

results = []
for item in client.datasets.items("dataset-slug"):
    output = my_agent(item.input_text)
    result = client.evals.score(item, output, scorers)
    results.append(result)

aggregator = EvalAggregator(results)
aggregator.assert_passing_rate(80.0)
```

### Pattern 3: Async Evaluation

```python
import asyncio

async with AsyncNoveumClient() as client:
    tasks = [
        client.evals.score(item, output, scorers)
        for item, output in items_with_outputs
    ]
    results = await asyncio.gather(*tasks)
```

## Troubleshooting

### "Could not load dataset item"

This means the dataset or item doesn't exist. Create it first:
1. Go to noveum.ai
2. Create a dataset
3. Add items to the dataset
4. Update the example with the correct dataset slug and item ID

### "Rate limited"

The API is rate limiting your requests. The SDK will automatically retry with backoff.

### "Authentication failed"

Ensure your API key is set correctly:
```bash
echo $NOVEUM_API_KEY  # Should print your key
```

## Next Steps

After exploring these examples, check out:

- [README.md](../README.md) - Full SDK documentation
- [API Reference](https://api.noveum.ai/docs) - Complete API documentation
- [Contributing Guide](../CONTRIBUTING.md) - How to contribute

## Questions?

If you have questions or issues:

1. Check the [README.md](../README.md) for more information
2. Open an issue on GitHub
3. Contact support@noveum.ai
