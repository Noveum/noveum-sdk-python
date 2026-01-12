#!/usr/bin/env python3
"""
API Keys Tests

Tests API key management endpoints (3 endpoints):
- List API keys
- Create API key
- Delete API key

Usage: python test_api_keys.py
"""

import json
import os
import sys
from datetime import datetime
from typing import Any

sys.path.insert(0, os.path.abspath("../.."))
sys.path.insert(0, os.path.abspath("../../tests"))

from noveum_api_client import Client, NoveumClient
from noveum_api_client.api.api_keys.delete_api_by_organisation_slug_api_keys import (
    sync_detailed as delete_api_by_organisation_slug_api_keys,
)
from noveum_api_client.api.api_keys.get_api_by_organisation_slug_api_keys import (
    sync_detailed as get_api_by_organisation_slug_api_keys,
)
from noveum_api_client.api.api_keys.post_api_by_organisation_slug_api_keys import (
    sync_detailed as post_api_by_organisation_slug_api_keys,
)

API_KEY = os.getenv("NOVEUM_API_KEY", "******")
BASE_URL = os.getenv("NOVEUM_BASE_URL", "https://api.noveum.ai")
ORG_SLUG = os.getenv("NOVEUM_ORG_SLUG", "NoveumSDK")

test_results: list[dict[str, Any]] = []
created_resources: dict[str, list[Any]] = {"api_keys": []}


def log_test(name: str, passed: bool, details: str = "") -> bool:
    test_results.append({"test": name, "passed": passed, "details": details, "timestamp": datetime.now().isoformat()})
    print(f"{'✅' if passed else '❌'} {name}" + (f" - {details}" if details else ""))
    return passed


def print_section(title: str):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def test_list_api_keys(low_level_client):
    print_section("TEST 1: List API Keys")
    try:
        response = get_api_by_organisation_slug_api_keys(client=low_level_client, organisation_slug=ORG_SLUG)
        passed = response.status_code == 200
        details = f"Status: {response.status_code}"
        if passed and response.parsed:
            api_keys = response.parsed.api_keys
            details += f", Found {len(api_keys)} API key(s)"
        log_test("List API keys", passed, details)
    except Exception as e:
        log_test("List API keys", False, f"Exception: {str(e)}")


def test_create_api_key(low_level_client):
    print_section("TEST 2: Create API Key")
    try:
        # Create API key with a test title
        test_title = f"SDK Test Key {datetime.now().strftime('%Y%m%d_%H%M%S')}"
        body = {"title": test_title}

        response = post_api_by_organisation_slug_api_keys(
            client=low_level_client, organisation_slug=ORG_SLUG, body=body
        )
        passed = response.status_code == 201
        details = f"Status: {response.status_code}"

        if passed and response.parsed:
            api_key_id = response.parsed.id
            created_resources["api_keys"].append(api_key_id)
            details += f", Created API key ID: {api_key_id[:8]}..."

        log_test("Create API key", passed, details)
        return api_key_id if passed else None
    except Exception as e:
        log_test("Create API key", False, f"Exception: {str(e)}")
        return None


def test_delete_api_key(low_level_client, api_key_id: str | None):
    print_section("TEST 3: Delete API Key")
    if not api_key_id:
        log_test("Delete API key", True, "Skipped - no API key to delete")
        return

    try:
        response = delete_api_by_organisation_slug_api_keys(
            client=low_level_client, organisation_slug=ORG_SLUG, id=api_key_id
        )
        passed = response.status_code == 200
        details = f"Status: {response.status_code}"

        if passed:
            # Remove from cleanup list if deletion was successful
            if api_key_id in created_resources["api_keys"]:
                created_resources["api_keys"].remove(api_key_id)
            details += f", Deleted API key ID: {api_key_id[:8]}..."

        log_test("Delete API key", passed, details)
    except Exception as e:
        log_test("Delete API key", False, f"Exception: {str(e)}")


def cleanup_resources(low_level_client):
    """Clean up any remaining test resources"""
    print_section("CLEANUP")
    if not created_resources["api_keys"]:
        print("✅ No resources to clean up")
        return

    print(f"Cleaning up {len(created_resources['api_keys'])} API key(s)...")
    for api_key_id in created_resources["api_keys"]:
        try:
            response = delete_api_by_organisation_slug_api_keys(
                client=low_level_client, organisation_slug=ORG_SLUG, id=api_key_id
            )
            if response.status_code == 200:
                print(f"✅ Cleaned up API key: {api_key_id[:8]}...")
            else:
                print(f"⚠️  Failed to clean up API key: {api_key_id[:8]}...")
        except Exception as e:
            print(f"⚠️  Error cleaning up API key {api_key_id[:8]}...: {str(e)}")


def run_all_tests():
    print("\n" + "=" * 60)
    print("API KEYS TESTS")
    print("=" * 60)
    print("Testing 3 API key endpoints")
    print("=" * 60)

    global client, low_level_client
    client = NoveumClient(api_key=API_KEY, base_url=BASE_URL)
    low_level_client = Client(base_url=BASE_URL, headers={"Authorization": f"Bearer {API_KEY}"})

    # Run tests in sequence
    test_list_api_keys(low_level_client)
    api_key_id = test_create_api_key(low_level_client)
    test_delete_api_key(low_level_client, api_key_id)

    # Cleanup any remaining resources
    cleanup_resources(low_level_client)

    print_section("TEST SUMMARY")
    total = len(test_results)
    passed = sum(1 for r in test_results if r["passed"])
    print(f"\nTotal: {total}, Passed: {passed}, Failed: {total-passed}")
    print(f"Success Rate: {(passed/total*100):.1f}%" if total > 0 else "N/A")

    try:
        os.makedirs("../../test_results", exist_ok=True)
        with open(f"../../test_results/api_keys_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json", "w") as f:
            json.dump(test_results, f, indent=2)
    except Exception:
        pass

    return passed == total


if __name__ == "__main__":
    sys.exit(0 if run_all_tests() else 1)
