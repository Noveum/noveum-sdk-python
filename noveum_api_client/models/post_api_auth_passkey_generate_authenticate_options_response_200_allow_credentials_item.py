from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200AllowCredentialsItem")


@_attrs_define
class PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200AllowCredentialsItem:
    """
    Attributes:
        id (str | Unset):
        type_ (str | Unset):
        transports (list[str] | Unset):
    """

    id: str | Unset = UNSET
    type_: str | Unset = UNSET
    transports: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        transports: list[str] | Unset = UNSET
        if not isinstance(self.transports, Unset):
            transports = self.transports

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if transports is not UNSET:
            field_dict["transports"] = transports

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        transports = cast(list[str], d.pop("transports", UNSET))

        post_api_auth_passkey_generate_authenticate_options_response_200_allow_credentials_item = cls(
            id=id,
            type_=type_,
            transports=transports,
        )

        post_api_auth_passkey_generate_authenticate_options_response_200_allow_credentials_item.additional_properties = (
            d
        )
        return post_api_auth_passkey_generate_authenticate_options_response_200_allow_credentials_item

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
