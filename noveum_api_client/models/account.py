from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Account")


@_attrs_define
class Account:
    """
    Attributes:
        id (str | Unset):
        account_id (str | Unset):
        provider_id (str | Unset):
        user_id (str | Unset):
        access_token (str | Unset):
        refresh_token (str | Unset):
        id_token (str | Unset):
        access_token_expires_at (datetime.date | Unset):
        refresh_token_expires_at (datetime.date | Unset):
        scope (str | Unset):
        password (str | Unset):
        created_at (datetime.date | Unset):
        updated_at (datetime.date | Unset):
    """

    id: str | Unset = UNSET
    account_id: str | Unset = UNSET
    provider_id: str | Unset = UNSET
    user_id: str | Unset = UNSET
    access_token: str | Unset = UNSET
    refresh_token: str | Unset = UNSET
    id_token: str | Unset = UNSET
    access_token_expires_at: datetime.date | Unset = UNSET
    refresh_token_expires_at: datetime.date | Unset = UNSET
    scope: str | Unset = UNSET
    password: str | Unset = UNSET
    created_at: datetime.date | Unset = UNSET
    updated_at: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        account_id = self.account_id

        provider_id = self.provider_id

        user_id = self.user_id

        access_token = self.access_token

        refresh_token = self.refresh_token

        id_token = self.id_token

        access_token_expires_at: str | Unset = UNSET
        if not isinstance(self.access_token_expires_at, Unset):
            access_token_expires_at = self.access_token_expires_at.isoformat()

        refresh_token_expires_at: str | Unset = UNSET
        if not isinstance(self.refresh_token_expires_at, Unset):
            refresh_token_expires_at = self.refresh_token_expires_at.isoformat()

        scope = self.scope

        password = self.password

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if provider_id is not UNSET:
            field_dict["providerId"] = provider_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if access_token is not UNSET:
            field_dict["accessToken"] = access_token
        if refresh_token is not UNSET:
            field_dict["refreshToken"] = refresh_token
        if id_token is not UNSET:
            field_dict["idToken"] = id_token
        if access_token_expires_at is not UNSET:
            field_dict["accessTokenExpiresAt"] = access_token_expires_at
        if refresh_token_expires_at is not UNSET:
            field_dict["refreshTokenExpiresAt"] = refresh_token_expires_at
        if scope is not UNSET:
            field_dict["scope"] = scope
        if password is not UNSET:
            field_dict["password"] = password
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        account_id = d.pop("accountId", UNSET)

        provider_id = d.pop("providerId", UNSET)

        user_id = d.pop("userId", UNSET)

        access_token = d.pop("accessToken", UNSET)

        refresh_token = d.pop("refreshToken", UNSET)

        id_token = d.pop("idToken", UNSET)

        _access_token_expires_at = d.pop("accessTokenExpiresAt", UNSET)
        access_token_expires_at: datetime.date | Unset
        if isinstance(_access_token_expires_at, Unset):
            access_token_expires_at = UNSET
        else:
            access_token_expires_at = isoparse(_access_token_expires_at).date()

        _refresh_token_expires_at = d.pop("refreshTokenExpiresAt", UNSET)
        refresh_token_expires_at: datetime.date | Unset
        if isinstance(_refresh_token_expires_at, Unset):
            refresh_token_expires_at = UNSET
        else:
            refresh_token_expires_at = isoparse(_refresh_token_expires_at).date()

        scope = d.pop("scope", UNSET)

        password = d.pop("password", UNSET)

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

        account = cls(
            id=id,
            account_id=account_id,
            provider_id=provider_id,
            user_id=user_id,
            access_token=access_token,
            refresh_token=refresh_token,
            id_token=id_token,
            access_token_expires_at=access_token_expires_at,
            refresh_token_expires_at=refresh_token_expires_at,
            scope=scope,
            password=password,
            created_at=created_at,
            updated_at=updated_at,
        )

        account.additional_properties = d
        return account

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
