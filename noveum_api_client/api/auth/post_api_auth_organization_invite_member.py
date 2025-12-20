from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_auth_organization_invite_member_body import PostApiAuthOrganizationInviteMemberBody
from ...models.post_api_auth_organization_invite_member_response_200 import (
    PostApiAuthOrganizationInviteMemberResponse200,
)
from ...models.post_api_auth_organization_invite_member_response_400 import (
    PostApiAuthOrganizationInviteMemberResponse400,
)
from ...models.post_api_auth_organization_invite_member_response_401 import (
    PostApiAuthOrganizationInviteMemberResponse401,
)
from ...models.post_api_auth_organization_invite_member_response_403 import (
    PostApiAuthOrganizationInviteMemberResponse403,
)
from ...models.post_api_auth_organization_invite_member_response_404 import (
    PostApiAuthOrganizationInviteMemberResponse404,
)
from ...models.post_api_auth_organization_invite_member_response_429 import (
    PostApiAuthOrganizationInviteMemberResponse429,
)
from ...models.post_api_auth_organization_invite_member_response_500 import (
    PostApiAuthOrganizationInviteMemberResponse500,
)
from ...types import Response


def _get_kwargs(
    *,
    body: PostApiAuthOrganizationInviteMemberBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/organization/invite-member",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostApiAuthOrganizationInviteMemberResponse200
    | PostApiAuthOrganizationInviteMemberResponse400
    | PostApiAuthOrganizationInviteMemberResponse401
    | PostApiAuthOrganizationInviteMemberResponse403
    | PostApiAuthOrganizationInviteMemberResponse404
    | PostApiAuthOrganizationInviteMemberResponse429
    | PostApiAuthOrganizationInviteMemberResponse500
    | None
):
    if response.status_code == 200:
        response_200 = PostApiAuthOrganizationInviteMemberResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PostApiAuthOrganizationInviteMemberResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostApiAuthOrganizationInviteMemberResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostApiAuthOrganizationInviteMemberResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostApiAuthOrganizationInviteMemberResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = PostApiAuthOrganizationInviteMemberResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PostApiAuthOrganizationInviteMemberResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostApiAuthOrganizationInviteMemberResponse200
    | PostApiAuthOrganizationInviteMemberResponse400
    | PostApiAuthOrganizationInviteMemberResponse401
    | PostApiAuthOrganizationInviteMemberResponse403
    | PostApiAuthOrganizationInviteMemberResponse404
    | PostApiAuthOrganizationInviteMemberResponse429
    | PostApiAuthOrganizationInviteMemberResponse500
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
    body: PostApiAuthOrganizationInviteMemberBody,
) -> Response[
    PostApiAuthOrganizationInviteMemberResponse200
    | PostApiAuthOrganizationInviteMemberResponse400
    | PostApiAuthOrganizationInviteMemberResponse401
    | PostApiAuthOrganizationInviteMemberResponse403
    | PostApiAuthOrganizationInviteMemberResponse404
    | PostApiAuthOrganizationInviteMemberResponse429
    | PostApiAuthOrganizationInviteMemberResponse500
]:
    """Invite a user to an organization

    Args:
        body (PostApiAuthOrganizationInviteMemberBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthOrganizationInviteMemberResponse200 | PostApiAuthOrganizationInviteMemberResponse400 | PostApiAuthOrganizationInviteMemberResponse401 | PostApiAuthOrganizationInviteMemberResponse403 | PostApiAuthOrganizationInviteMemberResponse404 | PostApiAuthOrganizationInviteMemberResponse429 | PostApiAuthOrganizationInviteMemberResponse500]
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
    body: PostApiAuthOrganizationInviteMemberBody,
) -> (
    PostApiAuthOrganizationInviteMemberResponse200
    | PostApiAuthOrganizationInviteMemberResponse400
    | PostApiAuthOrganizationInviteMemberResponse401
    | PostApiAuthOrganizationInviteMemberResponse403
    | PostApiAuthOrganizationInviteMemberResponse404
    | PostApiAuthOrganizationInviteMemberResponse429
    | PostApiAuthOrganizationInviteMemberResponse500
    | None
):
    """Invite a user to an organization

    Args:
        body (PostApiAuthOrganizationInviteMemberBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthOrganizationInviteMemberResponse200 | PostApiAuthOrganizationInviteMemberResponse400 | PostApiAuthOrganizationInviteMemberResponse401 | PostApiAuthOrganizationInviteMemberResponse403 | PostApiAuthOrganizationInviteMemberResponse404 | PostApiAuthOrganizationInviteMemberResponse429 | PostApiAuthOrganizationInviteMemberResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthOrganizationInviteMemberBody,
) -> Response[
    PostApiAuthOrganizationInviteMemberResponse200
    | PostApiAuthOrganizationInviteMemberResponse400
    | PostApiAuthOrganizationInviteMemberResponse401
    | PostApiAuthOrganizationInviteMemberResponse403
    | PostApiAuthOrganizationInviteMemberResponse404
    | PostApiAuthOrganizationInviteMemberResponse429
    | PostApiAuthOrganizationInviteMemberResponse500
]:
    """Invite a user to an organization

    Args:
        body (PostApiAuthOrganizationInviteMemberBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthOrganizationInviteMemberResponse200 | PostApiAuthOrganizationInviteMemberResponse400 | PostApiAuthOrganizationInviteMemberResponse401 | PostApiAuthOrganizationInviteMemberResponse403 | PostApiAuthOrganizationInviteMemberResponse404 | PostApiAuthOrganizationInviteMemberResponse429 | PostApiAuthOrganizationInviteMemberResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthOrganizationInviteMemberBody,
) -> (
    PostApiAuthOrganizationInviteMemberResponse200
    | PostApiAuthOrganizationInviteMemberResponse400
    | PostApiAuthOrganizationInviteMemberResponse401
    | PostApiAuthOrganizationInviteMemberResponse403
    | PostApiAuthOrganizationInviteMemberResponse404
    | PostApiAuthOrganizationInviteMemberResponse429
    | PostApiAuthOrganizationInviteMemberResponse500
    | None
):
    """Invite a user to an organization

    Args:
        body (PostApiAuthOrganizationInviteMemberBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthOrganizationInviteMemberResponse200 | PostApiAuthOrganizationInviteMemberResponse400 | PostApiAuthOrganizationInviteMemberResponse401 | PostApiAuthOrganizationInviteMemberResponse403 | PostApiAuthOrganizationInviteMemberResponse404 | PostApiAuthOrganizationInviteMemberResponse429 | PostApiAuthOrganizationInviteMemberResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
