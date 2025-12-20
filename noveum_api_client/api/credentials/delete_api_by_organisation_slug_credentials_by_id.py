from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_api_by_organisation_slug_credentials_by_id_response_401 import (
    DeleteApiByOrganisationSlugCredentialsByIdResponse401,
)
from ...models.delete_api_by_organisation_slug_credentials_by_id_response_403 import (
    DeleteApiByOrganisationSlugCredentialsByIdResponse403,
)
from ...models.delete_api_by_organisation_slug_credentials_by_id_response_404 import (
    DeleteApiByOrganisationSlugCredentialsByIdResponse404,
)
from ...types import Response


def _get_kwargs(
    organisation_slug: str,
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/{organisation_slug}/credentials/{id}".format(
            organisation_slug=quote(str(organisation_slug), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteApiByOrganisationSlugCredentialsByIdResponse401
    | DeleteApiByOrganisationSlugCredentialsByIdResponse403
    | DeleteApiByOrganisationSlugCredentialsByIdResponse404
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = DeleteApiByOrganisationSlugCredentialsByIdResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteApiByOrganisationSlugCredentialsByIdResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteApiByOrganisationSlugCredentialsByIdResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteApiByOrganisationSlugCredentialsByIdResponse401
    | DeleteApiByOrganisationSlugCredentialsByIdResponse403
    | DeleteApiByOrganisationSlugCredentialsByIdResponse404
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
    Any
    | DeleteApiByOrganisationSlugCredentialsByIdResponse401
    | DeleteApiByOrganisationSlugCredentialsByIdResponse403
    | DeleteApiByOrganisationSlugCredentialsByIdResponse404
]:
    """Remove credentials

     Soft delete provider credentials. The credential will be marked as deleted but not permanently
    removed.

    Args:
        organisation_slug (str):
        id (str): The credential ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteApiByOrganisationSlugCredentialsByIdResponse401 | DeleteApiByOrganisationSlugCredentialsByIdResponse403 | DeleteApiByOrganisationSlugCredentialsByIdResponse404]
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
    Any
    | DeleteApiByOrganisationSlugCredentialsByIdResponse401
    | DeleteApiByOrganisationSlugCredentialsByIdResponse403
    | DeleteApiByOrganisationSlugCredentialsByIdResponse404
    | None
):
    """Remove credentials

     Soft delete provider credentials. The credential will be marked as deleted but not permanently
    removed.

    Args:
        organisation_slug (str):
        id (str): The credential ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteApiByOrganisationSlugCredentialsByIdResponse401 | DeleteApiByOrganisationSlugCredentialsByIdResponse403 | DeleteApiByOrganisationSlugCredentialsByIdResponse404
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
    Any
    | DeleteApiByOrganisationSlugCredentialsByIdResponse401
    | DeleteApiByOrganisationSlugCredentialsByIdResponse403
    | DeleteApiByOrganisationSlugCredentialsByIdResponse404
]:
    """Remove credentials

     Soft delete provider credentials. The credential will be marked as deleted but not permanently
    removed.

    Args:
        organisation_slug (str):
        id (str): The credential ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteApiByOrganisationSlugCredentialsByIdResponse401 | DeleteApiByOrganisationSlugCredentialsByIdResponse403 | DeleteApiByOrganisationSlugCredentialsByIdResponse404]
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
    Any
    | DeleteApiByOrganisationSlugCredentialsByIdResponse401
    | DeleteApiByOrganisationSlugCredentialsByIdResponse403
    | DeleteApiByOrganisationSlugCredentialsByIdResponse404
    | None
):
    """Remove credentials

     Soft delete provider credentials. The credential will be marked as deleted but not permanently
    removed.

    Args:
        organisation_slug (str):
        id (str): The credential ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteApiByOrganisationSlugCredentialsByIdResponse401 | DeleteApiByOrganisationSlugCredentialsByIdResponse403 | DeleteApiByOrganisationSlugCredentialsByIdResponse404
    """

    return (
        await asyncio_detailed(
            organisation_slug=organisation_slug,
            id=id,
            client=client,
        )
    ).parsed
