"""HTTP client with retry logic and error handling."""

import time
from typing import Any, Dict, Optional

import httpx

from .auth import ClientConfig
from .exceptions import (
    ConnectionError,
    ConnectionTimeoutError,
    NoveumAPIError,
    NoveumNetworkError,
    NoveumRateLimitError,
    NoveumTimeoutError,
    RequestTimeoutError,
    get_exception_for_status_code,
)


class HTTPClient:
    """Synchronous HTTP client with retry logic."""

    def __init__(self, config: ClientConfig):
        """
        Initialize HTTP client.

        Args:
            config: Client configuration
        """
        self.config = config
        self.client = httpx.Client(
            base_url=config.base_url,
            headers=config.get_headers(),
            timeout=config.timeout,
        )

    def request(
        self,
        method: str,
        url: str,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        """
        Make HTTP request with retry logic.

        Args:
            method: HTTP method (GET, POST, etc.)
            url: Request URL
            **kwargs: Additional arguments to pass to httpx

        Returns:
            Parsed JSON response

        Raises:
            NoveumAPIError: If API returns an error
            NoveumNetworkError: If network error occurs
        """
        for attempt in range(self.config.max_retries + 1):
            try:
                response = self.client.request(method, url, **kwargs)
                return self._handle_response(response)

            except httpx.TimeoutException as e:
                if attempt == self.config.max_retries:
                    raise NoveumTimeoutError(f"Request timeout after {self.config.timeout}s") from e
                self._wait_before_retry(attempt)

            except httpx.ConnectError as e:
                if attempt == self.config.max_retries:
                    raise ConnectionError(f"Failed to connect to {self.config.base_url}") from e
                self._wait_before_retry(attempt)

            except httpx.RequestError as e:
                if attempt == self.config.max_retries:
                    raise NoveumNetworkError(f"Network error: {str(e)}") from e
                self._wait_before_retry(attempt)

        raise NoveumNetworkError("Max retries exceeded")

    def get(self, url: str, **kwargs: Any) -> Dict[str, Any]:
        """Make GET request."""
        return self.request("GET", url, **kwargs)

    def post(self, url: str, **kwargs: Any) -> Dict[str, Any]:
        """Make POST request."""
        return self.request("POST", url, **kwargs)

    def put(self, url: str, **kwargs: Any) -> Dict[str, Any]:
        """Make PUT request."""
        return self.request("PUT", url, **kwargs)

    def patch(self, url: str, **kwargs: Any) -> Dict[str, Any]:
        """Make PATCH request."""
        return self.request("PATCH", url, **kwargs)

    def delete(self, url: str, **kwargs: Any) -> Dict[str, Any]:
        """Make DELETE request."""
        return self.request("DELETE", url, **kwargs)

    def _handle_response(self, response: httpx.Response) -> Dict[str, Any]:
        """
        Handle HTTP response and raise exceptions for errors.

        Args:
            response: HTTP response

        Returns:
            Parsed JSON response

        Raises:
            NoveumAPIError: If response indicates an error
        """
        # Success response
        if 200 <= response.status_code < 300:
            try:
                return response.json()
            except ValueError:
                return {}

        # Rate limit
        if response.status_code == 429:
            retry_after = response.headers.get("Retry-After")
            retry_after_int = int(retry_after) if retry_after else None
            raise NoveumRateLimitError(
                "Rate limit exceeded",
                retry_after=retry_after_int,
                status_code=429,
                response_data=self._parse_error_response(response),
            )

        # Other errors
        error_data = self._parse_error_response(response)
        message = error_data.get("message", response.text or f"HTTP {response.status_code}")

        raise get_exception_for_status_code(
            response.status_code,
            message,
            error_data,
        )

    @staticmethod
    def _parse_error_response(response: httpx.Response) -> Dict[str, Any]:
        """Parse error response from API."""
        try:
            return response.json()
        except ValueError:
            return {"message": response.text or f"HTTP {response.status_code}"}

    def _wait_before_retry(self, attempt: int) -> None:
        """Wait before retrying with exponential backoff."""
        wait_time = self.config.retry_backoff_factor ** attempt
        time.sleep(wait_time)

    def close(self) -> None:
        """Close HTTP client."""
        self.client.close()

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()


class AsyncHTTPClient:
    """Asynchronous HTTP client with retry logic."""

    def __init__(self, config: ClientConfig):
        """
        Initialize async HTTP client.

        Args:
            config: Client configuration
        """
        self.config = config
        self.client = httpx.AsyncClient(
            base_url=config.base_url,
            headers=config.get_headers(),
            timeout=config.timeout,
        )

    async def request(
        self,
        method: str,
        url: str,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        """
        Make async HTTP request with retry logic.

        Args:
            method: HTTP method (GET, POST, etc.)
            url: Request URL
            **kwargs: Additional arguments to pass to httpx

        Returns:
            Parsed JSON response

        Raises:
            NoveumAPIError: If API returns an error
            NoveumNetworkError: If network error occurs
        """
        for attempt in range(self.config.max_retries + 1):
            try:
                response = await self.client.request(method, url, **kwargs)
                return self._handle_response(response)

            except httpx.TimeoutException as e:
                if attempt == self.config.max_retries:
                    raise NoveumTimeoutError(f"Request timeout after {self.config.timeout}s") from e
                await self._wait_before_retry(attempt)

            except httpx.ConnectError as e:
                if attempt == self.config.max_retries:
                    raise ConnectionError(f"Failed to connect to {self.config.base_url}") from e
                await self._wait_before_retry(attempt)

            except httpx.RequestError as e:
                if attempt == self.config.max_retries:
                    raise NoveumNetworkError(f"Network error: {str(e)}") from e
                await self._wait_before_retry(attempt)

        raise NoveumNetworkError("Max retries exceeded")

    async def get(self, url: str, **kwargs: Any) -> Dict[str, Any]:
        """Make async GET request."""
        return await self.request("GET", url, **kwargs)

    async def post(self, url: str, **kwargs: Any) -> Dict[str, Any]:
        """Make async POST request."""
        return await self.request("POST", url, **kwargs)

    async def put(self, url: str, **kwargs: Any) -> Dict[str, Any]:
        """Make async PUT request."""
        return await self.request("PUT", url, **kwargs)

    async def patch(self, url: str, **kwargs: Any) -> Dict[str, Any]:
        """Make async PATCH request."""
        return await self.request("PATCH", url, **kwargs)

    async def delete(self, url: str, **kwargs: Any) -> Dict[str, Any]:
        """Make async DELETE request."""
        return await self.request("DELETE", url, **kwargs)

    def _handle_response(self, response: httpx.Response) -> Dict[str, Any]:
        """
        Handle HTTP response and raise exceptions for errors.

        Args:
            response: HTTP response

        Returns:
            Parsed JSON response

        Raises:
            NoveumAPIError: If response indicates an error
        """
        # Success response
        if 200 <= response.status_code < 300:
            try:
                return response.json()
            except ValueError:
                return {}

        # Rate limit
        if response.status_code == 429:
            retry_after = response.headers.get("Retry-After")
            retry_after_int = int(retry_after) if retry_after else None
            raise NoveumRateLimitError(
                "Rate limit exceeded",
                retry_after=retry_after_int,
                status_code=429,
                response_data=self._parse_error_response(response),
            )

        # Other errors
        error_data = self._parse_error_response(response)
        message = error_data.get("message", response.text or f"HTTP {response.status_code}")

        raise get_exception_for_status_code(
            response.status_code,
            message,
            error_data,
        )

    @staticmethod
    def _parse_error_response(response: httpx.Response) -> Dict[str, Any]:
        """Parse error response from API."""
        try:
            return response.json()
        except ValueError:
            return {"message": response.text or f"HTTP {response.status_code}"}

    async def _wait_before_retry(self, attempt: int) -> None:
        """Wait before retrying with exponential backoff."""
        import asyncio

        wait_time = self.config.retry_backoff_factor ** attempt
        await asyncio.sleep(wait_time)

    async def close(self) -> None:
        """Close async HTTP client."""
        await self.client.aclose()

    async def __aenter__(self):
        """Async context manager entry."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()
