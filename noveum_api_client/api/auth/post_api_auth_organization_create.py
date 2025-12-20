from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.organization import Organization
from ...models.post_api_auth_organization_create_body import PostApiAuthOrganizationCreateBody
from ...models.post_api_auth_organization_create_response_400 import PostApiAuthOrganizationCreateResponse400
from ...models.post_api_auth_organization_create_response_401 import PostApiAuthOrganizationCreateResponse401
from ...models.post_api_auth_organization_create_response_403 import PostApiAuthOrganizationCreateResponse403
from ...models.post_api_auth_organization_create_response_404 import PostApiAuthOrganizationCreateResponse404
from ...models.post_api_auth_organization_create_response_429 import PostApiAuthOrganizationCreateResponse429
from ...models.post_api_auth_organization_create_response_500 import PostApiAuthOrganizationCreateResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: PostApiAuthOrganizationCreateBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/organization/create",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Organization
    | PostApiAuthOrganizationCreateResponse400
    | PostApiAuthOrganizationCreateResponse401
    | PostApiAuthOrganizationCreateResponse403
    | PostApiAuthOrganizationCreateResponse404
    | PostApiAuthOrganizationCreateResponse429
    | PostApiAuthOrganizationCreateResponse500
    | None
):
    if response.status_code == 200:
        response_200 = Organization.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PostApiAuthOrganizationCreateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostApiAuthOrganizationCreateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostApiAuthOrganizationCreateResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostApiAuthOrganizationCreateResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = PostApiAuthOrganizationCreateResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PostApiAuthOrganizationCreateResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Organization
    | PostApiAuthOrganizationCreateResponse400
    | PostApiAuthOrganizationCreateResponse401
    | PostApiAuthOrganizationCreateResponse403
    | PostApiAuthOrganizationCreateResponse404
    | PostApiAuthOrganizationCreateResponse429
    | PostApiAuthOrganizationCreateResponse500
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
    body: PostApiAuthOrganizationCreateBody,
) -> Response[
    Organization
    | PostApiAuthOrganizationCreateResponse400
    | PostApiAuthOrganizationCreateResponse401
    | PostApiAuthOrganizationCreateResponse403
    | PostApiAuthOrganizationCreateResponse404
    | PostApiAuthOrganizationCreateResponse429
    | PostApiAuthOrganizationCreateResponse500
]:
    """Create an organization

    Args:
        body (PostApiAuthOrganizationCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Organization | PostApiAuthOrganizationCreateResponse400 | PostApiAuthOrganizationCreateResponse401 | PostApiAuthOrganizationCreateResponse403 | PostApiAuthOrganizationCreateResponse404 | PostApiAuthOrganizationCreateResponse429 | PostApiAuthOrganizationCreateResponse500]
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
    body: PostApiAuthOrganizationCreateBody,
) -> (
    Organization
    | PostApiAuthOrganizationCreateResponse400
    | PostApiAuthOrganizationCreateResponse401
    | PostApiAuthOrganizationCreateResponse403
    | PostApiAuthOrganizationCreateResponse404
    | PostApiAuthOrganizationCreateResponse429
    | PostApiAuthOrganizationCreateResponse500
    | None
):
    """Create an organization

    Args:
        body (PostApiAuthOrganizationCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Organization | PostApiAuthOrganizationCreateResponse400 | PostApiAuthOrganizationCreateResponse401 | PostApiAuthOrganizationCreateResponse403 | PostApiAuthOrganizationCreateResponse404 | PostApiAuthOrganizationCreateResponse429 | PostApiAuthOrganizationCreateResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthOrganizationCreateBody,
) -> Response[
    Organization
    | PostApiAuthOrganizationCreateResponse400
    | PostApiAuthOrganizationCreateResponse401
    | PostApiAuthOrganizationCreateResponse403
    | PostApiAuthOrganizationCreateResponse404
    | PostApiAuthOrganizationCreateResponse429
    | PostApiAuthOrganizationCreateResponse500
]:
    """Create an organization

    Args:
        body (PostApiAuthOrganizationCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Organization | PostApiAuthOrganizationCreateResponse400 | PostApiAuthOrganizationCreateResponse401 | PostApiAuthOrganizationCreateResponse403 | PostApiAuthOrganizationCreateResponse404 | PostApiAuthOrganizationCreateResponse429 | PostApiAuthOrganizationCreateResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthOrganizationCreateBody,
) -> (
    Organization
    | PostApiAuthOrganizationCreateResponse400
    | PostApiAuthOrganizationCreateResponse401
    | PostApiAuthOrganizationCreateResponse403
    | PostApiAuthOrganizationCreateResponse404
    | PostApiAuthOrganizationCreateResponse429
    | PostApiAuthOrganizationCreateResponse500
    | None
):
    """Create an organization

    Args:
        body (PostApiAuthOrganizationCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Organization | PostApiAuthOrganizationCreateResponse400 | PostApiAuthOrganizationCreateResponse401 | PostApiAuthOrganizationCreateResponse403 | PostApiAuthOrganizationCreateResponse404 | PostApiAuthOrganizationCreateResponse429 | PostApiAuthOrganizationCreateResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
