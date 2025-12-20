from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApiAuthOrganizationInviteMemberResponse200")


@_attrs_define
class PostApiAuthOrganizationInviteMemberResponse200:
    """
    Attributes:
        id (str):
        email (str):
        role (str):
        organization_id (str):
        inviter_id (str):
        status (str):
        expires_at (str):
    """

    id: str
    email: str
    role: str
    organization_id: str
    inviter_id: str
    status: str
    expires_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        role = self.role

        organization_id = self.organization_id

        inviter_id = self.inviter_id

        status = self.status

        expires_at = self.expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "email": email,
                "role": role,
                "organizationId": organization_id,
                "inviterId": inviter_id,
                "status": status,
                "expiresAt": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        email = d.pop("email")

        role = d.pop("role")

        organization_id = d.pop("organizationId")

        inviter_id = d.pop("inviterId")

        status = d.pop("status")

        expires_at = d.pop("expiresAt")

        post_api_auth_organization_invite_member_response_200 = cls(
            id=id,
            email=email,
            role=role,
            organization_id=organization_id,
            inviter_id=inviter_id,
            status=status,
            expires_at=expires_at,
        )

        post_api_auth_organization_invite_member_response_200.additional_properties = d
        return post_api_auth_organization_invite_member_response_200

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
