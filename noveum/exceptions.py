"""
Exception hierarchy for Noveum SDK.

All SDK exceptions inherit from NoveumError, enabling granular error handling.
"""

from typing import Any, Dict, Optional


class NoveumError(Exception):
    """Base exception for all Noveum SDK errors."""

    def __init__(
        self,
        message: str,
        status_code: Optional[int] = None,
        response_data: Optional[Dict[str, Any]] = None,
    ):
        """
        Initialize NoveumError.

        Args:
            message: Error message
            status_code: HTTP status code (if applicable)
            response_data: Raw response data from API (if applicable)
        """
        self.message = message
        self.status_code = status_code
        self.response_data = response_data
        super().__init__(message)

    def __str__(self) -> str:
        """Return string representation of error."""
        if self.status_code:
            return f"[{self.status_code}] {self.message}"
        return self.message


class NoveumAuthenticationError(NoveumError):
    """Raised when authentication fails."""

    pass


class InvalidAPIKeyError(NoveumAuthenticationError):
    """Raised when API key is invalid or missing."""

    pass


class NoveumAPIError(NoveumError):
    """Base class for API-related errors."""

    pass


class NoveumNotFoundError(NoveumAPIError):
    """Raised when a requested resource is not found (404)."""

    pass


class NoveumConflictError(NoveumAPIError):
    """Raised when there is a conflict with existing resource (409)."""

    pass


class NoveumValidationError(NoveumAPIError):
    """Raised when request validation fails."""

    def __init__(
        self,
        message: str,
        errors: Optional[Dict[str, Any]] = None,
        status_code: Optional[int] = None,
        response_data: Optional[Dict[str, Any]] = None,
    ):
        """
        Initialize NoveumValidationError.

        Args:
            message: Error message
            errors: Validation error details
            status_code: HTTP status code
            response_data: Raw response data
        """
        super().__init__(message, status_code, response_data)
        self.errors = errors or {}

    def __str__(self) -> str:
        """Return string representation with validation details."""
        base = super().__str__()
        if self.errors:
            return f"{base} - Errors: {self.errors}"
        return base


class InvalidParameterError(NoveumValidationError):
    """Raised when a parameter has an invalid value."""

    pass


class MissingParameterError(NoveumValidationError):
    """Raised when a required parameter is missing."""

    pass


class NoveumRateLimitError(NoveumAPIError):
    """Raised when rate limit is exceeded (429)."""

    def __init__(
        self,
        message: str,
        retry_after: Optional[int] = None,
        status_code: int = 429,
        response_data: Optional[Dict[str, Any]] = None,
    ):
        """
        Initialize NoveumRateLimitError.

        Args:
            message: Error message
            retry_after: Seconds to wait before retrying
            status_code: HTTP status code
            response_data: Raw response data
        """
        super().__init__(message, status_code, response_data)
        self.retry_after = retry_after

    def __str__(self) -> str:
        """Return string representation with retry info."""
        base = super().__str__()
        if self.retry_after:
            return f"{base} (retry after {self.retry_after}s)"
        return base


class NoveumInternalError(NoveumAPIError):
    """Raised when server returns 500+ error."""

    pass


class NoveumNetworkError(NoveumError):
    """Base class for network-related errors."""

    pass


class ConnectionTimeoutError(NoveumNetworkError):
    """Raised when connection times out."""

    pass


class RequestTimeoutError(NoveumNetworkError):
    """Raised when request times out."""

    pass


class ConnectionError(NoveumNetworkError):
    """Raised when connection fails."""

    pass


class NoveumConfigurationError(NoveumError):
    """Raised when SDK configuration is invalid."""

    pass


class NoveumTimeoutError(NoveumError):
    """Raised when an operation times out."""

    pass


# Mapping of HTTP status codes to exception classes
HTTP_STATUS_TO_EXCEPTION = {
    400: NoveumValidationError,
    401: NoveumAuthenticationError,
    403: NoveumAuthenticationError,
    404: NoveumNotFoundError,
    409: NoveumConflictError,
    429: NoveumRateLimitError,
    500: NoveumInternalError,
    502: NoveumInternalError,
    503: NoveumInternalError,
    504: NoveumInternalError,
}


def get_exception_for_status_code(
    status_code: int,
    message: str,
    response_data: Optional[Dict[str, Any]] = None,
) -> NoveumAPIError:
    """
    Get appropriate exception class for HTTP status code.

    Args:
        status_code: HTTP status code
        message: Error message
        response_data: Raw response data

    Returns:
        Appropriate NoveumAPIError subclass instance
    """
    exception_class = HTTP_STATUS_TO_EXCEPTION.get(status_code, NoveumAPIError)
    return exception_class(message, status_code, response_data)
