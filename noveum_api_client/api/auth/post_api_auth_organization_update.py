from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.organization import Organization
from ...models.post_api_auth_organization_update_body import PostApiAuthOrganizationUpdateBody
from ...models.post_api_auth_organization_update_response_400 import PostApiAuthOrganizationUpdateResponse400
from ...models.post_api_auth_organization_update_response_401 import PostApiAuthOrganizationUpdateResponse401
from ...models.post_api_auth_organization_update_response_403 import PostApiAuthOrganizationUpdateResponse403
from ...models.post_api_auth_organization_update_response_404 import PostApiAuthOrganizationUpdateResponse404
from ...models.post_api_auth_organization_update_response_429 import PostApiAuthOrganizationUpdateResponse429
from ...models.post_api_auth_organization_update_response_500 import PostApiAuthOrganizationUpdateResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: PostApiAuthOrganizationUpdateBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/organization/update",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Organization
    | PostApiAuthOrganizationUpdateResponse400
    | PostApiAuthOrganizationUpdateResponse401
    | PostApiAuthOrganizationUpdateResponse403
    | PostApiAuthOrganizationUpdateResponse404
    | PostApiAuthOrganizationUpdateResponse429
    | PostApiAuthOrganizationUpdateResponse500
    | None
):
    if response.status_code == 200:
        response_200 = Organization.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PostApiAuthOrganizationUpdateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostApiAuthOrganizationUpdateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostApiAuthOrganizationUpdateResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostApiAuthOrganizationUpdateResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = PostApiAuthOrganizationUpdateResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PostApiAuthOrganizationUpdateResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Organization
    | PostApiAuthOrganizationUpdateResponse400
    | PostApiAuthOrganizationUpdateResponse401
    | PostApiAuthOrganizationUpdateResponse403
    | PostApiAuthOrganizationUpdateResponse404
    | PostApiAuthOrganizationUpdateResponse429
    | PostApiAuthOrganizationUpdateResponse500
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
    body: PostApiAuthOrganizationUpdateBody,
) -> Response[
    Organization
    | PostApiAuthOrganizationUpdateResponse400
    | PostApiAuthOrganizationUpdateResponse401
    | PostApiAuthOrganizationUpdateResponse403
    | PostApiAuthOrganizationUpdateResponse404
    | PostApiAuthOrganizationUpdateResponse429
    | PostApiAuthOrganizationUpdateResponse500
]:
    """Update an organization

    Args:
        body (PostApiAuthOrganizationUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Organization | PostApiAuthOrganizationUpdateResponse400 | PostApiAuthOrganizationUpdateResponse401 | PostApiAuthOrganizationUpdateResponse403 | PostApiAuthOrganizationUpdateResponse404 | PostApiAuthOrganizationUpdateResponse429 | PostApiAuthOrganizationUpdateResponse500]
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
    body: PostApiAuthOrganizationUpdateBody,
) -> (
    Organization
    | PostApiAuthOrganizationUpdateResponse400
    | PostApiAuthOrganizationUpdateResponse401
    | PostApiAuthOrganizationUpdateResponse403
    | PostApiAuthOrganizationUpdateResponse404
    | PostApiAuthOrganizationUpdateResponse429
    | PostApiAuthOrganizationUpdateResponse500
    | None
):
    """Update an organization

    Args:
        body (PostApiAuthOrganizationUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Organization | PostApiAuthOrganizationUpdateResponse400 | PostApiAuthOrganizationUpdateResponse401 | PostApiAuthOrganizationUpdateResponse403 | PostApiAuthOrganizationUpdateResponse404 | PostApiAuthOrganizationUpdateResponse429 | PostApiAuthOrganizationUpdateResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthOrganizationUpdateBody,
) -> Response[
    Organization
    | PostApiAuthOrganizationUpdateResponse400
    | PostApiAuthOrganizationUpdateResponse401
    | PostApiAuthOrganizationUpdateResponse403
    | PostApiAuthOrganizationUpdateResponse404
    | PostApiAuthOrganizationUpdateResponse429
    | PostApiAuthOrganizationUpdateResponse500
]:
    """Update an organization

    Args:
        body (PostApiAuthOrganizationUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Organization | PostApiAuthOrganizationUpdateResponse400 | PostApiAuthOrganizationUpdateResponse401 | PostApiAuthOrganizationUpdateResponse403 | PostApiAuthOrganizationUpdateResponse404 | PostApiAuthOrganizationUpdateResponse429 | PostApiAuthOrganizationUpdateResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthOrganizationUpdateBody,
) -> (
    Organization
    | PostApiAuthOrganizationUpdateResponse400
    | PostApiAuthOrganizationUpdateResponse401
    | PostApiAuthOrganizationUpdateResponse403
    | PostApiAuthOrganizationUpdateResponse404
    | PostApiAuthOrganizationUpdateResponse429
    | PostApiAuthOrganizationUpdateResponse500
    | None
):
    """Update an organization

    Args:
        body (PostApiAuthOrganizationUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Organization | PostApiAuthOrganizationUpdateResponse400 | PostApiAuthOrganizationUpdateResponse401 | PostApiAuthOrganizationUpdateResponse403 | PostApiAuthOrganizationUpdateResponse404 | PostApiAuthOrganizationUpdateResponse429 | PostApiAuthOrganizationUpdateResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
