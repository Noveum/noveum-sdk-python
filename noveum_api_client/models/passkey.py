from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Passkey")


@_attrs_define
class Passkey:
    """
    Attributes:
        id (str | Unset):
        name (str | Unset):
        public_key (str | Unset):
        user_id (str | Unset):
        credential_id (str | Unset):
        counter (float | Unset):
        device_type (str | Unset):
        backed_up (bool | Unset):
        transports (str | Unset):
        created_at (datetime.date | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    public_key: str | Unset = UNSET
    user_id: str | Unset = UNSET
    credential_id: str | Unset = UNSET
    counter: float | Unset = UNSET
    device_type: str | Unset = UNSET
    backed_up: bool | Unset = UNSET
    transports: str | Unset = UNSET
    created_at: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        public_key = self.public_key

        user_id = self.user_id

        credential_id = self.credential_id

        counter = self.counter

        device_type = self.device_type

        backed_up = self.backed_up

        transports = self.transports

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if public_key is not UNSET:
            field_dict["publicKey"] = public_key
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if credential_id is not UNSET:
            field_dict["credentialID"] = credential_id
        if counter is not UNSET:
            field_dict["counter"] = counter
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if backed_up is not UNSET:
            field_dict["backedUp"] = backed_up
        if transports is not UNSET:
            field_dict["transports"] = transports
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        public_key = d.pop("publicKey", UNSET)

        user_id = d.pop("userId", UNSET)

        credential_id = d.pop("credentialID", UNSET)

        counter = d.pop("counter", UNSET)

        device_type = d.pop("deviceType", UNSET)

        backed_up = d.pop("backedUp", UNSET)

        transports = d.pop("transports", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.date | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at).date()

        passkey = cls(
            id=id,
            name=name,
            public_key=public_key,
            user_id=user_id,
            credential_id=credential_id,
            counter=counter,
            device_type=device_type,
            backed_up=backed_up,
            transports=transports,
            created_at=created_at,
        )

        passkey.additional_properties = d
        return passkey

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
