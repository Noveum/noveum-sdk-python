from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_api_ai_chats_response_200_messages_item import PostApiAiChatsResponse200MessagesItem


T = TypeVar("T", bound="PostApiAiChatsResponse200")


@_attrs_define
class PostApiAiChatsResponse200:
    """
    Attributes:
        id (str):
        organization_id (None | str):
        user_id (None | str):
        title (None | str):
        messages (list[PostApiAiChatsResponse200MessagesItem]):
        created_at (str):
        updated_at (str):
    """

    id: str
    organization_id: None | str
    user_id: None | str
    title: None | str
    messages: list[PostApiAiChatsResponse200MessagesItem]
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        organization_id: None | str
        organization_id = self.organization_id

        user_id: None | str
        user_id = self.user_id

        title: None | str
        title = self.title

        messages = []
        for messages_item_data in self.messages:
            messages_item = messages_item_data.to_dict()
            messages.append(messages_item)

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "organizationId": organization_id,
                "userId": user_id,
                "title": title,
                "messages": messages,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_ai_chats_response_200_messages_item import PostApiAiChatsResponse200MessagesItem

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_organization_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        organization_id = _parse_organization_id(d.pop("organizationId"))

        def _parse_user_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        user_id = _parse_user_id(d.pop("userId"))

        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))

        messages = []
        _messages = d.pop("messages")
        for messages_item_data in _messages:
            messages_item = PostApiAiChatsResponse200MessagesItem.from_dict(messages_item_data)

            messages.append(messages_item)

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        post_api_ai_chats_response_200 = cls(
            id=id,
            organization_id=organization_id,
            user_id=user_id,
            title=title,
            messages=messages,
            created_at=created_at,
            updated_at=updated_at,
        )

        post_api_ai_chats_response_200.additional_properties = d
        return post_api_ai_chats_response_200

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
