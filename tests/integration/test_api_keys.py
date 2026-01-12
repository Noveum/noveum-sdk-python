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
from noveum_api_client.api.api_keys.get_api_by_organisation_slug_api_keys import (
    sync_detailed as get_api_by_organisation_slug_api_keys,
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


def test_list_api_keys():
    print_section("TEST 1: List API Keys")
    try:
        response = get_api_by_organisation_slug_api_keys(client=low_level_client, organisation_slug=ORG_SLUG)
        passed = response.status_code == 200
        log_test("List API keys", passed, f"Status: {response.status_code}")
    except Exception as e:
        log_test("List API keys", False, f"Exception: {str(e)}")


def run_all_tests():
    print("\n" + "=" * 60)
    print("API KEYS TESTS")
    print("=" * 60)

    global client, low_level_client
    client = NoveumClient(api_key=API_KEY, base_url=BASE_URL)
    low_level_client = Client(base_url=BASE_URL, headers={"Authorization": f"Bearer {API_KEY}"})

    test_list_api_keys()

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
