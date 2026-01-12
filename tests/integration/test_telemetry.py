#!/usr/bin/env python3
"""
Telemetry API Tests

Tests telemetry metrics endpoints (18 endpoints):
- Cost metrics by provider
- Cost trends
- Latency metrics
- Model usage
- Error rates
- Request trends
- Slowest requests
- Top projects
- Dashboard metrics

Usage: python test_telemetry.py
"""

import json
import os
import sys
from datetime import datetime

import pytest

from noveum_api_client import Client, NoveumClient
from noveum_api_client.api.telemetry import (
    get_api_telemetry_metrics,
    get_api_telemetry_metrics_cost_by_provider,
    get_api_telemetry_metrics_cost_trends,
    get_api_telemetry_metrics_cost_trends_per_project,
    get_api_telemetry_metrics_dashboard,
    get_api_telemetry_metrics_error_rate,
    get_api_telemetry_metrics_latency_by_provider,
    get_api_telemetry_metrics_latency_trends,
    get_api_telemetry_metrics_model_usage,
    get_api_telemetry_metrics_recent_errors,
    get_api_telemetry_metrics_requests_trends,
    get_api_telemetry_metrics_requests_trends_per_project,
    get_api_telemetry_metrics_slowest_requests,
    get_api_telemetry_metrics_top_projects_api,
    get_api_telemetry_metrics_top_projects_tokens,
    get_api_telemetry_metrics_usage_trends,
    get_api_telemetry_metrics_usage_trends_per_project,
    get_api_telemetry_metrics_with_trends,
)

API_KEY = os.getenv("NOVEUM_API_KEY")
BASE_URL = os.getenv("NOVEUM_BASE_URL", "https://api.noveum.ai")

test_results = []

if not API_KEY:
    pytest.skip("NOVEUM_API_KEY not set; skipping integration tests", allow_module_level=True)

client = NoveumClient(api_key=API_KEY, base_url=BASE_URL)
low_level_client = Client(base_url=BASE_URL, headers={"Authorization": f"Bearer {API_KEY}"})


def log_test(name: str, passed: bool, details: str = "") -> bool:
    test_results.append({"test": name, "passed": passed, "details": details, "timestamp": datetime.now().isoformat()})
    print(f"{'✅' if passed else '❌'} {name}" + (f" - {details}" if details else ""))
    return passed


def print_section(title: str):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def test_dashboard_metrics():
    print_section("TEST 1: Dashboard Metrics")
    response = get_api_telemetry_metrics_dashboard.sync_detailed(client=low_level_client)
    passed = response.status_code == 200
    log_test("Dashboard metrics", passed, f"Status: {response.status_code}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"


def test_metrics():
    print_section("TEST 2: General Metrics")
    response = get_api_telemetry_metrics.sync_detailed(client=low_level_client)
    passed = response.status_code == 200
    log_test("General metrics", passed, f"Status: {response.status_code}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"


def test_metrics_with_trends():
    print_section("TEST 3: Metrics with Trends")
    response = get_api_telemetry_metrics_with_trends.sync_detailed(client=low_level_client)
    passed = response.status_code == 200
    log_test("Metrics with trends", passed, f"Status: {response.status_code}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"


def test_cost_by_provider():
    print_section("TEST 4: Cost by Provider")
    response = get_api_telemetry_metrics_cost_by_provider.sync_detailed(client=low_level_client)
    passed = response.status_code == 200
    log_test("Cost by provider", passed, f"Status: {response.status_code}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"


def test_cost_trends():
    print_section("TEST 5: Cost Trends")
    response = get_api_telemetry_metrics_cost_trends.sync_detailed(client=low_level_client)
    passed = response.status_code == 200
    log_test("Cost trends", passed, f"Status: {response.status_code}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"


def test_cost_trends_per_project():
    print_section("TEST 6: Cost Trends Per Project")
    response = get_api_telemetry_metrics_cost_trends_per_project.sync_detailed(client=low_level_client)
    passed = response.status_code == 200
    log_test("Cost trends per project", passed, f"Status: {response.status_code}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"


def test_latency_by_provider():
    print_section("TEST 7: Latency by Provider")
    response = get_api_telemetry_metrics_latency_by_provider.sync_detailed(client=low_level_client)
    passed = response.status_code == 200
    log_test("Latency by provider", passed, f"Status: {response.status_code}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"


def test_latency_trends():
    print_section("TEST 8: Latency Trends")
    response = get_api_telemetry_metrics_latency_trends.sync_detailed(client=low_level_client)
    passed = response.status_code == 200
    log_test("Latency trends", passed, f"Status: {response.status_code}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"


def test_model_usage():
    print_section("TEST 9: Model Usage")
    response = get_api_telemetry_metrics_model_usage.sync_detailed(client=low_level_client)
    passed = response.status_code == 200
    log_test("Model usage", passed, f"Status: {response.status_code}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"


def test_error_rate():
    print_section("TEST 10: Error Rate")
    response = get_api_telemetry_metrics_error_rate.sync_detailed(client=low_level_client)
    passed = response.status_code == 200
    log_test("Error rate", passed, f"Status: {response.status_code}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"


def test_recent_errors():
    print_section("TEST 11: Recent Errors")
    response = get_api_telemetry_metrics_recent_errors.sync_detailed(client=low_level_client, limit=10)
    passed = response.status_code == 200
    log_test("Recent errors", passed, f"Status: {response.status_code}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"


def test_requests_trends():
    print_section("TEST 12: Requests Trends")
    response = get_api_telemetry_metrics_requests_trends.sync_detailed(client=low_level_client)
    passed = response.status_code == 200
    log_test("Requests trends", passed, f"Status: {response.status_code}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"


def test_requests_trends_per_project():
    print_section("TEST 13: Requests Trends Per Project")
    response = get_api_telemetry_metrics_requests_trends_per_project.sync_detailed(client=low_level_client)
    passed = response.status_code == 200
    log_test("Requests trends per project", passed, f"Status: {response.status_code}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"


def test_slowest_requests():
    print_section("TEST 14: Slowest Requests")
    response = get_api_telemetry_metrics_slowest_requests.sync_detailed(client=low_level_client, limit=10)
    passed = response.status_code == 200
    log_test("Slowest requests", passed, f"Status: {response.status_code}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"


def test_top_projects_api():
    print_section("TEST 15: Top Projects by API")
    response = get_api_telemetry_metrics_top_projects_api.sync_detailed(client=low_level_client, limit=10)
    passed = response.status_code == 200
    log_test("Top projects by API", passed, f"Status: {response.status_code}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"


def test_top_projects_tokens():
    print_section("TEST 16: Top Projects by Tokens")
    response = get_api_telemetry_metrics_top_projects_tokens.sync_detailed(client=low_level_client, limit=10)
    passed = response.status_code == 200
    log_test("Top projects by tokens", passed, f"Status: {response.status_code}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"


def test_usage_trends():
    print_section("TEST 17: Usage Trends")
    response = get_api_telemetry_metrics_usage_trends.sync_detailed(client=low_level_client)
    passed = response.status_code == 200
    log_test("Usage trends", passed, f"Status: {response.status_code}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"


def test_usage_trends_per_project():
    print_section("TEST 18: Usage Trends Per Project")
    response = get_api_telemetry_metrics_usage_trends_per_project.sync_detailed(client=low_level_client)
    passed = response.status_code == 200
    log_test("Usage trends per project", passed, f"Status: {response.status_code}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"


def run_all_tests():
    print("\n" + "=" * 60)
    print("TELEMETRY API TESTS - COMPLETE COVERAGE")
    print("=" * 60)
    print("Testing 18 telemetry metrics endpoints")
    print("=" * 60)

    # List of all test functions to run
    test_functions = [
        test_dashboard_metrics,
        test_metrics,
        test_metrics_with_trends,
        test_cost_by_provider,
        test_cost_trends,
        test_cost_trends_per_project,
        test_latency_by_provider,
        test_latency_trends,
        test_model_usage,
        test_error_rate,
        test_recent_errors,
        test_requests_trends,
        test_requests_trends_per_project,
        test_slowest_requests,
        test_top_projects_api,
        test_top_projects_tokens,
        test_usage_trends,
        test_usage_trends_per_project,
    ]

    # Track failures
    failures = []

    # Run each test, catching exceptions to allow all tests to run
    for test_func in test_functions:
        try:
            test_func()
        except AssertionError as e:
            failures.append(
                {
                    "test": test_func.__name__,
                    "error_type": "AssertionError",
                    "error": str(e),
                }
            )
        except Exception as e:
            failures.append(
                {
                    "test": test_func.__name__,
                    "error_type": type(e).__name__,
                    "error": str(e),
                }
            )

    print_section("TEST SUMMARY")
    total = len(test_results)
    passed = sum(1 for r in test_results if r["passed"])
    print(f"\nTotal: {total}, Passed: {passed}, Failed: {total-passed}")
    print(f"Success Rate: {(passed/total*100):.1f}%" if total > 0 else "N/A")

    # Print detailed failure information
    if failures:
        print("\n" + "=" * 60)
        print("FAILED TESTS:")
        print("=" * 60)
        for failure in failures:
            print(f"\n❌ {failure['test']}")
            print(f"   Error Type: {failure['error_type']}")
            print(f"   Details: {failure['error']}")

    try:
        os.makedirs("../../test_results", exist_ok=True)
        with open(f"../../test_results/telemetry_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json", "w") as f:
            json.dump(test_results, f, indent=2)
    except Exception:
        pass

    return len(failures) == 0


if __name__ == "__main__":
    sys.exit(0 if run_all_tests() else 1)
