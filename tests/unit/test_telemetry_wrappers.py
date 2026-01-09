"""
Unit Tests for Telemetry API Wrappers

Tests all telemetry-related API wrapper functions with mocked responses.
"""

from unittest.mock import Mock

import httpx
import pytest

from noveum_api_client.api.telemetry import (
    get_api_telemetry_metrics,
    get_api_telemetry_metrics_cost_by_provider,
    get_api_telemetry_metrics_dashboard,
    get_api_telemetry_metrics_error_rate,
    get_api_telemetry_metrics_latency_by_provider,
    get_api_telemetry_metrics_model_usage,
    get_api_telemetry_metrics_recent_errors,
    get_api_telemetry_metrics_slowest_requests,
    get_api_telemetry_metrics_usage_trends,
    get_api_telemetry_metrics_with_trends,
)


class TestTelemetryStatsWrappers:
    """Test telemetry stats API wrappers"""

    def test_get_telemetry_stats_has_methods(self):
        """Test get telemetry stats has required methods"""
        assert hasattr(get_api_telemetry_metrics, "sync_detailed")
        assert hasattr(get_api_telemetry_metrics, "asyncio_detailed")

    def test_get_telemetry_stats_accepts_filters(self, mock_client):
        """Test get telemetry stats accepts filter parameters"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = {"stats": {}}

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_telemetry_metrics.sync_detailed(client=mock_client, organization_id="test-org-id")

        assert response.status_code == 200


class TestTelemetryCostWrappers:
    """Test telemetry cost stats API wrappers"""

    def test_get_cost_stats_has_methods(self):
        """Test get cost stats has required methods"""
        assert hasattr(get_api_telemetry_metrics_cost_by_provider, "sync_detailed")
        assert hasattr(get_api_telemetry_metrics_cost_by_provider, "asyncio_detailed")

    def test_get_cost_stats_returns_cost_data(self, mock_client):
        """Test get cost stats returns cost data"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = {"total_cost": 123.45, "currency": "USD"}

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_telemetry_metrics_cost_by_provider.sync_detailed(
            client=mock_client, organization_id="test-org-id"
        )

        assert response.status_code == 200


class TestTelemetryErrorWrappers:
    """Test telemetry error stats API wrappers"""

    def test_get_error_stats_has_methods(self):
        """Test get error stats has required methods"""
        assert hasattr(get_api_telemetry_metrics_recent_errors, "sync_detailed")
        assert hasattr(get_api_telemetry_metrics_recent_errors, "asyncio_detailed")

    def test_get_error_stats_returns_error_data(self, mock_client):
        """Test get error stats returns error data"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = {"error_count": 42, "error_rate": 0.05}

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_telemetry_metrics_recent_errors.sync_detailed(
            client=mock_client, organization_id="test-org-id"
        )

        assert response.status_code == 200


class TestTelemetryLatencyWrappers:
    """Test telemetry latency stats API wrappers"""

    def test_get_latency_stats_has_methods(self):
        """Test get latency stats has required methods"""
        assert hasattr(get_api_telemetry_metrics_latency_by_provider, "sync_detailed")
        assert hasattr(get_api_telemetry_metrics_latency_by_provider, "asyncio_detailed")

    def test_get_latency_stats_returns_latency_data(self, mock_client):
        """Test get latency stats returns latency data"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = {"avg_latency": 250.5, "p95_latency": 500.0}

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_telemetry_metrics_latency_by_provider.sync_detailed(
            client=mock_client, organization_id="test-org-id"
        )

        assert response.status_code == 200


class TestTelemetryModelWrappers:
    """Test telemetry model stats API wrappers"""

    def test_get_model_stats_has_methods(self):
        """Test get model stats has required methods"""
        assert hasattr(get_api_telemetry_metrics_model_usage, "sync_detailed")
        assert hasattr(get_api_telemetry_metrics_model_usage, "asyncio_detailed")

    def test_get_provider_stats_has_methods(self):
        """Test get provider stats has required methods"""
        assert hasattr(get_api_telemetry_metrics_dashboard, "sync_detailed")
        assert hasattr(get_api_telemetry_metrics_dashboard, "asyncio_detailed")


class TestTelemetrySuccessWrappers:
    """Test telemetry success stats API wrappers"""

    def test_get_success_stats_has_methods(self):
        """Test get success stats has required methods"""
        assert hasattr(get_api_telemetry_metrics_error_rate, "sync_detailed")
        assert hasattr(get_api_telemetry_metrics_error_rate, "asyncio_detailed")

    def test_get_success_stats_returns_success_data(self, mock_client):
        """Test get success stats returns success data"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = {"success_count": 1000, "success_rate": 0.95}

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_telemetry_metrics_error_rate.sync_detailed(client=mock_client, organization_id="test-org-id")

        assert response.status_code == 200


class TestTelemetryTokenWrappers:
    """Test telemetry token stats API wrappers"""

    def test_get_token_stats_has_methods(self):
        """Test get token stats has required methods"""
        assert hasattr(get_api_telemetry_metrics_usage_trends, "sync_detailed")
        assert hasattr(get_api_telemetry_metrics_usage_trends, "asyncio_detailed")

    def test_get_token_stats_returns_token_data(self, mock_client):
        """Test get token stats returns token data"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "total_tokens": 1000000,
            "prompt_tokens": 600000,
            "completion_tokens": 400000,
        }

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_telemetry_metrics_usage_trends.sync_detailed(
            client=mock_client, organization_id="test-org-id"
        )

        assert response.status_code == 200


class TestTelemetryTotalWrappers:
    """Test telemetry total stats API wrappers"""

    def test_get_total_stats_has_methods(self):
        """Test get total stats has required methods"""
        assert hasattr(get_api_telemetry_metrics_with_trends, "sync_detailed")
        assert hasattr(get_api_telemetry_metrics_with_trends, "asyncio_detailed")


class TestTelemetryPromptsWrappers:
    """Test telemetry prompts API wrappers"""

    def test_get_top_prompts_has_methods(self):
        """Test get top prompts has required methods"""
        assert hasattr(get_api_telemetry_metrics_slowest_requests, "sync_detailed")
        assert hasattr(get_api_telemetry_metrics_slowest_requests, "asyncio_detailed")

    def test_get_top_prompts_returns_prompts_data(self, mock_client):
        """Test get top prompts returns prompts data"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = [{"prompt": "What is...", "count": 100}, {"prompt": "How to...", "count": 80}]

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_telemetry_metrics_slowest_requests.sync_detailed(
            client=mock_client, organization_id="test-org-id"
        )

        assert response.status_code == 200


class TestTelemetryErrorHandling:
    """Test error handling in telemetry wrappers"""

    @pytest.mark.parametrize("status_code", [400, 401, 404, 500])
    def test_handles_error_status_codes(self, mock_client, status_code):
        """Test telemetry wrappers handle various error codes"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = status_code
        mock_response.content = b'{"error": "Error message"}'
        mock_response.headers = {}
        mock_response.json.return_value = {"error": "Error message"}

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_telemetry_metrics.sync_detailed(client=mock_client, organization_id="test-org-id")

        assert response.status_code == status_code
