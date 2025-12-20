from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiAuthOrganizationCreateBody")


@_attrs_define
class PostApiAuthOrganizationCreateBody:
    """
    Attributes:
        name (str): The name of the organization
        slug (str): The slug of the organization
        user_id (str | Unset): The user id of the organization creator. If not provided, the current user will be used.
            Should only be used by admins or when called by the server.
        logo (str | Unset): The logo of the organization
        metadata (str | Unset): The metadata of the organization
    """

    name: str
    slug: str
    user_id: str | Unset = UNSET
    logo: str | Unset = UNSET
    metadata: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        slug = self.slug

        user_id = self.user_id

        logo = self.logo

        metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "slug": slug,
            }
        )
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if logo is not UNSET:
            field_dict["logo"] = logo
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        slug = d.pop("slug")

        user_id = d.pop("userId", UNSET)

        logo = d.pop("logo", UNSET)

        metadata = d.pop("metadata", UNSET)

        post_api_auth_organization_create_body = cls(
            name=name,
            slug=slug,
            user_id=user_id,
            logo=logo,
            metadata=metadata,
        )

        post_api_auth_organization_create_body.additional_properties = d
        return post_api_auth_organization_create_body

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
