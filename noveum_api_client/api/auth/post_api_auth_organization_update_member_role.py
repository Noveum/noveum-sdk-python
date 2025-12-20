from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_auth_organization_update_member_role_body import PostApiAuthOrganizationUpdateMemberRoleBody
from ...models.post_api_auth_organization_update_member_role_response_200 import (
    PostApiAuthOrganizationUpdateMemberRoleResponse200,
)
from ...models.post_api_auth_organization_update_member_role_response_400 import (
    PostApiAuthOrganizationUpdateMemberRoleResponse400,
)
from ...models.post_api_auth_organization_update_member_role_response_401 import (
    PostApiAuthOrganizationUpdateMemberRoleResponse401,
)
from ...models.post_api_auth_organization_update_member_role_response_403 import (
    PostApiAuthOrganizationUpdateMemberRoleResponse403,
)
from ...models.post_api_auth_organization_update_member_role_response_404 import (
    PostApiAuthOrganizationUpdateMemberRoleResponse404,
)
from ...models.post_api_auth_organization_update_member_role_response_429 import (
    PostApiAuthOrganizationUpdateMemberRoleResponse429,
)
from ...models.post_api_auth_organization_update_member_role_response_500 import (
    PostApiAuthOrganizationUpdateMemberRoleResponse500,
)
from ...types import Response


def _get_kwargs(
    *,
    body: PostApiAuthOrganizationUpdateMemberRoleBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/organization/update-member-role",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostApiAuthOrganizationUpdateMemberRoleResponse200
    | PostApiAuthOrganizationUpdateMemberRoleResponse400
    | PostApiAuthOrganizationUpdateMemberRoleResponse401
    | PostApiAuthOrganizationUpdateMemberRoleResponse403
    | PostApiAuthOrganizationUpdateMemberRoleResponse404
    | PostApiAuthOrganizationUpdateMemberRoleResponse429
    | PostApiAuthOrganizationUpdateMemberRoleResponse500
    | None
):
    if response.status_code == 200:
        response_200 = PostApiAuthOrganizationUpdateMemberRoleResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PostApiAuthOrganizationUpdateMemberRoleResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostApiAuthOrganizationUpdateMemberRoleResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostApiAuthOrganizationUpdateMemberRoleResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostApiAuthOrganizationUpdateMemberRoleResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = PostApiAuthOrganizationUpdateMemberRoleResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PostApiAuthOrganizationUpdateMemberRoleResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostApiAuthOrganizationUpdateMemberRoleResponse200
    | PostApiAuthOrganizationUpdateMemberRoleResponse400
    | PostApiAuthOrganizationUpdateMemberRoleResponse401
    | PostApiAuthOrganizationUpdateMemberRoleResponse403
    | PostApiAuthOrganizationUpdateMemberRoleResponse404
    | PostApiAuthOrganizationUpdateMemberRoleResponse429
    | PostApiAuthOrganizationUpdateMemberRoleResponse500
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
    body: PostApiAuthOrganizationUpdateMemberRoleBody,
) -> Response[
    PostApiAuthOrganizationUpdateMemberRoleResponse200
    | PostApiAuthOrganizationUpdateMemberRoleResponse400
    | PostApiAuthOrganizationUpdateMemberRoleResponse401
    | PostApiAuthOrganizationUpdateMemberRoleResponse403
    | PostApiAuthOrganizationUpdateMemberRoleResponse404
    | PostApiAuthOrganizationUpdateMemberRoleResponse429
    | PostApiAuthOrganizationUpdateMemberRoleResponse500
]:
    """Update the role of a member in an organization

    Args:
        body (PostApiAuthOrganizationUpdateMemberRoleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthOrganizationUpdateMemberRoleResponse200 | PostApiAuthOrganizationUpdateMemberRoleResponse400 | PostApiAuthOrganizationUpdateMemberRoleResponse401 | PostApiAuthOrganizationUpdateMemberRoleResponse403 | PostApiAuthOrganizationUpdateMemberRoleResponse404 | PostApiAuthOrganizationUpdateMemberRoleResponse429 | PostApiAuthOrganizationUpdateMemberRoleResponse500]
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
    body: PostApiAuthOrganizationUpdateMemberRoleBody,
) -> (
    PostApiAuthOrganizationUpdateMemberRoleResponse200
    | PostApiAuthOrganizationUpdateMemberRoleResponse400
    | PostApiAuthOrganizationUpdateMemberRoleResponse401
    | PostApiAuthOrganizationUpdateMemberRoleResponse403
    | PostApiAuthOrganizationUpdateMemberRoleResponse404
    | PostApiAuthOrganizationUpdateMemberRoleResponse429
    | PostApiAuthOrganizationUpdateMemberRoleResponse500
    | None
):
    """Update the role of a member in an organization

    Args:
        body (PostApiAuthOrganizationUpdateMemberRoleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthOrganizationUpdateMemberRoleResponse200 | PostApiAuthOrganizationUpdateMemberRoleResponse400 | PostApiAuthOrganizationUpdateMemberRoleResponse401 | PostApiAuthOrganizationUpdateMemberRoleResponse403 | PostApiAuthOrganizationUpdateMemberRoleResponse404 | PostApiAuthOrganizationUpdateMemberRoleResponse429 | PostApiAuthOrganizationUpdateMemberRoleResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthOrganizationUpdateMemberRoleBody,
) -> Response[
    PostApiAuthOrganizationUpdateMemberRoleResponse200
    | PostApiAuthOrganizationUpdateMemberRoleResponse400
    | PostApiAuthOrganizationUpdateMemberRoleResponse401
    | PostApiAuthOrganizationUpdateMemberRoleResponse403
    | PostApiAuthOrganizationUpdateMemberRoleResponse404
    | PostApiAuthOrganizationUpdateMemberRoleResponse429
    | PostApiAuthOrganizationUpdateMemberRoleResponse500
]:
    """Update the role of a member in an organization

    Args:
        body (PostApiAuthOrganizationUpdateMemberRoleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthOrganizationUpdateMemberRoleResponse200 | PostApiAuthOrganizationUpdateMemberRoleResponse400 | PostApiAuthOrganizationUpdateMemberRoleResponse401 | PostApiAuthOrganizationUpdateMemberRoleResponse403 | PostApiAuthOrganizationUpdateMemberRoleResponse404 | PostApiAuthOrganizationUpdateMemberRoleResponse429 | PostApiAuthOrganizationUpdateMemberRoleResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthOrganizationUpdateMemberRoleBody,
) -> (
    PostApiAuthOrganizationUpdateMemberRoleResponse200
    | PostApiAuthOrganizationUpdateMemberRoleResponse400
    | PostApiAuthOrganizationUpdateMemberRoleResponse401
    | PostApiAuthOrganizationUpdateMemberRoleResponse403
    | PostApiAuthOrganizationUpdateMemberRoleResponse404
    | PostApiAuthOrganizationUpdateMemberRoleResponse429
    | PostApiAuthOrganizationUpdateMemberRoleResponse500
    | None
):
    """Update the role of a member in an organization

    Args:
        body (PostApiAuthOrganizationUpdateMemberRoleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthOrganizationUpdateMemberRoleResponse200 | PostApiAuthOrganizationUpdateMemberRoleResponse400 | PostApiAuthOrganizationUpdateMemberRoleResponse401 | PostApiAuthOrganizationUpdateMemberRoleResponse403 | PostApiAuthOrganizationUpdateMemberRoleResponse404 | PostApiAuthOrganizationUpdateMemberRoleResponse429 | PostApiAuthOrganizationUpdateMemberRoleResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
