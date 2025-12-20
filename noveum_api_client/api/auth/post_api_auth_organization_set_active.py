from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.organization import Organization
from ...models.post_api_auth_organization_set_active_body import PostApiAuthOrganizationSetActiveBody
from ...models.post_api_auth_organization_set_active_response_400 import PostApiAuthOrganizationSetActiveResponse400
from ...models.post_api_auth_organization_set_active_response_401 import PostApiAuthOrganizationSetActiveResponse401
from ...models.post_api_auth_organization_set_active_response_403 import PostApiAuthOrganizationSetActiveResponse403
from ...models.post_api_auth_organization_set_active_response_404 import PostApiAuthOrganizationSetActiveResponse404
from ...models.post_api_auth_organization_set_active_response_429 import PostApiAuthOrganizationSetActiveResponse429
from ...models.post_api_auth_organization_set_active_response_500 import PostApiAuthOrganizationSetActiveResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: PostApiAuthOrganizationSetActiveBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/organization/set-active",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Organization
    | PostApiAuthOrganizationSetActiveResponse400
    | PostApiAuthOrganizationSetActiveResponse401
    | PostApiAuthOrganizationSetActiveResponse403
    | PostApiAuthOrganizationSetActiveResponse404
    | PostApiAuthOrganizationSetActiveResponse429
    | PostApiAuthOrganizationSetActiveResponse500
    | None
):
    if response.status_code == 200:
        response_200 = Organization.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PostApiAuthOrganizationSetActiveResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostApiAuthOrganizationSetActiveResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostApiAuthOrganizationSetActiveResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostApiAuthOrganizationSetActiveResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = PostApiAuthOrganizationSetActiveResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PostApiAuthOrganizationSetActiveResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Organization
    | PostApiAuthOrganizationSetActiveResponse400
    | PostApiAuthOrganizationSetActiveResponse401
    | PostApiAuthOrganizationSetActiveResponse403
    | PostApiAuthOrganizationSetActiveResponse404
    | PostApiAuthOrganizationSetActiveResponse429
    | PostApiAuthOrganizationSetActiveResponse500
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
    body: PostApiAuthOrganizationSetActiveBody,
) -> Response[
    Organization
    | PostApiAuthOrganizationSetActiveResponse400
    | PostApiAuthOrganizationSetActiveResponse401
    | PostApiAuthOrganizationSetActiveResponse403
    | PostApiAuthOrganizationSetActiveResponse404
    | PostApiAuthOrganizationSetActiveResponse429
    | PostApiAuthOrganizationSetActiveResponse500
]:
    """Set the active organization

    Args:
        body (PostApiAuthOrganizationSetActiveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Organization | PostApiAuthOrganizationSetActiveResponse400 | PostApiAuthOrganizationSetActiveResponse401 | PostApiAuthOrganizationSetActiveResponse403 | PostApiAuthOrganizationSetActiveResponse404 | PostApiAuthOrganizationSetActiveResponse429 | PostApiAuthOrganizationSetActiveResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthOrganizationSetActiveBody,
) -> (
    Organization
    | PostApiAuthOrganizationSetActiveResponse400
    | PostApiAuthOrganizationSetActiveResponse401
    | PostApiAuthOrganizationSetActiveResponse403
    | PostApiAuthOrganizationSetActiveResponse404
    | PostApiAuthOrganizationSetActiveResponse429
    | PostApiAuthOrganizationSetActiveResponse500
    | None
):
    """Set the active organization

    Args:
        body (PostApiAuthOrganizationSetActiveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Organization | PostApiAuthOrganizationSetActiveResponse400 | PostApiAuthOrganizationSetActiveResponse401 | PostApiAuthOrganizationSetActiveResponse403 | PostApiAuthOrganizationSetActiveResponse404 | PostApiAuthOrganizationSetActiveResponse429 | PostApiAuthOrganizationSetActiveResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthOrganizationSetActiveBody,
) -> Response[
    Organization
    | PostApiAuthOrganizationSetActiveResponse400
    | PostApiAuthOrganizationSetActiveResponse401
    | PostApiAuthOrganizationSetActiveResponse403
    | PostApiAuthOrganizationSetActiveResponse404
    | PostApiAuthOrganizationSetActiveResponse429
    | PostApiAuthOrganizationSetActiveResponse500
]:
    """Set the active organization

    Args:
        body (PostApiAuthOrganizationSetActiveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Organization | PostApiAuthOrganizationSetActiveResponse400 | PostApiAuthOrganizationSetActiveResponse401 | PostApiAuthOrganizationSetActiveResponse403 | PostApiAuthOrganizationSetActiveResponse404 | PostApiAuthOrganizationSetActiveResponse429 | PostApiAuthOrganizationSetActiveResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthOrganizationSetActiveBody,
) -> (
    Organization
    | PostApiAuthOrganizationSetActiveResponse400
    | PostApiAuthOrganizationSetActiveResponse401
    | PostApiAuthOrganizationSetActiveResponse403
    | PostApiAuthOrganizationSetActiveResponse404
    | PostApiAuthOrganizationSetActiveResponse429
    | PostApiAuthOrganizationSetActiveResponse500
    | None
):
    """Set the active organization

    Args:
        body (PostApiAuthOrganizationSetActiveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Organization | PostApiAuthOrganizationSetActiveResponse400 | PostApiAuthOrganizationSetActiveResponse401 | PostApiAuthOrganizationSetActiveResponse403 | PostApiAuthOrganizationSetActiveResponse404 | PostApiAuthOrganizationSetActiveResponse429 | PostApiAuthOrganizationSetActiveResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
