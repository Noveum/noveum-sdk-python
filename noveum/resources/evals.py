"""Evals resource for evaluation API."""

from typing import Any, AsyncIterator, Dict, Iterator, List, Optional

from ..http_client import AsyncHTTPClient, HTTPClient
from ..models.datasets import DatasetItem
from ..models.evals import EvalRequest, EvalResult, ScorerConfig, TestResult
from ..pagination import AsyncPaginatedIterator, PaginatedIterator
from .base import AsyncBaseResource, BaseResource


class EvalsResource(BaseResource):
    """
    Synchronous evals resource for evaluation operations.

    This is the primary interface for CI/CD test integration.
    """

    def score(
        self,
        dataset_item: DatasetItem,
        agent_output: str,
        scorers: List[ScorerConfig],
        metadata: Optional[Dict[str, Any]] = None,
    ) -> EvalResult:
        """
        Score agent output against a dataset item.

        This is the main method for test integration. Submits an agent's output
        for evaluation using specified scorers.

        Args:
            dataset_item: Dataset item to evaluate against
            agent_output: Agent's output to evaluate
            scorers: List of scorers to apply
            metadata: Optional custom metadata

        Returns:
            EvalResult with scores and reasoning

        Raises:
            NoveumAPIError: If API request fails
            NoveumValidationError: If input validation fails

        Example:
            >>> client = NoveumClient()
            >>> item = client.datasets.get_item("item-123")
            >>> result = client.evals.score(
            ...     dataset_item=item,
            ...     agent_output="My agent's response",
            ...     scorers=[ScorerConfig(scorer_id="factuality_scorer")]
            ... )
            >>> print(f"Score: {result.overall_score}/10")
            >>> print(f"Reasoning: {result.scores[0].reasoning}")
        """
        # Build request
        request = EvalRequest(
            dataset_item=dataset_item,
            agent_output=agent_output,
            scorers=scorers,
            metadata=metadata,
        )

        # Make API call
        url = self._build_url("/evals/score")
        response = self.http_client.post(url, json=request.model_dump())

        # Parse response
        return EvalResult(**response)

    def score_batch(
        self,
        items: List[tuple[DatasetItem, str]],
        scorers: List[ScorerConfig],
        parallel: int = 5,
    ) -> Iterator[EvalResult]:
        """
        Batch evaluate multiple items with parallel scoring.

        Yields results as they complete, enabling streaming processing.

        Args:
            items: List of (dataset_item, agent_output) tuples
            scorers: List of scorers to apply
            parallel: Number of concurrent evaluations

        Yields:
            EvalResult for each item as it completes

        Raises:
            NoveumAPIError: If API request fails

        Example:
            >>> items = [(item1, output1), (item2, output2)]
            >>> for result in client.evals.score_batch(items, scorers):
            ...     print(f"Item {result.item_id}: {result.overall_score}")
        """
        # Prepare batch request
        batch_items = [
            {
                "dataset_item": item.model_dump(),
                "agent_output": output,
            }
            for item, output in items
        ]

        url = self._build_url("/evals/score-batch")
        response = self.http_client.post(
            url,
            json={
                "items": batch_items,
                "scorers": [s.model_dump() for s in scorers],
                "parallel": parallel,
            },
        )

        # Parse streaming response
        if isinstance(response, list):
            for result_data in response:
                yield EvalResult(**result_data)
        else:
            yield EvalResult(**response)

    def score_with_retries(
        self,
        dataset_item: DatasetItem,
        agent_output: str,
        scorers: List[ScorerConfig],
        max_retries: int = 3,
        backoff_factor: float = 2.0,
    ) -> EvalResult:
        """
        Score with automatic retry on transient failures.

        Args:
            dataset_item: Dataset item to evaluate against
            agent_output: Agent's output to evaluate
            scorers: List of scorers to apply
            max_retries: Maximum number of retries
            backoff_factor: Exponential backoff factor

        Returns:
            EvalResult with scores and reasoning

        Raises:
            NoveumAPIError: If all retries fail

        Example:
            >>> result = client.evals.score_with_retries(
            ...     dataset_item=item,
            ...     agent_output=output,
            ...     scorers=scorers,
            ...     max_retries=5
            ... )
        """
        import time

        last_error = None
        for attempt in range(max_retries + 1):
            try:
                return self.score(dataset_item, agent_output, scorers)
            except Exception as e:
                last_error = e
                if attempt < max_retries:
                    wait_time = backoff_factor ** attempt
                    time.sleep(wait_time)

        raise last_error or Exception("Failed to score after retries")

    def aggregate_results(self, results: List[EvalResult]) -> TestResult:
        """
        Aggregate multiple evaluation results for test assertions.

        Args:
            results: List of EvalResult objects

        Returns:
            TestResult with aggregated statistics

        Example:
            >>> results = [client.evals.score(...) for item in items]
            >>> test_result = client.evals.aggregate_results(results)
            >>> test_result.assert_passing_rate(0.8)
        """
        if not results:
            return TestResult(
                total_items=0,
                passed_items=0,
                failed_items=0,
                passing_rate=0.0,
                avg_score=0.0,
                results_by_scorer={},
            )

        total = len(results)
        passed = sum(1 for r in results if r.overall_passed)
        failed = total - passed
        avg_score = sum(r.overall_score for r in results) / total if total > 0 else 0

        # Group scores by scorer
        results_by_scorer: Dict[str, List[float]] = {}
        for result in results:
            for score in result.scores:
                if score.scorer_id not in results_by_scorer:
                    results_by_scorer[score.scorer_id] = []
                results_by_scorer[score.scorer_id].append(score.score)

        failed_items = [r for r in results if not r.overall_passed]

        return TestResult(
            total_items=total,
            passed_items=passed,
            failed_items=failed,
            passing_rate=passed / total if total > 0 else 0,
            avg_score=avg_score,
            results_by_scorer=results_by_scorer,
            failed_items_detail=failed_items,
        )


class AsyncEvalsResource(AsyncBaseResource):
    """
    Asynchronous evals resource for evaluation operations.

    Async version of EvalsResource for use with AsyncNoveumClient.
    """

    async def score(
        self,
        dataset_item: DatasetItem,
        agent_output: str,
        scorers: List[ScorerConfig],
        metadata: Optional[Dict[str, Any]] = None,
    ) -> EvalResult:
        """
        Async score agent output against a dataset item.

        Args:
            dataset_item: Dataset item to evaluate against
            agent_output: Agent's output to evaluate
            scorers: List of scorers to apply
            metadata: Optional custom metadata

        Returns:
            EvalResult with scores and reasoning

        Raises:
            NoveumAPIError: If API request fails
        """
        request = EvalRequest(
            dataset_item=dataset_item,
            agent_output=agent_output,
            scorers=scorers,
            metadata=metadata,
        )

        url = self._build_url("/evals/score")
        response = await self.http_client.post(url, json=request.model_dump())

        return EvalResult(**response)

    async def score_batch(
        self,
        items: List[tuple[DatasetItem, str]],
        scorers: List[ScorerConfig],
        parallel: int = 5,
    ) -> AsyncIterator[EvalResult]:
        """
        Async batch evaluate multiple items with parallel scoring.

        Args:
            items: List of (dataset_item, agent_output) tuples
            scorers: List of scorers to apply
            parallel: Number of concurrent evaluations

        Yields:
            EvalResult for each item as it completes
        """
        batch_items = [
            {
                "dataset_item": item.model_dump(),
                "agent_output": output,
            }
            for item, output in items
        ]

        url = self._build_url("/evals/score-batch")
        response = await self.http_client.post(
            url,
            json={
                "items": batch_items,
                "scorers": [s.model_dump() for s in scorers],
                "parallel": parallel,
            },
        )

        if isinstance(response, list):
            for result_data in response:
                yield EvalResult(**result_data)
        else:
            yield EvalResult(**response)

    async def score_with_retries(
        self,
        dataset_item: DatasetItem,
        agent_output: str,
        scorers: List[ScorerConfig],
        max_retries: int = 3,
        backoff_factor: float = 2.0,
    ) -> EvalResult:
        """
        Async score with automatic retry on transient failures.

        Args:
            dataset_item: Dataset item to evaluate against
            agent_output: Agent's output to evaluate
            scorers: List of scorers to apply
            max_retries: Maximum number of retries
            backoff_factor: Exponential backoff factor

        Returns:
            EvalResult with scores and reasoning
        """
        import asyncio

        last_error = None
        for attempt in range(max_retries + 1):
            try:
                return await self.score(dataset_item, agent_output, scorers)
            except Exception as e:
                last_error = e
                if attempt < max_retries:
                    wait_time = backoff_factor ** attempt
                    await asyncio.sleep(wait_time)

        raise last_error or Exception("Failed to score after retries")

    def aggregate_results(self, results: List[EvalResult]) -> TestResult:
        """
        Aggregate multiple evaluation results for test assertions.

        Args:
            results: List of EvalResult objects

        Returns:
            TestResult with aggregated statistics
        """
        if not results:
            return TestResult(
                total_items=0,
                passed_items=0,
                failed_items=0,
                passing_rate=0.0,
                avg_score=0.0,
                results_by_scorer={},
            )

        total = len(results)
        passed = sum(1 for r in results if r.overall_passed)
        failed = total - passed
        avg_score = sum(r.overall_score for r in results) / total if total > 0 else 0

        results_by_scorer: Dict[str, List[float]] = {}
        for result in results:
            for score in result.scores:
                if score.scorer_id not in results_by_scorer:
                    results_by_scorer[score.scorer_id] = []
                results_by_scorer[score.scorer_id].append(score.score)

        failed_items = [r for r in results if not r.overall_passed]

        return TestResult(
            total_items=total,
            passed_items=passed,
            failed_items=failed,
            passing_rate=passed / total if total > 0 else 0,
            avg_score=avg_score,
            results_by_scorer=results_by_scorer,
            failed_items_detail=failed_items,
        )
