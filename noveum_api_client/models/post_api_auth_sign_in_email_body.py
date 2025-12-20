from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiAuthSignInEmailBody")


@_attrs_define
class PostApiAuthSignInEmailBody:
    """
    Attributes:
        email (str): Email of the user
        password (str): Password of the user
        callback_url (str | Unset): Callback URL to use as a redirect for email verification
        remember_me (str | Unset): If this is false, the session will not be remembered. Default is `true`.
    """

    email: str
    password: str
    callback_url: str | Unset = UNSET
    remember_me: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        password = self.password

        callback_url = self.callback_url

        remember_me = self.remember_me

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "password": password,
            }
        )
        if callback_url is not UNSET:
            field_dict["callbackURL"] = callback_url
        if remember_me is not UNSET:
            field_dict["rememberMe"] = remember_me

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        password = d.pop("password")

        callback_url = d.pop("callbackURL", UNSET)

        remember_me = d.pop("rememberMe", UNSET)

        post_api_auth_sign_in_email_body = cls(
            email=email,
            password=password,
            callback_url=callback_url,
            remember_me=remember_me,
        )

        post_api_auth_sign_in_email_body.additional_properties = d
        return post_api_auth_sign_in_email_body

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
