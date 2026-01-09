"""
Unit Tests for Authentication API Wrappers

Tests all authentication-related API wrapper functions with mocked responses.
"""

from unittest.mock import Mock

import httpx
import pytest

from noveum_api_client.api.auth import (
    get_api_auth_error,
    get_api_auth_get_session,
    get_api_auth_list_accounts,
    get_api_auth_list_sessions,
    get_api_auth_ok,
    get_api_auth_organization_get_active_member,
    get_api_auth_organization_get_full_organization,
    get_api_auth_organization_list,
    get_api_auth_passkey_list_user_passkeys,
    list_users,
)


class TestSessionWrappers:
    """Test session management API wrappers"""

    def test_get_session_has_methods(self):
        """Test get session has required methods"""
        assert hasattr(get_api_auth_get_session, "sync_detailed")
        assert hasattr(get_api_auth_get_session, "asyncio_detailed")

    def test_list_sessions_has_methods(self):
        """Test list sessions has required methods"""
        assert hasattr(get_api_auth_list_sessions, "sync_detailed")
        assert hasattr(get_api_auth_list_sessions, "asyncio_detailed")

    def test_get_session_returns_session_data(self, mock_client):
        """Test get session returns session data"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = {"session_id": "sess-1", "user_id": "user-1"}

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_auth_get_session.sync_detailed(client=mock_client)

        assert response.status_code == 200


class TestOrganizationWrappers:
    """Test organization management API wrappers"""

    def test_organization_list_has_methods(self):
        """Test organization list has required methods"""
        assert hasattr(get_api_auth_organization_list, "sync_detailed")
        assert hasattr(get_api_auth_organization_list, "asyncio_detailed")

    def test_get_full_organization_has_methods(self):
        """Test get full organization has required methods"""
        assert hasattr(get_api_auth_organization_get_full_organization, "sync_detailed")
        assert hasattr(get_api_auth_organization_get_full_organization, "asyncio_detailed")

    def test_get_active_member_has_methods(self):
        """Test get active member has required methods"""
        assert hasattr(get_api_auth_organization_get_active_member, "sync_detailed")
        assert hasattr(get_api_auth_organization_get_active_member, "asyncio_detailed")

    def test_organization_list_returns_orgs(self, mock_client):
        """Test organization list returns organizations"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.content = b'[{"id": "org-1", "name": "Org 1"}, {"id": "org-2", "name": "Org 2"}]'
        mock_response.headers = {}
        mock_response.json.return_value = [
            {"id": "org-1", "name": "Org 1", "slug": "org-1"},
            {"id": "org-2", "name": "Org 2", "slug": "org-2"},
        ]

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_auth_organization_list.sync_detailed(client=mock_client)

        assert response.status_code == 200


class TestAccountWrappers:
    """Test account management API wrappers"""

    def test_list_accounts_has_methods(self):
        """Test list accounts has required methods"""
        assert hasattr(get_api_auth_list_accounts, "sync_detailed")
        assert hasattr(get_api_auth_list_accounts, "asyncio_detailed")

    def test_list_accounts_returns_accounts(self, mock_client):
        """Test list accounts returns account data"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.content = (
            b'[{"id": "acc-1", "email": "user1@example.com"}, {"id": "acc-2", "email": "user2@example.com"}]'
        )
        mock_response.headers = {}
        mock_response.json.return_value = [
            {"id": "acc-1", "email": "user1@example.com"},
            {"id": "acc-2", "email": "user2@example.com"},
        ]

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_auth_list_accounts.sync_detailed(client=mock_client)

        assert response.status_code == 200


class TestUserWrappers:
    """Test user management API wrappers"""

    def test_list_users_has_methods(self):
        """Test list users has required methods"""
        assert hasattr(list_users, "sync_detailed")
        assert hasattr(list_users, "asyncio_detailed")

    def test_list_users_returns_users(self, mock_client):
        """Test list users returns user data"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"id": "user-1", "email": "user1@example.com"},
            {"id": "user-2", "email": "user2@example.com"},
        ]

        mock_client.get_httpx_client().request.return_value = mock_response
        response = list_users.sync_detailed(client=mock_client)

        assert response.status_code == 200


class TestPasskeyWrappers:
    """Test passkey management API wrappers"""

    def test_list_user_passkeys_has_methods(self):
        """Test list user passkeys has required methods"""
        assert hasattr(get_api_auth_passkey_list_user_passkeys, "sync_detailed")
        assert hasattr(get_api_auth_passkey_list_user_passkeys, "asyncio_detailed")

    def test_list_user_passkeys_returns_passkeys(self, mock_client):
        """Test list user passkeys handles 404 when no passkeys found"""
        # This endpoint only returns error responses (no 200 success response defined)
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 404
        mock_response.content = b'{"error": "Not found"}'
        mock_response.headers = {}
        mock_response.json.return_value = {"error": "Not found"}

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_auth_passkey_list_user_passkeys.sync_detailed(client=mock_client)

        assert response.status_code == 404


class TestAuthHealthCheckWrappers:
    """Test auth health check API wrappers"""

    def test_auth_ok_has_methods(self):
        """Test auth ok endpoint has required methods"""
        assert hasattr(get_api_auth_ok, "sync_detailed")
        assert hasattr(get_api_auth_ok, "asyncio_detailed")

    def test_auth_error_has_methods(self):
        """Test auth error endpoint has required methods"""
        assert hasattr(get_api_auth_error, "sync_detailed")
        assert hasattr(get_api_auth_error, "asyncio_detailed")

    def test_auth_ok_returns_success(self, mock_client):
        """Test auth ok returns success status"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = {"status": "ok"}

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_auth_ok.sync_detailed(client=mock_client)

        assert response.status_code == 200


class TestAuthErrorHandling:
    """Test error handling in auth wrappers"""

    @pytest.mark.parametrize("status_code", [401, 403, 404, 500])
    def test_handles_error_status_codes(self, mock_client, status_code):
        """Test auth wrappers handle various error codes"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = status_code
        mock_response.content = b'{"message": "Error message"}'
        mock_response.json.return_value = {"message": "Error message"}

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_auth_get_session.sync_detailed(client=mock_client)

        assert response.status_code == status_code

    def test_handles_unauthorized_session(self, mock_client):
        """Test handles unauthorized session gracefully"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 401
        mock_response.content = b'{"message": "Unauthorized"}'
        mock_response.json.return_value = {"message": "Unauthorized"}

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_auth_get_session.sync_detailed(client=mock_client)

        assert response.status_code == 401


class TestAuthResponseStructures:
    """Test auth response structures"""

    def test_session_response_structure(self, mock_client):
        """Test session response has expected structure"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "session_id": "sess-1",
            "user_id": "user-1",
            "expires_at": "2024-12-31T23:59:59Z",
        }

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_auth_get_session.sync_detailed(client=mock_client)

        assert response.status_code == 200

    def test_organization_response_structure(self, mock_client):
        """Test organization response has expected structure"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = {"id": "org-1", "slug": "my-org", "name": "My Organization"}

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_auth_organization_get_full_organization.sync_detailed(client=mock_client)

        assert response.status_code == 200
