from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiAuthSendVerificationEmailBody")


@_attrs_define
class PostApiAuthSendVerificationEmailBody:
    """
    Attributes:
        email (str): The email to send the verification email to
        callback_url (str | Unset): The URL to use for email verification callback
    """

    email: str
    callback_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        callback_url = self.callback_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
            }
        )
        if callback_url is not UNSET:
            field_dict["callbackURL"] = callback_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        callback_url = d.pop("callbackURL", UNSET)

        post_api_auth_send_verification_email_body = cls(
            email=email,
            callback_url=callback_url,
        )

        post_api_auth_send_verification_email_body.additional_properties = d
        return post_api_auth_send_verification_email_body

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
