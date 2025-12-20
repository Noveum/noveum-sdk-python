from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.passkey import Passkey
from ...models.post_api_auth_passkey_verify_registration_body import PostApiAuthPasskeyVerifyRegistrationBody
from ...models.post_api_auth_passkey_verify_registration_response_401 import (
    PostApiAuthPasskeyVerifyRegistrationResponse401,
)
from ...models.post_api_auth_passkey_verify_registration_response_403 import (
    PostApiAuthPasskeyVerifyRegistrationResponse403,
)
from ...models.post_api_auth_passkey_verify_registration_response_404 import (
    PostApiAuthPasskeyVerifyRegistrationResponse404,
)
from ...models.post_api_auth_passkey_verify_registration_response_429 import (
    PostApiAuthPasskeyVerifyRegistrationResponse429,
)
from ...models.post_api_auth_passkey_verify_registration_response_500 import (
    PostApiAuthPasskeyVerifyRegistrationResponse500,
)
from ...types import Response


def _get_kwargs(
    *,
    body: PostApiAuthPasskeyVerifyRegistrationBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/passkey/verify-registration",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | Passkey
    | PostApiAuthPasskeyVerifyRegistrationResponse401
    | PostApiAuthPasskeyVerifyRegistrationResponse403
    | PostApiAuthPasskeyVerifyRegistrationResponse404
    | PostApiAuthPasskeyVerifyRegistrationResponse429
    | PostApiAuthPasskeyVerifyRegistrationResponse500
    | None
):
    if response.status_code == 200:
        response_200 = Passkey.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = PostApiAuthPasskeyVerifyRegistrationResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostApiAuthPasskeyVerifyRegistrationResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostApiAuthPasskeyVerifyRegistrationResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = PostApiAuthPasskeyVerifyRegistrationResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PostApiAuthPasskeyVerifyRegistrationResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | Passkey
    | PostApiAuthPasskeyVerifyRegistrationResponse401
    | PostApiAuthPasskeyVerifyRegistrationResponse403
    | PostApiAuthPasskeyVerifyRegistrationResponse404
    | PostApiAuthPasskeyVerifyRegistrationResponse429
    | PostApiAuthPasskeyVerifyRegistrationResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthPasskeyVerifyRegistrationBody,
) -> Response[
    Any
    | Passkey
    | PostApiAuthPasskeyVerifyRegistrationResponse401
    | PostApiAuthPasskeyVerifyRegistrationResponse403
    | PostApiAuthPasskeyVerifyRegistrationResponse404
    | PostApiAuthPasskeyVerifyRegistrationResponse429
    | PostApiAuthPasskeyVerifyRegistrationResponse500
]:
    """Verify registration of a new passkey

    Args:
        body (PostApiAuthPasskeyVerifyRegistrationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Passkey | PostApiAuthPasskeyVerifyRegistrationResponse401 | PostApiAuthPasskeyVerifyRegistrationResponse403 | PostApiAuthPasskeyVerifyRegistrationResponse404 | PostApiAuthPasskeyVerifyRegistrationResponse429 | PostApiAuthPasskeyVerifyRegistrationResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthPasskeyVerifyRegistrationBody,
) -> (
    Any
    | Passkey
    | PostApiAuthPasskeyVerifyRegistrationResponse401
    | PostApiAuthPasskeyVerifyRegistrationResponse403
    | PostApiAuthPasskeyVerifyRegistrationResponse404
    | PostApiAuthPasskeyVerifyRegistrationResponse429
    | PostApiAuthPasskeyVerifyRegistrationResponse500
    | None
):
    """Verify registration of a new passkey

    Args:
        body (PostApiAuthPasskeyVerifyRegistrationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Passkey | PostApiAuthPasskeyVerifyRegistrationResponse401 | PostApiAuthPasskeyVerifyRegistrationResponse403 | PostApiAuthPasskeyVerifyRegistrationResponse404 | PostApiAuthPasskeyVerifyRegistrationResponse429 | PostApiAuthPasskeyVerifyRegistrationResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthPasskeyVerifyRegistrationBody,
) -> Response[
    Any
    | Passkey
    | PostApiAuthPasskeyVerifyRegistrationResponse401
    | PostApiAuthPasskeyVerifyRegistrationResponse403
    | PostApiAuthPasskeyVerifyRegistrationResponse404
    | PostApiAuthPasskeyVerifyRegistrationResponse429
    | PostApiAuthPasskeyVerifyRegistrationResponse500
]:
    """Verify registration of a new passkey

    Args:
        body (PostApiAuthPasskeyVerifyRegistrationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Passkey | PostApiAuthPasskeyVerifyRegistrationResponse401 | PostApiAuthPasskeyVerifyRegistrationResponse403 | PostApiAuthPasskeyVerifyRegistrationResponse404 | PostApiAuthPasskeyVerifyRegistrationResponse429 | PostApiAuthPasskeyVerifyRegistrationResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthPasskeyVerifyRegistrationBody,
) -> (
    Any
    | Passkey
    | PostApiAuthPasskeyVerifyRegistrationResponse401
    | PostApiAuthPasskeyVerifyRegistrationResponse403
    | PostApiAuthPasskeyVerifyRegistrationResponse404
    | PostApiAuthPasskeyVerifyRegistrationResponse429
    | PostApiAuthPasskeyVerifyRegistrationResponse500
    | None
):
    """Verify registration of a new passkey

    Args:
        body (PostApiAuthPasskeyVerifyRegistrationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Passkey | PostApiAuthPasskeyVerifyRegistrationResponse401 | PostApiAuthPasskeyVerifyRegistrationResponse403 | PostApiAuthPasskeyVerifyRegistrationResponse404 | PostApiAuthPasskeyVerifyRegistrationResponse429 | PostApiAuthPasskeyVerifyRegistrationResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
