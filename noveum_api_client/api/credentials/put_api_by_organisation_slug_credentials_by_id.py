from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_api_by_organisation_slug_credentials_by_id_response_200 import (
    PutApiByOrganisationSlugCredentialsByIdResponse200,
)
from ...models.put_api_by_organisation_slug_credentials_by_id_response_400 import (
    PutApiByOrganisationSlugCredentialsByIdResponse400,
)
from ...models.put_api_by_organisation_slug_credentials_by_id_response_401 import (
    PutApiByOrganisationSlugCredentialsByIdResponse401,
)
from ...models.put_api_by_organisation_slug_credentials_by_id_response_403 import (
    PutApiByOrganisationSlugCredentialsByIdResponse403,
)
from ...models.put_api_by_organisation_slug_credentials_by_id_response_404 import (
    PutApiByOrganisationSlugCredentialsByIdResponse404,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organisation_slug: str,
    id: str,
    *,
    body: Any | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/{organisation_slug}/credentials/{id}".format(
            organisation_slug=quote(str(organisation_slug), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PutApiByOrganisationSlugCredentialsByIdResponse200
    | PutApiByOrganisationSlugCredentialsByIdResponse400
    | PutApiByOrganisationSlugCredentialsByIdResponse401
    | PutApiByOrganisationSlugCredentialsByIdResponse403
    | PutApiByOrganisationSlugCredentialsByIdResponse404
    | None
):
    if response.status_code == 200:
        response_200 = PutApiByOrganisationSlugCredentialsByIdResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PutApiByOrganisationSlugCredentialsByIdResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PutApiByOrganisationSlugCredentialsByIdResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PutApiByOrganisationSlugCredentialsByIdResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PutApiByOrganisationSlugCredentialsByIdResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PutApiByOrganisationSlugCredentialsByIdResponse200
    | PutApiByOrganisationSlugCredentialsByIdResponse400
    | PutApiByOrganisationSlugCredentialsByIdResponse401
    | PutApiByOrganisationSlugCredentialsByIdResponse403
    | PutApiByOrganisationSlugCredentialsByIdResponse404
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
    body: Any | Unset = UNSET,
) -> Response[
    PutApiByOrganisationSlugCredentialsByIdResponse200
    | PutApiByOrganisationSlugCredentialsByIdResponse400
    | PutApiByOrganisationSlugCredentialsByIdResponse401
    | PutApiByOrganisationSlugCredentialsByIdResponse403
    | PutApiByOrganisationSlugCredentialsByIdResponse404
]:
    """Update provider credentials

     Update existing AI provider credentials. Only provided fields will be updated.

    Args:
        organisation_slug (str):
        id (str): The credential ID
        body (Any | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutApiByOrganisationSlugCredentialsByIdResponse200 | PutApiByOrganisationSlugCredentialsByIdResponse400 | PutApiByOrganisationSlugCredentialsByIdResponse401 | PutApiByOrganisationSlugCredentialsByIdResponse403 | PutApiByOrganisationSlugCredentialsByIdResponse404]
    """

    kwargs = _get_kwargs(
        organisation_slug=organisation_slug,
        id=id,
        body=body,
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
    body: Any | Unset = UNSET,
) -> (
    PutApiByOrganisationSlugCredentialsByIdResponse200
    | PutApiByOrganisationSlugCredentialsByIdResponse400
    | PutApiByOrganisationSlugCredentialsByIdResponse401
    | PutApiByOrganisationSlugCredentialsByIdResponse403
    | PutApiByOrganisationSlugCredentialsByIdResponse404
    | None
):
    """Update provider credentials

     Update existing AI provider credentials. Only provided fields will be updated.

    Args:
        organisation_slug (str):
        id (str): The credential ID
        body (Any | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutApiByOrganisationSlugCredentialsByIdResponse200 | PutApiByOrganisationSlugCredentialsByIdResponse400 | PutApiByOrganisationSlugCredentialsByIdResponse401 | PutApiByOrganisationSlugCredentialsByIdResponse403 | PutApiByOrganisationSlugCredentialsByIdResponse404
    """

    return sync_detailed(
        organisation_slug=organisation_slug,
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    organisation_slug: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: Any | Unset = UNSET,
) -> Response[
    PutApiByOrganisationSlugCredentialsByIdResponse200
    | PutApiByOrganisationSlugCredentialsByIdResponse400
    | PutApiByOrganisationSlugCredentialsByIdResponse401
    | PutApiByOrganisationSlugCredentialsByIdResponse403
    | PutApiByOrganisationSlugCredentialsByIdResponse404
]:
    """Update provider credentials

     Update existing AI provider credentials. Only provided fields will be updated.

    Args:
        organisation_slug (str):
        id (str): The credential ID
        body (Any | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutApiByOrganisationSlugCredentialsByIdResponse200 | PutApiByOrganisationSlugCredentialsByIdResponse400 | PutApiByOrganisationSlugCredentialsByIdResponse401 | PutApiByOrganisationSlugCredentialsByIdResponse403 | PutApiByOrganisationSlugCredentialsByIdResponse404]
    """

    kwargs = _get_kwargs(
        organisation_slug=organisation_slug,
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organisation_slug: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: Any | Unset = UNSET,
) -> (
    PutApiByOrganisationSlugCredentialsByIdResponse200
    | PutApiByOrganisationSlugCredentialsByIdResponse400
    | PutApiByOrganisationSlugCredentialsByIdResponse401
    | PutApiByOrganisationSlugCredentialsByIdResponse403
    | PutApiByOrganisationSlugCredentialsByIdResponse404
    | None
):
    """Update provider credentials

     Update existing AI provider credentials. Only provided fields will be updated.

    Args:
        organisation_slug (str):
        id (str): The credential ID
        body (Any | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutApiByOrganisationSlugCredentialsByIdResponse200 | PutApiByOrganisationSlugCredentialsByIdResponse400 | PutApiByOrganisationSlugCredentialsByIdResponse401 | PutApiByOrganisationSlugCredentialsByIdResponse403 | PutApiByOrganisationSlugCredentialsByIdResponse404
    """

    return (
        await asyncio_detailed(
            organisation_slug=organisation_slug,
            id=id,
            client=client,
            body=body,
        )
    ).parsed
