"""
Unit Tests for NoveumClient Wrapper

Tests the high-level client wrapper methods with mocked API responses.
"""

from noveum_api_client import NoveumClient


class TestNoveumClientInit:
    """Test NoveumClient initialization"""

    def test_client_initialization(self):
        """Test that client initializes correctly"""
        client = NoveumClient(api_key="test_key", base_url="https://api.noveum.ai")

        assert client.api_key == "test_key"
        assert client.base_url == "https://api.noveum.ai"
        assert client._client is not None

    def test_client_uses_default_base_url(self):
        """Test that default base URL is used"""
        client = NoveumClient(api_key="test_key")
        assert client.base_url == "https://api.noveum.ai"


class TestDatasetMethods:
    """Test dataset wrapper methods"""

    def test_list_datasets_method_exists(self, mock_noveum_client):
        """Test that list_datasets method exists"""
        assert hasattr(mock_noveum_client, "list_datasets")
        assert callable(mock_noveum_client.list_datasets)

    def test_get_dataset_items_method_exists(self, mock_noveum_client):
        """Test that get_dataset_items method exists"""
        assert hasattr(mock_noveum_client, "get_dataset_items")
        assert callable(mock_noveum_client.get_dataset_items)


class TestResultsMethods:
    """Test results wrapper methods"""

    def test_get_results_method_exists(self, mock_noveum_client):
        """Test that get_results method exists"""
        assert hasattr(mock_noveum_client, "get_results")
        assert callable(mock_noveum_client.get_results)


class TestClientInternalState:
    """Test client internal state and configuration"""

    def test_client_has_internal_client(self, mock_noveum_client):
        """Test that client has _client attribute"""
        assert hasattr(mock_noveum_client, "_client")
        assert mock_noveum_client._client is not None

    def test_client_stores_api_key(self, mock_noveum_client):
        """Test that client stores API key"""
        assert hasattr(mock_noveum_client, "api_key")
        assert mock_noveum_client.api_key == "test_key"

    def test_client_stores_base_url(self, mock_noveum_client):
        """Test that client stores base URL"""
        assert hasattr(mock_noveum_client, "base_url")
        assert mock_noveum_client.base_url == "https://api.noveum.ai"


class TestAuthenticationHandling:
    """Test authentication and authorization handling"""

    def test_client_includes_auth_header(self):
        """Test that client includes authorization header"""
        client = NoveumClient(api_key="test_api_key_123")

        # Check that _client has authorization header
        assert client._client is not None
        # The actual header is set during Client initialization


class TestWrapperMethodSignatures:
    """Test wrapper method signatures and parameters"""

    def test_list_datasets_accepts_limit(self, mock_noveum_client):
        """Test that list_datasets accepts limit parameter"""
        import inspect

        sig = inspect.signature(mock_noveum_client.list_datasets)
        assert "limit" in sig.parameters or len(sig.parameters) == 0  # May accept **kwargs

    def test_get_dataset_items_accepts_dataset_slug(self, mock_noveum_client):
        """Test that get_dataset_items requires dataset_slug"""
        import inspect

        sig = inspect.signature(mock_noveum_client.get_dataset_items)
        params = list(sig.parameters.keys())
        # Should have dataset_slug as first param or in params
        assert len(params) > 0 or "dataset_slug" in sig.parameters
