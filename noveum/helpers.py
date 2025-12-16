"""Helper utilities for Noveum SDK.

Provides convenience functions for common operations.
"""

from typing import List, Optional, Tuple

from .models.datasets import DatasetItem
from .models.evals import EvalResult, ScorerConfig, ScorerResult


class EvalAggregator:
    """Aggregates evaluation results for analysis."""

    def __init__(self, results: List[EvalResult]):
        """
        Initialize aggregator with results.

        Args:
            results: List of evaluation results
        """
        self.results = results

    @property
    def total_items(self) -> int:
        """Get total number of items evaluated."""
        return len(self.results)

    @property
    def passed_items(self) -> int:
        """Get number of items that passed."""
        return sum(1 for r in self.results if r.overall_passed)

    @property
    def failed_items(self) -> int:
        """Get number of items that failed."""
        return self.total_items - self.passed_items

    @property
    def passing_rate(self) -> float:
        """Get passing rate as percentage (0-100)."""
        if self.total_items == 0:
            return 0.0
        return (self.passed_items / self.total_items) * 100

    @property
    def average_score(self) -> float:
        """Get average overall score."""
        if self.total_items == 0:
            return 0.0
        return sum(r.overall_score for r in self.results) / self.total_items

    @property
    def min_score(self) -> float:
        """Get minimum score."""
        if not self.results:
            return 0.0
        return min(r.overall_score for r in self.results)

    @property
    def max_score(self) -> float:
        """Get maximum score."""
        if not self.results:
            return 0.0
        return max(r.overall_score for r in self.results)

    def get_failed_items(self) -> List[EvalResult]:
        """Get all failed items."""
        return [r for r in self.results if not r.overall_passed]

    def get_passed_items(self) -> List[EvalResult]:
        """Get all passed items."""
        return [r for r in self.results if r.overall_passed]

    def get_by_scorer(self, scorer_id: str) -> List[ScorerResult]:
        """Get all results for a specific scorer."""
        results = []
        for eval_result in self.results:
            for score in eval_result.scores:
                if score.scorer_id == scorer_id:
                    results.append(score)
        return results

    def get_scorer_stats(self, scorer_id: str) -> dict:
        """Get statistics for a specific scorer."""
        scores = self.get_by_scorer(scorer_id)
        if not scores:
            return {}

        return {
            "scorer_id": scorer_id,
            "total": len(scores),
            "passed": sum(1 for s in scores if s.passed),
            "failed": sum(1 for s in scores if not s.passed),
            "passing_rate": (sum(1 for s in scores if s.passed) / len(scores)) * 100,
            "average_score": sum(s.score for s in scores) / len(scores),
            "min_score": min(s.score for s in scores),
            "max_score": max(s.score for s in scores),
        }

    def summary(self) -> dict:
        """Get summary statistics."""
        return {
            "total_items": self.total_items,
            "passed_items": self.passed_items,
            "failed_items": self.failed_items,
            "passing_rate": self.passing_rate,
            "average_score": self.average_score,
            "min_score": self.min_score,
            "max_score": self.max_score,
        }

    def assert_passing_rate(self, threshold: float) -> None:
        """
        Assert that passing rate meets threshold.

        Args:
            threshold: Minimum passing rate (0-100)

        Raises:
            AssertionError: If passing rate is below threshold
        """
        if self.passing_rate < threshold:
            raise AssertionError(
                f"Passing rate {self.passing_rate:.1f}% is below threshold {threshold}%"
            )

    def assert_average_score(self, threshold: float) -> None:
        """
        Assert that average score meets threshold.

        Args:
            threshold: Minimum average score

        Raises:
            AssertionError: If average score is below threshold
        """
        if self.average_score < threshold:
            raise AssertionError(
                f"Average score {self.average_score:.1f} is below threshold {threshold}"
            )

    def __repr__(self) -> str:
        """Return string representation."""
        return (
            f"EvalAggregator(total={self.total_items}, "
            f"passed={self.passed_items}, "
            f"rate={self.passing_rate:.1f}%)"
        )


class ScorerConfigBuilder:
    """Builder for creating scorer configurations."""

    def __init__(self, scorer_id: str):
        """
        Initialize builder.

        Args:
            scorer_id: ID of the scorer
        """
        self.scorer_id = scorer_id
        self.config: dict = {}

    def with_config(self, key: str, value) -> "ScorerConfigBuilder":
        """
        Add configuration parameter.

        Args:
            key: Configuration key
            value: Configuration value

        Returns:
            Self for chaining
        """
        self.config[key] = value
        return self

    def with_model(self, model: str) -> "ScorerConfigBuilder":
        """
        Set model parameter.

        Args:
            model: Model name

        Returns:
            Self for chaining
        """
        self.config["model"] = model
        return self

    def with_temperature(self, temperature: float) -> "ScorerConfigBuilder":
        """
        Set temperature parameter.

        Args:
            temperature: Temperature value (0-1)

        Returns:
            Self for chaining
        """
        self.config["temperature"] = temperature
        return self

    def build(self) -> ScorerConfig:
        """
        Build scorer configuration.

        Returns:
            ScorerConfig instance
        """
        return ScorerConfig(
            scorer_id=self.scorer_id,
            config=self.config if self.config else None,
        )


class DatasetItemBuilder:
    """Builder for creating dataset items."""

    def __init__(self, item_id: str, dataset_slug: str, input_text: str):
        """
        Initialize builder.

        Args:
            item_id: Item ID
            dataset_slug: Dataset slug
            input_text: Input text
        """
        self.item_id = item_id
        self.dataset_slug = dataset_slug
        self.input_text = input_text
        self.expected_output: Optional[str] = None
        self.metadata: dict = {}

    def with_expected_output(self, output: str) -> "DatasetItemBuilder":
        """
        Set expected output.

        Args:
            output: Expected output text

        Returns:
            Self for chaining
        """
        self.expected_output = output
        return self

    def with_metadata(self, key: str, value) -> "DatasetItemBuilder":
        """
        Add metadata.

        Args:
            key: Metadata key
            value: Metadata value

        Returns:
            Self for chaining
        """
        self.metadata[key] = value
        return self

    def build(self) -> DatasetItem:
        """
        Build dataset item.

        Returns:
            DatasetItem instance
        """
        from datetime import datetime

        return DatasetItem(
            id=self.item_id,
            created_at=datetime.now(),
            item_id=self.item_id,
            dataset_slug=self.dataset_slug,
            input_text=self.input_text,
            expected_output=self.expected_output,
            metadata=self.metadata if self.metadata else None,
        )


def create_scorer_config(scorer_id: str, **config) -> ScorerConfig:
    """
    Create a scorer configuration.

    Args:
        scorer_id: ID of the scorer
        **config: Additional configuration parameters

    Returns:
        ScorerConfig instance
    """
    return ScorerConfig(
        scorer_id=scorer_id,
        config=config if config else None,
    )


def create_scorer_configs(scorer_ids: List[str]) -> List[ScorerConfig]:
    """
    Create multiple scorer configurations.

    Args:
        scorer_ids: List of scorer IDs

    Returns:
        List of ScorerConfig instances
    """
    return [ScorerConfig(scorer_id=sid) for sid in scorer_ids]


def batch_results(
    results: List[EvalResult], batch_size: int = 10
) -> List[List[EvalResult]]:
    """
    Batch evaluation results.

    Args:
        results: List of evaluation results
        batch_size: Size of each batch

    Returns:
        List of batches
    """
    return [results[i : i + batch_size] for i in range(0, len(results), batch_size)]


def filter_by_score(
    results: List[EvalResult], min_score: float = 0.0, max_score: float = 10.0
) -> List[EvalResult]:
    """
    Filter results by score range.

    Args:
        results: List of evaluation results
        min_score: Minimum score
        max_score: Maximum score

    Returns:
        Filtered results
    """
    return [
        r
        for r in results
        if min_score <= r.overall_score <= max_score
    ]


def filter_by_status(
    results: List[EvalResult], passed: bool = True
) -> List[EvalResult]:
    """
    Filter results by pass/fail status.

    Args:
        results: List of evaluation results
        passed: Filter for passed (True) or failed (False)

    Returns:
        Filtered results
    """
    return [r for r in results if r.overall_passed == passed]
