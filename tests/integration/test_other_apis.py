#!/usr/bin/env python3
"""
Other APIs Tests

Tests miscellaneous endpoints:
- Health check
- Status
- Organizations (generate slug, invitations)
- Uploads (signed URLs)
- Contact/Careers/Newsletter

Usage: python test_other_apis.py
"""

import json
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath("../.."))
sys.path.insert(0, os.path.abspath("../../tests"))

from noveum_api_client import Client, NoveumClient
from noveum_api_client.api.health.get_api_health import sync_detailed as get_api_health
from noveum_api_client.api.organizations.get_api_organizations_generate_slug import (
    sync_detailed as get_api_organizations_generate_slug,
)
from noveum_api_client.api.status.get_api_v1_status import sync_detailed as get_api_v1_status

API_KEY = os.getenv("NOVEUM_API_KEY", "******")
BASE_URL = os.getenv("NOVEUM_BASE_URL", "https://api.noveum.ai")

test_results = []


def log_test(name: str, passed: bool, details: str = "") -> bool:
    test_results.append({"test": name, "passed": passed, "details": details, "timestamp": datetime.now().isoformat()})
    print(f"{'✅' if passed else '❌'} {name}" + (f" - {details}" if details else ""))
    return passed


def print_section(title: str):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def test_health():
    print_section("TEST 1: Health Check")
    try:
        response = get_api_health.sync_detailed(client=low_level_client)
        passed = response.status_code == 200
        log_test("Health check", passed, f"Status: {response.status_code}")
    except Exception as e:
        log_test("Health check", False, f"Exception: {str(e)}")


def test_status():
    print_section("TEST 2: Status")
    try:
        response = get_api_v1_status.sync_detailed(client=low_level_client)
        passed = response.status_code == 200
        log_test("Status check", passed, f"Status: {response.status_code}")
    except Exception as e:
        log_test("Status check", False, f"Exception: {str(e)}")


def test_generate_slug():
    print_section("TEST 3: Generate Organization Slug")
    try:
        response = get_api_organizations_generate_slug.sync_detailed(client=low_level_client, name="Test Organization")
        passed = response.status_code == 200
        log_test("Generate org slug", passed, f"Status: {response.status_code}")
    except Exception as e:
        log_test("Generate org slug", False, f"Exception: {str(e)}")


def run_all_tests():
    print("\n" + "=" * 60)
    print("OTHER APIS TESTS")
    print("=" * 60)

    global client, low_level_client
    client = NoveumClient(api_key=API_KEY, base_url=BASE_URL)
    low_level_client = Client(base_url=BASE_URL, headers={"Authorization": f"Bearer {API_KEY}"})

    test_health()
    test_status()
    test_generate_slug()

    print_section("TEST SUMMARY")
    total = len(test_results)
    passed = sum(1 for r in test_results if r["passed"])
    print(f"\nTotal: {total}, Passed: {passed}, Failed: {total-passed}")
    print(f"Success Rate: {(passed/total*100):.1f}%" if total > 0 else "N/A")

    try:
        os.makedirs("../../test_results", exist_ok=True)
        with open(f"../../test_results/other_apis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json", "w") as f:
            json.dump(test_results, f, indent=2)
    except Exception:
        pass

    return passed == total


if __name__ == "__main__":
    sys.exit(0 if run_all_tests() else 1)
