from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BanUserBody")


@_attrs_define
class BanUserBody:
    """
    Attributes:
        user_id (str): The user id
        ban_reason (str | Unset): The reason for the ban
        ban_expires_in (str | Unset): The number of seconds until the ban expires
    """

    user_id: str
    ban_reason: str | Unset = UNSET
    ban_expires_in: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        ban_reason = self.ban_reason

        ban_expires_in = self.ban_expires_in

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
            }
        )
        if ban_reason is not UNSET:
            field_dict["banReason"] = ban_reason
        if ban_expires_in is not UNSET:
            field_dict["banExpiresIn"] = ban_expires_in

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("userId")

        ban_reason = d.pop("banReason", UNSET)

        ban_expires_in = d.pop("banExpiresIn", UNSET)

        ban_user_body = cls(
            user_id=user_id,
            ban_reason=ban_reason,
            ban_expires_in=ban_expires_in,
        )

        ban_user_body.additional_properties = d
        return ban_user_body

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
