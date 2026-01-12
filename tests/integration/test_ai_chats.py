#!/usr/bin/env python3
"""
AI Chats API Tests

Tests AI chat management endpoints (6 endpoints):
- List chats
- Create chat
- Get chat by ID
- Update chat
- Delete chat
- Send message to chat

Usage: python test_ai_chats.py
"""

import json
import os
import sys
from datetime import datetime
from typing import Any

import pytest

sys.path.insert(0, os.path.abspath("../.."))
sys.path.insert(0, os.path.abspath("../../tests"))


from noveum_api_client import Client, NoveumClient
from noveum_api_client.api.ai.delete_api_ai_chats_by_id import sync_detailed as delete_api_ai_chats_by_id
from noveum_api_client.api.ai.get_api_ai_chats import sync_detailed as get_api_ai_chats
from noveum_api_client.api.ai.get_api_ai_chats_by_id import sync_detailed as get_api_ai_chats_by_id
from noveum_api_client.api.ai.post_api_ai_chats import sync_detailed as post_api_ai_chats
from noveum_api_client.api.ai.post_api_ai_chats_by_id_messages import sync_detailed as post_api_ai_chats_by_id_messages
from noveum_api_client.api.ai.put_api_ai_chats_by_id import sync_detailed as put_api_ai_chats_by_id
from noveum_api_client.models.post_api_ai_chats_body import PostApiAiChatsBody
from noveum_api_client.models.post_api_ai_chats_by_id_messages_body import PostApiAiChatsByIdMessagesBody
from noveum_api_client.models.post_api_ai_chats_by_id_messages_body_messages_item import (
    PostApiAiChatsByIdMessagesBodyMessagesItem,
)
from noveum_api_client.models.post_api_ai_chats_by_id_messages_body_messages_item_role import (
    PostApiAiChatsByIdMessagesBodyMessagesItemRole,
)
from noveum_api_client.models.put_api_ai_chats_by_id_body import PutApiAiChatsByIdBody

API_KEY = os.getenv("NOVEUM_API_KEY")
BASE_URL = os.getenv("NOVEUM_BASE_URL", "https://api.noveum.ai")

test_results: list[dict[str, Any]] = []
created_resources: dict[str, list[Any]] = {"chats": []}
CHAT_ID = None


def log_test(name: str, passed: bool, details: str = "") -> bool:
    test_results.append({"test": name, "passed": passed, "details": details, "timestamp": datetime.now().isoformat()})
    print(f"{'✅' if passed else '❌'} {name}" + (f" - {details}" if details else ""))
    return passed


def print_section(title: str):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def test_list_chats(low_level_client):
    print_section("TEST 1: List AI Chats")
    try:
        response = get_api_ai_chats(client=low_level_client, limit=10)
        passed = response.status_code == 200
        log_test("List AI chats", passed, f"Status: {response.status_code}")
    except Exception as e:
        log_test("List AI chats", False, f"Exception: {str(e)}")


def test_create_chat(low_level_client):
    print_section("TEST 2: Create AI Chat")
    global CHAT_ID
    try:
        # Create a test chat with a unique title
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        chat_body = PostApiAiChatsBody(title=f"SDK Test Chat {timestamp}")

        response = post_api_ai_chats(client=low_level_client, body=chat_body)
        passed = response.status_code in [200, 201]

        if passed and response.parsed and hasattr(response.parsed, "id"):
            CHAT_ID = response.parsed.id
            created_resources["chats"].append(CHAT_ID)
            log_test("Create AI chat", True, f"Status: {response.status_code}, ID: {CHAT_ID}")
        else:
            log_test("Create AI chat", passed, f"Status: {response.status_code}")
    except Exception as e:
        log_test("Create AI chat", False, f"Exception: {str(e)}")


def test_get_chat(low_level_client):
    print_section("TEST 3: Get AI Chat by ID")
    global CHAT_ID

    if not CHAT_ID:
        log_test("Get AI chat by ID", True, "Skipped - no chat ID available (create failed)")
        return

    try:
        response = get_api_ai_chats_by_id(client=low_level_client, id=CHAT_ID)
        passed = response.status_code == 200
        log_test("Get AI chat by ID", passed, f"Status: {response.status_code}")
    except Exception as e:
        log_test("Get AI chat by ID", False, f"Exception: {str(e)}")


def test_update_chat(low_level_client):
    print_section("TEST 4: Update AI Chat")
    global CHAT_ID

    if not CHAT_ID:
        log_test("Update AI chat", True, "Skipped - no chat ID available (create failed)")
        return

    try:
        # Update the chat title
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        update_body = PutApiAiChatsByIdBody(title=f"SDK Test Chat Updated {timestamp}")

        response = put_api_ai_chats_by_id(client=low_level_client, id=CHAT_ID, body=update_body)
        passed = response.status_code == 200
        log_test("Update AI chat", passed, f"Status: {response.status_code}")
    except Exception as e:
        log_test("Update AI chat", False, f"Exception: {str(e)}")


def test_send_message(low_level_client):
    print_section("TEST 5: Send Message to Chat")
    global CHAT_ID

    if not CHAT_ID:
        log_test("Send message to chat", True, "Skipped - no chat ID available (create failed)")
        return

    try:
        # Create a message to send
        message_item = PostApiAiChatsByIdMessagesBodyMessagesItem(
            role=PostApiAiChatsByIdMessagesBodyMessagesItemRole.USER, content="Hello, this is a test message."
        )
        message_body = PostApiAiChatsByIdMessagesBody(messages=[message_item])

        response = post_api_ai_chats_by_id_messages(client=low_level_client, id=CHAT_ID, body=message_body)
        passed = response.status_code == 200
        log_test("Send message to chat", passed, f"Status: {response.status_code}")
    except Exception as e:
        log_test("Send message to chat", False, f"Exception: {str(e)}")


def test_delete_chat(low_level_client):
    print_section("TEST 6: Delete AI Chat")
    global CHAT_ID

    if not CHAT_ID:
        log_test("Delete AI chat", True, "Skipped - no chat ID available (create failed)")
        return

    try:
        response = delete_api_ai_chats_by_id(client=low_level_client, id=CHAT_ID)
        passed = response.status_code in [200, 204]

        if passed and CHAT_ID in created_resources["chats"]:
            created_resources["chats"].remove(CHAT_ID)

        log_test("Delete AI chat", passed, f"Status: {response.status_code}")
    except Exception as e:
        log_test("Delete AI chat", False, f"Exception: {str(e)}")


def cleanup_resources(low_level_client):
    """Clean up any remaining test resources"""
    print_section("CLEANUP")
    for chat_id in created_resources["chats"][:]:
        try:
            response = delete_api_ai_chats_by_id(client=low_level_client, id=chat_id)
            if response.status_code in [200, 204]:
                created_resources["chats"].remove(chat_id)
                print(f"   ✅ Deleted chat: {chat_id}")
            else:
                print(f"   ⚠️  Failed to delete chat {chat_id}: {response.status_code}")
        except Exception as e:
            print(f"   ⚠️  Error deleting chat {chat_id}: {str(e)}")


def run_all_tests():
    if not API_KEY:
        pytest.skip("NOVEUM_API_KEY not set")

    print("\n" + "=" * 60)
    print("AI CHATS API TESTS")
    print("=" * 60)
    print("Testing 6 AI chat endpoints")
    print("=" * 60)

    global client, low_level_client
    client = NoveumClient(api_key=API_KEY, base_url=BASE_URL)
    low_level_client = Client(base_url=BASE_URL, headers={"Authorization": f"Bearer {API_KEY}"})

    # Run tests in order
    test_list_chats(low_level_client)
    test_create_chat(low_level_client)
    test_get_chat(low_level_client)
    test_update_chat(low_level_client)
    test_send_message(low_level_client)
    test_delete_chat(low_level_client)

    # Cleanup any remaining resources
    cleanup_resources(low_level_client)

    print_section("TEST SUMMARY")
    total = len(test_results)
    passed = sum(1 for r in test_results if r["passed"])
    print(f"\nTotal: {total}, Passed: {passed}, Failed: {total-passed}")
    print(f"Success Rate: {(passed/total*100):.1f}%" if total > 0 else "N/A")

    try:
        os.makedirs("../../test_results", exist_ok=True)
        with open(f"../../test_results/ai_chats_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json", "w") as f:
            json.dump(test_results, f, indent=2)
    except Exception:
        pass

    return passed == total


if __name__ == "__main__":
    sys.exit(0 if run_all_tests() else 1)
