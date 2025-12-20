from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_auth_sign_in_social_body import PostApiAuthSignInSocialBody
from ...models.post_api_auth_sign_in_social_response_200 import PostApiAuthSignInSocialResponse200
from ...models.post_api_auth_sign_in_social_response_400 import PostApiAuthSignInSocialResponse400
from ...models.post_api_auth_sign_in_social_response_401 import PostApiAuthSignInSocialResponse401
from ...models.post_api_auth_sign_in_social_response_403 import PostApiAuthSignInSocialResponse403
from ...models.post_api_auth_sign_in_social_response_404 import PostApiAuthSignInSocialResponse404
from ...models.post_api_auth_sign_in_social_response_429 import PostApiAuthSignInSocialResponse429
from ...models.post_api_auth_sign_in_social_response_500 import PostApiAuthSignInSocialResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: PostApiAuthSignInSocialBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/sign-in/social",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostApiAuthSignInSocialResponse200
    | PostApiAuthSignInSocialResponse400
    | PostApiAuthSignInSocialResponse401
    | PostApiAuthSignInSocialResponse403
    | PostApiAuthSignInSocialResponse404
    | PostApiAuthSignInSocialResponse429
    | PostApiAuthSignInSocialResponse500
    | None
):
    if response.status_code == 200:
        response_200 = PostApiAuthSignInSocialResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PostApiAuthSignInSocialResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostApiAuthSignInSocialResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostApiAuthSignInSocialResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostApiAuthSignInSocialResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = PostApiAuthSignInSocialResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PostApiAuthSignInSocialResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostApiAuthSignInSocialResponse200
    | PostApiAuthSignInSocialResponse400
    | PostApiAuthSignInSocialResponse401
    | PostApiAuthSignInSocialResponse403
    | PostApiAuthSignInSocialResponse404
    | PostApiAuthSignInSocialResponse429
    | PostApiAuthSignInSocialResponse500
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
    body: PostApiAuthSignInSocialBody,
) -> Response[
    PostApiAuthSignInSocialResponse200
    | PostApiAuthSignInSocialResponse400
    | PostApiAuthSignInSocialResponse401
    | PostApiAuthSignInSocialResponse403
    | PostApiAuthSignInSocialResponse404
    | PostApiAuthSignInSocialResponse429
    | PostApiAuthSignInSocialResponse500
]:
    """Sign in with a social provider

    Args:
        body (PostApiAuthSignInSocialBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthSignInSocialResponse200 | PostApiAuthSignInSocialResponse400 | PostApiAuthSignInSocialResponse401 | PostApiAuthSignInSocialResponse403 | PostApiAuthSignInSocialResponse404 | PostApiAuthSignInSocialResponse429 | PostApiAuthSignInSocialResponse500]
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
    body: PostApiAuthSignInSocialBody,
) -> (
    PostApiAuthSignInSocialResponse200
    | PostApiAuthSignInSocialResponse400
    | PostApiAuthSignInSocialResponse401
    | PostApiAuthSignInSocialResponse403
    | PostApiAuthSignInSocialResponse404
    | PostApiAuthSignInSocialResponse429
    | PostApiAuthSignInSocialResponse500
    | None
):
    """Sign in with a social provider

    Args:
        body (PostApiAuthSignInSocialBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthSignInSocialResponse200 | PostApiAuthSignInSocialResponse400 | PostApiAuthSignInSocialResponse401 | PostApiAuthSignInSocialResponse403 | PostApiAuthSignInSocialResponse404 | PostApiAuthSignInSocialResponse429 | PostApiAuthSignInSocialResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthSignInSocialBody,
) -> Response[
    PostApiAuthSignInSocialResponse200
    | PostApiAuthSignInSocialResponse400
    | PostApiAuthSignInSocialResponse401
    | PostApiAuthSignInSocialResponse403
    | PostApiAuthSignInSocialResponse404
    | PostApiAuthSignInSocialResponse429
    | PostApiAuthSignInSocialResponse500
]:
    """Sign in with a social provider

    Args:
        body (PostApiAuthSignInSocialBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthSignInSocialResponse200 | PostApiAuthSignInSocialResponse400 | PostApiAuthSignInSocialResponse401 | PostApiAuthSignInSocialResponse403 | PostApiAuthSignInSocialResponse404 | PostApiAuthSignInSocialResponse429 | PostApiAuthSignInSocialResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthSignInSocialBody,
) -> (
    PostApiAuthSignInSocialResponse200
    | PostApiAuthSignInSocialResponse400
    | PostApiAuthSignInSocialResponse401
    | PostApiAuthSignInSocialResponse403
    | PostApiAuthSignInSocialResponse404
    | PostApiAuthSignInSocialResponse429
    | PostApiAuthSignInSocialResponse500
    | None
):
    """Sign in with a social provider

    Args:
        body (PostApiAuthSignInSocialBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthSignInSocialResponse200 | PostApiAuthSignInSocialResponse400 | PostApiAuthSignInSocialResponse401 | PostApiAuthSignInSocialResponse403 | PostApiAuthSignInSocialResponse404 | PostApiAuthSignInSocialResponse429 | PostApiAuthSignInSocialResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
