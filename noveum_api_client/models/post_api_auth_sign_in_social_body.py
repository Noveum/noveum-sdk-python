from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiAuthSignInSocialBody")


@_attrs_define
class PostApiAuthSignInSocialBody:
    """
    Attributes:
        provider (str): OAuth2 provider to use
        callback_url (str | Unset): Callback URL to redirect to after the user has signed in
        new_user_callback_url (str | Unset):
        error_callback_url (str | Unset): Callback URL to redirect to if an error happens
        disable_redirect (str | Unset): Disable automatic redirection to the provider. Useful for handling the
            redirection yourself
        id_token (str | Unset): ID token from the provider to sign in the user with id token
    """

    provider: str
    callback_url: str | Unset = UNSET
    new_user_callback_url: str | Unset = UNSET
    error_callback_url: str | Unset = UNSET
    disable_redirect: str | Unset = UNSET
    id_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider

        callback_url = self.callback_url

        new_user_callback_url = self.new_user_callback_url

        error_callback_url = self.error_callback_url

        disable_redirect = self.disable_redirect

        id_token = self.id_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
            }
        )
        if callback_url is not UNSET:
            field_dict["callbackURL"] = callback_url
        if new_user_callback_url is not UNSET:
            field_dict["newUserCallbackURL"] = new_user_callback_url
        if error_callback_url is not UNSET:
            field_dict["errorCallbackURL"] = error_callback_url
        if disable_redirect is not UNSET:
            field_dict["disableRedirect"] = disable_redirect
        if id_token is not UNSET:
            field_dict["idToken"] = id_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider = d.pop("provider")

        callback_url = d.pop("callbackURL", UNSET)

        new_user_callback_url = d.pop("newUserCallbackURL", UNSET)

        error_callback_url = d.pop("errorCallbackURL", UNSET)

        disable_redirect = d.pop("disableRedirect", UNSET)

        id_token = d.pop("idToken", UNSET)

        post_api_auth_sign_in_social_body = cls(
            provider=provider,
            callback_url=callback_url,
            new_user_callback_url=new_user_callback_url,
            error_callback_url=error_callback_url,
            disable_redirect=disable_redirect,
            id_token=id_token,
        )

        post_api_auth_sign_in_social_body.additional_properties = d
        return post_api_auth_sign_in_social_body

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
