"""Unit tests for SDK resources."""

from unittest.mock import MagicMock, patch

import pytest

from noveum import NoveumClient, ScorerConfig
from noveum.resources.datasets import DatasetsResource
from noveum.resources.evals import EvalsResource
from noveum.resources.scorers import ScorersResource
from noveum.resources.traces import TracesResource


@pytest.mark.unit
class TestDatasetsResource:
    """Tests for DatasetsResource."""

    def test_datasets_resource_initialization(self, noveum_client):
        """Test DatasetsResource initialization."""
        assert isinstance(noveum_client.datasets, DatasetsResource)

    def test_datasets_list_method_exists(self, noveum_client):
        """Test that list method exists."""
        assert hasattr(noveum_client.datasets, "list")
        assert callable(noveum_client.datasets.list)

    def test_datasets_get_method_exists(self, noveum_client):
        """Test that get method exists."""
        assert hasattr(noveum_client.datasets, "get")
        assert callable(noveum_client.datasets.get)

    def test_datasets_items_method_exists(self, noveum_client):
        """Test that items method exists."""
        assert hasattr(noveum_client.datasets, "items")
        assert callable(noveum_client.datasets.items)

    def test_datasets_get_item_method_exists(self, noveum_client):
        """Test that get_item method exists."""
        assert hasattr(noveum_client.datasets, "get_item")
        assert callable(noveum_client.datasets.get_item)


@pytest.mark.unit
class TestEvalsResource:
    """Tests for EvalsResource."""

    def test_evals_resource_initialization(self, noveum_client):
        """Test EvalsResource initialization."""
        assert isinstance(noveum_client.evals, EvalsResource)

    def test_evals_score_method_exists(self, noveum_client):
        """Test that score method exists."""
        assert hasattr(noveum_client.evals, "score")
        assert callable(noveum_client.evals.score)

    def test_evals_score_batch_method_exists(self, noveum_client):
        """Test that score_batch method exists."""
        assert hasattr(noveum_client.evals, "score_batch")
        assert callable(noveum_client.evals.score_batch)

    def test_evals_score_with_retries_method_exists(self, noveum_client):
        """Test that score_with_retries method exists."""
        assert hasattr(noveum_client.evals, "score_with_retries")
        assert callable(noveum_client.evals.score_with_retries)

    def test_evals_aggregate_results_method_exists(self, noveum_client):
        """Test that aggregate_results method exists."""
        assert hasattr(noveum_client.evals, "aggregate_results")
        assert callable(noveum_client.evals.aggregate_results)

    def test_aggregate_results_with_empty_list(self, noveum_client):
        """Test aggregate_results with empty list."""
        result = noveum_client.evals.aggregate_results([])
        assert result.total_items == 0
        assert result.passed_items == 0
        assert result.passing_rate == 0.0


@pytest.mark.unit
class TestScorersResource:
    """Tests for ScorersResource."""

    def test_scorers_resource_initialization(self, noveum_client):
        """Test ScorersResource initialization."""
        assert isinstance(noveum_client.scorers, ScorersResource)

    def test_scorers_list_method_exists(self, noveum_client):
        """Test that list method exists."""
        assert hasattr(noveum_client.scorers, "list")
        assert callable(noveum_client.scorers.list)

    def test_scorers_get_method_exists(self, noveum_client):
        """Test that get method exists."""
        assert hasattr(noveum_client.scorers, "get")
        assert callable(noveum_client.scorers.get)

    def test_scorers_get_results_method_exists(self, noveum_client):
        """Test that get_results method exists."""
        assert hasattr(noveum_client.scorers, "get_results")
        assert callable(noveum_client.scorers.get_results)


@pytest.mark.unit
class TestTracesResource:
    """Tests for TracesResource."""

    def test_traces_resource_initialization(self, noveum_client):
        """Test TracesResource initialization."""
        assert isinstance(noveum_client.traces, TracesResource)

    def test_traces_submit_method_exists(self, noveum_client):
        """Test that submit method exists."""
        assert hasattr(noveum_client.traces, "submit")
        assert callable(noveum_client.traces.submit)

    def test_traces_list_method_exists(self, noveum_client):
        """Test that list method exists."""
        assert hasattr(noveum_client.traces, "list")
        assert callable(noveum_client.traces.list)

    def test_traces_get_method_exists(self, noveum_client):
        """Test that get method exists."""
        assert hasattr(noveum_client.traces, "get")
        assert callable(noveum_client.traces.get)


@pytest.mark.unit
class TestResourceMethods:
    """Tests for resource method signatures."""

    def test_datasets_items_returns_iterator(self, noveum_client):
        """Test that datasets.items returns an iterator."""
        with patch.object(
            noveum_client._http_client, "get", return_value={"data": [], "pagination": {"total": 0}}
        ):
            items_iter = noveum_client.datasets.items("test-dataset")
            # Should be an iterator
            assert hasattr(items_iter, "__iter__")

    def test_scorers_list_returns_iterator(self, noveum_client):
        """Test that scorers.list returns an iterator."""
        with patch.object(
            noveum_client._http_client, "get", return_value={"data": [], "pagination": {"total": 0}}
        ):
            scorers_iter = noveum_client.scorers.list()
            # Should be an iterator
            assert hasattr(scorers_iter, "__iter__")

    def test_traces_list_returns_iterator(self, noveum_client):
        """Test that traces.list returns an iterator."""
        with patch.object(
            noveum_client._http_client, "get", return_value={"data": [], "pagination": {"total": 0}}
        ):
            traces_iter = noveum_client.traces.list()
            # Should be an iterator
            assert hasattr(traces_iter, "__iter__")
