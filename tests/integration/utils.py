"""
Shared utilities for integration tests.

These helpers standardize response parsing and assertions.
"""

from __future__ import annotations

import json
from collections.abc import Iterable
from typing import Any

import pytest


def parse_response(response: Any) -> Any:
    """Parse response body, handling SDK models and raw content."""
    if response is None:
        return None
    parsed = getattr(response, "parsed", None)
    if parsed is not None:
        if hasattr(parsed, "to_dict"):
            return parsed.to_dict()
        return parsed
    content = getattr(response, "content", None)
    if content:
        try:
            return json.loads(content)
        except (json.JSONDecodeError, TypeError):
            return None
    return None


def get_field(obj: Any, field: str) -> Any:
    """Get field value from dict or object."""
    if obj is None:
        return None
    if isinstance(obj, dict):
        return obj.get(field)
    return getattr(obj, field, None)


def ensure_dict(value: Any, message: str) -> dict[str, Any]:
    """Ensure value is a dict."""
    if not isinstance(value, dict):
        pytest.fail(message)
    return value


def ensure_list(value: Any, message: str) -> list[Any]:
    """Ensure value is a list."""
    if not isinstance(value, list):
        pytest.fail(message)
    return value


def assert_has_keys(obj: dict[str, Any], keys: Iterable[str], context: str) -> None:
    """Assert a dict has expected keys."""
    missing = [key for key in keys if key not in obj]
    if missing:
        pytest.fail(f"{context} missing keys: {missing}")


def assert_non_empty_string(value: Any, context: str) -> None:
    """Assert value is a non-empty string."""
    if not isinstance(value, str) or not value.strip():
        pytest.fail(f"{context} should be a non-empty string")


def assert_positive_number(value: Any, context: str) -> None:
    """Assert value is a positive number."""
    if not isinstance(value, (int, float)) or value <= 0:
        pytest.fail(f"{context} should be a positive number")


def assert_optional_string(value: Any, context: str) -> None:
    """Assert value is None or a non-empty string."""
    if value is None:
        return
    assert_non_empty_string(value, context)
