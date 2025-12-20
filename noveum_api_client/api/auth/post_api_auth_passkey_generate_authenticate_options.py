from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_auth_passkey_generate_authenticate_options_response_200 import (
    PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200,
)
from ...models.post_api_auth_passkey_generate_authenticate_options_response_400 import (
    PostApiAuthPasskeyGenerateAuthenticateOptionsResponse400,
)
from ...models.post_api_auth_passkey_generate_authenticate_options_response_401 import (
    PostApiAuthPasskeyGenerateAuthenticateOptionsResponse401,
)
from ...models.post_api_auth_passkey_generate_authenticate_options_response_403 import (
    PostApiAuthPasskeyGenerateAuthenticateOptionsResponse403,
)
from ...models.post_api_auth_passkey_generate_authenticate_options_response_404 import (
    PostApiAuthPasskeyGenerateAuthenticateOptionsResponse404,
)
from ...models.post_api_auth_passkey_generate_authenticate_options_response_429 import (
    PostApiAuthPasskeyGenerateAuthenticateOptionsResponse429,
)
from ...models.post_api_auth_passkey_generate_authenticate_options_response_500 import (
    PostApiAuthPasskeyGenerateAuthenticateOptionsResponse500,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/passkey/generate-authenticate-options",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse400
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse401
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse403
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse404
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse429
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse500
    | None
):
    if response.status_code == 200:
        response_200 = PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PostApiAuthPasskeyGenerateAuthenticateOptionsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostApiAuthPasskeyGenerateAuthenticateOptionsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostApiAuthPasskeyGenerateAuthenticateOptionsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostApiAuthPasskeyGenerateAuthenticateOptionsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = PostApiAuthPasskeyGenerateAuthenticateOptionsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PostApiAuthPasskeyGenerateAuthenticateOptionsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse400
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse401
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse403
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse404
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse429
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse500
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
) -> Response[
    PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse400
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse401
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse403
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse404
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse429
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse500
]:
    """Generate authentication options for a passkey

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200 | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse400 | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse401 | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse403 | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse404 | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse429 | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse500]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> (
    PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse400
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse401
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse403
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse404
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse429
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse500
    | None
):
    """Generate authentication options for a passkey

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200 | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse400 | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse401 | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse403 | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse404 | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse429 | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse500
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse400
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse401
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse403
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse404
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse429
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse500
]:
    """Generate authentication options for a passkey

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200 | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse400 | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse401 | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse403 | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse404 | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse429 | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse500]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> (
    PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse400
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse401
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse403
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse404
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse429
    | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse500
    | None
):
    """Generate authentication options for a passkey

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthPasskeyGenerateAuthenticateOptionsResponse200 | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse400 | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse401 | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse403 | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse404 | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse429 | PostApiAuthPasskeyGenerateAuthenticateOptionsResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
