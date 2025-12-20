from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiAuthOrganizationRemoveMemberBody")


@_attrs_define
class PostApiAuthOrganizationRemoveMemberBody:
    """
    Attributes:
        member_id_or_email (str): The ID or email of the member to remove
        organization_id (str | Unset): The ID of the organization to remove the member from. If not provided, the active
            organization will be used
    """

    member_id_or_email: str
    organization_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        member_id_or_email = self.member_id_or_email

        organization_id = self.organization_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "memberIdOrEmail": member_id_or_email,
            }
        )
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        member_id_or_email = d.pop("memberIdOrEmail")

        organization_id = d.pop("organizationId", UNSET)

        post_api_auth_organization_remove_member_body = cls(
            member_id_or_email=member_id_or_email,
            organization_id=organization_id,
        )

        post_api_auth_organization_remove_member_body.additional_properties = d
        return post_api_auth_organization_remove_member_body

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
