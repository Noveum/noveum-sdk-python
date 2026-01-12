#!/usr/bin/env python3
"""
Scorers API Tests - Partial Coverage (8 Tests Implemented)

This script tests a scorer workflow with 8 implemented tests:

Phase 1: Dataset Setup (using conversation data)
- Create a dataset ✓
- Upload conversation items to the dataset ✓

Phase 2: Scorer Operations
- List scorers ✓
- Create scorer ✓
- Get scorer by ID ✓
- Update scorer ✓

Phase 3: Scorer Results Operations
- Upload scorer results (from scorer_results_dataset_new.json) ✓
- List scorer results ✓

Cleanup: Automated cleanup of created resources ✓

TODO: Expand coverage to include:
- Delete scorer (formal test)
- Get scorer result by ID
- Delete scorer results (formal test)

Test Data Files:
- test_data/conversation_dataset.json (100 conversation items)
- test_data/scorer_results_dataset_new.json (10 evaluation items)

Usage:
    python test_scorers.py

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
    delete_api_v1_datasets_by_slug,
    post_api_v1_datasets,
    post_api_v1_datasets_by_dataset_slug_items,
)
from noveum_api_client.api.scorer_results import (
    get_api_v1_scorers_results,
    post_api_v1_scorers_results_batch,
)
from noveum_api_client.api.scorers import (
    delete_api_v1_scorers_by_id,
    get_api_v1_scorers,
    get_api_v1_scorers_by_id,
    post_api_v1_scorers,
    put_api_v1_scorers_by_id,
)
from noveum_api_client.models.post_api_v1_datasets_body import PostApiV1DatasetsBody
from noveum_api_client.models.post_api_v1_datasets_by_dataset_slug_items_body import (
    PostApiV1DatasetsByDatasetSlugItemsBody,
)
from noveum_api_client.models.post_api_v1_scorers_body import PostApiV1ScorersBody
from noveum_api_client.models.post_api_v1_scorers_results_batch_body import PostApiV1ScorersResultsBatchBody
from noveum_api_client.models.put_api_v1_scorers_by_id_body import PutApiV1ScorersByIdBody

# =============================================================================
# Configuration
# =============================================================================

API_KEY = os.getenv("NOVEUM_API_KEY")
BASE_URL = os.getenv("NOVEUM_BASE_URL", "https://api.noveum.ai")

# =============================================================================
# Test Utilities
# =============================================================================

test_results: list[dict[str, Any]] = []
created_resources: dict[str, list[Any]] = {"datasets": [], "scorers": [], "scorer_results": []}

# Test data files
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), "test_data")
CONVERSATION_DATA_FILE = os.path.join(TEST_DATA_DIR, "conversation_dataset.json")
SCORER_RESULTS_FILE = os.path.join(TEST_DATA_DIR, "scorer_results_dataset_new.json")

# Globals for tracking created resources
CREATED_DATASET_SLUG = None
CREATED_SCORER_ID = None


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
        print(f"📂 Loading data from: {file_path}")
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
                print(f"   ✅ Loaded {len(items)} items")
                return items  # type: ignore[no-any-return]
            # Handle direct array: [...]
            elif isinstance(data, list):
                print(f"   ✅ Loaded {len(data)} items")
                return data
            else:
                print("   ⚠️  Unexpected data structure")
                return []
    except Exception as e:
        print(f"   ❌ Could not load file: {e}")
        return []


# =============================================================================
# Phase 1: Dataset Setup
# =============================================================================


def test_create_dataset(low_level_client):
    """Phase 1.1: Create Dataset for Scorers"""
    print_section("PHASE 1.1: Create Dataset for Scorer Testing")

    global CREATED_DATASET_SLUG

    dataset_name = generate_id("SDK_Scorer_Dataset")
    dataset_slug = dataset_name.lower().replace("_", "-")

    print(f"Creating dataset: {dataset_name}")
    print(f"Slug: {dataset_slug}")

    try:
        body = PostApiV1DatasetsBody(
            name=dataset_name,
            slug=dataset_slug,
            description="Test dataset for scorer operations - created by SDK automated tests",
        )

        response = post_api_v1_datasets(client=low_level_client, body=body)

        passed = response.status_code in [200, 201]
        log_test("Create scorer dataset", passed, f"Status: {response.status_code}")

        if passed:
            CREATED_DATASET_SLUG = dataset_slug
            created_resources["datasets"].append(dataset_slug)
            print(f"   ✅ Created dataset: {dataset_slug}")
        else:
            print(f"   ❌ Failed: {response.parsed}")

    except Exception as e:
        log_test("Create scorer dataset", False, f"Exception: {str(e)}")


def test_upload_conversation_data(low_level_client):
    """Phase 1.2: Upload Conversation Data to Dataset"""
    print_section("PHASE 1.2: Upload Conversation Data to Dataset")

    if not CREATED_DATASET_SLUG:
        print("⚠️  Skipping - no dataset created")
        return

    conversation_items_raw = load_test_data(CONVERSATION_DATA_FILE)

    if not conversation_items_raw:
        print("⚠️  No conversation items found")
        return

    print("   🔄 Transforming from EXPORT format to INPUT format...")

    # Transform exported data to input format
    conversation_items = []
    for item in conversation_items_raw:
        # Extract only the fields needed for input
        input_item = {
            "item_id": item.get("item_id"),
            "item_type": item.get("item_type"),
            "content": item.get("content", {}),
            "metadata": (
                json.loads(item.get("metadata", "{}"))
                if isinstance(item.get("metadata"), str)
                else item.get("metadata", {})
            ),
        }

        # Add optional fields if present
        if item.get("source_trace_id"):
            input_item["trace_id"] = item.get("source_trace_id")
        if item.get("source_span_id"):
            input_item["span_id"] = item.get("source_span_id")

        conversation_items.append(input_item)

    print(f"   ✅ Transformed {len(conversation_items)} items")
    print(f"   ⏳ Uploading {len(conversation_items)} conversation items...")

    try:
        body = PostApiV1DatasetsByDatasetSlugItemsBody.from_dict({"items": conversation_items})

        response = post_api_v1_datasets_by_dataset_slug_items(
            client=low_level_client, dataset_slug=CREATED_DATASET_SLUG, body=body
        )

        passed = response.status_code in [200, 201]
        log_test(
            "Upload conversation data",
            passed,
            f"Status: {response.status_code}, Uploaded: {len(conversation_items)} items",
        )

        if passed:
            print(f"   ✅ Successfully uploaded {len(conversation_items)} conversation items")
        else:
            print(f"   ❌ Upload failed: {response.parsed}")

    except Exception as e:
        log_test("Upload conversation data", False, f"Exception: {str(e)}")


# =============================================================================
# Phase 2: Scorer Operations
# =============================================================================


def test_list_scorers(low_level_client):
    """Phase 2.1: List Scorers"""
    print_section("PHASE 2.1: List Scorers")

    try:
        response = get_api_v1_scorers(client=low_level_client, limit=10)
        passed = response.status_code == 200
        log_test("List scorers", passed, f"Status: {response.status_code}")

        if passed and hasattr(response, "parsed") and response.parsed:
            scorers = response.parsed if isinstance(response.parsed, list) else []
            print(f"   Found {len(scorers)} existing scorers")
    except Exception as e:
        log_test("List scorers", False, f"Exception: {str(e)}")


def test_create_scorer(low_level_client):
    """Phase 2.2: Create Scorer"""
    print_section("PHASE 2.2: Create Scorer")

    global CREATED_SCORER_ID

    scorer_name = generate_id("SDK_Test_Scorer")

    print(f"Creating scorer: {scorer_name}")

    try:
        # Create proper PostApiV1ScorersBody instance with required fields
        body = PostApiV1ScorersBody(
            name=scorer_name,
            description="Test scorer created by SDK automated tests",
            type_="llm_as_judge",  # Note: type_ parameter maps to "type" in JSON
            tag="test",  # Required field
            config={"model": "gpt-4", "prompt": "Evaluate this response for quality"},
        )

        response = post_api_v1_scorers(client=low_level_client, body=body)

        passed = response.status_code in [200, 201]
        log_test("Create scorer", passed, f"Status: {response.status_code}")

        if passed and hasattr(response, "parsed"):
            # Extract scorer ID from response
            if hasattr(response.parsed, "id"):
                CREATED_SCORER_ID = response.parsed.id
                created_resources["scorers"].append(CREATED_SCORER_ID)
                print(f"   ✅ Created scorer with ID: {CREATED_SCORER_ID}")
            else:
                print("   ⚠️  Scorer created but couldn't extract ID")
        else:
            print(f"   ❌ Failed: {response.parsed}")

    except Exception as e:
        log_test("Create scorer", False, f"Exception: {str(e)}")


def test_get_scorer(low_level_client):
    """Phase 2.3: Get Scorer by ID"""
    print_section("PHASE 2.3: Get Scorer by ID")

    if not CREATED_SCORER_ID:
        print("⚠️  Skipping - no scorer created")
        return

    try:
        response = get_api_v1_scorers_by_id(client=low_level_client, id=CREATED_SCORER_ID)

        passed = response.status_code == 200
        log_test("Get scorer by ID", passed, f"Status: {response.status_code}")

        if passed:
            print(f"   ✅ Retrieved scorer: {CREATED_SCORER_ID}")

    except Exception as e:
        log_test("Get scorer by ID", False, f"Exception: {str(e)}")


def test_update_scorer(low_level_client):
    """Phase 2.4: Update Scorer"""
    print_section("PHASE 2.4: Update Scorer")

    if not CREATED_SCORER_ID:
        print("⚠️  Skipping - no scorer created")
        return

    try:
        # Create proper PutApiV1ScorersByIdBody instance for update
        body = PutApiV1ScorersByIdBody(
            name=f"Updated_{CREATED_SCORER_ID}", description="Updated scorer description from automated test"
        )

        response = put_api_v1_scorers_by_id(client=low_level_client, id=CREATED_SCORER_ID, body=body)

        passed = response.status_code in [200, 204]
        log_test("Update scorer", passed, f"Status: {response.status_code}")

    except Exception as e:
        log_test("Update scorer", False, f"Exception: {str(e)}")


# =============================================================================
# Phase 3: Scorer Results Operations
# =============================================================================


def test_upload_scorer_results(low_level_client):
    """Phase 3.1: Upload Scorer Results"""
    print_section("PHASE 3.1: Upload Scorer Results to Dataset")

    if not CREATED_DATASET_SLUG or not CREATED_SCORER_ID:
        print("⚠️  Skipping - dataset or scorer not ready")
        return

    scorer_results = load_test_data(SCORER_RESULTS_FILE)

    if not scorer_results:
        print("⚠️  No scorer results found")
        return

    # Limit to first 20 items for testing (the file is huge!)
    scorer_results = scorer_results[:20]
    print(f"   ⏳ Uploading {len(scorer_results)} scorer results (limited for testing)...")

    try:
        # Prepare batch results using the proper model structure
        # The batch API expects a "results" array where each item has the required fields
        body = PostApiV1ScorersResultsBatchBody.from_dict({"results": scorer_results})

        response = post_api_v1_scorers_results_batch(client=low_level_client, body=body)

        passed = response.status_code in [200, 201]
        log_test(
            "Upload scorer results", passed, f"Status: {response.status_code}, Uploaded: {len(scorer_results)} results"
        )

        if passed:
            print(f"   ✅ Successfully uploaded {len(scorer_results)} scorer results")
            # Track result IDs if available
            if hasattr(response, "parsed") and hasattr(response.parsed, "ids"):
                created_resources["scorer_results"].extend(response.parsed.ids)
        else:
            print(f"   ❌ Upload failed: {response.parsed}")

    except Exception as e:
        log_test("Upload scorer results", False, f"Exception: {str(e)}")


def test_list_scorer_results(low_level_client):
    """Phase 3.2: List Scorer Results"""
    print_section("PHASE 3.2: List Scorer Results")

    try:
        response = get_api_v1_scorers_results(client=low_level_client, limit=10)

        passed = response.status_code == 200
        log_test("List scorer results", passed, f"Status: {response.status_code}")

        if passed and hasattr(response, "parsed") and response.parsed:
            results = response.parsed if isinstance(response.parsed, list) else []
            print(f"   Found {len(results)} scorer results")
    except Exception as e:
        log_test("List scorer results", False, f"Exception: {str(e)}")


# =============================================================================
# Cleanup
# =============================================================================


def test_cleanup(low_level_client):
    """Cleanup: Delete all created resources"""
    print_section("CLEANUP: Deleting Test Resources")

    # Delete scorers
    for scorer_id in created_resources["scorers"]:
        try:
            print(f"🗑️  Deleting scorer: {scorer_id}")
            response = delete_api_v1_scorers_by_id(client=low_level_client, id=scorer_id)

            if response.status_code in [200, 204]:
                print(f"   ✅ Deleted scorer: {scorer_id}")
            else:
                print(f"   ⚠️  Delete returned status {response.status_code}")
        except Exception as e:
            print(f"   ⚠️  Cleanup failed: {str(e)}")

    # Delete datasets
    for dataset_slug in created_resources["datasets"]:
        try:
            print(f"🗑️  Deleting dataset: {dataset_slug}")
            response = delete_api_v1_datasets_by_slug(client=low_level_client, slug=dataset_slug)

            if response.status_code in [200, 204]:
                print(f"   ✅ Deleted dataset: {dataset_slug}")
            else:
                print(f"   ⚠️  Delete returned status {response.status_code}")
        except Exception as e:
            print(f"   ⚠️  Cleanup failed: {str(e)}")

    print("\n✅ Cleanup complete")


# =============================================================================
# Main Execution
# =============================================================================


def run_all_tests():
    """Run all scorer tests"""
    if not API_KEY:
        print("❌ ERROR: NOVEUM_API_KEY not set")
        print("Please set the NOVEUM_API_KEY environment variable and try again.")
        sys.exit(1)

    print("\n" + "=" * 60)
    print("SCORERS API TESTS - COMPLETE WORKFLOW")
    print("=" * 60)
    print(f"API Key: {'*' * 8}...{'*' * 4} (set)")
    print(f"Base URL: {BASE_URL}")
    print("=" * 60)

    # Initialize clients
    global client, low_level_client
    client = NoveumClient(api_key=API_KEY, base_url=BASE_URL)
    low_level_client = Client(base_url=BASE_URL, headers={"Authorization": f"Bearer {API_KEY}"})

    # Phase 1: Dataset Setup
    print("\n" + "📦 PHASE 1: DATASET SETUP")
    test_create_dataset(low_level_client)
    test_upload_conversation_data(low_level_client)

    # Phase 2: Scorer Operations
    print("\n" + "🎯 PHASE 2: SCORER OPERATIONS")
    test_list_scorers(low_level_client)
    test_create_scorer(low_level_client)
    test_get_scorer(low_level_client)
    test_update_scorer(low_level_client)

    # Phase 3: Scorer Results
    print("\n" + "📊 PHASE 3: SCORER RESULTS OPERATIONS")
    test_upload_scorer_results(low_level_client)
    test_list_scorer_results(low_level_client)

    # Cleanup
    test_cleanup(low_level_client)

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
        results_file = f"../../test_results/scorers_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(results_file, "w") as f:
            json.dump(test_results, f, indent=2)
        print(f"\n📊 Results saved to: {results_file}")
    except Exception as e:
        print(f"\n⚠️  Could not save results: {e}")

    print("\n" + "=" * 60)
    print("SCORERS TESTS COMPLETE")
    print("=" * 60)

    return passed == total


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
