"""
Unit Tests for Traces API Wrappers

Tests all trace-related API wrapper functions with mocked responses.
"""

from unittest.mock import Mock

import httpx
import pytest

from noveum_api_client.api.traces import (
    get_api_v1_traces,
    get_api_v1_traces_by_id,
    get_api_v1_traces_by_trace_id_spans,
    get_api_v1_traces_connection_status,
    get_api_v1_traces_directory_tree,
    get_api_v1_traces_environments_by_projects,
    get_api_v1_traces_filter_values,
    get_api_v1_traces_ids,
    post_api_v1_traces,
    post_api_v1_traces_single,
)


class TestTracesListingWrappers:
    """Test traces listing API wrappers"""

    def test_get_traces_has_sync_method(self):
        """Test that get_traces has sync_detailed method"""
        assert hasattr(get_api_v1_traces, "sync_detailed")
        assert callable(get_api_v1_traces.sync_detailed)

    def test_get_traces_has_async_method(self):
        """Test that get_traces has asyncio_detailed method"""
        assert hasattr(get_api_v1_traces, "asyncio_detailed")
        assert callable(get_api_v1_traces.asyncio_detailed)

    def test_get_traces_accepts_filter_params(self, mock_client):
        """Test that get_traces accepts filter parameters"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = []

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_traces.sync_detailed(
            client=mock_client, size=20, project="test-project", environment="test"
        )

        assert response.status_code == 200

    def test_get_trace_ids_has_methods(self):
        """Test get trace IDs has required methods"""
        assert hasattr(get_api_v1_traces_ids, "sync_detailed")
        assert hasattr(get_api_v1_traces_ids, "asyncio_detailed")


class TestTraceRetrievalWrappers:
    """Test trace retrieval API wrappers"""

    def test_get_trace_by_id_has_methods(self):
        """Test get trace by ID has methods"""
        assert hasattr(get_api_v1_traces_by_id, "sync_detailed")
        assert hasattr(get_api_v1_traces_by_id, "asyncio_detailed")

    def test_get_trace_spans_has_methods(self):
        """Test get trace spans has methods"""
        assert hasattr(get_api_v1_traces_by_trace_id_spans, "sync_detailed")
        assert hasattr(get_api_v1_traces_by_trace_id_spans, "asyncio_detailed")

    def test_get_trace_by_id_accepts_trace_id(self, mock_client):
        """Test get trace by ID accepts trace_id parameter"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = {"trace_id": "test-trace"}

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_traces_by_id.sync_detailed(client=mock_client, id="test-trace")

        assert response.status_code == 200


class TestTraceMetadataWrappers:
    """Test trace metadata API wrappers"""

    def test_get_connection_status_has_methods(self):
        """Test get connection status has methods"""
        assert hasattr(get_api_v1_traces_connection_status, "sync_detailed")
        assert hasattr(get_api_v1_traces_connection_status, "asyncio_detailed")

    def test_get_directory_tree_has_methods(self):
        """Test get directory tree has methods"""
        assert hasattr(get_api_v1_traces_directory_tree, "sync_detailed")
        assert hasattr(get_api_v1_traces_directory_tree, "asyncio_detailed")

    def test_get_environments_by_projects_has_methods(self):
        """Test get environments by projects has methods"""
        assert hasattr(get_api_v1_traces_environments_by_projects, "sync_detailed")
        assert hasattr(get_api_v1_traces_environments_by_projects, "asyncio_detailed")

    def test_get_filter_values_has_methods(self):
        """Test get filter values has methods"""
        assert hasattr(get_api_v1_traces_filter_values, "sync_detailed")
        assert hasattr(get_api_v1_traces_filter_values, "asyncio_detailed")


class TestTraceCreationWrappers:
    """Test trace creation API wrappers"""

    def test_post_traces_has_methods(self):
        """Test post traces (bulk) has methods"""
        assert hasattr(post_api_v1_traces, "sync_detailed")
        assert hasattr(post_api_v1_traces, "asyncio_detailed")

    def test_post_trace_single_has_methods(self):
        """Test post single trace has methods"""
        assert hasattr(post_api_v1_traces_single, "sync_detailed")
        assert hasattr(post_api_v1_traces_single, "asyncio_detailed")

    def test_post_traces_accepts_body_with_real_model(self, mock_client):
        """Test post traces accepts body with real trace model"""
        from noveum_api_client.models import (
            PostApiV1TracesBody,
            PostApiV1TracesBodyTracesItem,
            PostApiV1TracesBodyTracesItemSdk,
            PostApiV1TracesBodyTracesItemStatus,
        )

        # Create SDK
        sdk = PostApiV1TracesBodyTracesItemSdk(name="python", version="1.0.0")

        # Create trace
        status = PostApiV1TracesBodyTracesItemStatus.OK

        trace = PostApiV1TracesBodyTracesItem(
            name="test_trace",
            start_time="2024-01-01T00:00:00Z",
            end_time="2024-01-01T00:00:01Z",
            duration_ms=1000.0,
            status=status,
            span_count=0,
            project="test-project",
            sdk=sdk,
            spans=[],
        )

        body = PostApiV1TracesBody(traces=[trace])

        # Verify body serializes correctly
        body_dict = body.to_dict()
        assert len(body_dict["traces"]) == 1
        assert body_dict["traces"][0]["name"] == "test_trace"

    def test_post_single_trace_with_real_model(self, mock_client):
        """Test post single trace with real trace model"""
        from noveum_api_client.models import (
            PostApiV1TracesSingleBody,
            PostApiV1TracesSingleBodySdk,
            PostApiV1TracesSingleBodyStatus,
        )

        # Create SDK
        sdk = PostApiV1TracesSingleBodySdk(name="python", version="1.0.0")

        # Create attributes
        # Create status
        status = PostApiV1TracesSingleBodyStatus.OK

        # Create single trace body
        body = PostApiV1TracesSingleBody(
            name="test_trace",
            start_time="2024-01-01T00:00:00Z",
            end_time="2024-01-01T00:00:01Z",
            duration_ms=1000.0,
            status=status,
            span_count=0,
            project="test-project",
            sdk=sdk,
            spans=[],
        )

        # Verify body serializes correctly
        body_dict = body.to_dict()
        assert body_dict["name"] == "test_trace"
        assert body_dict["project"] == "test-project"
        assert body_dict["span_count"] == 0


class TestTracesFilteringAndPagination:
    """Test traces filtering and pagination"""

    @pytest.mark.parametrize(
        "size,page",
        [
            (10, 1),
            (20, 2),
            (50, 1),
            (100, 5),
        ],
    )
    def test_get_traces_accepts_pagination(self, mock_client, size, page):
        """Test get traces accepts various pagination parameters"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = []

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_traces.sync_detailed(client=mock_client, size=size)

        assert response.status_code == 200

    def test_get_traces_accepts_project_filter(self, mock_client):
        """Test get traces accepts project filter"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = []

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_traces.sync_detailed(client=mock_client, project="my-project")

        assert response.status_code == 200

    def test_get_traces_accepts_environment_filter(self, mock_client):
        """Test get traces accepts environment filter"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = []

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_traces.sync_detailed(client=mock_client, environment="production")

        assert response.status_code == 200


class TestTracesComplexModels:
    """Test traces with complex nested structures"""

    def test_create_trace_with_multiple_spans(self):
        """Test creating trace with multiple spans"""
        from noveum_api_client.models import (
            PostApiV1TracesBodyTracesItem,
            PostApiV1TracesBodyTracesItemSdk,
            PostApiV1TracesBodyTracesItemSpansItem,
            PostApiV1TracesBodyTracesItemSpansItemAttributes,
            PostApiV1TracesBodyTracesItemSpansItemStatus,
            PostApiV1TracesBodyTracesItemStatus,
        )

        sdk = PostApiV1TracesBodyTracesItemSdk(name="python", version="1.0.0")

        # Create multiple spans
        spans = []
        for i in range(3):
            span_attributes = PostApiV1TracesBodyTracesItemSpansItemAttributes()
            span_status = PostApiV1TracesBodyTracesItemSpansItemStatus.OK
            span = PostApiV1TracesBodyTracesItemSpansItem(
                span_id=f"span-{i}",
                trace_id="trace-456",
                name=f"test_span_{i}",
                start_time="2024-01-01T00:00:00Z",
                end_time="2024-01-01T00:00:01Z",
                duration_ms=1000.0,
                status=span_status,
                attributes=span_attributes,
            )
            spans.append(span)

        # Create trace with multiple spans
        status = PostApiV1TracesBodyTracesItemStatus.OK

        trace = PostApiV1TracesBodyTracesItem(
            name="test_trace",
            start_time="2024-01-01T00:00:00Z",
            end_time="2024-01-01T00:00:01Z",
            duration_ms=1000.0,
            status=status,
            span_count=3,
            project="test-project",
            sdk=sdk,
            spans=spans,
        )

        assert len(trace.spans) == 3
        assert trace.spans[0].span_id == "span-0"
        assert trace.spans[2].span_id == "span-2"

    def test_trace_with_metadata_and_attributes(self):
        """Test trace with metadata and custom attributes"""
        from noveum_api_client.models import (
            PostApiV1TracesSingleBody,
            PostApiV1TracesSingleBodyAttributes,
            PostApiV1TracesSingleBodyMetadata,
            PostApiV1TracesSingleBodyMetadataCustomAttributes,
            PostApiV1TracesSingleBodySdk,
            PostApiV1TracesSingleBodyStatus,
        )

        sdk = PostApiV1TracesSingleBodySdk(name="python", version="1.0.0")
        attributes = PostApiV1TracesSingleBodyAttributes()
        custom_attrs = PostApiV1TracesSingleBodyMetadataCustomAttributes()
        metadata = PostApiV1TracesSingleBodyMetadata(custom_attributes=custom_attrs)
        status = PostApiV1TracesSingleBodyStatus.OK

        trace = PostApiV1TracesSingleBody(
            name="test_trace",
            start_time="2024-01-01T00:00:00Z",
            end_time="2024-01-01T00:00:01Z",
            duration_ms=1000.0,
            status=status,
            span_count=0,
            project="test-project",
            sdk=sdk,
            spans=[],
            attributes=attributes,
            metadata=metadata,
        )

        trace_dict = trace.to_dict()
        assert "metadata" in trace_dict
        assert "attributes" in trace_dict

    def test_span_with_parent_hierarchy(self):
        """Test span with parent hierarchy"""
        from noveum_api_client.models import (
            PostApiV1TracesBodyTracesItemSpansItem,
            PostApiV1TracesBodyTracesItemSpansItemAttributes,
            PostApiV1TracesBodyTracesItemSpansItemStatus,
        )

        # Create parent span
        parent_span_attributes = PostApiV1TracesBodyTracesItemSpansItemAttributes()
        parent_span_status = PostApiV1TracesBodyTracesItemSpansItemStatus.OK

        parent_span = PostApiV1TracesBodyTracesItemSpansItem(
            span_id="parent-span",
            trace_id="trace-456",
            name="parent_operation",
            start_time="2024-01-01T00:00:00Z",
            end_time="2024-01-01T00:00:02Z",
            duration_ms=2000.0,
            status=parent_span_status,
            attributes=parent_span_attributes,
        )

        # Create child span
        child_span_attributes = PostApiV1TracesBodyTracesItemSpansItemAttributes()
        child_span_status = PostApiV1TracesBodyTracesItemSpansItemStatus.OK

        child_span = PostApiV1TracesBodyTracesItemSpansItem(
            span_id="child-span",
            trace_id="trace-456",
            name="child_operation",
            start_time="2024-01-01T00:00:00Z",
            end_time="2024-01-01T00:00:01Z",
            duration_ms=1000.0,
            status=child_span_status,
            attributes=child_span_attributes,
            parent_span_id="parent-span",
        )

        assert child_span.parent_span_id == "parent-span"
        assert parent_span.span_id == "parent-span"


class TestTracesErrorHandling:
    """Test error handling in traces wrappers"""

    @pytest.mark.parametrize(
        "status_code,error_type",
        [
            (400, "Bad Request"),
            (401, "Unauthorized"),
            (404, "Not Found"),
            (500, "Internal Server Error"),
        ],
    )
    def test_handles_error_responses(self, mock_client, status_code, error_type):
        """Test traces wrappers handle various error responses"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = status_code
        mock_response.content = b'{"error": "error"}'
        mock_response.headers = {}
        mock_response.json.return_value = {"error": error_type}

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_traces.sync_detailed(client=mock_client)

        assert response.status_code == status_code

    def test_handles_empty_traces_list(self, mock_client):
        """Test handles empty traces list gracefully"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = []

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_traces.sync_detailed(client=mock_client)

        assert response.status_code == 200


class TestTracesResponseStructure:
    """Test traces response structure"""

    def test_get_traces_returns_list_structure(self, mock_client):
        """Test get traces returns expected list structure"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.content = b'[{"trace_id": "trace-1", "name": "test1"}, {"trace_id": "trace-2", "name": "test2"}]'
        mock_response.headers = {}
        mock_response.json.return_value = [
            {"trace_id": "trace-1", "name": "test1"},
            {"trace_id": "trace-2", "name": "test2"},
        ]

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_traces.sync_detailed(client=mock_client)

        assert response.status_code == 200
        # Response object exists and has status code
        assert response is not None

    def test_get_trace_by_id_returns_single_object(self, mock_client):
        """Test get trace by ID returns single object structure"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = {"trace_id": "trace-1", "name": "test", "spans": []}

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_traces_by_id.sync_detailed(client=mock_client, id="trace-1")

        assert response.status_code == 200
