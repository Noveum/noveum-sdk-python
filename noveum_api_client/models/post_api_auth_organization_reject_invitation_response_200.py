from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_auth_organization_reject_invitation_response_200_invitation import (
        PostApiAuthOrganizationRejectInvitationResponse200Invitation,
    )


T = TypeVar("T", bound="PostApiAuthOrganizationRejectInvitationResponse200")


@_attrs_define
class PostApiAuthOrganizationRejectInvitationResponse200:
    """
    Attributes:
        invitation (PostApiAuthOrganizationRejectInvitationResponse200Invitation | Unset):
        member (None | Unset):
    """

    invitation: PostApiAuthOrganizationRejectInvitationResponse200Invitation | Unset = UNSET
    member: None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        invitation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.invitation, Unset):
            invitation = self.invitation.to_dict()

        member = self.member

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invitation is not UNSET:
            field_dict["invitation"] = invitation
        if member is not UNSET:
            field_dict["member"] = member

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_auth_organization_reject_invitation_response_200_invitation import (
            PostApiAuthOrganizationRejectInvitationResponse200Invitation,
        )

        d = dict(src_dict)
        _invitation = d.pop("invitation", UNSET)
        invitation: PostApiAuthOrganizationRejectInvitationResponse200Invitation | Unset
        if isinstance(_invitation, Unset):
            invitation = UNSET
        else:
            invitation = PostApiAuthOrganizationRejectInvitationResponse200Invitation.from_dict(_invitation)

        member = d.pop("member", UNSET)

        post_api_auth_organization_reject_invitation_response_200 = cls(
            invitation=invitation,
            member=member,
        )

        post_api_auth_organization_reject_invitation_response_200.additional_properties = d
        return post_api_auth_organization_reject_invitation_response_200

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
