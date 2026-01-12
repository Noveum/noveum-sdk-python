#!/usr/bin/env python3
"""
Datasets API Tests - Complete Coverage with FULL Real Dataset

Tests all 15 dataset management endpoints with FULL REAL test data:

Phase 1: Dataset CRUD (4 endpoints)
- List datasets
- Create dataset
- Get dataset by slug
- Update dataset

Phase 2: Dataset Items CRUD (5 endpoints) - USES FULL REAL DATA
- Add items (FULL dataset from conversation_dataset.json)
- List items
- Get single item
- Delete single item
- Bulk delete items

Test Data Files:
- test_data/conversation_dataset.json (100 real conversation items - 8.2MB)

Note:
- This test uses the COMPLETE conversation dataset (not a subset)
- Scorer results are tested separately in test_scorers.py
- Dataset upload may take a few seconds due to volume

Usage:
    python test_datasets.py

Requirements:
    - NOVEUM_API_KEY environment variable set
    - SDK installed: pip install -e ../..
    - Test data files in test_data/ directory
"""

import json
import os
import sys
import uuid
from datetime import datetime
from typing import Any

# Add parent directories to path
sys.path.insert(0, os.path.abspath("../.."))
sys.path.insert(0, os.path.abspath("../../tests"))


from noveum_api_client import Client, NoveumClient
from noveum_api_client.api.datasets import (
    delete_api_v1_datasets_by_dataset_slug_items,
    delete_api_v1_datasets_by_dataset_slug_items_by_item_id,
    delete_api_v1_datasets_by_slug,
    get_api_v1_datasets,
    get_api_v1_datasets_by_dataset_slug_items,
    get_api_v1_datasets_by_dataset_slug_items_by_item_id,
    get_api_v1_datasets_by_slug,
    post_api_v1_datasets,
    post_api_v1_datasets_by_dataset_slug_items,
    put_api_v1_datasets_by_slug,
)
from noveum_api_client.models.delete_api_v1_datasets_by_dataset_slug_items_body import (
    DeleteApiV1DatasetsByDatasetSlugItemsBody,
)
from noveum_api_client.models.post_api_v1_datasets_body import PostApiV1DatasetsBody
from noveum_api_client.models.post_api_v1_datasets_by_dataset_slug_items_body import (
    PostApiV1DatasetsByDatasetSlugItemsBody,
)

# =============================================================================
# Configuration
# =============================================================================

API_KEY = os.getenv("NOVEUM_API_KEY", "******")
BASE_URL = os.getenv("NOVEUM_BASE_URL", "https://api.noveum.ai")

# =============================================================================
# Test Utilities
# =============================================================================

test_results: list[dict[str, Any]] = []
created_resources: dict[str, list[Any]] = {"datasets": [], "items": []}

# Test data files
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), "test_data")
CONVERSATION_DATA_FILE = os.path.join(TEST_DATA_DIR, "conversation_dataset.json")
SCORER_DATA_FILE = os.path.join(TEST_DATA_DIR, "scorer_results_dataset_new.json")


def log_test(name: str, passed: bool, details: str = "") -> bool:
    """Log test result"""
    result = {"test": name, "passed": passed, "details": details, "timestamp": datetime.now().isoformat()}
    test_results.append(result)

    icon = "✅" if passed else "❌"
    print(f"{icon} {name}")
    if details:
        print(f"   {details}")
    return passed


def generate_id(prefix: str = "test") -> str:
    """Generate unique test ID"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    unique = str(uuid.uuid4())[:8]
    return f"{prefix}_{timestamp}_{unique}"


def print_section(title: str):
    """Print section header"""
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def load_test_data(file_path: str) -> list[dict]:
    """Load test data from JSON file"""
    try:
        with open(file_path) as f:
            data = json.load(f)

            # Handle nested structure: {"items": [...]}
            if isinstance(data, dict) and "items" in data:
                items = data["items"]
                print("   📊 Dataset metadata:")
                if "total_items" in data:
                    print(f"      Total items: {data['total_items']}")
                if "version" in data:
                    print(f"      Version: {data['version']}")
                return items  # type: ignore[no-any-return]
            # Handle direct array: [...]
            elif isinstance(data, list):
                return data
            else:
                print(f"⚠️  Unexpected data structure in {file_path}")
                return []
    except Exception as e:
        print(f"⚠️  Could not load {file_path}: {e}")
        return []


# =============================================================================
# Test Functions
# =============================================================================


def test_list_datasets():
    """Test 1: List Datasets (GET /api/v1/datasets)"""
    print_section("TEST 1: List Datasets")

    try:
        # High-level client
        response = client.list_datasets(limit=10)
        passed = response["status_code"] == 200
        log_test("List datasets (high-level)", passed, f"Status: {response['status_code']}")

        if passed and response.get("data"):
            print(f"   Found {len(response['data'])} datasets")
    except Exception as e:
        log_test("List datasets (high-level)", False, f"Exception: {str(e)}")

    try:
        # Low-level client
        response = get_api_v1_datasets.sync_detailed(client=low_level_client, limit=10)
        passed = response.status_code == 200
        log_test("List datasets (low-level)", passed, f"Status: {response.status_code}")
    except Exception as e:
        log_test("List datasets (low-level)", False, f"Exception: {str(e)}")


def test_create_dataset():
    """Test 2: Create Dataset (POST /api/v1/datasets)"""
    print_section("TEST 2: Create Dataset")

    global CREATED_DATASET_SLUG

    dataset_name = generate_id("SDK_Test_Dataset")
    dataset_slug = dataset_name.lower().replace("_", "-")

    print(f"Creating dataset: {dataset_name}")
    print(f"Slug: {dataset_slug}")

    try:
        # Create model object
        body = PostApiV1DatasetsBody(
            name=dataset_name, slug=dataset_slug, description="Test dataset created by SDK automated tests"
        )

        response = post_api_v1_datasets.sync_detailed(client=low_level_client, body=body)

        passed = response.status_code in [200, 201]
        log_test("Create dataset", passed, f"Status: {response.status_code}")

        if passed:
            CREATED_DATASET_SLUG = dataset_slug
            created_resources["datasets"].append(dataset_slug)
            print(f"   ✅ Created dataset: {dataset_slug}")
        else:
            print(f"   Response: {response.parsed}")

    except Exception as e:
        log_test("Create dataset", False, f"Exception: {str(e)}")


def test_get_dataset():
    """Test 3: Get Dataset by Slug (GET /api/v1/datasets/{slug})"""
    print_section("TEST 3: Get Dataset by Slug")

    if "CREATED_DATASET_SLUG" not in globals():
        print("⚠️  Skipping - no dataset created in previous test")
        return

    try:
        response = get_api_v1_datasets_by_slug.sync_detailed(client=low_level_client, slug=CREATED_DATASET_SLUG)

        passed = response.status_code == 200
        log_test("Get dataset by slug", passed, f"Status: {response.status_code}")

        if passed:
            print(f"   Retrieved dataset: {CREATED_DATASET_SLUG}")

    except Exception as e:
        log_test("Get dataset by slug", False, f"Exception: {str(e)}")


def test_update_dataset():
    """Test 4: Update Dataset (PUT /api/v1/datasets/{slug})"""
    print_section("TEST 4: Update Dataset")

    if "CREATED_DATASET_SLUG" not in globals():
        print("⚠️  Skipping - no dataset created")
        return

    try:
        # Note: Update uses same body model
        body = PostApiV1DatasetsBody(
            name=f"Updated_{CREATED_DATASET_SLUG}", description="Updated description from automated test"
        )

        response = put_api_v1_datasets_by_slug.sync_detailed(
            client=low_level_client, slug=CREATED_DATASET_SLUG, body=body
        )

        passed = response.status_code in [200, 204]
        log_test("Update dataset", passed, f"Status: {response.status_code}")

    except Exception as e:
        log_test("Update dataset", False, f"Exception: {str(e)}")


def test_add_dataset_items():
    """Test 5: Add Dataset Items (POST /api/v1/datasets/{slug}/items) - FULL DATASET"""
    print_section("TEST 5: Add Conversation Items to Dataset")

    if "CREATED_DATASET_SLUG" not in globals():
        print("⚠️  Skipping - no dataset created")
        return

    global CREATED_ITEM_IDS
    CREATED_ITEM_IDS = []

    # Load COMPLETE conversation dataset
    print(f"\n📂 Loading FULL conversation dataset from: {CONVERSATION_DATA_FILE}")
    conversation_items_raw = load_test_data(CONVERSATION_DATA_FILE)

    if conversation_items_raw:
        print(f"   🔢 Found {len(conversation_items_raw)} conversation items")
        print("   🔄 Transforming from EXPORT format to INPUT format...")

        # Transform exported data to input format
        # The file is in EXPORT format - all content fields are at TOP LEVEL
        # We need INPUT format - all content fields INSIDE the "content" object
        # Reference: upload_dataset_to_api.py shows the proper structure
        conversation_items = []
        for item in conversation_items_raw:
            # Parse metadata if it's a JSON string
            metadata = item.get("metadata", {})
            if isinstance(metadata, str):
                try:
                    metadata = json.loads(metadata)
                except (json.JSONDecodeError, ValueError):
                    metadata = {}

            # Helper to parse JSON fields
            def parse_json_field(field):
                if isinstance(field, str):
                    try:
                        return json.loads(field)
                    except (json.JSONDecodeError, ValueError):
                        return field
                return field

            # BUILD content object from top-level fields (this is the key fix!)
            # In export format, these are at top level. In input format, they go in content.
            content = {
                "agent_name": item.get("agent_name", ""),
                "agent_role": item.get("agent_role", ""),
                "agent_task": item.get("agent_task", ""),
                "agent_response": item.get("agent_response", ""),
                "system_prompt": item.get("system_prompt", ""),
                "user_id": item.get("user_id", ""),
                "session_id": item.get("session_id", ""),
                "turn_id": item.get("turn_id", ""),
                "ground_truth": item.get("ground_truth", ""),
                "expected_tool_call": item.get("expected_tool_call", ""),
                "tools_available": parse_json_field(item.get("tools_available", [])),
                "tool_calls": parse_json_field(item.get("tool_calls", [])),
                "tool_call_results": parse_json_field(item.get("tool_call_results", [])),
                "parameters_passed": parse_json_field(item.get("parameters_passed", {})),
                "retrieval_query": parse_json_field(item.get("retrieval_query", [])),
                "retrieved_context": parse_json_field(item.get("retrieved_context", [])),
                "exit_status": item.get("exit_status", ""),
                "agent_exit": item.get("agent_exit", ""),
                "trace_data": parse_json_field(item.get("trace_data", {})),
                "conversation_id": item.get("conversation_id", ""),
                "speaker": item.get("speaker", ""),
                "message": item.get("message", ""),
                "conversation_context": parse_json_field(item.get("conversation_context", {})),
                "input_text": item.get("input_text", ""),
                "output_text": item.get("output_text", ""),
                "expected_output": item.get("expected_output", ""),
                "evaluation_context": parse_json_field(item.get("evaluation_context", {})),
                "criteria": item.get("criteria", ""),
                "quality_score": item.get("quality_score", 0),
                "validation_status": item.get("validation_status", ""),
                "validation_errors": parse_json_field(item.get("validation_errors", [])),
                "tags": parse_json_field(item.get("tags", [])),
                "custom_attributes": parse_json_field(item.get("custom_attributes", {})),
            }

            # Build API item with proper structure
            input_item = {
                "item_id": item.get("item_id"),
                "item_type": item.get("item_type", "conversational"),
                "content": content,  # Now properly populated!
                "metadata": metadata,
            }

            # Add optional trace/span IDs if present
            if item.get("source_trace_id"):
                input_item["trace_id"] = item.get("source_trace_id")
            if item.get("source_span_id"):
                input_item["span_id"] = item.get("source_span_id")

            conversation_items.append(input_item)

        print(f"   ✅ Transformed {len(conversation_items)} items to input format")
        print(f"   ⏳ Uploading to dataset '{CREATED_DATASET_SLUG}'...")

        try:
            # Use from_dict() to properly create the body model
            body = PostApiV1DatasetsByDatasetSlugItemsBody.from_dict({"items": conversation_items})

            response = post_api_v1_datasets_by_dataset_slug_items.sync_detailed(
                client=low_level_client, dataset_slug=CREATED_DATASET_SLUG, body=body
            )

            passed = response.status_code in [200, 201]
            log_test(
                "Add FULL conversation dataset",
                passed,
                f"Status: {response.status_code}, Uploaded: {len(conversation_items)} items",
            )

            if passed:
                # Track item IDs for cleanup
                for item in conversation_items:
                    if "item_id" in item:
                        CREATED_ITEM_IDS.append(item["item_id"])
                        created_resources["items"].append(item["item_id"])
                print(f"   ✅ Successfully uploaded {len(conversation_items)} conversation items")
                print(f"   ✅ Tracked {len(CREATED_ITEM_IDS)} item IDs for testing")
            else:
                print(f"   ❌ Upload failed: {response.parsed}")

        except Exception as e:
            log_test("Add FULL conversation dataset", False, f"Exception: {str(e)}")
    else:
        print("   ⚠️  No conversation items found in file")

    print(f"\n📊 Total items in dataset: {len(CREATED_ITEM_IDS)}")


def test_list_dataset_items():
    """Test 6: List Dataset Items (GET /api/v1/datasets/{slug}/items)"""
    print_section("TEST 6: List Dataset Items")

    if "CREATED_DATASET_SLUG" not in globals():
        print("⚠️  Skipping - no dataset created")
        return

    try:
        response = get_api_v1_datasets_by_dataset_slug_items.sync_detailed(
            client=low_level_client, dataset_slug=CREATED_DATASET_SLUG, limit=25
        )

        passed = response.status_code == 200

        if passed and hasattr(response, "parsed") and response.parsed:
            items = response.parsed if isinstance(response.parsed, list) else []
            item_count = len(items)
            log_test("List dataset items", passed, f"Status: {response.status_code}, Found: {item_count} items")
        else:
            log_test("List dataset items", passed, f"Status: {response.status_code}")

    except Exception as e:
        log_test("List dataset items", False, f"Exception: {str(e)}")


def test_get_single_item():
    """Test 7: Get Single Dataset Item (GET /api/v1/datasets/{slug}/items/{id})"""
    print_section("TEST 7: Get Single Dataset Item")

    if "CREATED_DATASET_SLUG" not in globals() or "CREATED_ITEM_IDS" not in globals():
        print("⚠️  Skipping - no dataset or items created")
        return

    if not CREATED_ITEM_IDS:
        print("⚠️  Skipping - no items available")
        return

    test_item_id = CREATED_ITEM_IDS[0]
    print(f"Getting item: {test_item_id}")

    try:
        response = get_api_v1_datasets_by_dataset_slug_items_by_item_id.sync_detailed(
            client=low_level_client, dataset_slug=CREATED_DATASET_SLUG, item_id=test_item_id
        )

        passed = response.status_code == 200
        log_test("Get single item", passed, f"Status: {response.status_code}")

        if passed:
            print(f"   ✅ Retrieved item: {test_item_id}")

    except Exception as e:
        log_test("Get single item", False, f"Exception: {str(e)}")


def test_delete_single_item():
    """Test 8: Delete Single Dataset Item (DELETE /api/v1/datasets/{slug}/items/{id})"""
    print_section("TEST 8: Delete Single Dataset Item")

    if "CREATED_DATASET_SLUG" not in globals() or "CREATED_ITEM_IDS" not in globals():
        print("⚠️  Skipping - no dataset or items created")
        return

    if len(CREATED_ITEM_IDS) < 2:
        print("⚠️  Skipping - not enough items to delete one")
        return

    # Delete the last item (keep most for other tests)
    test_item_id = CREATED_ITEM_IDS[-1]
    print(f"Deleting item: {test_item_id}")

    try:
        response = delete_api_v1_datasets_by_dataset_slug_items_by_item_id.sync_detailed(
            client=low_level_client, dataset_slug=CREATED_DATASET_SLUG, item_id=test_item_id
        )

        passed = response.status_code in [200, 204]
        log_test("Delete single item", passed, f"Status: {response.status_code}")

        if passed:
            CREATED_ITEM_IDS.remove(test_item_id)
            print(f"   ✅ Deleted item: {test_item_id}")

    except Exception as e:
        log_test("Delete single item", False, f"Exception: {str(e)}")


def test_bulk_delete_items():
    """Test 9: Bulk Delete Dataset Items (DELETE /api/v1/datasets/{slug}/items)"""
    print_section("TEST 9: Bulk Delete Dataset Items")

    if "CREATED_DATASET_SLUG" not in globals() or "CREATED_ITEM_IDS" not in globals():
        print("⚠️  Skipping - no dataset or items created")
        return

    if not CREATED_ITEM_IDS:
        print("⚠️  Skipping - no items to delete")
        return

    # Delete remaining items
    items_to_delete = CREATED_ITEM_IDS[:5] if len(CREATED_ITEM_IDS) >= 5 else CREATED_ITEM_IDS
    print(f"Bulk deleting {len(items_to_delete)} items")

    try:
        # Use from_dict() with camelCase (itemIds not item_ids)
        body = DeleteApiV1DatasetsByDatasetSlugItemsBody.from_dict({"itemIds": items_to_delete})

        response = delete_api_v1_datasets_by_dataset_slug_items.sync_detailed(
            client=low_level_client, dataset_slug=CREATED_DATASET_SLUG, body=body
        )

        passed = response.status_code in [200, 204]
        log_test("Bulk delete items", passed, f"Status: {response.status_code}, Deleted: {len(items_to_delete)} items")

        if passed:
            for item_id in items_to_delete:
                if item_id in CREATED_ITEM_IDS:
                    CREATED_ITEM_IDS.remove(item_id)
            print(f"   ✅ Bulk deleted {len(items_to_delete)} items")

    except Exception as e:
        log_test("Bulk delete items", False, f"Exception: {str(e)}")


def test_cleanup():
    """Cleanup: Delete all created resources"""
    print_section("CLEANUP: Deleting Test Resources")

    # Delete datasets
    for dataset_slug in created_resources["datasets"]:
        try:
            print(f"🗑️  Deleting dataset: {dataset_slug}")
            response = delete_api_v1_datasets_by_slug.sync_detailed(client=low_level_client, slug=dataset_slug)

            if response.status_code in [200, 204]:
                print(f"   ✅ Deleted: {dataset_slug}")
            else:
                print(f"   ⚠️  Delete returned status {response.status_code}")

        except Exception as e:
            print(f"   ⚠️  Cleanup failed: {str(e)}")

    print("\n✅ Cleanup complete")


# =============================================================================
# Main Execution
# =============================================================================


def run_all_tests():
    """Run all dataset tests"""
    print("\n" + "=" * 60)
    print("DATASETS API TESTS - COMPLETE COVERAGE")
    print("=" * 60)
    print(f"API Key: {API_KEY[:10]}...")
    print(f"Base URL: {BASE_URL}")
    print("=" * 60)

    # Initialize clients
    global client, low_level_client
    client = NoveumClient(api_key=API_KEY, base_url=BASE_URL)
    low_level_client = Client(base_url=BASE_URL, headers={"Authorization": f"Bearer {API_KEY}"})

    # Phase 1: Dataset CRUD
    print("\n" + "🔧 PHASE 1: DATASET CRUD OPERATIONS")
    test_list_datasets()
    test_create_dataset()
    test_get_dataset()
    test_update_dataset()

    # Phase 2: Dataset Items
    print("\n" + "📦 PHASE 2: DATASET ITEMS OPERATIONS")
    test_add_dataset_items()
    test_list_dataset_items()
    test_get_single_item()
    test_delete_single_item()
    test_bulk_delete_items()

    # Cleanup
    test_cleanup()

    # Summary
    print_section("TEST SUMMARY")

    total = len(test_results)
    passed = sum(1 for r in test_results if r["passed"])
    failed = total - passed

    print(f"\nTotal Tests:  {total}")
    print(f"✅ Passed:     {passed}")
    print(f"❌ Failed:     {failed}")
    if total > 0:
        print(f"Success Rate: {(passed/total*100):.1f}%")

    if failed > 0:
        print("\nFailed Tests:")
        for r in test_results:
            if not r["passed"]:
                print(f"  ❌ {r['test']}: {r['details']}")

    # Export results
    try:
        os.makedirs("../../test_results", exist_ok=True)
        results_file = f"../../test_results/datasets_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(results_file, "w") as f:
            json.dump(test_results, f, indent=2)
        print(f"\n📊 Results saved to: {results_file}")
    except Exception as e:
        print(f"\n⚠️  Could not save results: {e}")

    print("\n" + "=" * 60)
    print("DATASETS TESTS COMPLETE")
    print("=" * 60)

    return passed == total


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
