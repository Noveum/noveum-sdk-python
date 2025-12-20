from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.revoke_user_session_body import RevokeUserSessionBody
from ...models.revoke_user_session_response_200 import RevokeUserSessionResponse200
from ...models.revoke_user_session_response_400 import RevokeUserSessionResponse400
from ...models.revoke_user_session_response_401 import RevokeUserSessionResponse401
from ...models.revoke_user_session_response_403 import RevokeUserSessionResponse403
from ...models.revoke_user_session_response_404 import RevokeUserSessionResponse404
from ...models.revoke_user_session_response_429 import RevokeUserSessionResponse429
from ...models.revoke_user_session_response_500 import RevokeUserSessionResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: RevokeUserSessionBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/admin/revoke-user-session",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RevokeUserSessionResponse200
    | RevokeUserSessionResponse400
    | RevokeUserSessionResponse401
    | RevokeUserSessionResponse403
    | RevokeUserSessionResponse404
    | RevokeUserSessionResponse429
    | RevokeUserSessionResponse500
    | None
):
    if response.status_code == 200:
        response_200 = RevokeUserSessionResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RevokeUserSessionResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = RevokeUserSessionResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = RevokeUserSessionResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = RevokeUserSessionResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = RevokeUserSessionResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RevokeUserSessionResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RevokeUserSessionResponse200
    | RevokeUserSessionResponse400
    | RevokeUserSessionResponse401
    | RevokeUserSessionResponse403
    | RevokeUserSessionResponse404
    | RevokeUserSessionResponse429
    | RevokeUserSessionResponse500
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
    body: RevokeUserSessionBody,
) -> Response[
    RevokeUserSessionResponse200
    | RevokeUserSessionResponse400
    | RevokeUserSessionResponse401
    | RevokeUserSessionResponse403
    | RevokeUserSessionResponse404
    | RevokeUserSessionResponse429
    | RevokeUserSessionResponse500
]:
    """Revoke a user session

    Args:
        body (RevokeUserSessionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RevokeUserSessionResponse200 | RevokeUserSessionResponse400 | RevokeUserSessionResponse401 | RevokeUserSessionResponse403 | RevokeUserSessionResponse404 | RevokeUserSessionResponse429 | RevokeUserSessionResponse500]
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
    body: RevokeUserSessionBody,
) -> (
    RevokeUserSessionResponse200
    | RevokeUserSessionResponse400
    | RevokeUserSessionResponse401
    | RevokeUserSessionResponse403
    | RevokeUserSessionResponse404
    | RevokeUserSessionResponse429
    | RevokeUserSessionResponse500
    | None
):
    """Revoke a user session

    Args:
        body (RevokeUserSessionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RevokeUserSessionResponse200 | RevokeUserSessionResponse400 | RevokeUserSessionResponse401 | RevokeUserSessionResponse403 | RevokeUserSessionResponse404 | RevokeUserSessionResponse429 | RevokeUserSessionResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RevokeUserSessionBody,
) -> Response[
    RevokeUserSessionResponse200
    | RevokeUserSessionResponse400
    | RevokeUserSessionResponse401
    | RevokeUserSessionResponse403
    | RevokeUserSessionResponse404
    | RevokeUserSessionResponse429
    | RevokeUserSessionResponse500
]:
    """Revoke a user session

    Args:
        body (RevokeUserSessionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RevokeUserSessionResponse200 | RevokeUserSessionResponse400 | RevokeUserSessionResponse401 | RevokeUserSessionResponse403 | RevokeUserSessionResponse404 | RevokeUserSessionResponse429 | RevokeUserSessionResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RevokeUserSessionBody,
) -> (
    RevokeUserSessionResponse200
    | RevokeUserSessionResponse400
    | RevokeUserSessionResponse401
    | RevokeUserSessionResponse403
    | RevokeUserSessionResponse404
    | RevokeUserSessionResponse429
    | RevokeUserSessionResponse500
    | None
):
    """Revoke a user session

    Args:
        body (RevokeUserSessionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RevokeUserSessionResponse200 | RevokeUserSessionResponse400 | RevokeUserSessionResponse401 | RevokeUserSessionResponse403 | RevokeUserSessionResponse404 | RevokeUserSessionResponse429 | RevokeUserSessionResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
