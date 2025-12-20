from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_auth_error_response_400 import GetApiAuthErrorResponse400
from ...models.get_api_auth_error_response_401 import GetApiAuthErrorResponse401
from ...models.get_api_auth_error_response_403 import GetApiAuthErrorResponse403
from ...models.get_api_auth_error_response_404 import GetApiAuthErrorResponse404
from ...models.get_api_auth_error_response_429 import GetApiAuthErrorResponse429
from ...models.get_api_auth_error_response_500 import GetApiAuthErrorResponse500
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/auth/error",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetApiAuthErrorResponse400
    | GetApiAuthErrorResponse401
    | GetApiAuthErrorResponse403
    | GetApiAuthErrorResponse404
    | GetApiAuthErrorResponse429
    | GetApiAuthErrorResponse500
    | str
    | None
):
    if response.status_code == 200:
        response_200 = response.text
        return response_200

    if response.status_code == 400:
        response_400 = GetApiAuthErrorResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetApiAuthErrorResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetApiAuthErrorResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetApiAuthErrorResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = GetApiAuthErrorResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetApiAuthErrorResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetApiAuthErrorResponse400
    | GetApiAuthErrorResponse401
    | GetApiAuthErrorResponse403
    | GetApiAuthErrorResponse404
    | GetApiAuthErrorResponse429
    | GetApiAuthErrorResponse500
    | str
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
    GetApiAuthErrorResponse400
    | GetApiAuthErrorResponse401
    | GetApiAuthErrorResponse403
    | GetApiAuthErrorResponse404
    | GetApiAuthErrorResponse429
    | GetApiAuthErrorResponse500
    | str
]:
    """Displays an error page

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiAuthErrorResponse400 | GetApiAuthErrorResponse401 | GetApiAuthErrorResponse403 | GetApiAuthErrorResponse404 | GetApiAuthErrorResponse429 | GetApiAuthErrorResponse500 | str]
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
    GetApiAuthErrorResponse400
    | GetApiAuthErrorResponse401
    | GetApiAuthErrorResponse403
    | GetApiAuthErrorResponse404
    | GetApiAuthErrorResponse429
    | GetApiAuthErrorResponse500
    | str
    | None
):
    """Displays an error page

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiAuthErrorResponse400 | GetApiAuthErrorResponse401 | GetApiAuthErrorResponse403 | GetApiAuthErrorResponse404 | GetApiAuthErrorResponse429 | GetApiAuthErrorResponse500 | str
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    GetApiAuthErrorResponse400
    | GetApiAuthErrorResponse401
    | GetApiAuthErrorResponse403
    | GetApiAuthErrorResponse404
    | GetApiAuthErrorResponse429
    | GetApiAuthErrorResponse500
    | str
]:
    """Displays an error page

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiAuthErrorResponse400 | GetApiAuthErrorResponse401 | GetApiAuthErrorResponse403 | GetApiAuthErrorResponse404 | GetApiAuthErrorResponse429 | GetApiAuthErrorResponse500 | str]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> (
    GetApiAuthErrorResponse400
    | GetApiAuthErrorResponse401
    | GetApiAuthErrorResponse403
    | GetApiAuthErrorResponse404
    | GetApiAuthErrorResponse429
    | GetApiAuthErrorResponse500
    | str
    | None
):
    """Displays an error page

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiAuthErrorResponse400 | GetApiAuthErrorResponse401 | GetApiAuthErrorResponse403 | GetApiAuthErrorResponse404 | GetApiAuthErrorResponse429 | GetApiAuthErrorResponse500 | str
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
