"""Evaluation API data models."""

from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from .datasets import DatasetItem


class ScorerConfig(BaseModel):
    """Configuration for a scorer during evaluation."""

    scorer_id: str = Field(..., description="Scorer identifier")
    config: Optional[Dict[str, Any]] = Field(None, description="Scorer-specific configuration")
    weight: float = Field(default=1.0, description="Weight for aggregation (0-1)")

    class Config:
        """Pydantic config."""

        json_schema_extra = {
            "example": {
                "scorer_id": "factuality_scorer",
                "config": {"model": "gpt-4", "temperature": 0.0},
                "weight": 1.0,
            }
        }


class EvalRequest(BaseModel):
    """Request to evaluate an agent output."""

    dataset_item: DatasetItem = Field(..., description="Dataset item to evaluate")
    agent_output: str = Field(..., description="Agent's output to evaluate")
    scorers: List[ScorerConfig] = Field(..., description="Scorers to apply")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Custom metadata")

    class Config:
        """Pydantic config."""

        json_schema_extra = {
            "example": {
                "dataset_item": {
                    "item_id": "uuid",
                    "dataset_slug": "test-set",
                    "input_text": "What is AI?",
                    "expected_output": "Artificial Intelligence...",
                },
                "agent_output": "AI stands for Artificial Intelligence...",
                "scorers": [
                    {
                        "scorer_id": "factuality_scorer",
                        "config": {"model": "gpt-4"},
                    }
                ],
            }
        }


class ScorerResult(BaseModel):
    """Result from a single scorer."""

    scorer_id: str = Field(..., description="Scorer identifier")
    scorer_name: str = Field(..., description="Human-readable scorer name")
    score: float = Field(..., description="Numeric score (typically 0-10)")
    passed: bool = Field(..., description="Whether item passed this scorer")
    reasoning: Optional[str] = Field(None, description="Reasoning for the score")
    execution_time_ms: Optional[int] = Field(None, description="Scorer execution time")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Scorer-specific metadata")

    class Config:
        """Pydantic config."""

        json_schema_extra = {
            "example": {
                "scorer_id": "factuality_scorer",
                "scorer_name": "Factuality",
                "score": 8.5,
                "passed": True,
                "reasoning": "The response is factually accurate...",
                "execution_time_ms": 1234,
            }
        }


class EvalResult(BaseModel):
    """Complete evaluation result for an item."""

    item_id: str = Field(..., description="Dataset item ID")
    dataset_slug: str = Field(..., description="Dataset slug")
    agent_output: str = Field(..., description="Agent output that was evaluated")
    scores: List[ScorerResult] = Field(..., description="Results from all scorers")
    overall_score: float = Field(..., description="Aggregated score")
    overall_passed: bool = Field(..., description="Whether item passed overall")
    execution_time_ms: int = Field(..., description="Total execution time")
    created_at: datetime = Field(..., description="Result creation timestamp")

    class Config:
        """Pydantic config."""

        json_encoders = {
            datetime: lambda v: v.isoformat() if v else None,
        }

    def get_score(self, scorer_id: str) -> Optional[float]:
        """Get score for a specific scorer."""
        for score in self.scores:
            if score.scorer_id == scorer_id:
                return score.score
        return None

    def get_reasoning(self, scorer_id: str) -> Optional[str]:
        """Get reasoning for a specific scorer."""
        for score in self.scores:
            if score.scorer_id == scorer_id:
                return score.reasoning
        return None

    def get_passed(self, scorer_id: str) -> Optional[bool]:
        """Get passed status for a specific scorer."""
        for score in self.scores:
            if score.scorer_id == scorer_id:
                return score.passed
        return None


class TestResult(BaseModel):
    """Aggregated results for test assertions."""

    total_items: int = Field(..., description="Total items evaluated")
    passed_items: int = Field(..., description="Items that passed")
    failed_items: int = Field(..., description="Items that failed")
    passing_rate: float = Field(..., description="Passing rate (0-1)")
    avg_score: float = Field(..., description="Average score across all items")
    results_by_scorer: Dict[str, List[float]] = Field(
        ..., description="Scores grouped by scorer"
    )
    failed_items_detail: List[EvalResult] = Field(
        default_factory=list, description="Details of failed items"
    )

    class Config:
        """Pydantic config."""

        json_encoders = {
            datetime: lambda v: v.isoformat() if v else None,
        }

    def assert_passing_rate(self, threshold: float) -> None:
        """
        Assert minimum passing rate.

        Args:
            threshold: Minimum passing rate (0-1)

        Raises:
            AssertionError: If passing rate is below threshold
        """
        if self.passing_rate < threshold:
            raise AssertionError(
                f"Passing rate {self.passing_rate:.1%} below threshold {threshold:.1%} "
                f"({self.passed_items}/{self.total_items} items passed)"
            )

    def assert_scorer_score(self, scorer_id: str, threshold: float) -> None:
        """
        Assert minimum score for specific scorer.

        Args:
            scorer_id: Scorer identifier
            threshold: Minimum average score

        Raises:
            ValueError: If scorer not found
            AssertionError: If average score is below threshold
        """
        if scorer_id not in self.results_by_scorer:
            raise ValueError(f"Scorer {scorer_id} not found in results")

        scores = self.results_by_scorer[scorer_id]
        avg = sum(scores) / len(scores) if scores else 0

        if avg < threshold:
            raise AssertionError(
                f"Scorer {scorer_id} average {avg:.1f} below threshold {threshold:.1f}"
            )

    def get_scorer_stats(self, scorer_id: str) -> Dict[str, float]:
        """
        Get statistics for a specific scorer.

        Args:
            scorer_id: Scorer identifier

        Returns:
            Dictionary with min, max, avg, and count

        Raises:
            ValueError: If scorer not found
        """
        if scorer_id not in self.results_by_scorer:
            raise ValueError(f"Scorer {scorer_id} not found in results")

        scores = self.results_by_scorer[scorer_id]
        if not scores:
            return {"min": 0, "max": 0, "avg": 0, "count": 0}

        return {
            "min": min(scores),
            "max": max(scores),
            "avg": sum(scores) / len(scores),
            "count": len(scores),
        }
