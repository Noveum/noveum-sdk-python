"""Authentication module for Noveum SDK.

Supports API key authentication only. No login/session management.
API keys are generated on Noveum.ai and passed to the SDK.
"""

import os
from typing import Optional

from .exceptions import InvalidAPIKeyError, NoveumConfigurationError


class APIKeyAuth:
    """API key authentication handler."""

    ENV_VAR_NAME = "NOVEM_API_KEY"

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize API key authentication.

        Args:
            api_key: API key. If None, will try to load from environment variable.

        Raises:
            InvalidAPIKeyError: If no valid API key is provided or found.
        """
        self.api_key = api_key or self._load_from_env()

        if not self.api_key:
            raise InvalidAPIKeyError(
                f"No API key provided. Pass api_key parameter or set {self.ENV_VAR_NAME} "
                "environment variable. Get your API key from https://noveum.ai/settings/api-keys"
            )

        if not self._is_valid_format(self.api_key):
            raise InvalidAPIKeyError("API key format is invalid")

    @staticmethod
    def _load_from_env() -> Optional[str]:
        """Load API key from environment variable."""
        api_key = os.environ.get(APIKeyAuth.ENV_VAR_NAME)
        if api_key:
            api_key = api_key.strip()
        return api_key if api_key else None

    @staticmethod
    def _is_valid_format(api_key: str) -> bool:
        """
        Validate API key format.

        Args:
            api_key: API key to validate

        Returns:
            True if format is valid, False otherwise
        """
        # Basic validation: non-empty string
        # Adjust based on actual API key format from Noveum.ai
        return isinstance(api_key, str) and len(api_key) > 0

    def get_headers(self) -> dict:
        """
        Get HTTP headers for API requests.

        Returns:
            Dictionary with Authorization header
        """
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def __repr__(self) -> str:
        """Return string representation (masked API key)."""
        masked = f"{self.api_key[:4]}...{self.api_key[-4:]}" if self.api_key else "***"
        return f"APIKeyAuth(api_key={masked})"


class ClientConfig:
    """Client configuration."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = "https://api.noveum.ai/api/v1",
        timeout: float = 30.0,
        max_retries: int = 3,
        retry_backoff_factor: float = 2.0,
    ):
        """
        Initialize client configuration.

        Args:
            api_key: API key for authentication
            base_url: Base URL for API requests
            timeout: Request timeout in seconds
            max_retries: Maximum number of retries for failed requests
            retry_backoff_factor: Backoff factor for exponential retry

        Raises:
            InvalidAPIKeyError: If API key is invalid
            NoveumConfigurationError: If configuration is invalid
        """
        self.auth = APIKeyAuth(api_key)
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries
        self.retry_backoff_factor = retry_backoff_factor

        if timeout <= 0:
            raise NoveumConfigurationError("timeout must be positive")

        if max_retries < 0:
            raise NoveumConfigurationError("max_retries must be non-negative")

        if retry_backoff_factor <= 1:
            raise NoveumConfigurationError("retry_backoff_factor must be > 1")

    def get_headers(self) -> dict:
        """Get HTTP headers for requests."""
        return self.auth.get_headers()

    def __repr__(self) -> str:
        """Return string representation."""
        return (
            f"ClientConfig(base_url={self.base_url}, timeout={self.timeout}, "
            f"max_retries={self.max_retries}, auth={self.auth})"
        )
