#!/usr/bin/env python3
"""
Upload scorer results to Noveum API.

This script reads the scorer_results_dataset.json file and uploads scorer results
to the Noveum API using the batch scorer results endpoint.
"""

from __future__ import annotations

import contextlib
import json
import sys
import time
from pathlib import Path
from typing import Any

import requests


def repo_root() -> Path:
    """Get the repository root directory."""
    return Path(__file__).resolve().parents[2]


def transform_scorer_result_for_api(
    result: dict[str, Any],
    dataset_slug: str,
) -> dict[str, Any]:
    """Transform scorer result to API format."""
    # Parse metadata if it's a JSON string
    metadata = result.get("metadata", {})
    if isinstance(metadata, str):
        try:
            metadata = json.loads(metadata)
        except (json.JSONDecodeError, ValueError):
            metadata = {}
    elif not isinstance(metadata, dict):
        metadata = {}

    # Convert passed from int (0/1) to boolean
    passed = result.get("passed", False)
    if isinstance(passed, int):
        passed = bool(passed)

    # Build API result
    api_result = {
        "datasetSlug": dataset_slug,
        "itemId": result.get("item_id", ""),
        "scorerId": result.get("scorer_id", ""),
        "score": float(result.get("score", 0.0)),
        "passed": passed,
        "metadata": metadata,
        "error": result.get("error", ""),
        "executionTimeMs": int(result.get("execution_time_ms", 0)),
    }

    return api_result


def upload_results_batch(
    api_url: str,
    api_token: str,
    results: list[dict[str, Any]],
    batch_num: int,
    total_batches: int,
    organization_slug: str = "",
) -> bool:
    """Upload a batch of scorer results to the API."""
    payload = {"results": results}

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_token}",
    }

    cookies = {
        "apiKeyCookie": api_token,
    }

    # Add organization slug as query parameter if provided
    request_url = api_url
    if organization_slug:
        if "?" in request_url:
            request_url = f"{request_url}&organizationSlug={organization_slug}"
        else:
            request_url = f"{request_url}?organizationSlug={organization_slug}"

    try:
        print(f"📤 Uploading batch {batch_num}/{total_batches} ({len(results)} results)...")
        response = requests.post(
            request_url,
            json=payload,
            headers=headers,
            cookies=cookies,
            timeout=60,
        )
        response.raise_for_status()

        # Check if response is successful (201 Created)
        if response.status_code == 201:
            print(f"✅ Batch {batch_num} uploaded successfully")
            return True
        else:
            print(f"❌ Batch {batch_num} failed: Status {response.status_code}")
            try:
                result = response.json()
                print(f"   Response: {result}")
            except Exception:
                print(f"   Response body: {response.text[:500]}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"❌ Error uploading batch {batch_num}: {e}")
        if hasattr(e, "response") and e.response is not None:
            print(f"   Response status: {e.response.status_code}")
            with contextlib.suppress(Exception):
                print(f"   Response body: {e.response.text[:500]}")
        return False


def main() -> int:
    """Upload scorer results to Noveum API."""
    # Configuration
    api_token = "nv_5Ib0BtGFqRKzpVIiHRw1o0fIUiTXUGYJ"
    dataset_slug = "awstestingscores"
    organization_slug = "aws_testing"
    api_url = "https://testapp.noveum.ai/api/v1/scorers/results/batch"

    # Paths
    scorer_results_path = repo_root() / "Test_NovaBotDatasets-Demo" / "Data" / "scorer_results_dataset_new.json"

    print(f"📖 Reading scorer results from {scorer_results_path}...")

    try:
        with open(scorer_results_path, encoding="utf-8") as f:
            dataset = json.load(f)
    except Exception as e:
        print(f"❌ Error reading scorer results file: {e}", file=sys.stderr)
        return 1

    # Extract all scorer results from the dataset
    # The dataset structure: list of items, each item has a "scorer_results" array
    all_results = []
    items = dataset if isinstance(dataset, list) else dataset.get("items", [])

    for item in items:
        scorer_results = item.get("scorer_results", [])
        for result in scorer_results:
            all_results.append(result)

    total_results = len(all_results)

    if total_results == 0:
        print("❌ No scorer results found in dataset", file=sys.stderr)
        return 1

    print(f"📊 Found {total_results} scorer results to upload")
    print(f"🔗 API URL: {api_url}")
    print(f"📦 Dataset: {dataset_slug}")
    print(f"🏢 Organization: {organization_slug}")

    # Transform results to API format
    print("🔄 Transforming results to API format...")
    api_results = []
    for i, result in enumerate(all_results):
        try:
            api_result = transform_scorer_result_for_api(result, dataset_slug)
            api_results.append(api_result)
        except Exception as e:
            print(f"⚠️  Error transforming result {i+1}: {e}")
            continue

    print(f"✅ Transformed {len(api_results)} results")

    # Upload in batches (API limit: max 100 per batch)
    batch_size = 100
    total_batches = (len(api_results) + batch_size - 1) // batch_size

    print(f"\n📤 Uploading {len(api_results)} results in {total_batches} batches...")

    success_count = 0
    failed_count = 0

    for i in range(0, len(api_results), batch_size):
        batch = api_results[i : i + batch_size]
        batch_num = (i // batch_size) + 1

        if upload_results_batch(api_url, api_token, batch, batch_num, total_batches, organization_slug):
            success_count += len(batch)
        else:
            failed_count += len(batch)

        # Small delay between batches to avoid rate limiting
        if i + batch_size < len(api_results):
            time.sleep(0.5)

    print("\n📊 Upload Summary:")
    print(f"   ✅ Successfully uploaded: {success_count} results")
    print(f"   ❌ Failed: {failed_count} results")
    print(f"   📈 Total: {len(api_results)} results")

    if failed_count > 0:
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
