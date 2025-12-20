from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetApiAuthPasskeyGenerateRegisterOptionsResponse200PubKeyCredParamsItem")


@_attrs_define
class GetApiAuthPasskeyGenerateRegisterOptionsResponse200PubKeyCredParamsItem:
    """
    Attributes:
        type_ (str | Unset):
        alg (float | Unset):
    """

    type_: str | Unset = UNSET
    alg: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        alg = self.alg

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if alg is not UNSET:
            field_dict["alg"] = alg

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        alg = d.pop("alg", UNSET)

        get_api_auth_passkey_generate_register_options_response_200_pub_key_cred_params_item = cls(
            type_=type_,
            alg=alg,
        )

        get_api_auth_passkey_generate_register_options_response_200_pub_key_cred_params_item.additional_properties = d
        return get_api_auth_passkey_generate_register_options_response_200_pub_key_cred_params_item

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
