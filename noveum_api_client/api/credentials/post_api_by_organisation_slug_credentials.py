from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_by_organisation_slug_credentials_response_201 import (
    PostApiByOrganisationSlugCredentialsResponse201,
)
from ...models.post_api_by_organisation_slug_credentials_response_400 import (
    PostApiByOrganisationSlugCredentialsResponse400,
)
from ...models.post_api_by_organisation_slug_credentials_response_401 import (
    PostApiByOrganisationSlugCredentialsResponse401,
)
from ...models.post_api_by_organisation_slug_credentials_response_403 import (
    PostApiByOrganisationSlugCredentialsResponse403,
)
from ...models.post_api_by_organisation_slug_credentials_response_404 import (
    PostApiByOrganisationSlugCredentialsResponse404,
)
from ...models.post_api_by_organisation_slug_credentials_response_500 import (
    PostApiByOrganisationSlugCredentialsResponse500,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organisation_slug: str,
    *,
    body: Any | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/{organisation_slug}/credentials".format(
            organisation_slug=quote(str(organisation_slug), safe=""),
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
    PostApiByOrganisationSlugCredentialsResponse201
    | PostApiByOrganisationSlugCredentialsResponse400
    | PostApiByOrganisationSlugCredentialsResponse401
    | PostApiByOrganisationSlugCredentialsResponse403
    | PostApiByOrganisationSlugCredentialsResponse404
    | PostApiByOrganisationSlugCredentialsResponse500
    | None
):
    if response.status_code == 201:
        response_201 = PostApiByOrganisationSlugCredentialsResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = PostApiByOrganisationSlugCredentialsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostApiByOrganisationSlugCredentialsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostApiByOrganisationSlugCredentialsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostApiByOrganisationSlugCredentialsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = PostApiByOrganisationSlugCredentialsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostApiByOrganisationSlugCredentialsResponse201
    | PostApiByOrganisationSlugCredentialsResponse400
    | PostApiByOrganisationSlugCredentialsResponse401
    | PostApiByOrganisationSlugCredentialsResponse403
    | PostApiByOrganisationSlugCredentialsResponse404
    | PostApiByOrganisationSlugCredentialsResponse500
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
    body: Any | Unset = UNSET,
) -> Response[
    PostApiByOrganisationSlugCredentialsResponse201
    | PostApiByOrganisationSlugCredentialsResponse400
    | PostApiByOrganisationSlugCredentialsResponse401
    | PostApiByOrganisationSlugCredentialsResponse403
    | PostApiByOrganisationSlugCredentialsResponse404
    | PostApiByOrganisationSlugCredentialsResponse500
]:
    """Create a new credential

     Create a new AI provider credential for an organization. The credentials will be encrypted and
    stored securely.

    Args:
        organisation_slug (str):
        body (Any | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiByOrganisationSlugCredentialsResponse201 | PostApiByOrganisationSlugCredentialsResponse400 | PostApiByOrganisationSlugCredentialsResponse401 | PostApiByOrganisationSlugCredentialsResponse403 | PostApiByOrganisationSlugCredentialsResponse404 | PostApiByOrganisationSlugCredentialsResponse500]
    """

    kwargs = _get_kwargs(
        organisation_slug=organisation_slug,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organisation_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: Any | Unset = UNSET,
) -> (
    PostApiByOrganisationSlugCredentialsResponse201
    | PostApiByOrganisationSlugCredentialsResponse400
    | PostApiByOrganisationSlugCredentialsResponse401
    | PostApiByOrganisationSlugCredentialsResponse403
    | PostApiByOrganisationSlugCredentialsResponse404
    | PostApiByOrganisationSlugCredentialsResponse500
    | None
):
    """Create a new credential

     Create a new AI provider credential for an organization. The credentials will be encrypted and
    stored securely.

    Args:
        organisation_slug (str):
        body (Any | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiByOrganisationSlugCredentialsResponse201 | PostApiByOrganisationSlugCredentialsResponse400 | PostApiByOrganisationSlugCredentialsResponse401 | PostApiByOrganisationSlugCredentialsResponse403 | PostApiByOrganisationSlugCredentialsResponse404 | PostApiByOrganisationSlugCredentialsResponse500
    """

    return sync_detailed(
        organisation_slug=organisation_slug,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    organisation_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: Any | Unset = UNSET,
) -> Response[
    PostApiByOrganisationSlugCredentialsResponse201
    | PostApiByOrganisationSlugCredentialsResponse400
    | PostApiByOrganisationSlugCredentialsResponse401
    | PostApiByOrganisationSlugCredentialsResponse403
    | PostApiByOrganisationSlugCredentialsResponse404
    | PostApiByOrganisationSlugCredentialsResponse500
]:
    """Create a new credential

     Create a new AI provider credential for an organization. The credentials will be encrypted and
    stored securely.

    Args:
        organisation_slug (str):
        body (Any | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiByOrganisationSlugCredentialsResponse201 | PostApiByOrganisationSlugCredentialsResponse400 | PostApiByOrganisationSlugCredentialsResponse401 | PostApiByOrganisationSlugCredentialsResponse403 | PostApiByOrganisationSlugCredentialsResponse404 | PostApiByOrganisationSlugCredentialsResponse500]
    """

    kwargs = _get_kwargs(
        organisation_slug=organisation_slug,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organisation_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: Any | Unset = UNSET,
) -> (
    PostApiByOrganisationSlugCredentialsResponse201
    | PostApiByOrganisationSlugCredentialsResponse400
    | PostApiByOrganisationSlugCredentialsResponse401
    | PostApiByOrganisationSlugCredentialsResponse403
    | PostApiByOrganisationSlugCredentialsResponse404
    | PostApiByOrganisationSlugCredentialsResponse500
    | None
):
    """Create a new credential

     Create a new AI provider credential for an organization. The credentials will be encrypted and
    stored securely.

    Args:
        organisation_slug (str):
        body (Any | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiByOrganisationSlugCredentialsResponse201 | PostApiByOrganisationSlugCredentialsResponse400 | PostApiByOrganisationSlugCredentialsResponse401 | PostApiByOrganisationSlugCredentialsResponse403 | PostApiByOrganisationSlugCredentialsResponse404 | PostApiByOrganisationSlugCredentialsResponse500
    """

    return (
        await asyncio_detailed(
            organisation_slug=organisation_slug,
            client=client,
            body=body,
        )
    ).parsed
