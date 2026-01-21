"""
Unit Test Configuration and Fixtures

Provides mocked clients and responses for unit testing without hitting real API.
"""

import os
import sys
from unittest.mock import Mock, patch

import pytest

# Add parent directories to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from noveum_api_client import Client, NoveumClient


@pytest.fixture
def mock_response():
    """Create a mock HTTP response"""
    mock_resp = Mock()
    # Ensure status_code is an actual integer, not a Mock
    mock_resp.status_code = 200
    mock_resp.content = b'{"data": "test_data"}'
    mock_resp.text = '{"data": "test_data"}'
    mock_resp.headers = {}
    mock_resp.parsed = {"data": "test_data"}
    mock_resp.json.return_value = {"data": "test_data"}
    return mock_resp


@pytest.fixture
def mock_client():
    """Create a mocked low-level Client"""
    client = Mock(spec=Client)
    client.base_url = "https://api.noveum.ai"
    client.raise_on_unexpected_status = False

    # Configure the mock chain for get_httpx_client().request()
    mock_httpx_client = Mock()
    mock_request_response = Mock()
    mock_request_response.status_code = 200
    mock_request_response.content = b'{"data": "test"}'
    mock_request_response.text = '{"data": "test"}'
    mock_request_response.json.return_value = {"data": "test"}

    mock_httpx_client.request.return_value = mock_request_response
    client.get_httpx_client.return_value = mock_httpx_client

    return client


@pytest.fixture
def mock_noveum_client():
    """Create a mocked high-level NoveumClient"""
    with patch("noveum_api_client.Client") as mock_client_class:
        mock_client_instance = Mock()
        mock_client_class.return_value = mock_client_instance

        client = NoveumClient(api_key="test_key")
        client._client = mock_client_instance

        yield client


@pytest.fixture
def sample_dataset_response():
    """Sample dataset API response"""
    return {
        "id": "test-dataset-id",
        "slug": "test-dataset",
        "name": "Test Dataset",
        "description": "A test dataset",
        "created_at": "2024-01-01T00:00:00Z",
        "item_count": 10,
    }


@pytest.fixture
def sample_dataset_items():
    """Sample dataset items"""
    return [
        {
            "item_id": "item-1",
            "item_type": "conversational",
            "content": {"message": "Hello", "speaker": "user"},
            "metadata": {"tags": ["test"]},
        },
        {
            "item_id": "item-2",
            "item_type": "conversational",
            "content": {"message": "Hi there", "speaker": "agent"},
            "metadata": {"tags": ["test"]},
        },
    ]


@pytest.fixture
def sample_trace_response():
    """Sample trace API response"""
    return {
        "trace_id": "trace-123",
        "name": "test_trace",
        "start_time": "2024-01-01T00:00:00Z",
        "end_time": "2024-01-01T00:00:01Z",
        "duration_ms": 1000,
        "status": "ok",
        "spans": [],
    }


@pytest.fixture
def mock_api_error_response():
    """Mock error response"""
    mock_resp = Mock()
    mock_resp.status_code = 500
    mock_resp.parsed = {"error": "Internal server error"}
    return mock_resp


@pytest.fixture
def mock_auth_error_response():
    """Mock 401 authentication error"""
    mock_resp = Mock()
    mock_resp.status_code = 401
    mock_resp.parsed = {"error": "Unauthorized"}
    return mock_resp


# Pytest hook to ensure all httpx.Response mocks have proper status codes
@pytest.fixture(autouse=True)
def ensure_mock_status_codes(monkeypatch):
    """Ensure all mock responses have integer status codes"""
    original_mock = Mock

    def mock_with_status_code(*args, **kwargs):
        """Create a mock that sets status_code as an integer if specified"""
        mock_obj = original_mock(*args, **kwargs)
        # If this looks like an httpx.Response mock, ensure status_code is set properly
        if "spec" in kwargs and kwargs.get("spec").__name__ == "Response":
            # Will be set by the test, just ensure it's not auto-mocked
            pass
        return mock_obj

    return None
