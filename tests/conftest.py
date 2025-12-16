"""Pytest configuration and fixtures."""

import os
from datetime import datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from noveum import (
    DatasetItem,
    NoveumClient,
    ScorerConfig,
    ScorerResult,
    EvalResult,
)


@pytest.fixture
def api_key():
    """Test API key."""
    return "test-api-key-12345"


@pytest.fixture
def noveum_client(api_key):
    """Create a test NoveumClient."""
    return NoveumClient(api_key=api_key, base_url="https://test.noveum.ai/api/v1")


@pytest.fixture
def mock_http_client():
    """Create a mock HTTP client."""
    return MagicMock()


@pytest.fixture
def sample_dataset_item():
    """Create a sample DatasetItem for testing."""
    return DatasetItem(
        id="item-123",
        created_at=datetime.now(),
        item_id="item-123",
        dataset_slug="test-dataset",
        input_text="What is the capital of France?",
        expected_output="Paris",
        metadata={"source": "test"},
    )


@pytest.fixture
def sample_scorer_config():
    """Create a sample ScorerConfig."""
    return ScorerConfig(
        scorer_id="factuality_scorer",
        config={"model": "gpt-4", "temperature": 0.0},
    )


@pytest.fixture
def sample_eval_result(sample_dataset_item, sample_scorer_config):
    """Create a sample EvalResult."""
    return EvalResult(
        item_id=sample_dataset_item.item_id,
        scores=[
            ScorerResult(
                scorer_id=sample_scorer_config.scorer_id,
                scorer_name="Factuality Scorer",
                score=8.5,
                passed=True,
                reasoning="The output is factually correct.",
            )
        ],
        overall_score=8.5,
        overall_passed=True,
    )


@pytest.fixture
def mock_response():
    """Create a mock API response."""
    return {
        "data": [],
        "pagination": {"total": 0, "limit": 20, "offset": 0},
    }


@pytest.fixture
def integration_api_key():
    """Get integration test API key from environment."""
    key = os.getenv("NOVEUM_API_KEY")
    if not key:
        pytest.skip("NOVEUM_API_KEY not set")
    return key


@pytest.fixture
def integration_client(integration_api_key):
    """Create a real client for integration tests."""
    return NoveumClient(api_key=integration_api_key)


# Markers for test categorization
def pytest_configure(config):
    """Register custom markers."""
    config.addinivalue_line("markers", "unit: mark test as a unit test")
    config.addinivalue_line("markers", "integration: mark test as an integration test")
    config.addinivalue_line("markers", "slow: mark test as slow running")
