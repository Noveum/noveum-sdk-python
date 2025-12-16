"""Base resource class for all API resources."""

from typing import Any, Dict, Optional

from ..http_client import HTTPClient, AsyncHTTPClient


class BaseResource:
    """Base class for all API resources."""

    def __init__(self, http_client: HTTPClient):
        """
        Initialize resource.

        Args:
            http_client: HTTP client instance
        """
        self.http_client = http_client

    def _build_url(self, path: str) -> str:
        """
        Build full URL for endpoint.

        Args:
            path: API path (e.g., '/datasets')

        Returns:
            Full URL
        """
        return path.lstrip("/")

    def _build_query_params(self, **kwargs) -> Dict[str, Any]:
        """
        Build query parameters, filtering out None values.

        Args:
            **kwargs: Query parameters

        Returns:
            Dictionary of non-None parameters
        """
        return {k: v for k, v in kwargs.items() if v is not None}


class AsyncBaseResource:
    """Base class for all async API resources."""

    def __init__(self, http_client: AsyncHTTPClient):
        """
        Initialize async resource.

        Args:
            http_client: Async HTTP client instance
        """
        self.http_client = http_client

    def _build_url(self, path: str) -> str:
        """
        Build full URL for endpoint.

        Args:
            path: API path (e.g., '/datasets')

        Returns:
            Full URL
        """
        return path.lstrip("/")

    def _build_query_params(self, **kwargs) -> Dict[str, Any]:
        """
        Build query parameters, filtering out None values.

        Args:
            **kwargs: Query parameters

        Returns:
            Dictionary of non-None parameters
        """
        return {k: v for k, v in kwargs.items() if v is not None}
