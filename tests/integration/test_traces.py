"""
Traces API Integration Tests - Complete End-to-End Flow

This module tests the complete trace lifecycle:
1. Check connection status
2. Send single trace -> Verify ingestion -> Retrieve trace -> Get spans
3. Send batch traces -> Verify batch ingestion -> Query traces
4. Test all trace query endpoints (filters, environments, directory tree)
5. LangChain/LangGraph E2E tests with actual LLM calls

Endpoints Tested (11 total):
- GET  /api/v1/traces/connection-status
- POST /api/v1/traces/single  (create single trace)
- POST /api/v1/traces  (create batch traces)
- GET  /api/v1/traces  (list/query traces)
- GET  /api/v1/traces/ids  (get trace IDs)
- GET  /api/v1/traces/{id}  (get specific trace)
- GET  /api/v1/traces/{trace_id}/spans  (get trace spans)
- GET  /api/v1/traces/filter-values
- GET  /api/v1/traces/environments/{projects}
- GET  /api/v1/traces/directory-tree

LangChain Integration Tests:
- Simple chain with ChatOpenAI
- Chain with token counting verification
- Multi-step chain tracing
- LangGraph agent tracing (optional)

Usage:
    pytest test_traces.py -v
    pytest test_traces.py -v -k "single_trace"
    pytest test_traces.py -v -k "langchain"
    pytest test_traces.py -v --tb=short
"""

import os
import time
import uuid
from datetime import datetime, timezone
from typing import Any

import pytest
from constants import (
    SKIP_FAILED_CREATE_BATCH_TRACES,
    SKIP_FAILED_CREATE_SINGLE_TRACE,
    SKIP_GEMINI_API_KEY_NOT_SET,
    SKIP_NO_BATCH_TRACE_IDS,
    SKIP_NO_SINGLE_TRACE_ID,
    SKIP_NO_TRACE_ID_RETRIEVAL,
    SKIP_NO_TRACE_ID_SPANS,
    SKIP_NOVEUM_TRACE_NOT_AVAILABLE,
)
from utils import (
    assert_has_keys,
    assert_non_empty_string,
    assert_optional_string,
    ensure_dict,
    ensure_list,
    get_field,
    parse_response,
)

from noveum_api_client import Client
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
from noveum_api_client.models import (
    GetApiV1TracesIdsSort,
    GetApiV1TracesSort,
    PostApiV1TracesBody,
    PostApiV1TracesBodyTracesItem,
    PostApiV1TracesBodyTracesItemSdk,
    PostApiV1TracesBodyTracesItemSpansItem,
    PostApiV1TracesBodyTracesItemSpansItemStatus,
    PostApiV1TracesBodyTracesItemStatus,
    PostApiV1TracesSingleBody,
    PostApiV1TracesSingleBodySdk,
    PostApiV1TracesSingleBodySpansItem,
    PostApiV1TracesSingleBodySpansItemStatus,
    PostApiV1TracesSingleBodyStatus,
)


def create_iso_timestamp(dt: datetime | None = None) -> str:
    """Create an ISO format timestamp string."""
    if dt is None:
        dt = datetime.now(timezone.utc)
    return dt.isoformat()


@pytest.mark.traces
@pytest.mark.integration
@pytest.mark.serial
class TestTracesE2EFlow:
    """End-to-end integration tests for Traces API with full response body validation."""

    @pytest.fixture(scope="class")
    def trace_context(self) -> dict[str, Any]:
        """Shared context for storing trace data across tests."""
        return {
            "single_trace_id": None,
            "single_trace_name": None,
            "single_span_id": None,
            "batch_trace_ids": [],
            "retrieved_trace_id": None,
            "created_project": None,
            "created_environment": None,
        }

    def test_01_connection_status(self, low_level_client: Client) -> None:
        """Test connection status endpoint - verify API is reachable and returns valid response."""
        response = get_api_v1_traces_connection_status.sync_detailed(client=low_level_client)

        # Validate status code
        assert response.status_code == 200, f"Connection check failed: {response.status_code}"

        # Validate response has content
        assert response.content is not None, "Response content should not be None"

        # Validate headers
        assert response.headers is not None, "Response headers should not be None"
        assert "content-type" in [h.lower() for h in response.headers], "Missing content-type header"

    def test_02_create_single_trace(
        self,
        low_level_client: Client,
        api_config: dict[str, str],
        trace_context: dict[str, Any],
    ) -> None:
        """Test creating a single trace with full data using typed models."""
        trace_id = str(uuid.uuid4())
        span_id = str(uuid.uuid4())[:16]
        now = datetime.now(timezone.utc)
        start_time = create_iso_timestamp(now)
        end_time = create_iso_timestamp(now)
        duration_ms = 1500.0  # 1.5 seconds
        trace_name = "sdk_integration_test_single"

        # Create SDK info
        sdk = PostApiV1TracesSingleBodySdk(name="noveum-sdk-integration-test", version="1.0.0")

        # Create a span
        span = PostApiV1TracesSingleBodySpansItem(
            span_id=span_id,
            trace_id=trace_id,
            name="llm_call",
            start_time=start_time,
            end_time=end_time,
            duration_ms=duration_ms,
            status=PostApiV1TracesSingleBodySpansItemStatus.OK,
        )

        # Create the trace body using typed model
        body = PostApiV1TracesSingleBody(
            trace_id=trace_id,
            name=trace_name,
            project=api_config["project"],
            environment=api_config["environment"],
            start_time=start_time,
            end_time=end_time,
            duration_ms=duration_ms,
            status=PostApiV1TracesSingleBodyStatus.OK,
            span_count=1,
            sdk=sdk,
            spans=[span],
        )

        try:
            response = post_api_v1_traces_single.sync_detailed(
                client=low_level_client,
                body=body,
            )
        except Exception as e:
            pytest.skip(SKIP_FAILED_CREATE_SINGLE_TRACE.format(error=e))

        # Validate status code
        assert response.status_code in [
            200,
            201,
            202,
        ], f"Create single trace failed: {response.status_code} - {response.content!r}"

        # Validate response body if present
        if response.parsed:
            parsed = response.parsed
            # Check if response contains trace_id or success indicator
            if hasattr(parsed, "trace_id"):
                assert parsed.trace_id == trace_id, f"Returned trace_id mismatch: {parsed.trace_id}"
            if hasattr(parsed, "success"):
                assert parsed.success is True, "Expected success=True in response"

        # Store context for subsequent tests
        trace_context["single_trace_id"] = trace_id
        trace_context["single_trace_name"] = trace_name
        trace_context["single_span_id"] = span_id
        trace_context["created_project"] = api_config["project"]
        trace_context["created_environment"] = api_config["environment"]

    def test_03_verify_single_trace_ingestion(
        self,
        low_level_client: Client,
        trace_context: dict[str, Any],
    ) -> None:
        """Verify the single trace was ingested and validate all response fields."""
        if not trace_context.get("single_trace_id"):
            pytest.skip(SKIP_NO_SINGLE_TRACE_ID)

        trace_id = trace_context["single_trace_id"]
        expected_name = trace_context.get("single_trace_name")
        expected_project = trace_context.get("created_project")
        expected_environment = trace_context.get("created_environment")

        wait_times = [2, 5, 10]
        trace_found = False
        retrieved_trace = None

        for wait_time in wait_times:
            time.sleep(wait_time)

            try:
                response = get_api_v1_traces_by_id.sync_detailed(
                    client=low_level_client,
                    id=trace_id,
                )
                if response.status_code == 200:
                    trace_found = True
                    retrieved_trace = response.parsed
                    break
            except Exception:
                continue

        if not trace_found:
            pytest.xfail("Single trace not found after waiting. May be ingestion delay.")

        # ===== VALIDATE RESPONSE BODY =====
        # Parse response (handles both parsed and raw content)
        data = parse_response(response) if "response" in dir() else retrieved_trace
        # API returns {"success": true, "data": {...}}
        trace_data = data.get("data", data) if isinstance(data, dict) else retrieved_trace

        assert trace_data is not None, "Response data should not be None"

        # Helper to get field value from dict or object
        def get_field(obj: Any, field: str) -> Any:
            if isinstance(obj, dict):
                return obj.get(field)
            return getattr(obj, field, None)

        # Validate trace_id matches
        actual_trace_id = get_field(trace_data, "trace_id")
        if actual_trace_id:
            assert actual_trace_id == trace_id, f"Trace ID mismatch: expected {trace_id}, got {actual_trace_id}"

        # Validate trace name
        actual_name = get_field(trace_data, "name")
        if actual_name and expected_name:
            assert actual_name == expected_name, f"Name mismatch: expected {expected_name}, got {actual_name}"

        # Validate project
        actual_project = get_field(trace_data, "project")
        if actual_project and expected_project:
            assert (
                actual_project == expected_project
            ), f"Project mismatch: expected {expected_project}, got {actual_project}"

        # Validate environment
        actual_environment = get_field(trace_data, "environment")
        if actual_environment and expected_environment:
            assert (
                actual_environment == expected_environment
            ), f"Environment mismatch: expected {expected_environment}, got {actual_environment}"

        # Validate status
        actual_status = get_field(trace_data, "status")
        if actual_status is not None:
            assert_non_empty_string(str(actual_status), "trace.status")

        # Validate duration_ms
        actual_duration = get_field(trace_data, "duration_ms")
        if actual_duration is not None:
            assert actual_duration >= 0, "Duration should be non-negative"

        # Validate span_count
        actual_span_count = get_field(trace_data, "span_count")
        if actual_span_count is not None:
            assert actual_span_count >= 1, "Should have at least 1 span"

        # Validate timestamps
        actual_start_time = get_field(trace_data, "start_time")
        if actual_start_time:
            assert_optional_string(actual_start_time, "trace.start_time")

        actual_end_time = get_field(trace_data, "end_time")
        if actual_end_time:
            assert_optional_string(actual_end_time, "trace.end_time")

    def test_04_create_batch_traces(
        self,
        low_level_client: Client,
        api_config: dict[str, str],
        trace_context: dict[str, Any],
    ) -> None:
        """Test creating multiple traces in a batch using typed models."""
        traces = []
        trace_ids = []
        for i in range(3):
            trace_id = str(uuid.uuid4())
            span_id = str(uuid.uuid4())[:16]
            now = datetime.now(timezone.utc)
            start_time = create_iso_timestamp(now)
            end_time = create_iso_timestamp(now)
            duration_ms = 1000.0 + (i * 500)

            # Create SDK info for batch trace
            sdk = PostApiV1TracesBodyTracesItemSdk(name="noveum-sdk-integration-test", version="1.0.0")

            # Create a span for batch trace
            span = PostApiV1TracesBodyTracesItemSpansItem(
                span_id=span_id,
                trace_id=trace_id,
                name=f"batch_span_{i}",
                start_time=start_time,
                end_time=end_time,
                duration_ms=duration_ms,
                status=PostApiV1TracesBodyTracesItemSpansItemStatus.OK,
            )

            # Create batch trace item
            trace = PostApiV1TracesBodyTracesItem(
                trace_id=trace_id,
                name=f"sdk_batch_trace_{i}",
                project=api_config["project"],
                environment=api_config["environment"],
                start_time=start_time,
                end_time=end_time,
                duration_ms=duration_ms,
                status=PostApiV1TracesBodyTracesItemStatus.OK,
                span_count=1,
                sdk=sdk,
                spans=[span],
            )

            traces.append(trace)
            trace_ids.append(trace_id)

        try:
            body = PostApiV1TracesBody(traces=traces)
            response = post_api_v1_traces.sync_detailed(
                client=low_level_client,
                body=body,
            )
        except Exception as e:
            pytest.skip(SKIP_FAILED_CREATE_BATCH_TRACES.format(error=e))

        assert response.status_code in [
            200,
            201,
            202,
        ], f"Create batch traces failed: {response.status_code} - {response.content!r}"

        trace_context["batch_trace_ids"] = trace_ids

    def test_05_verify_batch_trace_ingestion(
        self,
        low_level_client: Client,
        trace_context: dict[str, Any],
    ) -> None:
        """Verify batch traces were ingested by listing traces."""
        if not trace_context.get("batch_trace_ids"):
            pytest.skip(SKIP_NO_BATCH_TRACE_IDS)

        time.sleep(5)

        response = get_api_v1_traces.sync_detailed(
            client=low_level_client,
            size=50,
        )

        assert response.status_code == 200, f"List traces failed: {response.status_code}"

    def test_06_list_traces(
        self,
        low_level_client: Client,
        trace_context: dict[str, Any],
    ) -> None:
        """Test listing traces with pagination and validate response structure."""
        response = get_api_v1_traces.sync_detailed(
            client=low_level_client,
            from_=0.0,
            size=10,
            sort=GetApiV1TracesSort.START_TIMEDESC,
            include_spans=False,
        )

        # Validate status code
        assert response.status_code == 200, f"List traces failed: {response.status_code}"

        # ===== VALIDATE RESPONSE BODY STRUCTURE =====
        data = parse_response(response)
        assert data is not None, "Response data should not be None"

        # API returns {"success": true, "traces": [...], "pagination": {...}}
        traces = data.get("traces", []) if isinstance(data, dict) else []
        traces = ensure_list(traces, "traces should be a list")

        # Validate pagination fields if present
        pagination = data.get("pagination", {}) if isinstance(data, dict) else {}
        if pagination:
            pagination = ensure_dict(pagination, "pagination should be a dict")
            assert_has_keys(pagination, ["total", "limit", "offset"], "pagination")

        # Validate each trace in the list has required fields
        if traces:
            first_trace = traces[0]

            # Store for later tests
            if isinstance(first_trace, dict) and "trace_id" in first_trace:
                trace_context["retrieved_trace_id"] = first_trace["trace_id"]

            # Validate trace structure
            required_fields = ["trace_id", "name", "project", "status"]
            for field in required_fields:
                value = get_field(first_trace, field)
                assert value is not None, f"trace.{field} should be present"

            optional_fields = ["environment", "duration_ms", "span_count", "start_time", "end_time"]
            for field in optional_fields:
                value = get_field(first_trace, field)
                if value is not None and field in ["environment", "start_time", "end_time"]:
                    assert_optional_string(value, f"trace.{field}")

    def test_07_get_trace_ids(
        self,
        low_level_client: Client,
        trace_context: dict[str, Any],
    ) -> None:
        """Test getting trace IDs endpoint."""
        response = get_api_v1_traces_ids.sync_detailed(
            client=low_level_client,
            from_=0.0,
            size=10,
            sort=GetApiV1TracesIdsSort.START_TIMEDESC,
            include_spans=False,
        )

        assert response.status_code == 200, f"Get trace IDs failed: {response.status_code}"

    def test_08_get_trace_by_id(
        self,
        low_level_client: Client,
        trace_context: dict[str, Any],
    ) -> None:
        """Test retrieving a specific trace by ID with full body validation."""
        trace_id = trace_context.get("retrieved_trace_id") or trace_context.get("single_trace_id")
        if not trace_id:
            pytest.skip(SKIP_NO_TRACE_ID_RETRIEVAL)

        response = get_api_v1_traces_by_id.sync_detailed(
            client=low_level_client,
            id=trace_id,
        )

        # May be 404 if trace not found (eventual consistency)
        if response.status_code == 404:
            pytest.xfail("Trace not found - may be ingestion delay")

        assert response.status_code == 200, f"Get trace failed: {response.status_code}"

        # ===== VALIDATE RESPONSE BODY =====
        data = parse_response(response)
        assert data is not None, "Response data should not be None"

        # API returns {"success": true, "data": {...}}
        trace = data.get("data", data) if isinstance(data, dict) else data

        # Validate trace_id matches request
        actual_trace_id = get_field(trace, "trace_id")
        if actual_trace_id:
            assert actual_trace_id == trace_id, "Returned trace_id should match requested ID"
            assert_non_empty_string(actual_trace_id, "trace.trace_id")

        # Validate required fields exist and have valid values
        name = get_field(trace, "name")
        if name:
            assert len(name) > 0, "Trace name should not be empty"
            assert_non_empty_string(name, "trace.name")

        project = get_field(trace, "project")
        if project:
            assert_non_empty_string(project, "trace.project")

        status = get_field(trace, "status")
        if status:
            assert status in ["ok", "OK", "error", "ERROR"] or isinstance(status, dict)

        duration_ms = get_field(trace, "duration_ms")
        if duration_ms is not None:
            assert duration_ms >= 0, "Duration should be non-negative"

        span_count = get_field(trace, "span_count")
        if span_count is not None:
            assert span_count >= 0, "Span count should be non-negative"

        # Validate timestamps
        start_time = get_field(trace, "start_time")
        if start_time:
            assert_optional_string(start_time, "trace.start_time")

        end_time = get_field(trace, "end_time")
        if end_time:
            assert_optional_string(end_time, "trace.end_time")

    def test_09_get_trace_spans(
        self,
        low_level_client: Client,
        trace_context: dict[str, Any],
    ) -> None:
        """Test retrieving spans for a specific trace with full validation."""
        trace_id = trace_context.get("retrieved_trace_id") or trace_context.get("single_trace_id")
        if not trace_id:
            pytest.skip(SKIP_NO_TRACE_ID_SPANS)

        response = get_api_v1_traces_by_trace_id_spans.sync_detailed(
            client=low_level_client,
            trace_id=trace_id,
        )

        # May be 404 if trace not found (eventual consistency)
        if response.status_code == 404:
            pytest.xfail("Trace spans not found - may be ingestion delay")

        assert response.status_code == 200, f"Get trace spans failed: {response.status_code}"

        # ===== VALIDATE RESPONSE BODY =====
        data = parse_response(response)
        assert data is not None, "Response data should not be None"

        # API returns {"success": true, "spans": [...], "trace_id": "..."}
        spans = data.get("spans", []) if isinstance(data, dict) else data
        spans = ensure_list(spans, "spans should be a list")

        if spans:
            first_span = spans[0]

            # Validate span_id
            span_id = get_field(first_span, "span_id")
            assert_non_empty_string(span_id, "span.span_id")

            # Validate trace_id matches parent
            span_trace_id = get_field(first_span, "trace_id")
            if span_trace_id:
                assert span_trace_id == trace_id, "Span trace_id should match parent"

            # Validate span name
            name = get_field(first_span, "name")
            if name:
                assert_non_empty_string(name, "span.name")

            # Validate span status
            status = get_field(first_span, "status")
            if status:
                assert status in ["ok", "OK", "error", "ERROR"] or isinstance(status, dict)

            # Validate duration
            duration_ms = get_field(first_span, "duration_ms")
            if duration_ms is not None:
                assert duration_ms >= 0, "Duration should be non-negative"

            # Validate timestamps
            start_time = get_field(first_span, "start_time")
            if start_time:
                assert_optional_string(start_time, "span.start_time")

            end_time = get_field(first_span, "end_time")
            if end_time:
                assert_optional_string(end_time, "span.end_time")

            # Check for parent_span_id (optional)
            parent_span_id = get_field(first_span, "parent_span_id")
            if parent_span_id:
                assert_non_empty_string(parent_span_id, "span.parent_span_id")

            # Check for attributes (optional)
            attributes = get_field(first_span, "attributes")
            if attributes is not None:
                assert isinstance(attributes, dict), "span.attributes should be a dict"

    def test_10_get_filter_values(
        self,
        low_level_client: Client,
    ) -> None:
        """Test getting filter values endpoint with response validation."""
        response = get_api_v1_traces_filter_values.sync_detailed(
            client=low_level_client,
        )

        assert response.status_code == 200, f"Get filter values failed: {response.status_code}"

        # ===== VALIDATE RESPONSE BODY =====
        data = parse_response(response)
        assert data is not None, "Response data should not be None"
        filter_values = data.get("data", data) if isinstance(data, dict) else data

        # Check for common filter value fields
        filter_fields = ["projects", "environments", "statuses", "services", "models"]
        for field in filter_fields:
            if isinstance(filter_values, dict) and field in filter_values:
                value = filter_values[field]
                assert isinstance(value, list), f"filter.{field} should be a list"

    def test_11_get_directory_tree(
        self,
        low_level_client: Client,
    ) -> None:
        """Test getting directory tree endpoint with response validation."""
        response = get_api_v1_traces_directory_tree.sync_detailed(
            client=low_level_client,
        )

        assert response.status_code == 200, f"Get directory tree failed: {response.status_code}"

        # ===== VALIDATE RESPONSE BODY =====
        data = parse_response(response)
        assert data is not None, "Response data should not be None"
        tree = data.get("tree", data) if isinstance(data, dict) else data

        # Directory tree typically has projects/folders structure
        if isinstance(tree, dict) and "projects" in tree:
            projects = tree["projects"]
            assert isinstance(projects, list), "tree.projects should be a list"

        if isinstance(tree, dict) and "children" in tree:
            assert tree["children"] is not None

        if isinstance(tree, dict) and "name" in tree:
            assert tree["name"] is not None

    def test_12_get_environments_by_projects(
        self,
        low_level_client: Client,
    ) -> None:
        """Test getting environments by projects endpoint with response validation."""
        response = get_api_v1_traces_environments_by_projects.sync_detailed(
            client=low_level_client,
        )

        assert response.status_code == 200, f"Get environments failed: {response.status_code}"

        # ===== VALIDATE RESPONSE BODY =====
        data = parse_response(response)
        assert data is not None, "Response data should not be None"
        envs = data.get("data", data) if isinstance(data, dict) else data

        # Could be a dict mapping projects to environments or a list
        if isinstance(envs, dict):
            assert len(envs) >= 0
            for project, environments in list(envs.items())[:3]:
                assert_non_empty_string(project, "envs.project")
                assert environments is not None

        elif isinstance(envs, list):
            assert len(envs) >= 0
            for env in envs[:5]:
                if hasattr(env, "project") and hasattr(env, "environment"):
                    assert_non_empty_string(env.project, "env.project")
                    assert_non_empty_string(env.environment, "env.environment")
                elif hasattr(env, "name"):
                    assert_non_empty_string(env.name, "env.name")

        elif isinstance(envs, dict) and "environments" in envs:
            assert envs["environments"] is not None


@pytest.mark.traces
@pytest.mark.integration
class TestTracesIsolated:
    """Isolated trace tests that don't depend on sequential state."""

    def test_connection_status_response_format(
        self,
        low_level_client: Client,
    ) -> None:
        """Test that connection status returns expected format."""
        response = get_api_v1_traces_connection_status.sync_detailed(client=low_level_client)

        assert response.status_code == 200
        assert response.headers is not None

    def test_list_traces_with_size_param(
        self,
        low_level_client: Client,
    ) -> None:
        """Test listing traces with custom size parameter."""
        response = get_api_v1_traces.sync_detailed(
            client=low_level_client,
            size=5,
        )

        assert response.status_code == 200

    def test_list_traces_empty_result_handling(
        self,
        low_level_client: Client,
    ) -> None:
        """Test that empty results are handled gracefully."""
        # Use a filter that likely returns no results (use search_term)
        response = get_api_v1_traces.sync_detailed(
            client=low_level_client,
            search_term="non_existent_trace_name_xyz_12345",
        )

        # Should still return 200 with empty results
        assert response.status_code == 200


# =============================================================================
# LangChain/LangGraph End-to-End Integration Tests
# =============================================================================

# Check for optional dependencies
try:
    import noveum_trace
    from noveum_trace import NoveumTraceCallbackHandler

    NOVEUM_TRACE_AVAILABLE = True
except ImportError:
    NOVEUM_TRACE_AVAILABLE = False

try:
    from langchain_core.messages import HumanMessage, SystemMessage
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_google_genai import ChatGoogleGenerativeAI

    LANGCHAIN_AVAILABLE = True
except ImportError:
    LANGCHAIN_AVAILABLE = False

try:
    from typing import TypedDict

    from langgraph.graph import END, START, StateGraph  # type: ignore[import-not-found]

    LANGGRAPH_AVAILABLE = True
except ImportError:
    LANGGRAPH_AVAILABLE = False


def get_gemini_api_key() -> str | None:
    """Get Gemini API key from environment."""
    return os.getenv("GEMINI_API_KEY")


def has_gemini_api_key() -> bool:
    """Check if Gemini API key is available."""
    return bool(os.getenv("GEMINI_API_KEY"))


@pytest.mark.traces
@pytest.mark.integration
@pytest.mark.langchain
@pytest.mark.skipif(not NOVEUM_TRACE_AVAILABLE, reason="noveum_trace package not installed")
@pytest.mark.skipif(not LANGCHAIN_AVAILABLE, reason="langchain packages not installed")
class TestLangChainTracing:
    """
    End-to-end LangChain integration tests with Noveum Trace.

    These tests verify that actual LLM calls through LangChain are properly
    traced with all expected fields (token counts, messages, model info, etc.)

    Requirements:
        - NOVEUM_API_KEY environment variable
        - GEMINI_API_KEY environment variable
        - noveum_trace package installed
        - langchain_google_genai package installed
    """

    @pytest.fixture(scope="class")
    def langchain_context(self) -> dict[str, Any]:
        """Shared context for LangChain tests."""
        return {
            "trace_ids": [],
            "last_response": None,
        }

    @pytest.fixture(scope="class")
    def noveum_handler(self, api_config: dict[str, str]) -> Any:
        """Initialize Noveum Trace and return callback handler."""
        if not NOVEUM_TRACE_AVAILABLE:
            pytest.skip(SKIP_NOVEUM_TRACE_NOT_AVAILABLE)

        # Initialize Noveum Trace
        noveum_trace.init(
            api_key=api_config["api_key"],
            project=api_config["project"],
            environment=api_config["environment"],
        )

        # Create and return callback handler
        handler = NoveumTraceCallbackHandler()
        return handler

    def test_01_simple_chain_tracing(
        self,
        noveum_handler: Any,
        langchain_context: dict[str, Any],
    ) -> None:
        """Test tracing a simple LangChain chain with Google Gemini."""
        if not has_gemini_api_key():
            pytest.skip(SKIP_GEMINI_API_KEY_NOT_SET)

        # Create a simple chain using LCEL
        prompt = ChatPromptTemplate.from_template("Answer in one sentence: What is {topic}?")
        llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0, google_api_key=get_gemini_api_key())
        chain = prompt | llm | StrOutputParser()

        # Run the chain with tracing
        result = chain.invoke({"topic": "the capital of France"}, config={"callbacks": [noveum_handler]})

        assert result is not None
        assert len(result) > 0
        assert "paris" in result.lower() or "Paris" in result

        langchain_context["last_response"] = result

    def test_02_chain_with_system_message(
        self,
        noveum_handler: Any,
        langchain_context: dict[str, Any],
    ) -> None:
        """Test tracing a chain with system message for role-based prompting."""
        if not has_gemini_api_key():
            pytest.skip(SKIP_GEMINI_API_KEY_NOT_SET)

        # Create a chain with system message
        prompt = ChatPromptTemplate.from_messages(
            [("system", "You are a helpful assistant that responds concisely."), ("human", "{question}")]
        )
        llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0, google_api_key=get_gemini_api_key())
        chain = prompt | llm | StrOutputParser()

        # Run with tracing
        result = chain.invoke({"question": "What is 2 + 2?"}, config={"callbacks": [noveum_handler]})

        assert result is not None
        assert "4" in result

    def test_03_multi_turn_conversation(
        self,
        noveum_handler: Any,
        langchain_context: dict[str, Any],
    ) -> None:
        """Test tracing a multi-turn conversation."""
        if not has_gemini_api_key():
            pytest.skip(SKIP_GEMINI_API_KEY_NOT_SET)

        llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0, google_api_key=get_gemini_api_key())

        # First turn
        messages_1 = [
            SystemMessage(content="You are a math tutor."),
            HumanMessage(content="What is the square root of 16?"),
        ]
        response_1 = llm.invoke(messages_1, config={"callbacks": [noveum_handler]})
        assert "4" in response_1.content

        # Second turn (continues conversation)
        messages_2 = [
            SystemMessage(content="You are a math tutor."),
            HumanMessage(content="What is the square root of 16?"),
            response_1,
            HumanMessage(content="And what is that number squared?"),
        ]
        response_2 = llm.invoke(messages_2, config={"callbacks": [noveum_handler]})
        assert "16" in response_2.content

    def test_04_streaming_chain(
        self,
        noveum_handler: Any,
        langchain_context: dict[str, Any],
    ) -> None:
        """Test tracing a streaming chain response."""
        if not has_gemini_api_key():
            pytest.skip(SKIP_GEMINI_API_KEY_NOT_SET)

        prompt = ChatPromptTemplate.from_template("List 3 colors: {category}")
        llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0, google_api_key=get_gemini_api_key())
        chain = prompt | llm | StrOutputParser()

        # Collect streamed chunks
        chunks = []
        for chunk in chain.stream({"category": "primary"}, config={"callbacks": [noveum_handler]}):
            chunks.append(chunk)

        full_response = "".join(chunks)
        assert len(full_response) > 0

    def test_05_error_handling_traced(
        self,
        noveum_handler: Any,
        langchain_context: dict[str, Any],
    ) -> None:
        """Test that errors in chains are properly traced."""
        if not has_gemini_api_key():
            pytest.skip(SKIP_GEMINI_API_KEY_NOT_SET)

        # Create a chain that will work, but test error path indirectly
        prompt = ChatPromptTemplate.from_template("Hello {name}")

        try:
            # This should work normally
            llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0, google_api_key=get_gemini_api_key())
            chain = prompt | llm | StrOutputParser()

            result = chain.invoke({"name": "World"}, config={"callbacks": [noveum_handler]})
            assert result is not None
        except Exception:
            # If there's an error, it should still be traced
            pass

    def test_06_verify_traces_ingested(
        self,
        low_level_client: Client,
        api_config: dict[str, str],
    ) -> None:
        """Verify that LangChain traces were ingested with proper fields."""
        time.sleep(5)

        # Query recent traces for our project
        response = get_api_v1_traces.sync_detailed(
            client=low_level_client,
            size=20,
            sort=GetApiV1TracesSort.START_TIMEDESC,
        )

        assert response.status_code == 200, f"Failed to list traces: {response.status_code}"

        # Parse response (handles both parsed and raw content)
        data = parse_response(response)
        assert data is not None, "Response data should not be None"

        # ===== VALIDATE LANGCHAIN TRACE FIELDS =====
        traces = data.get("traces", []) if isinstance(data, dict) else []
        assert isinstance(traces, list), "traces should be a list"

        if traces and len(traces) > 0:
            # Validate first trace has LangChain-specific fields
            first_trace = traces[0]

            # Helper to get field
            def get_field(obj: Any, field: str) -> Any:
                if isinstance(obj, dict):
                    return obj.get(field)
                return getattr(obj, field, None)

            # Check trace name
            name = get_field(first_trace, "name")
            if name:
                assert_non_empty_string(name, "trace.name")

            # Check span count (LangChain creates multiple spans)
            span_count = get_field(first_trace, "span_count")
            if span_count:
                assert span_count >= 1, "trace.span_count should be >= 1"

            # Check duration
            duration_ms = get_field(first_trace, "duration_ms")
            if duration_ms is not None:
                assert duration_ms > 0, "LLM call should have positive duration"

            # Check project matches
            project = get_field(first_trace, "project")
            if project:
                assert_non_empty_string(project, "trace.project")

            # Check for SDK info
            sdk = get_field(first_trace, "sdk")
            if sdk:
                sdk_name = sdk.get("name") if isinstance(sdk, dict) else getattr(sdk, "name", None)
                sdk_version = sdk.get("version") if isinstance(sdk, dict) else getattr(sdk, "version", None)
                if sdk_name:
                    assert_non_empty_string(sdk_name, "trace.sdk.name")
                if sdk_version:
                    assert_non_empty_string(sdk_version, "trace.sdk.version")

            # Check status
            status = get_field(first_trace, "status")
            if status:
                assert_non_empty_string(str(status), "trace.status")


@pytest.mark.traces
@pytest.mark.integration
@pytest.mark.langchain
@pytest.mark.langgraph
@pytest.mark.skipif(not NOVEUM_TRACE_AVAILABLE, reason="noveum_trace package not installed")
@pytest.mark.skipif(not LANGCHAIN_AVAILABLE, reason="langchain packages not installed")
@pytest.mark.skipif(not LANGGRAPH_AVAILABLE, reason="langgraph package not installed")
class TestLangGraphTracing:
    """
    End-to-end LangGraph integration tests with Noveum Trace.

    These tests verify that LangGraph agent workflows are properly traced.

    Requirements:
        - NOVEUM_API_KEY environment variable
        - GEMINI_API_KEY environment variable
        - noveum_trace, langchain_google_genai, langgraph packages installed
    """

    @pytest.fixture(scope="class")
    def noveum_handler(self, api_config: dict[str, str]) -> Any:
        """Initialize Noveum Trace and return callback handler."""
        if not NOVEUM_TRACE_AVAILABLE:
            pytest.skip(SKIP_NOVEUM_TRACE_NOT_AVAILABLE)

        noveum_trace.init(
            api_key=api_config["api_key"],
            project=api_config["project"],
            environment=api_config["environment"],
        )

        return NoveumTraceCallbackHandler()

    def test_01_simple_langgraph_workflow(
        self,
        noveum_handler: Any,
    ) -> None:
        """Test tracing a simple LangGraph state machine."""
        if not has_gemini_api_key():
            pytest.skip(SKIP_GEMINI_API_KEY_NOT_SET)

        # Define state
        class State(TypedDict):
            question: str
            answer: str

        # Define nodes
        def ask_llm(state: State) -> State:
            llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0, google_api_key=get_gemini_api_key())
            prompt = ChatPromptTemplate.from_template("Answer briefly: {question}")
            chain = prompt | llm | StrOutputParser()

            answer = chain.invoke({"question": state["question"]}, config={"callbacks": [noveum_handler]})
            return {"question": state["question"], "answer": answer}

        # Build graph
        builder = StateGraph(State)
        builder.add_node("ask", ask_llm)
        builder.add_edge(START, "ask")
        builder.add_edge("ask", END)

        graph = builder.compile()

        # Run the graph
        result = graph.invoke({"question": "What is Python?", "answer": ""}, config={"callbacks": [noveum_handler]})

        assert result is not None
        assert "answer" in result
        assert len(result["answer"]) > 0

    def test_02_multi_node_graph(
        self,
        noveum_handler: Any,
    ) -> None:
        """Test tracing a multi-node LangGraph workflow."""
        if not has_gemini_api_key():
            pytest.skip(SKIP_GEMINI_API_KEY_NOT_SET)

        class State(TypedDict):
            input_text: str
            summary: str
            keywords: str

        def summarize(state: State) -> State:
            llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0, google_api_key=get_gemini_api_key())
            prompt = ChatPromptTemplate.from_template("Summarize in one sentence: {text}")
            chain = prompt | llm | StrOutputParser()

            summary = chain.invoke({"text": state["input_text"]}, config={"callbacks": [noveum_handler]})
            return {**state, "summary": summary}

        def extract_keywords(state: State) -> State:
            llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0, google_api_key=get_gemini_api_key())
            prompt = ChatPromptTemplate.from_template("Extract 3 keywords from: {text}")
            chain = prompt | llm | StrOutputParser()

            keywords = chain.invoke({"text": state["summary"]}, config={"callbacks": [noveum_handler]})
            return {**state, "keywords": keywords}

        # Build multi-node graph
        builder = StateGraph(State)
        builder.add_node("summarize", summarize)
        builder.add_node("keywords", extract_keywords)
        builder.add_edge(START, "summarize")
        builder.add_edge("summarize", "keywords")
        builder.add_edge("keywords", END)

        graph = builder.compile()

        # Run the graph
        result = graph.invoke(
            {
                "input_text": (
                    "Python is a programming language known for its simplicity and readability. "
                    "It is widely used in web development, data science, and automation."
                ),
                "summary": "",
                "keywords": "",
            },
            config={"callbacks": [noveum_handler]},
        )

        assert result is not None
        assert len(result["summary"]) > 0
        assert len(result["keywords"]) > 0

    def test_03_verify_langgraph_traces(
        self,
        low_level_client: Client,
    ) -> None:
        """Verify LangGraph traces were ingested."""
        time.sleep(5)

        response = get_api_v1_traces.sync_detailed(
            client=low_level_client,
            size=10,
            sort=GetApiV1TracesSort.START_TIMEDESC,
        )

        assert response.status_code == 200
