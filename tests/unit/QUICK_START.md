# 🚀 Quick Start: Unit Tests

## Run All Tests

```bash
cd /Users/mramanindia/work/noveum-sdk-python/tests/unit
pytest -v
```

## Run Specific Category

```bash
# Datasets
pytest test_datasets_wrappers.py -v

# Traces  
pytest test_traces_wrappers.py -v

# Scorers
pytest test_scorers_wrappers.py -v

# Auth
pytest test_auth_wrappers.py -v
```

## Run by Marker

```bash
pytest -m datasets -v
pytest -m traces -v
pytest -m models -v
```

## Quick Summary

```bash
pytest -q
```

## With Coverage

```bash
pytest --cov=noveum_api_client --cov-report=html
```

---

## ✅ What's Included

- **11 test files**
- **200+ tests**
- **10 API categories** (matching integration test structure)
- **No API key needed**
- **< 5 second execution**

## 📁 Test Files

| File | Tests | Category |
|------|-------|----------|
| `test_datasets_wrappers.py` | 20+ | Datasets API |
| `test_traces_wrappers.py` | 30+ | Traces API |
| `test_scorers_wrappers.py` | 20+ | Scorers API |
| `test_scorer_results_wrappers.py` | 15+ | Scorer Results API |
| `test_auth_wrappers.py` | 25+ | Authentication API |
| `test_api_keys_wrappers.py` | 15+ | API Keys API |
| `test_telemetry_wrappers.py` | 25+ | Telemetry API |
| `test_webhooks_projects_other_wrappers.py` | 20+ | Other APIs |
| `test_client_wrapper.py` | 11 | High-level client |
| `test_api_wrappers.py` | 15 | Low-level wrappers |
| `test_models.py` | 19 | Data models |

---

## 🎯 Key Benefits

- ⚡ **Fast**: < 5 seconds
- 🔒 **Safe**: No real API calls
- 🎯 **Comprehensive**: All categories covered
- 🧪 **Mocked**: Simulated responses
- 🚀 **CI/CD Ready**: Perfect for pipelines

---

See `UNIT_TESTS_COMPLETE.md` for full documentation.

