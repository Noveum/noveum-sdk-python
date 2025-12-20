from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_by_organisation_slug_api_keys_response_200 import GetApiByOrganisationSlugApiKeysResponse200
from ...models.get_api_by_organisation_slug_api_keys_response_401 import GetApiByOrganisationSlugApiKeysResponse401
from ...models.get_api_by_organisation_slug_api_keys_response_403 import GetApiByOrganisationSlugApiKeysResponse403
from ...types import Response


def _get_kwargs(
    organisation_slug: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/{organisation_slug}/api-keys".format(
            organisation_slug=quote(str(organisation_slug), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetApiByOrganisationSlugApiKeysResponse200
    | GetApiByOrganisationSlugApiKeysResponse401
    | GetApiByOrganisationSlugApiKeysResponse403
    | None
):
    if response.status_code == 200:
        response_200 = GetApiByOrganisationSlugApiKeysResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetApiByOrganisationSlugApiKeysResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetApiByOrganisationSlugApiKeysResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetApiByOrganisationSlugApiKeysResponse200
    | GetApiByOrganisationSlugApiKeysResponse401
    | GetApiByOrganisationSlugApiKeysResponse403
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organisation_slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetApiByOrganisationSlugApiKeysResponse200
    | GetApiByOrganisationSlugApiKeysResponse401
    | GetApiByOrganisationSlugApiKeysResponse403
]:
    """Get all API keys

     Get all API keys for the current organization. Organization admins can see all keys, regular members
    only see their own.

    Args:
        organisation_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiByOrganisationSlugApiKeysResponse200 | GetApiByOrganisationSlugApiKeysResponse401 | GetApiByOrganisationSlugApiKeysResponse403]
    """

    kwargs = _get_kwargs(
        organisation_slug=organisation_slug,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organisation_slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetApiByOrganisationSlugApiKeysResponse200
    | GetApiByOrganisationSlugApiKeysResponse401
    | GetApiByOrganisationSlugApiKeysResponse403
    | None
):
    """Get all API keys

     Get all API keys for the current organization. Organization admins can see all keys, regular members
    only see their own.

    Args:
        organisation_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiByOrganisationSlugApiKeysResponse200 | GetApiByOrganisationSlugApiKeysResponse401 | GetApiByOrganisationSlugApiKeysResponse403
    """

    return sync_detailed(
        organisation_slug=organisation_slug,
        client=client,
    ).parsed


async def asyncio_detailed(
    organisation_slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetApiByOrganisationSlugApiKeysResponse200
    | GetApiByOrganisationSlugApiKeysResponse401
    | GetApiByOrganisationSlugApiKeysResponse403
]:
    """Get all API keys

     Get all API keys for the current organization. Organization admins can see all keys, regular members
    only see their own.

    Args:
        organisation_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiByOrganisationSlugApiKeysResponse200 | GetApiByOrganisationSlugApiKeysResponse401 | GetApiByOrganisationSlugApiKeysResponse403]
    """

    kwargs = _get_kwargs(
        organisation_slug=organisation_slug,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organisation_slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetApiByOrganisationSlugApiKeysResponse200
    | GetApiByOrganisationSlugApiKeysResponse401
    | GetApiByOrganisationSlugApiKeysResponse403
    | None
):
    """Get all API keys

     Get all API keys for the current organization. Organization admins can see all keys, regular members
    only see their own.

    Args:
        organisation_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiByOrganisationSlugApiKeysResponse200 | GetApiByOrganisationSlugApiKeysResponse401 | GetApiByOrganisationSlugApiKeysResponse403
    """

    return (
        await asyncio_detailed(
            organisation_slug=organisation_slug,
            client=client,
        )
    ).parsed
