from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_auth_list_accounts_response_200_item import GetApiAuthListAccountsResponse200Item
from ...models.get_api_auth_list_accounts_response_400 import GetApiAuthListAccountsResponse400
from ...models.get_api_auth_list_accounts_response_401 import GetApiAuthListAccountsResponse401
from ...models.get_api_auth_list_accounts_response_403 import GetApiAuthListAccountsResponse403
from ...models.get_api_auth_list_accounts_response_404 import GetApiAuthListAccountsResponse404
from ...models.get_api_auth_list_accounts_response_429 import GetApiAuthListAccountsResponse429
from ...models.get_api_auth_list_accounts_response_500 import GetApiAuthListAccountsResponse500
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/auth/list-accounts",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetApiAuthListAccountsResponse400
    | GetApiAuthListAccountsResponse401
    | GetApiAuthListAccountsResponse403
    | GetApiAuthListAccountsResponse404
    | GetApiAuthListAccountsResponse429
    | GetApiAuthListAccountsResponse500
    | list[GetApiAuthListAccountsResponse200Item]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetApiAuthListAccountsResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = GetApiAuthListAccountsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetApiAuthListAccountsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetApiAuthListAccountsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetApiAuthListAccountsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = GetApiAuthListAccountsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetApiAuthListAccountsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetApiAuthListAccountsResponse400
    | GetApiAuthListAccountsResponse401
    | GetApiAuthListAccountsResponse403
    | GetApiAuthListAccountsResponse404
    | GetApiAuthListAccountsResponse429
    | GetApiAuthListAccountsResponse500
    | list[GetApiAuthListAccountsResponse200Item]
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
    GetApiAuthListAccountsResponse400
    | GetApiAuthListAccountsResponse401
    | GetApiAuthListAccountsResponse403
    | GetApiAuthListAccountsResponse404
    | GetApiAuthListAccountsResponse429
    | GetApiAuthListAccountsResponse500
    | list[GetApiAuthListAccountsResponse200Item]
]:
    """List all accounts linked to the user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiAuthListAccountsResponse400 | GetApiAuthListAccountsResponse401 | GetApiAuthListAccountsResponse403 | GetApiAuthListAccountsResponse404 | GetApiAuthListAccountsResponse429 | GetApiAuthListAccountsResponse500 | list[GetApiAuthListAccountsResponse200Item]]
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
    GetApiAuthListAccountsResponse400
    | GetApiAuthListAccountsResponse401
    | GetApiAuthListAccountsResponse403
    | GetApiAuthListAccountsResponse404
    | GetApiAuthListAccountsResponse429
    | GetApiAuthListAccountsResponse500
    | list[GetApiAuthListAccountsResponse200Item]
    | None
):
    """List all accounts linked to the user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiAuthListAccountsResponse400 | GetApiAuthListAccountsResponse401 | GetApiAuthListAccountsResponse403 | GetApiAuthListAccountsResponse404 | GetApiAuthListAccountsResponse429 | GetApiAuthListAccountsResponse500 | list[GetApiAuthListAccountsResponse200Item]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    GetApiAuthListAccountsResponse400
    | GetApiAuthListAccountsResponse401
    | GetApiAuthListAccountsResponse403
    | GetApiAuthListAccountsResponse404
    | GetApiAuthListAccountsResponse429
    | GetApiAuthListAccountsResponse500
    | list[GetApiAuthListAccountsResponse200Item]
]:
    """List all accounts linked to the user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiAuthListAccountsResponse400 | GetApiAuthListAccountsResponse401 | GetApiAuthListAccountsResponse403 | GetApiAuthListAccountsResponse404 | GetApiAuthListAccountsResponse429 | GetApiAuthListAccountsResponse500 | list[GetApiAuthListAccountsResponse200Item]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> (
    GetApiAuthListAccountsResponse400
    | GetApiAuthListAccountsResponse401
    | GetApiAuthListAccountsResponse403
    | GetApiAuthListAccountsResponse404
    | GetApiAuthListAccountsResponse429
    | GetApiAuthListAccountsResponse500
    | list[GetApiAuthListAccountsResponse200Item]
    | None
):
    """List all accounts linked to the user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiAuthListAccountsResponse400 | GetApiAuthListAccountsResponse401 | GetApiAuthListAccountsResponse403 | GetApiAuthListAccountsResponse404 | GetApiAuthListAccountsResponse429 | GetApiAuthListAccountsResponse500 | list[GetApiAuthListAccountsResponse200Item]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
