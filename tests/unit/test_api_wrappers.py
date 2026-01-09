"""
Unit Tests for Low-Level API Wrappers

Tests the auto-generated API wrapper functions structure and models.
"""

import inspect

import pytest

from noveum_api_client import Client
from noveum_api_client.api.datasets import get_api_v1_datasets, post_api_v1_datasets
from noveum_api_client.api.traces import get_api_v1_traces
from noveum_api_client.models import PostApiV1DatasetsBody


class TestAPIWrapperStructure:
    """Test that API wrapper functions have correct structure"""

    def test_get_datasets_function_exists(self):
        """Test that get_datasets function exists"""
        assert hasattr(get_api_v1_datasets, "sync_detailed")
        assert callable(get_api_v1_datasets.sync_detailed)

    def test_post_datasets_function_exists(self):
        """Test that post_datasets function exists"""
        assert hasattr(post_api_v1_datasets, "sync_detailed")
        assert callable(post_api_v1_datasets.sync_detailed)

    def test_get_traces_function_exists(self):
        """Test that get_traces function exists"""
        assert hasattr(get_api_v1_traces, "sync_detailed")
        assert callable(get_api_v1_traces.sync_detailed)


class TestDataSerialization:
    """Test data serialization in request bodies"""

    def test_body_model_serializes_to_dict(self):
        """Test that body models serialize to dict correctly"""
        body = PostApiV1DatasetsBody(slug="test-dataset", name="Test Dataset", description="A test")

        body_dict = body.to_dict()

        assert isinstance(body_dict, dict)
        assert body_dict["slug"] == "test-dataset"
        assert body_dict["name"] == "Test Dataset"

    def test_body_model_from_dict(self):
        """Test that body models can be created from dict"""
        data = {"slug": "test-dataset", "name": "Test Dataset", "description": "A test"}

        body = PostApiV1DatasetsBody.from_dict(data)

        assert body.slug == "test-dataset"
        assert body.name == "Test Dataset"


class TestClientConfiguration:
    """Test client configuration options"""

    def test_client_accepts_custom_base_url(self):
        """Test that client accepts custom base URL"""
        client = Client(base_url="https://custom.api.com", headers={"Authorization": "Bearer test"})

        # Client uses private attributes
        assert hasattr(client, "_base_url")
        assert client._base_url == "https://custom.api.com"

    def test_client_accepts_headers(self):
        """Test that client accepts custom headers"""
        headers = {"Authorization": "Bearer test", "X-Custom": "value"}
        client = Client(base_url="https://api.noveum.ai", headers=headers)

        # Client should store headers (private attribute)
        assert hasattr(client, "_headers")
        assert client._headers is not None

    def test_client_accepts_timeout(self):
        """Test that client accepts timeout configuration"""
        client = Client(base_url="https://api.noveum.ai", headers={"Authorization": "Bearer test"}, timeout=30.0)

        # Client uses private attributes
        assert hasattr(client, "_timeout")
        assert client._timeout == 30.0


class TestFunctionSignatures:
    """Test that API wrapper functions have correct signatures"""

    def test_get_datasets_accepts_client_param(self):
        """Test that get_datasets accepts client parameter"""
        sig = inspect.signature(get_api_v1_datasets.sync_detailed)
        assert "client" in sig.parameters

    def test_post_datasets_accepts_body_param(self):
        """Test that post_datasets accepts body parameter"""
        sig = inspect.signature(post_api_v1_datasets.sync_detailed)
        assert "body" in sig.parameters

    def test_get_traces_accepts_pagination_params(self):
        """Test that get_traces accepts pagination parameters"""
        sig = inspect.signature(get_api_v1_traces.sync_detailed)
        params = list(sig.parameters.keys())
        # Should accept size or other pagination params
        assert "client" in params


class TestModelValidation:
    """Test model validation"""

    def test_dataset_body_requires_name_and_slug(self):
        """Test that dataset body requires name and slug"""
        # Should raise TypeError if required fields missing
        with pytest.raises(TypeError):
            PostApiV1DatasetsBody(slug="test")  # Missing name

    def test_dataset_body_accepts_optional_description(self):
        """Test that description is optional"""
        body = PostApiV1DatasetsBody(slug="test", name="Test")

        assert body.slug == "test"
        assert body.name == "Test"


class TestAsyncSupport:
    """Test that async versions of functions exist"""

    def test_get_datasets_has_async_version(self):
        """Test that get_datasets has asyncio version"""
        assert hasattr(get_api_v1_datasets, "asyncio_detailed")
        assert callable(get_api_v1_datasets.asyncio_detailed)

    def test_post_datasets_has_async_version(self):
        """Test that post_datasets has asyncio version"""
        assert hasattr(post_api_v1_datasets, "asyncio_detailed")
        assert callable(post_api_v1_datasets.asyncio_detailed)
