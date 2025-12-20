from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_auth_passkey_generate_authenticate_options_response_200_allow_credentials_item import (
        PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200AllowCredentialsItem,
    )
    from ..models.post_api_auth_passkey_generate_authenticate_options_response_200_authenticator_selection import (
        PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200AuthenticatorSelection,
    )
    from ..models.post_api_auth_passkey_generate_authenticate_options_response_200_extensions import (
        PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200Extensions,
    )
    from ..models.post_api_auth_passkey_generate_authenticate_options_response_200_rp import (
        PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200Rp,
    )
    from ..models.post_api_auth_passkey_generate_authenticate_options_response_200_user import (
        PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200User,
    )


T = TypeVar("T", bound="PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200")


@_attrs_define
class PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200:
    """
    Attributes:
        challenge (str | Unset):
        rp (PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200Rp | Unset):
        user (PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200User | Unset):
        timeout (float | Unset):
        allow_credentials (list[PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200AllowCredentialsItem] | Unset):
        user_verification (str | Unset):
        authenticator_selection (PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200AuthenticatorSelection |
            Unset):
        extensions (PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200Extensions | Unset):
    """

    challenge: str | Unset = UNSET
    rp: PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200Rp | Unset = UNSET
    user: PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200User | Unset = UNSET
    timeout: float | Unset = UNSET
    allow_credentials: list[PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200AllowCredentialsItem] | Unset = (
        UNSET
    )
    user_verification: str | Unset = UNSET
    authenticator_selection: PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200AuthenticatorSelection | Unset = (
        UNSET
    )
    extensions: PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200Extensions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        challenge = self.challenge

        rp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rp, Unset):
            rp = self.rp.to_dict()

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        timeout = self.timeout

        allow_credentials: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.allow_credentials, Unset):
            allow_credentials = []
            for allow_credentials_item_data in self.allow_credentials:
                allow_credentials_item = allow_credentials_item_data.to_dict()
                allow_credentials.append(allow_credentials_item)

        user_verification = self.user_verification

        authenticator_selection: dict[str, Any] | Unset = UNSET
        if not isinstance(self.authenticator_selection, Unset):
            authenticator_selection = self.authenticator_selection.to_dict()

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if challenge is not UNSET:
            field_dict["challenge"] = challenge
        if rp is not UNSET:
            field_dict["rp"] = rp
        if user is not UNSET:
            field_dict["user"] = user
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if allow_credentials is not UNSET:
            field_dict["allowCredentials"] = allow_credentials
        if user_verification is not UNSET:
            field_dict["userVerification"] = user_verification
        if authenticator_selection is not UNSET:
            field_dict["authenticatorSelection"] = authenticator_selection
        if extensions is not UNSET:
            field_dict["extensions"] = extensions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_auth_passkey_generate_authenticate_options_response_200_allow_credentials_item import (
            PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200AllowCredentialsItem,
        )
        from ..models.post_api_auth_passkey_generate_authenticate_options_response_200_authenticator_selection import (
            PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200AuthenticatorSelection,
        )
        from ..models.post_api_auth_passkey_generate_authenticate_options_response_200_extensions import (
            PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200Extensions,
        )
        from ..models.post_api_auth_passkey_generate_authenticate_options_response_200_rp import (
            PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200Rp,
        )
        from ..models.post_api_auth_passkey_generate_authenticate_options_response_200_user import (
            PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200User,
        )

        d = dict(src_dict)
        challenge = d.pop("challenge", UNSET)

        _rp = d.pop("rp", UNSET)
        rp: PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200Rp | Unset
        if isinstance(_rp, Unset):
            rp = UNSET
        else:
            rp = PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200Rp.from_dict(_rp)

        _user = d.pop("user", UNSET)
        user: PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200User | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200User.from_dict(_user)

        timeout = d.pop("timeout", UNSET)

        _allow_credentials = d.pop("allowCredentials", UNSET)
        allow_credentials: (
            list[PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200AllowCredentialsItem] | Unset
        ) = UNSET
        if _allow_credentials is not UNSET:
            allow_credentials = []
            for allow_credentials_item_data in _allow_credentials:
                allow_credentials_item = (
                    PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200AllowCredentialsItem.from_dict(
                        allow_credentials_item_data
                    )
                )

                allow_credentials.append(allow_credentials_item)

        user_verification = d.pop("userVerification", UNSET)

        _authenticator_selection = d.pop("authenticatorSelection", UNSET)
        authenticator_selection: PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200AuthenticatorSelection | Unset
        if isinstance(_authenticator_selection, Unset):
            authenticator_selection = UNSET
        else:
            authenticator_selection = (
                PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200AuthenticatorSelection.from_dict(
                    _authenticator_selection
                )
            )

        _extensions = d.pop("extensions", UNSET)
        extensions: PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200Extensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200Extensions.from_dict(_extensions)

        post_api_auth_passkey_generate_authenticate_options_response_200 = cls(
            challenge=challenge,
            rp=rp,
            user=user,
            timeout=timeout,
            allow_credentials=allow_credentials,
            user_verification=user_verification,
            authenticator_selection=authenticator_selection,
            extensions=extensions,
        )

        post_api_auth_passkey_generate_authenticate_options_response_200.additional_properties = d
        return post_api_auth_passkey_generate_authenticate_options_response_200

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
