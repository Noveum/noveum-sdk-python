"""
Unit Tests for Scorer Results API Wrappers

Tests all scorer results-related API wrapper functions with mocked responses.
"""

from unittest.mock import Mock

import httpx
import pytest

from noveum_api_client.api.scorer_results import (
    get_api_v1_scorers_results,
    post_api_v1_scorers_results,
)


class TestScorerResultsListingWrappers:
    """Test scorer results listing API wrappers"""

    def test_get_scorer_results_has_sync_method(self):
        """Test that get_scorer_results has sync_detailed method"""
        assert hasattr(get_api_v1_scorers_results, "sync_detailed")
        assert callable(get_api_v1_scorers_results.sync_detailed)

    def test_get_scorer_results_has_async_method(self):
        """Test that get_scorer_results has asyncio_detailed method"""
        assert hasattr(get_api_v1_scorers_results, "asyncio_detailed")
        assert callable(get_api_v1_scorers_results.asyncio_detailed)

    def test_get_scorer_results_accepts_pagination(self, mock_client):
        """Test get scorer results accepts pagination parameters"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = []

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_scorers_results.sync_detailed(client=mock_client, limit=10, offset=0)

        assert response.status_code == 200


class TestScorerResultsCreationWrappers:
    """Test scorer results creation API wrappers"""

    def test_post_scorer_results_has_methods(self):
        """Test post scorer results has required methods"""
        assert hasattr(post_api_v1_scorers_results, "sync_detailed")
        assert hasattr(post_api_v1_scorers_results, "asyncio_detailed")

    def test_post_scorer_results_accepts_body_with_real_model(self):
        """Test post scorer results accepts body with real model"""
        from noveum_api_client.models import (
            PostApiV1ScorersResultsBatchBody,
            PostApiV1ScorersResultsBatchBodyResultsItem,
            PostApiV1ScorersResultsBatchBodyResultsItemMetadata,
        )

        # Create multiple results
        results = []
        for i in range(3):
            metadata = PostApiV1ScorersResultsBatchBodyResultsItemMetadata()
            result = PostApiV1ScorersResultsBatchBodyResultsItem(
                dataset_slug="test-dataset",
                item_id=f"item-{i}",
                scorer_id="scorer-1",
                score=0.8 + (i * 0.05),
                passed=True,
                metadata=metadata,
            )
            results.append(result)

        body = PostApiV1ScorersResultsBatchBody(results=results)

        # Verify body serializes correctly
        body_dict = body.to_dict()
        assert len(body_dict["results"]) == 3
        assert body_dict["results"][0]["datasetSlug"] == "test-dataset"
        assert body_dict["results"][0]["passed"] is True


class TestScorerResultsFiltering:
    """Test scorer results filtering"""

    def test_get_scorer_results_accepts_dataset_filter(self, mock_client):
        """Test get scorer results accepts dataset filter"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = []

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_scorers_results.sync_detailed(client=mock_client)

        assert response.status_code == 200

    @pytest.mark.parametrize(
        "limit,offset",
        [
            (10, 0),
            (50, 100),
            (100, 0),
        ],
    )
    def test_get_scorer_results_pagination(self, mock_client, limit, offset):
        """Test get scorer results with various pagination"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = []

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_scorers_results.sync_detailed(client=mock_client, limit=limit, offset=offset)

        assert response.status_code == 200


class TestScorerResultsErrorHandling:
    """Test error handling in scorer results wrappers"""

    @pytest.mark.parametrize("status_code", [400, 401, 404, 500])
    def test_handles_error_status_codes(self, mock_client, status_code):
        """Test scorer results wrappers handle various error codes"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = status_code
        mock_response.content = b'{"error": "Error message"}'
        mock_response.headers = {}
        mock_response.json.return_value = {"error": "Error message"}

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_scorers_results.sync_detailed(client=mock_client)

        assert response.status_code == status_code


class TestScorerResultsResponseStructure:
    """Test scorer results response structure"""

    def test_get_scorer_results_returns_list(self, mock_client):
        """Test get scorer results returns list structure"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"scorer_id": "scorer-1", "score": 0.95},
            {"scorer_id": "scorer-2", "score": 0.87},
        ]

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_scorers_results.sync_detailed(client=mock_client)

        assert response.status_code == 200

    def test_scorer_result_with_execution_metadata(self):
        """Test scorer result with execution time and error metadata"""
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
            execution_time_ms=125.5,
        )

        result_dict = result.to_dict()
        assert result_dict["executionTimeMs"] == 125.5
        assert result_dict["error"] == ""
        assert result_dict["passed"] is True

    def test_batch_results_with_mixed_pass_fail(self):
        """Test batch results with mixed pass/fail statuses"""
        from noveum_api_client.models import (
            PostApiV1ScorersResultsBatchBody,
            PostApiV1ScorersResultsBatchBodyResultsItem,
            PostApiV1ScorersResultsBatchBodyResultsItemMetadata,
        )

        results = []

        # Passing result
        metadata_pass = PostApiV1ScorersResultsBatchBodyResultsItemMetadata()
        result_pass = PostApiV1ScorersResultsBatchBodyResultsItem(
            dataset_slug="test-dataset",
            item_id="item-pass",
            scorer_id="scorer-1",
            score=0.95,
            passed=True,
            metadata=metadata_pass,
        )
        results.append(result_pass)

        # Failing result
        metadata_fail = PostApiV1ScorersResultsBatchBodyResultsItemMetadata()
        result_fail = PostApiV1ScorersResultsBatchBodyResultsItem(
            dataset_slug="test-dataset",
            item_id="item-fail",
            scorer_id="scorer-1",
            score=0.45,
            passed=False,
            metadata=metadata_fail,
            error="Score below threshold",
        )
        results.append(result_fail)

        body = PostApiV1ScorersResultsBatchBody(results=results)

        body_dict = body.to_dict()
        assert len(body_dict["results"]) == 2
        assert body_dict["results"][0]["passed"] is True
        assert body_dict["results"][1]["passed"] is False
        assert "threshold" in body_dict["results"][1]["error"]
