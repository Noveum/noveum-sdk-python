from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_by_organisation_slug_credentials_by_id_response_200_credentials import (
        GetApiByOrganisationSlugCredentialsByIdResponse200Credentials,
    )


T = TypeVar("T", bound="GetApiByOrganisationSlugCredentialsByIdResponse200")


@_attrs_define
class GetApiByOrganisationSlugCredentialsByIdResponse200:
    """
    Attributes:
        id (str):
        provider_id (str):
        name (str):
        title (None | str):
        credentials (GetApiByOrganisationSlugCredentialsByIdResponse200Credentials):
        is_enabled (bool):
        organization_id (str):
        created_at (str):
        updated_at (str):
    """

    id: str
    provider_id: str
    name: str
    title: None | str
    credentials: GetApiByOrganisationSlugCredentialsByIdResponse200Credentials
    is_enabled: bool
    organization_id: str
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        provider_id = self.provider_id

        name = self.name

        title: None | str
        title = self.title

        credentials = self.credentials.to_dict()

        is_enabled = self.is_enabled

        organization_id = self.organization_id

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "providerId": provider_id,
                "name": name,
                "title": title,
                "credentials": credentials,
                "isEnabled": is_enabled,
                "organizationId": organization_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_by_organisation_slug_credentials_by_id_response_200_credentials import (
            GetApiByOrganisationSlugCredentialsByIdResponse200Credentials,
        )

        d = dict(src_dict)
        id = d.pop("id")

        provider_id = d.pop("providerId")

        name = d.pop("name")

        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))

        credentials = GetApiByOrganisationSlugCredentialsByIdResponse200Credentials.from_dict(d.pop("credentials"))

        is_enabled = d.pop("isEnabled")

        organization_id = d.pop("organizationId")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        get_api_by_organisation_slug_credentials_by_id_response_200 = cls(
            id=id,
            provider_id=provider_id,
            name=name,
            title=title,
            credentials=credentials,
            is_enabled=is_enabled,
            organization_id=organization_id,
            created_at=created_at,
            updated_at=updated_at,
        )

        get_api_by_organisation_slug_credentials_by_id_response_200.additional_properties = d
        return get_api_by_organisation_slug_credentials_by_id_response_200

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
