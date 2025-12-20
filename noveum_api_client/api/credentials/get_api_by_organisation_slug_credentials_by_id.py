from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_by_organisation_slug_credentials_by_id_response_200 import (
    GetApiByOrganisationSlugCredentialsByIdResponse200,
)
from ...models.get_api_by_organisation_slug_credentials_by_id_response_401 import (
    GetApiByOrganisationSlugCredentialsByIdResponse401,
)
from ...models.get_api_by_organisation_slug_credentials_by_id_response_403 import (
    GetApiByOrganisationSlugCredentialsByIdResponse403,
)
from ...models.get_api_by_organisation_slug_credentials_by_id_response_404 import (
    GetApiByOrganisationSlugCredentialsByIdResponse404,
)
from ...types import Response


def _get_kwargs(
    organisation_slug: str,
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/{organisation_slug}/credentials/{id}".format(
            organisation_slug=quote(str(organisation_slug), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetApiByOrganisationSlugCredentialsByIdResponse200
    | GetApiByOrganisationSlugCredentialsByIdResponse401
    | GetApiByOrganisationSlugCredentialsByIdResponse403
    | GetApiByOrganisationSlugCredentialsByIdResponse404
    | None
):
    if response.status_code == 200:
        response_200 = GetApiByOrganisationSlugCredentialsByIdResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetApiByOrganisationSlugCredentialsByIdResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetApiByOrganisationSlugCredentialsByIdResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetApiByOrganisationSlugCredentialsByIdResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetApiByOrganisationSlugCredentialsByIdResponse200
    | GetApiByOrganisationSlugCredentialsByIdResponse401
    | GetApiByOrganisationSlugCredentialsByIdResponse403
    | GetApiByOrganisationSlugCredentialsByIdResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organisation_slug: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetApiByOrganisationSlugCredentialsByIdResponse200
    | GetApiByOrganisationSlugCredentialsByIdResponse401
    | GetApiByOrganisationSlugCredentialsByIdResponse403
    | GetApiByOrganisationSlugCredentialsByIdResponse404
]:
    """Get specific credential details

     Get detailed information about a specific credential. Sensitive credential data is masked for
    security.

    Args:
        organisation_slug (str):
        id (str): The credential ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiByOrganisationSlugCredentialsByIdResponse200 | GetApiByOrganisationSlugCredentialsByIdResponse401 | GetApiByOrganisationSlugCredentialsByIdResponse403 | GetApiByOrganisationSlugCredentialsByIdResponse404]
    """

    kwargs = _get_kwargs(
        organisation_slug=organisation_slug,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organisation_slug: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetApiByOrganisationSlugCredentialsByIdResponse200
    | GetApiByOrganisationSlugCredentialsByIdResponse401
    | GetApiByOrganisationSlugCredentialsByIdResponse403
    | GetApiByOrganisationSlugCredentialsByIdResponse404
    | None
):
    """Get specific credential details

     Get detailed information about a specific credential. Sensitive credential data is masked for
    security.

    Args:
        organisation_slug (str):
        id (str): The credential ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiByOrganisationSlugCredentialsByIdResponse200 | GetApiByOrganisationSlugCredentialsByIdResponse401 | GetApiByOrganisationSlugCredentialsByIdResponse403 | GetApiByOrganisationSlugCredentialsByIdResponse404
    """

    return sync_detailed(
        organisation_slug=organisation_slug,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    organisation_slug: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetApiByOrganisationSlugCredentialsByIdResponse200
    | GetApiByOrganisationSlugCredentialsByIdResponse401
    | GetApiByOrganisationSlugCredentialsByIdResponse403
    | GetApiByOrganisationSlugCredentialsByIdResponse404
]:
    """Get specific credential details

     Get detailed information about a specific credential. Sensitive credential data is masked for
    security.

    Args:
        organisation_slug (str):
        id (str): The credential ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiByOrganisationSlugCredentialsByIdResponse200 | GetApiByOrganisationSlugCredentialsByIdResponse401 | GetApiByOrganisationSlugCredentialsByIdResponse403 | GetApiByOrganisationSlugCredentialsByIdResponse404]
    """

    kwargs = _get_kwargs(
        organisation_slug=organisation_slug,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organisation_slug: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetApiByOrganisationSlugCredentialsByIdResponse200
    | GetApiByOrganisationSlugCredentialsByIdResponse401
    | GetApiByOrganisationSlugCredentialsByIdResponse403
    | GetApiByOrganisationSlugCredentialsByIdResponse404
    | None
):
    """Get specific credential details

     Get detailed information about a specific credential. Sensitive credential data is masked for
    security.

    Args:
        organisation_slug (str):
        id (str): The credential ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiByOrganisationSlugCredentialsByIdResponse200 | GetApiByOrganisationSlugCredentialsByIdResponse401 | GetApiByOrganisationSlugCredentialsByIdResponse403 | GetApiByOrganisationSlugCredentialsByIdResponse404
    """

    return (
        await asyncio_detailed(
            organisation_slug=organisation_slug,
            id=id,
            client=client,
        )
    ).parsed
