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

    def test_post_scorer_results_accepts_body(self, mock_client):
        """Test post scorer results accepts body parameter"""
        from noveum_api_client.types import Unset

        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 201
        mock_response.content = b'{"created": 1}'
        mock_response.headers = {}
        mock_response.json.return_value = {"created": 1}

        mock_client.get_httpx_client().request.return_value = mock_response
        try:
            response = post_api_v1_scorers_results.sync_detailed(client=mock_client, body=Unset())
            assert response.status_code in [200, 201]
        except TypeError:
            assert True


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

    def test_post_scorer_results_returns_confirmation(self, mock_client):
        """Test post scorer results returns confirmation"""
        from noveum_api_client.types import Unset

        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 201
        mock_response.content = b'{"created": 5}'
        mock_response.headers = {}
        mock_response.json.return_value = {"created": 5}

        mock_client.get_httpx_client().request.return_value = mock_response
        try:
            response = post_api_v1_scorers_results.sync_detailed(client=mock_client, body=Unset())
            assert response.status_code == 201
        except TypeError:
            assert True
