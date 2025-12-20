from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_api_auth_sign_in_social_response_200_user import PostApiAuthSignInSocialResponse200User


T = TypeVar("T", bound="PostApiAuthSignInSocialResponse200")


@_attrs_define
class PostApiAuthSignInSocialResponse200:
    """
    Attributes:
        session (str):
        user (PostApiAuthSignInSocialResponse200User):
        url (str):
        redirect (bool):
    """

    session: str
    user: PostApiAuthSignInSocialResponse200User
    url: str
    redirect: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        session = self.session

        user = self.user.to_dict()

        url = self.url

        redirect = self.redirect

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "session": session,
                "user": user,
                "url": url,
                "redirect": redirect,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_auth_sign_in_social_response_200_user import PostApiAuthSignInSocialResponse200User

        d = dict(src_dict)
        session = d.pop("session")

        user = PostApiAuthSignInSocialResponse200User.from_dict(d.pop("user"))

        url = d.pop("url")

        redirect = d.pop("redirect")

        post_api_auth_sign_in_social_response_200 = cls(
            session=session,
            user=user,
            url=url,
            redirect=redirect,
        )

        post_api_auth_sign_in_social_response_200.additional_properties = d
        return post_api_auth_sign_in_social_response_200

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
