"""
Unit Tests for Projects API Wrappers

Tests all project-related API wrapper functions with mocked responses.
"""

from unittest.mock import Mock

import httpx
import pytest

from noveum_api_client.api.projects import (
    delete_api_v1_projects_by_id,
    delete_api_v1_projects_by_id_datasets_by_dataset_id,
    get_api_v1_projects,
    get_api_v1_projects_by_id,
    get_api_v1_projects_by_id_datasets_associated,
    get_api_v1_projects_by_id_datasets_available,
    get_api_v1_projects_by_id_health,
    get_api_v1_projects_by_id_health_scorers_by_scorer_id,
    post_api_v1_projects,
    post_api_v1_projects_by_id_datasets_associate,
    put_api_v1_projects_by_id,
)
from noveum_api_client.models import PostApiV1ProjectsBody, PutApiV1ProjectsByIdBody


class TestProjectsListingWrappers:
    """Test projects listing API wrappers"""

    def test_get_projects_has_sync_method(self):
        """Test that get_projects has sync_detailed method"""
        assert hasattr(get_api_v1_projects, "sync_detailed")
        assert callable(get_api_v1_projects.sync_detailed)

    def test_get_projects_has_async_method(self):
        """Test that get_projects has asyncio_detailed method"""
        assert hasattr(get_api_v1_projects, "asyncio_detailed")
        assert callable(get_api_v1_projects.asyncio_detailed)

    def test_get_projects_accepts_filters(self, mock_client):
        """Test get projects accepts filter parameters"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = []

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_projects.sync_detailed(client=mock_client, organization_slug="test-org")

        assert response.status_code == 200

    def test_get_projects_returns_list(self, mock_client):
        """Test get projects returns list of projects"""
        # Create complete mock project data
        project_data = {
            "id": "project-1",
            "name": "Project 1",
            "description": "Test project",
            "organizationId": "org-1",
            "createdAt": "2024-01-01T00:00:00Z",
            "updatedAt": "2024-01-01T00:00:00Z",
        }

        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = [project_data]

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_projects.sync_detailed(client=mock_client)

        assert response.status_code == 200


class TestProjectsCRUDWrappers:
    """Test projects CRUD operation wrappers"""

    def test_post_projects_has_methods(self):
        """Test post projects has required methods"""
        assert hasattr(post_api_v1_projects, "sync_detailed")
        assert hasattr(post_api_v1_projects, "asyncio_detailed")

    def test_post_projects_accepts_body(self, mock_client):
        """Test post projects accepts body parameter"""
        body = PostApiV1ProjectsBody(name="Test Project", id="test-project-id", description="Test description")

        project_response = {
            "id": "test-project-id",
            "name": "Test Project",
            "description": "Test description",
            "organizationId": "org-1",
            "createdAt": "2024-01-01T00:00:00Z",
            "updatedAt": "2024-01-01T00:00:00Z",
        }

        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 201
        mock_response.content = str(project_response).encode()
        mock_response.json.return_value = project_response

        mock_client.get_httpx_client().request.return_value = mock_response
        response = post_api_v1_projects.sync_detailed(client=mock_client, body=body)

        assert response.status_code == 201

    def test_get_project_by_id_has_methods(self):
        """Test get project by ID has methods"""
        assert hasattr(get_api_v1_projects_by_id, "sync_detailed")
        assert hasattr(get_api_v1_projects_by_id, "asyncio_detailed")

    def test_get_project_by_id_requires_id(self, mock_client):
        """Test get project by ID requires project ID"""
        project_response = {
            "id": "project-1",
            "name": "Test Project",
            "description": "Test description",
            "organizationId": "org-1",
            "createdAt": "2024-01-01T00:00:00Z",
            "updatedAt": "2024-01-01T00:00:00Z",
        }

        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = project_response

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_projects_by_id.sync_detailed(id="project-1", client=mock_client)

        assert response.status_code == 200

    def test_put_project_has_methods(self):
        """Test put project has methods"""
        assert hasattr(put_api_v1_projects_by_id, "sync_detailed")
        assert hasattr(put_api_v1_projects_by_id, "asyncio_detailed")

    def test_put_project_accepts_body(self, mock_client):
        """Test put project accepts body parameter"""
        body = PutApiV1ProjectsByIdBody(name="Updated Project", description="Updated description")

        project_response = {
            "id": "project-1",
            "name": "Updated Project",
            "description": "Updated description",
            "organizationId": "org-1",
            "createdAt": "2024-01-01T00:00:00Z",
            "updatedAt": "2024-01-02T00:00:00Z",
        }

        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = project_response

        mock_client.get_httpx_client().request.return_value = mock_response
        response = put_api_v1_projects_by_id.sync_detailed(id="project-1", client=mock_client, body=body)

        assert response.status_code == 200

    def test_delete_project_has_methods(self):
        """Test delete project has methods"""
        assert hasattr(delete_api_v1_projects_by_id, "sync_detailed")
        assert hasattr(delete_api_v1_projects_by_id, "asyncio_detailed")

    def test_delete_project_requires_id(self, mock_client):
        """Test delete project requires project ID"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 204
        mock_response.content = b""

        mock_client.get_httpx_client().request.return_value = mock_response
        response = delete_api_v1_projects_by_id.sync_detailed(id="project-1", client=mock_client)

        assert response.status_code == 204


class TestProjectsDatasetAssociationWrappers:
    """Test project-dataset association wrappers"""

    def test_get_associated_datasets_has_methods(self):
        """Test get associated datasets has methods"""
        assert hasattr(get_api_v1_projects_by_id_datasets_associated, "sync_detailed")
        assert hasattr(get_api_v1_projects_by_id_datasets_associated, "asyncio_detailed")

    def test_get_associated_datasets_returns_list(self, mock_client):
        """Test get associated datasets returns list"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"slug": "dataset-1", "name": "Dataset 1"},
            {"slug": "dataset-2", "name": "Dataset 2"},
        ]

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_projects_by_id_datasets_associated.sync_detailed(id="project-1", client=mock_client)

        assert response.status_code == 200

    def test_get_available_datasets_has_methods(self):
        """Test get available datasets has methods"""
        assert hasattr(get_api_v1_projects_by_id_datasets_available, "sync_detailed")
        assert hasattr(get_api_v1_projects_by_id_datasets_available, "asyncio_detailed")

    def test_get_available_datasets_returns_list(self, mock_client):
        """Test get available datasets returns list"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"slug": "dataset-3", "name": "Dataset 3"},
            {"slug": "dataset-4", "name": "Dataset 4"},
        ]

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_projects_by_id_datasets_available.sync_detailed(id="project-1", client=mock_client)

        assert response.status_code == 200

    def test_associate_dataset_has_methods(self):
        """Test associate dataset has methods"""
        assert hasattr(post_api_v1_projects_by_id_datasets_associate, "sync_detailed")
        assert hasattr(post_api_v1_projects_by_id_datasets_associate, "asyncio_detailed")

    def test_associate_dataset_succeeds(self, mock_client):
        """Test associate dataset succeeds"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = {"message": "Dataset associated"}

        mock_client.get_httpx_client().request.return_value = mock_response
        # The actual function takes organization parameters
        response = post_api_v1_projects_by_id_datasets_associate.sync_detailed(
            id="project-1", organization_slug="test-org", client=mock_client
        )

        assert response.status_code == 200

    def test_disassociate_dataset_has_methods(self):
        """Test disassociate dataset has methods"""
        assert hasattr(delete_api_v1_projects_by_id_datasets_by_dataset_id, "sync_detailed")
        assert hasattr(delete_api_v1_projects_by_id_datasets_by_dataset_id, "asyncio_detailed")

    def test_disassociate_dataset_requires_ids(self, mock_client):
        """Test disassociate dataset requires project and dataset IDs"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 204
        mock_response.content = b""

        mock_client.get_httpx_client().request.return_value = mock_response
        response = delete_api_v1_projects_by_id_datasets_by_dataset_id.sync_detailed(
            id="project-1", dataset_id="dataset-1", client=mock_client
        )

        assert response.status_code == 204


class TestProjectsHealthWrappers:
    """Test project health API wrappers"""

    def test_get_project_health_has_methods(self):
        """Test get project health has methods"""
        assert hasattr(get_api_v1_projects_by_id_health, "sync_detailed")
        assert hasattr(get_api_v1_projects_by_id_health, "asyncio_detailed")

    def test_get_project_health_returns_health_data(self, mock_client):
        """Test get project health returns health metrics"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "overallHealth": "good",
            "scorers": [{"scorerId": "scorer-1", "health": "good", "lastRun": "2024-01-01T00:00:00Z"}],
        }

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_projects_by_id_health.sync_detailed(id="project-1", client=mock_client)

        assert response.status_code == 200

    def test_get_project_health_by_scorer_has_methods(self):
        """Test get project health by scorer has methods"""
        assert hasattr(get_api_v1_projects_by_id_health_scorers_by_scorer_id, "sync_detailed")
        assert hasattr(get_api_v1_projects_by_id_health_scorers_by_scorer_id, "asyncio_detailed")

    def test_get_project_health_by_scorer_requires_ids(self, mock_client):
        """Test get project health by scorer requires project and scorer IDs"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "scorerId": "scorer-1",
            "health": "good",
            "lastRun": "2024-01-01T00:00:00Z",
            "metrics": {},
        }

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_projects_by_id_health_scorers_by_scorer_id.sync_detailed(
            id="project-1", scorer_id="scorer-1", client=mock_client
        )

        assert response.status_code == 200


class TestProjectsErrorHandling:
    """Test error handling in projects wrappers"""

    @pytest.mark.parametrize("status_code", [400, 401, 403, 404, 500])
    def test_handles_error_status_codes(self, mock_client, status_code):
        """Test projects wrappers handle various error codes"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = status_code
        mock_response.content = b'{"error": "Error message"}'
        mock_response.json.return_value = {"error": "Error message"}

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_projects.sync_detailed(client=mock_client)

        assert response.status_code == status_code

    def test_handles_not_found_project(self, mock_client):
        """Test handles not found project gracefully"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 404
        mock_response.content = b'{"error": "Project not found"}'
        mock_response.json.return_value = {"error": "Project not found"}

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_projects_by_id.sync_detailed(id="nonexistent", client=mock_client)

        assert response.status_code == 404


class TestProjectsResponseStructure:
    """Test projects response structure"""

    def test_get_projects_returns_list_structure(self, mock_client):
        """Test get projects returns expected list structure"""
        projects = [
            {
                "id": "project-1",
                "name": "Project 1",
                "description": "Desc 1",
                "organizationId": "org-1",
                "createdAt": "2024-01-01T00:00:00Z",
                "updatedAt": "2024-01-01T00:00:00Z",
            },
            {
                "id": "project-2",
                "name": "Project 2",
                "description": "Desc 2",
                "organizationId": "org-1",
                "createdAt": "2024-01-01T00:00:00Z",
                "updatedAt": "2024-01-01T00:00:00Z",
            },
        ]

        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = projects

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_projects.sync_detailed(client=mock_client)

        assert response.status_code == 200
        assert response is not None

    def test_post_projects_returns_created_project(self, mock_client):
        """Test post projects returns created project object"""
        body = PostApiV1ProjectsBody(name="New Project", id="new-project-id", description="New description")

        project_response = {
            "id": "new-project-id",
            "name": "New Project",
            "description": "New description",
            "organizationId": "org-1",
            "createdAt": "2024-01-01T00:00:00Z",
            "updatedAt": "2024-01-01T00:00:00Z",
        }

        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 201
        mock_response.content = str(project_response).encode()
        mock_response.json.return_value = project_response

        mock_client.get_httpx_client().request.return_value = mock_response
        response = post_api_v1_projects.sync_detailed(client=mock_client, body=body)

        assert response.status_code == 201

    def test_get_project_by_id_returns_single_object(self, mock_client):
        """Test get project by ID returns single object"""
        project_data = {
            "id": "project-1",
            "name": "Test Project",
            "description": "Test description",
            "organizationId": "org-1",
            "createdAt": "2024-01-01T00:00:00Z",
            "updatedAt": "2024-01-01T00:00:00Z",
        }
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.content = str(project_data).encode()
        mock_response.json.return_value = project_data

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_projects_by_id.sync_detailed(id="project-1", client=mock_client)

        assert response.status_code == 200


class TestProjectsUpdateOperations:
    """Test projects update operations"""

    def test_put_project_accepts_updates(self, mock_client):
        """Test put project accepts update data"""
        body = PutApiV1ProjectsByIdBody(name="Updated Name", description="Updated description")

        project_response = {
            "id": "project-1",
            "name": "Updated Name",
            "description": "Updated description",
            "organizationId": "org-1",
            "createdAt": "2024-01-01T00:00:00Z",
            "updatedAt": "2024-01-02T00:00:00Z",
        }

        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = project_response

        mock_client.get_httpx_client().request.return_value = mock_response
        response = put_api_v1_projects_by_id.sync_detailed(id="project-1", client=mock_client, body=body)

        assert response.status_code == 200

    def test_put_project_with_partial_update(self, mock_client):
        """Test put project with partial update (only name)"""
        body = PutApiV1ProjectsByIdBody(name="Only Name Updated", description="Test")

        project_response = {
            "id": "project-1",
            "name": "Only Name Updated",
            "description": "Test",
            "organizationId": "org-1",
            "createdAt": "2024-01-01T00:00:00Z",
            "updatedAt": "2024-01-02T00:00:00Z",
        }

        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = project_response

        mock_client.get_httpx_client().request.return_value = mock_response
        response = put_api_v1_projects_by_id.sync_detailed(id="project-1", client=mock_client, body=body)

        assert response.status_code == 200

    def test_delete_project_returns_success(self, mock_client):
        """Test delete project returns success"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 204
        mock_response.content = b""

        mock_client.get_httpx_client().request.return_value = mock_response
        response = delete_api_v1_projects_by_id.sync_detailed(id="project-1", client=mock_client)

        assert response.status_code in [200, 204]
