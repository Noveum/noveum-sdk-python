"""
Async evaluation example.

This example demonstrates how to:
1. Use AsyncNoveumClient for async/await
2. Load datasets asynchronously
3. Run parallel evaluations
4. Handle async errors
"""

import asyncio

from noveum import AsyncNoveumClient, ScorerConfig


async def my_async_agent(prompt: str) -> str:
    """Simulate an async agent."""
    await asyncio.sleep(0.1)  # Simulate processing
    return f"Async response to: {prompt}"


async def main():
    """Run async evaluation example."""
    # Use async context manager
    async with AsyncNoveumClient() as client:
        try:
            # Load dataset items asynchronously
            print("Loading dataset items...")
            items = []
            async for item in client.datasets.items("test-dataset"):
                items.append(item)
                print(f"  Loaded: {item.item_id}")

            if not items:
                print("No items in dataset")
                return

            # Prepare evaluation tasks
            scorers = [ScorerConfig(scorer_id="factuality_scorer")]
            tasks = []

            print(f"\nRunning {len(items)} evaluations in parallel...")
            for item in items:
                # Create evaluation task
                output = await my_async_agent(item.input_text)
                task = client.evals.score(
                    dataset_item=item,
                    agent_output=output,
                    scorers=scorers,
                )
                tasks.append(task)

            # Run all evaluations concurrently
            results = await asyncio.gather(*tasks)

            # Display results
            print(f"\nResults:")
            for result in results:
                print(f"  Item {result.item_id}: {result.overall_score}/10")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
