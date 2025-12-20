from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_auth_ok_response_200 import GetApiAuthOkResponse200
from ...models.get_api_auth_ok_response_400 import GetApiAuthOkResponse400
from ...models.get_api_auth_ok_response_401 import GetApiAuthOkResponse401
from ...models.get_api_auth_ok_response_403 import GetApiAuthOkResponse403
from ...models.get_api_auth_ok_response_404 import GetApiAuthOkResponse404
from ...models.get_api_auth_ok_response_429 import GetApiAuthOkResponse429
from ...models.get_api_auth_ok_response_500 import GetApiAuthOkResponse500
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/auth/ok",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetApiAuthOkResponse200
    | GetApiAuthOkResponse400
    | GetApiAuthOkResponse401
    | GetApiAuthOkResponse403
    | GetApiAuthOkResponse404
    | GetApiAuthOkResponse429
    | GetApiAuthOkResponse500
    | None
):
    if response.status_code == 200:
        response_200 = GetApiAuthOkResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetApiAuthOkResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetApiAuthOkResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetApiAuthOkResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetApiAuthOkResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = GetApiAuthOkResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetApiAuthOkResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetApiAuthOkResponse200
    | GetApiAuthOkResponse400
    | GetApiAuthOkResponse401
    | GetApiAuthOkResponse403
    | GetApiAuthOkResponse404
    | GetApiAuthOkResponse429
    | GetApiAuthOkResponse500
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
    GetApiAuthOkResponse200
    | GetApiAuthOkResponse400
    | GetApiAuthOkResponse401
    | GetApiAuthOkResponse403
    | GetApiAuthOkResponse404
    | GetApiAuthOkResponse429
    | GetApiAuthOkResponse500
]:
    """Check if the API is working

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiAuthOkResponse200 | GetApiAuthOkResponse400 | GetApiAuthOkResponse401 | GetApiAuthOkResponse403 | GetApiAuthOkResponse404 | GetApiAuthOkResponse429 | GetApiAuthOkResponse500]
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
    GetApiAuthOkResponse200
    | GetApiAuthOkResponse400
    | GetApiAuthOkResponse401
    | GetApiAuthOkResponse403
    | GetApiAuthOkResponse404
    | GetApiAuthOkResponse429
    | GetApiAuthOkResponse500
    | None
):
    """Check if the API is working

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiAuthOkResponse200 | GetApiAuthOkResponse400 | GetApiAuthOkResponse401 | GetApiAuthOkResponse403 | GetApiAuthOkResponse404 | GetApiAuthOkResponse429 | GetApiAuthOkResponse500
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    GetApiAuthOkResponse200
    | GetApiAuthOkResponse400
    | GetApiAuthOkResponse401
    | GetApiAuthOkResponse403
    | GetApiAuthOkResponse404
    | GetApiAuthOkResponse429
    | GetApiAuthOkResponse500
]:
    """Check if the API is working

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiAuthOkResponse200 | GetApiAuthOkResponse400 | GetApiAuthOkResponse401 | GetApiAuthOkResponse403 | GetApiAuthOkResponse404 | GetApiAuthOkResponse429 | GetApiAuthOkResponse500]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> (
    GetApiAuthOkResponse200
    | GetApiAuthOkResponse400
    | GetApiAuthOkResponse401
    | GetApiAuthOkResponse403
    | GetApiAuthOkResponse404
    | GetApiAuthOkResponse429
    | GetApiAuthOkResponse500
    | None
):
    """Check if the API is working

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiAuthOkResponse200 | GetApiAuthOkResponse400 | GetApiAuthOkResponse401 | GetApiAuthOkResponse403 | GetApiAuthOkResponse404 | GetApiAuthOkResponse429 | GetApiAuthOkResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
