from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Invitation")


@_attrs_define
class Invitation:
    """
    Attributes:
        id (str | Unset):
        organization_id (str | Unset):
        email (str | Unset):
        role (str | Unset):
        status (str | Unset):
        expires_at (datetime.date | Unset):
        inviter_id (str | Unset):
    """

    id: str | Unset = UNSET
    organization_id: str | Unset = UNSET
    email: str | Unset = UNSET
    role: str | Unset = UNSET
    status: str | Unset = UNSET
    expires_at: datetime.date | Unset = UNSET
    inviter_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        organization_id = self.organization_id

        email = self.email

        role = self.role

        status = self.status

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        inviter_id = self.inviter_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if email is not UNSET:
            field_dict["email"] = email
        if role is not UNSET:
            field_dict["role"] = role
        if status is not UNSET:
            field_dict["status"] = status
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if inviter_id is not UNSET:
            field_dict["inviterId"] = inviter_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        organization_id = d.pop("organizationId", UNSET)

        email = d.pop("email", UNSET)

        role = d.pop("role", UNSET)

        status = d.pop("status", UNSET)

        _expires_at = d.pop("expiresAt", UNSET)
        expires_at: datetime.date | Unset
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = isoparse(_expires_at).date()

        inviter_id = d.pop("inviterId", UNSET)

        invitation = cls(
            id=id,
            organization_id=organization_id,
            email=email,
            role=role,
            status=status,
            expires_at=expires_at,
            inviter_id=inviter_id,
        )

        invitation.additional_properties = d
        return invitation

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
