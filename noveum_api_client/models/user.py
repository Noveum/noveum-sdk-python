from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """
    Attributes:
        id (str | Unset):
        name (str | Unset):
        email (str | Unset):
        email_verified (bool | Unset):
        image (str | Unset):
        created_at (datetime.date | Unset):
        updated_at (datetime.date | Unset):
        username (str | Unset):
        role (str | Unset):
        banned (bool | Unset):
        ban_reason (str | Unset):
        ban_expires (datetime.date | Unset):
        onboarding_complete (bool | Unset):
        locale (str | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    email: str | Unset = UNSET
    email_verified: bool | Unset = UNSET
    image: str | Unset = UNSET
    created_at: datetime.date | Unset = UNSET
    updated_at: datetime.date | Unset = UNSET
    username: str | Unset = UNSET
    role: str | Unset = UNSET
    banned: bool | Unset = UNSET
    ban_reason: str | Unset = UNSET
    ban_expires: datetime.date | Unset = UNSET
    onboarding_complete: bool | Unset = UNSET
    locale: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        email = self.email

        email_verified = self.email_verified

        image = self.image

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        username = self.username

        role = self.role

        banned = self.banned

        ban_reason = self.ban_reason

        ban_expires: str | Unset = UNSET
        if not isinstance(self.ban_expires, Unset):
            ban_expires = self.ban_expires.isoformat()

        onboarding_complete = self.onboarding_complete

        locale = self.locale

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if email_verified is not UNSET:
            field_dict["emailVerified"] = email_verified
        if image is not UNSET:
            field_dict["image"] = image
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if username is not UNSET:
            field_dict["username"] = username
        if role is not UNSET:
            field_dict["role"] = role
        if banned is not UNSET:
            field_dict["banned"] = banned
        if ban_reason is not UNSET:
            field_dict["banReason"] = ban_reason
        if ban_expires is not UNSET:
            field_dict["banExpires"] = ban_expires
        if onboarding_complete is not UNSET:
            field_dict["onboardingComplete"] = onboarding_complete
        if locale is not UNSET:
            field_dict["locale"] = locale

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        email_verified = d.pop("emailVerified", UNSET)

        image = d.pop("image", UNSET)

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

        username = d.pop("username", UNSET)

        role = d.pop("role", UNSET)

        banned = d.pop("banned", UNSET)

        ban_reason = d.pop("banReason", UNSET)

        _ban_expires = d.pop("banExpires", UNSET)
        ban_expires: datetime.date | Unset
        if isinstance(_ban_expires, Unset):
            ban_expires = UNSET
        else:
            ban_expires = isoparse(_ban_expires).date()

        onboarding_complete = d.pop("onboardingComplete", UNSET)

        locale = d.pop("locale", UNSET)

        user = cls(
            id=id,
            name=name,
            email=email,
            email_verified=email_verified,
            image=image,
            created_at=created_at,
            updated_at=updated_at,
            username=username,
            role=role,
            banned=banned,
            ban_reason=ban_reason,
            ban_expires=ban_expires,
            onboarding_complete=onboarding_complete,
            locale=locale,
        )

        user.additional_properties = d
        return user

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
