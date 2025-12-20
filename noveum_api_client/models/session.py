from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Session")


@_attrs_define
class Session:
    """
    Attributes:
        id (str | Unset):
        expires_at (datetime.date | Unset):
        token (str | Unset):
        created_at (datetime.date | Unset):
        updated_at (datetime.date | Unset):
        ip_address (str | Unset):
        user_agent (str | Unset):
        user_id (str | Unset):
        impersonated_by (str | Unset):
        active_organization_id (str | Unset):
    """

    id: str | Unset = UNSET
    expires_at: datetime.date | Unset = UNSET
    token: str | Unset = UNSET
    created_at: datetime.date | Unset = UNSET
    updated_at: datetime.date | Unset = UNSET
    ip_address: str | Unset = UNSET
    user_agent: str | Unset = UNSET
    user_id: str | Unset = UNSET
    impersonated_by: str | Unset = UNSET
    active_organization_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        token = self.token

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        ip_address = self.ip_address

        user_agent = self.user_agent

        user_id = self.user_id

        impersonated_by = self.impersonated_by

        active_organization_id = self.active_organization_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if token is not UNSET:
            field_dict["token"] = token
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if ip_address is not UNSET:
            field_dict["ipAddress"] = ip_address
        if user_agent is not UNSET:
            field_dict["userAgent"] = user_agent
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if impersonated_by is not UNSET:
            field_dict["impersonatedBy"] = impersonated_by
        if active_organization_id is not UNSET:
            field_dict["activeOrganizationId"] = active_organization_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _expires_at = d.pop("expiresAt", UNSET)
        expires_at: datetime.date | Unset
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = isoparse(_expires_at).date()

        token = d.pop("token", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.date | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at).date()

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.date | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at).date()

        ip_address = d.pop("ipAddress", UNSET)

        user_agent = d.pop("userAgent", UNSET)

        user_id = d.pop("userId", UNSET)

        impersonated_by = d.pop("impersonatedBy", UNSET)

        active_organization_id = d.pop("activeOrganizationId", UNSET)

        session = cls(
            id=id,
            expires_at=expires_at,
            token=token,
            created_at=created_at,
            updated_at=updated_at,
            ip_address=ip_address,
            user_agent=user_agent,
            user_id=user_id,
            impersonated_by=impersonated_by,
            active_organization_id=active_organization_id,
        )

        session.additional_properties = d
        return session

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
