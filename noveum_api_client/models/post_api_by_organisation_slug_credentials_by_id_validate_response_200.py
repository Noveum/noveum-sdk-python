from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApiByOrganisationSlugCredentialsByIdValidateResponse200")


@_attrs_define
class PostApiByOrganisationSlugCredentialsByIdValidateResponse200:
    """
    Attributes:
        valid (bool):
        message (str):
        tested_at (str):
    """

    valid: bool
    message: str
    tested_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        valid = self.valid

        message = self.message

        tested_at = self.tested_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "valid": valid,
                "message": message,
                "testedAt": tested_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        valid = d.pop("valid")

        message = d.pop("message")

        tested_at = d.pop("testedAt")

        post_api_by_organisation_slug_credentials_by_id_validate_response_200 = cls(
            valid=valid,
            message=message,
            tested_at=tested_at,
        )

        post_api_by_organisation_slug_credentials_by_id_validate_response_200.additional_properties = d
        return post_api_by_organisation_slug_credentials_by_id_validate_response_200

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
