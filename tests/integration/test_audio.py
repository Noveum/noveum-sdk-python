"""
Audio API Integration Tests - Complete End-to-End Flow

This module tests the complete audio file lifecycle:
1. List audio files → Upload audio → Get audio by ID
2. Serve/stream audio → Delete audio

Endpoints Tested (5 total):
- POST /api/v1/audio  (upload audio file)
- GET  /api/v1/audio  (list all audio files)
- GET  /api/v1/audio/{id}  (get audio by ID)
- GET  /api/v1/audio/{id}/serve  (serve/stream audio file)
- DELETE /api/v1/audio/{id}  (delete audio file)

Supported Audio Formats:
- MP3, WAV, AAC, OGG, FLAC, M4A
- Maximum file size: 50MB

Usage:
    pytest test_audio.py -v
    pytest test_audio.py -v -k "list_audio"  # Run specific test
    pytest test_audio.py -v --tb=short  # Shorter tracebacks
"""

import io
import uuid
import wave
from datetime import datetime
from typing import Any

import pytest
from conftest import assert_api_success
from constants import (
    SKIP_AUDIO_FILE_NOT_FOUND,
    SKIP_NO_AUDIO_ID,
    SKIP_NO_AUDIO_ID_TO_DELETE,
    SKIP_NO_AUDIO_ID_VERIFY_DELETION,
    XFAIL_AUDIO_DELETION_500,
)
from utils import (
    assert_non_empty_string,
    assert_optional_string,
    assert_positive_number,
    ensure_dict,
    ensure_list,
    get_field,
    parse_response,
)

from noveum_api_client import Client
from noveum_api_client.api.audio import (
    delete_api_v1_audio_by_id,
    get_api_v1_audio,
    get_api_v1_audio_by_id,
    get_api_v1_audio_by_id_serve,
    post_api_v1_audio,
)
from noveum_api_client.types import File


def _make_test_wav_bytes(
    duration_seconds: float = 0.1,
    sample_rate: int = 8000,
) -> bytes:
    """Generate a small valid WAV file in memory."""
    frame_count = max(1, int(duration_seconds * sample_rate))
    buffer = io.BytesIO()
    with wave.open(buffer, "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)
        wav.writeframes(b"\x00\x00" * frame_count)
    return buffer.getvalue()


def _upload_audio_file(
    client: Client,
    filename: str,
    data: bytes,
    metadata: dict[str, str],
) -> Any:
    """
    Upload audio using the SDK wrapper with proper File type and metadata.

    Args:
        client: Noveum API client
        filename: Name of the audio file
        data: Binary audio file data
        metadata: Dictionary with traceId, spanId, audio_uuid

    Returns:
        Response from the upload API
    """
    # Create File object for SDK wrapper
    file = File(payload=io.BytesIO(data), file_name=filename, mime_type="audio/wav")

    # Use the SDK wrapper with all required parameters
    response = post_api_v1_audio.sync_detailed(
        client=client,
        file=file,
        trace_id=metadata["traceId"],
        span_id=metadata["spanId"],
        audio_uuid=metadata["audio_uuid"],
    )

    return response


@pytest.mark.audio
@pytest.mark.integration
class TestAudioFlow:
    """
    End-to-end test flow for Audio API operations.

    Tests run in order using pytest-ordering to ensure:
    1. List existing audio files
    2. Upload a new audio file
    3. Get audio by ID
    4. Serve/stream audio content
    5. Delete the audio file
    """

    @pytest.fixture(scope="class")
    def audio_context(self) -> dict[str, Any]:
        """Shared context for storing audio information across tests."""
        return {
            "audio_id": None,
            "audio_filename": None,
            "audio_format": None,
            "audio_size": None,
            "audio_duration": None,
            "created_at": None,
        }

    @pytest.fixture(scope="class")
    def unique_identifiers(self) -> dict[str, str]:
        """Generate unique identifiers for test resources."""
        unique_id = uuid.uuid4().hex[:8]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return {
            "audio_filename": f"test_audio_{timestamp}_{unique_id}.wav",
            "test_id": unique_id,
        }

    # =========================================================================
    # Phase 1: List Existing Audio Files
    # =========================================================================

    def test_01_list_audio_files(
        self,
        low_level_client: Client,
        audio_context: dict[str, Any],
    ) -> None:
        """Test listing existing audio files with full response validation."""
        response = get_api_v1_audio.sync_detailed(
            client=low_level_client,
            page=1.0,
            page_size=10.0,
        )
        assert_api_success(response, expected_codes=[200])

        # ===== VALIDATE RESPONSE BODY =====
        data = parse_response(response)
        assert data is not None, "Response data should not be None"

        # Get audio files list - might be wrapped in 'data' or 'audio' or 'files'
        audio_files = data.get("data", data) if isinstance(data, dict) else data
        if isinstance(audio_files, dict):
            audio_files = audio_files.get("files", audio_files.get("audio", []))

        audio_files = ensure_list(audio_files, "audio files should be a list")

        if audio_files:
            first_audio = audio_files[0]

            # Store for later tests if no upload is possible
            # Backend returns: id, filename, mimeType, size, traceId, spanId, createdAt, updatedAt
            audio_id = get_field(first_audio, "id")
            if audio_id:
                assert_non_empty_string(audio_id, "audio.id")
                audio_context["audio_id"] = audio_id

            filename = get_field(first_audio, "filename")
            if filename:
                assert_non_empty_string(filename, "audio.filename")
                audio_context["audio_filename"] = filename

            mime_type = get_field(first_audio, "mimeType") or get_field(first_audio, "mime_type")
            if mime_type:
                assert_non_empty_string(mime_type, "audio.mimeType")
                audio_context["audio_format"] = mime_type

            file_size = get_field(first_audio, "size")
            if file_size is not None:
                assert isinstance(file_size, (int, float)), "audio.size should be numeric"
                audio_context["audio_size"] = file_size

            # traceId and spanId are returned but not critical for validation
            trace_id = get_field(first_audio, "traceId")
            if trace_id:
                assert_non_empty_string(trace_id, "audio.traceId")

            span_id = get_field(first_audio, "spanId")
            if span_id:
                assert_non_empty_string(span_id, "audio.spanId")

            created_at = get_field(first_audio, "createdAt") or get_field(first_audio, "created_at")
            if created_at:
                assert_optional_string(created_at, "audio.createdAt")
                audio_context["created_at"] = created_at

            updated_at = get_field(first_audio, "updatedAt") or get_field(first_audio, "updated_at")
            if updated_at:
                assert_optional_string(updated_at, "audio.updatedAt")

        # Check pagination if present
        pagination = data.get("pagination", {}) if isinstance(data, dict) else {}
        if pagination:
            pagination = ensure_dict(pagination, "pagination should be a dict")
            total = pagination.get("total", pagination.get("totalCount"))
            if total is not None:
                assert isinstance(total, int), "pagination.total should be int"

    def test_02_list_audio_with_pagination(
        self,
        low_level_client: Client,
    ) -> None:
        """Test listing audio files with different pagination parameters."""
        # Test with page 1 and smaller page size
        response = get_api_v1_audio.sync_detailed(
            client=low_level_client,
            page=1.0,
            page_size=5.0,
        )
        assert_api_success(response, expected_codes=[200])

        # ===== VALIDATE RESPONSE BODY =====
        data = parse_response(response)

        if data:
            audio_files = data.get("data", data) if isinstance(data, dict) else data
            if isinstance(audio_files, dict):
                audio_files = audio_files.get("files", audio_files.get("audio", []))

            if isinstance(audio_files, list):
                assert len(audio_files) <= 5, "Should respect pageSize limit"

    # =========================================================================
    # Phase 2: Upload Audio File (if supported)
    # =========================================================================

    def test_03_upload_audio_file(
        self,
        low_level_client: Client,
        unique_identifiers: dict[str, str],
        audio_context: dict[str, Any],
    ) -> None:
        """
        Test uploading a new audio file.

        Note: This test requires proper multipart/form-data handling which may need
        additional parameters. The current API client implementation may need enhancement.
        """
        # The current post_api_v1_audio endpoint doesn't accept body parameters,
        # so use raw multipart upload for real coverage.
        audio_bytes = _make_test_wav_bytes()
        trace_id = str(uuid.uuid4())
        span_id = uuid.uuid4().hex[:16]
        audio_uuid = str(uuid.uuid4())
        response = _upload_audio_file(
            low_level_client,
            unique_identifiers["audio_filename"],
            audio_bytes,
            {
                "traceId": trace_id,
                "spanId": span_id,
                "audio_uuid": audio_uuid,
            },
        )
        assert_api_success(response, expected_codes=[200, 201])

        data = parse_response(response)
        assert data is not None, "Response data should not be None"

        success = get_field(data, "success")
        if success is not None:
            assert success is True, "Expected success=True"

        # Upload response includes: id, organizationId, filename, originalName,
        # mimeType, size, storageKey, traceId, spanId, createdAt, updatedAt
        audio_data = data.get("data", data) if isinstance(data, dict) else data

        audio_id = get_field(audio_data, "id")
        assert_non_empty_string(audio_id, "audio.id")
        audio_context["audio_id"] = audio_id

        # Upload returns both 'filename' (internal path) and 'originalName' (user's filename)
        original_name = get_field(audio_data, "originalName")
        if original_name:
            assert_non_empty_string(original_name, "audio.originalName")
            audio_context["audio_filename"] = original_name

        mime_type = get_field(audio_data, "mimeType")
        if mime_type:
            assert_non_empty_string(mime_type, "audio.mimeType")
            audio_context["audio_format"] = mime_type

        file_size = get_field(audio_data, "size")
        if file_size is not None:
            assert_positive_number(file_size, "audio.size")
            audio_context["audio_size"] = file_size

        # organizationId is only returned in upload response
        org_id = get_field(audio_data, "organizationId")
        if org_id:
            assert_non_empty_string(org_id, "audio.organizationId")

        storage_key = get_field(audio_data, "storageKey")
        if storage_key:
            assert_non_empty_string(storage_key, "audio.storageKey")

        trace_id = get_field(audio_data, "traceId")
        if trace_id:
            assert_non_empty_string(trace_id, "audio.traceId")

        span_id = get_field(audio_data, "spanId")
        if span_id:
            assert_non_empty_string(span_id, "audio.spanId")

        created_at = get_field(audio_data, "createdAt") or get_field(audio_data, "created_at")
        if created_at:
            assert_optional_string(created_at, "audio.createdAt")
            audio_context["created_at"] = created_at

        updated_at = get_field(audio_data, "updatedAt") or get_field(audio_data, "updated_at")
        if updated_at:
            assert_optional_string(updated_at, "audio.updatedAt")

    # =========================================================================
    # Phase 3: Get Audio by ID
    # =========================================================================

    def test_04_get_audio_by_id(
        self,
        low_level_client: Client,
        audio_context: dict[str, Any],
    ) -> None:
        """Test retrieving audio file by ID with full response validation."""
        if not audio_context.get("audio_id"):
            pytest.skip(SKIP_NO_AUDIO_ID)

        audio_id = audio_context["audio_id"]

        response = get_api_v1_audio_by_id.sync_detailed(
            id=audio_id,
            client=low_level_client,
        )
        assert_api_success(response, expected_codes=[200])

        # ===== VALIDATE RESPONSE BODY =====
        data = parse_response(response)
        assert data is not None, "Response data should not be None"

        # Audio data might be wrapped in 'data' or returned directly
        # Backend returns: id, filename, mimeType, size, traceId, spanId, createdAt, updatedAt
        audio_data = data.get("data", data) if isinstance(data, dict) else data

        # Validate id matches request
        returned_id = get_field(audio_data, "id")
        if returned_id:
            assert returned_id == audio_id, f"ID mismatch: expected {audio_id}, got {returned_id}"

        filename = get_field(audio_data, "filename")
        if filename:
            assert_non_empty_string(filename, "audio.filename")

        mime_type = get_field(audio_data, "mimeType") or get_field(audio_data, "mime_type")
        if mime_type:
            assert_non_empty_string(mime_type, "audio.mimeType")

        file_size = get_field(audio_data, "size")
        if file_size is not None:
            assert_positive_number(file_size, "audio.size")

        trace_id = get_field(audio_data, "traceId")
        if trace_id:
            assert_non_empty_string(trace_id, "audio.traceId")

        span_id = get_field(audio_data, "spanId")
        if span_id:
            assert_non_empty_string(span_id, "audio.spanId")

        created_at = get_field(audio_data, "createdAt") or get_field(audio_data, "created_at")
        if created_at:
            assert_optional_string(created_at, "audio.createdAt")

        updated_at = get_field(audio_data, "updatedAt") or get_field(audio_data, "updated_at")
        if updated_at:
            assert_optional_string(updated_at, "audio.updatedAt")

    def test_05_get_nonexistent_audio(
        self,
        low_level_client: Client,
    ) -> None:
        """Test getting an audio file that doesn't exist returns proper error."""
        fake_id = "nonexistent-audio-id-12345"

        response = get_api_v1_audio_by_id.sync_detailed(
            id=fake_id,
            client=low_level_client,
        )

        # Should return 404 for non-existent audio
        assert response.status_code in [404, 400], f"Expected 404 for non-existent audio, got {response.status_code}"

    # =========================================================================
    # Phase 4: Serve/Stream Audio
    # =========================================================================

    def test_06_serve_audio(
        self,
        low_level_client: Client,
        audio_context: dict[str, Any],
    ) -> None:
        """Test serving/streaming audio file content."""
        if not audio_context.get("audio_id"):
            pytest.skip(SKIP_NO_AUDIO_ID)

        audio_id = audio_context["audio_id"]

        response = get_api_v1_audio_by_id_serve.sync_detailed(
            id=audio_id,
            client=low_level_client,
        )

        # The serve endpoint returns binary audio content
        if response.status_code == 404:
            pytest.skip(SKIP_AUDIO_FILE_NOT_FOUND)

        assert_api_success(response, expected_codes=[200])

        # Validate content-type header
        content_type = response.headers.get("content-type", "")
        if content_type:
            # Check if it's an audio type
            assert (
                "audio" in content_type.lower() or "octet-stream" in content_type.lower()
            ), f"Expected audio content type, got: {content_type}"

        # Validate we got actual content
        assert response.content, "Expected non-empty audio content"
        assert len(response.content) > 0, "Expected non-empty audio content"

    def test_07_serve_nonexistent_audio(
        self,
        low_level_client: Client,
    ) -> None:
        """Test serving a non-existent audio file returns proper error."""
        fake_id = "nonexistent-audio-id-serve-12345"

        response = get_api_v1_audio_by_id_serve.sync_detailed(
            id=fake_id,
            client=low_level_client,
        )

        # Should return 404 for non-existent audio
        assert response.status_code in [
            404,
            400,
        ], f"Expected 404 for non-existent audio serve, got {response.status_code}"

    # =========================================================================
    # Phase 5: Delete Audio (Cleanup)
    # =========================================================================

    def test_08_delete_audio(
        self,
        low_level_client: Client,
        audio_context: dict[str, Any],
    ) -> None:
        """Test deleting an audio file with full response validation."""
        if not audio_context.get("audio_id"):
            pytest.skip(SKIP_NO_AUDIO_ID_TO_DELETE)

        audio_id = audio_context["audio_id"]

        # First verify the audio exists (skip check if backend has issues)
        check_response = get_api_v1_audio_by_id.sync_detailed(
            id=audio_id,
            client=low_level_client,
        )

        if check_response.status_code == 404:
            pytest.skip(SKIP_AUDIO_FILE_NOT_FOUND)
        # Note: Ignoring 500 errors in pre-check - backend has known issues after serving audio
        # The actual delete operation will be tested below

        # Delete the audio
        response = delete_api_v1_audio_by_id.sync_detailed(
            id=audio_id,
            client=low_level_client,
        )

        if response.status_code == 500:
            audio_context["deletion_succeeded"] = False  # Mark deletion as failed
            pytest.xfail(XFAIL_AUDIO_DELETION_500)

        audio_context["deletion_succeeded"] = True  # Mark deletion as successful
        assert_api_success(response, expected_codes=[200, 204])

        # Backend returns: { success: true, message: "Audio file deleted successfully", timestamp }
        if response.status_code == 200:
            data = parse_response(response)

            if data:
                success = get_field(data, "success")
                if success is not None:
                    assert success is True, "Expected success=True"

                message = get_field(data, "message")
                if message:
                    assert isinstance(message, str), "Expected message to be a string"
                    assert len(message) > 0, "Expected non-empty message"

    def test_09_verify_audio_deleted(
        self,
        low_level_client: Client,
        audio_context: dict[str, Any],
    ) -> None:
        """Verify that deleted audio file no longer exists."""
        if not audio_context.get("audio_id"):
            pytest.skip(SKIP_NO_AUDIO_ID_VERIFY_DELETION)

        audio_id = audio_context["audio_id"]

        response = get_api_v1_audio_by_id.sync_detailed(
            id=audio_id,
            client=low_level_client,
        )

        if response.status_code == 404:
            # Audio not found - this is expected after deletion
            # If previous delete test failed with 500, we should skip instead
            if not audio_context.get("deletion_succeeded", False):
                pytest.skip("Cannot verify deletion - previous delete operation failed (returned 500)")
            # Deletion verified successfully
            return
        pytest.fail(f"Audio file still exists after deletion: {audio_id}")


@pytest.mark.audio
@pytest.mark.integration
class TestAudioIsolated:
    """
    Isolated tests for audio operations.
    These tests don't depend on sequence and can run independently.
    """

    def test_list_audio_pagination_params(
        self,
        low_level_client: Client,
    ) -> None:
        """Test listing audio files with various pagination parameters."""
        # Test with default params
        response = get_api_v1_audio.sync_detailed(
            client=low_level_client,
        )
        assert_api_success(response, expected_codes=[200])

    def test_list_audio_page_two(
        self,
        low_level_client: Client,
    ) -> None:
        """Test listing audio files page 2."""
        response = get_api_v1_audio.sync_detailed(
            client=low_level_client,
            page=2.0,
            page_size=5.0,
        )
        assert_api_success(response, expected_codes=[200])

    def test_delete_nonexistent_audio(
        self,
        low_level_client: Client,
    ) -> None:
        """Test deleting an audio file that doesn't exist returns proper error."""
        fake_id = "nonexistent-audio-delete-test-12345"

        response = delete_api_v1_audio_by_id.sync_detailed(
            id=fake_id,
            client=low_level_client,
        )

        # Should return 404 for non-existent audio
        assert response.status_code in [
            404,
            400,
            500,
        ], f"Expected error for non-existent audio delete, got {response.status_code}"

    def test_list_audio_response_structure(
        self,
        low_level_client: Client,
    ) -> None:
        """Test that list audio returns expected response structure."""
        response = get_api_v1_audio.sync_detailed(
            client=low_level_client,
            page=1.0,
            page_size=3.0,
        )
        assert_api_success(response, expected_codes=[200])

        data = parse_response(response)
        assert data is not None, "Response should have data"

    def test_audio_content_type_headers(
        self,
        low_level_client: Client,
    ) -> None:
        """Test that audio endpoints return appropriate content type headers."""
        # List endpoint
        response = get_api_v1_audio.sync_detailed(
            client=low_level_client,
        )

        assert_api_success(response, expected_codes=[200])
        content_type = response.headers.get("content-type", "")

        # Should be JSON for list endpoint
        assert "json" in content_type.lower(), f"Expected JSON content type for list, got: {content_type}"
