from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.revoke_user_sessions_body import RevokeUserSessionsBody
from ...models.revoke_user_sessions_response_200 import RevokeUserSessionsResponse200
from ...models.revoke_user_sessions_response_400 import RevokeUserSessionsResponse400
from ...models.revoke_user_sessions_response_401 import RevokeUserSessionsResponse401
from ...models.revoke_user_sessions_response_403 import RevokeUserSessionsResponse403
from ...models.revoke_user_sessions_response_404 import RevokeUserSessionsResponse404
from ...models.revoke_user_sessions_response_429 import RevokeUserSessionsResponse429
from ...models.revoke_user_sessions_response_500 import RevokeUserSessionsResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: RevokeUserSessionsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/admin/revoke-user-sessions",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RevokeUserSessionsResponse200
    | RevokeUserSessionsResponse400
    | RevokeUserSessionsResponse401
    | RevokeUserSessionsResponse403
    | RevokeUserSessionsResponse404
    | RevokeUserSessionsResponse429
    | RevokeUserSessionsResponse500
    | None
):
    if response.status_code == 200:
        response_200 = RevokeUserSessionsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RevokeUserSessionsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = RevokeUserSessionsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = RevokeUserSessionsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = RevokeUserSessionsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = RevokeUserSessionsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RevokeUserSessionsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RevokeUserSessionsResponse200
    | RevokeUserSessionsResponse400
    | RevokeUserSessionsResponse401
    | RevokeUserSessionsResponse403
    | RevokeUserSessionsResponse404
    | RevokeUserSessionsResponse429
    | RevokeUserSessionsResponse500
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
    body: RevokeUserSessionsBody,
) -> Response[
    RevokeUserSessionsResponse200
    | RevokeUserSessionsResponse400
    | RevokeUserSessionsResponse401
    | RevokeUserSessionsResponse403
    | RevokeUserSessionsResponse404
    | RevokeUserSessionsResponse429
    | RevokeUserSessionsResponse500
]:
    """Revoke all user sessions

    Args:
        body (RevokeUserSessionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RevokeUserSessionsResponse200 | RevokeUserSessionsResponse400 | RevokeUserSessionsResponse401 | RevokeUserSessionsResponse403 | RevokeUserSessionsResponse404 | RevokeUserSessionsResponse429 | RevokeUserSessionsResponse500]
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
    body: RevokeUserSessionsBody,
) -> (
    RevokeUserSessionsResponse200
    | RevokeUserSessionsResponse400
    | RevokeUserSessionsResponse401
    | RevokeUserSessionsResponse403
    | RevokeUserSessionsResponse404
    | RevokeUserSessionsResponse429
    | RevokeUserSessionsResponse500
    | None
):
    """Revoke all user sessions

    Args:
        body (RevokeUserSessionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RevokeUserSessionsResponse200 | RevokeUserSessionsResponse400 | RevokeUserSessionsResponse401 | RevokeUserSessionsResponse403 | RevokeUserSessionsResponse404 | RevokeUserSessionsResponse429 | RevokeUserSessionsResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RevokeUserSessionsBody,
) -> Response[
    RevokeUserSessionsResponse200
    | RevokeUserSessionsResponse400
    | RevokeUserSessionsResponse401
    | RevokeUserSessionsResponse403
    | RevokeUserSessionsResponse404
    | RevokeUserSessionsResponse429
    | RevokeUserSessionsResponse500
]:
    """Revoke all user sessions

    Args:
        body (RevokeUserSessionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RevokeUserSessionsResponse200 | RevokeUserSessionsResponse400 | RevokeUserSessionsResponse401 | RevokeUserSessionsResponse403 | RevokeUserSessionsResponse404 | RevokeUserSessionsResponse429 | RevokeUserSessionsResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RevokeUserSessionsBody,
) -> (
    RevokeUserSessionsResponse200
    | RevokeUserSessionsResponse400
    | RevokeUserSessionsResponse401
    | RevokeUserSessionsResponse403
    | RevokeUserSessionsResponse404
    | RevokeUserSessionsResponse429
    | RevokeUserSessionsResponse500
    | None
):
    """Revoke all user sessions

    Args:
        body (RevokeUserSessionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RevokeUserSessionsResponse200 | RevokeUserSessionsResponse400 | RevokeUserSessionsResponse401 | RevokeUserSessionsResponse403 | RevokeUserSessionsResponse404 | RevokeUserSessionsResponse429 | RevokeUserSessionsResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
