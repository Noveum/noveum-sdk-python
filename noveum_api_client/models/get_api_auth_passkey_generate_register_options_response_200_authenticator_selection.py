from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetApiAuthPasskeyGenerateRegisterOptionsResponse200AuthenticatorSelection")


@_attrs_define
class GetApiAuthPasskeyGenerateRegisterOptionsResponse200AuthenticatorSelection:
    """
    Attributes:
        authenticator_attachment (str | Unset):
        require_resident_key (bool | Unset):
        user_verification (str | Unset):
    """

    authenticator_attachment: str | Unset = UNSET
    require_resident_key: bool | Unset = UNSET
    user_verification: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authenticator_attachment = self.authenticator_attachment

        require_resident_key = self.require_resident_key

        user_verification = self.user_verification

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authenticator_attachment is not UNSET:
            field_dict["authenticatorAttachment"] = authenticator_attachment
        if require_resident_key is not UNSET:
            field_dict["requireResidentKey"] = require_resident_key
        if user_verification is not UNSET:
            field_dict["userVerification"] = user_verification

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        authenticator_attachment = d.pop("authenticatorAttachment", UNSET)

        require_resident_key = d.pop("requireResidentKey", UNSET)

        user_verification = d.pop("userVerification", UNSET)

        get_api_auth_passkey_generate_register_options_response_200_authenticator_selection = cls(
            authenticator_attachment=authenticator_attachment,
            require_resident_key=require_resident_key,
            user_verification=user_verification,
        )

        get_api_auth_passkey_generate_register_options_response_200_authenticator_selection.additional_properties = d
        return get_api_auth_passkey_generate_register_options_response_200_authenticator_selection

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
