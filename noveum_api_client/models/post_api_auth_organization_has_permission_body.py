from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_api_auth_organization_has_permission_body_permission import (
        PostApiAuthOrganizationHasPermissionBodyPermission,
    )


T = TypeVar("T", bound="PostApiAuthOrganizationHasPermissionBody")


@_attrs_define
class PostApiAuthOrganizationHasPermissionBody:
    """
    Attributes:
        permission (PostApiAuthOrganizationHasPermissionBodyPermission): The permission to check
    """

    permission: PostApiAuthOrganizationHasPermissionBodyPermission
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        permission = self.permission.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "permission": permission,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_auth_organization_has_permission_body_permission import (
            PostApiAuthOrganizationHasPermissionBodyPermission,
        )

        d = dict(src_dict)
        permission = PostApiAuthOrganizationHasPermissionBodyPermission.from_dict(d.pop("permission"))

        post_api_auth_organization_has_permission_body = cls(
            permission=permission,
        )

        post_api_auth_organization_has_permission_body.additional_properties = d
        return post_api_auth_organization_has_permission_body

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
