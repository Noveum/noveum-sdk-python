from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiAuthDeleteUserBody")


@_attrs_define
class PostApiAuthDeleteUserBody:
    """
    Attributes:
        callback_url (str | Unset):
        password (str | Unset):
        token (str | Unset):
    """

    callback_url: str | Unset = UNSET
    password: str | Unset = UNSET
    token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        callback_url = self.callback_url

        password = self.password

        token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if callback_url is not UNSET:
            field_dict["callbackURL"] = callback_url
        if password is not UNSET:
            field_dict["password"] = password
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        callback_url = d.pop("callbackURL", UNSET)

        password = d.pop("password", UNSET)

        token = d.pop("token", UNSET)

        post_api_auth_delete_user_body = cls(
            callback_url=callback_url,
            password=password,
            token=token,
        )

        post_api_auth_delete_user_body.additional_properties = d
        return post_api_auth_delete_user_body

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
