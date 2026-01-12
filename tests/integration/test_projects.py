#!/usr/bin/env python3
"""
Projects API Tests - Partial Coverage (1 Test Implemented)

Currently implements 1 test:
- List projects

TODO: Expand coverage to include remaining project management endpoints:
- Create project
- Get project
- Update project
- Delete project
- Project settings
- Team management
- Additional project endpoints

Note: The Noveum API includes 12 project management endpoints.
This test file provides partial coverage with plans to expand.

Usage: python test_projects.py
"""

import json
import os
import sys
from datetime import datetime
from typing import Any

sys.path.insert(0, os.path.abspath("../.."))
sys.path.insert(0, os.path.abspath("../../tests"))

from noveum_api_client import Client, NoveumClient
from noveum_api_client.api.projects.get_api_v1_projects import sync_detailed as get_api_v1_projects

API_KEY = os.getenv("NOVEUM_API_KEY", "******")
BASE_URL = os.getenv("NOVEUM_BASE_URL", "https://api.noveum.ai")

test_results: list[dict[str, Any]] = []
created_resources: dict[str, list[Any]] = {"projects": []}


def log_test(name: str, passed: bool, details: str = "") -> bool:
    test_results.append({"test": name, "passed": passed, "details": details, "timestamp": datetime.now().isoformat()})
    print(f"{'✅' if passed else '❌'} {name}" + (f" - {details}" if details else ""))
    return passed


def print_section(title: str):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def test_list_projects(low_level_client):
    print_section("TEST 1: List Projects")
    try:
        response = get_api_v1_projects(client=low_level_client, limit=10)
        passed = response.status_code == 200
        log_test("List projects", passed, f"Status: {response.status_code}")
    except Exception as e:
        log_test("List projects", False, f"Exception: {str(e)}")


def run_all_tests():
    print("\n" + "=" * 60)
    print("PROJECTS API TESTS")
    print("=" * 60)

    global client, low_level_client
    client = NoveumClient(api_key=API_KEY, base_url=BASE_URL)
    low_level_client = Client(base_url=BASE_URL, headers={"Authorization": f"Bearer {API_KEY}"})

    test_list_projects(low_level_client)

    print_section("TEST SUMMARY")
    total = len(test_results)
    passed = sum(1 for r in test_results if r["passed"])
    print(f"\nTotal: {total}, Passed: {passed}, Failed: {total-passed}")
    print(f"Success Rate: {(passed/total*100):.1f}%" if total > 0 else "N/A")

    try:
        os.makedirs("../../test_results", exist_ok=True)
        with open(f"../../test_results/projects_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json", "w") as f:
            json.dump(test_results, f, indent=2)
    except Exception:
        pass

    return passed == total


if __name__ == "__main__":
    sys.exit(0 if run_all_tests() else 1)
