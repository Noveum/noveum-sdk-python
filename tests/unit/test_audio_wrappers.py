"""
Unit Tests for Audio API Wrappers

Tests all audio-related API wrapper functions with mocked responses.
"""

import io
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
from noveum_api_client.types import File


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

    def test_post_audio_accepts_required_parameters(self, mock_client):
        """Test upload accepts all required parameters"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 201
        mock_response.content = b'{"success": true, "data": {"id": "audio-123"}}'
        mock_response.json.return_value = {"success": True, "data": {"id": "audio-123"}}

        mock_client.get_httpx_client().request.return_value = mock_response

        # Create test file
        test_file = File(payload=io.BytesIO(b"fake audio data"), file_name="test.wav", mime_type="audio/wav")

        # Call with all required parameters
        response = post_api_v1_audio.sync_detailed(
            client=mock_client,
            file=test_file,
            trace_id="trace-123",
            span_id="span-456",
            audio_uuid="audio-uuid-789",
        )

        assert response.status_code == 201

        # Verify request was called
        mock_client.get_httpx_client().request.assert_called_once()

        # Verify request parameters
        call_kwargs = mock_client.get_httpx_client().request.call_args[1]
        assert call_kwargs["method"] == "post"
        assert call_kwargs["url"] == "/api/v1/audio"
        assert "files" in call_kwargs
        assert "data" in call_kwargs
        assert call_kwargs["data"]["traceId"] == "trace-123"
        assert call_kwargs["data"]["spanId"] == "span-456"
        assert call_kwargs["data"]["audio_uuid"] == "audio-uuid-789"

    def test_post_audio_builds_multipart_request(self, mock_client):
        """Test upload builds correct multipart/form-data request"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 201
        mock_response.content = b'{"success": true}'

        mock_client.get_httpx_client().request.return_value = mock_response

        test_file = File(payload=io.BytesIO(b"test audio content"), file_name="recording.mp3", mime_type="audio/mpeg")

        post_api_v1_audio.sync_detailed(
            client=mock_client,
            file=test_file,
            trace_id="trace-abc",
            span_id="span-def",
            audio_uuid="uuid-ghi",
        )

        # Verify multipart structure
        call_kwargs = mock_client.get_httpx_client().request.call_args[1]
        assert "files" in call_kwargs
        assert "file" in call_kwargs["files"]

        # File tuple should be (filename, payload, mime_type)
        file_tuple = call_kwargs["files"]["file"]
        assert file_tuple[0] == "recording.mp3"  # filename
        assert file_tuple[2] == "audio/mpeg"  # mime_type

    def test_post_audio_handles_upload_success(self, mock_client):
        """Test upload handles successful response"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 201
        mock_response.content = b'{"success": true, "data": {"id": "uploaded-id"}}'

        mock_client.get_httpx_client().request.return_value = mock_response

        test_file = File(payload=io.BytesIO(b"audio data"), file_name="test.wav", mime_type="audio/wav")

        response = post_api_v1_audio.sync_detailed(
            client=mock_client,
            file=test_file,
            trace_id="t1",
            span_id="s1",
            audio_uuid="a1",
        )

        assert response.status_code == 201

    def test_post_audio_handles_upload_error(self, mock_client):
        """Test upload handles error responses"""
        mock_response = Mock(spec=httpx.Response)
        mock_response.headers = {}
        mock_response.status_code = 400
        mock_response.content = b'{"error": "Invalid file"}'
        mock_response.json.return_value = {"error": "Invalid file"}

        mock_client.get_httpx_client().request.return_value = mock_response

        test_file = File(payload=io.BytesIO(b"invalid"), file_name="bad.txt", mime_type="text/plain")

        response = post_api_v1_audio.sync_detailed(
            client=mock_client,
            file=test_file,
            trace_id="t1",
            span_id="s1",
            audio_uuid="a1",
        )

        assert response.status_code == 400


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
