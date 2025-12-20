from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_auth_list_sessions_response_200_item import GetApiAuthListSessionsResponse200Item
from ...models.get_api_auth_list_sessions_response_400 import GetApiAuthListSessionsResponse400
from ...models.get_api_auth_list_sessions_response_401 import GetApiAuthListSessionsResponse401
from ...models.get_api_auth_list_sessions_response_403 import GetApiAuthListSessionsResponse403
from ...models.get_api_auth_list_sessions_response_404 import GetApiAuthListSessionsResponse404
from ...models.get_api_auth_list_sessions_response_429 import GetApiAuthListSessionsResponse429
from ...models.get_api_auth_list_sessions_response_500 import GetApiAuthListSessionsResponse500
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/auth/list-sessions",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetApiAuthListSessionsResponse400
    | GetApiAuthListSessionsResponse401
    | GetApiAuthListSessionsResponse403
    | GetApiAuthListSessionsResponse404
    | GetApiAuthListSessionsResponse429
    | GetApiAuthListSessionsResponse500
    | list[GetApiAuthListSessionsResponse200Item]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetApiAuthListSessionsResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = GetApiAuthListSessionsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetApiAuthListSessionsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetApiAuthListSessionsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetApiAuthListSessionsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = GetApiAuthListSessionsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetApiAuthListSessionsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetApiAuthListSessionsResponse400
    | GetApiAuthListSessionsResponse401
    | GetApiAuthListSessionsResponse403
    | GetApiAuthListSessionsResponse404
    | GetApiAuthListSessionsResponse429
    | GetApiAuthListSessionsResponse500
    | list[GetApiAuthListSessionsResponse200Item]
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
    GetApiAuthListSessionsResponse400
    | GetApiAuthListSessionsResponse401
    | GetApiAuthListSessionsResponse403
    | GetApiAuthListSessionsResponse404
    | GetApiAuthListSessionsResponse429
    | GetApiAuthListSessionsResponse500
    | list[GetApiAuthListSessionsResponse200Item]
]:
    """List all active sessions for the user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiAuthListSessionsResponse400 | GetApiAuthListSessionsResponse401 | GetApiAuthListSessionsResponse403 | GetApiAuthListSessionsResponse404 | GetApiAuthListSessionsResponse429 | GetApiAuthListSessionsResponse500 | list[GetApiAuthListSessionsResponse200Item]]
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
    GetApiAuthListSessionsResponse400
    | GetApiAuthListSessionsResponse401
    | GetApiAuthListSessionsResponse403
    | GetApiAuthListSessionsResponse404
    | GetApiAuthListSessionsResponse429
    | GetApiAuthListSessionsResponse500
    | list[GetApiAuthListSessionsResponse200Item]
    | None
):
    """List all active sessions for the user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiAuthListSessionsResponse400 | GetApiAuthListSessionsResponse401 | GetApiAuthListSessionsResponse403 | GetApiAuthListSessionsResponse404 | GetApiAuthListSessionsResponse429 | GetApiAuthListSessionsResponse500 | list[GetApiAuthListSessionsResponse200Item]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    GetApiAuthListSessionsResponse400
    | GetApiAuthListSessionsResponse401
    | GetApiAuthListSessionsResponse403
    | GetApiAuthListSessionsResponse404
    | GetApiAuthListSessionsResponse429
    | GetApiAuthListSessionsResponse500
    | list[GetApiAuthListSessionsResponse200Item]
]:
    """List all active sessions for the user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiAuthListSessionsResponse400 | GetApiAuthListSessionsResponse401 | GetApiAuthListSessionsResponse403 | GetApiAuthListSessionsResponse404 | GetApiAuthListSessionsResponse429 | GetApiAuthListSessionsResponse500 | list[GetApiAuthListSessionsResponse200Item]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> (
    GetApiAuthListSessionsResponse400
    | GetApiAuthListSessionsResponse401
    | GetApiAuthListSessionsResponse403
    | GetApiAuthListSessionsResponse404
    | GetApiAuthListSessionsResponse429
    | GetApiAuthListSessionsResponse500
    | list[GetApiAuthListSessionsResponse200Item]
    | None
):
    """List all active sessions for the user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiAuthListSessionsResponse400 | GetApiAuthListSessionsResponse401 | GetApiAuthListSessionsResponse403 | GetApiAuthListSessionsResponse404 | GetApiAuthListSessionsResponse429 | GetApiAuthListSessionsResponse500 | list[GetApiAuthListSessionsResponse200Item]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
