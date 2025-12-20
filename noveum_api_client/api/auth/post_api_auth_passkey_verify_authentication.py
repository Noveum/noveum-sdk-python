from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_auth_passkey_verify_authentication_body import PostApiAuthPasskeyVerifyAuthenticationBody
from ...models.post_api_auth_passkey_verify_authentication_response_200 import (
    PostApiAuthPasskeyVerifyAuthenticationResponse200,
)
from ...models.post_api_auth_passkey_verify_authentication_response_400 import (
    PostApiAuthPasskeyVerifyAuthenticationResponse400,
)
from ...models.post_api_auth_passkey_verify_authentication_response_401 import (
    PostApiAuthPasskeyVerifyAuthenticationResponse401,
)
from ...models.post_api_auth_passkey_verify_authentication_response_403 import (
    PostApiAuthPasskeyVerifyAuthenticationResponse403,
)
from ...models.post_api_auth_passkey_verify_authentication_response_404 import (
    PostApiAuthPasskeyVerifyAuthenticationResponse404,
)
from ...models.post_api_auth_passkey_verify_authentication_response_429 import (
    PostApiAuthPasskeyVerifyAuthenticationResponse429,
)
from ...models.post_api_auth_passkey_verify_authentication_response_500 import (
    PostApiAuthPasskeyVerifyAuthenticationResponse500,
)
from ...types import Response


def _get_kwargs(
    *,
    body: PostApiAuthPasskeyVerifyAuthenticationBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/passkey/verify-authentication",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostApiAuthPasskeyVerifyAuthenticationResponse200
    | PostApiAuthPasskeyVerifyAuthenticationResponse400
    | PostApiAuthPasskeyVerifyAuthenticationResponse401
    | PostApiAuthPasskeyVerifyAuthenticationResponse403
    | PostApiAuthPasskeyVerifyAuthenticationResponse404
    | PostApiAuthPasskeyVerifyAuthenticationResponse429
    | PostApiAuthPasskeyVerifyAuthenticationResponse500
    | None
):
    if response.status_code == 200:
        response_200 = PostApiAuthPasskeyVerifyAuthenticationResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PostApiAuthPasskeyVerifyAuthenticationResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostApiAuthPasskeyVerifyAuthenticationResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostApiAuthPasskeyVerifyAuthenticationResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostApiAuthPasskeyVerifyAuthenticationResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = PostApiAuthPasskeyVerifyAuthenticationResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PostApiAuthPasskeyVerifyAuthenticationResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostApiAuthPasskeyVerifyAuthenticationResponse200
    | PostApiAuthPasskeyVerifyAuthenticationResponse400
    | PostApiAuthPasskeyVerifyAuthenticationResponse401
    | PostApiAuthPasskeyVerifyAuthenticationResponse403
    | PostApiAuthPasskeyVerifyAuthenticationResponse404
    | PostApiAuthPasskeyVerifyAuthenticationResponse429
    | PostApiAuthPasskeyVerifyAuthenticationResponse500
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
    body: PostApiAuthPasskeyVerifyAuthenticationBody,
) -> Response[
    PostApiAuthPasskeyVerifyAuthenticationResponse200
    | PostApiAuthPasskeyVerifyAuthenticationResponse400
    | PostApiAuthPasskeyVerifyAuthenticationResponse401
    | PostApiAuthPasskeyVerifyAuthenticationResponse403
    | PostApiAuthPasskeyVerifyAuthenticationResponse404
    | PostApiAuthPasskeyVerifyAuthenticationResponse429
    | PostApiAuthPasskeyVerifyAuthenticationResponse500
]:
    """Verify authentication of a passkey

    Args:
        body (PostApiAuthPasskeyVerifyAuthenticationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthPasskeyVerifyAuthenticationResponse200 | PostApiAuthPasskeyVerifyAuthenticationResponse400 | PostApiAuthPasskeyVerifyAuthenticationResponse401 | PostApiAuthPasskeyVerifyAuthenticationResponse403 | PostApiAuthPasskeyVerifyAuthenticationResponse404 | PostApiAuthPasskeyVerifyAuthenticationResponse429 | PostApiAuthPasskeyVerifyAuthenticationResponse500]
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
    body: PostApiAuthPasskeyVerifyAuthenticationBody,
) -> (
    PostApiAuthPasskeyVerifyAuthenticationResponse200
    | PostApiAuthPasskeyVerifyAuthenticationResponse400
    | PostApiAuthPasskeyVerifyAuthenticationResponse401
    | PostApiAuthPasskeyVerifyAuthenticationResponse403
    | PostApiAuthPasskeyVerifyAuthenticationResponse404
    | PostApiAuthPasskeyVerifyAuthenticationResponse429
    | PostApiAuthPasskeyVerifyAuthenticationResponse500
    | None
):
    """Verify authentication of a passkey

    Args:
        body (PostApiAuthPasskeyVerifyAuthenticationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthPasskeyVerifyAuthenticationResponse200 | PostApiAuthPasskeyVerifyAuthenticationResponse400 | PostApiAuthPasskeyVerifyAuthenticationResponse401 | PostApiAuthPasskeyVerifyAuthenticationResponse403 | PostApiAuthPasskeyVerifyAuthenticationResponse404 | PostApiAuthPasskeyVerifyAuthenticationResponse429 | PostApiAuthPasskeyVerifyAuthenticationResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthPasskeyVerifyAuthenticationBody,
) -> Response[
    PostApiAuthPasskeyVerifyAuthenticationResponse200
    | PostApiAuthPasskeyVerifyAuthenticationResponse400
    | PostApiAuthPasskeyVerifyAuthenticationResponse401
    | PostApiAuthPasskeyVerifyAuthenticationResponse403
    | PostApiAuthPasskeyVerifyAuthenticationResponse404
    | PostApiAuthPasskeyVerifyAuthenticationResponse429
    | PostApiAuthPasskeyVerifyAuthenticationResponse500
]:
    """Verify authentication of a passkey

    Args:
        body (PostApiAuthPasskeyVerifyAuthenticationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthPasskeyVerifyAuthenticationResponse200 | PostApiAuthPasskeyVerifyAuthenticationResponse400 | PostApiAuthPasskeyVerifyAuthenticationResponse401 | PostApiAuthPasskeyVerifyAuthenticationResponse403 | PostApiAuthPasskeyVerifyAuthenticationResponse404 | PostApiAuthPasskeyVerifyAuthenticationResponse429 | PostApiAuthPasskeyVerifyAuthenticationResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthPasskeyVerifyAuthenticationBody,
) -> (
    PostApiAuthPasskeyVerifyAuthenticationResponse200
    | PostApiAuthPasskeyVerifyAuthenticationResponse400
    | PostApiAuthPasskeyVerifyAuthenticationResponse401
    | PostApiAuthPasskeyVerifyAuthenticationResponse403
    | PostApiAuthPasskeyVerifyAuthenticationResponse404
    | PostApiAuthPasskeyVerifyAuthenticationResponse429
    | PostApiAuthPasskeyVerifyAuthenticationResponse500
    | None
):
    """Verify authentication of a passkey

    Args:
        body (PostApiAuthPasskeyVerifyAuthenticationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthPasskeyVerifyAuthenticationResponse200 | PostApiAuthPasskeyVerifyAuthenticationResponse400 | PostApiAuthPasskeyVerifyAuthenticationResponse401 | PostApiAuthPasskeyVerifyAuthenticationResponse403 | PostApiAuthPasskeyVerifyAuthenticationResponse404 | PostApiAuthPasskeyVerifyAuthenticationResponse429 | PostApiAuthPasskeyVerifyAuthenticationResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
