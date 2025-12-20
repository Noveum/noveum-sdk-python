from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_auth_update_user_body import PostApiAuthUpdateUserBody
from ...models.post_api_auth_update_user_response_200 import PostApiAuthUpdateUserResponse200
from ...models.post_api_auth_update_user_response_400 import PostApiAuthUpdateUserResponse400
from ...models.post_api_auth_update_user_response_401 import PostApiAuthUpdateUserResponse401
from ...models.post_api_auth_update_user_response_403 import PostApiAuthUpdateUserResponse403
from ...models.post_api_auth_update_user_response_404 import PostApiAuthUpdateUserResponse404
from ...models.post_api_auth_update_user_response_429 import PostApiAuthUpdateUserResponse429
from ...models.post_api_auth_update_user_response_500 import PostApiAuthUpdateUserResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApiAuthUpdateUserBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/update-user",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostApiAuthUpdateUserResponse200
    | PostApiAuthUpdateUserResponse400
    | PostApiAuthUpdateUserResponse401
    | PostApiAuthUpdateUserResponse403
    | PostApiAuthUpdateUserResponse404
    | PostApiAuthUpdateUserResponse429
    | PostApiAuthUpdateUserResponse500
    | None
):
    if response.status_code == 200:
        response_200 = PostApiAuthUpdateUserResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PostApiAuthUpdateUserResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostApiAuthUpdateUserResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostApiAuthUpdateUserResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostApiAuthUpdateUserResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = PostApiAuthUpdateUserResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PostApiAuthUpdateUserResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostApiAuthUpdateUserResponse200
    | PostApiAuthUpdateUserResponse400
    | PostApiAuthUpdateUserResponse401
    | PostApiAuthUpdateUserResponse403
    | PostApiAuthUpdateUserResponse404
    | PostApiAuthUpdateUserResponse429
    | PostApiAuthUpdateUserResponse500
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
    body: PostApiAuthUpdateUserBody | Unset = UNSET,
) -> Response[
    PostApiAuthUpdateUserResponse200
    | PostApiAuthUpdateUserResponse400
    | PostApiAuthUpdateUserResponse401
    | PostApiAuthUpdateUserResponse403
    | PostApiAuthUpdateUserResponse404
    | PostApiAuthUpdateUserResponse429
    | PostApiAuthUpdateUserResponse500
]:
    """Update the current user

    Args:
        body (PostApiAuthUpdateUserBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthUpdateUserResponse200 | PostApiAuthUpdateUserResponse400 | PostApiAuthUpdateUserResponse401 | PostApiAuthUpdateUserResponse403 | PostApiAuthUpdateUserResponse404 | PostApiAuthUpdateUserResponse429 | PostApiAuthUpdateUserResponse500]
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
    body: PostApiAuthUpdateUserBody | Unset = UNSET,
) -> (
    PostApiAuthUpdateUserResponse200
    | PostApiAuthUpdateUserResponse400
    | PostApiAuthUpdateUserResponse401
    | PostApiAuthUpdateUserResponse403
    | PostApiAuthUpdateUserResponse404
    | PostApiAuthUpdateUserResponse429
    | PostApiAuthUpdateUserResponse500
    | None
):
    """Update the current user

    Args:
        body (PostApiAuthUpdateUserBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthUpdateUserResponse200 | PostApiAuthUpdateUserResponse400 | PostApiAuthUpdateUserResponse401 | PostApiAuthUpdateUserResponse403 | PostApiAuthUpdateUserResponse404 | PostApiAuthUpdateUserResponse429 | PostApiAuthUpdateUserResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthUpdateUserBody | Unset = UNSET,
) -> Response[
    PostApiAuthUpdateUserResponse200
    | PostApiAuthUpdateUserResponse400
    | PostApiAuthUpdateUserResponse401
    | PostApiAuthUpdateUserResponse403
    | PostApiAuthUpdateUserResponse404
    | PostApiAuthUpdateUserResponse429
    | PostApiAuthUpdateUserResponse500
]:
    """Update the current user

    Args:
        body (PostApiAuthUpdateUserBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthUpdateUserResponse200 | PostApiAuthUpdateUserResponse400 | PostApiAuthUpdateUserResponse401 | PostApiAuthUpdateUserResponse403 | PostApiAuthUpdateUserResponse404 | PostApiAuthUpdateUserResponse429 | PostApiAuthUpdateUserResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthUpdateUserBody | Unset = UNSET,
) -> (
    PostApiAuthUpdateUserResponse200
    | PostApiAuthUpdateUserResponse400
    | PostApiAuthUpdateUserResponse401
    | PostApiAuthUpdateUserResponse403
    | PostApiAuthUpdateUserResponse404
    | PostApiAuthUpdateUserResponse429
    | PostApiAuthUpdateUserResponse500
    | None
):
    """Update the current user

    Args:
        body (PostApiAuthUpdateUserBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthUpdateUserResponse200 | PostApiAuthUpdateUserResponse400 | PostApiAuthUpdateUserResponse401 | PostApiAuthUpdateUserResponse403 | PostApiAuthUpdateUserResponse404 | PostApiAuthUpdateUserResponse429 | PostApiAuthUpdateUserResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
