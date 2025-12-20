from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiAuthOrganizationSetActiveBody")


@_attrs_define
class PostApiAuthOrganizationSetActiveBody:
    """
    Attributes:
        organization_id (str | Unset): The organization id to set as active. It can be null to unset the active
            organization
        organization_slug (str | Unset): The organization slug to set as active. It can be null to unset the active
            organization if organizationId is not provided
    """

    organization_id: str | Unset = UNSET
    organization_slug: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization_id = self.organization_id

        organization_slug = self.organization_slug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization_slug is not UNSET:
            field_dict["organizationSlug"] = organization_slug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        organization_id = d.pop("organizationId", UNSET)

        organization_slug = d.pop("organizationSlug", UNSET)

        post_api_auth_organization_set_active_body = cls(
            organization_id=organization_id,
            organization_slug=organization_slug,
        )

        post_api_auth_organization_set_active_body.additional_properties = d
        return post_api_auth_organization_set_active_body

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
