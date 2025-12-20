from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_by_organisation_slug_api_keys_response_201 import PostApiByOrganisationSlugApiKeysResponse201
from ...models.post_api_by_organisation_slug_api_keys_response_400 import PostApiByOrganisationSlugApiKeysResponse400
from ...models.post_api_by_organisation_slug_api_keys_response_401 import PostApiByOrganisationSlugApiKeysResponse401
from ...models.post_api_by_organisation_slug_api_keys_response_403 import PostApiByOrganisationSlugApiKeysResponse403
from ...models.post_api_by_organisation_slug_api_keys_response_500 import PostApiByOrganisationSlugApiKeysResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organisation_slug: str,
    *,
    body: Any | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/{organisation_slug}/api-keys".format(
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
    PostApiByOrganisationSlugApiKeysResponse201
    | PostApiByOrganisationSlugApiKeysResponse400
    | PostApiByOrganisationSlugApiKeysResponse401
    | PostApiByOrganisationSlugApiKeysResponse403
    | PostApiByOrganisationSlugApiKeysResponse500
    | None
):
    if response.status_code == 201:
        response_201 = PostApiByOrganisationSlugApiKeysResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = PostApiByOrganisationSlugApiKeysResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostApiByOrganisationSlugApiKeysResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostApiByOrganisationSlugApiKeysResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = PostApiByOrganisationSlugApiKeysResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostApiByOrganisationSlugApiKeysResponse201
    | PostApiByOrganisationSlugApiKeysResponse400
    | PostApiByOrganisationSlugApiKeysResponse401
    | PostApiByOrganisationSlugApiKeysResponse403
    | PostApiByOrganisationSlugApiKeysResponse500
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
    PostApiByOrganisationSlugApiKeysResponse201
    | PostApiByOrganisationSlugApiKeysResponse400
    | PostApiByOrganisationSlugApiKeysResponse401
    | PostApiByOrganisationSlugApiKeysResponse403
    | PostApiByOrganisationSlugApiKeysResponse500
]:
    """Create a new API key

     Create a new API key for the current organization. The API key will be generated automatically and
    returned only once.

    Args:
        organisation_slug (str):
        body (Any | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiByOrganisationSlugApiKeysResponse201 | PostApiByOrganisationSlugApiKeysResponse400 | PostApiByOrganisationSlugApiKeysResponse401 | PostApiByOrganisationSlugApiKeysResponse403 | PostApiByOrganisationSlugApiKeysResponse500]
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
    PostApiByOrganisationSlugApiKeysResponse201
    | PostApiByOrganisationSlugApiKeysResponse400
    | PostApiByOrganisationSlugApiKeysResponse401
    | PostApiByOrganisationSlugApiKeysResponse403
    | PostApiByOrganisationSlugApiKeysResponse500
    | None
):
    """Create a new API key

     Create a new API key for the current organization. The API key will be generated automatically and
    returned only once.

    Args:
        organisation_slug (str):
        body (Any | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiByOrganisationSlugApiKeysResponse201 | PostApiByOrganisationSlugApiKeysResponse400 | PostApiByOrganisationSlugApiKeysResponse401 | PostApiByOrganisationSlugApiKeysResponse403 | PostApiByOrganisationSlugApiKeysResponse500
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
    PostApiByOrganisationSlugApiKeysResponse201
    | PostApiByOrganisationSlugApiKeysResponse400
    | PostApiByOrganisationSlugApiKeysResponse401
    | PostApiByOrganisationSlugApiKeysResponse403
    | PostApiByOrganisationSlugApiKeysResponse500
]:
    """Create a new API key

     Create a new API key for the current organization. The API key will be generated automatically and
    returned only once.

    Args:
        organisation_slug (str):
        body (Any | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiByOrganisationSlugApiKeysResponse201 | PostApiByOrganisationSlugApiKeysResponse400 | PostApiByOrganisationSlugApiKeysResponse401 | PostApiByOrganisationSlugApiKeysResponse403 | PostApiByOrganisationSlugApiKeysResponse500]
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
    PostApiByOrganisationSlugApiKeysResponse201
    | PostApiByOrganisationSlugApiKeysResponse400
    | PostApiByOrganisationSlugApiKeysResponse401
    | PostApiByOrganisationSlugApiKeysResponse403
    | PostApiByOrganisationSlugApiKeysResponse500
    | None
):
    """Create a new API key

     Create a new API key for the current organization. The API key will be generated automatically and
    returned only once.

    Args:
        organisation_slug (str):
        body (Any | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiByOrganisationSlugApiKeysResponse201 | PostApiByOrganisationSlugApiKeysResponse400 | PostApiByOrganisationSlugApiKeysResponse401 | PostApiByOrganisationSlugApiKeysResponse403 | PostApiByOrganisationSlugApiKeysResponse500
    """

    return (
        await asyncio_detailed(
            organisation_slug=organisation_slug,
            client=client,
            body=body,
        )
    ).parsed
