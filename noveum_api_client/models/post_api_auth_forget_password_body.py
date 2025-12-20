from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiAuthForgetPasswordBody")


@_attrs_define
class PostApiAuthForgetPasswordBody:
    """
    Attributes:
        email (str): The email address of the user to send a password reset email to
        redirect_to (str | Unset): The URL to redirect the user to reset their password. If the token isn't valid or
            expired, it'll be redirected with a query parameter `?error=INVALID_TOKEN`. If the token is valid, it'll be
            redirected with a query parameter `?token=VALID_TOKEN
    """

    email: str
    redirect_to: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        redirect_to = self.redirect_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
            }
        )
        if redirect_to is not UNSET:
            field_dict["redirectTo"] = redirect_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        redirect_to = d.pop("redirectTo", UNSET)

        post_api_auth_forget_password_body = cls(
            email=email,
            redirect_to=redirect_to,
        )

        post_api_auth_forget_password_body.additional_properties = d
        return post_api_auth_forget_password_body

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
