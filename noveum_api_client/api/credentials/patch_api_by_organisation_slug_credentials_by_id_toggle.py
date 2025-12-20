from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_api_by_organisation_slug_credentials_by_id_toggle_response_200 import (
    PatchApiByOrganisationSlugCredentialsByIdToggleResponse200,
)
from ...models.patch_api_by_organisation_slug_credentials_by_id_toggle_response_401 import (
    PatchApiByOrganisationSlugCredentialsByIdToggleResponse401,
)
from ...models.patch_api_by_organisation_slug_credentials_by_id_toggle_response_403 import (
    PatchApiByOrganisationSlugCredentialsByIdToggleResponse403,
)
from ...models.patch_api_by_organisation_slug_credentials_by_id_toggle_response_404 import (
    PatchApiByOrganisationSlugCredentialsByIdToggleResponse404,
)
from ...types import Response


def _get_kwargs(
    organisation_slug: str,
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/{organisation_slug}/credentials/{id}/toggle".format(
            organisation_slug=quote(str(organisation_slug), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PatchApiByOrganisationSlugCredentialsByIdToggleResponse200
    | PatchApiByOrganisationSlugCredentialsByIdToggleResponse401
    | PatchApiByOrganisationSlugCredentialsByIdToggleResponse403
    | PatchApiByOrganisationSlugCredentialsByIdToggleResponse404
    | None
):
    if response.status_code == 200:
        response_200 = PatchApiByOrganisationSlugCredentialsByIdToggleResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = PatchApiByOrganisationSlugCredentialsByIdToggleResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchApiByOrganisationSlugCredentialsByIdToggleResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchApiByOrganisationSlugCredentialsByIdToggleResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchApiByOrganisationSlugCredentialsByIdToggleResponse200
    | PatchApiByOrganisationSlugCredentialsByIdToggleResponse401
    | PatchApiByOrganisationSlugCredentialsByIdToggleResponse403
    | PatchApiByOrganisationSlugCredentialsByIdToggleResponse404
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
    PatchApiByOrganisationSlugCredentialsByIdToggleResponse200
    | PatchApiByOrganisationSlugCredentialsByIdToggleResponse401
    | PatchApiByOrganisationSlugCredentialsByIdToggleResponse403
    | PatchApiByOrganisationSlugCredentialsByIdToggleResponse404
]:
    """Toggle credential enabled status

     Toggle the enabled/disabled status of a credential. Disabled credentials cannot be used for AI
    operations.

    Args:
        organisation_slug (str):
        id (str): The credential ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchApiByOrganisationSlugCredentialsByIdToggleResponse200 | PatchApiByOrganisationSlugCredentialsByIdToggleResponse401 | PatchApiByOrganisationSlugCredentialsByIdToggleResponse403 | PatchApiByOrganisationSlugCredentialsByIdToggleResponse404]
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
    PatchApiByOrganisationSlugCredentialsByIdToggleResponse200
    | PatchApiByOrganisationSlugCredentialsByIdToggleResponse401
    | PatchApiByOrganisationSlugCredentialsByIdToggleResponse403
    | PatchApiByOrganisationSlugCredentialsByIdToggleResponse404
    | None
):
    """Toggle credential enabled status

     Toggle the enabled/disabled status of a credential. Disabled credentials cannot be used for AI
    operations.

    Args:
        organisation_slug (str):
        id (str): The credential ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchApiByOrganisationSlugCredentialsByIdToggleResponse200 | PatchApiByOrganisationSlugCredentialsByIdToggleResponse401 | PatchApiByOrganisationSlugCredentialsByIdToggleResponse403 | PatchApiByOrganisationSlugCredentialsByIdToggleResponse404
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
    PatchApiByOrganisationSlugCredentialsByIdToggleResponse200
    | PatchApiByOrganisationSlugCredentialsByIdToggleResponse401
    | PatchApiByOrganisationSlugCredentialsByIdToggleResponse403
    | PatchApiByOrganisationSlugCredentialsByIdToggleResponse404
]:
    """Toggle credential enabled status

     Toggle the enabled/disabled status of a credential. Disabled credentials cannot be used for AI
    operations.

    Args:
        organisation_slug (str):
        id (str): The credential ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchApiByOrganisationSlugCredentialsByIdToggleResponse200 | PatchApiByOrganisationSlugCredentialsByIdToggleResponse401 | PatchApiByOrganisationSlugCredentialsByIdToggleResponse403 | PatchApiByOrganisationSlugCredentialsByIdToggleResponse404]
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
    PatchApiByOrganisationSlugCredentialsByIdToggleResponse200
    | PatchApiByOrganisationSlugCredentialsByIdToggleResponse401
    | PatchApiByOrganisationSlugCredentialsByIdToggleResponse403
    | PatchApiByOrganisationSlugCredentialsByIdToggleResponse404
    | None
):
    """Toggle credential enabled status

     Toggle the enabled/disabled status of a credential. Disabled credentials cannot be used for AI
    operations.

    Args:
        organisation_slug (str):
        id (str): The credential ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchApiByOrganisationSlugCredentialsByIdToggleResponse200 | PatchApiByOrganisationSlugCredentialsByIdToggleResponse401 | PatchApiByOrganisationSlugCredentialsByIdToggleResponse403 | PatchApiByOrganisationSlugCredentialsByIdToggleResponse404
    """

    return (
        await asyncio_detailed(
            organisation_slug=organisation_slug,
            id=id,
            client=client,
        )
    ).parsed
