from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiAuthOrganizationInviteMemberBody")


@_attrs_define
class PostApiAuthOrganizationInviteMemberBody:
    """
    Attributes:
        email (str): The email address of the user to invite
        role (str): The role to assign to the user
        organization_id (str | Unset): The organization ID to invite the user to
        resend (str | Unset): Resend the invitation email, if the user is already invited
    """

    email: str
    role: str
    organization_id: str | Unset = UNSET
    resend: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        role = self.role

        organization_id = self.organization_id

        resend = self.resend

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "role": role,
            }
        )
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if resend is not UNSET:
            field_dict["resend"] = resend

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        role = d.pop("role")

        organization_id = d.pop("organizationId", UNSET)

        resend = d.pop("resend", UNSET)

        post_api_auth_organization_invite_member_body = cls(
            email=email,
            role=role,
            organization_id=organization_id,
            resend=resend,
        )

        post_api_auth_organization_invite_member_body.additional_properties = d
        return post_api_auth_organization_invite_member_body

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
