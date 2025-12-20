from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_auth_forget_password_body import PostApiAuthForgetPasswordBody
from ...models.post_api_auth_forget_password_response_200 import PostApiAuthForgetPasswordResponse200
from ...models.post_api_auth_forget_password_response_400 import PostApiAuthForgetPasswordResponse400
from ...models.post_api_auth_forget_password_response_401 import PostApiAuthForgetPasswordResponse401
from ...models.post_api_auth_forget_password_response_403 import PostApiAuthForgetPasswordResponse403
from ...models.post_api_auth_forget_password_response_404 import PostApiAuthForgetPasswordResponse404
from ...models.post_api_auth_forget_password_response_429 import PostApiAuthForgetPasswordResponse429
from ...models.post_api_auth_forget_password_response_500 import PostApiAuthForgetPasswordResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: PostApiAuthForgetPasswordBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/forget-password",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostApiAuthForgetPasswordResponse200
    | PostApiAuthForgetPasswordResponse400
    | PostApiAuthForgetPasswordResponse401
    | PostApiAuthForgetPasswordResponse403
    | PostApiAuthForgetPasswordResponse404
    | PostApiAuthForgetPasswordResponse429
    | PostApiAuthForgetPasswordResponse500
    | None
):
    if response.status_code == 200:
        response_200 = PostApiAuthForgetPasswordResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PostApiAuthForgetPasswordResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostApiAuthForgetPasswordResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostApiAuthForgetPasswordResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostApiAuthForgetPasswordResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = PostApiAuthForgetPasswordResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PostApiAuthForgetPasswordResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostApiAuthForgetPasswordResponse200
    | PostApiAuthForgetPasswordResponse400
    | PostApiAuthForgetPasswordResponse401
    | PostApiAuthForgetPasswordResponse403
    | PostApiAuthForgetPasswordResponse404
    | PostApiAuthForgetPasswordResponse429
    | PostApiAuthForgetPasswordResponse500
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
    body: PostApiAuthForgetPasswordBody,
) -> Response[
    PostApiAuthForgetPasswordResponse200
    | PostApiAuthForgetPasswordResponse400
    | PostApiAuthForgetPasswordResponse401
    | PostApiAuthForgetPasswordResponse403
    | PostApiAuthForgetPasswordResponse404
    | PostApiAuthForgetPasswordResponse429
    | PostApiAuthForgetPasswordResponse500
]:
    """Send a password reset email to the user

    Args:
        body (PostApiAuthForgetPasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthForgetPasswordResponse200 | PostApiAuthForgetPasswordResponse400 | PostApiAuthForgetPasswordResponse401 | PostApiAuthForgetPasswordResponse403 | PostApiAuthForgetPasswordResponse404 | PostApiAuthForgetPasswordResponse429 | PostApiAuthForgetPasswordResponse500]
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
    body: PostApiAuthForgetPasswordBody,
) -> (
    PostApiAuthForgetPasswordResponse200
    | PostApiAuthForgetPasswordResponse400
    | PostApiAuthForgetPasswordResponse401
    | PostApiAuthForgetPasswordResponse403
    | PostApiAuthForgetPasswordResponse404
    | PostApiAuthForgetPasswordResponse429
    | PostApiAuthForgetPasswordResponse500
    | None
):
    """Send a password reset email to the user

    Args:
        body (PostApiAuthForgetPasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthForgetPasswordResponse200 | PostApiAuthForgetPasswordResponse400 | PostApiAuthForgetPasswordResponse401 | PostApiAuthForgetPasswordResponse403 | PostApiAuthForgetPasswordResponse404 | PostApiAuthForgetPasswordResponse429 | PostApiAuthForgetPasswordResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthForgetPasswordBody,
) -> Response[
    PostApiAuthForgetPasswordResponse200
    | PostApiAuthForgetPasswordResponse400
    | PostApiAuthForgetPasswordResponse401
    | PostApiAuthForgetPasswordResponse403
    | PostApiAuthForgetPasswordResponse404
    | PostApiAuthForgetPasswordResponse429
    | PostApiAuthForgetPasswordResponse500
]:
    """Send a password reset email to the user

    Args:
        body (PostApiAuthForgetPasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthForgetPasswordResponse200 | PostApiAuthForgetPasswordResponse400 | PostApiAuthForgetPasswordResponse401 | PostApiAuthForgetPasswordResponse403 | PostApiAuthForgetPasswordResponse404 | PostApiAuthForgetPasswordResponse429 | PostApiAuthForgetPasswordResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthForgetPasswordBody,
) -> (
    PostApiAuthForgetPasswordResponse200
    | PostApiAuthForgetPasswordResponse400
    | PostApiAuthForgetPasswordResponse401
    | PostApiAuthForgetPasswordResponse403
    | PostApiAuthForgetPasswordResponse404
    | PostApiAuthForgetPasswordResponse429
    | PostApiAuthForgetPasswordResponse500
    | None
):
    """Send a password reset email to the user

    Args:
        body (PostApiAuthForgetPasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthForgetPasswordResponse200 | PostApiAuthForgetPasswordResponse400 | PostApiAuthForgetPasswordResponse401 | PostApiAuthForgetPasswordResponse403 | PostApiAuthForgetPasswordResponse404 | PostApiAuthForgetPasswordResponse429 | PostApiAuthForgetPasswordResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
