# Test Data Files

This directory contains sample datasets used for testing the Noveum SDK.

## Files

### 1. `conversation_dataset.json`
**Purpose:** Standard conversation/Q&A dataset  
**Items:** 10 conversation examples  
**Structure:**
```json
{
  "id": "conv_001",
  "input": "Question or prompt",
  "output": "Response or completion",
  "metadata": {
    "model": "gpt-4",
    "tokens": 15,
    "cost": 0.00045,
    "latency_ms": 850
  }
}
```

**Use Cases:**
- Testing dataset creation
- Testing dataset item operations
- LLM conversation tracking
- Model performance analysis

---

### 2. `scorer_results_dataset_new.json`
**Purpose:** Evaluation/scorer results dataset  
**Items:** 10 evaluation records  
**Structure:**
```json
{
  "id": "eval_001",
  "item_id": "conv_001",
  "input": "Original input",
  "output": "Generated output",
  "expected_output": "Expected result",
  "score": 1.0,
  "passed": true,
  "scorer": "accuracy_checker",
  "metadata": {
    "evaluation_time": "2026-01-08T10:15:30Z",
    "model": "gpt-4"
  }
}
```

**Use Cases:**
- Testing evaluation workflows
- Testing scorer results tracking
- Quality assurance testing
- Model comparison

---

## Usage in Tests

### In `test_datasets.py`:

```python
# Load test data
conversation_items = load_test_data('test_data/conversation_dataset.json')
scorer_items = load_test_data('test_data/scorer_results_dataset_new.json')

# Create dataset
dataset = create_dataset("test_dataset")

# Add items
add_items(dataset, conversation_items)
add_items(dataset, scorer_items)

# Test operations
list_items(dataset)
get_item(dataset, item_id)
delete_item(dataset, item_id)
```

---

## Data Characteristics

### Conversation Dataset
- **Models:** GPT-4, GPT-3.5-turbo, Claude-3-Sonnet, Claude-3-Opus
- **Token Range:** 15-52 tokens
- **Cost Range:** $0.000036 - $0.00225
- **Latency Range:** 450-1200ms
- **Topics:** Science, coding, translation, general knowledge

### Scorer Dataset
- **Scorers:** accuracy_checker, clarity_scorer, code_quality, comprehensiveness, etc.
- **Score Range:** 0.85 - 1.0
- **Pass Rate:** 100% (all items passed)
- **Linked Items:** References conv_001 - conv_010
- **Evaluation Types:** Accuracy, clarity, code quality, practical advice

---

## Modifying Test Data

### To add more items:
1. Copy an existing item structure
2. Change the `id` field (must be unique)
3. Update the content fields
4. Save the file

### To use custom data:
1. Create a new JSON file in this directory
2. Follow the same structure
3. Update `test_datasets.py` to load your file

---

## File Sizes

- `conversation_dataset.json`: ~2.5 KB (10 items)
- `scorer_results_dataset_new.json`: ~3.8 KB (10 items)

**Total:** ~6.3 KB

---

## Cleanup

These test data files are NOT cleaned up automatically. They are static fixtures for testing.

The datasets and items CREATED from these files are cleaned up after tests complete.

---

## Best Practices

1. ✅ Keep items small (10-20 items per file)
2. ✅ Use realistic but simple data
3. ✅ Include variety (different models, scorers, etc.)
4. ✅ Use clear, descriptive IDs
5. ✅ Include metadata for context
6. ✅ Maintain valid JSON format

---

## Validation

To validate JSON format:
```bash
python -m json.tool test_data/conversation_dataset.json
python -m json.tool test_data/scorer_results_dataset_new.json
```

Expected output: Formatted JSON (no errors)

---

**Last Updated:** January 8, 2026  
**Maintained By:** SDK Test Suite

