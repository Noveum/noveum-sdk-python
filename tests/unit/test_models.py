"""Unit tests for Pydantic models."""

from datetime import datetime

import pytest

from noveum import (
    Dataset,
    DatasetItem,
    DatasetItemType,
    EvalResult,
    ScorerConfig,
    ScorerResult,
    Trace,
    TraceStatus,
)


@pytest.mark.unit
class TestDatasetItem:
    """Tests for DatasetItem model."""

    def test_dataset_item_creation(self):
        """Test creating a DatasetItem."""
        item = DatasetItem(
            id="item-1",
            created_at=datetime.now(),
            item_id="item-1",
            dataset_slug="test-dataset",
            input_text="Test input",
        )
        assert item.item_id == "item-1"
        assert item.dataset_slug == "test-dataset"
        assert item.input_text == "Test input"

    def test_dataset_item_with_optional_fields(self):
        """Test DatasetItem with optional fields."""
        item = DatasetItem(
            id="item-1",
            created_at=datetime.now(),
            item_id="item-1",
            dataset_slug="test-dataset",
            input_text="Test input",
            expected_output="Expected output",
            metadata={"source": "test"},
        )
        assert item.expected_output == "Expected output"
        assert item.metadata == {"source": "test"}

    def test_dataset_item_type_default(self):
        """Test DatasetItem type defaults to CUSTOM."""
        item = DatasetItem(
            id="item-1",
            created_at=datetime.now(),
            item_id="item-1",
            dataset_slug="test-dataset",
            input_text="Test input",
        )
        assert item.item_type == DatasetItemType.CUSTOM

    def test_dataset_item_serialization(self):
        """Test DatasetItem serialization to dict."""
        item = DatasetItem(
            id="item-1",
            created_at=datetime.now(),
            item_id="item-1",
            dataset_slug="test-dataset",
            input_text="Test input",
        )
        data = item.model_dump()
        assert data["item_id"] == "item-1"
        assert data["dataset_slug"] == "test-dataset"


@pytest.mark.unit
class TestScorerConfig:
    """Tests for ScorerConfig model."""

    def test_scorer_config_creation(self):
        """Test creating a ScorerConfig."""
        config = ScorerConfig(scorer_id="factuality_scorer")
        assert config.scorer_id == "factuality_scorer"

    def test_scorer_config_with_custom_config(self):
        """Test ScorerConfig with custom configuration."""
        custom_config = {"model": "gpt-4", "temperature": 0.0}
        config = ScorerConfig(scorer_id="test_scorer", config=custom_config)
        assert config.config == custom_config

    def test_scorer_config_serialization(self):
        """Test ScorerConfig serialization."""
        config = ScorerConfig(scorer_id="test_scorer")
        data = config.model_dump()
        assert data["scorer_id"] == "test_scorer"


@pytest.mark.unit
class TestScorerResult:
    """Tests for ScorerResult model."""

    def test_scorer_result_creation(self):
        """Test creating a ScorerResult."""
        result = ScorerResult(
            scorer_id="factuality_scorer",
            scorer_name="Factuality Scorer",
            score=8.5,
            passed=True,
            reasoning="The output is factually correct.",
        )
        assert result.scorer_id == "factuality_scorer"
        assert result.score == 8.5
        assert result.passed is True

    def test_scorer_result_with_metadata(self):
        """Test ScorerResult with metadata."""
        result = ScorerResult(
            scorer_id="test_scorer",
            scorer_name="Test Scorer",
            score=7.0,
            passed=False,
            metadata={"detail": "test"},
        )
        assert result.metadata == {"detail": "test"}


@pytest.mark.unit
class TestEvalResult:
    """Tests for EvalResult model."""

    def test_eval_result_creation(self):
        """Test creating an EvalResult."""
        scores = [
            ScorerResult(
                scorer_id="test_scorer",
                scorer_name="Test Scorer",
                score=8.0,
                passed=True,
            )
        ]
        result = EvalResult(
            id="result-1",
            created_at=datetime.now(),
            item_id="item-1",
            dataset_slug="test-dataset",
            agent_output="Test output",
            execution_time_ms=100,
            scores=scores,
            overall_score=8.0,
            overall_passed=True,
        )
        assert result.item_id == "item-1"
        assert result.overall_score == 8.0
        assert len(result.scores) == 1

    def test_eval_result_with_multiple_scorers(self):
        """Test EvalResult with multiple scorers."""
        scores = [
            ScorerResult(
                scorer_id="scorer1",
                scorer_name="Scorer 1",
                score=8.0,
                passed=True,
            ),
            ScorerResult(
                scorer_id="scorer2",
                scorer_name="Scorer 2",
                score=7.0,
                passed=True,
            ),
        ]
        result = EvalResult(
            id="result-1",
            created_at=datetime.now(),
            item_id="item-1",
            dataset_slug="test-dataset",
            agent_output="Test output",
            execution_time_ms=100,
            scores=scores,
            overall_score=7.5,
            overall_passed=True,
        )
        assert len(result.scores) == 2
        assert result.overall_score == 7.5


@pytest.mark.unit
class TestTrace:
    """Tests for Trace model."""

    def test_trace_creation(self):
        """Test creating a Trace."""
        trace = Trace(
            id="trace-1",
            created_at=datetime.now(),
            trace_id="trace-1",
            name="Test Trace",
            status=TraceStatus.OK,
            duration_ms=100,
            project="test-project",
            environment="test",
            start_time=datetime.now().isoformat(),
            end_time=datetime.now().isoformat(),
            span_count=0,
            error_count=0,
            sdk={"name": "test", "version": "1.0"},
        )
        assert trace.trace_id == "trace-1"
        assert trace.status == TraceStatus.OK

    def test_trace_with_spans(self):
        """Test Trace with spans."""
        trace = Trace(
            id="trace-1",
            created_at=datetime.now(),
            trace_id="trace-1",
            name="Test Trace",
            status=TraceStatus.OK,
            duration_ms=100,
            project="test-project",
            environment="test",
            start_time=datetime.now().isoformat(),
            end_time=datetime.now().isoformat(),
            span_count=0,
            error_count=0,
            sdk={"name": "test", "version": "1.0"},
            spans=[],
        )
        assert isinstance(trace.spans, list)


@pytest.mark.unit
class TestDataset:
    """Tests for Dataset model."""

    def test_dataset_creation(self):
        """Test creating a Dataset."""
        dataset = Dataset(
            id="dataset-1",
            created_at=datetime.now(),
            slug="test-dataset",
            name="Test Dataset",
            item_count=10,
            item_type=DatasetItemType.CUSTOM,
            organization_id="org-1",
        )
        assert dataset.slug == "test-dataset"
        assert dataset.name == "Test Dataset"
        assert dataset.item_count == 10


@pytest.mark.unit
class TestModelValidation:
    """Tests for model validation."""

    def test_dataset_item_requires_item_id(self):
        """Test that DatasetItem requires item_id."""
        with pytest.raises(ValueError):
            DatasetItem(
                id="item-1",
                created_at=datetime.now(),
                dataset_slug="test-dataset",
                input_text="Test input",
            )

    def test_scorer_config_requires_scorer_id(self):
        """Test that ScorerConfig requires scorer_id."""
        with pytest.raises(ValueError):
            ScorerConfig()

    def test_eval_result_requires_item_id(self):
        """Test that EvalResult requires item_id."""
        with pytest.raises(ValueError):
            EvalResult(scores=[], overall_score=0.0, overall_passed=False)

    def test_scorer_result_requires_scorer_id(self):
        """Test that ScorerResult requires scorer_id."""
        with pytest.raises(ValueError):
            ScorerResult(
                scorer_name="Test",
                score=8.0,
                passed=True,
            )
