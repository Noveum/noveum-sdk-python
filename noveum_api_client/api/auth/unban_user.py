from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.unban_user_body import UnbanUserBody
from ...models.unban_user_response_200 import UnbanUserResponse200
from ...models.unban_user_response_400 import UnbanUserResponse400
from ...models.unban_user_response_401 import UnbanUserResponse401
from ...models.unban_user_response_403 import UnbanUserResponse403
from ...models.unban_user_response_404 import UnbanUserResponse404
from ...models.unban_user_response_429 import UnbanUserResponse429
from ...models.unban_user_response_500 import UnbanUserResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: UnbanUserBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/admin/unban-user",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    UnbanUserResponse200
    | UnbanUserResponse400
    | UnbanUserResponse401
    | UnbanUserResponse403
    | UnbanUserResponse404
    | UnbanUserResponse429
    | UnbanUserResponse500
    | None
):
    if response.status_code == 200:
        response_200 = UnbanUserResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UnbanUserResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UnbanUserResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = UnbanUserResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UnbanUserResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = UnbanUserResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = UnbanUserResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    UnbanUserResponse200
    | UnbanUserResponse400
    | UnbanUserResponse401
    | UnbanUserResponse403
    | UnbanUserResponse404
    | UnbanUserResponse429
    | UnbanUserResponse500
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
    body: UnbanUserBody,
) -> Response[
    UnbanUserResponse200
    | UnbanUserResponse400
    | UnbanUserResponse401
    | UnbanUserResponse403
    | UnbanUserResponse404
    | UnbanUserResponse429
    | UnbanUserResponse500
]:
    """Unban a user

    Args:
        body (UnbanUserBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UnbanUserResponse200 | UnbanUserResponse400 | UnbanUserResponse401 | UnbanUserResponse403 | UnbanUserResponse404 | UnbanUserResponse429 | UnbanUserResponse500]
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
    body: UnbanUserBody,
) -> (
    UnbanUserResponse200
    | UnbanUserResponse400
    | UnbanUserResponse401
    | UnbanUserResponse403
    | UnbanUserResponse404
    | UnbanUserResponse429
    | UnbanUserResponse500
    | None
):
    """Unban a user

    Args:
        body (UnbanUserBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UnbanUserResponse200 | UnbanUserResponse400 | UnbanUserResponse401 | UnbanUserResponse403 | UnbanUserResponse404 | UnbanUserResponse429 | UnbanUserResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UnbanUserBody,
) -> Response[
    UnbanUserResponse200
    | UnbanUserResponse400
    | UnbanUserResponse401
    | UnbanUserResponse403
    | UnbanUserResponse404
    | UnbanUserResponse429
    | UnbanUserResponse500
]:
    """Unban a user

    Args:
        body (UnbanUserBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UnbanUserResponse200 | UnbanUserResponse400 | UnbanUserResponse401 | UnbanUserResponse403 | UnbanUserResponse404 | UnbanUserResponse429 | UnbanUserResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UnbanUserBody,
) -> (
    UnbanUserResponse200
    | UnbanUserResponse400
    | UnbanUserResponse401
    | UnbanUserResponse403
    | UnbanUserResponse404
    | UnbanUserResponse429
    | UnbanUserResponse500
    | None
):
    """Unban a user

    Args:
        body (UnbanUserBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UnbanUserResponse200 | UnbanUserResponse400 | UnbanUserResponse401 | UnbanUserResponse403 | UnbanUserResponse404 | UnbanUserResponse429 | UnbanUserResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
