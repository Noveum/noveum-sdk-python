from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_auth_organization_leave_body import PostApiAuthOrganizationLeaveBody
from ...models.post_api_auth_organization_leave_response_400 import PostApiAuthOrganizationLeaveResponse400
from ...models.post_api_auth_organization_leave_response_401 import PostApiAuthOrganizationLeaveResponse401
from ...models.post_api_auth_organization_leave_response_403 import PostApiAuthOrganizationLeaveResponse403
from ...models.post_api_auth_organization_leave_response_404 import PostApiAuthOrganizationLeaveResponse404
from ...models.post_api_auth_organization_leave_response_429 import PostApiAuthOrganizationLeaveResponse429
from ...models.post_api_auth_organization_leave_response_500 import PostApiAuthOrganizationLeaveResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: PostApiAuthOrganizationLeaveBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/organization/leave",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostApiAuthOrganizationLeaveResponse400
    | PostApiAuthOrganizationLeaveResponse401
    | PostApiAuthOrganizationLeaveResponse403
    | PostApiAuthOrganizationLeaveResponse404
    | PostApiAuthOrganizationLeaveResponse429
    | PostApiAuthOrganizationLeaveResponse500
    | None
):
    if response.status_code == 400:
        response_400 = PostApiAuthOrganizationLeaveResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostApiAuthOrganizationLeaveResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostApiAuthOrganizationLeaveResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostApiAuthOrganizationLeaveResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = PostApiAuthOrganizationLeaveResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PostApiAuthOrganizationLeaveResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostApiAuthOrganizationLeaveResponse400
    | PostApiAuthOrganizationLeaveResponse401
    | PostApiAuthOrganizationLeaveResponse403
    | PostApiAuthOrganizationLeaveResponse404
    | PostApiAuthOrganizationLeaveResponse429
    | PostApiAuthOrganizationLeaveResponse500
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
    body: PostApiAuthOrganizationLeaveBody,
) -> Response[
    PostApiAuthOrganizationLeaveResponse400
    | PostApiAuthOrganizationLeaveResponse401
    | PostApiAuthOrganizationLeaveResponse403
    | PostApiAuthOrganizationLeaveResponse404
    | PostApiAuthOrganizationLeaveResponse429
    | PostApiAuthOrganizationLeaveResponse500
]:
    """
    Args:
        body (PostApiAuthOrganizationLeaveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthOrganizationLeaveResponse400 | PostApiAuthOrganizationLeaveResponse401 | PostApiAuthOrganizationLeaveResponse403 | PostApiAuthOrganizationLeaveResponse404 | PostApiAuthOrganizationLeaveResponse429 | PostApiAuthOrganizationLeaveResponse500]
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
    body: PostApiAuthOrganizationLeaveBody,
) -> (
    PostApiAuthOrganizationLeaveResponse400
    | PostApiAuthOrganizationLeaveResponse401
    | PostApiAuthOrganizationLeaveResponse403
    | PostApiAuthOrganizationLeaveResponse404
    | PostApiAuthOrganizationLeaveResponse429
    | PostApiAuthOrganizationLeaveResponse500
    | None
):
    """
    Args:
        body (PostApiAuthOrganizationLeaveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthOrganizationLeaveResponse400 | PostApiAuthOrganizationLeaveResponse401 | PostApiAuthOrganizationLeaveResponse403 | PostApiAuthOrganizationLeaveResponse404 | PostApiAuthOrganizationLeaveResponse429 | PostApiAuthOrganizationLeaveResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthOrganizationLeaveBody,
) -> Response[
    PostApiAuthOrganizationLeaveResponse400
    | PostApiAuthOrganizationLeaveResponse401
    | PostApiAuthOrganizationLeaveResponse403
    | PostApiAuthOrganizationLeaveResponse404
    | PostApiAuthOrganizationLeaveResponse429
    | PostApiAuthOrganizationLeaveResponse500
]:
    """
    Args:
        body (PostApiAuthOrganizationLeaveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthOrganizationLeaveResponse400 | PostApiAuthOrganizationLeaveResponse401 | PostApiAuthOrganizationLeaveResponse403 | PostApiAuthOrganizationLeaveResponse404 | PostApiAuthOrganizationLeaveResponse429 | PostApiAuthOrganizationLeaveResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthOrganizationLeaveBody,
) -> (
    PostApiAuthOrganizationLeaveResponse400
    | PostApiAuthOrganizationLeaveResponse401
    | PostApiAuthOrganizationLeaveResponse403
    | PostApiAuthOrganizationLeaveResponse404
    | PostApiAuthOrganizationLeaveResponse429
    | PostApiAuthOrganizationLeaveResponse500
    | None
):
    """
    Args:
        body (PostApiAuthOrganizationLeaveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthOrganizationLeaveResponse400 | PostApiAuthOrganizationLeaveResponse401 | PostApiAuthOrganizationLeaveResponse403 | PostApiAuthOrganizationLeaveResponse404 | PostApiAuthOrganizationLeaveResponse429 | PostApiAuthOrganizationLeaveResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
