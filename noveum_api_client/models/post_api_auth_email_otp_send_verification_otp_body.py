from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApiAuthEmailOtpSendVerificationOtpBody")


@_attrs_define
class PostApiAuthEmailOtpSendVerificationOtpBody:
    """
    Attributes:
        email (str): Email address to send the OTP
        type_ (str): Type of the OTP
    """

    email: str
    type_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        type_ = d.pop("type")

        post_api_auth_email_otp_send_verification_otp_body = cls(
            email=email,
            type_=type_,
        )

        post_api_auth_email_otp_send_verification_otp_body.additional_properties = d
        return post_api_auth_email_otp_send_verification_otp_body

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
