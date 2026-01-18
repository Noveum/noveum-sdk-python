# Test Data Files

This directory contains sample datasets used for testing the Noveum SDK.

**Organization:** Noveum Inc

## Overview

Test data is available in two forms:
1. **Embedded in `conftest.py`** - Small datasets directly in code (recommended for most tests)
2. **JSON files** - Minimal datasets for file-based testing scenarios

## Files

### 1. `conversation_dataset.json`
**Purpose:** Standard conversation/Q&A dataset  
**Items:** 10 conversation examples  
**Size:** ~4 KB

**Structure:**
```json
{
  "item_id": "conv_001",
  "item_type": "conversational",
  "content": {
    "input": "Question or prompt",
    "output": "Response or completion",
    "agent_name": "assistant",
    "agent_role": "helpful_assistant",
    "system_prompt": "You are a helpful assistant."
  },
  "metadata": {
    "model": "gpt-4",
    "tokens": 15,
    "latency_ms": 850,
    "organization": "Noveum Inc"
  }
}
```

**Use Cases:**
- Testing dataset creation
- Testing dataset item operations
- LLM conversation tracking

---

### 2. `scorer_results_dataset_new.json`
**Purpose:** Evaluation/scorer results dataset  
**Items:** 10 evaluation records  
**Size:** ~5 KB

**Structure:**
```json
{
  "item_id": "eval_001",
  "item_type": "evaluation",
  "content": {
    "input": "Original input",
    "output": "Generated output",
    "expected_output": "Expected result",
    "score": 1.0,
    "passed": true
  },
  "metadata": {
    "scorer": "accuracy_checker",
    "evaluation_time": "2026-01-17T10:00:00Z",
    "model": "gpt-4"
  }
}
```

**Use Cases:**
- Testing evaluation workflows
- Testing scorer results tracking
- Quality assurance testing

---

## Usage in Tests

### Recommended: Use Embedded Fixtures (from conftest.py)

```python
def test_with_embedded_data(conversation_dataset, scorer_results_dataset):
    """Use embedded fixtures - no file I/O required."""
    # conversation_dataset contains 5 items
    # scorer_results_dataset contains 5 items
    
    for item in conversation_dataset:
        assert "item_id" in item
        assert "content" in item
```

### Optional: Load from Files

```python
def test_with_file_data(conversation_dataset_from_file, scorer_results_dataset_from_file):
    """Use file-based fixtures for larger datasets."""
    # Loads from JSON files in test_data/
    
    for item in conversation_dataset_from_file:
        assert "item_id" in item
```

---

## Data Characteristics

### Conversation Dataset
- **Models:** GPT-4, GPT-3.5-turbo, Claude-3-Sonnet, Claude-3-Opus
- **Token Range:** 12-55 tokens
- **Latency Range:** 450-1200ms
- **Topics:** Science, coding, translation, general knowledge

### Scorer Dataset
- **Scorers:** accuracy_checker, clarity_scorer, code_quality, comprehensiveness, translation_accuracy
- **Score Range:** 0.78 - 1.0
- **Pass Rate:** 100% (all items passed)
- **Evaluation Types:** Accuracy, clarity, code quality, practical advice

---

## File Sizes

| File | Items | Size |
|------|-------|------|
| `conversation_dataset.json` | 10 | ~4 KB |
| `scorer_results_dataset_new.json` | 10 | ~5 KB |
| **Total** | 20 | ~9 KB |

---

## Best Practices

1. ✅ **Use embedded fixtures** for most tests (faster, no file I/O)
2. ✅ Keep file datasets small (10-20 items max)
3. ✅ Use realistic but simple data
4. ✅ Include variety (different models, scorers, etc.)
5. ✅ Use clear, descriptive IDs
6. ✅ Include metadata for context

---

## Validation

To validate JSON format:
```bash
python -m json.tool test_data/conversation_dataset.json
python -m json.tool test_data/scorer_results_dataset_new.json
```

---

**Organization:** Noveum Inc  
**Last Updated:** January 17, 2026  
**Maintained By:** SDK Test Suite
