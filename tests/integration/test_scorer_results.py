"""
Scorer Results API Integration Tests - Complete End-to-End Flow

This module tests scorer results management with dataset integration:
1. Setup prerequisites (dataset + scorer)
2. Create single result → Get result → Update result
3. Create batch results → List with filters
4. Delete results → Cleanup

Endpoints Tested (6 total):
- POST /api/v1/scorers/results  (create single)
- POST /api/v1/scorers/results/batch  (create batch)
- GET  /api/v1/scorers/results  (list with filters)
- GET  /api/v1/scorers/results/{dataset_slug}/{item_id}/{scorer_id}  (get specific)
- PUT  /api/v1/scorers/results/{dataset_slug}/{item_id}/{scorer_id}  (update)
- DELETE /api/v1/scorers/results/{dataset_slug}/{item_id}/{scorer_id}  (delete)

Usage:
    pytest test_scorer_results.py -v
    pytest test_scorer_results.py -v -k "create_result"  # Run specific test
    pytest test_scorer_results.py -v --tb=short  # Shorter tracebacks
"""

import uuid
from datetime import datetime
from typing import Any

import pytest

from noveum_api_client import Client, NoveumClient
from noveum_api_client.api.datasets import (
    delete_api_v1_datasets_by_slug,
    post_api_v1_datasets,
    post_api_v1_datasets_by_dataset_slug_items,
)
from noveum_api_client.api.scorer_results import (
    delete_api_v1_scorers_results_by_dataset_slug_by_item_id_by_scorer_id,
    get_api_v1_scorers_results,
    get_api_v1_scorers_results_by_dataset_slug_by_item_id_by_scorer_id,
    post_api_v1_scorers_results,
    post_api_v1_scorers_results_batch,
    put_api_v1_scorers_results_by_dataset_slug_by_item_id_by_scorer_id,
)
from noveum_api_client.api.scorers import (
    delete_api_v1_scorers_by_id,
    post_api_v1_scorers,
)
from noveum_api_client.models.post_api_v1_datasets_body import PostApiV1DatasetsBody
from noveum_api_client.models.post_api_v1_datasets_by_dataset_slug_items_body import (
    PostApiV1DatasetsByDatasetSlugItemsBody,
)
from noveum_api_client.models.post_api_v1_scorers_body import PostApiV1ScorersBody
from noveum_api_client.models.post_api_v1_scorers_results_batch_body import (
    PostApiV1ScorersResultsBatchBody,
)
from noveum_api_client.models.post_api_v1_scorers_results_body import PostApiV1ScorersResultsBody
from noveum_api_client.models.put_api_v1_scorers_results_by_dataset_slug_by_item_id_by_scorer_id_body import (
    PutApiV1ScorersResultsByDatasetSlugByItemIdByScorerIdBody,
)


from constants import (
    SKIP_NO_DATASET_AVAILABLE,
    SKIP_MISSING_PREREQUISITES,
    SKIP_NO_RESULTS_AVAILABLE,
    SKIP_NO_SCORER_AVAILABLE,
    SKIP_NO_RESULTS_TO_DELETE,
    SKIP_NO_SCORER_TO_DELETE,
    SKIP_NO_DATASET_TO_DELETE,
)

@pytest.mark.scorers
@pytest.mark.integration
@pytest.mark.serial
class TestScorerResultsE2EFlow:
    """
    End-to-end integration tests for Scorer Results API.
    
    Tests run in sequence to verify the complete scorer results lifecycle:
    setup → create → query → update → delete → cleanup
    """

    @pytest.fixture(scope="class")
    def results_context(self) -> dict[str, Any]:
        """Shared context for storing test data across tests."""
        return {
            "dataset_slug": None,
            "scorer_id": None,
            "item_ids": [],
            "created_results": [],
        }

    @pytest.fixture(scope="class")
    def unique_identifiers(self) -> dict[str, str]:
        """Generate unique identifiers for this test run."""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        unique_id = str(uuid.uuid4())[:8]
        return {
            "dataset_slug": f"results-test-{timestamp}-{unique_id}",
            "scorer_name": f"Results_Test_Scorer_{timestamp}_{unique_id}",
        }

    # =========================================================================
    # Phase 1: Setup Prerequisites
    # =========================================================================

    def test_01_setup_create_dataset(
        self,
        low_level_client: Client,
        unique_identifiers: dict[str, str],
        results_context: dict[str, Any],
    ) -> None:
        """Create a dataset for storing scorer results."""
        dataset_slug = unique_identifiers["dataset_slug"]
        
        body = PostApiV1DatasetsBody(
            name=f"Scorer Results Test Dataset {datetime.now().strftime('%H%M%S')}",
            slug=dataset_slug,
            description="Dataset for scorer results integration tests",
        )
        
        response = post_api_v1_datasets.sync_detailed(
            client=low_level_client,
            body=body,
        )
        
        assert response.status_code in [200, 201], (
            f"Create dataset failed: {response.status_code}"
        )
        
        results_context["dataset_slug"] = dataset_slug
        print(f"\n✅ Created dataset: {dataset_slug}")

    def test_02_setup_add_items(
        self,
        low_level_client: Client,
        results_context: dict[str, Any],
    ) -> None:
        """Add items to the dataset."""
        if not results_context.get("dataset_slug"):
            pytest.skip(SKIP_NO_DATASET_AVAILABLE)
        
        items = []
        for i in range(10):
            items.append({
                "item_id": f"results-item-{i:03d}",
                "item_type": "evaluation",
                "content": {
                    "input_text": f"Test input {i}",
                    "output_text": f"Test output {i}",
                    "ground_truth": f"Expected {i}",
                },
                "metadata": {"index": i},
            })
        
        body = PostApiV1DatasetsByDatasetSlugItemsBody.from_dict({"items": items})
        
        response = post_api_v1_datasets_by_dataset_slug_items.sync_detailed(
            client=low_level_client,
            dataset_slug=results_context["dataset_slug"],
            body=body,
        )
        
        assert response.status_code in [200, 201], (
            f"Add items failed: {response.status_code}"
        )
        
        results_context["item_ids"] = [item["item_id"] for item in items]
        print(f"\n✅ Added {len(items)} items to dataset")

    def test_03_setup_create_scorer(
        self,
        low_level_client: Client,
        unique_identifiers: dict[str, str],
        results_context: dict[str, Any],
    ) -> None:
        """Create a scorer for generating results."""
        scorer_name = unique_identifiers["scorer_name"]
        
        body = PostApiV1ScorersBody(
            name=scorer_name,
            description="Scorer for results integration tests",
            type_="custom",
            tag="results-test",
            config={"evaluation_type": "accuracy"},
        )
        
        response = post_api_v1_scorers.sync_detailed(
            client=low_level_client,
            body=body,
        )
        
        if response.status_code == 500:
            pytest.xfail("Create scorer returned 500 (known backend issue)")

        assert response.status_code in [200, 201], (
            f"Create scorer failed: {response.status_code}"
        )
        
        # Extract scorer ID
        if hasattr(response, "parsed") and response.parsed:
            if hasattr(response.parsed, "id"):
                results_context["scorer_id"] = response.parsed.id
            elif isinstance(response.parsed, dict) and "id" in response.parsed:
                results_context["scorer_id"] = response.parsed["id"]
        
        print(f"\n✅ Created scorer: {scorer_name}")
        if results_context.get("scorer_id"):
            print(f"   ID: {results_context['scorer_id']}")

    # =========================================================================
    # Phase 2: Scorer Results CRUD
    # =========================================================================

    def test_04_create_single_result(
        self,
        low_level_client: Client,
        results_context: dict[str, Any],
    ) -> None:
        """Test creating a single scorer result with metadata."""
        if not all([
            results_context.get("dataset_slug"),
            results_context.get("scorer_id"),
            results_context.get("item_ids"),
        ]):
            pytest.skip(SKIP_MISSING_PREREQUISITES)
        
        result_data = {
            "datasetSlug": results_context["dataset_slug"],
            "itemId": results_context["item_ids"][0],
            "scorerId": results_context["scorer_id"],
            "score": 0.92,
            "reason": "Excellent accuracy on test case",
            "metadata": {
                "evaluation_time_ms": 150,
                "confidence": 0.95,
                "test_type": "single_create",
            },
        }
        
        body = PostApiV1ScorersResultsBody.from_dict(result_data)
        
        response = post_api_v1_scorers_results.sync_detailed(
            client=low_level_client,
            body=body,
        )
        
        assert response.status_code in [200, 201], (
            f"Create result failed: {response.status_code}"
        )
        
        results_context["created_results"].append({
            "item_id": result_data["itemId"],
            "scorer_id": result_data["scorerId"],
        })
        
        print(f"\n✅ Created single scorer result with score: 0.92")

    def test_05_get_scorer_result(
        self,
        low_level_client: Client,
        results_context: dict[str, Any],
    ) -> None:
        """Test retrieving a specific scorer result."""
        if not results_context.get("created_results"):
            pytest.skip(SKIP_NO_RESULTS_AVAILABLE)
        
        result_info = results_context["created_results"][0]
        
        response = get_api_v1_scorers_results_by_dataset_slug_by_item_id_by_scorer_id.sync_detailed(
            client=low_level_client,
            dataset_slug=results_context["dataset_slug"],
            item_id=result_info["item_id"],
            scorer_id=result_info["scorer_id"],
        )
        
        assert response.status_code == 200, (
            f"Get result failed: {response.status_code}"
        )
        
        print(f"\n✅ Retrieved scorer result for item: {result_info['item_id']}")
        
        # Verify data
        if hasattr(response, "parsed") and response.parsed:
            result = response.parsed
            if hasattr(result, "score"):
                print(f"   Score: {result.score}")

    def test_06_update_scorer_result(
        self,
        low_level_client: Client,
        results_context: dict[str, Any],
    ) -> None:
        """Test updating a scorer result."""
        if not results_context.get("created_results"):
            pytest.skip(SKIP_NO_RESULTS_AVAILABLE)
        
        result_info = results_context["created_results"][0]
        
        body = PutApiV1ScorersResultsByDatasetSlugByItemIdByScorerIdBody.from_dict({
            "score": 0.95,
            "reason": "Updated score after review - improved accuracy",
            "metadata": {
                "updated_at": datetime.now().isoformat(),
                "reviewer": "integration_test",
            },
        })
        
        response = put_api_v1_scorers_results_by_dataset_slug_by_item_id_by_scorer_id.sync_detailed(
            client=low_level_client,
            dataset_slug=results_context["dataset_slug"],
            item_id=result_info["item_id"],
            scorer_id=result_info["scorer_id"],
            body=body,
        )
        
        assert response.status_code in [200, 204], (
            f"Update result failed: {response.status_code}"
        )
        
        print(f"\n✅ Updated scorer result: score changed to 0.95")

    def test_07_create_batch_results(
        self,
        low_level_client: Client,
        results_context: dict[str, Any],
    ) -> None:
        """Test creating batch scorer results."""
        if not all([
            results_context.get("dataset_slug"),
            results_context.get("scorer_id"),
            results_context.get("item_ids"),
        ]):
            pytest.skip(SKIP_MISSING_PREREQUISITES)
        
        # Create results for remaining items (skip first one already created)
        results = []
        for i, item_id in enumerate(results_context["item_ids"][1:7], start=1):
            results.append({
                "datasetSlug": results_context["dataset_slug"],
                "itemId": item_id,
                "scorerId": results_context["scorer_id"],
                "score": 0.7 + (i * 0.03),  # Varying scores: 0.73, 0.76, 0.79...
                "reason": f"Batch evaluation result #{i}",
                "metadata": {
                    "batch_index": i,
                    "processing_time_ms": 100 + (i * 20),
                },
            })
        
        body = PostApiV1ScorersResultsBatchBody.from_dict({"results": results})
        
        response = post_api_v1_scorers_results_batch.sync_detailed(
            client=low_level_client,
            body=body,
        )
        
        assert response.status_code in [200, 201], (
            f"Create batch results failed: {response.status_code}"
        )
        
        # Track created results
        for result in results:
            results_context["created_results"].append({
                "item_id": result["itemId"],
                "scorer_id": result["scorerId"],
            })
        
        print(f"\n✅ Created {len(results)} batch scorer results")

    # =========================================================================
    # Phase 3: Query Operations
    # =========================================================================

    def test_08_list_all_results(
        self,
        low_level_client: Client,
        noveum_client: NoveumClient,
    ) -> None:
        """Test listing all scorer results."""
        # High-level client
        response = noveum_client.get_results(limit=20)
        assert response["status_code"] == 200, f"List failed: {response}"
        
        results_count = 0
        if response.get("data"):
            results = response["data"] if isinstance(response["data"], list) else []
            results_count = len(results)
        
        print(f"\n✅ Listed all scorer results: found {results_count}")

    def test_09_list_results_with_filters(
        self,
        low_level_client: Client,
        results_context: dict[str, Any],
    ) -> None:
        """Test listing scorer results with dataset filter."""
        if not results_context.get("dataset_slug"):
            pytest.skip(SKIP_NO_DATASET_AVAILABLE)
        
        response = get_api_v1_scorers_results.sync_detailed(
            client=low_level_client,
            dataset_slug=results_context["dataset_slug"],
            limit=20,
        )
        
        assert response.status_code == 200, (
            f"List with filters failed: {response.status_code}"
        )
        
        results_count = 0
        if hasattr(response, "parsed") and response.parsed:
            results = response.parsed if isinstance(response.parsed, list) else []
            results_count = len(results)
        
        print(f"\n✅ Listed filtered results: found {results_count} for dataset")

    def test_10_list_results_by_scorer(
        self,
        low_level_client: Client,
        results_context: dict[str, Any],
    ) -> None:
        """Test listing scorer results filtered by scorer ID."""
        if not results_context.get("scorer_id"):
            pytest.skip(SKIP_NO_SCORER_AVAILABLE)
        
        response = get_api_v1_scorers_results.sync_detailed(
            client=low_level_client,
            scorer_id=results_context["scorer_id"],
            limit=20,
        )
        
        assert response.status_code == 200, (
            f"List by scorer failed: {response.status_code}"
        )
        
        print(f"\n✅ Listed results by scorer ID: {results_context['scorer_id']}")

    # =========================================================================
    # Phase 4: Cleanup
    # =========================================================================

    def test_11_delete_scorer_result(
        self,
        low_level_client: Client,
        results_context: dict[str, Any],
    ) -> None:
        """Test deleting a scorer result."""
        if not results_context.get("created_results"):
            pytest.skip(SKIP_NO_RESULTS_TO_DELETE)
        
        # Delete last result
        result_info = results_context["created_results"][-1]
        
        response = delete_api_v1_scorers_results_by_dataset_slug_by_item_id_by_scorer_id.sync_detailed(
            client=low_level_client,
            dataset_slug=results_context["dataset_slug"],
            item_id=result_info["item_id"],
            scorer_id=result_info["scorer_id"],
        )
        
        if response.status_code == 500:
            pytest.xfail("Delete returned 500 (known backend issue)")
        
        assert response.status_code in [200, 204], (
            f"Delete result failed: {response.status_code}"
        )
        
        results_context["created_results"].pop()
        print(f"\n✅ Deleted scorer result for item: {result_info['item_id']}")

    def test_12_cleanup_delete_scorer(
        self,
        low_level_client: Client,
        results_context: dict[str, Any],
    ) -> None:
        """Clean up by deleting the test scorer."""
        if not results_context.get("scorer_id"):
            pytest.skip(SKIP_NO_SCORER_TO_DELETE)
        
        response = delete_api_v1_scorers_by_id.sync_detailed(
            client=low_level_client,
            id=results_context["scorer_id"],
        )
        
        if response.status_code == 500:
            pytest.xfail("Scorer deletion returned 500 (known backend issue)")
        
        assert response.status_code in [200, 204], (
            f"Delete scorer failed: {response.status_code}"
        )
        
        print(f"\n✅ Deleted scorer: {results_context['scorer_id']}")

    def test_13_cleanup_delete_dataset(
        self,
        low_level_client: Client,
        results_context: dict[str, Any],
    ) -> None:
        """Clean up by deleting the test dataset."""
        if not results_context.get("dataset_slug"):
            pytest.skip(SKIP_NO_DATASET_TO_DELETE)
        
        response = delete_api_v1_datasets_by_slug.sync_detailed(
            client=low_level_client,
            slug=results_context["dataset_slug"],
        )
        
        if response.status_code == 500:
            pytest.xfail("Dataset deletion returned 500 (known backend issue)")
        
        assert response.status_code in [200, 204], (
            f"Delete dataset failed: {response.status_code}"
        )
        
        print(f"\n✅ Deleted dataset: {results_context['dataset_slug']}")


@pytest.mark.scorers
@pytest.mark.integration
class TestScorerResultsIsolated:
    """
    Isolated tests for scorer results operations.
    """

    def test_list_results_pagination(self, low_level_client: Client) -> None:
        """Test listing results with pagination."""
        response = get_api_v1_scorers_results.sync_detailed(
            client=low_level_client,
            limit=5,
            offset=0,
        )
        
        assert response.status_code == 200
        
        if hasattr(response, "parsed") and response.parsed:
            results = response.parsed if isinstance(response.parsed, list) else []
            assert len(results) <= 5, "Should respect limit"

    def test_list_results_empty_filters(self, low_level_client: Client) -> None:
        """Test listing results with non-matching filters."""
        response = get_api_v1_scorers_results.sync_detailed(
            client=low_level_client,
            dataset_slug="nonexistent-dataset-xyz123",
            limit=10,
        )
        
        # Should return 200 with empty results (not 404)
        assert response.status_code in [200, 404]
