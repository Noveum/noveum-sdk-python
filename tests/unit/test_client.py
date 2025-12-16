"""Unit tests for NoveumClient."""

import pytest

from noveum import NoveumClient, AsyncNoveumClient
from noveum.exceptions import InvalidAPIKeyError


@pytest.mark.unit
class TestNoveumClient:
    """Tests for NoveumClient initialization and configuration."""

    def test_client_initialization_with_api_key(self):
        """Test client initialization with API key."""
        client = NoveumClient(api_key="test-key")
        assert client is not None
        assert client._http_client is not None

    def test_client_initialization_without_api_key_raises_error(self):
        """Test that client initialization without API key raises error."""
        with pytest.raises(InvalidAPIKeyError):
            NoveumClient()

    def test_client_with_custom_base_url(self):
        """Test client initialization with custom base URL."""
        custom_url = "https://custom.noveum.ai/api/v1"
        client = NoveumClient(api_key="test-key", base_url=custom_url)
        assert client._http_client.config.base_url == custom_url

    def test_client_with_custom_timeout(self):
        """Test client initialization with custom timeout."""
        client = NoveumClient(api_key="test-key", timeout=120.0)
        assert client._http_client.config.timeout == 120.0

    def test_client_with_custom_max_retries(self):
        """Test client initialization with custom max retries."""
        client = NoveumClient(api_key="test-key", max_retries=10)
        assert client._http_client.config.max_retries == 10

    def test_client_resources_accessible(self):
        """Test that all resources are accessible from client."""
        client = NoveumClient(api_key="test-key")
        
        assert hasattr(client, "datasets")
        assert hasattr(client, "evals")
        assert hasattr(client, "scorers")
        assert hasattr(client, "traces")

    def test_client_context_manager(self):
        """Test client as context manager."""
        with NoveumClient(api_key="test-key") as client:
            assert client is not None
            assert hasattr(client, "datasets")

    def test_async_client_initialization(self):
        """Test AsyncNoveumClient initialization."""
        client = AsyncNoveumClient(api_key="test-key")
        assert client is not None
        assert client._http_client is not None

    def test_async_client_context_manager(self):
        """Test AsyncNoveumClient as async context manager."""
        import asyncio

        async def test():
            async with AsyncNoveumClient(api_key="test-key") as client:
                assert client is not None
                assert hasattr(client, "datasets")

        asyncio.run(test())


@pytest.mark.unit
class TestClientConfiguration:
    """Tests for client configuration."""

    def test_default_base_url(self):
        """Test default base URL."""
        client = NoveumClient(api_key="test-key")
        assert "api.noveum.ai" in client._http_client.config.base_url

    def test_default_timeout(self):
        """Test default timeout value."""
        client = NoveumClient(api_key="test-key")
        assert client._http_client.config.timeout > 0

    def test_default_max_retries(self):
        """Test default max retries value."""
        client = NoveumClient(api_key="test-key")
        assert client._http_client.config.max_retries > 0

    def test_client_headers_include_auth(self):
        """Test that client headers include authorization."""
        client = NoveumClient(api_key="test-key")
        headers = client._http_client.client.headers
        assert "authorization" in headers
        assert "Bearer" in str(headers["authorization"])

    def test_client_headers_include_user_agent(self):
        """Test that client headers include user agent."""
        client = NoveumClient(api_key="test-key")
        headers = client._http_client.client.headers
        assert "user-agent" in headers
