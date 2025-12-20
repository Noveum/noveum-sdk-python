from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiAuthSignInUsernameBody")


@_attrs_define
class PostApiAuthSignInUsernameBody:
    """
    Attributes:
        username (str): The username of the user
        password (str): The password of the user
        remember_me (str | Unset): Remember the user session
    """

    username: str
    password: str
    remember_me: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        password = self.password

        remember_me = self.remember_me

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "password": password,
            }
        )
        if remember_me is not UNSET:
            field_dict["rememberMe"] = remember_me

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username")

        password = d.pop("password")

        remember_me = d.pop("rememberMe", UNSET)

        post_api_auth_sign_in_username_body = cls(
            username=username,
            password=password,
            remember_me=remember_me,
        )

        post_api_auth_sign_in_username_body.additional_properties = d
        return post_api_auth_sign_in_username_body

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
