from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_user_body import CreateUserBody
from ...models.create_user_response_200 import CreateUserResponse200
from ...models.create_user_response_400 import CreateUserResponse400
from ...models.create_user_response_401 import CreateUserResponse401
from ...models.create_user_response_403 import CreateUserResponse403
from ...models.create_user_response_404 import CreateUserResponse404
from ...models.create_user_response_429 import CreateUserResponse429
from ...models.create_user_response_500 import CreateUserResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: CreateUserBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/admin/create-user",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreateUserResponse200
    | CreateUserResponse400
    | CreateUserResponse401
    | CreateUserResponse403
    | CreateUserResponse404
    | CreateUserResponse429
    | CreateUserResponse500
    | None
):
    if response.status_code == 200:
        response_200 = CreateUserResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CreateUserResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreateUserResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = CreateUserResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CreateUserResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = CreateUserResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = CreateUserResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateUserResponse200
    | CreateUserResponse400
    | CreateUserResponse401
    | CreateUserResponse403
    | CreateUserResponse404
    | CreateUserResponse429
    | CreateUserResponse500
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
    body: CreateUserBody,
) -> Response[
    CreateUserResponse200
    | CreateUserResponse400
    | CreateUserResponse401
    | CreateUserResponse403
    | CreateUserResponse404
    | CreateUserResponse429
    | CreateUserResponse500
]:
    """Create a new user

    Args:
        body (CreateUserBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateUserResponse200 | CreateUserResponse400 | CreateUserResponse401 | CreateUserResponse403 | CreateUserResponse404 | CreateUserResponse429 | CreateUserResponse500]
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
    body: CreateUserBody,
) -> (
    CreateUserResponse200
    | CreateUserResponse400
    | CreateUserResponse401
    | CreateUserResponse403
    | CreateUserResponse404
    | CreateUserResponse429
    | CreateUserResponse500
    | None
):
    """Create a new user

    Args:
        body (CreateUserBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateUserResponse200 | CreateUserResponse400 | CreateUserResponse401 | CreateUserResponse403 | CreateUserResponse404 | CreateUserResponse429 | CreateUserResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateUserBody,
) -> Response[
    CreateUserResponse200
    | CreateUserResponse400
    | CreateUserResponse401
    | CreateUserResponse403
    | CreateUserResponse404
    | CreateUserResponse429
    | CreateUserResponse500
]:
    """Create a new user

    Args:
        body (CreateUserBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateUserResponse200 | CreateUserResponse400 | CreateUserResponse401 | CreateUserResponse403 | CreateUserResponse404 | CreateUserResponse429 | CreateUserResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateUserBody,
) -> (
    CreateUserResponse200
    | CreateUserResponse400
    | CreateUserResponse401
    | CreateUserResponse403
    | CreateUserResponse404
    | CreateUserResponse429
    | CreateUserResponse500
    | None
):
    """Create a new user

    Args:
        body (CreateUserBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateUserResponse200 | CreateUserResponse400 | CreateUserResponse401 | CreateUserResponse403 | CreateUserResponse404 | CreateUserResponse429 | CreateUserResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
