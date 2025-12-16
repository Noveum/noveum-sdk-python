"""Pagination utilities for handling API pagination transparently."""

from typing import Any, Callable, Generic, Iterator, List, Optional, TypeVar

T = TypeVar("T")


class PaginatedIterator(Generic[T]):
    """Iterator for paginated API responses."""

    def __init__(
        self,
        fetch_fn: Callable[[int, int], tuple[List[T], int]],
        limit: int = 100,
        offset: int = 0,
    ):
        """
        Initialize paginated iterator.

        Args:
            fetch_fn: Function that fetches items. Should return (items, total_count).
            limit: Items per page
            offset: Starting offset
        """
        self.fetch_fn = fetch_fn
        self.limit = limit
        self.offset = offset
        self.current_page: Optional[List[T]] = None
        self.current_index = 0
        self.total_count: Optional[int] = None
        self.items_fetched = 0

    def __iter__(self) -> Iterator[T]:
        """Return iterator."""
        return self

    def __next__(self) -> T:
        """Get next item."""
        # Load first page if needed
        if self.current_page is None:
            self._load_next_page()

        # Check if we've reached the end
        if self.current_page is None or (
            self.total_count is not None and self.items_fetched >= self.total_count
        ):
            raise StopIteration

        # Check if we need to load next page
        if self.current_index >= len(self.current_page):
            self._load_next_page()
            if self.current_page is None:
                raise StopIteration

        # Get item from current page
        item = self.current_page[self.current_index]
        self.current_index += 1
        self.items_fetched += 1
        return item

    def _load_next_page(self) -> None:
        """Load next page of results."""
        items, total_count = self.fetch_fn(self.limit, self.offset)
        self.current_page = items
        self.current_index = 0
        self.total_count = total_count
        self.offset += self.limit

    def by_page(self, page_size: Optional[int] = None) -> Iterator[List[T]]:
        """
        Iterate by page instead of by item.

        Args:
            page_size: Items per page (overrides default)

        Yields:
            Lists of items (pages)
        """
        if page_size:
            self.limit = page_size

        while True:
            items, total_count = self.fetch_fn(self.limit, self.offset)
            self.total_count = total_count

            if not items:
                break

            yield items
            self.offset += self.limit

            # Check if we've fetched all items
            if len(items) < self.limit:
                break


class AsyncPaginatedIterator(Generic[T]):
    """Async iterator for paginated API responses."""

    def __init__(
        self,
        fetch_fn: Callable[[int, int], Any],
        limit: int = 100,
        offset: int = 0,
    ):
        """
        Initialize async paginated iterator.

        Args:
            fetch_fn: Async function that fetches items. Should return (items, total_count).
            limit: Items per page
            offset: Starting offset
        """
        self.fetch_fn = fetch_fn
        self.limit = limit
        self.offset = offset
        self.current_page: Optional[List[T]] = None
        self.current_index = 0
        self.total_count: Optional[int] = None
        self.items_fetched = 0

    def __aiter__(self):
        """Return async iterator."""
        return self

    async def __anext__(self) -> T:
        """Get next item asynchronously."""
        # Load first page if needed
        if self.current_page is None:
            await self._load_next_page()

        # Check if we've reached the end
        if self.current_page is None or (
            self.total_count is not None and self.items_fetched >= self.total_count
        ):
            raise StopAsyncIteration

        # Check if we need to load next page
        if self.current_index >= len(self.current_page):
            await self._load_next_page()
            if self.current_page is None:
                raise StopAsyncIteration

        # Get item from current page
        item = self.current_page[self.current_index]
        self.current_index += 1
        self.items_fetched += 1
        return item

    async def _load_next_page(self) -> None:
        """Load next page of results asynchronously."""
        items, total_count = await self.fetch_fn(self.limit, self.offset)
        self.current_page = items
        self.current_index = 0
        self.total_count = total_count
        self.offset += self.limit

    async def by_page(self, page_size: Optional[int] = None):
        """
        Iterate by page instead of by item asynchronously.

        Args:
            page_size: Items per page (overrides default)

        Yields:
            Lists of items (pages)
        """
        if page_size:
            self.limit = page_size

        while True:
            items, total_count = await self.fetch_fn(self.limit, self.offset)
            self.total_count = total_count

            if not items:
                break

            yield items
            self.offset += self.limit

            # Check if we've fetched all items
            if len(items) < self.limit:
                break
