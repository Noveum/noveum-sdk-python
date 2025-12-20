from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApiAuthOrganizationGetActiveMemberResponse200")


@_attrs_define
class GetApiAuthOrganizationGetActiveMemberResponse200:
    """
    Attributes:
        id (str):
        user_id (str):
        organization_id (str):
        role (str):
    """

    id: str
    user_id: str
    organization_id: str
    role: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        organization_id = self.organization_id

        role = self.role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "userId": user_id,
                "organizationId": organization_id,
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("userId")

        organization_id = d.pop("organizationId")

        role = d.pop("role")

        get_api_auth_organization_get_active_member_response_200 = cls(
            id=id,
            user_id=user_id,
            organization_id=organization_id,
            role=role,
        )

        get_api_auth_organization_get_active_member_response_200.additional_properties = d
        return get_api_auth_organization_get_active_member_response_200

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
