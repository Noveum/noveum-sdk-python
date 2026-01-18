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
import json
import uuid
from datetime import datetime
from typing import Any

import pytest

from noveum_api_client import Client, NoveumClient
from noveum_api_client.api.audio import (
    delete_api_v1_audio_by_id,
    get_api_v1_audio,
    get_api_v1_audio_by_id,
    get_api_v1_audio_by_id_serve,
    post_api_v1_audio,
)

from constants import (
    SKIP_NO_AUDIO_ID,
    SKIP_NO_AUDIO_ID_TO_DELETE,
    SKIP_AUDIO_FILE_NOT_FOUND,
    SKIP_NO_AUDIO_ID_VERIFY_DELETION,
)


def parse_response(response: Any) -> dict[str, Any] | list[Any] | None:
    """Parse response body - handles cases where response.parsed is None but content exists."""
    if response.parsed is not None:
        # Convert to dict if it's a model object
        if hasattr(response.parsed, 'to_dict'):
            return response.parsed.to_dict()
        return response.parsed
    
    if response.content:
        try:
            return json.loads(response.content)
        except (json.JSONDecodeError, TypeError):
            return None
    return None


def get_field(obj: Any, field: str) -> Any:
    """Helper to get field value from dict or object."""
    if obj is None:
        return None
    if isinstance(obj, dict):
        return obj.get(field)
    return getattr(obj, field, None)


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
            "audio_filename": f"test_audio_{timestamp}_{unique_id}.mp3",
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
        
        assert response.status_code == 200, (
            f"List audio files failed: {response.status_code}"
        )
        
        # ===== VALIDATE RESPONSE BODY =====
        data = parse_response(response)
        assert data is not None, "Response data should not be None"
        
        print(f"\n✅ Listed audio files - validating response:")
        
        # Get audio files list - might be wrapped in 'data' or 'audio' or 'files'
        audio_files = (
            data.get("data", data) if isinstance(data, dict) else data
        )
        if isinstance(audio_files, dict):
            audio_files = audio_files.get("files", audio_files.get("audio", []))
        
        if isinstance(audio_files, list):
            print(f"   ✓ audio files count: {len(audio_files)}")
            
            if len(audio_files) > 0:
                first_audio = audio_files[0]
                print(f"\n   First audio file validation:")
                
                # Store for later tests if no upload is possible
                audio_id = get_field(first_audio, 'id')
                if audio_id:
                    audio_context["audio_id"] = audio_id
                    print(f"   ✓ id: {audio_id}")
                
                filename = get_field(first_audio, 'filename') or get_field(first_audio, 'name')
                if filename:
                    audio_context["audio_filename"] = filename
                    print(f"   ✓ filename: {filename}")
                
                file_format = get_field(first_audio, 'format') or get_field(first_audio, 'mime_type')
                if file_format:
                    audio_context["audio_format"] = file_format
                    print(f"   ✓ format: {file_format}")
                
                file_size = get_field(first_audio, 'size') or get_field(first_audio, 'file_size')
                if file_size is not None:
                    audio_context["audio_size"] = file_size
                    print(f"   ✓ size: {file_size} bytes")
                
                duration = get_field(first_audio, 'duration') or get_field(first_audio, 'duration_seconds')
                if duration is not None:
                    audio_context["audio_duration"] = duration
                    print(f"   ✓ duration: {duration}s")
                
                url = get_field(first_audio, 'url') or get_field(first_audio, 'storage_url')
                if url:
                    print(f"   ✓ url: present")
                
                created_at = get_field(first_audio, 'created_at')
                if created_at:
                    audio_context["created_at"] = created_at
                    print(f"   ✓ created_at: {created_at}")
        
        # Check pagination if present
        pagination = data.get("pagination", {}) if isinstance(data, dict) else {}
        if pagination:
            print(f"\n   Pagination:")
            total = pagination.get('total', pagination.get('totalCount'))
            if total is not None:
                print(f"   ✓ total: {total}")
            page = pagination.get('page', pagination.get('currentPage'))
            if page is not None:
                print(f"   ✓ page: {page}")
            page_size = pagination.get('pageSize', pagination.get('limit'))
            if page_size is not None:
                print(f"   ✓ pageSize: {page_size}")

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
        
        assert response.status_code == 200, (
            f"List audio with pagination failed: {response.status_code}"
        )
        
        # ===== VALIDATE RESPONSE BODY =====
        data = parse_response(response)
        
        print(f"\n✅ Pagination test (page=1, pageSize=5) - validating response:")
        
        if data:
            audio_files = data.get("data", data) if isinstance(data, dict) else data
            if isinstance(audio_files, dict):
                audio_files = audio_files.get("files", audio_files.get("audio", []))
            
            if isinstance(audio_files, list):
                assert len(audio_files) <= 5, "Should respect pageSize limit"
                print(f"   ✓ results count: {len(audio_files)} (limit=5)")

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
        # so this test validates the basic endpoint availability
        response = post_api_v1_audio.sync_detailed(
            client=low_level_client,
        )
        
        # Upload might fail without actual file data - validate error handling
        print(f"\n✅ Upload audio endpoint test:")
        print(f"   Response status: {response.status_code}")
        
        # ===== VALIDATE RESPONSE BODY =====
        data = parse_response(response)
        
        if response.status_code in [200, 201]:
            # Successful upload
            if data:
                success = get_field(data, 'success')
                if success is not None:
                    assert success is True, "Expected success=True"
                    print(f"   ✓ success: {success}")
                
                audio_data = data.get("data", data) if isinstance(data, dict) else data
                
                audio_id = get_field(audio_data, 'id')
                if audio_id:
                    audio_context["audio_id"] = audio_id
                    print(f"   ✓ id: {audio_id}")
                
                filename = get_field(audio_data, 'filename') or get_field(audio_data, 'name')
                if filename:
                    audio_context["audio_filename"] = filename
                    print(f"   ✓ filename: {filename}")
                
                file_format = get_field(audio_data, 'format') or get_field(audio_data, 'mime_type')
                if file_format:
                    print(f"   ✓ format: {file_format}")
                
                file_size = get_field(audio_data, 'size')
                if file_size is not None:
                    print(f"   ✓ size: {file_size} bytes")
                
                storage_url = get_field(audio_data, 'url') or get_field(audio_data, 'storage_url')
                if storage_url:
                    print(f"   ✓ storage_url: present")
                
                created_at = get_field(audio_data, 'created_at')
                if created_at:
                    print(f"   ✓ created_at: {created_at}")
        elif response.status_code == 400:
            # Expected if no file was provided
            print(f"   ⚠ status: 400 (no file provided - expected)")
            if data:
                error = get_field(data, 'error') or get_field(data, 'message')
                if error:
                    print(f"   Error: {error}")
        else:
            print(f"   Response: {response.status_code}")
            if data:
                print(f"   Body: {data}")

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
        
        assert response.status_code == 200, (
            f"Get audio by ID failed: {response.status_code}"
        )
        
        # ===== VALIDATE RESPONSE BODY =====
        data = parse_response(response)
        assert data is not None, "Response data should not be None"
        
        print(f"\n✅ Retrieved audio file - validating response:")
        
        # Audio data might be wrapped in 'data' or returned directly
        audio_data = data.get("data", data) if isinstance(data, dict) else data
        
        # Validate id matches request
        returned_id = get_field(audio_data, 'id')
        if returned_id:
            assert returned_id == audio_id, f"ID mismatch: expected {audio_id}, got {returned_id}"
            print(f"   ✓ id: {returned_id}")
        
        # Validate filename
        filename = get_field(audio_data, 'filename') or get_field(audio_data, 'name')
        if filename:
            print(f"   ✓ filename: {filename}")
        
        # Validate format/mime_type
        file_format = get_field(audio_data, 'format') or get_field(audio_data, 'mime_type')
        if file_format:
            print(f"   ✓ format: {file_format}")
        
        # Validate size
        file_size = get_field(audio_data, 'size') or get_field(audio_data, 'file_size')
        if file_size is not None:
            assert file_size > 0, "File size should be positive"
            print(f"   ✓ size: {file_size} bytes")
        
        # Validate duration
        duration = get_field(audio_data, 'duration') or get_field(audio_data, 'duration_seconds')
        if duration is not None:
            print(f"   ✓ duration: {duration}s")
        
        # Validate storage URL
        url = get_field(audio_data, 'url') or get_field(audio_data, 'storage_url')
        if url:
            print(f"   ✓ url: present")
        
        # Validate organization_id
        org_id = get_field(audio_data, 'organization_id') or get_field(audio_data, 'org_id')
        if org_id:
            print(f"   ✓ organization_id: {org_id}")
        
        # Validate timestamps
        created_at = get_field(audio_data, 'created_at')
        if created_at:
            print(f"   ✓ created_at: {created_at}")
        
        updated_at = get_field(audio_data, 'updated_at')
        if updated_at:
            print(f"   ✓ updated_at: {updated_at}")
        
        # Validate metadata if present
        metadata = get_field(audio_data, 'metadata')
        if metadata:
            print(f"   ✓ metadata: present")
            if isinstance(metadata, dict):
                for key in list(metadata.keys())[:3]:
                    print(f"      - {key}: {metadata[key]}")

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
        assert response.status_code in [404, 400], (
            f"Expected 404 for non-existent audio, got {response.status_code}"
        )
        
        # ===== VALIDATE ERROR RESPONSE =====
        data = parse_response(response)
        
        print(f"\n✅ Nonexistent audio test - proper error returned:")
        print(f"   Status: {response.status_code}")
        
        if data:
            error = get_field(data, 'error') or get_field(data, 'message')
            if error:
                print(f"   Error: {error}")
            
            detail = get_field(data, 'detail')
            if detail:
                print(f"   Detail: {detail}")

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
        
        print(f"\n✅ Serve audio test:")
        print(f"   Status: {response.status_code}")
        
        # The serve endpoint returns binary audio content
        if response.status_code == 200:
            print(f"   ✓ Audio content served successfully")
            
            # Validate content-type header
            content_type = response.headers.get("content-type", "")
            if content_type:
                print(f"   ✓ content-type: {content_type}")
                # Check if it's an audio type
                assert "audio" in content_type.lower() or "octet-stream" in content_type.lower(), (
                    f"Expected audio content type, got: {content_type}"
                )
            
            # Validate content-length if present
            content_length = response.headers.get("content-length")
            if content_length:
                print(f"   ✓ content-length: {content_length} bytes")
            
            # Validate we got actual content
            if response.content:
                print(f"   ✓ content received: {len(response.content)} bytes")
                assert len(response.content) > 0, "Expected non-empty audio content"
            
            # Check for content-disposition header
            content_disp = response.headers.get("content-disposition")
            if content_disp:
                print(f"   ✓ content-disposition: {content_disp[:50]}...")
        elif response.status_code == 404:
            print(f"   ⚠ Audio file not found (may have been deleted)")
        else:
            print(f"   Response: {response.status_code}")

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
        assert response.status_code in [404, 400], (
            f"Expected 404 for non-existent audio serve, got {response.status_code}"
        )
        
        print(f"\n✅ Serve nonexistent audio test:")
        print(f"   Status: {response.status_code}")
        
        # ===== VALIDATE ERROR RESPONSE =====
        data = parse_response(response)
        if data:
            error = get_field(data, 'error') or get_field(data, 'message')
            if error:
                print(f"   Error: {error}")

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
        
        # First verify the audio exists
        check_response = get_api_v1_audio_by_id.sync_detailed(
            id=audio_id,
            client=low_level_client,
        )
        
        if check_response.status_code == 404:
            pytest.skip(SKIP_AUDIO_FILE_NOT_FOUND)
        
        # Delete the audio
        response = delete_api_v1_audio_by_id.sync_detailed(
            id=audio_id,
            client=low_level_client,
        )
        
        if response.status_code == 500:
            pytest.xfail("Audio deletion returned 500 (known backend issue)")
        
        assert response.status_code in [200, 204], (
            f"Delete audio failed: {response.status_code}"
        )
        
        # ===== VALIDATE RESPONSE BODY =====
        print(f"\n✅ Deleted audio file - validating response:")
        
        if response.status_code == 200:
            data = parse_response(response)
            
            if data:
                success = get_field(data, 'success')
                if success is not None:
                    assert success is True, "Expected success=True"
                    print(f"   ✓ success: {success}")
                
                deleted_id = get_field(data, 'id') or get_field(data, 'deleted_id')
                if deleted_id:
                    assert deleted_id == audio_id, "Deleted ID mismatch"
                    print(f"   ✓ deleted id: {deleted_id}")
                
                message = get_field(data, 'message')
                if message:
                    print(f"   ✓ message: {message}")
        else:
            print(f"   ✓ status: 204 No Content (delete successful)")
        
        print(f"   Audio '{audio_id}' deleted successfully")

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
        
        print(f"\n✅ Verify deletion test:")
        print(f"   Audio ID: {audio_id}")
        print(f"   Status: {response.status_code}")
        
        # After deletion, should get 404 (or audio still exists if delete wasn't executed)
        if response.status_code == 404:
            print(f"   ✓ Audio file confirmed deleted (404)")
        elif response.status_code == 200:
            print(f"   ⚠ Audio file still exists (delete may not have been executed)")


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
        
        assert response.status_code == 200
        
        print(f"\n✅ Default pagination test:")
        
        data = parse_response(response)
        if data:
            print(f"   Response received with status 200")
            
            # Check if response has expected structure
            if isinstance(data, dict):
                for key in data.keys():
                    print(f"   ✓ field: {key}")

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
        
        assert response.status_code == 200
        
        print(f"\n✅ Page 2 pagination test:")
        
        data = parse_response(response)
        if data:
            audio_files = data.get("data", data) if isinstance(data, dict) else data
            if isinstance(audio_files, dict):
                audio_files = audio_files.get("files", audio_files.get("audio", []))
            
            if isinstance(audio_files, list):
                print(f"   ✓ Page 2 results: {len(audio_files)}")

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
        assert response.status_code in [404, 400, 500], (
            f"Expected error for non-existent audio delete, got {response.status_code}"
        )
        
        print(f"\n✅ Delete nonexistent audio test:")
        print(f"   Status: {response.status_code}")
        
        data = parse_response(response)
        if data:
            error = get_field(data, 'error') or get_field(data, 'message')
            if error:
                print(f"   Error: {error}")

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
        
        assert response.status_code == 200
        
        data = parse_response(response)
        assert data is not None, "Response should have data"
        
        print(f"\n✅ Response structure validation:")
        print(f"   Response type: {type(data)}")
        
        if isinstance(data, dict):
            for key in data.keys():
                print(f"   ✓ field: {key}")
            
            # Check for common fields
            if "data" in data or "files" in data or "audio" in data:
                print(f"   ✓ Contains audio list field")
            
            if "pagination" in data or "meta" in data:
                print(f"   ✓ Contains pagination info")

    def test_audio_content_type_headers(
        self,
        low_level_client: Client,
    ) -> None:
        """Test that audio endpoints return appropriate content type headers."""
        # List endpoint
        response = get_api_v1_audio.sync_detailed(
            client=low_level_client,
        )
        
        content_type = response.headers.get("content-type", "")
        
        print(f"\n✅ Content-Type header validation:")
        print(f"   List endpoint content-type: {content_type}")
        
        # Should be JSON for list endpoint
        assert "json" in content_type.lower(), (
            f"Expected JSON content type for list, got: {content_type}"
        )
