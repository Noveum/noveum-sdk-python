#!/usr/bin/env python3
"""
Upload conversation dataset items to Noveum API.

This script reads the conversation_dataset.json file and uploads items
to the Noveum API using the dataset items endpoint.
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


def transform_item_for_api(item: dict[str, Any]) -> dict[str, Any]:
    """Transform dataset item to API format."""

    # Parse JSON strings to objects
    def parse_json_field(field: Any) -> Any:
        if isinstance(field, str):
            try:
                return json.loads(field)
            except (json.JSONDecodeError, ValueError):
                return field
        return field

    # Parse conversation_context
    # UI expects: JSON string that parses to an array directly: '[{speaker: "human", message: "..."}, ...]'
    # The UI code does: JSON.parse(item.conversation_context) and expects Array.isArray() to be true
    # API validation requires: object format in content.conversation_context
    # Solution: Send as object for API validation, but the API should store it at top level as JSON string
    conversation_context_raw = parse_json_field(item.get("conversation_context", []))
    if isinstance(conversation_context_raw, list):
        # This is the array format the UI expects
        conversation_context_array = conversation_context_raw
    elif isinstance(conversation_context_raw, dict):
        # If it's already an object with "messages" key, extract the array
        if "messages" in conversation_context_raw:
            conversation_context_array = conversation_context_raw["messages"]
        else:
            conversation_context_array = []
    else:
        conversation_context_array = []

    # API requires object format for validation in content.conversation_context
    # But the UI reads conversation_context at top level and expects it to be a JSON string of array
    # The API should transform the object to a JSON string at top level
    # For now, send as object to pass validation - the API backend should handle the transformation
    conversation_context = {"messages": conversation_context_array}

    # Extract content fields
    content = {
        "agent_name": item.get("agent_name", ""),
        "agent_role": item.get("agent_role", ""),
        "agent_task": item.get("agent_task", ""),
        "agent_response": item.get("agent_response", ""),
        "system_prompt": item.get("system_prompt", ""),
        "user_id": item.get("user_id", ""),
        "session_id": item.get("session_id", ""),
        "turn_id": item.get("turn_id", ""),
        "ground_truth": item.get("ground_truth", ""),
        "expected_tool_call": item.get("expected_tool_call", ""),
        "tools_available": parse_json_field(item.get("tools_available", [])),
        "tool_calls": parse_json_field(item.get("tool_calls", [])),
        "tool_call_results": parse_json_field(item.get("tool_call_results", [])),
        "parameters_passed": parse_json_field(item.get("parameters_passed", {})),
        "retrieval_query": parse_json_field(item.get("retrieval_query", [])),
        "retrieved_context": parse_json_field(item.get("retrieved_context", [])),
        "exit_status": item.get("exit_status", ""),
        "agent_exit": item.get("agent_exit", ""),
        "trace_data": parse_json_field(item.get("trace_data", {})),
        "conversation_id": item.get("conversation_id", ""),
        "speaker": item.get("speaker", ""),
        "message": item.get("message", ""),
        # API requires object format for validation: {"messages": [...]}
        # UI expects JSON string that parses to array: '[{speaker: "human", message: "..."}, ...]'
        # The API backend should transform the object to array when storing at top level
        # For now, send as object to pass validation - API/UI compatibility issue needs backend fix
        "conversation_context": conversation_context,
        "input_text": item.get("input_text", ""),
        "output_text": item.get("output_text", ""),
        "expected_output": item.get("expected_output", ""),
        "evaluation_context": parse_json_field(item.get("evaluation_context", {})),
        "criteria": item.get("criteria", ""),
        "quality_score": item.get("quality_score", 0),
        "validation_status": item.get("validation_status", ""),
        "validation_errors": parse_json_field(item.get("validation_errors", [])),
        "tags": parse_json_field(item.get("tags", [])),
        "custom_attributes": parse_json_field(item.get("custom_attributes", {})),
    }

    # Extract metadata
    metadata = parse_json_field(item.get("metadata", {}))

    # Build API item
    api_item = {
        "item_id": item.get("item_id", ""),
        "item_type": item.get("item_type", "conversational"),
        "content": content,
        "metadata": metadata,
        "trace_id": item.get("source_trace_id", ""),
        "span_id": item.get("source_span_id", ""),
    }

    return api_item


def upload_items_batch(
    api_url: str,
    api_token: str,
    items: list[dict[str, Any]],
    batch_num: int,
    total_batches: int,
    organization_slug: str = "",
) -> bool:
    """Upload a batch of items to the API."""
    payload = {"items": items}

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_token}",
    }

    cookies = {
        "apiKeyCookie": api_token,
    }

    # Add organization slug as query parameter if provided
    if organization_slug:
        if "?" in api_url:
            api_url = f"{api_url}&organizationSlug={organization_slug}"
        else:
            api_url = f"{api_url}?organizationSlug={organization_slug}"

    try:
        print(f"📤 Uploading batch {batch_num}/{total_batches} ({len(items)} items)...")
        response = requests.post(
            api_url,
            json=payload,
            headers=headers,
            cookies=cookies,
            timeout=60,
        )
        response.raise_for_status()

        result = response.json()
        if result.get("success", False):
            print(f"✅ Batch {batch_num} uploaded successfully")
            return True
        else:
            print(f"❌ Batch {batch_num} failed: {result.get('error', 'Unknown error')}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"❌ Error uploading batch {batch_num}: {e}")
        if hasattr(e, "response") and e.response is not None:
            print(f"   Response status: {e.response.status_code}")
            with contextlib.suppress(Exception):
                print(f"   Response body: {e.response.text[:500]}")
        return False


def main() -> int:
    """Upload dataset items to Noveum API."""
    # Configuration
    api_token = "nv_5Ib0BtGFqRKzpVIiHRw1o0fIUiTXUGYJ"
    dataset_slug = "awstestingscores"
    organization_slug = "aws_testing"
    api_url = f"https://testapp.noveum.ai/api/v1/datasets/{dataset_slug}/items"

    # Paths
    dataset_path = repo_root() / "Test_NovaBotDatasets-Demo" / "Data" / "conversation_dataset.json"

    print(f"📖 Reading dataset from {dataset_path}...")

    try:
        with open(dataset_path, encoding="utf-8") as f:
            dataset = json.load(f)
    except Exception as e:
        print(f"❌ Error reading dataset file: {e}", file=sys.stderr)
        return 1

    items = dataset.get("items", [])
    total_items = len(items)

    if total_items == 0:
        print("❌ No items found in dataset", file=sys.stderr)
        return 1

    print(f"📊 Found {total_items} items to upload")
    print(f"🔗 API URL: {api_url}")

    # Transform items to API format
    print("🔄 Transforming items to API format...")
    api_items = []
    for i, item in enumerate(items):
        try:
            api_item = transform_item_for_api(item)
            api_items.append(api_item)
        except Exception as e:
            print(f"⚠️  Error transforming item {i+1}: {e}")
            continue

    print(f"✅ Transformed {len(api_items)} items")

    # Upload in batches (API might have limits)
    batch_size = 10  # Adjust based on API limits
    total_batches = (len(api_items) + batch_size - 1) // batch_size

    print(f"\n📤 Uploading {len(api_items)} items in {total_batches} batches...")

    success_count = 0
    failed_count = 0

    for i in range(0, len(api_items), batch_size):
        batch = api_items[i : i + batch_size]
        batch_num = (i // batch_size) + 1

        if upload_items_batch(api_url, api_token, batch, batch_num, total_batches, organization_slug):
            success_count += len(batch)
        else:
            failed_count += len(batch)

        # Small delay between batches to avoid rate limiting
        if i + batch_size < len(api_items):
            time.sleep(0.5)

    print("\n📊 Upload Summary:")
    print(f"   ✅ Successfully uploaded: {success_count} items")
    print(f"   ❌ Failed: {failed_count} items")
    print(f"   📈 Total: {len(api_items)} items")

    if failed_count > 0:
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
