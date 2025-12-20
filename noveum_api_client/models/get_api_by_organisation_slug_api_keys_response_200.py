from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_by_organisation_slug_api_keys_response_200_api_keys_item import (
        GetApiByOrganisationSlugApiKeysResponse200ApiKeysItem,
    )


T = TypeVar("T", bound="GetApiByOrganisationSlugApiKeysResponse200")


@_attrs_define
class GetApiByOrganisationSlugApiKeysResponse200:
    """
    Attributes:
        api_keys (list[GetApiByOrganisationSlugApiKeysResponse200ApiKeysItem]):
    """

    api_keys: list[GetApiByOrganisationSlugApiKeysResponse200ApiKeysItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_keys = []
        for api_keys_item_data in self.api_keys:
            api_keys_item = api_keys_item_data.to_dict()
            api_keys.append(api_keys_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKeys": api_keys,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_by_organisation_slug_api_keys_response_200_api_keys_item import (
            GetApiByOrganisationSlugApiKeysResponse200ApiKeysItem,
        )

        d = dict(src_dict)
        api_keys = []
        _api_keys = d.pop("apiKeys")
        for api_keys_item_data in _api_keys:
            api_keys_item = GetApiByOrganisationSlugApiKeysResponse200ApiKeysItem.from_dict(api_keys_item_data)

            api_keys.append(api_keys_item)

        get_api_by_organisation_slug_api_keys_response_200 = cls(
            api_keys=api_keys,
        )

        get_api_by_organisation_slug_api_keys_response_200.additional_properties = d
        return get_api_by_organisation_slug_api_keys_response_200

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
