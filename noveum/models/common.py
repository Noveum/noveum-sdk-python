"""Common data models used across the SDK."""

from datetime import datetime
from typing import Any, Dict, Generic, List, Optional, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PaginationMeta(BaseModel):
    """Pagination metadata."""

    limit: int = Field(..., description="Number of items per page")
    offset: int = Field(..., description="Number of items skipped")
    total: int = Field(..., description="Total number of items")
    has_more: bool = Field(..., description="Whether more items are available")

    @property
    def next_offset(self) -> Optional[int]:
        """Get offset for next page, or None if no more items."""
        if self.has_more:
            return self.offset + self.limit
        return None


class PaginatedResponse(BaseModel, Generic[T]):
    """Generic paginated response."""

    data: List[T] = Field(..., description="Items in this page")
    pagination: PaginationMeta = Field(..., description="Pagination metadata")


class BaseEntity(BaseModel):
    """Base model for all entities."""

    id: str = Field(..., description="Unique identifier")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="Last update timestamp")

    class Config:
        """Pydantic config."""

        json_encoders = {
            datetime: lambda v: v.isoformat() if v else None,
        }


class Metadata(BaseModel):
    """Generic metadata container."""

    extra: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")

    def __getitem__(self, key: str) -> Any:
        """Get metadata value by key."""
        return self.extra.get(key)

    def __setitem__(self, key: str, value: Any) -> None:
        """Set metadata value by key."""
        self.extra[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Get metadata value with default."""
        return self.extra.get(key, default)
