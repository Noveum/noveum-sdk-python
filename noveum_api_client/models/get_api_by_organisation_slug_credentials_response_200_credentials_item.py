from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApiByOrganisationSlugCredentialsResponse200CredentialsItem")


@_attrs_define
class GetApiByOrganisationSlugCredentialsResponse200CredentialsItem:
    """
    Attributes:
        id (str):
        provider_id (str):
        name (str):
        is_enabled (bool):
        created_at (str):
        updated_at (str):
    """

    id: str
    provider_id: str
    name: str
    is_enabled: bool
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        provider_id = self.provider_id

        name = self.name

        is_enabled = self.is_enabled

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "providerId": provider_id,
                "name": name,
                "isEnabled": is_enabled,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        provider_id = d.pop("providerId")

        name = d.pop("name")

        is_enabled = d.pop("isEnabled")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        get_api_by_organisation_slug_credentials_response_200_credentials_item = cls(
            id=id,
            provider_id=provider_id,
            name=name,
            is_enabled=is_enabled,
            created_at=created_at,
            updated_at=updated_at,
        )

        get_api_by_organisation_slug_credentials_response_200_credentials_item.additional_properties = d
        return get_api_by_organisation_slug_credentials_response_200_credentials_item

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
