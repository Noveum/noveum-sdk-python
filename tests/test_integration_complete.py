"""
Comprehensive integration tests for Noveum SDK.
Tests all major endpoints with real API.
"""

import os

import pytest

from noveum_api_client import Client, NoveumClient
from noveum_api_client.api.datasets import (
    get_api_v1_datasets,
)
from noveum_api_client.api.scorer_results import (
    get_api_v1_scorers_results,
)
from noveum_api_client.api.scorers import (
    get_api_v1_scorers,
)
from noveum_api_client.api.traces import (
    get_api_v1_traces,
)


@pytest.fixture
def api_key():
    """Get API key from environment."""
    key = os.getenv("NOVEUM_API_KEY")
    if not key:
        pytest.skip("NOVEUM_API_KEY not set")
    return key


@pytest.fixture
def client(api_key):
    """Create low-level client."""
    return Client(base_url="https://api.noveum.ai", headers={"Authorization": f"Bearer {api_key}"})


@pytest.fixture
def high_level_client(api_key):
    """Create high-level client."""
    return NoveumClient(api_key=api_key)


class TestDatasets:
    """Test dataset endpoints."""

    def test_list_datasets(self, client):
        """Test listing datasets."""
        response = get_api_v1_datasets.sync_detailed(client=client)
        assert response.status_code == 200
        print(f"✅ List datasets: {response.status_code}")

    def test_list_datasets_with_pagination(self, client):
        """Test listing datasets with pagination."""
        response = get_api_v1_datasets.sync_detailed(client=client, limit=5, offset=0)
        assert response.status_code == 200
        print(f"✅ List datasets with pagination: {response.status_code}")


class TestTraces:
    """Test trace endpoints."""

    def test_list_traces(self, client):
        """Test listing traces."""
        response = get_api_v1_traces.sync_detailed(client=client)
        assert response.status_code == 200
        print(f"✅ List traces: {response.status_code}")


class TestScorers:
    """Test scorer endpoints."""

    def test_list_scorers(self, client):
        """Test listing scorers."""
        response = get_api_v1_scorers.sync_detailed(client=client)
        assert response.status_code == 200
        print(f"✅ List scorers: {response.status_code}")


class TestScorerResults:
    """Test scorer results endpoints."""

    def test_list_results(self, client):
        """Test listing scorer results."""
        response = get_api_v1_scorers_results.sync_detailed(client=client)
        assert response.status_code == 200
        print(f"✅ List scorer results: {response.status_code}")


class TestHighLevelClient:
    """Test high-level convenience client."""

    def test_list_datasets(self, high_level_client):
        """Test listing datasets via high-level client."""
        response = high_level_client.list_datasets()
        assert response["status_code"] == 200
        print(f"✅ High-level list datasets: {response['status_code']}")

    def test_get_results(self, high_level_client):
        """Test getting results via high-level client."""
        response = high_level_client.get_results()
        assert response["status_code"] == 200
        print(f"✅ High-level get results: {response['status_code']}")


class TestClientConfiguration:
    """Test client configuration and setup."""

    def test_client_initialization(self, api_key):
        """Test client initialization."""
        client = Client(base_url="https://api.noveum.ai", headers={"Authorization": f"Bearer {api_key}"})
        assert client is not None
        print("✅ Client initialization")

    def test_high_level_client_initialization(self, api_key):
        """Test high-level client initialization."""
        client = NoveumClient(api_key=api_key)
        assert client is not None
        print("✅ High-level client initialization")

    def test_custom_base_url(self, api_key):
        """Test custom base URL."""
        client = NoveumClient(api_key=api_key, base_url="https://api.noveum.ai")
        assert client.base_url == "https://api.noveum.ai"
        print("✅ Custom base URL")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
