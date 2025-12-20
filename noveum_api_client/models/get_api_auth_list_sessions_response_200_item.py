from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetApiAuthListSessionsResponse200Item")


@_attrs_define
class GetApiAuthListSessionsResponse200Item:
    """
    Attributes:
        token (str | Unset):
        user_id (str | Unset):
        expires_at (str | Unset):
    """

    token: str | Unset = UNSET
    user_id: str | Unset = UNSET
    expires_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        user_id = self.user_id

        expires_at = self.expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token", UNSET)

        user_id = d.pop("userId", UNSET)

        expires_at = d.pop("expiresAt", UNSET)

        get_api_auth_list_sessions_response_200_item = cls(
            token=token,
            user_id=user_id,
            expires_at=expires_at,
        )

        get_api_auth_list_sessions_response_200_item.additional_properties = d
        return get_api_auth_list_sessions_response_200_item

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
