"""Scorer data models."""

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from .common import BaseEntity


class ScorerMetadata(BaseModel):
    """Metadata for a scorer."""

    input_schema: Optional[Dict[str, Any]] = Field(None, description="Input schema")
    output_schema: Optional[Dict[str, Any]] = Field(None, description="Output schema")
    score_range: tuple = Field(default=(0, 10), description="Score range (min, max)")
    requires_expected_output: bool = Field(
        False, description="Whether scorer requires expected output"
    )
    supports_batch: bool = Field(False, description="Whether scorer supports batch evaluation")
    estimated_latency_ms: Optional[int] = Field(None, description="Estimated latency")


class Scorer(BaseEntity):
    """Scorer definition."""

    scorer_id: str = Field(..., description="Unique scorer identifier")
    name: str = Field(..., description="Human-readable scorer name")
    description: Optional[str] = Field(None, description="Scorer description")
    category: str = Field(..., description="Scorer category (e.g., 'quality', 'safety')")
    is_custom: bool = Field(False, description="Whether this is a custom scorer")
    organization_id: Optional[str] = Field(None, description="Organization ID (for custom)")
    metadata: ScorerMetadata = Field(default_factory=ScorerMetadata, description="Scorer metadata")
    config_schema: Optional[Dict[str, Any]] = Field(None, description="Configuration schema")
    tags: List[str] = Field(default_factory=list, description="Scorer tags")
