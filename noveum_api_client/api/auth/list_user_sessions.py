from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_user_sessions_body import ListUserSessionsBody
from ...models.list_user_sessions_response_200 import ListUserSessionsResponse200
from ...models.list_user_sessions_response_400 import ListUserSessionsResponse400
from ...models.list_user_sessions_response_401 import ListUserSessionsResponse401
from ...models.list_user_sessions_response_403 import ListUserSessionsResponse403
from ...models.list_user_sessions_response_404 import ListUserSessionsResponse404
from ...models.list_user_sessions_response_429 import ListUserSessionsResponse429
from ...models.list_user_sessions_response_500 import ListUserSessionsResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: ListUserSessionsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/admin/list-user-sessions",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ListUserSessionsResponse200
    | ListUserSessionsResponse400
    | ListUserSessionsResponse401
    | ListUserSessionsResponse403
    | ListUserSessionsResponse404
    | ListUserSessionsResponse429
    | ListUserSessionsResponse500
    | None
):
    if response.status_code == 200:
        response_200 = ListUserSessionsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ListUserSessionsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ListUserSessionsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ListUserSessionsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ListUserSessionsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ListUserSessionsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ListUserSessionsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ListUserSessionsResponse200
    | ListUserSessionsResponse400
    | ListUserSessionsResponse401
    | ListUserSessionsResponse403
    | ListUserSessionsResponse404
    | ListUserSessionsResponse429
    | ListUserSessionsResponse500
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
    body: ListUserSessionsBody,
) -> Response[
    ListUserSessionsResponse200
    | ListUserSessionsResponse400
    | ListUserSessionsResponse401
    | ListUserSessionsResponse403
    | ListUserSessionsResponse404
    | ListUserSessionsResponse429
    | ListUserSessionsResponse500
]:
    """List user sessions

    Args:
        body (ListUserSessionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListUserSessionsResponse200 | ListUserSessionsResponse400 | ListUserSessionsResponse401 | ListUserSessionsResponse403 | ListUserSessionsResponse404 | ListUserSessionsResponse429 | ListUserSessionsResponse500]
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
    body: ListUserSessionsBody,
) -> (
    ListUserSessionsResponse200
    | ListUserSessionsResponse400
    | ListUserSessionsResponse401
    | ListUserSessionsResponse403
    | ListUserSessionsResponse404
    | ListUserSessionsResponse429
    | ListUserSessionsResponse500
    | None
):
    """List user sessions

    Args:
        body (ListUserSessionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListUserSessionsResponse200 | ListUserSessionsResponse400 | ListUserSessionsResponse401 | ListUserSessionsResponse403 | ListUserSessionsResponse404 | ListUserSessionsResponse429 | ListUserSessionsResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ListUserSessionsBody,
) -> Response[
    ListUserSessionsResponse200
    | ListUserSessionsResponse400
    | ListUserSessionsResponse401
    | ListUserSessionsResponse403
    | ListUserSessionsResponse404
    | ListUserSessionsResponse429
    | ListUserSessionsResponse500
]:
    """List user sessions

    Args:
        body (ListUserSessionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListUserSessionsResponse200 | ListUserSessionsResponse400 | ListUserSessionsResponse401 | ListUserSessionsResponse403 | ListUserSessionsResponse404 | ListUserSessionsResponse429 | ListUserSessionsResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ListUserSessionsBody,
) -> (
    ListUserSessionsResponse200
    | ListUserSessionsResponse400
    | ListUserSessionsResponse401
    | ListUserSessionsResponse403
    | ListUserSessionsResponse404
    | ListUserSessionsResponse429
    | ListUserSessionsResponse500
    | None
):
    """List user sessions

    Args:
        body (ListUserSessionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListUserSessionsResponse200 | ListUserSessionsResponse400 | ListUserSessionsResponse401 | ListUserSessionsResponse403 | ListUserSessionsResponse404 | ListUserSessionsResponse429 | ListUserSessionsResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
