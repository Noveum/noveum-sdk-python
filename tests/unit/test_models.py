"""
Unit Tests for Data Models

Tests attrs models for serialization, deserialization, and validation.
"""

import json

import pytest

from noveum_api_client.models import (
    PostApiV1DatasetsBody,
    PostApiV1DatasetsByDatasetSlugItemsBody,
    PostApiV1DatasetsByDatasetSlugItemsBodyItemsItem,
    PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemContent,
    PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemMetadata,
)


class TestDatasetModels:
    """Test dataset-related models"""

    def test_create_dataset_body_model(self):
        """Test creating PostApiV1DatasetsBody model"""
        body = PostApiV1DatasetsBody(slug="test-dataset", name="Test Dataset", description="A test dataset")

        assert body.slug == "test-dataset"
        assert body.name == "Test Dataset"
        assert body.description == "A test dataset"

    def test_dataset_body_to_dict(self):
        """Test serializing dataset body to dict"""
        body = PostApiV1DatasetsBody(slug="test-dataset", name="Test Dataset", description="Test")

        body_dict = body.to_dict()

        assert isinstance(body_dict, dict)
        assert body_dict["slug"] == "test-dataset"
        assert body_dict["name"] == "Test Dataset"

    def test_dataset_body_from_dict(self):
        """Test deserializing dataset body from dict"""
        data = {"slug": "test-dataset", "name": "Test Dataset", "description": "Test description"}

        body = PostApiV1DatasetsBody.from_dict(data)

        assert body.slug == "test-dataset"
        assert body.name == "Test Dataset"

    def test_dataset_body_with_optional_fields(self):
        """Test dataset body with optional fields"""
        body = PostApiV1DatasetsBody(
            slug="test",
            name="Test",
            # description is optional
        )

        assert body.slug == "test"
        assert body.name == "Test"


class TestDatasetItemModels:
    """Test dataset item models"""

    def test_create_dataset_item_model(self):
        """Test creating dataset item model"""
        content = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemContent(message="Hello")
        metadata = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemMetadata()

        item = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItem(
            item_id="test-item-1", item_type="conversational", content=content, metadata=metadata
        )

        assert item.item_id == "test-item-1"
        assert item.item_type == "conversational"
        assert item.content.message == "Hello"

    def test_dataset_item_to_dict(self):
        """Test serializing dataset item to dict"""
        content = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemContent(message="Hello")
        metadata = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemMetadata()

        item = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItem(
            item_id="test-item-1", item_type="conversational", content=content, metadata=metadata
        )

        item_dict = item.to_dict()

        assert isinstance(item_dict, dict)
        assert item_dict["item_id"] == "test-item-1"
        assert item_dict["item_type"] == "conversational"

    def test_dataset_item_from_dict(self):
        """Test deserializing dataset item from dict"""
        data = {
            "item_id": "test-item-1",
            "item_type": "conversational",
            "content": {"message": "Hello"},
            "metadata": {},
        }

        item = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItem.from_dict(data)

        assert item.item_id == "test-item-1"
        # Content is now a model, access via attribute
        assert item.content.message == "Hello"

    def test_dataset_items_body_with_multiple_items(self):
        """Test creating dataset items body with multiple items"""
        items = []
        for i in range(5):
            content = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemContent(message=f"Message {i}")
            metadata = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemMetadata()
            item = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItem(
                item_id=f"item-{i}", item_type="conversational", content=content, metadata=metadata
            )
            items.append(item)

        body = PostApiV1DatasetsByDatasetSlugItemsBody(items=items)

        assert len(body.items) == 5
        assert body.items[0].item_id == "item-0"
        assert body.items[4].item_id == "item-4"


class TestModelValidation:
    """Test model validation and error handling"""

    def test_required_fields_must_be_provided(self):
        """Test that required fields must be provided"""
        # slug and name are required
        with pytest.raises(TypeError):
            PostApiV1DatasetsBody(slug="test")  # Missing name

    def test_item_type_and_content_are_required(self):
        """Test that item_type and content are required for dataset items"""
        content = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemContent()

        # Should work with just item_type and content (item_id may be optional)
        item = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItem(item_type="conversational", content=content)

        assert item.item_type == "conversational"


class TestComplexDataTypes:
    """Test handling of complex data types"""

    def test_nested_dict_in_content(self):
        """Test that nested dicts in content are handled"""
        # Content model has specific fields + additional_properties
        content = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemContent(message="Hello", user_id="test_user")
        metadata = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemMetadata()

        item = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItem(
            item_id="test-item", item_type="conversational", content=content, metadata=metadata
        )

        item_dict = item.to_dict()

        assert item_dict["content"]["message"] == "Hello"
        assert item_dict["content"]["user_id"] == "test_user"

    def test_serialization_roundtrip(self):
        """Test that serialization roundtrip preserves data"""
        content = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemContent(message="Hello", quality_score=0.95)
        metadata = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemMetadata()

        original = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItem(
            item_id="test-item", item_type="conversational", content=content, metadata=metadata
        )

        # Serialize to dict
        as_dict = original.to_dict()

        # Deserialize from dict
        restored = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItem.from_dict(as_dict)

        assert restored.item_id == original.item_id
        assert restored.item_type == original.item_type
        assert restored.content.message == original.content.message

    def test_json_serialization(self):
        """Test that models can be JSON serialized"""
        content = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemContent(message="Hello")
        metadata = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemMetadata()

        item = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItem(
            item_id="test-item", item_type="conversational", content=content, metadata=metadata
        )

        # Convert to dict, then to JSON
        item_dict = item.to_dict()
        json_str = json.dumps(item_dict)

        # Should be valid JSON
        parsed = json.loads(json_str)
        assert parsed["item_id"] == "test-item"


class TestEdgeCases:
    """Test edge cases and boundary conditions"""

    def test_empty_content_model(self):
        """Test item with minimal content"""
        content = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemContent()
        metadata = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemMetadata()

        item = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItem(
            item_id="test-item", item_type="conversational", content=content, metadata=metadata
        )

        assert item.content is not None
        assert item.item_type == "conversational"

    def test_empty_metadata_model(self):
        """Test item with empty metadata"""
        content = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemContent(message="Hello")
        metadata = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemMetadata()

        item = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItem(
            item_id="test-item", item_type="conversational", content=content, metadata=metadata
        )

        assert item.metadata is not None

    def test_long_message_content(self):
        """Test item with long message content"""
        long_message = "Message " * 1000

        content = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemContent(message=long_message)
        metadata = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemMetadata()

        item = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItem(
            item_id="test-item", item_type="conversational", content=content, metadata=metadata
        )

        assert len(item.content.message) > 5000

    def test_special_characters_in_strings(self):
        """Test handling of special characters"""
        special_message = "Hello 🌍! Special chars: @#$%^&*()[]{}\n你好世界"

        content = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemContent(message=special_message)
        metadata = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemMetadata()

        item = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItem(
            item_id="test-item", item_type="conversational", content=content, metadata=metadata
        )

        item_dict = item.to_dict()
        assert "🌍" in item_dict["content"]["message"]
        assert "你好世界" in item_dict["content"]["message"]


class TestModelEquality:
    """Test model equality and comparison"""

    def test_equal_models_are_equal(self):
        """Test that models with same data are equal"""
        content1 = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemContent(message="Hello")
        metadata1 = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemMetadata()

        item1 = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItem(
            item_id="test-item", item_type="conversational", content=content1, metadata=metadata1
        )

        content2 = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemContent(message="Hello")
        metadata2 = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemMetadata()

        item2 = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItem(
            item_id="test-item", item_type="conversational", content=content2, metadata=metadata2
        )

        # attrs models should support equality via to_dict
        assert item1.to_dict() == item2.to_dict()

    def test_different_models_are_not_equal(self):
        """Test that models with different data are not equal"""
        content1 = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemContent(message="Hello")
        metadata1 = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemMetadata()

        item1 = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItem(
            item_id="test-item-1", item_type="conversational", content=content1, metadata=metadata1
        )

        content2 = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemContent(message="Hello")
        metadata2 = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItemMetadata()

        item2 = PostApiV1DatasetsByDatasetSlugItemsBodyItemsItem(
            item_id="test-item-2", item_type="conversational", content=content2, metadata=metadata2
        )

        assert item1.to_dict() != item2.to_dict()
