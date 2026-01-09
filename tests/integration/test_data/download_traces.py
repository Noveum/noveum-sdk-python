#!/usr/bin/env python3
"""
Download traces from Noveum API and save to traces.json.

This script fetches traces from the Noveum API with the specified filters
and saves them to Test_NovaBotDatasets-Demo/Data/traces.json.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import requests


def repo_root() -> Path:
    """Get the repository root directory."""
    return Path(__file__).resolve().parents[2]


def main() -> int:
    """Download traces from Noveum API."""
    # API configuration
    api_token = "nv_5Ib0BtGFqRKzpVIiHRw1o0fIUiTXUGYJ"
    environment = "dev-novabot"
    api_url = "https://testapp.noveum.ai/api/v1/traces"

    # Output path
    output_path = repo_root() / "Test_NovaBotDatasets-Demo" / "Data" / "traces_testing.json"

    # API parameters - only include non-empty values
    params = {
        "from": "0",
        "size": "100",
        "environment": environment,
        "sort": "start_time:desc",
        "includeSpans": "false",
    }

    # Headers
    headers = {
        "Authorization": f"Bearer {api_token}",
    }

    # Cookies
    cookies = {
        "apiKeyCookie": api_token,
    }

    print(f"🔍 Fetching traces from Noveum API (environment: {environment})...")

    try:
        response = requests.get(
            api_url,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=30,
        )
        response.raise_for_status()

        # Parse JSON response
        data = response.json()

        # Ensure output directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Write to file
        output_path.write_text(
            json.dumps(data, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

        print("✅ Successfully downloaded traces")
        print(f"✅ Saved to {output_path}")

        # Print summary if available
        if isinstance(data, dict):
            if "traces" in data:
                trace_count = len(data["traces"])
                print(f"📊 Found {trace_count} trace(s)")
                if "pagination" in data:
                    pagination = data["pagination"]
                    print(f"   Total available: {pagination.get('total', 'unknown')}")
                    print(f"   Has more: {pagination.get('has_more', False)}")
            elif "data" in data:
                traces = data.get("data", [])
                if isinstance(traces, list):
                    print(f"📊 Found {len(traces)} trace(s)")

        return 0

    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching traces: {e}", file=sys.stderr)
        if hasattr(e, "response") and e.response is not None:
            print(f"   Response status: {e.response.status_code}", file=sys.stderr)
            print(f"   Response body: {e.response.text[:500]}", file=sys.stderr)
        return 1
    except json.JSONDecodeError as e:
        print(f"❌ Error parsing JSON response: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"❌ Unexpected error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
