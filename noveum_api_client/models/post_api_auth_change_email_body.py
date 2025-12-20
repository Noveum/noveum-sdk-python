from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiAuthChangeEmailBody")


@_attrs_define
class PostApiAuthChangeEmailBody:
    """
    Attributes:
        new_email (str): The new email to set
        callback_url (str | Unset): The URL to redirect to after email verification
    """

    new_email: str
    callback_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        new_email = self.new_email

        callback_url = self.callback_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "newEmail": new_email,
            }
        )
        if callback_url is not UNSET:
            field_dict["callbackURL"] = callback_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        new_email = d.pop("newEmail")

        callback_url = d.pop("callbackURL", UNSET)

        post_api_auth_change_email_body = cls(
            new_email=new_email,
            callback_url=callback_url,
        )

        post_api_auth_change_email_body.additional_properties = d
        return post_api_auth_change_email_body

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
