"""
Basic evaluation example.

This example demonstrates how to:
1. Initialize the Noveum client
2. Load a dataset item
3. Run an agent/model
4. Evaluate the output
5. Display results
"""

from noveum import NoveumClient, ScorerConfig


def main():
    """Run basic evaluation example."""
    # Initialize client (uses NOVEUM_API_KEY environment variable)
    client = NoveumClient()

    # Define a simple agent for testing
    def simple_agent(prompt: str) -> str:
        """Simple agent that responds based on keywords."""
        if "hello" in prompt.lower():
            return "Hello! How can I assist you?"
        elif "goodbye" in prompt.lower():
            return "Goodbye! Have a great day!"
        else:
            return "I'm not sure how to respond to that."

    # Try to load a dataset item
    try:
        item = client.datasets.get_item("test-dataset", "item-1")
    except Exception as e:
        print(f"Note: Could not load dataset item. Error: {e}")
        print("To use this example, create a dataset with slug 'test-dataset'")
        print("and an item with ID 'item-1'.")
        return

    # Run the agent with the item's input
    print(f"Input: {item.input_text}")
    agent_output = simple_agent(item.input_text)
    print(f"Agent Output: {agent_output}")

    # Evaluate the output
    result = client.evals.score(
        dataset_item=item,
        agent_output=agent_output,
        scorers=[ScorerConfig(scorer_id="factuality_scorer")],
    )

    # Display results
    print(f"\nEvaluation Results:")
    print(f"  Overall Score: {result.overall_score}/10")
    print(f"  Passed: {result.overall_passed}")

    for score in result.scores:
        print(f"\n  Scorer: {score.scorer_name}")
        print(f"    Score: {score.score}")
        print(f"    Reasoning: {score.reasoning}")


if __name__ == "__main__":
    main()
