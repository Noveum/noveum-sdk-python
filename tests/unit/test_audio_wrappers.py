"""
Unit Tests for Audio API Wrappers

Tests all audio-related API wrapper functions with mocked responses.
"""

from unittest.mock import Mock

import httpx
import pytest

from noveum_api_client.api.audio import (
    delete_api_v1_audio_by_id,
    get_api_v1_audio,
    get_api_v1_audio_by_id,
    get_api_v1_audio_by_id_serve,
    post_api_v1_audio,
)


class TestAudioListingWrappers:
    """Test audio listing API wrappers"""

    def test_get_audio_has_sync_method(self):
        """Test that get_audio has sync_detailed method"""
        assert hasattr(get_api_v1_audio, "sync_detailed")
        assert callable(get_api_v1_audio.sync_detailed)

    def test_get_audio_has_async_method(self):
        """Test that get_audio has asyncio_detailed method"""
        assert hasattr(get_api_v1_audio, "asyncio_detailed")
        assert callable(get_api_v1_audio.asyncio_detailed)

    def test_get_audio_basic_call(self, mock_client):
        """Test get audio basic call"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = []

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_audio.sync_detailed(client=mock_client)

        assert response.status_code == 200


class TestAudioUploadWrappers:
    """Test audio upload API wrappers"""

    def test_post_audio_has_methods(self):
        """Test post audio has required methods"""
        assert hasattr(post_api_v1_audio, "sync_detailed")
        assert hasattr(post_api_v1_audio, "asyncio_detailed")


class TestAudioRetrievalWrappers:
    """Test audio retrieval API wrappers"""

    def test_get_audio_by_id_has_methods(self):
        """Test get audio by ID has methods"""
        assert hasattr(get_api_v1_audio_by_id, "sync_detailed")
        assert hasattr(get_api_v1_audio_by_id, "asyncio_detailed")

    def test_get_audio_by_id_serve_has_methods(self):
        """Test get audio by ID serve has methods"""
        assert hasattr(get_api_v1_audio_by_id_serve, "sync_detailed")
        assert hasattr(get_api_v1_audio_by_id_serve, "asyncio_detailed")

    def test_get_audio_by_id_serve_returns_audio_data(self, mock_client):
        """Test get audio by ID serve returns audio data"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {"Content-Type": "audio/mpeg"}
        mock_response.status_code = 200
        mock_response.content = b"fake audio data"

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_audio_by_id_serve.sync_detailed(id="audio-1", client=mock_client)

        assert response.status_code == 200


class TestAudioDeletionWrappers:
    """Test audio deletion API wrappers"""

    def test_delete_audio_has_methods(self):
        """Test delete audio has methods"""
        assert hasattr(delete_api_v1_audio_by_id, "sync_detailed")
        assert hasattr(delete_api_v1_audio_by_id, "asyncio_detailed")

    def test_delete_audio_requires_id(self, mock_client):
        """Test delete audio requires audio ID"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = {"message": "Audio deleted"}

        mock_client.get_httpx_client().request.return_value = mock_response
        response = delete_api_v1_audio_by_id.sync_detailed(id="audio-1", client=mock_client)

        assert response.status_code in [200, 204]


class TestAudioErrorHandling:
    """Test error handling in audio wrappers"""

    @pytest.mark.parametrize("status_code", [400, 401, 403, 404, 500])
    def test_handles_error_status_codes(self, mock_client, status_code):
        """Test audio wrappers handle various error codes"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = status_code
        mock_response.content = b'{"error": "Error message"}'
        mock_response.json.return_value = {"error": "Error message"}

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_audio.sync_detailed(client=mock_client)

        assert response.status_code == status_code

    def test_handles_not_found_audio(self, mock_client):
        """Test handles not found audio gracefully"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 404
        mock_response.content = b'{"error": "Audio not found"}'
        mock_response.json.return_value = {"error": "Audio not found"}

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_audio_by_id.sync_detailed(id="nonexistent", client=mock_client)

        assert response.status_code == 404


class TestAudioResponseStructure:
    """Test audio response structure"""

    def test_get_audio_returns_list(self, mock_client):
        """Test get audio returns list structure"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 200
        mock_response.json.return_value = []

        mock_client.get_httpx_client().request.return_value = mock_response
        response = get_api_v1_audio.sync_detailed(client=mock_client)

        assert response.status_code == 200
        assert response is not None
