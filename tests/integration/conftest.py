"""
Pytest Configuration and Shared Fixtures for Integration Tests

This module provides:
- Session-scoped and test-scoped fixtures
- Environment validation with helpful error messages
- Custom pytest markers for test organization
- Shared test data fixtures
- Cleanup utilities
"""

import json
import os
import sys
import time
import uuid
from datetime import datetime
from typing import Any, Generator

import pytest

# Add parent directories to path
sys.path.insert(0, os.path.abspath("../.."))
sys.path.insert(0, os.path.abspath("../../tests"))

from noveum_api_client import Client, NoveumClient

from constants import (
    SKIP_NO_API_KEY,
    SKIP_TEST_DATA_FILE_NOT_FOUND,
    FAIL_INVALID_RESPONSE_FORMAT,
    API_CALL_FAILED_HEADER,
    API_CALL_FAILED_EXPECTED,
    API_CALL_FAILED_GOT,
    API_CALL_FAILED_RESPONSE,
    API_CALL_FAILED_CONTENT,
    API_CALL_FAILED_HINT,
    STATUS_CODE_HINTS,
)


# =============================================================================
# Constants
# =============================================================================

DEFAULT_BASE_URL = "https://api.noveum.ai"
DEFAULT_PROJECT = "SDK_Integration_Test"
DEFAULT_ENVIRONMENT = "test"
DEFAULT_ORG_SLUG = "noveum-inc"
DEFAULT_ORG_NAME = "Noveum Inc"
WAIT_FOR_INGESTION_SECONDS = 3


# =============================================================================
# Pytest Configuration
# =============================================================================


def pytest_configure(config: pytest.Config) -> None:
    """Configure pytest with custom markers and validate environment."""
    # Register custom markers
    config.addinivalue_line("markers", "integration: mark test as integration test")
    config.addinivalue_line("markers", "slow: mark test as slow running")
    config.addinivalue_line("markers", "serial: mark test as requiring sequential execution")
    config.addinivalue_line("markers", "traces: mark test as traces-related")
    config.addinivalue_line("markers", "datasets: mark test as datasets-related")
    config.addinivalue_line("markers", "scorers: mark test as scorers-related")
    config.addinivalue_line("markers", "etl: mark test as ETL jobs-related")
    config.addinivalue_line("markers", "projects: mark test as projects-related")
    config.addinivalue_line("markers", "audio: mark test as audio-related")
    config.addinivalue_line("markers", "langchain: mark test as LangChain integration test")
    config.addinivalue_line("markers", "langgraph: mark test as LangGraph integration test")


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    """Modify test collection to add markers automatically."""
    for item in items:
        # Mark all tests in integration directory
        if "integration" in str(item.fspath):
            item.add_marker(pytest.mark.integration)

        # Add domain-specific markers based on test file names
        if "traces" in str(item.fspath).lower():
            item.add_marker(pytest.mark.traces)
        elif "datasets" in str(item.fspath).lower():
            item.add_marker(pytest.mark.datasets)
        elif "scorers" in str(item.fspath).lower():
            item.add_marker(pytest.mark.scorers)
        elif "etl" in str(item.fspath).lower():
            item.add_marker(pytest.mark.etl)
        elif "projects" in str(item.fspath).lower():
            item.add_marker(pytest.mark.projects)
        elif "audio" in str(item.fspath).lower():
            item.add_marker(pytest.mark.audio)


def pytest_report_header(config: pytest.Config) -> list[str]:
    """Add custom header information to pytest report."""
    api_key = os.getenv("NOVEUM_API_KEY")
    api_key_status = "✓ Set" if api_key else "✗ Not Set"
    org_slug = os.getenv("NOVEUM_ORG_SLUG", DEFAULT_ORG_SLUG)
    
    return [
        "",
        "=" * 70,
        f"{DEFAULT_ORG_NAME} - SDK Integration Tests",
        "=" * 70,
        f"  API Key: {api_key_status}",
        f"  Base URL: {os.getenv('NOVEUM_BASE_URL', DEFAULT_BASE_URL)}",
        f"  Organization: {DEFAULT_ORG_NAME} ({org_slug})",
        f"  Project: {os.getenv('NOVEUM_PROJECT', DEFAULT_PROJECT)}",
        f"  Environment: {os.getenv('NOVEUM_ENVIRONMENT', DEFAULT_ENVIRONMENT)}",
        "=" * 70,
        "",
    ]


def pytest_terminal_summary(terminalreporter: Any, exitstatus: int, config: pytest.Config) -> None:
    """Add custom summary at the end of test run."""
    terminalreporter.write_sep("=", "Integration Test Summary")

    passed = len(terminalreporter.stats.get("passed", []))
    failed = len(terminalreporter.stats.get("failed", []))
    skipped = len(terminalreporter.stats.get("skipped", []))
    total = passed + failed + skipped

    if total > 0:
        success_rate = (passed / total) * 100

        terminalreporter.write_line("\n📊 Results:")
        terminalreporter.write_line(f"   ✅ Passed:  {passed}/{total}")
        terminalreporter.write_line(f"   ❌ Failed:  {failed}/{total}")
        terminalreporter.write_line(f"   ⏭️  Skipped: {skipped}/{total}")
        terminalreporter.write_line(f"   📈 Success Rate: {success_rate:.1f}%")

        if failed > 0:
            terminalreporter.write_line("\n💡 Tips:")
            terminalreporter.write_line("   - Run with -v for verbose output")
            terminalreporter.write_line("   - Run with -s to see print statements")
            terminalreporter.write_line("   - Run with --tb=short for shorter tracebacks")

    terminalreporter.write_line("")


# =============================================================================
# Session-Scoped Fixtures (Run Once Per Test Session)
# =============================================================================


@pytest.fixture(scope="session")
def api_key() -> str:
    """Get API key from environment, skip all tests if not set."""
    key = os.getenv("NOVEUM_API_KEY")
    if not key:
        pytest.skip(SKIP_NO_API_KEY)
    return key


@pytest.fixture(scope="session")
def api_config(api_key: str) -> dict[str, str]:
    """Provide API configuration for all tests."""
    return {
        "api_key": api_key,
        "base_url": os.getenv("NOVEUM_BASE_URL", DEFAULT_BASE_URL),
        "project": os.getenv("NOVEUM_PROJECT", DEFAULT_PROJECT),
        "environment": os.getenv("NOVEUM_ENVIRONMENT", DEFAULT_ENVIRONMENT),
        "org_slug": os.getenv("NOVEUM_ORG_SLUG", DEFAULT_ORG_SLUG),
        "org_name": DEFAULT_ORG_NAME,
    }


@pytest.fixture(scope="session")
def session_client(api_config: dict[str, str]) -> Generator[Client, None, None]:
    """Provide a session-scoped low-level API client."""
    client = Client(
        base_url=api_config["base_url"],
        headers={"Authorization": f"Bearer {api_config['api_key']}"},
        timeout=60.0,
    )
    yield client


@pytest.fixture(scope="session")
def session_noveum_client(api_config: dict[str, str]) -> Generator[NoveumClient, None, None]:
    """Provide a session-scoped high-level Noveum client."""
    client = NoveumClient(
        api_key=api_config["api_key"],
        base_url=api_config["base_url"],
    )
    yield client
    client.close()


# =============================================================================
# Test-Scoped Fixtures (Run Per Test)
# =============================================================================


@pytest.fixture
def noveum_client(api_config: dict[str, str]) -> Generator[NoveumClient, None, None]:
    """Provide test-scoped high-level Noveum client."""
    client = NoveumClient(
        api_key=api_config["api_key"],
        base_url=api_config["base_url"],
    )
    yield client
    client.close()


@pytest.fixture
def low_level_client(api_config: dict[str, str]) -> Client:
    """Provide test-scoped low-level API client."""
    return Client(
        base_url=api_config["base_url"],
        headers={"Authorization": f"Bearer {api_config['api_key']}"},
        timeout=60.0,
    )


@pytest.fixture
def test_data_dir() -> str:
    """Provide path to test data directory."""
    return os.path.join(os.path.dirname(__file__), "test_data")


# =============================================================================
# Test Data Generation Fixtures
# =============================================================================


@pytest.fixture
def unique_id() -> str:
    """Generate a unique identifier for test resources."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    unique = str(uuid.uuid4())[:8]
    return f"{timestamp}_{unique}"


@pytest.fixture
def unique_slug(unique_id: str) -> str:
    """Generate a unique slug for datasets/resources."""
    return f"sdk-test-{unique_id}".lower().replace("_", "-")


@pytest.fixture
def unique_project_id(unique_id: str) -> str:
    """Generate a unique project ID."""
    return f"sdk-test-project-{unique_id}".lower().replace("_", "-")


@pytest.fixture
def sample_trace_data(api_config: dict[str, str]) -> dict[str, Any]:
    """Generate sample trace data for testing."""
    trace_id = str(uuid.uuid4())
    span_id = str(uuid.uuid4())[:16]
    now = datetime.now()
    
    return {
        "trace_id": trace_id,
        "name": "test_trace_operation",
        "project": api_config["project"],
        "environment": api_config["environment"],
        "start_time": int((now.timestamp() - 1) * 1_000_000),  # microseconds
        "end_time": int(now.timestamp() * 1_000_000),
        "status": {"code": "OK"},
        "attributes": {
            "llm.model": "gpt-4",
            "llm.operation": "test",
            "llm.prompt": "What is 2+2?",
            "llm.response": "4",
            "llm.prompt_tokens": 10,
            "llm.completion_tokens": 5,
            "llm.total_tokens": 15,
            "service.name": "sdk-integration-test",
        },
        "spans": [
            {
                "span_id": span_id,
                "trace_id": trace_id,
                "name": "llm_call",
                "kind": "LLM",
                "start_time": int((now.timestamp() - 0.5) * 1_000_000),
                "end_time": int(now.timestamp() * 1_000_000),
                "status": {"code": "OK"},
                "attributes": {
                    "llm.model": "gpt-4",
                    "input": "What is 2+2?",
                    "output": "4",
                },
            }
        ],
        "metadata": {
            "sdk_version": "1.0.0",
            "test_run": True,
        },
    }


@pytest.fixture
def sample_traces_batch(api_config: dict[str, str]) -> list[dict[str, Any]]:
    """Generate a batch of sample traces for testing."""
    traces = []
    models = ["gpt-4", "gpt-3.5-turbo", "claude-3-opus", "claude-3-sonnet"]
    operations = ["question_answering", "summarization", "code_generation"]
    
    for i in range(5):
        trace_id = str(uuid.uuid4())
        span_id = str(uuid.uuid4())[:16]
        now = datetime.now()
        
        traces.append({
            "trace_id": trace_id,
            "name": f"batch_trace_{i}",
            "project": api_config["project"],
            "environment": api_config["environment"],
            "start_time": int((now.timestamp() - 1) * 1_000_000),
            "end_time": int(now.timestamp() * 1_000_000),
            "status": {"code": "OK"},
            "attributes": {
                "llm.model": models[i % len(models)],
                "llm.operation": operations[i % len(operations)],
                "batch_index": i,
            },
            "spans": [
                {
                    "span_id": span_id,
                    "trace_id": trace_id,
                    "name": f"span_{i}",
                    "kind": "LLM",
                    "start_time": int((now.timestamp() - 0.5) * 1_000_000),
                    "end_time": int(now.timestamp() * 1_000_000),
                    "status": {"code": "OK"},
                    "attributes": {"index": i},
                }
            ],
        })
    
    return traces


@pytest.fixture
def sample_dataset_items() -> list[dict[str, Any]]:
    """Generate sample dataset items for testing."""
    items = []
    for i in range(10):
        items.append({
            "item_id": f"test-item-{i:03d}",
            "item_type": "conversational",
            "content": {
                "agent_name": f"test_agent_{i}",
                "agent_role": "assistant",
                "agent_task": f"Task {i}: Answer user questions",
                "agent_response": f"Response to query {i}",
                "system_prompt": "You are a helpful assistant.",
                "user_id": f"user_{i}",
                "session_id": f"session_{i}",
                "input_text": f"What is {i} + {i}?",
                "output_text": f"The answer is {i + i}.",
                "ground_truth": str(i + i),
            },
            "metadata": {
                "test_index": i,
                "created_by": "sdk_integration_test",
            },
        })
    return items


@pytest.fixture
def sample_scorer_results(unique_slug: str) -> list[dict[str, Any]]:
    """Generate sample scorer results for testing."""
    results = []
    for i in range(5):
        results.append({
            "datasetSlug": unique_slug,
            "itemId": f"test-item-{i:03d}",
            "scorerId": f"test-scorer-{i:03d}",
            "score": 0.8 + (i * 0.02),
            "reason": f"Test result {i}: Score based on evaluation criteria",
            "metadata": {
                "evaluation_type": "automated",
                "test_index": i,
            },
        })
    return results


# =============================================================================
# Utility Functions
# =============================================================================


def wait_for_ingestion(seconds: int = WAIT_FOR_INGESTION_SECONDS) -> None:
    """Wait for data to be ingested/processed by the backend."""
    time.sleep(seconds)


def assert_api_success(response: Any, expected_codes: list[int] | None = None) -> None:
    """Assert API response is successful with helpful error messages."""
    if expected_codes is None:
        expected_codes = [200, 201, 204]
    
    if hasattr(response, "status_code"):
        status = response.status_code
    elif isinstance(response, dict) and "status_code" in response:
        status = response["status_code"]
    else:
        pytest.fail(FAIL_INVALID_RESPONSE_FORMAT.format(response_type=type(response)))
    
    if status not in expected_codes:
        error_msg = API_CALL_FAILED_HEADER
        error_msg += API_CALL_FAILED_EXPECTED.format(expected_codes=expected_codes)
        error_msg += API_CALL_FAILED_GOT.format(status=status)
        
        if hasattr(response, "parsed"):
            error_msg += API_CALL_FAILED_RESPONSE.format(parsed=response.parsed)
        if hasattr(response, "content"):
            error_msg += API_CALL_FAILED_CONTENT.format(content=response.content[:500])
        
        # Add helpful hints based on status code
        if status in STATUS_CODE_HINTS:
            error_msg += API_CALL_FAILED_HINT.format(hint=STATUS_CODE_HINTS[status])
        
        pytest.fail(error_msg)


# =============================================================================
# Class-Scoped Context Fixtures
# =============================================================================


@pytest.fixture(scope="class")
def test_context() -> dict[str, Any]:
    """Shared context for all tests in a class (for sequential tests)."""
    return {}


@pytest.fixture(scope="class")
def created_resources() -> dict[str, list[Any]]:
    """Track created resources for cleanup within a test class."""
    return {
        "datasets": [],
        "scorers": [],
        "traces": [],
        "projects": [],
        "etl_jobs": [],
    }


# =============================================================================
# Embedded Test Data (No External Files Required)
# =============================================================================

# Small, representative conversation dataset for testing
EMBEDDED_CONVERSATION_DATA: list[dict[str, Any]] = [
    {
        "item_id": "conv_001",
        "item_type": "conversational",
        "content": {
            "input": "What is the capital of France?",
            "output": "The capital of France is Paris.",
            "agent_name": "assistant",
            "agent_role": "helpful_assistant",
            "system_prompt": "You are a helpful assistant.",
        },
        "metadata": {
            "model": "gpt-4",
            "tokens": 15,
            "latency_ms": 850,
            "organization": DEFAULT_ORG_NAME,
        },
    },
    {
        "item_id": "conv_002",
        "item_type": "conversational",
        "content": {
            "input": "Explain quantum computing briefly",
            "output": "Quantum computing uses quantum mechanics principles like superposition and entanglement to perform calculations.",
            "agent_name": "assistant",
            "agent_role": "explainer",
            "system_prompt": "You are a helpful assistant.",
        },
        "metadata": {
            "model": "gpt-4",
            "tokens": 28,
            "latency_ms": 1200,
            "organization": DEFAULT_ORG_NAME,
        },
    },
    {
        "item_id": "conv_003",
        "item_type": "conversational",
        "content": {
            "input": "Write a Python function to add two numbers",
            "output": "def add(a, b):\n    return a + b",
            "agent_name": "code_assistant",
            "agent_role": "coder",
            "system_prompt": "You are a coding assistant.",
        },
        "metadata": {
            "model": "gpt-3.5-turbo",
            "tokens": 22,
            "latency_ms": 650,
            "organization": DEFAULT_ORG_NAME,
        },
    },
    {
        "item_id": "conv_004",
        "item_type": "conversational",
        "content": {
            "input": "What are the benefits of exercise?",
            "output": "Exercise improves cardiovascular health, strengthens muscles, boosts mental health, and increases energy.",
            "agent_name": "assistant",
            "agent_role": "health_advisor",
            "system_prompt": "You are a helpful assistant.",
        },
        "metadata": {
            "model": "claude-3-sonnet",
            "tokens": 35,
            "latency_ms": 920,
            "organization": DEFAULT_ORG_NAME,
        },
    },
    {
        "item_id": "conv_005",
        "item_type": "conversational",
        "content": {
            "input": "Translate 'Hello' to Spanish",
            "output": "Hola",
            "agent_name": "translator",
            "agent_role": "translator",
            "system_prompt": "You are a translation assistant.",
        },
        "metadata": {
            "model": "gpt-3.5-turbo",
            "tokens": 8,
            "latency_ms": 450,
            "organization": DEFAULT_ORG_NAME,
        },
    },
]

# Small, representative scorer results dataset for testing
EMBEDDED_SCORER_RESULTS_DATA: list[dict[str, Any]] = [
    {
        "item_id": "eval_001",
        "item_type": "evaluation",
        "content": {
            "input": "What is the capital of France?",
            "output": "The capital of France is Paris.",
            "expected_output": "Paris",
            "score": 1.0,
            "passed": True,
        },
        "metadata": {
            "scorer": "accuracy_checker",
            "evaluation_time": "2026-01-17T10:00:00Z",
            "model": "gpt-4",
            "organization": DEFAULT_ORG_NAME,
        },
    },
    {
        "item_id": "eval_002",
        "item_type": "evaluation",
        "content": {
            "input": "Explain quantum computing briefly",
            "output": "Quantum computing uses quantum mechanics principles.",
            "score": 0.85,
            "passed": True,
        },
        "metadata": {
            "scorer": "clarity_scorer",
            "evaluation_time": "2026-01-17T10:01:00Z",
            "model": "gpt-4",
            "organization": DEFAULT_ORG_NAME,
        },
    },
    {
        "item_id": "eval_003",
        "item_type": "evaluation",
        "content": {
            "input": "Write a Python function to add two numbers",
            "output": "def add(a, b): return a + b",
            "score": 0.95,
            "passed": True,
        },
        "metadata": {
            "scorer": "code_quality",
            "evaluation_time": "2026-01-17T10:02:00Z",
            "model": "gpt-3.5-turbo",
            "syntax_correct": True,
            "organization": DEFAULT_ORG_NAME,
        },
    },
    {
        "item_id": "eval_004",
        "item_type": "evaluation",
        "content": {
            "input": "What are the benefits of exercise?",
            "output": "Exercise improves health.",
            "score": 0.78,
            "passed": True,
        },
        "metadata": {
            "scorer": "comprehensiveness",
            "evaluation_time": "2026-01-17T10:03:00Z",
            "model": "claude-3-sonnet",
            "organization": DEFAULT_ORG_NAME,
        },
    },
    {
        "item_id": "eval_005",
        "item_type": "evaluation",
        "content": {
            "input": "Translate 'Hello' to Spanish",
            "output": "Hola",
            "expected_output": "Hola",
            "score": 1.0,
            "passed": True,
        },
        "metadata": {
            "scorer": "translation_accuracy",
            "evaluation_time": "2026-01-17T10:04:00Z",
            "model": "gpt-3.5-turbo",
            "exact_match": True,
            "organization": DEFAULT_ORG_NAME,
        },
    },
]


# =============================================================================
# Test Data Fixtures (Embedded - No External Files)
# =============================================================================


@pytest.fixture
def conversation_dataset() -> list[dict[str, Any]]:
    """Provide embedded conversation dataset for testing (no file required)."""
    return EMBEDDED_CONVERSATION_DATA.copy()


@pytest.fixture
def scorer_results_dataset() -> list[dict[str, Any]]:
    """Provide embedded scorer results dataset for testing (no file required)."""
    return EMBEDDED_SCORER_RESULTS_DATA.copy()


# =============================================================================
# Optional: Load Test Data from Files (for larger datasets)
# =============================================================================


@pytest.fixture
def conversation_dataset_from_file(test_data_dir: str) -> list[dict[str, Any]]:
    """Load conversation dataset from test data file (optional, for larger tests)."""
    file_path = os.path.join(test_data_dir, "conversation_dataset.json")
    
    if not os.path.exists(file_path):
        pytest.skip(SKIP_TEST_DATA_FILE_NOT_FOUND.format(file_path=file_path))
    
    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)
    
    # Handle nested structure
    if isinstance(data, dict) and "items" in data:
        return data["items"][:10]  # Limit for testing
    elif isinstance(data, list):
        return data[:10]
    
    return []


@pytest.fixture
def scorer_results_dataset_from_file(test_data_dir: str) -> list[dict[str, Any]]:
    """Load scorer results dataset from test data file (optional)."""
    file_path = os.path.join(test_data_dir, "scorer_results_dataset_new.json")
    
    if not os.path.exists(file_path):
        pytest.skip(SKIP_TEST_DATA_FILE_NOT_FOUND.format(file_path=file_path))
    
    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)
    
    # Handle nested structure
    if isinstance(data, dict) and "items" in data:
        return data["items"][:10]
    elif isinstance(data, list):
        return data[:10]
    
    return []


# Make utility functions available
pytest.wait_for_ingestion = wait_for_ingestion  # type: ignore[attr-defined]
pytest.assert_api_success = assert_api_success  # type: ignore[attr-defined]
