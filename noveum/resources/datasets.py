"""Datasets resource for dataset operations."""

from typing import AsyncIterator, Iterator, Optional

from ..http_client import AsyncHTTPClient, HTTPClient
from ..models.datasets import Dataset, DatasetItem
from ..pagination import AsyncPaginatedIterator, PaginatedIterator
from .base import AsyncBaseResource, BaseResource


class DatasetsResource(BaseResource):
    """Synchronous datasets resource."""

    def list(
        self,
        limit: int = 20,
        offset: int = 0,
        visibility: str = "public",
        include_versions: bool = False,
    ) -> Iterator[Dataset]:
        """
        List datasets with pagination.

        Args:
            limit: Items per page
            offset: Starting offset
            visibility: Filter by visibility ('public', 'private', etc.)
            include_versions: Include version information

        Yields:
            Dataset objects

        Example:
            >>> for dataset in client.datasets.list():
            ...     print(dataset.name)
        """

        def fetch_fn(limit: int, offset: int):
            url = self._build_url("/datasets")
            params = self._build_query_params(
                limit=limit,
                offset=offset,
                visibility=visibility,
                includeVersions=include_versions,
            )
            response = self.http_client.get(url, params=params)

            items = [Dataset(**item) for item in response.get("data", [])]
            total = response.get("pagination", {}).get("total", 0)
            return items, total

        return PaginatedIterator(fetch_fn, limit=limit, offset=offset)

    def get(self, dataset_slug: str) -> Dataset:
        """
        Get a specific dataset by slug.

        Args:
            dataset_slug: Dataset slug identifier

        Returns:
            Dataset object

        Raises:
            NoveumNotFoundError: If dataset not found

        Example:
            >>> dataset = client.datasets.get("my-dataset")
        """
        url = self._build_url(f"/datasets/{dataset_slug}")
        response = self.http_client.get(url)
        return Dataset(**response)

    def items(
        self,
        dataset_slug: str,
        limit: int = 100,
        offset: int = 0,
    ) -> Iterator[DatasetItem]:
        """
        Get items from a dataset with pagination.

        This is the primary method for loading test data in CI/CD.

        Args:
            dataset_slug: Dataset slug identifier
            limit: Items per page
            offset: Starting offset

        Yields:
            DatasetItem objects

        Example:
            >>> for item in client.datasets.items("regression-tests"):
            ...     output = agent.run(item.input_text)
            ...     result = client.evals.score(item, output, scorers)
        """

        def fetch_fn(limit: int, offset: int):
            url = self._build_url(f"/datasets/{dataset_slug}/items")
            params = self._build_query_params(limit=limit, offset=offset)
            response = self.http_client.get(url, params=params)

            items = [DatasetItem(**item) for item in response.get("data", [])]
            total = response.get("pagination", {}).get("total", 0)
            return items, total

        return PaginatedIterator(fetch_fn, limit=limit, offset=offset)

    def get_item(self, dataset_slug: str, item_id: str) -> DatasetItem:
        """
        Get a specific dataset item.

        Args:
            dataset_slug: Dataset slug identifier
            item_id: Item identifier

        Returns:
            DatasetItem object

        Raises:
            NoveumNotFoundError: If item not found

        Example:
            >>> item = client.datasets.get_item("my-dataset", "item-123")
        """
        url = self._build_url(f"/datasets/{dataset_slug}/items/{item_id}")
        response = self.http_client.get(url)
        return DatasetItem(**response)


class AsyncDatasetsResource(AsyncBaseResource):
    """Asynchronous datasets resource."""

    async def list(
        self,
        limit: int = 20,
        offset: int = 0,
        visibility: str = "public",
        include_versions: bool = False,
    ) -> AsyncIterator[Dataset]:
        """
        Async list datasets with pagination.

        Args:
            limit: Items per page
            offset: Starting offset
            visibility: Filter by visibility
            include_versions: Include version information

        Yields:
            Dataset objects
        """

        async def fetch_fn(limit: int, offset: int):
            url = self._build_url("/datasets")
            params = self._build_query_params(
                limit=limit,
                offset=offset,
                visibility=visibility,
                includeVersions=include_versions,
            )
            response = await self.http_client.get(url, params=params)

            items = [Dataset(**item) for item in response.get("data", [])]
            total = response.get("pagination", {}).get("total", 0)
            return items, total

        async for item in AsyncPaginatedIterator(fetch_fn, limit=limit, offset=offset):
            yield item

    async def get(self, dataset_slug: str) -> Dataset:
        """
        Async get a specific dataset by slug.

        Args:
            dataset_slug: Dataset slug identifier

        Returns:
            Dataset object
        """
        url = self._build_url(f"/datasets/{dataset_slug}")
        response = await self.http_client.get(url)
        return Dataset(**response)

    async def items(
        self,
        dataset_slug: str,
        limit: int = 100,
        offset: int = 0,
    ) -> AsyncIterator[DatasetItem]:
        """
        Async get items from a dataset with pagination.

        Args:
            dataset_slug: Dataset slug identifier
            limit: Items per page
            offset: Starting offset

        Yields:
            DatasetItem objects
        """

        async def fetch_fn(limit: int, offset: int):
            url = self._build_url(f"/datasets/{dataset_slug}/items")
            params = self._build_query_params(limit=limit, offset=offset)
            response = await self.http_client.get(url, params=params)

            items = [DatasetItem(**item) for item in response.get("data", [])]
            total = response.get("pagination", {}).get("total", 0)
            return items, total

        async for item in AsyncPaginatedIterator(fetch_fn, limit=limit, offset=offset):
            yield item

    async def get_item(self, dataset_slug: str, item_id: str) -> DatasetItem:
        """
        Async get a specific dataset item.

        Args:
            dataset_slug: Dataset slug identifier
            item_id: Item identifier

        Returns:
            DatasetItem object
        """
        url = self._build_url(f"/datasets/{dataset_slug}/items/{item_id}")
        response = await self.http_client.get(url)
        return DatasetItem(**response)
