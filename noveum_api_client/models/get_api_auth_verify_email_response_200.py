from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_auth_verify_email_response_200_user import GetApiAuthVerifyEmailResponse200User


T = TypeVar("T", bound="GetApiAuthVerifyEmailResponse200")


@_attrs_define
class GetApiAuthVerifyEmailResponse200:
    """
    Attributes:
        user (GetApiAuthVerifyEmailResponse200User):
        status (bool):
    """

    user: GetApiAuthVerifyEmailResponse200User
    status: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user = self.user.to_dict()

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_auth_verify_email_response_200_user import GetApiAuthVerifyEmailResponse200User

        d = dict(src_dict)
        user = GetApiAuthVerifyEmailResponse200User.from_dict(d.pop("user"))

        status = d.pop("status")

        get_api_auth_verify_email_response_200 = cls(
            user=user,
            status=status,
        )

        get_api_auth_verify_email_response_200.additional_properties = d
        return get_api_auth_verify_email_response_200

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
