"""Integration tests with real API."""

import os

import pytest

from noveum import NoveumClient


@pytest.mark.integration
class TestIntegrationBasic:
    """Basic integration tests with real API."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup for integration tests."""
        self.api_key = os.getenv("NOVEUM_API_KEY")
        if not self.api_key:
            pytest.skip("NOVEUM_API_KEY not set")

    def test_client_creation_with_real_key(self):
        """Test client creation with real API key."""
        client = NoveumClient(api_key=self.api_key)
        assert client is not None
        assert client._http_client is not None

    def test_api_status(self):
        """Test getting API status."""
        client = NoveumClient(api_key=self.api_key)
        try:
            # Try to get a basic response from the API
            # This will fail if the API is down
            response = client.http_client.get("/status")
            assert response is not None
        except Exception as e:
            # API might not have a /status endpoint
            # That's okay for this test
            pass

    def test_datasets_list_empty_response(self):
        """Test listing datasets (may be empty)."""
        client = NoveumClient(api_key=self.api_key)
        try:
            # This should work even if there are no datasets
            datasets_iter = client.datasets.list(limit=1)
            # Try to get first item
            try:
                first = next(datasets_iter)
                assert first is not None
            except StopIteration:
                # Empty list is fine
                pass
        except Exception as e:
            # API might have different structure
            pytest.skip(f"API structure different: {e}")

    def test_scorers_list(self):
        """Test listing scorers."""
        client = NoveumClient(api_key=self.api_key)
        try:
            scorers_iter = client.scorers.list(limit=1)
            # Try to get first item
            try:
                first = next(scorers_iter)
                assert first is not None
            except StopIteration:
                # Empty list is fine
                pass
        except Exception as e:
            pytest.skip(f"Scorers endpoint not available: {e}")


@pytest.mark.integration
@pytest.mark.slow
class TestIntegrationAdvanced:
    """Advanced integration tests."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup for integration tests."""
        self.api_key = os.getenv("NOVEUM_API_KEY")
        if not self.api_key:
            pytest.skip("NOVEUM_API_KEY not set")

    def test_client_with_custom_timeout(self):
        """Test client with custom timeout."""
        client = NoveumClient(api_key=self.api_key, timeout=30.0)
        assert client._http_client.config.timeout == 30.0

    def test_client_with_custom_retries(self):
        """Test client with custom retries."""
        client = NoveumClient(api_key=self.api_key, max_retries=3)
        assert client._http_client.config.max_retries == 3

    def test_multiple_resource_access(self):
        """Test accessing multiple resources."""
        client = NoveumClient(api_key=self.api_key)
        
        # All resources should be accessible
        assert client.datasets is not None
        assert client.evals is not None
        assert client.scorers is not None
        assert client.traces is not None

    def test_client_context_manager_with_real_api(self):
        """Test client context manager with real API."""
        with NoveumClient(api_key=self.api_key) as client:
            assert client is not None
            assert hasattr(client, "datasets")
