from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_auth_sign_out_body import PostApiAuthSignOutBody
from ...models.post_api_auth_sign_out_response_200 import PostApiAuthSignOutResponse200
from ...models.post_api_auth_sign_out_response_400 import PostApiAuthSignOutResponse400
from ...models.post_api_auth_sign_out_response_401 import PostApiAuthSignOutResponse401
from ...models.post_api_auth_sign_out_response_403 import PostApiAuthSignOutResponse403
from ...models.post_api_auth_sign_out_response_404 import PostApiAuthSignOutResponse404
from ...models.post_api_auth_sign_out_response_429 import PostApiAuthSignOutResponse429
from ...models.post_api_auth_sign_out_response_500 import PostApiAuthSignOutResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApiAuthSignOutBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/sign-out",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostApiAuthSignOutResponse200
    | PostApiAuthSignOutResponse400
    | PostApiAuthSignOutResponse401
    | PostApiAuthSignOutResponse403
    | PostApiAuthSignOutResponse404
    | PostApiAuthSignOutResponse429
    | PostApiAuthSignOutResponse500
    | None
):
    if response.status_code == 200:
        response_200 = PostApiAuthSignOutResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PostApiAuthSignOutResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostApiAuthSignOutResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostApiAuthSignOutResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostApiAuthSignOutResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = PostApiAuthSignOutResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PostApiAuthSignOutResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostApiAuthSignOutResponse200
    | PostApiAuthSignOutResponse400
    | PostApiAuthSignOutResponse401
    | PostApiAuthSignOutResponse403
    | PostApiAuthSignOutResponse404
    | PostApiAuthSignOutResponse429
    | PostApiAuthSignOutResponse500
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
    body: PostApiAuthSignOutBody | Unset = UNSET,
) -> Response[
    PostApiAuthSignOutResponse200
    | PostApiAuthSignOutResponse400
    | PostApiAuthSignOutResponse401
    | PostApiAuthSignOutResponse403
    | PostApiAuthSignOutResponse404
    | PostApiAuthSignOutResponse429
    | PostApiAuthSignOutResponse500
]:
    """Sign out the current user

    Args:
        body (PostApiAuthSignOutBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthSignOutResponse200 | PostApiAuthSignOutResponse400 | PostApiAuthSignOutResponse401 | PostApiAuthSignOutResponse403 | PostApiAuthSignOutResponse404 | PostApiAuthSignOutResponse429 | PostApiAuthSignOutResponse500]
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
    body: PostApiAuthSignOutBody | Unset = UNSET,
) -> (
    PostApiAuthSignOutResponse200
    | PostApiAuthSignOutResponse400
    | PostApiAuthSignOutResponse401
    | PostApiAuthSignOutResponse403
    | PostApiAuthSignOutResponse404
    | PostApiAuthSignOutResponse429
    | PostApiAuthSignOutResponse500
    | None
):
    """Sign out the current user

    Args:
        body (PostApiAuthSignOutBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthSignOutResponse200 | PostApiAuthSignOutResponse400 | PostApiAuthSignOutResponse401 | PostApiAuthSignOutResponse403 | PostApiAuthSignOutResponse404 | PostApiAuthSignOutResponse429 | PostApiAuthSignOutResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthSignOutBody | Unset = UNSET,
) -> Response[
    PostApiAuthSignOutResponse200
    | PostApiAuthSignOutResponse400
    | PostApiAuthSignOutResponse401
    | PostApiAuthSignOutResponse403
    | PostApiAuthSignOutResponse404
    | PostApiAuthSignOutResponse429
    | PostApiAuthSignOutResponse500
]:
    """Sign out the current user

    Args:
        body (PostApiAuthSignOutBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthSignOutResponse200 | PostApiAuthSignOutResponse400 | PostApiAuthSignOutResponse401 | PostApiAuthSignOutResponse403 | PostApiAuthSignOutResponse404 | PostApiAuthSignOutResponse429 | PostApiAuthSignOutResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthSignOutBody | Unset = UNSET,
) -> (
    PostApiAuthSignOutResponse200
    | PostApiAuthSignOutResponse400
    | PostApiAuthSignOutResponse401
    | PostApiAuthSignOutResponse403
    | PostApiAuthSignOutResponse404
    | PostApiAuthSignOutResponse429
    | PostApiAuthSignOutResponse500
    | None
):
    """Sign out the current user

    Args:
        body (PostApiAuthSignOutBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthSignOutResponse200 | PostApiAuthSignOutResponse400 | PostApiAuthSignOutResponse401 | PostApiAuthSignOutResponse403 | PostApiAuthSignOutResponse404 | PostApiAuthSignOutResponse429 | PostApiAuthSignOutResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
