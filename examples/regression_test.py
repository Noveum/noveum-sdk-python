"""
Regression test example using pytest.

This example demonstrates how to:
1. Create a pytest test that uses the Noveum SDK
2. Load a dataset for regression testing
3. Run evaluations on multiple items
4. Aggregate results and assert quality metrics
"""

import pytest

from noveum import NoveumClient, ScorerConfig, EvalAggregator


@pytest.fixture
def noveum_client():
    """Fixture to provide Noveum client."""
    return NoveumClient()


def my_agent(prompt: str) -> str:
    """Dummy agent for testing."""
    # Replace with your actual agent/model
    return f"Response to: {prompt}"


def test_agent_quality_regression(noveum_client):
    """
    Test that agent maintains quality on regression test set.
    
    This test:
    1. Loads regression test dataset
    2. Runs agent on all items
    3. Evaluates outputs using scorers
    4. Asserts minimum quality metrics
    """
    # Load regression test dataset
    try:
        items = list(noveum_client.datasets.items("regression-tests"))
    except Exception as e:
        pytest.skip(f"Could not load regression test dataset: {e}")

    if not items:
        pytest.skip("No items in regression test dataset")

    # Define scorers
    scorers = [
        ScorerConfig(scorer_id="factuality_scorer"),
    ]

    # Run evaluations
    results = []
    for item in items:
        agent_output = my_agent(item.input_text)
        result = noveum_client.evals.score(
            dataset_item=item,
            agent_output=agent_output,
            scorers=scorers,
        )
        results.append(result)

    # Aggregate results
    aggregator = EvalAggregator(results)

    # Assert quality metrics
    print(f"\nRegression Test Results:")
    print(f"  Total Items: {aggregator.total_items}")
    print(f"  Passed: {aggregator.passed_items}")
    print(f"  Passing Rate: {aggregator.passing_rate:.1f}%")
    print(f"  Average Score: {aggregator.average_score:.1f}")

    # These assertions will cause the test to fail if quality drops
    aggregator.assert_passing_rate(80.0)  # At least 80% passing
    aggregator.assert_average_score(7.0)  # Average score >= 7.0


def test_agent_on_specific_scorer(noveum_client):
    """Test agent performance on a specific scorer."""
    try:
        items = list(noveum_client.datasets.items("regression-tests"))
    except Exception as e:
        pytest.skip(f"Could not load regression test dataset: {e}")

    if not items:
        pytest.skip("No items in regression test dataset")

    scorers = [ScorerConfig(scorer_id="factuality_scorer")]

    results = []
    for item in items[:5]:  # Test on first 5 items
        agent_output = my_agent(item.input_text)
        result = noveum_client.evals.score(item, agent_output, scorers)
        results.append(result)

    aggregator = EvalAggregator(results)

    # Get stats for specific scorer
    stats = aggregator.get_scorer_stats("factuality_scorer")
    print(f"\nFactuality Scorer Stats:")
    print(f"  Average Score: {stats.get('average_score', 0):.1f}")
    print(f"  Min Score: {stats.get('min_score', 0):.1f}")
    print(f"  Max Score: {stats.get('max_score', 0):.1f}")

    # Assert minimum average score
    assert stats.get("average_score", 0) >= 6.0, "Average score too low"


if __name__ == "__main__":
    # Run with: pytest examples/regression_test.py -v
    pytest.main([__file__, "-v"])
