from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiAuthChangePasswordBody")


@_attrs_define
class PostApiAuthChangePasswordBody:
    """
    Attributes:
        new_password (str): The new password to set
        current_password (str): The current password
        revoke_other_sessions (str | Unset): Revoke all other sessions
    """

    new_password: str
    current_password: str
    revoke_other_sessions: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        new_password = self.new_password

        current_password = self.current_password

        revoke_other_sessions = self.revoke_other_sessions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "newPassword": new_password,
                "currentPassword": current_password,
            }
        )
        if revoke_other_sessions is not UNSET:
            field_dict["revokeOtherSessions"] = revoke_other_sessions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        new_password = d.pop("newPassword")

        current_password = d.pop("currentPassword")

        revoke_other_sessions = d.pop("revokeOtherSessions", UNSET)

        post_api_auth_change_password_body = cls(
            new_password=new_password,
            current_password=current_password,
            revoke_other_sessions=revoke_other_sessions,
        )

        post_api_auth_change_password_body.additional_properties = d
        return post_api_auth_change_password_body

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
