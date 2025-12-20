from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_auth_organization_accept_invitation_body import PostApiAuthOrganizationAcceptInvitationBody
from ...models.post_api_auth_organization_accept_invitation_response_200 import (
    PostApiAuthOrganizationAcceptInvitationResponse200,
)
from ...models.post_api_auth_organization_accept_invitation_response_400 import (
    PostApiAuthOrganizationAcceptInvitationResponse400,
)
from ...models.post_api_auth_organization_accept_invitation_response_401 import (
    PostApiAuthOrganizationAcceptInvitationResponse401,
)
from ...models.post_api_auth_organization_accept_invitation_response_403 import (
    PostApiAuthOrganizationAcceptInvitationResponse403,
)
from ...models.post_api_auth_organization_accept_invitation_response_404 import (
    PostApiAuthOrganizationAcceptInvitationResponse404,
)
from ...models.post_api_auth_organization_accept_invitation_response_429 import (
    PostApiAuthOrganizationAcceptInvitationResponse429,
)
from ...models.post_api_auth_organization_accept_invitation_response_500 import (
    PostApiAuthOrganizationAcceptInvitationResponse500,
)
from ...types import Response


def _get_kwargs(
    *,
    body: PostApiAuthOrganizationAcceptInvitationBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/organization/accept-invitation",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostApiAuthOrganizationAcceptInvitationResponse200
    | PostApiAuthOrganizationAcceptInvitationResponse400
    | PostApiAuthOrganizationAcceptInvitationResponse401
    | PostApiAuthOrganizationAcceptInvitationResponse403
    | PostApiAuthOrganizationAcceptInvitationResponse404
    | PostApiAuthOrganizationAcceptInvitationResponse429
    | PostApiAuthOrganizationAcceptInvitationResponse500
    | None
):
    if response.status_code == 200:
        response_200 = PostApiAuthOrganizationAcceptInvitationResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PostApiAuthOrganizationAcceptInvitationResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostApiAuthOrganizationAcceptInvitationResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostApiAuthOrganizationAcceptInvitationResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostApiAuthOrganizationAcceptInvitationResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = PostApiAuthOrganizationAcceptInvitationResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PostApiAuthOrganizationAcceptInvitationResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostApiAuthOrganizationAcceptInvitationResponse200
    | PostApiAuthOrganizationAcceptInvitationResponse400
    | PostApiAuthOrganizationAcceptInvitationResponse401
    | PostApiAuthOrganizationAcceptInvitationResponse403
    | PostApiAuthOrganizationAcceptInvitationResponse404
    | PostApiAuthOrganizationAcceptInvitationResponse429
    | PostApiAuthOrganizationAcceptInvitationResponse500
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
    body: PostApiAuthOrganizationAcceptInvitationBody,
) -> Response[
    PostApiAuthOrganizationAcceptInvitationResponse200
    | PostApiAuthOrganizationAcceptInvitationResponse400
    | PostApiAuthOrganizationAcceptInvitationResponse401
    | PostApiAuthOrganizationAcceptInvitationResponse403
    | PostApiAuthOrganizationAcceptInvitationResponse404
    | PostApiAuthOrganizationAcceptInvitationResponse429
    | PostApiAuthOrganizationAcceptInvitationResponse500
]:
    """Accept an invitation to an organization

    Args:
        body (PostApiAuthOrganizationAcceptInvitationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthOrganizationAcceptInvitationResponse200 | PostApiAuthOrganizationAcceptInvitationResponse400 | PostApiAuthOrganizationAcceptInvitationResponse401 | PostApiAuthOrganizationAcceptInvitationResponse403 | PostApiAuthOrganizationAcceptInvitationResponse404 | PostApiAuthOrganizationAcceptInvitationResponse429 | PostApiAuthOrganizationAcceptInvitationResponse500]
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
    body: PostApiAuthOrganizationAcceptInvitationBody,
) -> (
    PostApiAuthOrganizationAcceptInvitationResponse200
    | PostApiAuthOrganizationAcceptInvitationResponse400
    | PostApiAuthOrganizationAcceptInvitationResponse401
    | PostApiAuthOrganizationAcceptInvitationResponse403
    | PostApiAuthOrganizationAcceptInvitationResponse404
    | PostApiAuthOrganizationAcceptInvitationResponse429
    | PostApiAuthOrganizationAcceptInvitationResponse500
    | None
):
    """Accept an invitation to an organization

    Args:
        body (PostApiAuthOrganizationAcceptInvitationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthOrganizationAcceptInvitationResponse200 | PostApiAuthOrganizationAcceptInvitationResponse400 | PostApiAuthOrganizationAcceptInvitationResponse401 | PostApiAuthOrganizationAcceptInvitationResponse403 | PostApiAuthOrganizationAcceptInvitationResponse404 | PostApiAuthOrganizationAcceptInvitationResponse429 | PostApiAuthOrganizationAcceptInvitationResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthOrganizationAcceptInvitationBody,
) -> Response[
    PostApiAuthOrganizationAcceptInvitationResponse200
    | PostApiAuthOrganizationAcceptInvitationResponse400
    | PostApiAuthOrganizationAcceptInvitationResponse401
    | PostApiAuthOrganizationAcceptInvitationResponse403
    | PostApiAuthOrganizationAcceptInvitationResponse404
    | PostApiAuthOrganizationAcceptInvitationResponse429
    | PostApiAuthOrganizationAcceptInvitationResponse500
]:
    """Accept an invitation to an organization

    Args:
        body (PostApiAuthOrganizationAcceptInvitationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthOrganizationAcceptInvitationResponse200 | PostApiAuthOrganizationAcceptInvitationResponse400 | PostApiAuthOrganizationAcceptInvitationResponse401 | PostApiAuthOrganizationAcceptInvitationResponse403 | PostApiAuthOrganizationAcceptInvitationResponse404 | PostApiAuthOrganizationAcceptInvitationResponse429 | PostApiAuthOrganizationAcceptInvitationResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthOrganizationAcceptInvitationBody,
) -> (
    PostApiAuthOrganizationAcceptInvitationResponse200
    | PostApiAuthOrganizationAcceptInvitationResponse400
    | PostApiAuthOrganizationAcceptInvitationResponse401
    | PostApiAuthOrganizationAcceptInvitationResponse403
    | PostApiAuthOrganizationAcceptInvitationResponse404
    | PostApiAuthOrganizationAcceptInvitationResponse429
    | PostApiAuthOrganizationAcceptInvitationResponse500
    | None
):
    """Accept an invitation to an organization

    Args:
        body (PostApiAuthOrganizationAcceptInvitationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthOrganizationAcceptInvitationResponse200 | PostApiAuthOrganizationAcceptInvitationResponse400 | PostApiAuthOrganizationAcceptInvitationResponse401 | PostApiAuthOrganizationAcceptInvitationResponse403 | PostApiAuthOrganizationAcceptInvitationResponse404 | PostApiAuthOrganizationAcceptInvitationResponse429 | PostApiAuthOrganizationAcceptInvitationResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
