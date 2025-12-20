from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_auth_admin_stop_impersonating_response_400 import PostApiAuthAdminStopImpersonatingResponse400
from ...models.post_api_auth_admin_stop_impersonating_response_401 import PostApiAuthAdminStopImpersonatingResponse401
from ...models.post_api_auth_admin_stop_impersonating_response_403 import PostApiAuthAdminStopImpersonatingResponse403
from ...models.post_api_auth_admin_stop_impersonating_response_404 import PostApiAuthAdminStopImpersonatingResponse404
from ...models.post_api_auth_admin_stop_impersonating_response_429 import PostApiAuthAdminStopImpersonatingResponse429
from ...models.post_api_auth_admin_stop_impersonating_response_500 import PostApiAuthAdminStopImpersonatingResponse500
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/admin/stop-impersonating",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostApiAuthAdminStopImpersonatingResponse400
    | PostApiAuthAdminStopImpersonatingResponse401
    | PostApiAuthAdminStopImpersonatingResponse403
    | PostApiAuthAdminStopImpersonatingResponse404
    | PostApiAuthAdminStopImpersonatingResponse429
    | PostApiAuthAdminStopImpersonatingResponse500
    | None
):
    if response.status_code == 400:
        response_400 = PostApiAuthAdminStopImpersonatingResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostApiAuthAdminStopImpersonatingResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostApiAuthAdminStopImpersonatingResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostApiAuthAdminStopImpersonatingResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = PostApiAuthAdminStopImpersonatingResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PostApiAuthAdminStopImpersonatingResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostApiAuthAdminStopImpersonatingResponse400
    | PostApiAuthAdminStopImpersonatingResponse401
    | PostApiAuthAdminStopImpersonatingResponse403
    | PostApiAuthAdminStopImpersonatingResponse404
    | PostApiAuthAdminStopImpersonatingResponse429
    | PostApiAuthAdminStopImpersonatingResponse500
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
) -> Response[
    PostApiAuthAdminStopImpersonatingResponse400
    | PostApiAuthAdminStopImpersonatingResponse401
    | PostApiAuthAdminStopImpersonatingResponse403
    | PostApiAuthAdminStopImpersonatingResponse404
    | PostApiAuthAdminStopImpersonatingResponse429
    | PostApiAuthAdminStopImpersonatingResponse500
]:
    """
    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthAdminStopImpersonatingResponse400 | PostApiAuthAdminStopImpersonatingResponse401 | PostApiAuthAdminStopImpersonatingResponse403 | PostApiAuthAdminStopImpersonatingResponse404 | PostApiAuthAdminStopImpersonatingResponse429 | PostApiAuthAdminStopImpersonatingResponse500]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> (
    PostApiAuthAdminStopImpersonatingResponse400
    | PostApiAuthAdminStopImpersonatingResponse401
    | PostApiAuthAdminStopImpersonatingResponse403
    | PostApiAuthAdminStopImpersonatingResponse404
    | PostApiAuthAdminStopImpersonatingResponse429
    | PostApiAuthAdminStopImpersonatingResponse500
    | None
):
    """
    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthAdminStopImpersonatingResponse400 | PostApiAuthAdminStopImpersonatingResponse401 | PostApiAuthAdminStopImpersonatingResponse403 | PostApiAuthAdminStopImpersonatingResponse404 | PostApiAuthAdminStopImpersonatingResponse429 | PostApiAuthAdminStopImpersonatingResponse500
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[
    PostApiAuthAdminStopImpersonatingResponse400
    | PostApiAuthAdminStopImpersonatingResponse401
    | PostApiAuthAdminStopImpersonatingResponse403
    | PostApiAuthAdminStopImpersonatingResponse404
    | PostApiAuthAdminStopImpersonatingResponse429
    | PostApiAuthAdminStopImpersonatingResponse500
]:
    """
    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthAdminStopImpersonatingResponse400 | PostApiAuthAdminStopImpersonatingResponse401 | PostApiAuthAdminStopImpersonatingResponse403 | PostApiAuthAdminStopImpersonatingResponse404 | PostApiAuthAdminStopImpersonatingResponse429 | PostApiAuthAdminStopImpersonatingResponse500]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> (
    PostApiAuthAdminStopImpersonatingResponse400
    | PostApiAuthAdminStopImpersonatingResponse401
    | PostApiAuthAdminStopImpersonatingResponse403
    | PostApiAuthAdminStopImpersonatingResponse404
    | PostApiAuthAdminStopImpersonatingResponse429
    | PostApiAuthAdminStopImpersonatingResponse500
    | None
):
    """
    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthAdminStopImpersonatingResponse400 | PostApiAuthAdminStopImpersonatingResponse401 | PostApiAuthAdminStopImpersonatingResponse403 | PostApiAuthAdminStopImpersonatingResponse404 | PostApiAuthAdminStopImpersonatingResponse429 | PostApiAuthAdminStopImpersonatingResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
