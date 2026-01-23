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


class TestProjectModels:
    """Test project-related models"""

    def test_create_project_body_minimal(self):
        """Test creating project body with minimal required fields"""
        from noveum_api_client.models import PostApiV1ProjectsBody

        body = PostApiV1ProjectsBody(name="Test Project", id="test-project-id")

        assert body.name == "Test Project"
        assert body.id == "test-project-id"

    def test_create_project_body_with_description(self):
        """Test creating project body with optional description"""
        from noveum_api_client.models import PostApiV1ProjectsBody

        body = PostApiV1ProjectsBody(
            name="Test Project", id="test-project-id", description="A test project for unit tests"
        )

        assert body.name == "Test Project"
        assert body.id == "test-project-id"
        assert body.description == "A test project for unit tests"

    def test_project_body_to_dict(self):
        """Test serializing project body to dict"""
        from noveum_api_client.models import PostApiV1ProjectsBody

        body = PostApiV1ProjectsBody(name="Test Project", id="test-project-id", description="Test description")

        body_dict = body.to_dict()

        assert isinstance(body_dict, dict)
        assert body_dict["name"] == "Test Project"
        assert body_dict["id"] == "test-project-id"
        assert body_dict["description"] == "Test description"

    def test_project_body_from_dict(self):
        """Test deserializing project body from dict"""
        from noveum_api_client.models import PostApiV1ProjectsBody

        data = {"name": "Test Project", "id": "test-project-id", "description": "Test description"}

        body = PostApiV1ProjectsBody.from_dict(data)

        assert body.name == "Test Project"
        assert body.id == "test-project-id"
        assert body.description == "Test description"

    def test_project_body_roundtrip(self):
        """Test project body serialization roundtrip"""
        from noveum_api_client.models import PostApiV1ProjectsBody

        original = PostApiV1ProjectsBody(name="Test Project", id="test-project-id", description="Test")

        # Serialize to dict
        as_dict = original.to_dict()

        # Deserialize from dict
        restored = PostApiV1ProjectsBody.from_dict(as_dict)

        assert restored.name == original.name
        assert restored.id == original.id
        assert restored.description == original.description


class TestETLJobModels:
    """Test ETL job-related models"""

    def test_create_etl_job_body(self):
        """Test creating ETL job body"""
        from noveum_api_client.models import PostApiV1EtlJobsBody

        body = PostApiV1EtlJobsBody(
            name="Test ETL Job",
            project_id="test-project",
            dataset_slug="test-dataset",
            environment="test",
            mapper_code="def mapper(item): return item",
        )

        assert body.name == "Test ETL Job"
        assert body.project_id == "test-project"
        assert body.dataset_slug == "test-dataset"
        assert body.environment == "test"
        assert "def mapper" in body.mapper_code

    def test_etl_job_body_to_dict(self):
        """Test serializing ETL job body to dict"""
        from noveum_api_client.models import PostApiV1EtlJobsBody

        body = PostApiV1EtlJobsBody(
            name="Test ETL Job",
            project_id="test-project",
            dataset_slug="test-dataset",
            environment="test",
            mapper_code="def mapper(item): return item",
        )

        body_dict = body.to_dict()

        assert isinstance(body_dict, dict)
        assert body_dict["name"] == "Test ETL Job"
        assert body_dict["projectId"] == "test-project"
        assert body_dict["datasetSlug"] == "test-dataset"
        assert body_dict["environment"] == "test"

    def test_etl_job_body_from_dict(self):
        """Test deserializing ETL job body from dict"""
        from noveum_api_client.models import PostApiV1EtlJobsBody

        data = {
            "name": "Test ETL Job",
            "projectId": "test-project",
            "datasetSlug": "test-dataset",
            "environment": "test",
            "mapperCode": "def mapper(item): return item",
        }

        body = PostApiV1EtlJobsBody.from_dict(data)

        assert body.name == "Test ETL Job"
        assert body.project_id == "test-project"
        assert body.dataset_slug == "test-dataset"
        assert body.environment == "test"


class TestTraceModels:
    """Test trace-related models"""

    def test_create_trace_sdk_model(self):
        """Test creating trace SDK model"""
        from noveum_api_client.models import PostApiV1TracesBodyTracesItemSdk

        sdk = PostApiV1TracesBodyTracesItemSdk(name="python", version="1.0.0")

        assert sdk.name == "python"
        assert sdk.version == "1.0.0"

    def test_create_trace_span_model(self):
        """Test creating trace span model"""
        from noveum_api_client.models import (
            PostApiV1TracesBodyTracesItemSpansItem,
            PostApiV1TracesBodyTracesItemSpansItemAttributes,
            PostApiV1TracesBodyTracesItemSpansItemStatus,
        )

        attributes = PostApiV1TracesBodyTracesItemSpansItemAttributes()
        status = PostApiV1TracesBodyTracesItemSpansItemStatus.OK

        span = PostApiV1TracesBodyTracesItemSpansItem(
            span_id="span-123",
            trace_id="trace-456",
            name="test_span",
            start_time="2024-01-01T00:00:00Z",
            end_time="2024-01-01T00:00:01Z",
            duration_ms=1000.0,
            status=status,
            attributes=attributes,
        )

        assert span.span_id == "span-123"
        assert span.trace_id == "trace-456"
        assert span.name == "test_span"
        assert span.duration_ms == 1000.0

    def test_create_trace_with_spans(self):
        """Test creating complete trace with spans"""
        from noveum_api_client.models import (
            PostApiV1TracesBodyTracesItem,
            PostApiV1TracesBodyTracesItemSdk,
            PostApiV1TracesBodyTracesItemSpansItem,
            PostApiV1TracesBodyTracesItemSpansItemAttributes,
            PostApiV1TracesBodyTracesItemSpansItemStatus,
            PostApiV1TracesBodyTracesItemStatus,
        )

        # Create SDK
        sdk = PostApiV1TracesBodyTracesItemSdk(name="python", version="1.0.0")

        # Create span
        span_attributes = PostApiV1TracesBodyTracesItemSpansItemAttributes()
        span_status = PostApiV1TracesBodyTracesItemSpansItemStatus.OK
        span = PostApiV1TracesBodyTracesItemSpansItem(
            span_id="span-123",
            trace_id="trace-456",
            name="test_span",
            start_time="2024-01-01T00:00:00Z",
            end_time="2024-01-01T00:00:01Z",
            duration_ms=1000.0,
            status=span_status,
            attributes=span_attributes,
        )

        # Create trace
        status = PostApiV1TracesBodyTracesItemStatus.OK

        trace = PostApiV1TracesBodyTracesItem(
            name="test_trace",
            start_time="2024-01-01T00:00:00Z",
            end_time="2024-01-01T00:00:01Z",
            duration_ms=1000.0,
            status=status,
            span_count=1,
            project="test-project",
            sdk=sdk,
            spans=[span],
        )

        assert trace.name == "test_trace"
        assert trace.span_count == 1
        assert len(trace.spans) == 1
        assert trace.spans[0].span_id == "span-123"

    def test_trace_to_dict_with_nested_spans(self):
        """Test serializing trace with nested spans to dict"""
        from noveum_api_client.models import (
            PostApiV1TracesBodyTracesItem,
            PostApiV1TracesBodyTracesItemSdk,
            PostApiV1TracesBodyTracesItemSpansItem,
            PostApiV1TracesBodyTracesItemSpansItemAttributes,
            PostApiV1TracesBodyTracesItemSpansItemStatus,
            PostApiV1TracesBodyTracesItemStatus,
        )

        sdk = PostApiV1TracesBodyTracesItemSdk(name="python", version="1.0.0")
        span_attributes = PostApiV1TracesBodyTracesItemSpansItemAttributes()
        span_status = PostApiV1TracesBodyTracesItemSpansItemStatus.OK
        span = PostApiV1TracesBodyTracesItemSpansItem(
            span_id="span-123",
            trace_id="trace-456",
            name="test_span",
            start_time="2024-01-01T00:00:00Z",
            end_time="2024-01-01T00:00:01Z",
            duration_ms=1000.0,
            status=span_status,
            attributes=span_attributes,
        )

        status = PostApiV1TracesBodyTracesItemStatus.OK
        trace = PostApiV1TracesBodyTracesItem(
            name="test_trace",
            start_time="2024-01-01T00:00:00Z",
            end_time="2024-01-01T00:00:01Z",
            duration_ms=1000.0,
            status=status,
            span_count=1,
            project="test-project",
            sdk=sdk,
            spans=[span],
        )

        trace_dict = trace.to_dict()

        assert isinstance(trace_dict, dict)
        assert trace_dict["name"] == "test_trace"
        assert len(trace_dict["spans"]) == 1
        assert trace_dict["spans"][0]["span_id"] == "span-123"
        assert trace_dict["sdk"]["name"] == "python"

    def test_trace_body_with_multiple_traces(self):
        """Test creating trace body with multiple traces"""
        from noveum_api_client.models import (
            PostApiV1TracesBody,
            PostApiV1TracesBodyTracesItem,
            PostApiV1TracesBodyTracesItemSdk,
            PostApiV1TracesBodyTracesItemStatus,
        )

        traces = []
        for i in range(3):
            sdk = PostApiV1TracesBodyTracesItemSdk(name="python", version="1.0.0")
            status = PostApiV1TracesBodyTracesItemStatus.OK

            trace = PostApiV1TracesBodyTracesItem(
                name=f"test_trace_{i}",
                start_time="2024-01-01T00:00:00Z",
                end_time="2024-01-01T00:00:01Z",
                duration_ms=1000.0,
                status=status,
                span_count=0,
                project="test-project",
                sdk=sdk,
                spans=[],
            )
            traces.append(trace)

        body = PostApiV1TracesBody(traces=traces)

        assert len(body.traces) == 3
        assert body.traces[0].name == "test_trace_0"
        assert body.traces[2].name == "test_trace_2"


class TestScorerModels:
    """Test scorer-related models"""

    def test_create_scorer_body(self):
        """Test creating scorer body"""
        from noveum_api_client.models import PostApiV1ScorersBody

        body = PostApiV1ScorersBody(
            name="Test Scorer",
            description="A test scorer",
            type_="llm_judge",
            tag="v1",
            config={"model": "gpt-4", "temperature": 0.7},
        )

        assert body.name == "Test Scorer"
        assert body.description == "A test scorer"
        assert body.type_ == "llm_judge"
        assert body.tag == "v1"
        assert body.config["model"] == "gpt-4"

    def test_scorer_body_to_dict(self):
        """Test serializing scorer body to dict"""
        from noveum_api_client.models import PostApiV1ScorersBody

        body = PostApiV1ScorersBody(
            name="Test Scorer", description="A test scorer", type_="llm_judge", tag="v1", config={"model": "gpt-4"}
        )

        body_dict = body.to_dict()

        assert isinstance(body_dict, dict)
        assert body_dict["name"] == "Test Scorer"
        assert body_dict["type"] == "llm_judge"
        assert body_dict["tag"] == "v1"
        assert body_dict["config"]["model"] == "gpt-4"

    def test_create_scorer_result_item(self):
        """Test creating scorer result item"""
        from noveum_api_client.models import (
            PostApiV1ScorersResultsBatchBodyResultsItem,
            PostApiV1ScorersResultsBatchBodyResultsItemMetadata,
        )

        metadata = PostApiV1ScorersResultsBatchBodyResultsItemMetadata()

        result = PostApiV1ScorersResultsBatchBodyResultsItem(
            dataset_slug="test-dataset", item_id="item-1", scorer_id="scorer-1", score=0.95, metadata=metadata
        )

        assert result.dataset_slug == "test-dataset"
        assert result.item_id == "item-1"
        assert result.scorer_id == "scorer-1"
        assert result.score == 0.95

    def test_scorer_result_batch_body(self):
        """Test creating scorer result batch body"""
        from noveum_api_client.models import (
            PostApiV1ScorersResultsBatchBody,
            PostApiV1ScorersResultsBatchBodyResultsItem,
            PostApiV1ScorersResultsBatchBodyResultsItemMetadata,
        )

        results = []
        for i in range(5):
            metadata = PostApiV1ScorersResultsBatchBodyResultsItemMetadata()
            result = PostApiV1ScorersResultsBatchBodyResultsItem(
                dataset_slug="test-dataset",
                item_id=f"item-{i}",
                scorer_id="scorer-1",
                score=0.8 + (i * 0.04),
                metadata=metadata,
            )
            results.append(result)

        body = PostApiV1ScorersResultsBatchBody(results=results)

        assert len(body.results) == 5
        assert body.results[0].score == 0.8
        assert abs(body.results[4].score - 0.96) < 0.001  # Approximate comparison for floats

    def test_scorer_result_to_dict(self):
        """Test serializing scorer result to dict"""
        from noveum_api_client.models import (
            PostApiV1ScorersResultsBatchBodyResultsItem,
            PostApiV1ScorersResultsBatchBodyResultsItemMetadata,
        )

        metadata = PostApiV1ScorersResultsBatchBodyResultsItemMetadata()
        result = PostApiV1ScorersResultsBatchBodyResultsItem(
            dataset_slug="test-dataset",
            item_id="item-1",
            scorer_id="scorer-1",
            score=0.95,
            passed=True,
            metadata=metadata,
            error="",
            execution_time_ms=123.45,
        )

        result_dict = result.to_dict()

        assert isinstance(result_dict, dict)
        assert result_dict["datasetSlug"] == "test-dataset"
        assert result_dict["itemId"] == "item-1"
        assert result_dict["scorerId"] == "scorer-1"
        assert result_dict["score"] == 0.95
        assert result_dict["passed"] is True
        assert result_dict["executionTimeMs"] == 123.45
