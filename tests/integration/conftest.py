"""
Pytest Configuration and Shared Fixtures for E2E Tests

This file provides:
- Shared fixtures for all tests
- Setup/teardown logic
- Environment validation
- Custom pytest markers
"""

import os
import sys

import pytest

# Add parent directories to path
sys.path.insert(0, os.path.abspath("../.."))
sys.path.insert(0, os.path.abspath("../../tests"))

from noveum_api_client import Client, NoveumClient

# =============================================================================
# Environment Validation
# =============================================================================


def validate_environment():
    """Validate required environment variables and provide helpful messages"""
    errors = []
    warnings = []

    # Check API Key
    api_key = os.getenv("NOVEUM_API_KEY")
    if not api_key:
        errors.append("❌ NOVEUM_API_KEY not set\n" "   Fix: export NOVEUM_API_KEY='your-api-key-here'")
    elif not api_key.startswith("nv_"):
        warnings.append("⚠️  NOVEUM_API_KEY doesn't start with 'nv_' - might be invalid")

    # Check optional vars
    if not os.getenv("NOVEUM_PROJECT"):
        warnings.append(
            "⚠️  NOVEUM_PROJECT not set (using default: 'SDK_Test_Project')\n"
            "   Set with: export NOVEUM_PROJECT='your-project-name'"
        )

    if not os.getenv("NOVEUM_ENVIRONMENT"):
        warnings.append(
            "⚠️  NOVEUM_ENVIRONMENT not set (using default: 'test')\n"
            "   Set with: export NOVEUM_ENVIRONMENT='your-environment'"
        )

    # Print warnings
    if warnings:
        print("\n" + "=" * 70)
        print("⚠️  SETUP WARNINGS")
        print("=" * 70)
        for warning in warnings:
            print(warning)
        print()

    # Raise errors if critical vars missing
    if errors:
        error_msg = "\n" + "=" * 70 + "\n"
        error_msg += "❌ SETUP ERRORS - CANNOT RUN TESTS\n"
        error_msg += "=" * 70 + "\n"
        for error in errors:
            error_msg += error + "\n"
        error_msg += "\n" + "=" * 70 + "\n"
        error_msg += "📚 Quick Setup Guide:\n"
        error_msg += "=" * 70 + "\n"
        error_msg += "1. Set your API key:\n"
        error_msg += "   export NOVEUM_API_KEY='nv_your_key_here'\n\n"
        error_msg += "2. (Optional) Set project and environment:\n"
        error_msg += "   export NOVEUM_PROJECT='your-project'\n"
        error_msg += "   export NOVEUM_ENVIRONMENT='test'\n\n"
        error_msg += "3. Install SDK:\n"
        error_msg += "   pip install -e ../..\n\n"
        error_msg += "4. Run tests:\n"
        error_msg += "   pytest test_datasets.py -v\n"
        error_msg += "   pytest test_traces.py -v\n"
        error_msg += "=" * 70

        pytest.exit(error_msg, returncode=1)


# =============================================================================
# Session-level Fixtures (Run Once)
# =============================================================================


def pytest_configure(config):
    """Validate environment before any tests run"""
    validate_environment()

    # Register custom markers
    config.addinivalue_line("markers", "integration: mark test as integration test")
    config.addinivalue_line("markers", "slow: mark test as slow running")


@pytest.fixture(scope="session")
def api_config():
    """Provide API configuration for all tests"""
    return {
        "api_key": os.getenv("NOVEUM_API_KEY"),
        "base_url": os.getenv("NOVEUM_BASE_URL", "https://api.noveum.ai"),
        "project": os.getenv("NOVEUM_PROJECT", "SDK_Test_Project"),
        "environment": os.getenv("NOVEUM_ENVIRONMENT", "test"),
        "org_slug": os.getenv("NOVEUM_ORG_SLUG", "NoveumSDK"),
    }


# =============================================================================
# Test-level Fixtures (Run Per Test)
# =============================================================================


@pytest.fixture
def noveum_client(api_config) -> NoveumClient:
    """Provide high-level Noveum client"""
    return NoveumClient(api_key=api_config["api_key"], base_url=api_config["base_url"])


@pytest.fixture
def low_level_client(api_config) -> Client:
    """Provide low-level API client"""
    return Client(base_url=api_config["base_url"], headers={"Authorization": f"Bearer {api_config['api_key']}"})


@pytest.fixture
def test_data_dir():
    """Provide path to test data directory"""
    return os.path.join(os.path.dirname(__file__), "test_data")


# =============================================================================
# Test Result Tracking
# =============================================================================


@pytest.fixture
def test_tracker():
    """Track test results for reporting"""
    results = {"passed": [], "failed": [], "skipped": []}
    return results


# =============================================================================
# Cleanup Fixtures
# =============================================================================


@pytest.fixture
def cleanup_resources():
    """Track and cleanup test resources"""
    resources = {
        "datasets": [],
        "traces": [],
        "scorers": [],
    }

    yield resources

    # Cleanup happens here after test completes
    # Note: Actual cleanup code would go in individual test files
    # since delete operations currently return 500


# =============================================================================
# Custom Assertions
# =============================================================================


def assert_api_success(response, expected_codes=None):
    """Custom assertion for API responses with helpful error messages"""
    if expected_codes is None:
        expected_codes = [200, 201]
    if hasattr(response, "status_code"):
        status = response.status_code
    elif isinstance(response, dict) and "status_code" in response:
        status = response["status_code"]
    else:
        pytest.fail(f"Invalid response format: {type(response)}")

    if status not in expected_codes:
        error_msg = "\n❌ API call failed\n"
        error_msg += f"   Expected: {expected_codes}\n"
        error_msg += f"   Got: {status}\n"

        if hasattr(response, "parsed"):
            error_msg += f"   Response: {response.parsed}\n"

        # Add helpful hints based on status code
        if status == 401:
            error_msg += "\n💡 Hint: Check your NOVEUM_API_KEY is valid\n"
        elif status == 403:
            error_msg += "\n💡 Hint: Your API key may lack permissions for this operation\n"
        elif status == 404:
            error_msg += "\n💡 Hint: The requested resource was not found\n"
        elif status == 500:
            error_msg += "\n💡 Hint: Server error - this may be a known API issue\n"
            error_msg += "   For delete operations, this is a known bug\n"

        pytest.fail(error_msg)


# Make assert_api_success available globally
pytest.assert_api_success = assert_api_success  # type: ignore[attr-defined]


# =============================================================================
# Pytest Hooks for Custom Reporting
# =============================================================================


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """Add custom summary at the end of test run"""
    terminalreporter.write_sep("=", "E2E Test Summary")

    # Get test statistics
    passed = len(terminalreporter.stats.get("passed", []))
    failed = len(terminalreporter.stats.get("failed", []))
    skipped = len(terminalreporter.stats.get("skipped", []))
    total = passed + failed + skipped

    if total > 0:
        success_rate = (passed / total) * 100

        terminalreporter.write_line("\n📊 Results:")
        terminalreporter.write_line(f"   ✅ Passed:  {passed}/{total}")
        terminalreporter.write_line(f"   ❌ Failed:  {failed}/{total}")
        terminalreporter.write_line(f"   ⏭️  Skipped: {skipped}/{total}")
        terminalreporter.write_line(f"   📈 Success Rate: {success_rate:.1f}%")

        if failed > 0:
            terminalreporter.write_line("\n💡 Tip: Run with -v for verbose output")
            terminalreporter.write_line("💡 Tip: Run with -s to see print statements")

    terminalreporter.write_line("")


# =============================================================================
# Module-level Setup
# =============================================================================


def pytest_collection_modifyitems(config, items):
    """Add markers to tests automatically"""
    for item in items:
        # Mark all tests as integration tests
        if "test_" in item.nodeid:
            item.add_marker(pytest.mark.integration)

        # Mark slow tests
        if any(slow_name in item.name for slow_name in ["upload", "create", "batch"]):
            item.add_marker(pytest.mark.slow)
