from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_auth_passkey_delete_passkey_body import PostApiAuthPasskeyDeletePasskeyBody
from ...models.post_api_auth_passkey_delete_passkey_response_400 import PostApiAuthPasskeyDeletePasskeyResponse400
from ...models.post_api_auth_passkey_delete_passkey_response_401 import PostApiAuthPasskeyDeletePasskeyResponse401
from ...models.post_api_auth_passkey_delete_passkey_response_403 import PostApiAuthPasskeyDeletePasskeyResponse403
from ...models.post_api_auth_passkey_delete_passkey_response_404 import PostApiAuthPasskeyDeletePasskeyResponse404
from ...models.post_api_auth_passkey_delete_passkey_response_429 import PostApiAuthPasskeyDeletePasskeyResponse429
from ...models.post_api_auth_passkey_delete_passkey_response_500 import PostApiAuthPasskeyDeletePasskeyResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: PostApiAuthPasskeyDeletePasskeyBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/passkey/delete-passkey",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostApiAuthPasskeyDeletePasskeyResponse400
    | PostApiAuthPasskeyDeletePasskeyResponse401
    | PostApiAuthPasskeyDeletePasskeyResponse403
    | PostApiAuthPasskeyDeletePasskeyResponse404
    | PostApiAuthPasskeyDeletePasskeyResponse429
    | PostApiAuthPasskeyDeletePasskeyResponse500
    | None
):
    if response.status_code == 400:
        response_400 = PostApiAuthPasskeyDeletePasskeyResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostApiAuthPasskeyDeletePasskeyResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostApiAuthPasskeyDeletePasskeyResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostApiAuthPasskeyDeletePasskeyResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = PostApiAuthPasskeyDeletePasskeyResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PostApiAuthPasskeyDeletePasskeyResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostApiAuthPasskeyDeletePasskeyResponse400
    | PostApiAuthPasskeyDeletePasskeyResponse401
    | PostApiAuthPasskeyDeletePasskeyResponse403
    | PostApiAuthPasskeyDeletePasskeyResponse404
    | PostApiAuthPasskeyDeletePasskeyResponse429
    | PostApiAuthPasskeyDeletePasskeyResponse500
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
    body: PostApiAuthPasskeyDeletePasskeyBody,
) -> Response[
    PostApiAuthPasskeyDeletePasskeyResponse400
    | PostApiAuthPasskeyDeletePasskeyResponse401
    | PostApiAuthPasskeyDeletePasskeyResponse403
    | PostApiAuthPasskeyDeletePasskeyResponse404
    | PostApiAuthPasskeyDeletePasskeyResponse429
    | PostApiAuthPasskeyDeletePasskeyResponse500
]:
    """
    Args:
        body (PostApiAuthPasskeyDeletePasskeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthPasskeyDeletePasskeyResponse400 | PostApiAuthPasskeyDeletePasskeyResponse401 | PostApiAuthPasskeyDeletePasskeyResponse403 | PostApiAuthPasskeyDeletePasskeyResponse404 | PostApiAuthPasskeyDeletePasskeyResponse429 | PostApiAuthPasskeyDeletePasskeyResponse500]
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
    body: PostApiAuthPasskeyDeletePasskeyBody,
) -> (
    PostApiAuthPasskeyDeletePasskeyResponse400
    | PostApiAuthPasskeyDeletePasskeyResponse401
    | PostApiAuthPasskeyDeletePasskeyResponse403
    | PostApiAuthPasskeyDeletePasskeyResponse404
    | PostApiAuthPasskeyDeletePasskeyResponse429
    | PostApiAuthPasskeyDeletePasskeyResponse500
    | None
):
    """
    Args:
        body (PostApiAuthPasskeyDeletePasskeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthPasskeyDeletePasskeyResponse400 | PostApiAuthPasskeyDeletePasskeyResponse401 | PostApiAuthPasskeyDeletePasskeyResponse403 | PostApiAuthPasskeyDeletePasskeyResponse404 | PostApiAuthPasskeyDeletePasskeyResponse429 | PostApiAuthPasskeyDeletePasskeyResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthPasskeyDeletePasskeyBody,
) -> Response[
    PostApiAuthPasskeyDeletePasskeyResponse400
    | PostApiAuthPasskeyDeletePasskeyResponse401
    | PostApiAuthPasskeyDeletePasskeyResponse403
    | PostApiAuthPasskeyDeletePasskeyResponse404
    | PostApiAuthPasskeyDeletePasskeyResponse429
    | PostApiAuthPasskeyDeletePasskeyResponse500
]:
    """
    Args:
        body (PostApiAuthPasskeyDeletePasskeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthPasskeyDeletePasskeyResponse400 | PostApiAuthPasskeyDeletePasskeyResponse401 | PostApiAuthPasskeyDeletePasskeyResponse403 | PostApiAuthPasskeyDeletePasskeyResponse404 | PostApiAuthPasskeyDeletePasskeyResponse429 | PostApiAuthPasskeyDeletePasskeyResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthPasskeyDeletePasskeyBody,
) -> (
    PostApiAuthPasskeyDeletePasskeyResponse400
    | PostApiAuthPasskeyDeletePasskeyResponse401
    | PostApiAuthPasskeyDeletePasskeyResponse403
    | PostApiAuthPasskeyDeletePasskeyResponse404
    | PostApiAuthPasskeyDeletePasskeyResponse429
    | PostApiAuthPasskeyDeletePasskeyResponse500
    | None
):
    """
    Args:
        body (PostApiAuthPasskeyDeletePasskeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthPasskeyDeletePasskeyResponse400 | PostApiAuthPasskeyDeletePasskeyResponse401 | PostApiAuthPasskeyDeletePasskeyResponse403 | PostApiAuthPasskeyDeletePasskeyResponse404 | PostApiAuthPasskeyDeletePasskeyResponse429 | PostApiAuthPasskeyDeletePasskeyResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
