"""Trace data models."""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from .common import BaseEntity


class TraceStatus(str, Enum):
    """Trace execution status."""

    OK = "ok"
    ERROR = "error"
    TIMEOUT = "timeout"
    CANCELLED = "cancelled"


class SDKInfo(BaseModel):
    """SDK information."""

    name: str = Field(..., description="SDK name (e.g., 'noveum-trace')")
    version: str = Field(..., description="SDK version")


class Span(BaseModel):
    """Individual span within a trace."""

    span_id: str = Field(..., description="Unique span identifier")
    trace_id: str = Field(..., description="Parent trace identifier")
    parent_span_id: Optional[str] = Field(None, description="Parent span ID")
    name: str = Field(..., description="Span name")
    start_time: datetime = Field(..., description="Span start time")
    end_time: datetime = Field(..., description="Span end time")
    duration_ms: float = Field(..., description="Span duration in milliseconds")
    status: TraceStatus = Field(..., description="Span execution status")
    status_message: Optional[str] = Field(None, description="Status message")
    attributes: Dict[str, Any] = Field(default_factory=dict, description="Span attributes")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Custom metadata")

    class Config:
        """Pydantic config."""

        json_encoders = {
            datetime: lambda v: v.isoformat() if v else None,
        }


class Trace(BaseEntity):
    """Execution trace with hierarchical spans."""

    trace_id: str = Field(..., description="Unique trace identifier")
    name: str = Field(..., description="Trace name")
    project: str = Field(..., description="Project name")
    environment: str = Field(..., description="Environment (e.g., 'production', 'staging')")
    start_time: datetime = Field(..., description="Trace start time")
    end_time: datetime = Field(..., description="Trace end time")
    duration_ms: float = Field(..., description="Total duration in milliseconds")
    status: TraceStatus = Field(..., description="Overall trace status")
    status_message: Optional[str] = Field(None, description="Status message")
    span_count: int = Field(..., description="Number of spans")
    error_count: int = Field(..., description="Number of errors")
    sdk: SDKInfo = Field(..., description="SDK information")
    spans: List[Span] = Field(default_factory=list, description="Spans in this trace")
    attributes: Dict[str, Any] = Field(default_factory=dict, description="Trace attributes")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Custom metadata")

    class Config:
        """Pydantic config."""

        json_encoders = {
            datetime: lambda v: v.isoformat() if v else None,
        }

    def get_root_spans(self) -> List[Span]:
        """Get root spans (no parent)."""
        return [s for s in self.spans if s.parent_span_id is None]

    def get_span_children(self, span_id: str) -> List[Span]:
        """Get all child spans for a given span."""
        return [s for s in self.spans if s.parent_span_id == span_id]
