"""
Unit Tests for ETL Jobs API Wrappers

Tests all ETL job-related API wrapper functions with mocked responses.
"""

from unittest.mock import Mock

import httpx
import pytest

from noveum_api_client.api.etl_jobs import (
    delete_api_v1_etl_jobs_by_id,
    get_api_v1_etl_jobs,
    get_api_v1_etl_jobs_by_id,
    get_api_v1_etl_jobs_by_id_runs,
    get_api_v1_etl_jobs_by_id_status,
    post_api_v1_etl_jobs,
    post_api_v1_etl_jobs_by_id_trigger,
    post_api_v1_etl_jobs_run_mapper,
    put_api_v1_etl_jobs_by_id,
)
from noveum_api_client.models import PostApiV1EtlJobsBody, PutApiV1EtlJobsByIdBody


class TestETLJobsListingWrappers:
    """Test ETL jobs listing API wrappers"""

    def test_get_etl_jobs_has_sync_method(self):
        """Test that get_etl_jobs has sync_detailed method"""
        assert hasattr(get_api_v1_etl_jobs, "sync_detailed")
        assert callable(get_api_v1_etl_jobs.sync_detailed)

    def test_get_etl_jobs_has_async_method(self):
        """Test that get_etl_jobs has asyncio_detailed method"""
        assert hasattr(get_api_v1_etl_jobs, "asyncio_detailed")
        assert callable(get_api_v1_etl_jobs.asyncio_detailed)

    def test_get_etl_jobs_basic_call(self, mock_client):
        """Test get ETL jobs basic call"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = []

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_etl_jobs.sync_detailed(client=mock_client)

        assert response.status_code == 200


class TestETLJobsCRUDWrappers:
    """Test ETL jobs CRUD operation wrappers"""

    def test_post_etl_jobs_has_methods(self):
        """Test post ETL jobs has required methods"""
        assert hasattr(post_api_v1_etl_jobs, "sync_detailed")
        assert hasattr(post_api_v1_etl_jobs, "asyncio_detailed")

    def test_get_etl_job_by_id_has_methods(self):
        """Test get ETL job by ID has methods"""
        assert hasattr(get_api_v1_etl_jobs_by_id, "sync_detailed")
        assert hasattr(get_api_v1_etl_jobs_by_id, "asyncio_detailed")

    def test_put_etl_job_has_methods(self):
        """Test put ETL job has methods"""
        assert hasattr(put_api_v1_etl_jobs_by_id, "sync_detailed")
        assert hasattr(put_api_v1_etl_jobs_by_id, "asyncio_detailed")

    def test_delete_etl_job_has_methods(self):
        """Test delete ETL job has methods"""
        assert hasattr(delete_api_v1_etl_jobs_by_id, "sync_detailed")
        assert hasattr(delete_api_v1_etl_jobs_by_id, "asyncio_detailed")

    def test_delete_etl_job_requires_id(self, mock_client):
        """Test delete ETL job requires job ID"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 204
        mock_response.content = b""

        mock_client.get_httpx_client().request.return_value = mock_response
        response = delete_api_v1_etl_jobs_by_id.sync_detailed(id="etl-job-1", client=mock_client)

        assert response.status_code == 204


class TestETLJobsExecutionWrappers:
    """Test ETL job execution wrappers"""

    def test_get_etl_job_status_has_methods(self):
        """Test get ETL job status has methods"""
        assert hasattr(get_api_v1_etl_jobs_by_id_status, "sync_detailed")
        assert hasattr(get_api_v1_etl_jobs_by_id_status, "asyncio_detailed")

    def test_get_etl_job_status_requires_id(self, mock_client):
        """Test get ETL job status requires job ID"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = {"status": "running", "progress": 50}

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_etl_jobs_by_id_status.sync_detailed(id="etl-job-1", client=mock_client)

        assert response.status_code == 200

    def test_trigger_etl_job_has_methods(self):
        """Test trigger ETL job has methods"""
        assert hasattr(post_api_v1_etl_jobs_by_id_trigger, "sync_detailed")
        assert hasattr(post_api_v1_etl_jobs_by_id_trigger, "asyncio_detailed")

    def test_get_etl_job_runs_has_methods(self):
        """Test get ETL job runs has methods"""
        assert hasattr(get_api_v1_etl_jobs_by_id_runs, "sync_detailed")
        assert hasattr(get_api_v1_etl_jobs_by_id_runs, "asyncio_detailed")


class TestETLJobsMapperWrappers:
    """Test ETL job mapper wrappers"""

    def test_run_mapper_has_methods(self):
        """Test run mapper has methods"""
        assert hasattr(post_api_v1_etl_jobs_run_mapper, "sync_detailed")
        assert hasattr(post_api_v1_etl_jobs_run_mapper, "asyncio_detailed")


class TestETLJobsErrorHandling:
    """Test error handling in ETL jobs wrappers"""

    @pytest.mark.parametrize("status_code", [400, 401, 403, 404, 500])
    def test_handles_error_status_codes(self, mock_client, status_code):
        """Test ETL jobs wrappers handle various error codes"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = status_code
        mock_response.content = b'{"error": "Error message"}'
        mock_response.json.return_value = {"error": "Error message"}

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_etl_jobs.sync_detailed(client=mock_client)

        assert response.status_code == status_code

    def test_handles_not_found_job(self, mock_client):
        """Test handles not found ETL job gracefully"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 404
        mock_response.content = b'{"error": "ETL job not found"}'
        mock_response.json.return_value = {"error": "ETL job not found"}

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_etl_jobs_by_id.sync_detailed(id="nonexistent", client=mock_client)

        assert response.status_code == 404


class TestETLJobsModelSerialization:
    """Test ETL jobs model serialization"""

    def test_create_etl_job_body_serializes(self):
        """Test ETL job body model serializes correctly"""
        body = PostApiV1EtlJobsBody(
            name="Test ETL Job",
            project_id="test-project",
            dataset_slug="test-dataset",
            environment="test",
            mapper_code="def mapper(item): return item",
        )

        body_dict = body.to_dict()

        assert body_dict["name"] == "Test ETL Job"
        assert body_dict["projectId"] == "test-project"
        assert body_dict["datasetSlug"] == "test-dataset"
        assert body_dict["environment"] == "test"
        assert "def mapper" in body_dict["mapperCode"]

    def test_update_etl_job_body_serializes(self):
        """Test ETL job update body serializes correctly"""
        body = PutApiV1EtlJobsByIdBody(name="Updated Name", mapper_code="def new_mapper(item): return item")

        body_dict = body.to_dict()

        assert body_dict["name"] == "Updated Name"
        assert "def new_mapper" in body_dict["mapperCode"]
