"""Scorers resource for scorer operations."""

from typing import AsyncIterator, Iterator, Optional

from ..http_client import AsyncHTTPClient, HTTPClient
from ..models.datasets import ScorerResultItem
from ..models.scorers import Scorer
from ..pagination import AsyncPaginatedIterator, PaginatedIterator
from .base import AsyncBaseResource, BaseResource


class ScorersResource(BaseResource):
    """Synchronous scorers resource."""

    def list(
        self,
        limit: int = 100,
        offset: int = 0,
        category: Optional[str] = None,
    ) -> Iterator[Scorer]:
        """
        List available scorers with pagination.

        Args:
            limit: Items per page
            offset: Starting offset
            category: Filter by scorer category

        Yields:
            Scorer objects

        Example:
            >>> for scorer in client.scorers.list():
            ...     print(f"{scorer.name}: {scorer.description}")
        """

        def fetch_fn(limit: int, offset: int):
            url = self._build_url("/scorers")
            params = self._build_query_params(
                limit=limit,
                offset=offset,
                category=category,
            )
            response = self.http_client.get(url, params=params)

            items = [Scorer(**item) for item in response.get("data", [])]
            total = response.get("pagination", {}).get("total", 0)
            return items, total

        return PaginatedIterator(fetch_fn, limit=limit, offset=offset)

    def get(self, scorer_id: str) -> Scorer:
        """
        Get a specific scorer by ID.

        Args:
            scorer_id: Scorer identifier

        Returns:
            Scorer object

        Raises:
            NoveumNotFoundError: If scorer not found

        Example:
            >>> scorer = client.scorers.get("factuality_scorer")
        """
        url = self._build_url(f"/scorers/{scorer_id}")
        response = self.http_client.get(url)
        return Scorer(**response)

    def get_results(
        self,
        dataset_slug: Optional[str] = None,
        item_id: Optional[str] = None,
        scorer_id: Optional[str] = None,
        limit: int = 100,
        offset: int = 0,
    ) -> Iterator[ScorerResultItem]:
        """
        Get scorer results with optional filtering.

        This retrieves historical evaluation results, not for real-time evaluation.
        For real-time evaluation, use client.evals.score().

        Args:
            dataset_slug: Filter by dataset slug
            item_id: Filter by item ID
            scorer_id: Filter by scorer ID
            limit: Items per page
            offset: Starting offset

        Yields:
            ScorerResultItem objects

        Example:
            >>> for result in client.scorers.get_results(dataset_slug="my-dataset"):
            ...     print(f"Item {result.result_id}: {result.score}")
        """

        def fetch_fn(limit: int, offset: int):
            url = self._build_url("/scorers/results")
            params = self._build_query_params(
                datasetSlug=dataset_slug,
                itemId=item_id,
                scorerId=scorer_id,
                limit=limit,
                offset=offset,
            )
            response = self.http_client.get(url, params=params)

            items = [ScorerResultItem(**item) for item in response.get("data", [])]
            total = response.get("pagination", {}).get("total", 0)
            return items, total

        return PaginatedIterator(fetch_fn, limit=limit, offset=offset)


class AsyncScorersResource(AsyncBaseResource):
    """Asynchronous scorers resource."""

    async def list(
        self,
        limit: int = 100,
        offset: int = 0,
        category: Optional[str] = None,
    ) -> AsyncIterator[Scorer]:
        """
        Async list available scorers with pagination.

        Args:
            limit: Items per page
            offset: Starting offset
            category: Filter by scorer category

        Yields:
            Scorer objects
        """

        async def fetch_fn(limit: int, offset: int):
            url = self._build_url("/scorers")
            params = self._build_query_params(
                limit=limit,
                offset=offset,
                category=category,
            )
            response = await self.http_client.get(url, params=params)

            items = [Scorer(**item) for item in response.get("data", [])]
            total = response.get("pagination", {}).get("total", 0)
            return items, total

        async for item in AsyncPaginatedIterator(fetch_fn, limit=limit, offset=offset):
            yield item

    async def get(self, scorer_id: str) -> Scorer:
        """
        Async get a specific scorer by ID.

        Args:
            scorer_id: Scorer identifier

        Returns:
            Scorer object
        """
        url = self._build_url(f"/scorers/{scorer_id}")
        response = await self.http_client.get(url)
        return Scorer(**response)

    async def get_results(
        self,
        dataset_slug: Optional[str] = None,
        item_id: Optional[str] = None,
        scorer_id: Optional[str] = None,
        limit: int = 100,
        offset: int = 0,
    ) -> AsyncIterator[ScorerResultItem]:
        """
        Async get scorer results with optional filtering.

        Args:
            dataset_slug: Filter by dataset slug
            item_id: Filter by item ID
            scorer_id: Filter by scorer ID
            limit: Items per page
            offset: Starting offset

        Yields:
            ScorerResultItem objects
        """

        async def fetch_fn(limit: int, offset: int):
            url = self._build_url("/scorers/results")
            params = self._build_query_params(
                datasetSlug=dataset_slug,
                itemId=item_id,
                scorerId=scorer_id,
                limit=limit,
                offset=offset,
            )
            response = await self.http_client.get(url, params=params)

            items = [ScorerResultItem(**item) for item in response.get("data", [])]
            total = response.get("pagination", {}).get("total", 0)
            return items, total

        async for item in AsyncPaginatedIterator(fetch_fn, limit=limit, offset=offset):
            yield item
