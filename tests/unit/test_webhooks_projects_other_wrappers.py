"""
Unit Tests for Projects, ETL Jobs, Health, and Other API Wrappers

Tests projects, ETL jobs, health, and misc API wrapper functions.
"""

from unittest.mock import Mock

import httpx
import pytest

from noveum_api_client import Client


class TestProjectsWrappers:
    """Test projects API wrappers"""

    def test_projects_module_exists(self):
        """Test that projects module exists"""
        from noveum_api_client.api import projects

        assert projects is not None


class TestETLJobsWrappers:
    """Test ETL jobs API wrappers"""

    def test_etl_jobs_module_exists(self):
        """Test that ETL jobs module exists"""
        from noveum_api_client.api import etl_jobs

        assert etl_jobs is not None


class TestHealthCheckWrappers:
    """Test health check API wrappers"""

    def test_health_module_exists(self):
        """Test that health module exists"""
        from noveum_api_client.api import health

        assert health is not None

    def test_status_module_exists(self):
        """Test that status module exists"""
        from noveum_api_client.api import status

        assert status is not None


class TestModuleStructure:
    """Test overall API module structure"""

    def test_api_module_has_submodules(self):
        """Test that api module has expected submodules"""
        from noveum_api_client import api

        # Check for key modules
        assert hasattr(api, "datasets")
        assert hasattr(api, "traces")
        assert hasattr(api, "scorers")
        assert hasattr(api, "scorer_results")
        assert hasattr(api, "projects")
        assert hasattr(api, "etl_jobs")
        assert hasattr(api, "health")
        assert hasattr(api, "status")

    def test_client_import_works(self):
        """Test that Client can be imported"""
        from noveum_api_client import Client

        assert Client is not None

    def test_noveum_client_import_works(self):
        """Test that NoveumClient can be imported"""
        from noveum_api_client import NoveumClient

        assert NoveumClient is not None


class TestErrorHandlingAcrossModules:
    """Test error handling across different API modules"""

    @pytest.mark.parametrize("status_code", [400, 401, 403, 404, 500])
    def test_consistent_error_handling(self, mock_client, status_code):
        """Test that all modules handle errors consistently"""
        from noveum_api_client.api.datasets import get_api_v1_datasets

        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = status_code
        mock_response.content = b'{"error": "Error"}'
        mock_response.headers = {}
        mock_response.json.return_value = {"error": "Error"}

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_datasets.sync_detailed(client=mock_client)

        assert response.status_code == status_code


class TestAsyncSupportAcrossModules:
    """Test async support across different API modules"""

    def test_datasets_has_async_support(self):
        """Test datasets module has async methods"""
        from noveum_api_client.api.datasets import get_api_v1_datasets

        assert hasattr(get_api_v1_datasets, "asyncio_detailed")

    def test_traces_has_async_support(self):
        """Test traces module has async methods"""
        from noveum_api_client.api.traces import get_api_v1_traces

        assert hasattr(get_api_v1_traces, "asyncio_detailed")

    def test_scorers_has_async_support(self):
        """Test scorers module has async methods"""
        from noveum_api_client.api.scorers import get_api_v1_scorers

        assert hasattr(get_api_v1_scorers, "asyncio_detailed")

    def test_projects_has_async_support(self):
        """Test projects module has async methods"""
        from noveum_api_client.api.projects import get_api_v1_projects

        assert hasattr(get_api_v1_projects, "asyncio_detailed")

    def test_etl_jobs_has_async_support(self):
        """Test etl_jobs module has async methods"""
        from noveum_api_client.api.etl_jobs import get_api_v1_etl_jobs

        assert hasattr(get_api_v1_etl_jobs, "asyncio_detailed")


class TestPaginationSupportAcrossModules:
    """Test pagination support across different API modules"""

    def test_datasets_supports_pagination(self, mock_client):
        """Test datasets supports pagination"""
        from noveum_api_client.api.datasets import get_api_v1_datasets

        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = []

        mock_client.get_httpx_client().request.return_value = mock_response
        # Should accept limit/offset or similar pagination params
        response = get_api_v1_datasets.sync_detailed(client=mock_client, limit=10)

        assert response.status_code == 200

    def test_traces_supports_pagination(self, mock_client):
        """Test traces supports pagination"""
        from noveum_api_client.api.traces import get_api_v1_traces

        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = []

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_traces.sync_detailed(client=mock_client, size=20)

        assert response.status_code == 200


class TestClientConfigurationAcrossModules:
    """Test client configuration works across all modules"""

    def test_client_with_custom_base_url(self):
        """Test client accepts custom base URL"""
        client = Client(base_url="https://custom.api.com", headers={"Authorization": "Bearer test"})

        assert client._base_url == "https://custom.api.com"

    def test_client_with_timeout(self):
        """Test client accepts timeout configuration"""
        client = Client(base_url="https://api.noveum.ai", headers={"Authorization": "Bearer test"}, timeout=30.0)

        assert client._timeout == 30.0

    def test_client_with_custom_headers(self):
        """Test client accepts custom headers"""
        headers = {"Authorization": "Bearer test", "X-Custom-Header": "value"}

        client = Client(base_url="https://api.noveum.ai", headers=headers)

        assert client._headers is not None
