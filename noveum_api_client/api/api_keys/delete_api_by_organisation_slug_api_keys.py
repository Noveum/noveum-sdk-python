from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_api_by_organisation_slug_api_keys_response_200 import (
    DeleteApiByOrganisationSlugApiKeysResponse200,
)
from ...models.delete_api_by_organisation_slug_api_keys_response_400 import (
    DeleteApiByOrganisationSlugApiKeysResponse400,
)
from ...models.delete_api_by_organisation_slug_api_keys_response_401 import (
    DeleteApiByOrganisationSlugApiKeysResponse401,
)
from ...models.delete_api_by_organisation_slug_api_keys_response_403 import (
    DeleteApiByOrganisationSlugApiKeysResponse403,
)
from ...models.delete_api_by_organisation_slug_api_keys_response_404 import (
    DeleteApiByOrganisationSlugApiKeysResponse404,
)
from ...models.delete_api_by_organisation_slug_api_keys_response_500 import (
    DeleteApiByOrganisationSlugApiKeysResponse500,
)
from ...types import UNSET, Response


def _get_kwargs(
    organisation_slug: str,
    *,
    id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["id"] = id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/{organisation_slug}/api-keys".format(
            organisation_slug=quote(str(organisation_slug), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteApiByOrganisationSlugApiKeysResponse200
    | DeleteApiByOrganisationSlugApiKeysResponse400
    | DeleteApiByOrganisationSlugApiKeysResponse401
    | DeleteApiByOrganisationSlugApiKeysResponse403
    | DeleteApiByOrganisationSlugApiKeysResponse404
    | DeleteApiByOrganisationSlugApiKeysResponse500
    | None
):
    if response.status_code == 200:
        response_200 = DeleteApiByOrganisationSlugApiKeysResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = DeleteApiByOrganisationSlugApiKeysResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteApiByOrganisationSlugApiKeysResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteApiByOrganisationSlugApiKeysResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteApiByOrganisationSlugApiKeysResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = DeleteApiByOrganisationSlugApiKeysResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteApiByOrganisationSlugApiKeysResponse200
    | DeleteApiByOrganisationSlugApiKeysResponse400
    | DeleteApiByOrganisationSlugApiKeysResponse401
    | DeleteApiByOrganisationSlugApiKeysResponse403
    | DeleteApiByOrganisationSlugApiKeysResponse404
    | DeleteApiByOrganisationSlugApiKeysResponse500
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
    id: str,
) -> Response[
    DeleteApiByOrganisationSlugApiKeysResponse200
    | DeleteApiByOrganisationSlugApiKeysResponse400
    | DeleteApiByOrganisationSlugApiKeysResponse401
    | DeleteApiByOrganisationSlugApiKeysResponse403
    | DeleteApiByOrganisationSlugApiKeysResponse404
    | DeleteApiByOrganisationSlugApiKeysResponse500
]:
    """Delete an API key

     Delete an API key. Users can only delete their own keys unless they are organization admins.

    Args:
        organisation_slug (str):
        id (str): The ID of the API key to delete

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteApiByOrganisationSlugApiKeysResponse200 | DeleteApiByOrganisationSlugApiKeysResponse400 | DeleteApiByOrganisationSlugApiKeysResponse401 | DeleteApiByOrganisationSlugApiKeysResponse403 | DeleteApiByOrganisationSlugApiKeysResponse404 | DeleteApiByOrganisationSlugApiKeysResponse500]
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
    *,
    client: AuthenticatedClient | Client,
    id: str,
) -> (
    DeleteApiByOrganisationSlugApiKeysResponse200
    | DeleteApiByOrganisationSlugApiKeysResponse400
    | DeleteApiByOrganisationSlugApiKeysResponse401
    | DeleteApiByOrganisationSlugApiKeysResponse403
    | DeleteApiByOrganisationSlugApiKeysResponse404
    | DeleteApiByOrganisationSlugApiKeysResponse500
    | None
):
    """Delete an API key

     Delete an API key. Users can only delete their own keys unless they are organization admins.

    Args:
        organisation_slug (str):
        id (str): The ID of the API key to delete

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteApiByOrganisationSlugApiKeysResponse200 | DeleteApiByOrganisationSlugApiKeysResponse400 | DeleteApiByOrganisationSlugApiKeysResponse401 | DeleteApiByOrganisationSlugApiKeysResponse403 | DeleteApiByOrganisationSlugApiKeysResponse404 | DeleteApiByOrganisationSlugApiKeysResponse500
    """

    return sync_detailed(
        organisation_slug=organisation_slug,
        client=client,
        id=id,
    ).parsed


async def asyncio_detailed(
    organisation_slug: str,
    *,
    client: AuthenticatedClient | Client,
    id: str,
) -> Response[
    DeleteApiByOrganisationSlugApiKeysResponse200
    | DeleteApiByOrganisationSlugApiKeysResponse400
    | DeleteApiByOrganisationSlugApiKeysResponse401
    | DeleteApiByOrganisationSlugApiKeysResponse403
    | DeleteApiByOrganisationSlugApiKeysResponse404
    | DeleteApiByOrganisationSlugApiKeysResponse500
]:
    """Delete an API key

     Delete an API key. Users can only delete their own keys unless they are organization admins.

    Args:
        organisation_slug (str):
        id (str): The ID of the API key to delete

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteApiByOrganisationSlugApiKeysResponse200 | DeleteApiByOrganisationSlugApiKeysResponse400 | DeleteApiByOrganisationSlugApiKeysResponse401 | DeleteApiByOrganisationSlugApiKeysResponse403 | DeleteApiByOrganisationSlugApiKeysResponse404 | DeleteApiByOrganisationSlugApiKeysResponse500]
    """

    kwargs = _get_kwargs(
        organisation_slug=organisation_slug,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organisation_slug: str,
    *,
    client: AuthenticatedClient | Client,
    id: str,
) -> (
    DeleteApiByOrganisationSlugApiKeysResponse200
    | DeleteApiByOrganisationSlugApiKeysResponse400
    | DeleteApiByOrganisationSlugApiKeysResponse401
    | DeleteApiByOrganisationSlugApiKeysResponse403
    | DeleteApiByOrganisationSlugApiKeysResponse404
    | DeleteApiByOrganisationSlugApiKeysResponse500
    | None
):
    """Delete an API key

     Delete an API key. Users can only delete their own keys unless they are organization admins.

    Args:
        organisation_slug (str):
        id (str): The ID of the API key to delete

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteApiByOrganisationSlugApiKeysResponse200 | DeleteApiByOrganisationSlugApiKeysResponse400 | DeleteApiByOrganisationSlugApiKeysResponse401 | DeleteApiByOrganisationSlugApiKeysResponse403 | DeleteApiByOrganisationSlugApiKeysResponse404 | DeleteApiByOrganisationSlugApiKeysResponse500
    """

    return (
        await asyncio_detailed(
            organisation_slug=organisation_slug,
            client=client,
            id=id,
        )
    ).parsed
