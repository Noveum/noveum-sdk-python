from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_auth_admin_set_user_password_body import PostApiAuthAdminSetUserPasswordBody
from ...models.post_api_auth_admin_set_user_password_response_400 import PostApiAuthAdminSetUserPasswordResponse400
from ...models.post_api_auth_admin_set_user_password_response_401 import PostApiAuthAdminSetUserPasswordResponse401
from ...models.post_api_auth_admin_set_user_password_response_403 import PostApiAuthAdminSetUserPasswordResponse403
from ...models.post_api_auth_admin_set_user_password_response_404 import PostApiAuthAdminSetUserPasswordResponse404
from ...models.post_api_auth_admin_set_user_password_response_429 import PostApiAuthAdminSetUserPasswordResponse429
from ...models.post_api_auth_admin_set_user_password_response_500 import PostApiAuthAdminSetUserPasswordResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: PostApiAuthAdminSetUserPasswordBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/admin/set-user-password",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostApiAuthAdminSetUserPasswordResponse400
    | PostApiAuthAdminSetUserPasswordResponse401
    | PostApiAuthAdminSetUserPasswordResponse403
    | PostApiAuthAdminSetUserPasswordResponse404
    | PostApiAuthAdminSetUserPasswordResponse429
    | PostApiAuthAdminSetUserPasswordResponse500
    | None
):
    if response.status_code == 400:
        response_400 = PostApiAuthAdminSetUserPasswordResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostApiAuthAdminSetUserPasswordResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostApiAuthAdminSetUserPasswordResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostApiAuthAdminSetUserPasswordResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = PostApiAuthAdminSetUserPasswordResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PostApiAuthAdminSetUserPasswordResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostApiAuthAdminSetUserPasswordResponse400
    | PostApiAuthAdminSetUserPasswordResponse401
    | PostApiAuthAdminSetUserPasswordResponse403
    | PostApiAuthAdminSetUserPasswordResponse404
    | PostApiAuthAdminSetUserPasswordResponse429
    | PostApiAuthAdminSetUserPasswordResponse500
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
    body: PostApiAuthAdminSetUserPasswordBody,
) -> Response[
    PostApiAuthAdminSetUserPasswordResponse400
    | PostApiAuthAdminSetUserPasswordResponse401
    | PostApiAuthAdminSetUserPasswordResponse403
    | PostApiAuthAdminSetUserPasswordResponse404
    | PostApiAuthAdminSetUserPasswordResponse429
    | PostApiAuthAdminSetUserPasswordResponse500
]:
    """
    Args:
        body (PostApiAuthAdminSetUserPasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthAdminSetUserPasswordResponse400 | PostApiAuthAdminSetUserPasswordResponse401 | PostApiAuthAdminSetUserPasswordResponse403 | PostApiAuthAdminSetUserPasswordResponse404 | PostApiAuthAdminSetUserPasswordResponse429 | PostApiAuthAdminSetUserPasswordResponse500]
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
    body: PostApiAuthAdminSetUserPasswordBody,
) -> (
    PostApiAuthAdminSetUserPasswordResponse400
    | PostApiAuthAdminSetUserPasswordResponse401
    | PostApiAuthAdminSetUserPasswordResponse403
    | PostApiAuthAdminSetUserPasswordResponse404
    | PostApiAuthAdminSetUserPasswordResponse429
    | PostApiAuthAdminSetUserPasswordResponse500
    | None
):
    """
    Args:
        body (PostApiAuthAdminSetUserPasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthAdminSetUserPasswordResponse400 | PostApiAuthAdminSetUserPasswordResponse401 | PostApiAuthAdminSetUserPasswordResponse403 | PostApiAuthAdminSetUserPasswordResponse404 | PostApiAuthAdminSetUserPasswordResponse429 | PostApiAuthAdminSetUserPasswordResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthAdminSetUserPasswordBody,
) -> Response[
    PostApiAuthAdminSetUserPasswordResponse400
    | PostApiAuthAdminSetUserPasswordResponse401
    | PostApiAuthAdminSetUserPasswordResponse403
    | PostApiAuthAdminSetUserPasswordResponse404
    | PostApiAuthAdminSetUserPasswordResponse429
    | PostApiAuthAdminSetUserPasswordResponse500
]:
    """
    Args:
        body (PostApiAuthAdminSetUserPasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthAdminSetUserPasswordResponse400 | PostApiAuthAdminSetUserPasswordResponse401 | PostApiAuthAdminSetUserPasswordResponse403 | PostApiAuthAdminSetUserPasswordResponse404 | PostApiAuthAdminSetUserPasswordResponse429 | PostApiAuthAdminSetUserPasswordResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthAdminSetUserPasswordBody,
) -> (
    PostApiAuthAdminSetUserPasswordResponse400
    | PostApiAuthAdminSetUserPasswordResponse401
    | PostApiAuthAdminSetUserPasswordResponse403
    | PostApiAuthAdminSetUserPasswordResponse404
    | PostApiAuthAdminSetUserPasswordResponse429
    | PostApiAuthAdminSetUserPasswordResponse500
    | None
):
    """
    Args:
        body (PostApiAuthAdminSetUserPasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthAdminSetUserPasswordResponse400 | PostApiAuthAdminSetUserPasswordResponse401 | PostApiAuthAdminSetUserPasswordResponse403 | PostApiAuthAdminSetUserPasswordResponse404 | PostApiAuthAdminSetUserPasswordResponse429 | PostApiAuthAdminSetUserPasswordResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
