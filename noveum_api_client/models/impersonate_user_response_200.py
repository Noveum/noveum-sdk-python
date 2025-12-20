from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.session import Session
    from ..models.user import User


T = TypeVar("T", bound="ImpersonateUserResponse200")


@_attrs_define
class ImpersonateUserResponse200:
    """
    Attributes:
        session (Session | Unset):
        user (User | Unset):
    """

    session: Session | Unset = UNSET
    user: User | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        session: dict[str, Any] | Unset = UNSET
        if not isinstance(self.session, Unset):
            session = self.session.to_dict()

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if session is not UNSET:
            field_dict["session"] = session
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session import Session
        from ..models.user import User

        d = dict(src_dict)
        _session = d.pop("session", UNSET)
        session: Session | Unset
        if isinstance(_session, Unset):
            session = UNSET
        else:
            session = Session.from_dict(_session)

        _user = d.pop("user", UNSET)
        user: User | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = User.from_dict(_user)

        impersonate_user_response_200 = cls(
            session=session,
            user=user,
        )

        impersonate_user_response_200.additional_properties = d
        return impersonate_user_response_200

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
