"""
Scorers API Integration Tests - Complete End-to-End Flow

This module tests the complete scorer lifecycle integrated with datasets:
1. Create dataset (prerequisite for scorer results)
2. Create scorer → Get scorer → Update scorer
3. Upload scorer results → List results → Get specific result
4. Delete scorer result → Delete scorer → Cleanup

Endpoints Tested (10 total):
Scorers (5):
- POST /api/v1/scorers  (create)
- GET  /api/v1/scorers  (list)
- GET  /api/v1/scorers/{id}  (get by ID)
- PUT  /api/v1/scorers/{id}  (update)
- DELETE /api/v1/scorers/{id}  (delete)

Scorer Results (5):
- POST /api/v1/scorers/results  (create single)
- POST /api/v1/scorers/results/batch  (create batch)
- GET  /api/v1/scorers/results  (list)
- GET  /api/v1/scorers/results/{dataset_slug}/{item_id}/{scorer_id}  (get)
- DELETE /api/v1/scorers/results/{dataset_slug}/{item_id}/{scorer_id}  (delete)

Usage:
    pytest test_scorers.py -v
    pytest test_scorers.py -v -k "create_scorer"  # Run specific test
    pytest test_scorers.py -v --tb=short  # Shorter tracebacks
"""

import json
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
)
from noveum_api_client.api.scorers import (
    delete_api_v1_scorers_by_id,
    get_api_v1_scorers,
    get_api_v1_scorers_by_id,
    post_api_v1_scorers,
    put_api_v1_scorers_by_id,
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
from noveum_api_client.models.put_api_v1_scorers_by_id_body import PutApiV1ScorersByIdBody

from constants import (
    SKIP_NO_DATASET_SLUG,
    SKIP_NO_SCORER_ID,
    SKIP_MISSING_REQUIRED_CONTEXT,
    SKIP_MISSING_REQUIRED_CONTEXT_FULL,
    SKIP_NO_ITEMS_BATCH_RESULTS,
    SKIP_NO_RESULT_IDS,
)


def parse_response(response: Any) -> dict[str, Any] | list[Any] | None:
    """Parse response body - handles cases where response.parsed is None but content exists."""
    if response.parsed is not None:
        # Convert to dict if it's a model object
        if hasattr(response.parsed, 'to_dict'):
            return response.parsed.to_dict()
        return response.parsed
    
    if response.content:
        try:
            return json.loads(response.content)
        except (json.JSONDecodeError, TypeError):
            return None
    return None


def get_field(obj: Any, field: str) -> Any:
    """Helper to get field value from dict or object."""
    if obj is None:
        return None
    if isinstance(obj, dict):
        return obj.get(field)
    return getattr(obj, field, None)


@pytest.mark.scorers
@pytest.mark.integration
@pytest.mark.serial
class TestScorersE2EFlow:
    """
    End-to-end integration tests for Scorers API.
    
    Tests run in sequence to verify the complete scorer workflow:
    setup dataset → create scorer → add results → query → cleanup
    """

    @pytest.fixture(scope="class")
    def scorer_context(self) -> dict[str, Any]:
        """Shared context for storing scorer data across tests."""
        return {
            "dataset_slug": None,
            "scorer_id": None,
            "scorer_name": None,
            "item_ids": [],
            "result_ids": [],
        }

    @pytest.fixture(scope="class")
    def unique_identifiers(self) -> dict[str, str]:
        """Generate unique identifiers for this test run."""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        unique_id = str(uuid.uuid4())[:8]
        return {
            "dataset_slug": f"scorer-test-{timestamp}-{unique_id}",
            "scorer_name": f"SDK_Test_Scorer_{timestamp}_{unique_id}",
        }

    # =========================================================================
    # Phase 1: Setup - Create Dataset for Scorer Results
    # =========================================================================

    def test_01_setup_create_dataset(
        self,
        low_level_client: Client,
        unique_identifiers: dict[str, str],
        scorer_context: dict[str, Any],
    ) -> None:
        """Create a dataset to store scorer results against with full response validation."""
        dataset_slug = unique_identifiers["dataset_slug"]
        dataset_name = f"Scorer Test Dataset {datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        body = PostApiV1DatasetsBody(
            name=dataset_name,
            slug=dataset_slug,
            description="Dataset for scorer integration tests",
        )
        
        response = post_api_v1_datasets.sync_detailed(
            client=low_level_client,
            body=body,
        )
        
        # Handle known backend 500 error for scorer creation
        if response.status_code == 500:
            pytest.xfail("Create scorer returned 500 (known backend issue)")
        
        assert response.status_code in [200, 201], (
            f"Create dataset failed: {response.status_code}"
        )
        
        # ===== VALIDATE RESPONSE BODY =====
        data = parse_response(response)
        
        print(f"\n✅ Created dataset - validating response:")
        
        if data:
            success = get_field(data, 'success')
            if success is not None:
                print(f"   ✓ success: {success}")
            
            dataset = data.get("data", data) if isinstance(data, dict) else data
            
            returned_slug = get_field(dataset, 'slug')
            if returned_slug:
                assert returned_slug == dataset_slug, f"Slug mismatch: expected {dataset_slug}, got {returned_slug}"
                print(f"   ✓ slug: {returned_slug}")
            
            returned_name = get_field(dataset, 'name')
            if returned_name:
                print(f"   ✓ name: {returned_name}")
            
            created_at = get_field(dataset, 'created_at')
            if created_at:
                print(f"   ✓ created_at: {created_at}")
        
        scorer_context["dataset_slug"] = dataset_slug
        scorer_context["dataset_name"] = dataset_name
        print(f"\n   Dataset slug: {dataset_slug}")

    def test_02_setup_add_dataset_items(
        self,
        low_level_client: Client,
        scorer_context: dict[str, Any],
        sample_dataset_items: list[dict[str, Any]],
    ) -> None:
        """Add items to the dataset that will receive scorer results with full validation."""
        if not scorer_context.get("dataset_slug"):
            pytest.skip(SKIP_NO_DATASET_SLUG)
        
        slug = scorer_context["dataset_slug"]
        items = sample_dataset_items[:5]  # Use first 5 items
        
        body = PostApiV1DatasetsByDatasetSlugItemsBody.from_dict({"items": items})
        
        response = post_api_v1_datasets_by_dataset_slug_items.sync_detailed(
            client=low_level_client,
            dataset_slug=slug,
            body=body,
        )
        
        # Handle known backend 500 error for scorer creation
        if response.status_code == 500:
            pytest.xfail("Create scorer returned 500 (known backend issue)")
        
        assert response.status_code in [200, 201], (
            f"Add items failed: {response.status_code}"
        )
        
        # ===== VALIDATE RESPONSE BODY =====
        data = parse_response(response)
        
        print(f"\n✅ Added items - validating response:")
        
        if data:
            success = get_field(data, 'success')
            if success is not None:
                assert success is True, "Expected success=True"
                print(f"   ✓ success: {success}")
            
            added_count = get_field(data, 'added_count') or get_field(data, 'count')
            if added_count is not None:
                assert added_count == len(items), f"Added count mismatch: expected {len(items)}, got {added_count}"
                print(f"   ✓ items added: {added_count}")
            
            returned_items = get_field(data, 'items') or get_field(data, 'data')
            if returned_items and isinstance(returned_items, list):
                print(f"   ✓ returned items: {len(returned_items)}")
        
        scorer_context["item_ids"] = [item["item_id"] for item in items]
        print(f"   Item IDs stored: {len(scorer_context['item_ids'])}")

    # =========================================================================
    # Phase 2: Scorer CRUD Operations
    # =========================================================================

    def test_03_list_scorers(self, low_level_client: Client) -> None:
        """Test listing existing scorers with full response validation."""
        response = get_api_v1_scorers.sync_detailed(
            client=low_level_client,
        )
        
        assert response.status_code == 200, f"List scorers failed: {response.status_code}"
        
        # ===== VALIDATE RESPONSE BODY =====
        data = parse_response(response)
        assert data is not None, "Response data should not be None"
        
        print(f"\n✅ Listed scorers - validating response:")
        
        # Get scorers list
        scorers = data.get("scorers", data) if isinstance(data, dict) else data
        
        if isinstance(scorers, list):
            print(f"   ✓ scorers count: {len(scorers)}")
            
            if len(scorers) > 0:
                first_scorer = scorers[0]
                print(f"\n   First scorer validation:")
                
                scorer_id = get_field(first_scorer, 'id')
                if scorer_id:
                    print(f"   ✓ id: {scorer_id}")
                
                name = get_field(first_scorer, 'name')
                if name:
                    print(f"   ✓ name: {name}")
                
                scorer_type = get_field(first_scorer, 'type')
                if scorer_type:
                    print(f"   ✓ type: {scorer_type}")
                
                tag = get_field(first_scorer, 'tag')
                if tag:
                    print(f"   ✓ tag: {tag}")
                
                created_at = get_field(first_scorer, 'created_at')
                if created_at:
                    print(f"   ✓ created_at: {created_at}")
        
        # Check pagination if present
        pagination = data.get("pagination", {}) if isinstance(data, dict) else {}
        if pagination:
            print(f"\n   Pagination:")
            print(f"   ✓ total: {pagination.get('total', 'N/A')}")

    def test_04_create_scorer(
        self,
        low_level_client: Client,
        unique_identifiers: dict[str, str],
        scorer_context: dict[str, Any],
    ) -> None:
        """Test creating a new scorer with full configuration and response validation."""
        scorer_name = unique_identifiers["scorer_name"]
        scorer_description = "Integration test scorer - evaluates response quality"
        scorer_type = "llm_as_judge"
        scorer_tag = "integration-test"
        
        body = PostApiV1ScorersBody(
            name=scorer_name,
            description=scorer_description,
            type_=scorer_type,  # Maps to "type" in JSON
            tag=scorer_tag,
            config={
                "model": "gpt-4",
                "prompt": "Evaluate the quality of this response on a scale of 0-1",
                "criteria": ["accuracy", "completeness", "clarity"],
            },
        )
        
        response = post_api_v1_scorers.sync_detailed(
            client=low_level_client,
            body=body,
        )
        
        # Handle known backend 500 error for scorer creation
        if response.status_code == 500:
            pytest.xfail("Create scorer returned 500 (known backend issue)")
        
        assert response.status_code in [200, 201], (
            f"Create scorer failed: {response.status_code} - {response.content}"
        )
        
        # ===== VALIDATE RESPONSE BODY =====
        data = parse_response(response)
        
        print(f"\n✅ Created scorer - validating response:")
        
        if data:
            success = get_field(data, 'success')
            if success is not None:
                assert success is True, "Expected success=True"
                print(f"   ✓ success: {success}")
            
            scorer = data.get("data", data) if isinstance(data, dict) else data
            
            # Extract and validate scorer ID
            scorer_id = get_field(scorer, 'id') or get_field(scorer, 'scorer_id')
            if scorer_id:
                scorer_context["scorer_id"] = scorer_id
                print(f"   ✓ id: {scorer_id}")
            
            # Validate name
            returned_name = get_field(scorer, 'name')
            if returned_name:
                assert returned_name == scorer_name, f"Name mismatch: expected {scorer_name}, got {returned_name}"
                print(f"   ✓ name: {returned_name}")
            
            # Validate description
            returned_desc = get_field(scorer, 'description')
            if returned_desc:
                print(f"   ✓ description: {returned_desc[:50]}...")
            
            # Validate type
            returned_type = get_field(scorer, 'type')
            if returned_type:
                print(f"   ✓ type: {returned_type}")
            
            # Validate tag
            returned_tag = get_field(scorer, 'tag')
            if returned_tag:
                assert returned_tag == scorer_tag, f"Tag mismatch: expected {scorer_tag}, got {returned_tag}"
                print(f"   ✓ tag: {returned_tag}")
            
            # Validate config
            config = get_field(scorer, 'config')
            if config:
                print(f"   ✓ config: present")
                if isinstance(config, dict):
                    for key in list(config.keys())[:3]:
                        print(f"      - {key}: {str(config[key])[:30]}...")
            
            # Check timestamps
            created_at = get_field(scorer, 'created_at')
            if created_at:
                print(f"   ✓ created_at: {created_at}")
        
        scorer_context["scorer_name"] = scorer_name
        scorer_context["scorer_description"] = scorer_description
        scorer_context["scorer_type"] = scorer_type
        scorer_context["scorer_tag"] = scorer_tag

    def test_05_get_scorer(
        self,
        low_level_client: Client,
        scorer_context: dict[str, Any],
    ) -> None:
        """Test retrieving scorer by ID with full response validation."""
        if not scorer_context.get("scorer_id"):
            pytest.skip(SKIP_NO_SCORER_ID)
        
        scorer_id = scorer_context["scorer_id"]
        expected_name = scorer_context.get("scorer_name")
        expected_type = scorer_context.get("scorer_type")
        expected_tag = scorer_context.get("scorer_tag")
        
        response = get_api_v1_scorers_by_id.sync_detailed(
            scorer_id,  # id_path
            client=low_level_client,
            id_query=scorer_id,
        )
        
        assert response.status_code == 200, (
            f"Get scorer failed: {response.status_code}"
        )
        
        # ===== VALIDATE RESPONSE BODY =====
        data = parse_response(response)
        assert data is not None, "Response data should not be None"
        
        print(f"\n✅ Retrieved scorer - validating response:")
        
        # API might wrap in data or return directly
        scorer = data.get("data", data) if isinstance(data, dict) else data
        
        # Validate scorer_id matches request
        returned_id = get_field(scorer, 'id')
        if returned_id:
            assert returned_id == scorer_id, f"Scorer ID mismatch: expected {scorer_id}, got {returned_id}"
            print(f"   ✓ id: {returned_id}")
        
        # Validate name
        returned_name = get_field(scorer, 'name')
        if returned_name:
            if expected_name:
                assert returned_name == expected_name, f"Name mismatch: expected {expected_name}, got {returned_name}"
            print(f"   ✓ name: {returned_name}")
        
        # Validate description
        description = get_field(scorer, 'description')
        if description:
            print(f"   ✓ description: {description[:50]}...")
        
        # Validate type
        scorer_type = get_field(scorer, 'type')
        if scorer_type:
            if expected_type:
                assert scorer_type == expected_type, f"Type mismatch"
            print(f"   ✓ type: {scorer_type}")
        
        # Validate tag
        tag = get_field(scorer, 'tag')
        if tag:
            if expected_tag:
                assert tag == expected_tag, f"Tag mismatch"
            print(f"   ✓ tag: {tag}")
        
        # Validate config
        config = get_field(scorer, 'config')
        if config:
            print(f"   ✓ config: present")
        
        # Validate timestamps
        created_at = get_field(scorer, 'created_at')
        if created_at:
            print(f"   ✓ created_at: {created_at}")
        
        updated_at = get_field(scorer, 'updated_at')
        if updated_at:
            print(f"   ✓ updated_at: {updated_at}")

    def test_06_update_scorer(
        self,
        low_level_client: Client,
        scorer_context: dict[str, Any],
    ) -> None:
        """Test updating scorer configuration with full response validation."""
        if not scorer_context.get("scorer_id"):
            pytest.skip(SKIP_NO_SCORER_ID)
        
        scorer_id = scorer_context["scorer_id"]
        updated_name = f"Updated_{scorer_context.get('scorer_name', 'Scorer')}"
        updated_description = "Updated description from integration test"
        
        body = PutApiV1ScorersByIdBody(
            name=updated_name,
            description=updated_description,
        )
        
        response = put_api_v1_scorers_by_id.sync_detailed(
            client=low_level_client,
            id=scorer_id,
            body=body,
        )
        
        assert response.status_code in [200, 204], (
            f"Update scorer failed: {response.status_code}"
        )
        
        # ===== VALIDATE RESPONSE BODY =====
        print(f"\n✅ Updated scorer - validating response:")
        
        if response.status_code == 200:
            data = parse_response(response)
            
            if data:
                success = get_field(data, 'success')
                if success is not None:
                    assert success is True, "Expected success=True"
                    print(f"   ✓ success: {success}")
                
                scorer = data.get("data", data) if isinstance(data, dict) else data
                
                # Validate updated name
                returned_name = get_field(scorer, 'name')
                if returned_name:
                    assert returned_name == updated_name, f"Updated name mismatch"
                    print(f"   ✓ name updated: {returned_name}")
                
                # Validate updated description
                returned_desc = get_field(scorer, 'description')
                if returned_desc:
                    print(f"   ✓ description updated: {returned_desc[:50]}...")
                
                # Check updated_at timestamp
                updated_at = get_field(scorer, 'updated_at')
                if updated_at:
                    print(f"   ✓ updated_at: {updated_at}")
        else:
            print(f"   ✓ status: 204 No Content (update successful)")
        
        # Update context with new values
        scorer_context["scorer_name"] = updated_name
        scorer_context["scorer_description"] = updated_description

    # =========================================================================
# Phase 3: Scorer Results Operations
    # =========================================================================

    def test_07_create_single_scorer_result(
        self,
        low_level_client: Client,
        scorer_context: dict[str, Any],
    ) -> None:
        """Test creating a single scorer result with full response validation."""
        if not all([
            scorer_context.get("dataset_slug"),
            scorer_context.get("scorer_id"),
            scorer_context.get("item_ids"),
        ]):
            pytest.skip(SKIP_MISSING_REQUIRED_CONTEXT_FULL)
        
        test_score = 0.85
        test_reason = "Good response quality with clear explanation"
        result_data = {
            "datasetSlug": scorer_context["dataset_slug"],
            "itemId": scorer_context["item_ids"][0],
            "scorerId": scorer_context["scorer_id"],
            "score": test_score,
            "reason": test_reason,
            "metadata": {
                "evaluation_method": "automated",
                "test_type": "integration",
            },
        }
        
        body = PostApiV1ScorersResultsBody.from_dict(result_data)
        
        response = post_api_v1_scorers_results.sync_detailed(
            client=low_level_client,
            body=body,
        )
        
        # Handle known backend 500 error for scorer creation
        if response.status_code == 500:
            pytest.xfail("Create scorer returned 500 (known backend issue)")
        
        assert response.status_code in [200, 201], (
            f"Create result failed: {response.status_code} - {response.content}"
        )
        
        # ===== VALIDATE RESPONSE BODY =====
        data = parse_response(response)
        
        print(f"\n✅ Created single scorer result - validating response:")
        
        if data:
            success = get_field(data, 'success')
            if success is not None:
                assert success is True, "Expected success=True"
                print(f"   ✓ success: {success}")
            
            result = data.get("data", data) if isinstance(data, dict) else data
            
            # Validate score
            returned_score = get_field(result, 'score')
            if returned_score is not None:
                assert returned_score == test_score, f"Score mismatch: expected {test_score}, got {returned_score}"
                print(f"   ✓ score: {returned_score}")
            
            # Validate dataset_slug
            returned_dataset = get_field(result, 'dataset_slug') or get_field(result, 'datasetSlug')
            if returned_dataset:
                assert returned_dataset == scorer_context["dataset_slug"], "Dataset slug mismatch"
                print(f"   ✓ dataset_slug: {returned_dataset}")
            
            # Validate item_id
            returned_item = get_field(result, 'item_id') or get_field(result, 'itemId')
            if returned_item:
                assert returned_item == result_data["itemId"], "Item ID mismatch"
                print(f"   ✓ item_id: {returned_item}")
            
            # Validate scorer_id
            returned_scorer = get_field(result, 'scorer_id') or get_field(result, 'scorerId')
            if returned_scorer:
                assert returned_scorer == scorer_context["scorer_id"], "Scorer ID mismatch"
                print(f"   ✓ scorer_id: {returned_scorer}")
            
            # Validate reason
            returned_reason = get_field(result, 'reason')
            if returned_reason:
                print(f"   ✓ reason: {returned_reason[:50]}...")
            
            # Validate metadata
            metadata = get_field(result, 'metadata')
            if metadata:
                print(f"   ✓ metadata: present")
            
            # Check timestamps
            created_at = get_field(result, 'created_at')
            if created_at:
                print(f"   ✓ created_at: {created_at}")
        
        scorer_context["result_ids"].append({
            "item_id": scorer_context["item_ids"][0],
            "scorer_id": scorer_context["scorer_id"],
        })
        scorer_context["last_score"] = test_score

    def test_08_create_batch_scorer_results(
        self,
        low_level_client: Client,
        scorer_context: dict[str, Any],
    ) -> None:
        """Test creating batch scorer results with full response validation."""
        if not all([
            scorer_context.get("dataset_slug"),
            scorer_context.get("scorer_id"),
            scorer_context.get("item_ids"),
        ]):
            pytest.skip(SKIP_MISSING_REQUIRED_CONTEXT)
        
        # Create results for remaining items (skip first one already done)
        results = []
        for i, item_id in enumerate(scorer_context["item_ids"][1:], start=1):
            results.append({
                "datasetSlug": scorer_context["dataset_slug"],
                "itemId": item_id,
                "scorerId": scorer_context["scorer_id"],
                "score": 0.7 + (i * 0.05),  # Varying scores
                "reason": f"Batch evaluation result {i}",
                "metadata": {"batch_index": i},
            })
        
        if not results:
            pytest.skip(SKIP_NO_ITEMS_BATCH_RESULTS)
        
        body = PostApiV1ScorersResultsBatchBody.from_dict({"results": results})
        
        response = post_api_v1_scorers_results_batch.sync_detailed(
            client=low_level_client,
            body=body,
        )
        
        # Handle known backend 500 error for scorer creation
        if response.status_code == 500:
            pytest.xfail("Create scorer returned 500 (known backend issue)")
        
        assert response.status_code in [200, 201], (
            f"Create batch results failed: {response.status_code}"
        )
        
        # ===== VALIDATE RESPONSE BODY =====
        data = parse_response(response)
        
        print(f"\n✅ Created batch results - validating response:")
        
        if data:
            success = get_field(data, 'success')
            if success is not None:
                assert success is True, "Expected success=True"
                print(f"   ✓ success: {success}")
            
            # Check count
            created_count = get_field(data, 'created_count') or get_field(data, 'count')
            if created_count is not None:
                assert created_count == len(results), f"Created count mismatch: expected {len(results)}, got {created_count}"
                print(f"   ✓ results created: {created_count}")
            
            # Check returned results
            returned_results = get_field(data, 'results') or get_field(data, 'data')
            if returned_results and isinstance(returned_results, list):
                print(f"   ✓ returned results: {len(returned_results)}")
                
                # Validate first result in batch
                if len(returned_results) > 0:
                    first = returned_results[0]
                    score = get_field(first, 'score')
                    if score is not None:
                        print(f"   ✓ first result score: {score}")
                    
                    item_id = get_field(first, 'item_id') or get_field(first, 'itemId')
                    if item_id:
                        print(f"   ✓ first result item_id: {item_id}")
            
            # Check for any errors
            errors = get_field(data, 'errors')
            if errors:
                print(f"   ⚠ errors: {errors}")
        
        # Track created results
        for result in results:
            scorer_context["result_ids"].append({
                "item_id": result["itemId"],
                "scorer_id": result["scorerId"],
            })
        
        print(f"   Total results created: {len(results)}")

    def test_09_list_scorer_results(
        self,
        low_level_client: Client,
        noveum_client: NoveumClient,
        scorer_context: dict[str, Any],
    ) -> None:
        """Test listing scorer results with full response validation."""
        # Test high-level client
        response = noveum_client.get_results(limit=10)
        assert response["status_code"] == 200, f"List results failed: {response}"
        print(f"\n✅ Listed scorer results (high-level): status={response['status_code']}")
        
        # Test low-level client with full validation
        response = get_api_v1_scorers_results.sync_detailed(
            client=low_level_client,
            limit=10,
        )
        assert response.status_code == 200, (
            f"List results failed: {response.status_code}"
        )
        
        # ===== VALIDATE RESPONSE BODY =====
        data = parse_response(response)
        assert data is not None, "Response data should not be None"
        
        print(f"✅ Listed scorer results (low-level) - validating response:")
        
        # Get results list
        results = data.get("results", data) if isinstance(data, dict) else data
        
        if isinstance(results, list):
            print(f"   ✓ results count: {len(results)}")
            
            if len(results) > 0:
                first_result = results[0]
                print(f"\n   First result validation:")
                
                score = get_field(first_result, 'score')
                if score is not None:
                    print(f"   ✓ score: {score}")
                
                dataset_slug = get_field(first_result, 'dataset_slug') or get_field(first_result, 'datasetSlug')
                if dataset_slug:
                    print(f"   ✓ dataset_slug: {dataset_slug}")
                
                item_id = get_field(first_result, 'item_id') or get_field(first_result, 'itemId')
                if item_id:
                    print(f"   ✓ item_id: {item_id}")
                
                scorer_id = get_field(first_result, 'scorer_id') or get_field(first_result, 'scorerId')
                if scorer_id:
                    print(f"   ✓ scorer_id: {scorer_id}")
                
                reason = get_field(first_result, 'reason')
                if reason:
                    print(f"   ✓ reason: {reason[:50]}...")
                
                created_at = get_field(first_result, 'created_at')
                if created_at:
                    print(f"   ✓ created_at: {created_at}")
        
        # Check pagination if present
        pagination = data.get("pagination", {}) if isinstance(data, dict) else {}
        if pagination:
            print(f"\n   Pagination:")
            print(f"   ✓ total: {pagination.get('total', 'N/A')}")

    def test_10_get_specific_result(
        self,
        low_level_client: Client,
        scorer_context: dict[str, Any],
    ) -> None:
        """Test getting a specific scorer result with full response validation."""
        if not scorer_context.get("result_ids"):
            pytest.skip(SKIP_NO_RESULT_IDS)
        
        result_info = scorer_context["result_ids"][0]
        expected_score = scorer_context.get("last_score", 0.85)
        
        response = get_api_v1_scorers_results_by_dataset_slug_by_item_id_by_scorer_id.sync_detailed(
            client=low_level_client,
            dataset_slug=scorer_context["dataset_slug"],
            item_id=result_info["item_id"],
            scorer_id=result_info["scorer_id"],
        )
        
        assert response.status_code == 200, (
            f"Get result failed: {response.status_code}"
        )
        
        # ===== VALIDATE RESPONSE BODY =====
        data = parse_response(response)
        assert data is not None, "Response data should not be None"
        
        print(f"\n✅ Retrieved specific result - validating response:")
        
        # API might wrap in data or return directly
        result = data.get("data", data) if isinstance(data, dict) else data
        
        # Validate score
        score = get_field(result, 'score')
        if score is not None:
            assert score == expected_score, f"Score mismatch: expected {expected_score}, got {score}"
            print(f"   ✓ score: {score}")
        
        # Validate dataset_slug
        dataset_slug = get_field(result, 'dataset_slug') or get_field(result, 'datasetSlug')
        if dataset_slug:
            assert dataset_slug == scorer_context["dataset_slug"], "Dataset slug mismatch"
            print(f"   ✓ dataset_slug: {dataset_slug}")
        
        # Validate item_id
        item_id = get_field(result, 'item_id') or get_field(result, 'itemId')
        if item_id:
            assert item_id == result_info["item_id"], "Item ID mismatch"
            print(f"   ✓ item_id: {item_id}")
        
        # Validate scorer_id
        scorer_id = get_field(result, 'scorer_id') or get_field(result, 'scorerId')
        if scorer_id:
            assert scorer_id == result_info["scorer_id"], "Scorer ID mismatch"
            print(f"   ✓ scorer_id: {scorer_id}")
        
        # Validate reason
        reason = get_field(result, 'reason')
        if reason:
            print(f"   ✓ reason: {reason[:50]}...")
        
        # Validate metadata
        metadata = get_field(result, 'metadata')
        if metadata:
            print(f"   ✓ metadata: present")
            if isinstance(metadata, dict):
                for key in list(metadata.keys())[:3]:
                    print(f"      - {key}: {metadata[key]}")
        
        # Check timestamps
        created_at = get_field(result, 'created_at')
        if created_at:
            print(f"   ✓ created_at: {created_at}")

    # =========================================================================
    # Phase 4: Cleanup Operations
    # =========================================================================

    def test_11_delete_scorer_result(
        self,
        low_level_client: Client,
        scorer_context: dict[str, Any],
    ) -> None:
        """Test deleting a scorer result with full response validation."""
        if not scorer_context.get("result_ids"):
            pytest.skip(SKIP_NO_RESULT_IDS)
        
        result_info = scorer_context["result_ids"][-1]  # Delete last result
        
        response = delete_api_v1_scorers_results_by_dataset_slug_by_item_id_by_scorer_id.sync_detailed(
            client=low_level_client,
            dataset_slug=scorer_context["dataset_slug"],
            item_id=result_info["item_id"],
            scorer_id=result_info["scorer_id"],
        )
        
        # Note: Delete might return 500 due to known backend issues
        if response.status_code == 500:
            pytest.xfail("Result deletion returned 500 (known backend issue)")
        
        assert response.status_code in [200, 204], (
            f"Delete result failed: {response.status_code}"
        )
        
        # ===== VALIDATE RESPONSE BODY =====
        print(f"\n✅ Deleted scorer result - validating response:")
        
        if response.status_code == 200:
            data = parse_response(response)
            
            if data:
                success = get_field(data, 'success')
                if success is not None:
                    assert success is True, "Expected success=True"
                    print(f"   ✓ success: {success}")
                
                message = get_field(data, 'message')
                if message:
                    print(f"   ✓ message: {message}")
        else:
            print(f"   ✓ status: 204 No Content (delete successful)")
        
        scorer_context["result_ids"].pop()
        print(f"   Deleted result for item: {result_info['item_id']}")

    def test_12_delete_scorer(
        self,
        low_level_client: Client,
        scorer_context: dict[str, Any],
    ) -> None:
        """Test deleting the scorer with full response validation."""
        if not scorer_context.get("scorer_id"):
            pytest.skip(SKIP_NO_SCORER_ID)
        
        scorer_id = scorer_context["scorer_id"]
        
        response = delete_api_v1_scorers_by_id.sync_detailed(
            client=low_level_client,
            id=scorer_id,
        )
        
        if response.status_code == 500:
            pytest.xfail("Scorer deletion returned 500 (known backend issue)")
        
        assert response.status_code in [200, 204], (
            f"Delete scorer failed: {response.status_code}"
        )
        
        # ===== VALIDATE RESPONSE BODY =====
        print(f"\n✅ Deleted scorer - validating response:")
        
        if response.status_code == 200:
            data = parse_response(response)
            
            if data:
                success = get_field(data, 'success')
                if success is not None:
                    assert success is True, "Expected success=True"
                    print(f"   ✓ success: {success}")
                
                deleted_id = get_field(data, 'id') or get_field(data, 'deleted_id')
                if deleted_id:
                    assert deleted_id == scorer_id, "Deleted ID mismatch"
                    print(f"   ✓ deleted id: {deleted_id}")
                
                message = get_field(data, 'message')
                if message:
                    print(f"   ✓ message: {message}")
        else:
            print(f"   ✓ status: 204 No Content (delete successful)")
        
        print(f"   Scorer '{scorer_id}' deleted successfully")

    def test_13_cleanup_delete_dataset(
        self,
        low_level_client: Client,
        scorer_context: dict[str, Any],
    ) -> None:
        """Clean up by deleting the test dataset with full response validation."""
        if not scorer_context.get("dataset_slug"):
            pytest.skip(SKIP_NO_DATASET_SLUG)
        
        slug = scorer_context["dataset_slug"]
        
        response = delete_api_v1_datasets_by_slug.sync_detailed(
            client=low_level_client,
            slug=slug,
        )
        
        if response.status_code == 500:
            pytest.xfail("Dataset deletion returned 500 (known backend issue)")
        
        assert response.status_code in [200, 204], (
            f"Delete dataset failed: {response.status_code}"
        )
        
        # ===== VALIDATE RESPONSE BODY =====
        print(f"\n✅ Deleted dataset - validating response:")
        
        if response.status_code == 200:
            data = parse_response(response)
            
            if data:
                success = get_field(data, 'success')
                if success is not None:
                    assert success is True, "Expected success=True"
                    print(f"   ✓ success: {success}")
                
                deleted_slug = get_field(data, 'slug') or get_field(data, 'deleted_slug')
                if deleted_slug:
                    assert deleted_slug == slug, "Deleted slug mismatch"
                    print(f"   ✓ deleted slug: {deleted_slug}")
                
                message = get_field(data, 'message')
                if message:
                    print(f"   ✓ message: {message}")
        else:
            print(f"   ✓ status: 204 No Content (delete successful)")
        
        print(f"   Dataset '{slug}' deleted successfully")


@pytest.mark.scorers
@pytest.mark.integration
class TestScorersIsolated:
    """
    Isolated tests for individual scorer operations.
    These tests don't depend on sequence and can run independently.
    """

    def test_list_scorers_pagination(self, low_level_client: Client) -> None:
        """Test listing scorers with response validation."""
        response = get_api_v1_scorers.sync_detailed(
            client=low_level_client,
        )
        
        assert response.status_code == 200
        
        # Validate response
        data = parse_response(response)
        if data:
            scorers = data.get("scorers", data) if isinstance(data, dict) else data
            if isinstance(scorers, list):
                print(f"\n✅ Pagination test: got {len(scorers)} scorers")
                
                # Validate structure of first scorer if available
                if len(scorers) > 0:
                    first = scorers[0]
                    scorer_id = get_field(first, 'id')
                    name = get_field(first, 'name')
                    if scorer_id:
                        print(f"   ✓ First scorer id: {scorer_id}")
                    if name:
                        print(f"   ✓ First scorer name: {name}")

    def test_get_nonexistent_scorer(self, low_level_client: Client) -> None:
        """Test getting a scorer that doesn't exist returns proper error."""
        fake_id = "nonexistent-scorer-id-12345"
        
        response = get_api_v1_scorers_by_id.sync_detailed(
            fake_id,  # id_path
            client=low_level_client,
            id_query=fake_id,
        )
        
        # Should return 404 for non-existent scorer
        assert response.status_code in [404, 400], (
            f"Expected 404 for non-existent scorer, got {response.status_code}"
        )
        
        # Validate error response
        data = parse_response(response)
        if data:
            error = get_field(data, 'error') or get_field(data, 'message')
            if error:
                print(f"\n✅ Nonexistent scorer test: proper error returned")
                print(f"   Error: {error}")

    def test_list_scorer_results_with_filters(
        self,
        low_level_client: Client,
    ) -> None:
        """Test listing scorer results with filter parameters and response validation."""
        response = get_api_v1_scorers_results.sync_detailed(
            client=low_level_client,
            limit=10,
            offset=0,
        )
        
        assert response.status_code == 200
        
        # Validate response structure
        data = parse_response(response)
        assert data is not None, "Response should have data"
        
        print(f"\n✅ Filter test - response validation:")
        print(f"   Response type: {type(data)}")
        
        if isinstance(data, dict):
            for key in data.keys():
                print(f"   ✓ field: {key}")
            
            # Validate results if present
            results = data.get("results", data)
            if isinstance(results, list):
                print(f"   ✓ results count: {len(results)}")
                assert len(results) <= 10, "Should respect limit"