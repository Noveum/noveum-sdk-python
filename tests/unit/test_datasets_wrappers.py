"""
Unit Tests for Dataset API Wrappers

Tests all dataset-related API wrapper functions with mocked responses.
"""

from unittest.mock import Mock

import httpx
import pytest

from noveum_api_client.api.datasets import (
    delete_api_v1_datasets_by_dataset_slug_items,
    delete_api_v1_datasets_by_dataset_slug_items_by_item_id,
    delete_api_v1_datasets_by_slug,
    get_api_v1_datasets,
    get_api_v1_datasets_by_dataset_slug_items,
    get_api_v1_datasets_by_dataset_slug_items_by_item_id,
    get_api_v1_datasets_by_slug,
    post_api_v1_datasets,
    post_api_v1_datasets_by_dataset_slug_items,
    put_api_v1_datasets_by_slug,
)
from noveum_api_client.models import (
    PostApiV1DatasetsBody,
    PostApiV1DatasetsByDatasetSlugItemsBody,
    PostApiV1DatasetsByDatasetSlugItemsBodyItemsItem,
    PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemContent,
    PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemMetadata,
)


class TestDatasetListingWrappers:
    """Test dataset listing API wrappers"""

    def test_get_datasets_has_sync_method(self):
        """Test that get_datasets has sync_detailed method"""
        assert hasattr(get_api_v1_datasets, "sync_detailed")
        assert callable(get_api_v1_datasets.sync_detailed)

    def test_get_datasets_has_async_method(self):
        """Test that get_datasets has asyncio_detailed method"""
        assert hasattr(get_api_v1_datasets, "asyncio_detailed")
        assert callable(get_api_v1_datasets.asyncio_detailed)

    def test_get_datasets_accepts_pagination_params(self, mock_client):
        """Test that get_datasets accepts pagination parameters"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = []

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_datasets.sync_detailed(client=mock_client, limit=50, offset=10)

        assert response.status_code == 200


class TestDatasetCRUDWrappers:
    """Test dataset CRUD operation wrappers"""

    def test_post_datasets_accepts_body_model(self, mock_client):
        """Test that post_datasets accepts PostApiV1DatasetsBody"""
        body = PostApiV1DatasetsBody(slug="test-dataset", name="Test Dataset", description="Test")

        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 201
        mock_response.content = b'{"slug": "test-dataset"}'
        mock_response.headers = {}
        mock_response.json.return_value = {"slug": "test-dataset"}

        mock_client.get_httpx_client().request.return_value = mock_response
        response = post_api_v1_datasets.sync_detailed(client=mock_client, body=body)

        assert response.status_code == 201

    def test_get_dataset_by_slug_has_methods(self):
        """Test get dataset by slug has required methods"""
        assert hasattr(get_api_v1_datasets_by_slug, "sync_detailed")
        assert hasattr(get_api_v1_datasets_by_slug, "asyncio_detailed")

    def test_patch_dataset_has_methods(self):
        """Test patch dataset has required methods"""
        assert hasattr(put_api_v1_datasets_by_slug, "sync_detailed")
        assert hasattr(put_api_v1_datasets_by_slug, "asyncio_detailed")

    def test_delete_dataset_has_methods(self):
        """Test delete dataset has required methods"""
        assert hasattr(delete_api_v1_datasets_by_slug, "sync_detailed")
        assert hasattr(delete_api_v1_datasets_by_slug, "asyncio_detailed")


class TestDatasetItemWrappers:
    """Test dataset item API wrappers"""

    def test_get_dataset_items_accepts_params(self, mock_client):
        """Test get dataset items accepts pagination params"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = []

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_datasets_by_dataset_slug_items.sync_detailed(
            client=mock_client, dataset_slug="test-dataset", limit=10, offset=0
        )

        assert response.status_code == 200

    def test_post_dataset_items_accepts_body(self, mock_client):
        """Test post dataset items accepts body with items"""
        content = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemContent(message="Test message")
        metadata = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemMetadata()

        item = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItem(
            item_id="test-item", item_type="conversational", content=content, metadata=metadata
        )

        body = PostApiV1DatasetsByDatasetSlugItemsBody(items=[item])

        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 201
        mock_response.content = b'{"created": 1}'
        mock_response.headers = {}
        mock_response.json.return_value = {"created": 1}

        mock_client.get_httpx_client().request.return_value = mock_response
        response = post_api_v1_datasets_by_dataset_slug_items.sync_detailed(
            client=mock_client, dataset_slug="test-dataset", body=body
        )

        assert response.status_code == 201

    def test_get_dataset_item_by_id_has_methods(self):
        """Test get single dataset item has methods"""
        assert hasattr(get_api_v1_datasets_by_dataset_slug_items_by_item_id, "sync_detailed")
        assert hasattr(get_api_v1_datasets_by_dataset_slug_items_by_item_id, "asyncio_detailed")

    def test_patch_dataset_item_has_methods(self):
        """Test patch dataset item has methods"""
        assert hasattr(put_api_v1_datasets_by_slug, "sync_detailed")
        assert hasattr(put_api_v1_datasets_by_slug, "asyncio_detailed")

    def test_delete_dataset_item_has_methods(self):
        """Test delete single dataset item has methods"""
        assert hasattr(delete_api_v1_datasets_by_dataset_slug_items_by_item_id, "sync_detailed")
        assert hasattr(delete_api_v1_datasets_by_dataset_slug_items_by_item_id, "asyncio_detailed")

    def test_bulk_delete_dataset_items_has_methods(self):
        """Test bulk delete dataset items has methods"""
        assert hasattr(delete_api_v1_datasets_by_dataset_slug_items, "sync_detailed")
        assert hasattr(delete_api_v1_datasets_by_dataset_slug_items, "asyncio_detailed")


class TestDatasetModelSerialization:
    """Test dataset model serialization"""

    def test_dataset_body_serializes_correctly(self):
        """Test PostApiV1DatasetsBody serialization"""
        body = PostApiV1DatasetsBody(slug="test-dataset", name="Test Dataset", description="A test dataset")

        body_dict = body.to_dict()

        assert body_dict["slug"] == "test-dataset"
        assert body_dict["name"] == "Test Dataset"
        assert body_dict["description"] == "A test dataset"

    def test_dataset_item_serializes_correctly(self):
        """Test dataset item serialization"""
        content = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemContent(message="Test", user_id="user123")
        metadata = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemMetadata()

        item = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItem(
            item_id="item-1", item_type="conversational", content=content, metadata=metadata
        )

        item_dict = item.to_dict()

        assert item_dict["item_id"] == "item-1"
        assert item_dict["item_type"] == "conversational"
        assert "content" in item_dict

    def test_dataset_items_body_with_multiple_items(self):
        """Test body with multiple items"""
        items = []
        for i in range(3):
            content = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemContent(message=f"Message {i}")
            metadata = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemMetadata()
            item = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItem(
                item_id=f"item-{i}", item_type="conversational", content=content, metadata=metadata
            )
            items.append(item)

        body = PostApiV1DatasetsByDatasetSlugItemsBody(items=items)

        assert len(body.items) == 3


class TestDatasetErrorHandling:
    """Test error handling in dataset wrappers"""

    @pytest.mark.parametrize("status_code", [400, 401, 403, 404, 500])
    def test_handles_error_status_codes(self, mock_client, status_code):
        """Test that dataset wrappers handle various error codes"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = status_code
        mock_response.content = b'{"error": "Error message"}'
        mock_response.headers = {}
        mock_response.json.return_value = {"error": "Error message"}

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_datasets.sync_detailed(client=mock_client)

        assert response.status_code == status_code
