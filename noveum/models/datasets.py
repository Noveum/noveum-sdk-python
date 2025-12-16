"""Dataset data models."""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from .common import BaseEntity


class DatasetItemType(str, Enum):
    """Type of dataset item."""

    CONVERSATIONAL = "conversational"
    AGENT = "agent"
    RAG = "rag"
    CLASSIFICATION = "classification"
    EXTRACTION = "extraction"
    SUMMARIZATION = "summarization"
    TRANSLATION = "translation"
    CUSTOM = "custom"


class DatasetVersion(BaseModel):
    """Dataset version information."""

    version_id: str = Field(..., description="Version identifier")
    version_number: int = Field(..., description="Version number")
    created_at: datetime = Field(..., description="Creation timestamp")
    item_count: int = Field(..., description="Number of items in this version")
    description: Optional[str] = Field(None, description="Version description")

    class Config:
        """Pydantic config."""

        json_encoders = {
            datetime: lambda v: v.isoformat() if v else None,
        }


class Dataset(BaseEntity):
    """Dataset metadata."""

    slug: str = Field(..., description="URL-friendly dataset identifier")
    name: str = Field(..., description="Human-readable dataset name")
    description: Optional[str] = Field(None, description="Dataset description")
    item_count: int = Field(..., description="Total number of items")
    item_type: DatasetItemType = Field(..., description="Type of items in dataset")
    versions: List[DatasetVersion] = Field(default_factory=list, description="Dataset versions")
    visibility: str = Field(default="private", description="Visibility level")
    organization_id: str = Field(..., description="Organization ID")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Custom metadata")

    class Config:
        """Pydantic config."""

        json_encoders = {
            datetime: lambda v: v.isoformat() if v else None,
        }


class ScorerResultItem(BaseModel):
    """Scorer result for a dataset item."""

    result_id: str = Field(..., description="Result identifier")
    scorer_id: str = Field(..., description="Scorer identifier")
    scorer_name: str = Field(..., description="Human-readable scorer name")
    score: float = Field(..., description="Numeric score")
    passed: bool = Field(..., description="Whether item passed this scorer")
    reasoning: Optional[str] = Field(None, description="Reasoning for the score")
    execution_time_ms: Optional[int] = Field(None, description="Scorer execution time")
    created_at: datetime = Field(..., description="Result creation timestamp")

    class Config:
        """Pydantic config."""

        json_encoders = {
            datetime: lambda v: v.isoformat() if v else None,
        }


class DatasetItem(BaseEntity):
    """Single item in a dataset."""

    item_id: str = Field(..., description="Unique item identifier")
    dataset_slug: str = Field(..., description="Parent dataset slug")
    dataset_version_id: Optional[str] = Field(None, description="Dataset version ID")
    item_type: DatasetItemType = Field(default=DatasetItemType.CUSTOM, description="Type of item")
    source_trace_id: Optional[str] = Field(None, description="Source trace ID")
    
    # Content fields
    input_text: str = Field(..., description="Input/question text")
    output_text: Optional[str] = Field(None, description="Original output")
    expected_output: Optional[str] = Field(None, description="Expected output")
    
    # Conversational fields
    conversation_context: Optional[List[Dict[str, str]]] = Field(
        None, description="Conversation history"
    )
    
    # RAG fields
    retrieved_context: Optional[List[str]] = Field(None, description="Retrieved documents")
    
    # Custom fields
    custom_fields: Dict[str, Any] = Field(default_factory=dict, description="Custom fields")
    
    # Evaluation
    scorer_results: List[ScorerResultItem] = Field(
        default_factory=list, description="Scorer results for this item"
    )
    
    # Metadata
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Custom metadata")

    class Config:
        """Pydantic config."""

        json_encoders = {
            datetime: lambda v: v.isoformat() if v else None,
        }

    def get_scorer_result(self, scorer_id: str) -> Optional[ScorerResultItem]:
        """Get scorer result by ID."""
        for result in self.scorer_results:
            if result.scorer_id == scorer_id:
                return result
        return None

    def get_score(self, scorer_id: str) -> Optional[float]:
        """Get score for a specific scorer."""
        result = self.get_scorer_result(scorer_id)
        return result.score if result else None
