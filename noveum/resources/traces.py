"""Traces resource for trace operations."""

from typing import AsyncIterator, Iterator, List, Optional

from ..http_client import AsyncHTTPClient, HTTPClient
from ..models.traces import Trace
from ..pagination import AsyncPaginatedIterator, PaginatedIterator
from .base import AsyncBaseResource, BaseResource


class TracesResource(BaseResource):
    """Synchronous traces resource."""

    def submit(self, traces: List[Trace]) -> dict:
        """
        Submit traces to Noveum.

        This is typically called by the noveum-trace instrumentation library,
        not directly by SDK users.

        Args:
            traces: List of Trace objects to submit

        Returns:
            Response from API

        Example:
            >>> traces = [trace1, trace2]
            >>> response = client.traces.submit(traces)
        """
        url = self._build_url("/traces")
        payload = {
            "traces": [t.model_dump() for t in traces],
            "timestamp": int(__import__("time").time() * 1000),
        }
        return self.http_client.post(url, json=payload)

    def list(
        self,
        project: Optional[str] = None,
        limit: int = 100,
        offset: int = 0,
    ) -> Iterator[Trace]:
        """
        List traces with pagination.

        Args:
            project: Filter by project name
            limit: Items per page
            offset: Starting offset

        Yields:
            Trace objects
        """

        def fetch_fn(limit: int, offset: int):
            url = self._build_url("/traces")
            params = self._build_query_params(
                project=project,
                limit=limit,
                offset=offset,
            )
            response = self.http_client.get(url, params=params)

            items = [Trace(**item) for item in response.get("data", [])]
            total = response.get("pagination", {}).get("total", 0)
            return items, total

        return PaginatedIterator(fetch_fn, limit=limit, offset=offset)

    def get(self, trace_id: str) -> Trace:
        """
        Get a specific trace by ID.

        Args:
            trace_id: Trace identifier

        Returns:
            Trace object

        Raises:
            NoveumNotFoundError: If trace not found
        """
        url = self._build_url(f"/traces/{trace_id}")
        response = self.http_client.get(url)
        return Trace(**response)


class AsyncTracesResource(AsyncBaseResource):
    """Asynchronous traces resource."""

    async def submit(self, traces: List[Trace]) -> dict:
        """
        Async submit traces to Noveum.

        Args:
            traces: List of Trace objects to submit

        Returns:
            Response from API
        """
        url = self._build_url("/traces")
        payload = {
            "traces": [t.model_dump() for t in traces],
            "timestamp": int(__import__("time").time() * 1000),
        }
        return await self.http_client.post(url, json=payload)

    async def list(
        self,
        project: Optional[str] = None,
        limit: int = 100,
        offset: int = 0,
    ) -> AsyncIterator[Trace]:
        """
        Async list traces with pagination.

        Args:
            project: Filter by project name
            limit: Items per page
            offset: Starting offset

        Yields:
            Trace objects
        """

        async def fetch_fn(limit: int, offset: int):
            url = self._build_url("/traces")
            params = self._build_query_params(
                project=project,
                limit=limit,
                offset=offset,
            )
            response = await self.http_client.get(url, params=params)

            items = [Trace(**item) for item in response.get("data", [])]
            total = response.get("pagination", {}).get("total", 0)
            return items, total

        async for item in AsyncPaginatedIterator(fetch_fn, limit=limit, offset=offset):
            yield item

    async def get(self, trace_id: str) -> Trace:
        """
        Async get a specific trace by ID.

        Args:
            trace_id: Trace identifier

        Returns:
            Trace object
        """
        url = self._build_url(f"/traces/{trace_id}")
        response = await self.http_client.get(url)
        return Trace(**response)
