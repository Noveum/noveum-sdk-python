from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_auth_organization_get_full_organization_response_400 import (
    GetApiAuthOrganizationGetFullOrganizationResponse400,
)
from ...models.get_api_auth_organization_get_full_organization_response_401 import (
    GetApiAuthOrganizationGetFullOrganizationResponse401,
)
from ...models.get_api_auth_organization_get_full_organization_response_403 import (
    GetApiAuthOrganizationGetFullOrganizationResponse403,
)
from ...models.get_api_auth_organization_get_full_organization_response_404 import (
    GetApiAuthOrganizationGetFullOrganizationResponse404,
)
from ...models.get_api_auth_organization_get_full_organization_response_429 import (
    GetApiAuthOrganizationGetFullOrganizationResponse429,
)
from ...models.get_api_auth_organization_get_full_organization_response_500 import (
    GetApiAuthOrganizationGetFullOrganizationResponse500,
)
from ...models.organization import Organization
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/auth/organization/get-full-organization",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetApiAuthOrganizationGetFullOrganizationResponse400
    | GetApiAuthOrganizationGetFullOrganizationResponse401
    | GetApiAuthOrganizationGetFullOrganizationResponse403
    | GetApiAuthOrganizationGetFullOrganizationResponse404
    | GetApiAuthOrganizationGetFullOrganizationResponse429
    | GetApiAuthOrganizationGetFullOrganizationResponse500
    | Organization
    | None
):
    if response.status_code == 200:
        response_200 = Organization.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetApiAuthOrganizationGetFullOrganizationResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetApiAuthOrganizationGetFullOrganizationResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetApiAuthOrganizationGetFullOrganizationResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetApiAuthOrganizationGetFullOrganizationResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = GetApiAuthOrganizationGetFullOrganizationResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetApiAuthOrganizationGetFullOrganizationResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetApiAuthOrganizationGetFullOrganizationResponse400
    | GetApiAuthOrganizationGetFullOrganizationResponse401
    | GetApiAuthOrganizationGetFullOrganizationResponse403
    | GetApiAuthOrganizationGetFullOrganizationResponse404
    | GetApiAuthOrganizationGetFullOrganizationResponse429
    | GetApiAuthOrganizationGetFullOrganizationResponse500
    | Organization
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
    GetApiAuthOrganizationGetFullOrganizationResponse400
    | GetApiAuthOrganizationGetFullOrganizationResponse401
    | GetApiAuthOrganizationGetFullOrganizationResponse403
    | GetApiAuthOrganizationGetFullOrganizationResponse404
    | GetApiAuthOrganizationGetFullOrganizationResponse429
    | GetApiAuthOrganizationGetFullOrganizationResponse500
    | Organization
]:
    """Get the full organization

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiAuthOrganizationGetFullOrganizationResponse400 | GetApiAuthOrganizationGetFullOrganizationResponse401 | GetApiAuthOrganizationGetFullOrganizationResponse403 | GetApiAuthOrganizationGetFullOrganizationResponse404 | GetApiAuthOrganizationGetFullOrganizationResponse429 | GetApiAuthOrganizationGetFullOrganizationResponse500 | Organization]
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
    GetApiAuthOrganizationGetFullOrganizationResponse400
    | GetApiAuthOrganizationGetFullOrganizationResponse401
    | GetApiAuthOrganizationGetFullOrganizationResponse403
    | GetApiAuthOrganizationGetFullOrganizationResponse404
    | GetApiAuthOrganizationGetFullOrganizationResponse429
    | GetApiAuthOrganizationGetFullOrganizationResponse500
    | Organization
    | None
):
    """Get the full organization

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiAuthOrganizationGetFullOrganizationResponse400 | GetApiAuthOrganizationGetFullOrganizationResponse401 | GetApiAuthOrganizationGetFullOrganizationResponse403 | GetApiAuthOrganizationGetFullOrganizationResponse404 | GetApiAuthOrganizationGetFullOrganizationResponse429 | GetApiAuthOrganizationGetFullOrganizationResponse500 | Organization
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    GetApiAuthOrganizationGetFullOrganizationResponse400
    | GetApiAuthOrganizationGetFullOrganizationResponse401
    | GetApiAuthOrganizationGetFullOrganizationResponse403
    | GetApiAuthOrganizationGetFullOrganizationResponse404
    | GetApiAuthOrganizationGetFullOrganizationResponse429
    | GetApiAuthOrganizationGetFullOrganizationResponse500
    | Organization
]:
    """Get the full organization

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiAuthOrganizationGetFullOrganizationResponse400 | GetApiAuthOrganizationGetFullOrganizationResponse401 | GetApiAuthOrganizationGetFullOrganizationResponse403 | GetApiAuthOrganizationGetFullOrganizationResponse404 | GetApiAuthOrganizationGetFullOrganizationResponse429 | GetApiAuthOrganizationGetFullOrganizationResponse500 | Organization]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> (
    GetApiAuthOrganizationGetFullOrganizationResponse400
    | GetApiAuthOrganizationGetFullOrganizationResponse401
    | GetApiAuthOrganizationGetFullOrganizationResponse403
    | GetApiAuthOrganizationGetFullOrganizationResponse404
    | GetApiAuthOrganizationGetFullOrganizationResponse429
    | GetApiAuthOrganizationGetFullOrganizationResponse500
    | Organization
    | None
):
    """Get the full organization

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiAuthOrganizationGetFullOrganizationResponse400 | GetApiAuthOrganizationGetFullOrganizationResponse401 | GetApiAuthOrganizationGetFullOrganizationResponse403 | GetApiAuthOrganizationGetFullOrganizationResponse404 | GetApiAuthOrganizationGetFullOrganizationResponse429 | GetApiAuthOrganizationGetFullOrganizationResponse500 | Organization
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
