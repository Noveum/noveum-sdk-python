from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.get_api_by_organisation_slug_api_keys_response_200_api_keys_item_user import (
        GetApiByOrganisationSlugApiKeysResponse200ApiKeysItemUser,
    )


T = TypeVar("T", bound="GetApiByOrganisationSlugApiKeysResponse200ApiKeysItem")


@_attrs_define
class GetApiByOrganisationSlugApiKeysResponse200ApiKeysItem:
    """
    Attributes:
        id (str):
        title (str):
        key (str):
        expires_at (datetime.datetime | None):
        created_at (str):
        user (GetApiByOrganisationSlugApiKeysResponse200ApiKeysItemUser):
    """

    id: str
    title: str
    key: str
    expires_at: datetime.datetime | None
    created_at: str
    user: GetApiByOrganisationSlugApiKeysResponse200ApiKeysItemUser
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        key = self.key

        expires_at: None | str
        if isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        created_at = self.created_at

        user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "key": key,
                "expiresAt": expires_at,
                "createdAt": created_at,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_by_organisation_slug_api_keys_response_200_api_keys_item_user import (
            GetApiByOrganisationSlugApiKeysResponse200ApiKeysItemUser,
        )

        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        key = d.pop("key")

        def _parse_expires_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = isoparse(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        expires_at = _parse_expires_at(d.pop("expiresAt"))

        created_at = d.pop("createdAt")

        user = GetApiByOrganisationSlugApiKeysResponse200ApiKeysItemUser.from_dict(d.pop("user"))

        get_api_by_organisation_slug_api_keys_response_200_api_keys_item = cls(
            id=id,
            title=title,
            key=key,
            expires_at=expires_at,
            created_at=created_at,
            user=user,
        )

        get_api_by_organisation_slug_api_keys_response_200_api_keys_item.additional_properties = d
        return get_api_by_organisation_slug_api_keys_response_200_api_keys_item

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
