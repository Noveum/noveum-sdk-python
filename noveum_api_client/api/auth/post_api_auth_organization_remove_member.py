from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_auth_organization_remove_member_body import PostApiAuthOrganizationRemoveMemberBody
from ...models.post_api_auth_organization_remove_member_response_200 import (
    PostApiAuthOrganizationRemoveMemberResponse200,
)
from ...models.post_api_auth_organization_remove_member_response_400 import (
    PostApiAuthOrganizationRemoveMemberResponse400,
)
from ...models.post_api_auth_organization_remove_member_response_401 import (
    PostApiAuthOrganizationRemoveMemberResponse401,
)
from ...models.post_api_auth_organization_remove_member_response_403 import (
    PostApiAuthOrganizationRemoveMemberResponse403,
)
from ...models.post_api_auth_organization_remove_member_response_404 import (
    PostApiAuthOrganizationRemoveMemberResponse404,
)
from ...models.post_api_auth_organization_remove_member_response_429 import (
    PostApiAuthOrganizationRemoveMemberResponse429,
)
from ...models.post_api_auth_organization_remove_member_response_500 import (
    PostApiAuthOrganizationRemoveMemberResponse500,
)
from ...types import Response


def _get_kwargs(
    *,
    body: PostApiAuthOrganizationRemoveMemberBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/organization/remove-member",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostApiAuthOrganizationRemoveMemberResponse200
    | PostApiAuthOrganizationRemoveMemberResponse400
    | PostApiAuthOrganizationRemoveMemberResponse401
    | PostApiAuthOrganizationRemoveMemberResponse403
    | PostApiAuthOrganizationRemoveMemberResponse404
    | PostApiAuthOrganizationRemoveMemberResponse429
    | PostApiAuthOrganizationRemoveMemberResponse500
    | None
):
    if response.status_code == 200:
        response_200 = PostApiAuthOrganizationRemoveMemberResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PostApiAuthOrganizationRemoveMemberResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostApiAuthOrganizationRemoveMemberResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostApiAuthOrganizationRemoveMemberResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostApiAuthOrganizationRemoveMemberResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = PostApiAuthOrganizationRemoveMemberResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PostApiAuthOrganizationRemoveMemberResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostApiAuthOrganizationRemoveMemberResponse200
    | PostApiAuthOrganizationRemoveMemberResponse400
    | PostApiAuthOrganizationRemoveMemberResponse401
    | PostApiAuthOrganizationRemoveMemberResponse403
    | PostApiAuthOrganizationRemoveMemberResponse404
    | PostApiAuthOrganizationRemoveMemberResponse429
    | PostApiAuthOrganizationRemoveMemberResponse500
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
    body: PostApiAuthOrganizationRemoveMemberBody,
) -> Response[
    PostApiAuthOrganizationRemoveMemberResponse200
    | PostApiAuthOrganizationRemoveMemberResponse400
    | PostApiAuthOrganizationRemoveMemberResponse401
    | PostApiAuthOrganizationRemoveMemberResponse403
    | PostApiAuthOrganizationRemoveMemberResponse404
    | PostApiAuthOrganizationRemoveMemberResponse429
    | PostApiAuthOrganizationRemoveMemberResponse500
]:
    """Remove a member from an organization

    Args:
        body (PostApiAuthOrganizationRemoveMemberBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthOrganizationRemoveMemberResponse200 | PostApiAuthOrganizationRemoveMemberResponse400 | PostApiAuthOrganizationRemoveMemberResponse401 | PostApiAuthOrganizationRemoveMemberResponse403 | PostApiAuthOrganizationRemoveMemberResponse404 | PostApiAuthOrganizationRemoveMemberResponse429 | PostApiAuthOrganizationRemoveMemberResponse500]
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
    body: PostApiAuthOrganizationRemoveMemberBody,
) -> (
    PostApiAuthOrganizationRemoveMemberResponse200
    | PostApiAuthOrganizationRemoveMemberResponse400
    | PostApiAuthOrganizationRemoveMemberResponse401
    | PostApiAuthOrganizationRemoveMemberResponse403
    | PostApiAuthOrganizationRemoveMemberResponse404
    | PostApiAuthOrganizationRemoveMemberResponse429
    | PostApiAuthOrganizationRemoveMemberResponse500
    | None
):
    """Remove a member from an organization

    Args:
        body (PostApiAuthOrganizationRemoveMemberBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthOrganizationRemoveMemberResponse200 | PostApiAuthOrganizationRemoveMemberResponse400 | PostApiAuthOrganizationRemoveMemberResponse401 | PostApiAuthOrganizationRemoveMemberResponse403 | PostApiAuthOrganizationRemoveMemberResponse404 | PostApiAuthOrganizationRemoveMemberResponse429 | PostApiAuthOrganizationRemoveMemberResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthOrganizationRemoveMemberBody,
) -> Response[
    PostApiAuthOrganizationRemoveMemberResponse200
    | PostApiAuthOrganizationRemoveMemberResponse400
    | PostApiAuthOrganizationRemoveMemberResponse401
    | PostApiAuthOrganizationRemoveMemberResponse403
    | PostApiAuthOrganizationRemoveMemberResponse404
    | PostApiAuthOrganizationRemoveMemberResponse429
    | PostApiAuthOrganizationRemoveMemberResponse500
]:
    """Remove a member from an organization

    Args:
        body (PostApiAuthOrganizationRemoveMemberBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthOrganizationRemoveMemberResponse200 | PostApiAuthOrganizationRemoveMemberResponse400 | PostApiAuthOrganizationRemoveMemberResponse401 | PostApiAuthOrganizationRemoveMemberResponse403 | PostApiAuthOrganizationRemoveMemberResponse404 | PostApiAuthOrganizationRemoveMemberResponse429 | PostApiAuthOrganizationRemoveMemberResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthOrganizationRemoveMemberBody,
) -> (
    PostApiAuthOrganizationRemoveMemberResponse200
    | PostApiAuthOrganizationRemoveMemberResponse400
    | PostApiAuthOrganizationRemoveMemberResponse401
    | PostApiAuthOrganizationRemoveMemberResponse403
    | PostApiAuthOrganizationRemoveMemberResponse404
    | PostApiAuthOrganizationRemoveMemberResponse429
    | PostApiAuthOrganizationRemoveMemberResponse500
    | None
):
    """Remove a member from an organization

    Args:
        body (PostApiAuthOrganizationRemoveMemberBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthOrganizationRemoveMemberResponse200 | PostApiAuthOrganizationRemoveMemberResponse400 | PostApiAuthOrganizationRemoveMemberResponse401 | PostApiAuthOrganizationRemoveMemberResponse403 | PostApiAuthOrganizationRemoveMemberResponse404 | PostApiAuthOrganizationRemoveMemberResponse429 | PostApiAuthOrganizationRemoveMemberResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
