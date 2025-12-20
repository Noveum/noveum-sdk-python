from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_auth_organization_list_response_400 import GetApiAuthOrganizationListResponse400
from ...models.get_api_auth_organization_list_response_401 import GetApiAuthOrganizationListResponse401
from ...models.get_api_auth_organization_list_response_403 import GetApiAuthOrganizationListResponse403
from ...models.get_api_auth_organization_list_response_404 import GetApiAuthOrganizationListResponse404
from ...models.get_api_auth_organization_list_response_429 import GetApiAuthOrganizationListResponse429
from ...models.get_api_auth_organization_list_response_500 import GetApiAuthOrganizationListResponse500
from ...models.organization import Organization
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/auth/organization/list",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetApiAuthOrganizationListResponse400
    | GetApiAuthOrganizationListResponse401
    | GetApiAuthOrganizationListResponse403
    | GetApiAuthOrganizationListResponse404
    | GetApiAuthOrganizationListResponse429
    | GetApiAuthOrganizationListResponse500
    | list[Organization]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Organization.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = GetApiAuthOrganizationListResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetApiAuthOrganizationListResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetApiAuthOrganizationListResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetApiAuthOrganizationListResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = GetApiAuthOrganizationListResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetApiAuthOrganizationListResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetApiAuthOrganizationListResponse400
    | GetApiAuthOrganizationListResponse401
    | GetApiAuthOrganizationListResponse403
    | GetApiAuthOrganizationListResponse404
    | GetApiAuthOrganizationListResponse429
    | GetApiAuthOrganizationListResponse500
    | list[Organization]
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
    GetApiAuthOrganizationListResponse400
    | GetApiAuthOrganizationListResponse401
    | GetApiAuthOrganizationListResponse403
    | GetApiAuthOrganizationListResponse404
    | GetApiAuthOrganizationListResponse429
    | GetApiAuthOrganizationListResponse500
    | list[Organization]
]:
    """List all organizations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiAuthOrganizationListResponse400 | GetApiAuthOrganizationListResponse401 | GetApiAuthOrganizationListResponse403 | GetApiAuthOrganizationListResponse404 | GetApiAuthOrganizationListResponse429 | GetApiAuthOrganizationListResponse500 | list[Organization]]
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
    GetApiAuthOrganizationListResponse400
    | GetApiAuthOrganizationListResponse401
    | GetApiAuthOrganizationListResponse403
    | GetApiAuthOrganizationListResponse404
    | GetApiAuthOrganizationListResponse429
    | GetApiAuthOrganizationListResponse500
    | list[Organization]
    | None
):
    """List all organizations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiAuthOrganizationListResponse400 | GetApiAuthOrganizationListResponse401 | GetApiAuthOrganizationListResponse403 | GetApiAuthOrganizationListResponse404 | GetApiAuthOrganizationListResponse429 | GetApiAuthOrganizationListResponse500 | list[Organization]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    GetApiAuthOrganizationListResponse400
    | GetApiAuthOrganizationListResponse401
    | GetApiAuthOrganizationListResponse403
    | GetApiAuthOrganizationListResponse404
    | GetApiAuthOrganizationListResponse429
    | GetApiAuthOrganizationListResponse500
    | list[Organization]
]:
    """List all organizations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiAuthOrganizationListResponse400 | GetApiAuthOrganizationListResponse401 | GetApiAuthOrganizationListResponse403 | GetApiAuthOrganizationListResponse404 | GetApiAuthOrganizationListResponse429 | GetApiAuthOrganizationListResponse500 | list[Organization]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> (
    GetApiAuthOrganizationListResponse400
    | GetApiAuthOrganizationListResponse401
    | GetApiAuthOrganizationListResponse403
    | GetApiAuthOrganizationListResponse404
    | GetApiAuthOrganizationListResponse429
    | GetApiAuthOrganizationListResponse500
    | list[Organization]
    | None
):
    """List all organizations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiAuthOrganizationListResponse400 | GetApiAuthOrganizationListResponse401 | GetApiAuthOrganizationListResponse403 | GetApiAuthOrganizationListResponse404 | GetApiAuthOrganizationListResponse429 | GetApiAuthOrganizationListResponse500 | list[Organization]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
