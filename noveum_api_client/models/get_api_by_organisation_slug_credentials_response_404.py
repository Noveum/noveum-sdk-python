from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_api_by_organisation_slug_credentials_response_404_details import (
        GetApiByOrganisationSlugCredentialsResponse404Details,
    )


T = TypeVar("T", bound="GetApiByOrganisationSlugCredentialsResponse404")


@_attrs_define
class GetApiByOrganisationSlugCredentialsResponse404:
    """
    Attributes:
        error (str):
        error_code (str | Unset):
        details (GetApiByOrganisationSlugCredentialsResponse404Details | Unset):
    """

    error: str
    error_code: str | Unset = UNSET
    details: GetApiByOrganisationSlugCredentialsResponse404Details | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        error_code = self.error_code

        details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
            }
        )
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_by_organisation_slug_credentials_response_404_details import (
            GetApiByOrganisationSlugCredentialsResponse404Details,
        )

        d = dict(src_dict)
        error = d.pop("error")

        error_code = d.pop("errorCode", UNSET)

        _details = d.pop("details", UNSET)
        details: GetApiByOrganisationSlugCredentialsResponse404Details | Unset
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = GetApiByOrganisationSlugCredentialsResponse404Details.from_dict(_details)

        get_api_by_organisation_slug_credentials_response_404 = cls(
            error=error,
            error_code=error_code,
            details=details,
        )

        get_api_by_organisation_slug_credentials_response_404.additional_properties = d
        return get_api_by_organisation_slug_credentials_response_404

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
