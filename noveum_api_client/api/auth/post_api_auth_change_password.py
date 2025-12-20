from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_auth_change_password_body import PostApiAuthChangePasswordBody
from ...models.post_api_auth_change_password_response_200 import PostApiAuthChangePasswordResponse200
from ...models.post_api_auth_change_password_response_400 import PostApiAuthChangePasswordResponse400
from ...models.post_api_auth_change_password_response_401 import PostApiAuthChangePasswordResponse401
from ...models.post_api_auth_change_password_response_403 import PostApiAuthChangePasswordResponse403
from ...models.post_api_auth_change_password_response_404 import PostApiAuthChangePasswordResponse404
from ...models.post_api_auth_change_password_response_429 import PostApiAuthChangePasswordResponse429
from ...models.post_api_auth_change_password_response_500 import PostApiAuthChangePasswordResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: PostApiAuthChangePasswordBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/change-password",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostApiAuthChangePasswordResponse200
    | PostApiAuthChangePasswordResponse400
    | PostApiAuthChangePasswordResponse401
    | PostApiAuthChangePasswordResponse403
    | PostApiAuthChangePasswordResponse404
    | PostApiAuthChangePasswordResponse429
    | PostApiAuthChangePasswordResponse500
    | None
):
    if response.status_code == 200:
        response_200 = PostApiAuthChangePasswordResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PostApiAuthChangePasswordResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostApiAuthChangePasswordResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostApiAuthChangePasswordResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostApiAuthChangePasswordResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = PostApiAuthChangePasswordResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PostApiAuthChangePasswordResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostApiAuthChangePasswordResponse200
    | PostApiAuthChangePasswordResponse400
    | PostApiAuthChangePasswordResponse401
    | PostApiAuthChangePasswordResponse403
    | PostApiAuthChangePasswordResponse404
    | PostApiAuthChangePasswordResponse429
    | PostApiAuthChangePasswordResponse500
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
    body: PostApiAuthChangePasswordBody,
) -> Response[
    PostApiAuthChangePasswordResponse200
    | PostApiAuthChangePasswordResponse400
    | PostApiAuthChangePasswordResponse401
    | PostApiAuthChangePasswordResponse403
    | PostApiAuthChangePasswordResponse404
    | PostApiAuthChangePasswordResponse429
    | PostApiAuthChangePasswordResponse500
]:
    """Change the password of the user

    Args:
        body (PostApiAuthChangePasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthChangePasswordResponse200 | PostApiAuthChangePasswordResponse400 | PostApiAuthChangePasswordResponse401 | PostApiAuthChangePasswordResponse403 | PostApiAuthChangePasswordResponse404 | PostApiAuthChangePasswordResponse429 | PostApiAuthChangePasswordResponse500]
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
    body: PostApiAuthChangePasswordBody,
) -> (
    PostApiAuthChangePasswordResponse200
    | PostApiAuthChangePasswordResponse400
    | PostApiAuthChangePasswordResponse401
    | PostApiAuthChangePasswordResponse403
    | PostApiAuthChangePasswordResponse404
    | PostApiAuthChangePasswordResponse429
    | PostApiAuthChangePasswordResponse500
    | None
):
    """Change the password of the user

    Args:
        body (PostApiAuthChangePasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthChangePasswordResponse200 | PostApiAuthChangePasswordResponse400 | PostApiAuthChangePasswordResponse401 | PostApiAuthChangePasswordResponse403 | PostApiAuthChangePasswordResponse404 | PostApiAuthChangePasswordResponse429 | PostApiAuthChangePasswordResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthChangePasswordBody,
) -> Response[
    PostApiAuthChangePasswordResponse200
    | PostApiAuthChangePasswordResponse400
    | PostApiAuthChangePasswordResponse401
    | PostApiAuthChangePasswordResponse403
    | PostApiAuthChangePasswordResponse404
    | PostApiAuthChangePasswordResponse429
    | PostApiAuthChangePasswordResponse500
]:
    """Change the password of the user

    Args:
        body (PostApiAuthChangePasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthChangePasswordResponse200 | PostApiAuthChangePasswordResponse400 | PostApiAuthChangePasswordResponse401 | PostApiAuthChangePasswordResponse403 | PostApiAuthChangePasswordResponse404 | PostApiAuthChangePasswordResponse429 | PostApiAuthChangePasswordResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthChangePasswordBody,
) -> (
    PostApiAuthChangePasswordResponse200
    | PostApiAuthChangePasswordResponse400
    | PostApiAuthChangePasswordResponse401
    | PostApiAuthChangePasswordResponse403
    | PostApiAuthChangePasswordResponse404
    | PostApiAuthChangePasswordResponse429
    | PostApiAuthChangePasswordResponse500
    | None
):
    """Change the password of the user

    Args:
        body (PostApiAuthChangePasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthChangePasswordResponse200 | PostApiAuthChangePasswordResponse400 | PostApiAuthChangePasswordResponse401 | PostApiAuthChangePasswordResponse403 | PostApiAuthChangePasswordResponse404 | PostApiAuthChangePasswordResponse429 | PostApiAuthChangePasswordResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
