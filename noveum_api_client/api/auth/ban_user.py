from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ban_user_body import BanUserBody
from ...models.ban_user_response_200 import BanUserResponse200
from ...models.ban_user_response_400 import BanUserResponse400
from ...models.ban_user_response_401 import BanUserResponse401
from ...models.ban_user_response_403 import BanUserResponse403
from ...models.ban_user_response_404 import BanUserResponse404
from ...models.ban_user_response_429 import BanUserResponse429
from ...models.ban_user_response_500 import BanUserResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: BanUserBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/admin/ban-user",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    BanUserResponse200
    | BanUserResponse400
    | BanUserResponse401
    | BanUserResponse403
    | BanUserResponse404
    | BanUserResponse429
    | BanUserResponse500
    | None
):
    if response.status_code == 200:
        response_200 = BanUserResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = BanUserResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = BanUserResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = BanUserResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = BanUserResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = BanUserResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = BanUserResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    BanUserResponse200
    | BanUserResponse400
    | BanUserResponse401
    | BanUserResponse403
    | BanUserResponse404
    | BanUserResponse429
    | BanUserResponse500
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
    body: BanUserBody,
) -> Response[
    BanUserResponse200
    | BanUserResponse400
    | BanUserResponse401
    | BanUserResponse403
    | BanUserResponse404
    | BanUserResponse429
    | BanUserResponse500
]:
    """Ban a user

    Args:
        body (BanUserBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BanUserResponse200 | BanUserResponse400 | BanUserResponse401 | BanUserResponse403 | BanUserResponse404 | BanUserResponse429 | BanUserResponse500]
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
    body: BanUserBody,
) -> (
    BanUserResponse200
    | BanUserResponse400
    | BanUserResponse401
    | BanUserResponse403
    | BanUserResponse404
    | BanUserResponse429
    | BanUserResponse500
    | None
):
    """Ban a user

    Args:
        body (BanUserBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BanUserResponse200 | BanUserResponse400 | BanUserResponse401 | BanUserResponse403 | BanUserResponse404 | BanUserResponse429 | BanUserResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BanUserBody,
) -> Response[
    BanUserResponse200
    | BanUserResponse400
    | BanUserResponse401
    | BanUserResponse403
    | BanUserResponse404
    | BanUserResponse429
    | BanUserResponse500
]:
    """Ban a user

    Args:
        body (BanUserBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BanUserResponse200 | BanUserResponse400 | BanUserResponse401 | BanUserResponse403 | BanUserResponse404 | BanUserResponse429 | BanUserResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BanUserBody,
) -> (
    BanUserResponse200
    | BanUserResponse400
    | BanUserResponse401
    | BanUserResponse403
    | BanUserResponse404
    | BanUserResponse429
    | BanUserResponse500
    | None
):
    """Ban a user

    Args:
        body (BanUserBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BanUserResponse200 | BanUserResponse400 | BanUserResponse401 | BanUserResponse403 | BanUserResponse404 | BanUserResponse429 | BanUserResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
