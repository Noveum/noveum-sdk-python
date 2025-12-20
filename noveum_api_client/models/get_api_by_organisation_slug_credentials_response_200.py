from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_by_organisation_slug_credentials_response_200_credentials_item import (
        GetApiByOrganisationSlugCredentialsResponse200CredentialsItem,
    )


T = TypeVar("T", bound="GetApiByOrganisationSlugCredentialsResponse200")


@_attrs_define
class GetApiByOrganisationSlugCredentialsResponse200:
    """
    Attributes:
        credentials (list[GetApiByOrganisationSlugCredentialsResponse200CredentialsItem]):
    """

    credentials: list[GetApiByOrganisationSlugCredentialsResponse200CredentialsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credentials = []
        for credentials_item_data in self.credentials:
            credentials_item = credentials_item_data.to_dict()
            credentials.append(credentials_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credentials": credentials,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_by_organisation_slug_credentials_response_200_credentials_item import (
            GetApiByOrganisationSlugCredentialsResponse200CredentialsItem,
        )

        d = dict(src_dict)
        credentials = []
        _credentials = d.pop("credentials")
        for credentials_item_data in _credentials:
            credentials_item = GetApiByOrganisationSlugCredentialsResponse200CredentialsItem.from_dict(
                credentials_item_data
            )

            credentials.append(credentials_item)

        get_api_by_organisation_slug_credentials_response_200 = cls(
            credentials=credentials,
        )

        get_api_by_organisation_slug_credentials_response_200.additional_properties = d
        return get_api_by_organisation_slug_credentials_response_200

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
