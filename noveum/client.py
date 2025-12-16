"""Main Noveum SDK client."""

from typing import Optional

from .auth import ClientConfig
from .http_client import HTTPClient, AsyncHTTPClient
from .resources.datasets import DatasetsResource, AsyncDatasetsResource
from .resources.evals import EvalsResource, AsyncEvalsResource
from .resources.scorers import ScorersResource, AsyncScorersResource
from .resources.traces import TracesResource, AsyncTracesResource


class NoveumClient:
    """
    Synchronous Noveum SDK client.

    Main entry point for interacting with Noveum API.

    Example:
        >>> client = NoveumClient()
        >>> datasets = client.datasets.list()
        >>> for dataset in datasets:
        ...     print(dataset.name)
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = "https://api.noveum.ai/api/v1",
        timeout: float = 30.0,
        max_retries: int = 3,
    ):
        """
        Initialize Noveum client.

        Args:
            api_key: API key for authentication. If None, loads from NOVEM_API_KEY env var.
            base_url: Base URL for API requests
            timeout: Request timeout in seconds
            max_retries: Maximum number of retries for failed requests

        Raises:
            InvalidAPIKeyError: If API key is invalid or not provided
            NoveumConfigurationError: If configuration is invalid
        """
        self.config = ClientConfig(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
        )

        self._http_client = HTTPClient(self.config)

        # Initialize resources
        self.datasets = DatasetsResource(self._http_client)
        self.traces = TracesResource(self._http_client)
        self.scorers = ScorersResource(self._http_client)
        self.evals = EvalsResource(self._http_client)

    def close(self) -> None:
        """Close HTTP client and cleanup resources."""
        self._http_client.close()

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()

    def __repr__(self) -> str:
        """Return string representation."""
        return f"NoveumClient(config={self.config})"


class AsyncNoveumClient:
    """
    Asynchronous Noveum SDK client.

    Main entry point for async interaction with Noveum API.

    Example:
        >>> async with AsyncNoveumClient() as client:
        ...     datasets = await client.datasets.list()
        ...     async for dataset in datasets:
        ...         print(dataset.name)
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = "https://api.noveum.ai/api/v1",
        timeout: float = 30.0,
        max_retries: int = 3,
    ):
        """
        Initialize async Noveum client.

        Args:
            api_key: API key for authentication. If None, loads from NOVEM_API_KEY env var.
            base_url: Base URL for API requests
            timeout: Request timeout in seconds
            max_retries: Maximum number of retries for failed requests

        Raises:
            InvalidAPIKeyError: If API key is invalid or not provided
            NoveumConfigurationError: If configuration is invalid
        """
        self.config = ClientConfig(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
        )

        self._http_client = AsyncHTTPClient(self.config)

        # Initialize async resources
        self.datasets = AsyncDatasetsResource(self._http_client)
        self.traces = AsyncTracesResource(self._http_client)
        self.scorers = AsyncScorersResource(self._http_client)
        self.evals = AsyncEvalsResource(self._http_client)

    async def close(self) -> None:
        """Close HTTP client and cleanup resources."""
        await self._http_client.close()

    async def __aenter__(self):
        """Async context manager entry."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()

    def __repr__(self) -> str:
        """Return string representation."""
        return f"AsyncNoveumClient(config={self.config})"
