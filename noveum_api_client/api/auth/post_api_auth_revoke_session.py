from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_auth_revoke_session_body import PostApiAuthRevokeSessionBody
from ...models.post_api_auth_revoke_session_response_400 import PostApiAuthRevokeSessionResponse400
from ...models.post_api_auth_revoke_session_response_401 import PostApiAuthRevokeSessionResponse401
from ...models.post_api_auth_revoke_session_response_403 import PostApiAuthRevokeSessionResponse403
from ...models.post_api_auth_revoke_session_response_404 import PostApiAuthRevokeSessionResponse404
from ...models.post_api_auth_revoke_session_response_429 import PostApiAuthRevokeSessionResponse429
from ...models.post_api_auth_revoke_session_response_500 import PostApiAuthRevokeSessionResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApiAuthRevokeSessionBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/revoke-session",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostApiAuthRevokeSessionResponse400
    | PostApiAuthRevokeSessionResponse401
    | PostApiAuthRevokeSessionResponse403
    | PostApiAuthRevokeSessionResponse404
    | PostApiAuthRevokeSessionResponse429
    | PostApiAuthRevokeSessionResponse500
    | None
):
    if response.status_code == 400:
        response_400 = PostApiAuthRevokeSessionResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostApiAuthRevokeSessionResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostApiAuthRevokeSessionResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostApiAuthRevokeSessionResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = PostApiAuthRevokeSessionResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PostApiAuthRevokeSessionResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostApiAuthRevokeSessionResponse400
    | PostApiAuthRevokeSessionResponse401
    | PostApiAuthRevokeSessionResponse403
    | PostApiAuthRevokeSessionResponse404
    | PostApiAuthRevokeSessionResponse429
    | PostApiAuthRevokeSessionResponse500
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
    body: PostApiAuthRevokeSessionBody | Unset = UNSET,
) -> Response[
    PostApiAuthRevokeSessionResponse400
    | PostApiAuthRevokeSessionResponse401
    | PostApiAuthRevokeSessionResponse403
    | PostApiAuthRevokeSessionResponse404
    | PostApiAuthRevokeSessionResponse429
    | PostApiAuthRevokeSessionResponse500
]:
    """Revoke a single session

    Args:
        body (PostApiAuthRevokeSessionBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthRevokeSessionResponse400 | PostApiAuthRevokeSessionResponse401 | PostApiAuthRevokeSessionResponse403 | PostApiAuthRevokeSessionResponse404 | PostApiAuthRevokeSessionResponse429 | PostApiAuthRevokeSessionResponse500]
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
    body: PostApiAuthRevokeSessionBody | Unset = UNSET,
) -> (
    PostApiAuthRevokeSessionResponse400
    | PostApiAuthRevokeSessionResponse401
    | PostApiAuthRevokeSessionResponse403
    | PostApiAuthRevokeSessionResponse404
    | PostApiAuthRevokeSessionResponse429
    | PostApiAuthRevokeSessionResponse500
    | None
):
    """Revoke a single session

    Args:
        body (PostApiAuthRevokeSessionBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthRevokeSessionResponse400 | PostApiAuthRevokeSessionResponse401 | PostApiAuthRevokeSessionResponse403 | PostApiAuthRevokeSessionResponse404 | PostApiAuthRevokeSessionResponse429 | PostApiAuthRevokeSessionResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthRevokeSessionBody | Unset = UNSET,
) -> Response[
    PostApiAuthRevokeSessionResponse400
    | PostApiAuthRevokeSessionResponse401
    | PostApiAuthRevokeSessionResponse403
    | PostApiAuthRevokeSessionResponse404
    | PostApiAuthRevokeSessionResponse429
    | PostApiAuthRevokeSessionResponse500
]:
    """Revoke a single session

    Args:
        body (PostApiAuthRevokeSessionBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthRevokeSessionResponse400 | PostApiAuthRevokeSessionResponse401 | PostApiAuthRevokeSessionResponse403 | PostApiAuthRevokeSessionResponse404 | PostApiAuthRevokeSessionResponse429 | PostApiAuthRevokeSessionResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthRevokeSessionBody | Unset = UNSET,
) -> (
    PostApiAuthRevokeSessionResponse400
    | PostApiAuthRevokeSessionResponse401
    | PostApiAuthRevokeSessionResponse403
    | PostApiAuthRevokeSessionResponse404
    | PostApiAuthRevokeSessionResponse429
    | PostApiAuthRevokeSessionResponse500
    | None
):
    """Revoke a single session

    Args:
        body (PostApiAuthRevokeSessionBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthRevokeSessionResponse400 | PostApiAuthRevokeSessionResponse401 | PostApiAuthRevokeSessionResponse403 | PostApiAuthRevokeSessionResponse404 | PostApiAuthRevokeSessionResponse429 | PostApiAuthRevokeSessionResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
