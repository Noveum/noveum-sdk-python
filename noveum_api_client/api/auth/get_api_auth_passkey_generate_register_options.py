from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_auth_passkey_generate_register_options_response_200 import (
    GetApiAuthPasskeyGenerateRegisterOptionsResponse200,
)
from ...models.get_api_auth_passkey_generate_register_options_response_400 import (
    GetApiAuthPasskeyGenerateRegisterOptionsResponse400,
)
from ...models.get_api_auth_passkey_generate_register_options_response_401 import (
    GetApiAuthPasskeyGenerateRegisterOptionsResponse401,
)
from ...models.get_api_auth_passkey_generate_register_options_response_403 import (
    GetApiAuthPasskeyGenerateRegisterOptionsResponse403,
)
from ...models.get_api_auth_passkey_generate_register_options_response_404 import (
    GetApiAuthPasskeyGenerateRegisterOptionsResponse404,
)
from ...models.get_api_auth_passkey_generate_register_options_response_429 import (
    GetApiAuthPasskeyGenerateRegisterOptionsResponse429,
)
from ...models.get_api_auth_passkey_generate_register_options_response_500 import (
    GetApiAuthPasskeyGenerateRegisterOptionsResponse500,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/auth/passkey/generate-register-options",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetApiAuthPasskeyGenerateRegisterOptionsResponse200
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse400
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse401
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse403
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse404
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse429
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse500
    | None
):
    if response.status_code == 200:
        response_200 = GetApiAuthPasskeyGenerateRegisterOptionsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetApiAuthPasskeyGenerateRegisterOptionsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetApiAuthPasskeyGenerateRegisterOptionsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetApiAuthPasskeyGenerateRegisterOptionsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetApiAuthPasskeyGenerateRegisterOptionsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = GetApiAuthPasskeyGenerateRegisterOptionsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetApiAuthPasskeyGenerateRegisterOptionsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetApiAuthPasskeyGenerateRegisterOptionsResponse200
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse400
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse401
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse403
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse404
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse429
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse500
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
    GetApiAuthPasskeyGenerateRegisterOptionsResponse200
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse400
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse401
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse403
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse404
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse429
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse500
]:
    """Generate registration options for a new passkey

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiAuthPasskeyGenerateRegisterOptionsResponse200 | GetApiAuthPasskeyGenerateRegisterOptionsResponse400 | GetApiAuthPasskeyGenerateRegisterOptionsResponse401 | GetApiAuthPasskeyGenerateRegisterOptionsResponse403 | GetApiAuthPasskeyGenerateRegisterOptionsResponse404 | GetApiAuthPasskeyGenerateRegisterOptionsResponse429 | GetApiAuthPasskeyGenerateRegisterOptionsResponse500]
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
    GetApiAuthPasskeyGenerateRegisterOptionsResponse200
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse400
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse401
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse403
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse404
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse429
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse500
    | None
):
    """Generate registration options for a new passkey

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiAuthPasskeyGenerateRegisterOptionsResponse200 | GetApiAuthPasskeyGenerateRegisterOptionsResponse400 | GetApiAuthPasskeyGenerateRegisterOptionsResponse401 | GetApiAuthPasskeyGenerateRegisterOptionsResponse403 | GetApiAuthPasskeyGenerateRegisterOptionsResponse404 | GetApiAuthPasskeyGenerateRegisterOptionsResponse429 | GetApiAuthPasskeyGenerateRegisterOptionsResponse500
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    GetApiAuthPasskeyGenerateRegisterOptionsResponse200
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse400
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse401
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse403
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse404
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse429
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse500
]:
    """Generate registration options for a new passkey

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiAuthPasskeyGenerateRegisterOptionsResponse200 | GetApiAuthPasskeyGenerateRegisterOptionsResponse400 | GetApiAuthPasskeyGenerateRegisterOptionsResponse401 | GetApiAuthPasskeyGenerateRegisterOptionsResponse403 | GetApiAuthPasskeyGenerateRegisterOptionsResponse404 | GetApiAuthPasskeyGenerateRegisterOptionsResponse429 | GetApiAuthPasskeyGenerateRegisterOptionsResponse500]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> (
    GetApiAuthPasskeyGenerateRegisterOptionsResponse200
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse400
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse401
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse403
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse404
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse429
    | GetApiAuthPasskeyGenerateRegisterOptionsResponse500
    | None
):
    """Generate registration options for a new passkey

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiAuthPasskeyGenerateRegisterOptionsResponse200 | GetApiAuthPasskeyGenerateRegisterOptionsResponse400 | GetApiAuthPasskeyGenerateRegisterOptionsResponse401 | GetApiAuthPasskeyGenerateRegisterOptionsResponse403 | GetApiAuthPasskeyGenerateRegisterOptionsResponse404 | GetApiAuthPasskeyGenerateRegisterOptionsResponse429 | GetApiAuthPasskeyGenerateRegisterOptionsResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
