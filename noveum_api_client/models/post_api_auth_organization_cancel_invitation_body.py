from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApiAuthOrganizationCancelInvitationBody")


@_attrs_define
class PostApiAuthOrganizationCancelInvitationBody:
    """
    Attributes:
        invitation_id (str): The ID of the invitation to cancel
    """

    invitation_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        invitation_id = self.invitation_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invitationId": invitation_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        invitation_id = d.pop("invitationId")

        post_api_auth_organization_cancel_invitation_body = cls(
            invitation_id=invitation_id,
        )

        post_api_auth_organization_cancel_invitation_body.additional_properties = d
        return post_api_auth_organization_cancel_invitation_body

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
