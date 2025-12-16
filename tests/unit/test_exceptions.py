"""Unit tests for exceptions."""

import pytest

from noveum.exceptions import (
    ConnectionError,
    InvalidAPIKeyError,
    InvalidParameterError,
    MissingParameterError,
    NoveumAPIError,
    NoveumAuthenticationError,
    NoveumConflictError,
    NoveumError,
    NoveumInternalError,
    NoveumNetworkError,
    NoveumNotFoundError,
    NoveumRateLimitError,
    NoveumTimeoutError,
    NoveumValidationError,
)


@pytest.mark.unit
class TestExceptionHierarchy:
    """Tests for exception hierarchy."""

    def test_all_exceptions_inherit_from_noveum_error(self):
        """Test that all exceptions inherit from NoveumError."""
        exceptions = [
            NoveumAPIError,
            NoveumAuthenticationError,
            NoveumNetworkError,
            InvalidAPIKeyError,
            NoveumNotFoundError,
            NoveumConflictError,
            NoveumValidationError,
            InvalidParameterError,
            MissingParameterError,
            NoveumRateLimitError,
            NoveumInternalError,
            ConnectionError,
            NoveumTimeoutError,
        ]
        for exc_class in exceptions:
            assert issubclass(exc_class, NoveumError)

    def test_invalid_api_key_error_inheritance(self):
        """Test InvalidAPIKeyError inheritance."""
        assert issubclass(InvalidAPIKeyError, NoveumAuthenticationError)

    def test_noveum_validation_error_inheritance(self):
        """Test NoveumValidationError inheritance."""
        assert issubclass(NoveumValidationError, NoveumAPIError)

    def test_noveum_rate_limit_error_inheritance(self):
        """Test NoveumRateLimitError inheritance."""
        assert issubclass(NoveumRateLimitError, NoveumAPIError)

    def test_noveum_not_found_error_inheritance(self):
        """Test NoveumNotFoundError inheritance."""
        assert issubclass(NoveumNotFoundError, NoveumAPIError)


@pytest.mark.unit
class TestExceptionCreation:
    """Tests for exception creation and attributes."""

    def test_noveum_error_creation(self):
        """Test creating a NoveumError."""
        error = NoveumError("Test error")
        assert str(error) == "Test error"

    def test_invalid_api_key_error_creation(self):
        """Test creating an InvalidAPIKeyError."""
        error = InvalidAPIKeyError("Invalid key")
        assert "Invalid key" in str(error)

    def test_noveum_not_found_error_creation(self):
        """Test creating a NoveumNotFoundError."""
        error = NoveumNotFoundError("Resource not found")
        assert "Resource not found" in str(error)

    def test_noveum_validation_error_with_errors(self):
        """Test creating a NoveumValidationError with errors."""
        errors = [{"field": "name", "message": "Required"}]
        error = NoveumValidationError("Validation failed", errors=errors)
        assert error.errors == errors

    def test_noveum_rate_limit_error_with_retry_after(self):
        """Test creating a NoveumRateLimitError with retry_after."""
        error = NoveumRateLimitError("Rate limited", retry_after=60)
        assert error.retry_after == 60

    def test_noveum_conflict_error_creation(self):
        """Test creating a NoveumConflictError."""
        error = NoveumConflictError("Resource already exists")
        assert "Resource already exists" in str(error)

    def test_noveum_internal_error_creation(self):
        """Test creating a NoveumInternalError."""
        error = NoveumInternalError("Internal server error")
        assert "Internal server error" in str(error)

    def test_noveum_timeout_error_creation(self):
        """Test creating a NoveumTimeoutError."""
        error = NoveumTimeoutError("Request timeout")
        assert "Request timeout" in str(error)

    def test_noveum_network_error_creation(self):
        """Test creating a NoveumNetworkError."""
        error = NoveumNetworkError("Network error")
        assert "Network error" in str(error)


@pytest.mark.unit
class TestExceptionMessages:
    """Tests for exception messages."""

    def test_exception_message_preservation(self):
        """Test that exception messages are preserved."""
        message = "This is a test error message"
        error = NoveumError(message)
        assert message in str(error)

    def test_exception_repr(self):
        """Test exception repr."""
        error = NoveumError("Test")
        assert "NoveumError" in repr(error)

    def test_authentication_error_message(self):
        """Test authentication error message."""
        error = NoveumAuthenticationError("Auth failed")
        assert "Auth failed" in str(error)

    def test_parameter_error_messages(self):
        """Test parameter error messages."""
        error1 = InvalidParameterError("param", "Invalid value")
        error2 = MissingParameterError("param")
        
        assert "param" in str(error1)
        assert "param" in str(error2)
