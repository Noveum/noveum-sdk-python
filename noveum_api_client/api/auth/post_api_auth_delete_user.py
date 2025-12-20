from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_auth_delete_user_body import PostApiAuthDeleteUserBody
from ...models.post_api_auth_delete_user_response_200 import PostApiAuthDeleteUserResponse200
from ...models.post_api_auth_delete_user_response_400 import PostApiAuthDeleteUserResponse400
from ...models.post_api_auth_delete_user_response_401 import PostApiAuthDeleteUserResponse401
from ...models.post_api_auth_delete_user_response_403 import PostApiAuthDeleteUserResponse403
from ...models.post_api_auth_delete_user_response_404 import PostApiAuthDeleteUserResponse404
from ...models.post_api_auth_delete_user_response_429 import PostApiAuthDeleteUserResponse429
from ...models.post_api_auth_delete_user_response_500 import PostApiAuthDeleteUserResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: PostApiAuthDeleteUserBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/delete-user",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostApiAuthDeleteUserResponse200
    | PostApiAuthDeleteUserResponse400
    | PostApiAuthDeleteUserResponse401
    | PostApiAuthDeleteUserResponse403
    | PostApiAuthDeleteUserResponse404
    | PostApiAuthDeleteUserResponse429
    | PostApiAuthDeleteUserResponse500
    | None
):
    if response.status_code == 200:
        response_200 = PostApiAuthDeleteUserResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PostApiAuthDeleteUserResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostApiAuthDeleteUserResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostApiAuthDeleteUserResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostApiAuthDeleteUserResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = PostApiAuthDeleteUserResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PostApiAuthDeleteUserResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostApiAuthDeleteUserResponse200
    | PostApiAuthDeleteUserResponse400
    | PostApiAuthDeleteUserResponse401
    | PostApiAuthDeleteUserResponse403
    | PostApiAuthDeleteUserResponse404
    | PostApiAuthDeleteUserResponse429
    | PostApiAuthDeleteUserResponse500
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
    body: PostApiAuthDeleteUserBody,
) -> Response[
    PostApiAuthDeleteUserResponse200
    | PostApiAuthDeleteUserResponse400
    | PostApiAuthDeleteUserResponse401
    | PostApiAuthDeleteUserResponse403
    | PostApiAuthDeleteUserResponse404
    | PostApiAuthDeleteUserResponse429
    | PostApiAuthDeleteUserResponse500
]:
    """Delete the user

    Args:
        body (PostApiAuthDeleteUserBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthDeleteUserResponse200 | PostApiAuthDeleteUserResponse400 | PostApiAuthDeleteUserResponse401 | PostApiAuthDeleteUserResponse403 | PostApiAuthDeleteUserResponse404 | PostApiAuthDeleteUserResponse429 | PostApiAuthDeleteUserResponse500]
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
    body: PostApiAuthDeleteUserBody,
) -> (
    PostApiAuthDeleteUserResponse200
    | PostApiAuthDeleteUserResponse400
    | PostApiAuthDeleteUserResponse401
    | PostApiAuthDeleteUserResponse403
    | PostApiAuthDeleteUserResponse404
    | PostApiAuthDeleteUserResponse429
    | PostApiAuthDeleteUserResponse500
    | None
):
    """Delete the user

    Args:
        body (PostApiAuthDeleteUserBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthDeleteUserResponse200 | PostApiAuthDeleteUserResponse400 | PostApiAuthDeleteUserResponse401 | PostApiAuthDeleteUserResponse403 | PostApiAuthDeleteUserResponse404 | PostApiAuthDeleteUserResponse429 | PostApiAuthDeleteUserResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthDeleteUserBody,
) -> Response[
    PostApiAuthDeleteUserResponse200
    | PostApiAuthDeleteUserResponse400
    | PostApiAuthDeleteUserResponse401
    | PostApiAuthDeleteUserResponse403
    | PostApiAuthDeleteUserResponse404
    | PostApiAuthDeleteUserResponse429
    | PostApiAuthDeleteUserResponse500
]:
    """Delete the user

    Args:
        body (PostApiAuthDeleteUserBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthDeleteUserResponse200 | PostApiAuthDeleteUserResponse400 | PostApiAuthDeleteUserResponse401 | PostApiAuthDeleteUserResponse403 | PostApiAuthDeleteUserResponse404 | PostApiAuthDeleteUserResponse429 | PostApiAuthDeleteUserResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthDeleteUserBody,
) -> (
    PostApiAuthDeleteUserResponse200
    | PostApiAuthDeleteUserResponse400
    | PostApiAuthDeleteUserResponse401
    | PostApiAuthDeleteUserResponse403
    | PostApiAuthDeleteUserResponse404
    | PostApiAuthDeleteUserResponse429
    | PostApiAuthDeleteUserResponse500
    | None
):
    """Delete the user

    Args:
        body (PostApiAuthDeleteUserBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthDeleteUserResponse200 | PostApiAuthDeleteUserResponse400 | PostApiAuthDeleteUserResponse401 | PostApiAuthDeleteUserResponse403 | PostApiAuthDeleteUserResponse404 | PostApiAuthDeleteUserResponse429 | PostApiAuthDeleteUserResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
