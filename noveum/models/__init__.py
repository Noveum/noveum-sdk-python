"""
Data models for Noveum SDK.

All models are Pydantic-based for validation, serialization, and IDE support.
"""

from .common import PaginatedResponse, PaginationMeta
from .datasets import Dataset, DatasetItem, DatasetItemType, DatasetVersion
from .evals import EvalRequest, EvalResult, ScorerConfig, ScorerResult, TestResult
from .scorers import Scorer, ScorerMetadata
from .traces import Span, Trace, TraceStatus

__all__ = [
    # Common
    "PaginatedResponse",
    "PaginationMeta",
    # Datasets
    "Dataset",
    "DatasetItem",
    "DatasetItemType",
    "DatasetVersion",
    # Traces
    "Trace",
    "Span",
    "TraceStatus",
    # Scorers
    "Scorer",
    "ScorerMetadata",
    # Evals
    "EvalRequest",
    "EvalResult",
    "ScorerConfig",
    "ScorerResult",
    "TestResult",
]
