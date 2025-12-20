from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_auth_sign_in_username_body import PostApiAuthSignInUsernameBody
from ...models.post_api_auth_sign_in_username_response_200 import PostApiAuthSignInUsernameResponse200
from ...models.post_api_auth_sign_in_username_response_400 import PostApiAuthSignInUsernameResponse400
from ...models.post_api_auth_sign_in_username_response_401 import PostApiAuthSignInUsernameResponse401
from ...models.post_api_auth_sign_in_username_response_403 import PostApiAuthSignInUsernameResponse403
from ...models.post_api_auth_sign_in_username_response_404 import PostApiAuthSignInUsernameResponse404
from ...models.post_api_auth_sign_in_username_response_429 import PostApiAuthSignInUsernameResponse429
from ...models.post_api_auth_sign_in_username_response_500 import PostApiAuthSignInUsernameResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: PostApiAuthSignInUsernameBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/sign-in/username",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostApiAuthSignInUsernameResponse200
    | PostApiAuthSignInUsernameResponse400
    | PostApiAuthSignInUsernameResponse401
    | PostApiAuthSignInUsernameResponse403
    | PostApiAuthSignInUsernameResponse404
    | PostApiAuthSignInUsernameResponse429
    | PostApiAuthSignInUsernameResponse500
    | None
):
    if response.status_code == 200:
        response_200 = PostApiAuthSignInUsernameResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PostApiAuthSignInUsernameResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostApiAuthSignInUsernameResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostApiAuthSignInUsernameResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostApiAuthSignInUsernameResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = PostApiAuthSignInUsernameResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PostApiAuthSignInUsernameResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostApiAuthSignInUsernameResponse200
    | PostApiAuthSignInUsernameResponse400
    | PostApiAuthSignInUsernameResponse401
    | PostApiAuthSignInUsernameResponse403
    | PostApiAuthSignInUsernameResponse404
    | PostApiAuthSignInUsernameResponse429
    | PostApiAuthSignInUsernameResponse500
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
    body: PostApiAuthSignInUsernameBody,
) -> Response[
    PostApiAuthSignInUsernameResponse200
    | PostApiAuthSignInUsernameResponse400
    | PostApiAuthSignInUsernameResponse401
    | PostApiAuthSignInUsernameResponse403
    | PostApiAuthSignInUsernameResponse404
    | PostApiAuthSignInUsernameResponse429
    | PostApiAuthSignInUsernameResponse500
]:
    """Sign in with username

    Args:
        body (PostApiAuthSignInUsernameBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthSignInUsernameResponse200 | PostApiAuthSignInUsernameResponse400 | PostApiAuthSignInUsernameResponse401 | PostApiAuthSignInUsernameResponse403 | PostApiAuthSignInUsernameResponse404 | PostApiAuthSignInUsernameResponse429 | PostApiAuthSignInUsernameResponse500]
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
    body: PostApiAuthSignInUsernameBody,
) -> (
    PostApiAuthSignInUsernameResponse200
    | PostApiAuthSignInUsernameResponse400
    | PostApiAuthSignInUsernameResponse401
    | PostApiAuthSignInUsernameResponse403
    | PostApiAuthSignInUsernameResponse404
    | PostApiAuthSignInUsernameResponse429
    | PostApiAuthSignInUsernameResponse500
    | None
):
    """Sign in with username

    Args:
        body (PostApiAuthSignInUsernameBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthSignInUsernameResponse200 | PostApiAuthSignInUsernameResponse400 | PostApiAuthSignInUsernameResponse401 | PostApiAuthSignInUsernameResponse403 | PostApiAuthSignInUsernameResponse404 | PostApiAuthSignInUsernameResponse429 | PostApiAuthSignInUsernameResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthSignInUsernameBody,
) -> Response[
    PostApiAuthSignInUsernameResponse200
    | PostApiAuthSignInUsernameResponse400
    | PostApiAuthSignInUsernameResponse401
    | PostApiAuthSignInUsernameResponse403
    | PostApiAuthSignInUsernameResponse404
    | PostApiAuthSignInUsernameResponse429
    | PostApiAuthSignInUsernameResponse500
]:
    """Sign in with username

    Args:
        body (PostApiAuthSignInUsernameBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthSignInUsernameResponse200 | PostApiAuthSignInUsernameResponse400 | PostApiAuthSignInUsernameResponse401 | PostApiAuthSignInUsernameResponse403 | PostApiAuthSignInUsernameResponse404 | PostApiAuthSignInUsernameResponse429 | PostApiAuthSignInUsernameResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthSignInUsernameBody,
) -> (
    PostApiAuthSignInUsernameResponse200
    | PostApiAuthSignInUsernameResponse400
    | PostApiAuthSignInUsernameResponse401
    | PostApiAuthSignInUsernameResponse403
    | PostApiAuthSignInUsernameResponse404
    | PostApiAuthSignInUsernameResponse429
    | PostApiAuthSignInUsernameResponse500
    | None
):
    """Sign in with username

    Args:
        body (PostApiAuthSignInUsernameBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthSignInUsernameResponse200 | PostApiAuthSignInUsernameResponse400 | PostApiAuthSignInUsernameResponse401 | PostApiAuthSignInUsernameResponse403 | PostApiAuthSignInUsernameResponse404 | PostApiAuthSignInUsernameResponse429 | PostApiAuthSignInUsernameResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
