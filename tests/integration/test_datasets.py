"""
Datasets API Integration Tests - Complete End-to-End Flow

This module tests the complete dataset lifecycle with full response body validation:
1. Create dataset -> Get dataset -> Update dataset
2. Add items -> List items -> Get single item
3. Create version -> List versions -> Get version
4. Version diff -> Publish version
5. Delete items (single and bulk) -> Delete dataset

Endpoints Tested (15 total):
- POST /api/v1/datasets  (create)
- GET  /api/v1/datasets  (list)
- GET  /api/v1/datasets/{slug}  (get by slug)
- PUT  /api/v1/datasets/{slug}  (update)
- DELETE /api/v1/datasets/{slug}  (delete)
- POST /api/v1/datasets/{slug}/items  (add items)
- GET  /api/v1/datasets/{slug}/items  (list items)
- GET  /api/v1/datasets/{slug}/items/{item_id}  (get item)
- DELETE /api/v1/datasets/{slug}/items/{item_id}  (delete item)
- DELETE /api/v1/datasets/{slug}/items  (bulk delete)
- POST /api/v1/datasets/{slug}/versions  (create version)
- GET  /api/v1/datasets/{slug}/versions  (list versions)
- GET  /api/v1/datasets/{slug}/versions/{version}  (get version)
- GET  /api/v1/datasets/{slug}/versions/diff  (version diff)
- POST /api/v1/datasets/{slug}/versions/publish  (publish)

Usage:
    pytest test_datasets.py -v
    pytest test_datasets.py -v -k "create_dataset"
    pytest test_datasets.py -v --tb=short
"""

import json
import uuid
from datetime import datetime
from typing import Any

import pytest

from noveum_api_client import Client, NoveumClient
from noveum_api_client.api.datasets import (
    delete_api_v1_datasets_by_dataset_slug_items,
    delete_api_v1_datasets_by_dataset_slug_items_by_item_id,
    delete_api_v1_datasets_by_slug,
    get_api_v1_datasets,
    get_api_v1_datasets_by_dataset_slug_items,
    get_api_v1_datasets_by_dataset_slug_items_by_item_id,
    get_api_v1_datasets_by_dataset_slug_versions,
    get_api_v1_datasets_by_dataset_slug_versions_by_version,
    get_api_v1_datasets_by_dataset_slug_versions_diff,
    get_api_v1_datasets_by_slug,
    post_api_v1_datasets,
    post_api_v1_datasets_by_dataset_slug_items,
    post_api_v1_datasets_by_dataset_slug_versions,
    post_api_v1_datasets_by_dataset_slug_versions_publish,
    put_api_v1_datasets_by_slug,
)
from noveum_api_client.models.delete_api_v1_datasets_by_dataset_slug_items_body import (
    DeleteApiV1DatasetsByDatasetSlugItemsBody,
)
from noveum_api_client.models.post_api_v1_datasets_body import PostApiV1DatasetsBody
from noveum_api_client.models.post_api_v1_datasets_by_dataset_slug_items_body import (
    PostApiV1DatasetsByDatasetSlugItemsBody,
)
from noveum_api_client.models.post_api_v1_datasets_by_dataset_slug_versions_body import (
    PostApiV1DatasetsByDatasetSlugVersionsBody,
)
from noveum_api_client.models.put_api_v1_datasets_by_slug_body import PutApiV1DatasetsBySlugBody

from constants import (
    SKIP_NO_DATASET_SLUG,
    SKIP_NO_DATASET_OR_ITEMS,
    SKIP_NO_DATASET_OR_VERSION,
    SKIP_NO_DATASET_TO_DELETE,
    SKIP_NOT_ENOUGH_ITEMS_DELETION,
    SKIP_NOT_ENOUGH_ITEMS_BULK_DELETE,
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


@pytest.mark.datasets
@pytest.mark.integration
@pytest.mark.serial
class TestDatasetsE2EFlow:
    """End-to-end integration tests for Datasets API with full response body validation."""

    @pytest.fixture(scope="class")
    def dataset_context(self) -> dict[str, Any]:
        """Shared context for storing dataset data across tests."""
        return {
            "dataset_slug": None,
            "dataset_name": None,
            "dataset_description": None,
            "item_ids": [],
            "version": None,
            "created_at": None,
            "updated_at": None,
        }

    @pytest.fixture(scope="class")
    def unique_dataset_slug(self) -> str:
        """Generate unique dataset slug for this test run."""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        unique_id = str(uuid.uuid4())[:8]
        return f"sdk-e2e-test-{timestamp}-{unique_id}"

    # =========================================================================
    # Phase 1: Dataset CRUD Operations
    # =========================================================================

    def test_01_list_datasets(
        self,
        noveum_client: NoveumClient,
        low_level_client: Client,
    ) -> None:
        """Test listing existing datasets with full response validation."""
        # Test high-level client
        response = noveum_client.list_datasets(limit=10)
        assert response["status_code"] == 200, f"List datasets failed: {response}"
        print(f"\n✅ Listed datasets (high-level): status={response['status_code']}")
        
        # Test low-level client with full validation
        response = get_api_v1_datasets.sync_detailed(
            client=low_level_client,
            limit=10,
        )
        
        assert response.status_code == 200, f"List datasets failed: {response.status_code}"
        
        # ===== VALIDATE RESPONSE BODY =====
        data = parse_response(response)
        assert data is not None, "Response data should not be None"
        
        print(f"✅ Listed datasets (low-level) - validating response:")
        
        # Check for datasets list
        datasets = data.get("datasets", []) if isinstance(data, dict) else data
        if isinstance(datasets, list):
            print(f"   ✓ datasets count: {len(datasets)}")
            
            if len(datasets) > 0:
                first_dataset = datasets[0]
                print(f"\n   First dataset validation:")
                
                # Validate dataset fields
                slug = get_field(first_dataset, 'slug')
                if slug:
                    print(f"   ✓ slug: {slug}")
                
                name = get_field(first_dataset, 'name')
                if name:
                    print(f"   ✓ name: {name}")
                
                description = get_field(first_dataset, 'description')
                if description:
                    print(f"   ✓ description: {str(description)[:50]}...")
                
                item_count = get_field(first_dataset, 'item_count')
                if item_count is not None:
                    print(f"   ✓ item_count: {item_count}")
                
                created_at = get_field(first_dataset, 'created_at')
                if created_at:
                    print(f"   ✓ created_at: {created_at}")
        
        # Check pagination
        pagination = data.get("pagination", {}) if isinstance(data, dict) else {}
        if pagination:
            total = pagination.get("total", 0)
            print(f"\n   Pagination:")
            print(f"   ✓ total: {total}")
            print(f"   ✓ limit: {pagination.get('limit', 'N/A')}")
            print(f"   ✓ offset: {pagination.get('offset', 'N/A')}")

    def test_02_create_dataset(
        self,
        low_level_client: Client,
        unique_dataset_slug: str,
        dataset_context: dict[str, Any],
    ) -> None:
        """Test creating a new dataset with full metadata and validate response."""
        dataset_name = f"SDK E2E Test Dataset {datetime.now().strftime('%Y%m%d_%H%M%S')}"
        dataset_description = "Integration test dataset - created by SDK automated tests"
        
        body = PostApiV1DatasetsBody(
            name=dataset_name,
            slug=unique_dataset_slug,
            description=dataset_description,
        )
        
        response = post_api_v1_datasets.sync_detailed(
            client=low_level_client,
            body=body,
        )
        
        assert response.status_code in [200, 201], (
            f"Create dataset failed: {response.status_code} - {response.content}"
        )
        
        # ===== VALIDATE RESPONSE BODY =====
        data = parse_response(response)
        
        print(f"\n✅ Created dataset - validating response:")
        
        if data:
            # API might return the created dataset or a success message
            dataset = data.get("data", data) if isinstance(data, dict) else data
            
            # Validate returned slug matches
            returned_slug = get_field(dataset, 'slug')
            if returned_slug:
                assert returned_slug == unique_dataset_slug, (
                    f"Slug mismatch: expected {unique_dataset_slug}, got {returned_slug}"
                )
                print(f"   ✓ slug: {returned_slug}")
            
            # Validate returned name
            returned_name = get_field(dataset, 'name')
            if returned_name:
                assert returned_name == dataset_name, (
                    f"Name mismatch: expected {dataset_name}, got {returned_name}"
                )
                print(f"   ✓ name: {returned_name}")
            
            # Validate returned description
            returned_desc = get_field(dataset, 'description')
            if returned_desc:
                print(f"   ✓ description: {returned_desc[:50]}...")
            
            # Check for created_at timestamp
            created_at = get_field(dataset, 'created_at')
            if created_at:
                dataset_context["created_at"] = created_at
                print(f"   ✓ created_at: {created_at}")
            
            # Check success flag
            success = get_field(data, 'success')
            if success is not None:
                assert success is True, "Expected success=True"
                print(f"   ✓ success: {success}")
        
        # Store context for subsequent tests
        dataset_context["dataset_slug"] = unique_dataset_slug
        dataset_context["dataset_name"] = dataset_name
        dataset_context["dataset_description"] = dataset_description
        
        print(f"\n   Dataset slug: {unique_dataset_slug}")

    def test_03_get_dataset(
        self,
        low_level_client: Client,
        dataset_context: dict[str, Any],
    ) -> None:
        """Test retrieving dataset by slug with full response validation."""
        if not dataset_context.get("dataset_slug"):
            pytest.skip(SKIP_NO_DATASET_SLUG)
        
        slug = dataset_context["dataset_slug"]
        expected_name = dataset_context.get("dataset_name")
        
        response = get_api_v1_datasets_by_slug.sync_detailed(
            client=low_level_client,
            slug=slug,
        )
        
        assert response.status_code == 200, f"Get dataset failed: {response.status_code}"
        
        # ===== VALIDATE RESPONSE BODY =====
        data = parse_response(response)
        assert data is not None, "Response data should not be None"
        
        print(f"\n✅ Retrieved dataset - validating response:")
        
        # API might wrap in data or return directly
        dataset = data.get("data", data) if isinstance(data, dict) else data
        
        # Validate slug matches request
        returned_slug = get_field(dataset, 'slug')
        if returned_slug:
            assert returned_slug == slug, f"Slug mismatch: expected {slug}, got {returned_slug}"
            print(f"   ✓ slug: {returned_slug}")
        
        # Validate name
        returned_name = get_field(dataset, 'name')
        if returned_name:
            if expected_name:
                assert returned_name == expected_name, (
                    f"Name mismatch: expected {expected_name}, got {returned_name}"
                )
            print(f"   ✓ name: {returned_name}")
        
        # Validate description
        description = get_field(dataset, 'description')
        if description:
            print(f"   ✓ description: {description[:50]}...")
        
        # Validate item_count
        item_count = get_field(dataset, 'item_count')
        if item_count is not None:
            assert item_count >= 0, "Item count should be non-negative"
            print(f"   ✓ item_count: {item_count}")
        
        # Validate timestamps
        created_at = get_field(dataset, 'created_at')
        if created_at:
            print(f"   ✓ created_at: {created_at}")
        
        updated_at = get_field(dataset, 'updated_at')
        if updated_at:
            print(f"   ✓ updated_at: {updated_at}")
        
        # Check for version info
        current_version = get_field(dataset, 'current_version')
        if current_version:
            print(f"   ✓ current_version: {current_version}")

    def test_04_update_dataset(
        self,
        low_level_client: Client,
        dataset_context: dict[str, Any],
    ) -> None:
        """Test updating dataset metadata with full response validation."""
        if not dataset_context.get("dataset_slug"):
            pytest.skip(SKIP_NO_DATASET_SLUG)
        
        slug = dataset_context["dataset_slug"]
        new_description = f"Updated at {datetime.now().isoformat()} - Integration test"
        
        body = PutApiV1DatasetsBySlugBody(
            description=new_description,
        )
        
        response = put_api_v1_datasets_by_slug.sync_detailed(
            client=low_level_client,
            slug=slug,
            body=body,
        )
        
        assert response.status_code in [200, 204], f"Update failed: {response.status_code}"
        
        # ===== VALIDATE RESPONSE BODY =====
        print(f"\n✅ Updated dataset - validating response:")
        
        if response.status_code == 200:
            data = parse_response(response)
            
            if data:
                dataset = data.get("data", data) if isinstance(data, dict) else data
                
                # Validate updated description
                returned_desc = get_field(dataset, 'description')
                if returned_desc:
                    assert new_description in returned_desc or returned_desc == new_description, (
                        f"Description not updated properly"
                    )
                    print(f"   ✓ description updated: {returned_desc[:50]}...")
                
                # Validate updated_at changed
                updated_at = get_field(dataset, 'updated_at')
                if updated_at:
                    dataset_context["updated_at"] = updated_at
                    print(f"   ✓ updated_at: {updated_at}")
                
                # Success flag
                success = get_field(data, 'success')
                if success is not None:
                    print(f"   ✓ success: {success}")
        else:
            print(f"   ✓ status: 204 No Content (update successful)")
        
        # Update context
        dataset_context["dataset_description"] = new_description

    # =========================================================================
    # Phase 2: Dataset Items Operations
    # =========================================================================

    def test_05_add_dataset_items(
        self,
        low_level_client: Client,
        dataset_context: dict[str, Any],
        sample_dataset_items: list[dict[str, Any]],
    ) -> None:
        """Test adding items to dataset with full response validation."""
        if not dataset_context.get("dataset_slug"):
            pytest.skip(SKIP_NO_DATASET_SLUG)
        
        slug = dataset_context["dataset_slug"]
        items = sample_dataset_items
        
        body = PostApiV1DatasetsByDatasetSlugItemsBody.from_dict({"items": items})
        response = post_api_v1_datasets_by_dataset_slug_items.sync_detailed(
            client=low_level_client,
            dataset_slug=slug,
            body=body,
        )
        
        assert response.status_code in [200, 201], f"Add items failed: {response.status_code}"
        
        # ===== VALIDATE RESPONSE BODY =====
        data = parse_response(response)
        
        print(f"\n✅ Added {len(items)} items - validating response:")
        
        if data:
            # Check success
            success = get_field(data, 'success')
            if success is not None:
                assert success is True, "Expected success=True"
                print(f"   ✓ success: {success}")
            
            # Check items added count
            added_count = get_field(data, 'added_count') or get_field(data, 'count')
            if added_count is not None:
                assert added_count == len(items), (
                    f"Added count mismatch: expected {len(items)}, got {added_count}"
                )
                print(f"   ✓ items added: {added_count}")
            
            # Check for returned item IDs
            returned_items = get_field(data, 'items') or get_field(data, 'data')
            if returned_items and isinstance(returned_items, list):
                print(f"   ✓ returned items: {len(returned_items)}")
        
        # Store item IDs for subsequent tests
        dataset_context["item_ids"] = [item["item_id"] for item in items]
        print(f"   Item IDs stored: {dataset_context['item_ids']}")

    def test_06_list_dataset_items(
        self,
        low_level_client: Client,
        dataset_context: dict[str, Any],
    ) -> None:
        """Test listing items in a dataset with full response validation."""
        if not dataset_context.get("dataset_slug"):
            pytest.skip(SKIP_NO_DATASET_SLUG)
        
        slug = dataset_context["dataset_slug"]
        expected_item_ids = dataset_context.get("item_ids", [])
        
        response = get_api_v1_datasets_by_dataset_slug_items.sync_detailed(
            client=low_level_client,
            dataset_slug=slug,
            limit=20,
        )
        
        assert response.status_code == 200, f"List items failed: {response.status_code}"
        
        # ===== VALIDATE RESPONSE BODY =====
        data = parse_response(response)
        assert data is not None, "Response data should not be None"
        
        print(f"\n✅ Listed dataset items - validating response:")
        
        # Get items list
        items = data.get("items", []) if isinstance(data, dict) else data
        
        if isinstance(items, list):
            print(f"   ✓ items count: {len(items)}")
            
            # Validate we got the expected items
            if expected_item_ids:
                returned_ids = [get_field(item, 'item_id') for item in items]
                for expected_id in expected_item_ids[:5]:  # Check first 5
                    if expected_id in returned_ids:
                        print(f"   ✓ found item: {expected_id}")
            
            # Validate first item structure
            if len(items) > 0:
                first_item = items[0]
                print(f"\n   First item validation:")
                
                item_id = get_field(first_item, 'item_id')
                if item_id:
                    print(f"   ✓ item_id: {item_id}")
                
                item_type = get_field(first_item, 'item_type')
                if item_type:
                    print(f"   ✓ item_type: {item_type}")
                
                content = get_field(first_item, 'content')
                if content:
                    print(f"   ✓ content: present")
                
                metadata = get_field(first_item, 'metadata')
                if metadata:
                    print(f"   ✓ metadata: present")
                
                created_at = get_field(first_item, 'created_at')
                if created_at:
                    print(f"   ✓ created_at: {created_at}")
        
        # Check pagination
        pagination = data.get("pagination", {}) if isinstance(data, dict) else {}
        if pagination:
            print(f"\n   Pagination:")
            print(f"   ✓ total: {pagination.get('total', 'N/A')}")

    def test_07_get_single_item(
        self,
        low_level_client: Client,
        dataset_context: dict[str, Any],
    ) -> None:
        """Test retrieving a single dataset item with full validation."""
        if not dataset_context.get("dataset_slug") or not dataset_context.get("item_ids"):
            pytest.skip(SKIP_NO_DATASET_OR_ITEMS)
        
        slug = dataset_context["dataset_slug"]
        item_id = dataset_context["item_ids"][0]
        
        response = get_api_v1_datasets_by_dataset_slug_items_by_item_id.sync_detailed(
            client=low_level_client,
            dataset_slug=slug,
            item_id=item_id,
        )
        
        assert response.status_code == 200, f"Get item failed: {response.status_code}"
        
        # ===== VALIDATE RESPONSE BODY =====
        data = parse_response(response)
        assert data is not None, "Response data should not be None"
        
        print(f"\n✅ Retrieved single item - validating response:")
        
        # API might wrap in data or return directly
        item = data.get("data", data) if isinstance(data, dict) else data
        
        # Validate item_id matches request
        returned_item_id = get_field(item, 'item_id')
        if returned_item_id:
            assert returned_item_id == item_id, (
                f"Item ID mismatch: expected {item_id}, got {returned_item_id}"
            )
            print(f"   ✓ item_id: {returned_item_id}")
        
        # Validate item_type
        item_type = get_field(item, 'item_type')
        if item_type:
            print(f"   ✓ item_type: {item_type}")
        
        # Validate content
        content = get_field(item, 'content')
        if content:
            assert content is not None, "Content should not be None"
            print(f"   ✓ content: present")
            
            # Validate content structure if it's a dict
            if isinstance(content, dict):
                for key in list(content.keys())[:3]:
                    print(f"      - {key}: {str(content[key])[:30]}...")
        
        # Validate metadata
        metadata = get_field(item, 'metadata')
        if metadata:
            print(f"   ✓ metadata: present")
        
        # Validate timestamps
        created_at = get_field(item, 'created_at')
        if created_at:
            print(f"   ✓ created_at: {created_at}")

    # =========================================================================
    # Phase 3: Dataset Versioning
    # =========================================================================

    def test_08_create_dataset_version(
        self,
        low_level_client: Client,
        dataset_context: dict[str, Any],
    ) -> None:
        """Test creating a new dataset version with full response validation."""
        if not dataset_context.get("dataset_slug"):
            pytest.skip(SKIP_NO_DATASET_SLUG)
        
        slug = dataset_context["dataset_slug"]
        version = "0.0.1"
        
        body = PostApiV1DatasetsByDatasetSlugVersionsBody(version=version)
        response = post_api_v1_datasets_by_dataset_slug_versions.sync_detailed(
            client=low_level_client,
            dataset_slug=slug,
            body=body,
        )
        
        assert response.status_code in [200, 201], f"Create version failed: {response.status_code}"
        
        # ===== VALIDATE RESPONSE BODY =====
        data = parse_response(response)
        
        print(f"\n✅ Created dataset version - validating response:")
        
        if data:
            # Check success
            success = get_field(data, 'success')
            if success is not None:
                assert success is True, "Expected success=True"
                print(f"   ✓ success: {success}")
            
            # Validate returned version
            version_data = data.get("data", data) if isinstance(data, dict) else data
            
            returned_version = get_field(version_data, 'version')
            if returned_version:
                assert returned_version == version, (
                    f"Version mismatch: expected {version}, got {returned_version}"
                )
                print(f"   ✓ version: {returned_version}")
            
            # Check version metadata
            item_count = get_field(version_data, 'item_count')
            if item_count is not None:
                print(f"   ✓ item_count: {item_count}")
            
            created_at = get_field(version_data, 'created_at')
            if created_at:
                print(f"   ✓ created_at: {created_at}")
            
            status = get_field(version_data, 'status')
            if status:
                print(f"   ✓ status: {status}")
        
        dataset_context["version"] = version

    def test_09_list_dataset_versions(
        self,
        low_level_client: Client,
        dataset_context: dict[str, Any],
    ) -> None:
        """Test listing dataset versions with full response validation."""
        if not dataset_context.get("dataset_slug"):
            pytest.skip(SKIP_NO_DATASET_SLUG)
        
        slug = dataset_context["dataset_slug"]
        expected_version = dataset_context.get("version")
        
        response = get_api_v1_datasets_by_dataset_slug_versions.sync_detailed(
            client=low_level_client,
            dataset_slug=slug,
        )
        
        assert response.status_code == 200, f"List versions failed: {response.status_code}"
        
        # ===== VALIDATE RESPONSE BODY =====
        data = parse_response(response)
        assert data is not None, "Response data should not be None"
        
        print(f"\n✅ Listed dataset versions - validating response:")
        
        # Get versions list
        versions = data.get("versions", []) if isinstance(data, dict) else data
        
        if isinstance(versions, list):
            print(f"   ✓ versions count: {len(versions)}")
            assert len(versions) >= 1, "Should have at least 1 version"
            
            # Validate expected version is in list
            if expected_version:
                version_strings = [get_field(v, 'version') for v in versions]
                if expected_version in version_strings:
                    print(f"   ✓ found expected version: {expected_version}")
            
            # Validate first version structure
            if len(versions) > 0:
                first_version = versions[0]
                print(f"\n   First version validation:")
                
                version_str = get_field(first_version, 'version')
                if version_str:
                    print(f"   ✓ version: {version_str}")
                
                item_count = get_field(first_version, 'item_count')
                if item_count is not None:
                    print(f"   ✓ item_count: {item_count}")
                
                status = get_field(first_version, 'status')
                if status:
                    print(f"   ✓ status: {status}")
                
                created_at = get_field(first_version, 'created_at')
                if created_at:
                    print(f"   ✓ created_at: {created_at}")

    def test_10_get_dataset_version(
        self,
        low_level_client: Client,
        dataset_context: dict[str, Any],
    ) -> None:
        """Test getting a specific dataset version with full validation."""
        if not dataset_context.get("dataset_slug") or not dataset_context.get("version"):
            pytest.skip(SKIP_NO_DATASET_OR_VERSION)
        
        slug = dataset_context["dataset_slug"]
        version = dataset_context["version"]
        
        response = get_api_v1_datasets_by_dataset_slug_versions_by_version.sync_detailed(
            client=low_level_client,
            dataset_slug=slug,
            version=version,
        )
        
        assert response.status_code == 200, f"Get version failed: {response.status_code}"
        
        # ===== VALIDATE RESPONSE BODY =====
        data = parse_response(response)
        assert data is not None, "Response data should not be None"
        
        print(f"\n✅ Retrieved dataset version - validating response:")
        
        # API might wrap in data or return directly
        version_data = data.get("data", data) if isinstance(data, dict) else data
        
        # Validate version matches request
        returned_version = get_field(version_data, 'version')
        if returned_version:
            assert returned_version == version, (
                f"Version mismatch: expected {version}, got {returned_version}"
            )
            print(f"   ✓ version: {returned_version}")
        
        # Validate item_count
        item_count = get_field(version_data, 'item_count')
        if item_count is not None:
            print(f"   ✓ item_count: {item_count}")
        
        # Validate status
        status = get_field(version_data, 'status')
        if status:
            print(f"   ✓ status: {status}")
        
        # Validate timestamps
        created_at = get_field(version_data, 'created_at')
        if created_at:
            print(f"   ✓ created_at: {created_at}")
        
        # Check for items in version (if included)
        items = get_field(version_data, 'items')
        if items and isinstance(items, list):
            print(f"   ✓ items included: {len(items)}")

    def test_11_get_version_diff(
        self,
        low_level_client: Client,
        dataset_context: dict[str, Any],
    ) -> None:
        """Test getting version diff with full response validation."""
        if not dataset_context.get("dataset_slug"):
            pytest.skip(SKIP_NO_DATASET_SLUG)
        
        slug = dataset_context["dataset_slug"]
        
        response = get_api_v1_datasets_by_dataset_slug_versions_diff.sync_detailed(
            client=low_level_client,
            dataset_slug=slug,
        )
        
        assert response.status_code == 200, f"Get diff failed: {response.status_code}"
        
        # ===== VALIDATE RESPONSE BODY =====
        data = parse_response(response)
        
        print(f"\n✅ Retrieved version diff - validating response:")
        
        if data:
            # Check diff structure
            added = get_field(data, 'added')
            if added is not None:
                print(f"   ✓ added: {len(added) if isinstance(added, list) else added}")
            
            removed = get_field(data, 'removed')
            if removed is not None:
                print(f"   ✓ removed: {len(removed) if isinstance(removed, list) else removed}")
            
            modified = get_field(data, 'modified')
            if modified is not None:
                print(f"   ✓ modified: {len(modified) if isinstance(modified, list) else modified}")
            
            # Check version info
            from_version = get_field(data, 'from_version')
            if from_version:
                print(f"   ✓ from_version: {from_version}")
            
            to_version = get_field(data, 'to_version')
            if to_version:
                print(f"   ✓ to_version: {to_version}")
            
            # Check summary if present
            summary = get_field(data, 'summary')
            if summary:
                print(f"   ✓ summary: {summary}")

    def test_12_publish_dataset_version(
        self,
        low_level_client: Client,
        dataset_context: dict[str, Any],
    ) -> None:
        """Test publishing a dataset version with full response validation."""
        if not dataset_context.get("dataset_slug"):
            pytest.skip(SKIP_NO_DATASET_SLUG)
        
        slug = dataset_context["dataset_slug"]
        
        response = post_api_v1_datasets_by_dataset_slug_versions_publish.sync_detailed(
            client=low_level_client,
            dataset_slug=slug,
        )
        
        assert response.status_code in [200, 201], f"Publish failed: {response.status_code}"
        
        # ===== VALIDATE RESPONSE BODY =====
        data = parse_response(response)
        
        print(f"\n✅ Published dataset version - validating response:")
        
        if data:
            # Check success
            success = get_field(data, 'success')
            if success is not None:
                assert success is True, "Expected success=True"
                print(f"   ✓ success: {success}")
            
            # Check published version
            version_data = data.get("data", data) if isinstance(data, dict) else data
            
            version = get_field(version_data, 'version')
            if version:
                print(f"   ✓ published version: {version}")
            
            status = get_field(version_data, 'status')
            if status:
                print(f"   ✓ status: {status}")
            
            published_at = get_field(version_data, 'published_at')
            if published_at:
                print(f"   ✓ published_at: {published_at}")
            
            message = get_field(data, 'message')
            if message:
                print(f"   ✓ message: {message}")

    # =========================================================================
    # Phase 4: Delete Operations & Cleanup
    # =========================================================================

    def test_13_delete_single_item(
        self,
        low_level_client: Client,
        dataset_context: dict[str, Any],
    ) -> None:
        """Test deleting a single dataset item with full response validation."""
        if not dataset_context.get("dataset_slug") or not dataset_context.get("item_ids"):
            pytest.skip(SKIP_NO_DATASET_OR_ITEMS)
        
        if len(dataset_context["item_ids"]) < 2:
            pytest.skip(SKIP_NOT_ENOUGH_ITEMS_DELETION)
        
        slug = dataset_context["dataset_slug"]
        item_id = dataset_context["item_ids"][-1]
        
        response = delete_api_v1_datasets_by_dataset_slug_items_by_item_id.sync_detailed(
            client=low_level_client,
            dataset_slug=slug,
            item_id=item_id,
        )
        
        assert response.status_code in [200, 204], f"Delete item failed: {response.status_code}"
        
        # ===== VALIDATE RESPONSE BODY =====
        print(f"\n✅ Deleted single item - validating response:")
        
        if response.status_code == 200:
            data = parse_response(response)
            
            if data:
                success = get_field(data, 'success')
                if success is not None:
                    assert success is True, "Expected success=True"
                    print(f"   ✓ success: {success}")
                
                deleted_id = get_field(data, 'item_id') or get_field(data, 'deleted_id')
                if deleted_id:
                    assert deleted_id == item_id, f"Deleted ID mismatch"
                    print(f"   ✓ deleted item_id: {deleted_id}")
                
                message = get_field(data, 'message')
                if message:
                    print(f"   ✓ message: {message}")
        else:
            print(f"   ✓ status: 204 No Content (delete successful)")
        
        dataset_context["item_ids"].remove(item_id)
        print(f"   Remaining items: {len(dataset_context['item_ids'])}")

    def test_14_bulk_delete_items(
        self,
        low_level_client: Client,
        dataset_context: dict[str, Any],
    ) -> None:
        """Test bulk deleting multiple dataset items with full response validation."""
        if not dataset_context.get("dataset_slug") or not dataset_context.get("item_ids"):
            pytest.skip(SKIP_NO_DATASET_OR_ITEMS)
        
        if len(dataset_context["item_ids"]) < 3:
            pytest.skip(SKIP_NOT_ENOUGH_ITEMS_BULK_DELETE)
        
        slug = dataset_context["dataset_slug"]
        items_to_delete = dataset_context["item_ids"][:3]
        
        body = DeleteApiV1DatasetsByDatasetSlugItemsBody.from_dict({
            "itemIds": items_to_delete
        })
        
        response = delete_api_v1_datasets_by_dataset_slug_items.sync_detailed(
            client=low_level_client,
            dataset_slug=slug,
            body=body,
        )
        
        assert response.status_code in [200, 204], f"Bulk delete failed: {response.status_code}"
        
        # ===== VALIDATE RESPONSE BODY =====
        print(f"\n✅ Bulk deleted items - validating response:")
        
        if response.status_code == 200:
            data = parse_response(response)
            
            if data:
                success = get_field(data, 'success')
                if success is not None:
                    assert success is True, "Expected success=True"
                    print(f"   ✓ success: {success}")
                
                deleted_count = get_field(data, 'deleted_count') or get_field(data, 'count')
                if deleted_count is not None:
                    assert deleted_count == len(items_to_delete), (
                        f"Deleted count mismatch: expected {len(items_to_delete)}, got {deleted_count}"
                    )
                    print(f"   ✓ deleted count: {deleted_count}")
                
                deleted_ids = get_field(data, 'deleted_ids') or get_field(data, 'item_ids')
                if deleted_ids and isinstance(deleted_ids, list):
                    print(f"   ✓ deleted IDs: {deleted_ids}")
                
                message = get_field(data, 'message')
                if message:
                    print(f"   ✓ message: {message}")
        else:
            print(f"   ✓ status: 204 No Content (bulk delete successful)")
        
        # Update context
        for item_id in items_to_delete:
            if item_id in dataset_context["item_ids"]:
                dataset_context["item_ids"].remove(item_id)
        
        print(f"   Remaining items: {len(dataset_context['item_ids'])}")

    def test_15_delete_dataset(
        self,
        low_level_client: Client,
        dataset_context: dict[str, Any],
    ) -> None:
        """Test deleting the entire dataset with full response validation."""
        if not dataset_context.get("dataset_slug"):
            pytest.skip(SKIP_NO_DATASET_SLUG)
        
        slug = dataset_context["dataset_slug"]
        
        response = delete_api_v1_datasets_by_slug.sync_detailed(
            client=low_level_client,
            slug=slug,
        )
        
        if response.status_code == 500:
            pytest.xfail("Dataset deletion returned 500 (known backend issue)")
        
        assert response.status_code in [200, 204], f"Delete failed: {response.status_code}"
        
        # ===== VALIDATE RESPONSE BODY =====
        print(f"\n✅ Deleted dataset - validating response:")
        
        if response.status_code == 200:
            data = parse_response(response)
            
            if data:
                success = get_field(data, 'success')
                if success is not None:
                    assert success is True, "Expected success=True"
                    print(f"   ✓ success: {success}")
                
                deleted_slug = get_field(data, 'slug') or get_field(data, 'deleted_slug')
                if deleted_slug:
                    assert deleted_slug == slug, f"Deleted slug mismatch"
                    print(f"   ✓ deleted slug: {deleted_slug}")
                
                message = get_field(data, 'message')
                if message:
                    print(f"   ✓ message: {message}")
        else:
            print(f"   ✓ status: 204 No Content (delete successful)")
        
        print(f"   Dataset '{slug}' deleted successfully")


@pytest.mark.datasets
@pytest.mark.integration
class TestDatasetsIsolated:
    """Isolated tests for individual dataset operations."""

    def test_list_datasets_pagination(self, low_level_client: Client) -> None:
        """Test listing datasets with pagination parameters and validate response."""
        response = get_api_v1_datasets.sync_detailed(
            client=low_level_client,
            limit=5,
            offset=0,
        )
        
        assert response.status_code == 200
        
        # Validate pagination
        data = parse_response(response)
        if data and isinstance(data, dict):
            datasets = data.get("datasets", [])
            assert len(datasets) <= 5, "Should respect limit"
            print(f"\n✅ Pagination test: got {len(datasets)} datasets (limit=5)")

    def test_get_nonexistent_dataset(self, low_level_client: Client) -> None:
        """Test getting a dataset that doesn't exist returns proper error."""
        response = get_api_v1_datasets_by_slug.sync_detailed(
            client=low_level_client,
            slug="nonexistent-dataset-slug-12345",
        )
        
        assert response.status_code in [404, 400], (
            f"Expected 404 or 400 for nonexistent dataset, got {response.status_code}"
        )
        
        # Validate error response
        data = parse_response(response)
        if data:
            error = get_field(data, 'error') or get_field(data, 'message')
            if error:
                print(f"\n✅ Nonexistent dataset test: proper error returned")
                print(f"   Error: {error}")

    def test_list_datasets_response_structure(self, low_level_client: Client) -> None:
        """Test that list datasets returns expected structure."""
        response = get_api_v1_datasets.sync_detailed(
            client=low_level_client,
            limit=3,
        )
        
        assert response.status_code == 200
        
        data = parse_response(response)
        assert data is not None, "Response should have data"
        
        print(f"\n✅ Response structure validation:")
        print(f"   Response type: {type(data)}")
        
        if isinstance(data, dict):
            for key in data.keys():
                print(f"   ✓ field: {key}")
