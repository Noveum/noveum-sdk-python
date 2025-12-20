from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiAuthOrganizationUpdateMemberRoleBody")


@_attrs_define
class PostApiAuthOrganizationUpdateMemberRoleBody:
    """
    Attributes:
        role (str):
        member_id (str):
        organization_id (str | Unset):
    """

    role: str
    member_id: str
    organization_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role = self.role

        member_id = self.member_id

        organization_id = self.organization_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
                "memberId": member_id,
            }
        )
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        role = d.pop("role")

        member_id = d.pop("memberId")

        organization_id = d.pop("organizationId", UNSET)

        post_api_auth_organization_update_member_role_body = cls(
            role=role,
            member_id=member_id,
            organization_id=organization_id,
        )

        post_api_auth_organization_update_member_role_body.additional_properties = d
        return post_api_auth_organization_update_member_role_body

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
