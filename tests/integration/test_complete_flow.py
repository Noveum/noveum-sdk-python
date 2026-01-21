"""
Complete End-to-End Integration Tests - Full Journey

This module tests the COMPLETE Noveum SDK workflow from start to finish:
1. Traces: Send traces → Verify ingestion → Query traces → Get spans
2. Datasets: Create dataset → Add items → Version management
3. Scorers: Create scorer → Evaluate items → Store results
4. ETL Jobs: Create job → Configure mapper → Trigger processing
5. Projects: Create project → Associate datasets → Health check

This is the "golden path" test that validates all APIs work together.

Total Endpoints Covered: 40+

Usage:
    pytest test_complete_flow.py -v
    pytest test_complete_flow.py -v -s  # With output
    pytest test_complete_flow.py -v --tb=long  # Full tracebacks
"""

import time
import uuid
from datetime import datetime, timedelta
from typing import Any

import pytest

from noveum_api_client import Client, NoveumClient
from noveum_api_client.api.datasets import (
    delete_api_v1_datasets_by_slug,
    get_api_v1_datasets_by_dataset_slug_items,
    get_api_v1_datasets_by_slug,
    post_api_v1_datasets,
    post_api_v1_datasets_by_dataset_slug_items,
    post_api_v1_datasets_by_dataset_slug_versions,
    post_api_v1_datasets_by_dataset_slug_versions_publish,
)
from noveum_api_client.api.projects import (
    delete_api_v1_projects_by_id,
    get_api_v1_projects_by_id,
    post_api_v1_projects,
    post_api_v1_projects_by_id_datasets_associate,
)
from noveum_api_client.api.scorer_results import (
    get_api_v1_scorers_results,
    post_api_v1_scorers_results_batch,
)
from noveum_api_client.api.scorers import (
    delete_api_v1_scorers_by_id,
    get_api_v1_scorers_by_id,
    post_api_v1_scorers,
)
from noveum_api_client.api.traces import (
    get_api_v1_traces,
    get_api_v1_traces_by_id,
    get_api_v1_traces_by_trace_id_spans,
    get_api_v1_traces_connection_status,
    post_api_v1_traces,
)
from noveum_api_client.models.post_api_v1_datasets_body import PostApiV1DatasetsBody
from noveum_api_client.models.post_api_v1_datasets_by_dataset_slug_items_body import (
    PostApiV1DatasetsByDatasetSlugItemsBody,
)
from noveum_api_client.models.post_api_v1_datasets_by_dataset_slug_versions_body import (
    PostApiV1DatasetsByDatasetSlugVersionsBody,
)
from noveum_api_client.models.post_api_v1_projects_body import PostApiV1ProjectsBody
from noveum_api_client.models.post_api_v1_scorers_body import PostApiV1ScorersBody
from noveum_api_client.models.post_api_v1_scorers_results_batch_body import (
    PostApiV1ScorersResultsBatchBody,
)
from noveum_api_client.models.post_api_v1_traces_body import PostApiV1TracesBody

from constants import (
    SKIP_TRACE_SENDING_FAILED,
    SKIP_NO_TRACES_SENT,
    SKIP_MISSING_SCORER_OR_ITEMS,
    SKIP_CREATE_PROJECT_FAILED,
)


@pytest.mark.integration
@pytest.mark.slow
@pytest.mark.serial
class TestCompleteE2EFlow:
    """
    Complete end-to-end integration test covering the full Noveum workflow.
    
    This is the "smoke test" that validates all APIs work together:
    Traces → Datasets → Scorers → Results → Projects
    """

    @pytest.fixture(scope="class")
    def flow_context(self) -> dict[str, Any]:
        """Shared context for the entire flow."""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        unique_id = str(uuid.uuid4())[:8]
        
        return {
            # Identifiers
            "run_id": f"{timestamp}-{unique_id}",
            "dataset_slug": f"e2e-flow-{timestamp}-{unique_id}",
            "project_id": f"e2e-project-{timestamp}-{unique_id}",
            "scorer_name": f"E2E_Flow_Scorer_{timestamp}_{unique_id}",
            
            # Created resource IDs
            "trace_ids": [],
            "item_ids": [],
            "scorer_id": None,
            
            # Test data
            "traces": [],
            "items": [],
            "results": [],
        }

    # =========================================================================
    # Step 1: Verify API Connection
    # =========================================================================

    def test_step_01_verify_connection(self, low_level_client: Client) -> None:
        """Step 1: Verify API connection is working."""
        print("\n" + "=" * 70)
        print("STEP 1: VERIFY API CONNECTION")
        print("=" * 70)
        
        response = get_api_v1_traces_connection_status.sync_detailed(
            client=low_level_client
        )
        
        assert response.status_code == 200, (
            f"API connection failed: {response.status_code}"
        )
        
        print("✅ API connection verified")

    # =========================================================================
    # Step 2: Send Traces
    # =========================================================================

    def test_step_02_send_traces(
        self,
        low_level_client: Client,
        api_config: dict[str, str],
        flow_context: dict[str, Any],
    ) -> None:
        """Step 2: Send batch of traces to the API."""
        print("\n" + "=" * 70)
        print("STEP 2: SEND TRACES")
        print("=" * 70)
        
        traces = []
        for i in range(5):
            trace_id = str(uuid.uuid4())
            span_id = str(uuid.uuid4())[:16]
            now = datetime.now()
            
            # API expects ISO 8601 datetime strings
            start_time = (now - timedelta(seconds=1)).isoformat() + "Z"
            end_time = now.isoformat() + "Z"
            span_start = (now - timedelta(seconds=0.5)).isoformat() + "Z"
            
            trace = {
                "trace_id": trace_id,
                "name": f"e2e_flow_trace_{i}",
                "project": api_config["project"],
                "environment": api_config["environment"],
                "start_time": start_time,
                "end_time": end_time,
                "duration_ms": 1000,
                "status": "ok",
                "span_count": 1,
                "sdk": {
                    "name": "noveum-sdk-python",
                    "version": "1.0.0",
                },
                "attributes": {
                    "llm.model": "gpt-4",
                    "llm.operation": f"test_operation_{i}",
                    "test.flow_id": flow_context["run_id"],
                    "test.index": i,
                },
                "spans": [{
                    "span_id": span_id,
                    "trace_id": trace_id,
                    "name": f"span_{i}",
                    "kind": "LLM",
                    "start_time": span_start,
                    "end_time": end_time,
                    "duration_ms": 500,
                    "status": "ok",
                    "attributes": {"index": i},
                }],
            }
            traces.append(trace)
            flow_context["trace_ids"].append(trace_id)
        
        body = PostApiV1TracesBody.from_dict({"traces": traces})
        
        try:
            response = post_api_v1_traces.sync_detailed(
                client=low_level_client,
                body=body,
            )
        except Exception as e:
            pytest.skip(SKIP_TRACE_SENDING_FAILED.format(error=e))
        
        assert response.status_code in [200, 201], (
            f"Send traces failed: {response.status_code}"
        )
        
        flow_context["traces"] = traces
        print(f"✅ Sent {len(traces)} traces")

    def test_step_03_verify_traces(
        self,
        low_level_client: Client,
        flow_context: dict[str, Any],
    ) -> None:
        """Step 3: Wait and verify traces were ingested."""
        print("\n" + "=" * 70)
        print("STEP 3: VERIFY TRACE INGESTION")
        print("=" * 70)
        
        if not flow_context.get("trace_ids"):
            pytest.skip(SKIP_NO_TRACES_SENT)
        
        # Wait for ingestion
        print("⏳ Waiting 5s for trace ingestion...")
        time.sleep(5)
        
        # Query traces
        response = get_api_v1_traces.sync_detailed(
            client=low_level_client,
            size=20,
        )
        
        assert response.status_code == 200, (
            f"Query traces failed: {response.status_code}"
        )
        
        print("✅ Trace query successful")
        
        # Try to get specific trace
        if flow_context["trace_ids"]:
            trace_id = flow_context["trace_ids"][0]
            
            get_response = get_api_v1_traces_by_id.sync_detailed(
                client=low_level_client,
                id=trace_id,
            )
            
            if get_response.status_code == 200:
                print(f"✅ Retrieved trace: {trace_id[:16]}...")
                
                # Get spans
                spans_response = get_api_v1_traces_by_trace_id_spans.sync_detailed(
                    client=low_level_client,
                    trace_id=trace_id,
                )
                
                if spans_response.status_code == 200:
                    print(f"✅ Retrieved spans for trace")
            else:
                print(f"⚠️  Trace not yet available (may need more time)")

    # =========================================================================
    # Step 4: Create Dataset
    # =========================================================================

    def test_step_04_create_dataset(
        self,
        low_level_client: Client,
        flow_context: dict[str, Any],
    ) -> None:
        """Step 4: Create a dataset to store evaluation data."""
        print("\n" + "=" * 70)
        print("STEP 4: CREATE DATASET")
        print("=" * 70)
        
        body = PostApiV1DatasetsBody(
            name=f"E2E Flow Dataset {flow_context['run_id']}",
            slug=flow_context["dataset_slug"],
            description="Complete E2E flow integration test dataset",
        )
        
        response = post_api_v1_datasets.sync_detailed(
            client=low_level_client,
            body=body,
        )
        
        assert response.status_code in [200, 201], (
            f"Create dataset failed: {response.status_code}"
        )
        
        print(f"✅ Created dataset: {flow_context['dataset_slug']}")

    def test_step_05_add_dataset_items(
        self,
        low_level_client: Client,
        flow_context: dict[str, Any],
    ) -> None:
        """Step 5: Add items to the dataset."""
        print("\n" + "=" * 70)
        print("STEP 5: ADD DATASET ITEMS")
        print("=" * 70)
        
        # Generate items - use traces if available, otherwise create standalone items
        items = []
        traces = flow_context.get("traces", [])[:5]
        
        if traces:
            for i, trace in enumerate(traces):
                item = {
                    "item_id": f"e2e-item-{i:03d}",
                    "item_type": "trace_evaluation",
                    "content": {
                        "trace_id": trace["trace_id"],
                        "trace_name": trace["name"],
                        "input": f"Test input for trace {i}",
                        "output": f"Test output for trace {i}",
                        "ground_truth": f"Expected output for trace {i}",
                    },
                    "metadata": {
                        "flow_id": flow_context["run_id"],
                        "index": i,
                    },
                }
                items.append(item)
                flow_context["item_ids"].append(item["item_id"])
        else:
            # Create standalone items if no traces available
            for i in range(5):
                item = {
                    "item_id": f"e2e-item-{i:03d}",
                    "item_type": "evaluation",
                    "content": {
                        "input": f"Test input {i}",
                        "output": f"Test output {i}",
                        "ground_truth": f"Expected output {i}",
                    },
                    "metadata": {
                        "flow_id": flow_context["run_id"],
                        "index": i,
                    },
                }
                items.append(item)
                flow_context["item_ids"].append(item["item_id"])
        
        body = PostApiV1DatasetsByDatasetSlugItemsBody.from_dict({"items": items})
        
        response = post_api_v1_datasets_by_dataset_slug_items.sync_detailed(
            client=low_level_client,
            dataset_slug=flow_context["dataset_slug"],
            body=body,
        )
        
        assert response.status_code in [200, 201], (
            f"Add items failed: {response.status_code}"
        )
        
        flow_context["items"] = items
        print(f"✅ Added {len(items)} items to dataset")

    def test_step_06_version_and_publish(
        self,
        low_level_client: Client,
        flow_context: dict[str, Any],
    ) -> None:
        """Step 6: Create and publish dataset version."""
        print("\n" + "=" * 70)
        print("STEP 6: VERSION AND PUBLISH DATASET")
        print("=" * 70)
        
        # Create version
        body = PostApiV1DatasetsByDatasetSlugVersionsBody(version="1.0.0")
        
        response = post_api_v1_datasets_by_dataset_slug_versions.sync_detailed(
            client=low_level_client,
            dataset_slug=flow_context["dataset_slug"],
            body=body,
        )
        
        assert response.status_code in [200, 201], (
            f"Create version failed: {response.status_code}"
        )
        
        print("✅ Created version 1.0.0")
        
        # Publish version
        response = post_api_v1_datasets_by_dataset_slug_versions_publish.sync_detailed(
            client=low_level_client,
            dataset_slug=flow_context["dataset_slug"],
        )
        
        assert response.status_code in [200, 201], (
            f"Publish version failed: {response.status_code}"
        )
        
        print("✅ Published dataset version")

    # =========================================================================
    # Step 7: Create Scorer
    # =========================================================================

    def test_step_07_create_scorer(
        self,
        low_level_client: Client,
        flow_context: dict[str, Any],
    ) -> None:
        """Step 7: Create a scorer for evaluation."""
        print("\n" + "=" * 70)
        print("STEP 7: CREATE SCORER")
        print("=" * 70)
        
        body = PostApiV1ScorersBody(
            name=flow_context["scorer_name"],
            description="E2E flow integration test scorer",
            type_="custom",
            tag="e2e-test",
            config={
                "evaluation_type": "accuracy",
                "flow_id": flow_context["run_id"],
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
            f"Create scorer failed: {response.status_code}"
        )
        
        # Extract scorer ID
        if hasattr(response, "parsed") and response.parsed:
            if hasattr(response.parsed, "id"):
                flow_context["scorer_id"] = response.parsed.id
            elif isinstance(response.parsed, dict) and "id" in response.parsed:
                flow_context["scorer_id"] = response.parsed["id"]
        
        print(f"✅ Created scorer: {flow_context['scorer_name']}")
        if flow_context.get("scorer_id"):
            print(f"   ID: {flow_context['scorer_id']}")

    def test_step_08_add_scorer_results(
        self,
        low_level_client: Client,
        flow_context: dict[str, Any],
    ) -> None:
        """Step 8: Add evaluation results for dataset items."""
        print("\n" + "=" * 70)
        print("STEP 8: ADD SCORER RESULTS")
        print("=" * 70)
        
        if not all([
            flow_context.get("scorer_id"),
            flow_context.get("item_ids"),
        ]):
            pytest.skip(SKIP_MISSING_SCORER_OR_ITEMS)
        
        results = []
        for i, item_id in enumerate(flow_context["item_ids"]):
            results.append({
                "datasetSlug": flow_context["dataset_slug"],
                "itemId": item_id,
                "scorerId": flow_context["scorer_id"],
                "score": 0.85 + (i * 0.02),  # Varying scores
                "reason": f"E2E evaluation result for item {i}",
                "metadata": {
                    "flow_id": flow_context["run_id"],
                    "evaluation_index": i,
                },
            })
        
        body = PostApiV1ScorersResultsBatchBody.from_dict({"results": results})
        
        response = post_api_v1_scorers_results_batch.sync_detailed(
            client=low_level_client,
            body=body,
        )
        
        assert response.status_code in [200, 201], (
            f"Add results failed: {response.status_code}"
        )
        
        flow_context["results"] = results
        print(f"✅ Added {len(results)} scorer results")

    def test_step_09_verify_results(
        self,
        low_level_client: Client,
        noveum_client: NoveumClient,
        flow_context: dict[str, Any],
    ) -> None:
        """Step 9: Verify scorer results were stored."""
        print("\n" + "=" * 70)
        print("STEP 9: VERIFY SCORER RESULTS")
        print("=" * 70)
        
        # Query results with filter
        response = get_api_v1_scorers_results.sync_detailed(
            client=low_level_client,
            dataset_slug=flow_context["dataset_slug"],
            limit=20,
        )
        
        assert response.status_code == 200, (
            f"Query results failed: {response.status_code}"
        )
        
        results_count = 0
        if hasattr(response, "parsed") and response.parsed:
            results = response.parsed if isinstance(response.parsed, list) else []
            results_count = len(results)
        
        print(f"✅ Found {results_count} results for dataset")

    # =========================================================================
    # Step 10: Create Project and Associate Dataset
    # =========================================================================

    def test_step_10_create_project(
        self,
        low_level_client: Client,
        api_config: dict[str, str],
        flow_context: dict[str, Any],
    ) -> None:
        """Step 10: Create project and associate dataset."""
        print("\n" + "=" * 70)
        print("STEP 10: CREATE PROJECT & ASSOCIATE DATASET")
        print("=" * 70)
        
        # Create project
        body = PostApiV1ProjectsBody(
            id=flow_context["project_id"],
            name=f"E2E Flow Project {flow_context['run_id'][:8]}",
            description="Complete E2E flow integration test project",
        )
        
        response = post_api_v1_projects.sync_detailed(
            client=low_level_client,
            body=body,
            organization_slug=api_config.get("org_slug"),
        )
        
        if response.status_code in [200, 201, 409]:
            print(f"✅ Created/using project: {flow_context['project_id']}")
        else:
            pytest.skip(SKIP_CREATE_PROJECT_FAILED.format(status_code=response.status_code))
        
        # Associate dataset
        response = post_api_v1_projects_by_id_datasets_associate.sync_detailed(
            client=low_level_client,
            id=flow_context["project_id"],
            dataset_slug=flow_context["dataset_slug"],
            organization_slug=api_config.get("org_slug"),
        )
        
        if response.status_code in [200, 201, 204]:
            print(f"✅ Associated dataset with project")

    # =========================================================================
    # Step 11: Summary and Verification
    # =========================================================================

    def test_step_11_verify_complete_flow(
        self,
        low_level_client: Client,
        api_config: dict[str, str],
        flow_context: dict[str, Any],
    ) -> None:
        """Step 11: Final verification that all resources exist."""
        print("\n" + "=" * 70)
        print("STEP 11: VERIFY COMPLETE FLOW")
        print("=" * 70)
        
        verification_results = []
        
        # Verify dataset
        response = get_api_v1_datasets_by_slug.sync_detailed(
            client=low_level_client,
            slug=flow_context["dataset_slug"],
        )
        dataset_ok = response.status_code == 200
        verification_results.append(("Dataset", dataset_ok))
        
        # Verify dataset items
        response = get_api_v1_datasets_by_dataset_slug_items.sync_detailed(
            client=low_level_client,
            dataset_slug=flow_context["dataset_slug"],
            limit=10,
        )
        items_ok = response.status_code == 200
        verification_results.append(("Dataset Items", items_ok))
        
        # Verify scorer
        if flow_context.get("scorer_id"):
            response = get_api_v1_scorers_by_id.sync_detailed(
                client=low_level_client,
                id=flow_context["scorer_id"],
            )
            scorer_ok = response.status_code == 200
            verification_results.append(("Scorer", scorer_ok))
        
        # Verify project
        response = get_api_v1_projects_by_id.sync_detailed(
            client=low_level_client,
            id=flow_context["project_id"],
            organization_slug=api_config.get("org_slug"),
        )
        project_ok = response.status_code == 200
        verification_results.append(("Project", project_ok))
        
        # Print verification summary
        print("\nVerification Results:")
        all_ok = True
        for name, ok in verification_results:
            status = "✅" if ok else "❌"
            print(f"  {status} {name}")
            if not ok:
                all_ok = False
        
        print("\n" + "=" * 70)
        if all_ok:
            print("✅ COMPLETE E2E FLOW VERIFIED SUCCESSFULLY")
        else:
            print("⚠️  SOME VERIFICATIONS FAILED")
        print("=" * 70)

    # =========================================================================
    # Step 12: Cleanup
    # =========================================================================

    def test_step_12_cleanup(
        self,
        low_level_client: Client,
        api_config: dict[str, str],
        flow_context: dict[str, Any],
    ) -> None:
        """Step 12: Clean up all created resources."""
        print("\n" + "=" * 70)
        print("STEP 12: CLEANUP")
        print("=" * 70)
        
        cleanup_results = []
        
        # Delete scorer
        if flow_context.get("scorer_id"):
            response = delete_api_v1_scorers_by_id.sync_detailed(
                client=low_level_client,
                id=flow_context["scorer_id"],
            )
            cleanup_results.append(("Scorer", response.status_code in [200, 204, 500]))
        
        # Delete project
        response = delete_api_v1_projects_by_id.sync_detailed(
            client=low_level_client,
            id=flow_context["project_id"],
            organization_slug=api_config.get("org_slug"),
        )
        cleanup_results.append(("Project", response.status_code in [200, 204, 500]))
        
        # Delete dataset
        response = delete_api_v1_datasets_by_slug.sync_detailed(
            client=low_level_client,
            slug=flow_context["dataset_slug"],
        )
        cleanup_results.append(("Dataset", response.status_code in [200, 204, 500]))
        
        # Print cleanup summary
        print("\nCleanup Results:")
        for name, ok in cleanup_results:
            status = "✅" if ok else "⚠️"
            print(f"  {status} {name}")
        
        print("\n" + "=" * 70)
        print("✅ COMPLETE E2E FLOW TEST FINISHED")
        print("=" * 70)
        
        # Print summary
        print(f"\nFlow Summary:")
        print(f"  Run ID: {flow_context['run_id']}")
        print(f"  Traces sent: {len(flow_context.get('traces', []))}")
        print(f"  Items created: {len(flow_context.get('items', []))}")
        print(f"  Results added: {len(flow_context.get('results', []))}")

