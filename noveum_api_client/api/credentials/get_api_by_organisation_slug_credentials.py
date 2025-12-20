from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_by_organisation_slug_credentials_response_200 import (
    GetApiByOrganisationSlugCredentialsResponse200,
)
from ...models.get_api_by_organisation_slug_credentials_response_401 import (
    GetApiByOrganisationSlugCredentialsResponse401,
)
from ...models.get_api_by_organisation_slug_credentials_response_403 import (
    GetApiByOrganisationSlugCredentialsResponse403,
)
from ...models.get_api_by_organisation_slug_credentials_response_404 import (
    GetApiByOrganisationSlugCredentialsResponse404,
)
from ...types import Response


def _get_kwargs(
    organisation_slug: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/{organisation_slug}/credentials".format(
            organisation_slug=quote(str(organisation_slug), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetApiByOrganisationSlugCredentialsResponse200
    | GetApiByOrganisationSlugCredentialsResponse401
    | GetApiByOrganisationSlugCredentialsResponse403
    | GetApiByOrganisationSlugCredentialsResponse404
    | None
):
    if response.status_code == 200:
        response_200 = GetApiByOrganisationSlugCredentialsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetApiByOrganisationSlugCredentialsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetApiByOrganisationSlugCredentialsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetApiByOrganisationSlugCredentialsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetApiByOrganisationSlugCredentialsResponse200
    | GetApiByOrganisationSlugCredentialsResponse401
    | GetApiByOrganisationSlugCredentialsResponse403
    | GetApiByOrganisationSlugCredentialsResponse404
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
    GetApiByOrganisationSlugCredentialsResponse200
    | GetApiByOrganisationSlugCredentialsResponse401
    | GetApiByOrganisationSlugCredentialsResponse403
    | GetApiByOrganisationSlugCredentialsResponse404
]:
    """List organization's provider credentials

     Get all AI provider credentials for a specific organization. Only returns basic information for
    security.

    Args:
        organisation_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiByOrganisationSlugCredentialsResponse200 | GetApiByOrganisationSlugCredentialsResponse401 | GetApiByOrganisationSlugCredentialsResponse403 | GetApiByOrganisationSlugCredentialsResponse404]
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
    GetApiByOrganisationSlugCredentialsResponse200
    | GetApiByOrganisationSlugCredentialsResponse401
    | GetApiByOrganisationSlugCredentialsResponse403
    | GetApiByOrganisationSlugCredentialsResponse404
    | None
):
    """List organization's provider credentials

     Get all AI provider credentials for a specific organization. Only returns basic information for
    security.

    Args:
        organisation_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiByOrganisationSlugCredentialsResponse200 | GetApiByOrganisationSlugCredentialsResponse401 | GetApiByOrganisationSlugCredentialsResponse403 | GetApiByOrganisationSlugCredentialsResponse404
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
    GetApiByOrganisationSlugCredentialsResponse200
    | GetApiByOrganisationSlugCredentialsResponse401
    | GetApiByOrganisationSlugCredentialsResponse403
    | GetApiByOrganisationSlugCredentialsResponse404
]:
    """List organization's provider credentials

     Get all AI provider credentials for a specific organization. Only returns basic information for
    security.

    Args:
        organisation_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiByOrganisationSlugCredentialsResponse200 | GetApiByOrganisationSlugCredentialsResponse401 | GetApiByOrganisationSlugCredentialsResponse403 | GetApiByOrganisationSlugCredentialsResponse404]
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
    GetApiByOrganisationSlugCredentialsResponse200
    | GetApiByOrganisationSlugCredentialsResponse401
    | GetApiByOrganisationSlugCredentialsResponse403
    | GetApiByOrganisationSlugCredentialsResponse404
    | None
):
    """List organization's provider credentials

     Get all AI provider credentials for a specific organization. Only returns basic information for
    security.

    Args:
        organisation_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiByOrganisationSlugCredentialsResponse200 | GetApiByOrganisationSlugCredentialsResponse401 | GetApiByOrganisationSlugCredentialsResponse403 | GetApiByOrganisationSlugCredentialsResponse404
    """

    return (
        await asyncio_detailed(
            organisation_slug=organisation_slug,
            client=client,
        )
    ).parsed
