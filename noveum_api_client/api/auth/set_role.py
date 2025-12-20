from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.set_role_body import SetRoleBody
from ...models.set_role_response_200 import SetRoleResponse200
from ...models.set_role_response_400 import SetRoleResponse400
from ...models.set_role_response_401 import SetRoleResponse401
from ...models.set_role_response_403 import SetRoleResponse403
from ...models.set_role_response_404 import SetRoleResponse404
from ...models.set_role_response_429 import SetRoleResponse429
from ...models.set_role_response_500 import SetRoleResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: SetRoleBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/admin/set-role",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    SetRoleResponse200
    | SetRoleResponse400
    | SetRoleResponse401
    | SetRoleResponse403
    | SetRoleResponse404
    | SetRoleResponse429
    | SetRoleResponse500
    | None
):
    if response.status_code == 200:
        response_200 = SetRoleResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = SetRoleResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SetRoleResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = SetRoleResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = SetRoleResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = SetRoleResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = SetRoleResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    SetRoleResponse200
    | SetRoleResponse400
    | SetRoleResponse401
    | SetRoleResponse403
    | SetRoleResponse404
    | SetRoleResponse429
    | SetRoleResponse500
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
    body: SetRoleBody,
) -> Response[
    SetRoleResponse200
    | SetRoleResponse400
    | SetRoleResponse401
    | SetRoleResponse403
    | SetRoleResponse404
    | SetRoleResponse429
    | SetRoleResponse500
]:
    """Set the role of a user

    Args:
        body (SetRoleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SetRoleResponse200 | SetRoleResponse400 | SetRoleResponse401 | SetRoleResponse403 | SetRoleResponse404 | SetRoleResponse429 | SetRoleResponse500]
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
    body: SetRoleBody,
) -> (
    SetRoleResponse200
    | SetRoleResponse400
    | SetRoleResponse401
    | SetRoleResponse403
    | SetRoleResponse404
    | SetRoleResponse429
    | SetRoleResponse500
    | None
):
    """Set the role of a user

    Args:
        body (SetRoleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SetRoleResponse200 | SetRoleResponse400 | SetRoleResponse401 | SetRoleResponse403 | SetRoleResponse404 | SetRoleResponse429 | SetRoleResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SetRoleBody,
) -> Response[
    SetRoleResponse200
    | SetRoleResponse400
    | SetRoleResponse401
    | SetRoleResponse403
    | SetRoleResponse404
    | SetRoleResponse429
    | SetRoleResponse500
]:
    """Set the role of a user

    Args:
        body (SetRoleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SetRoleResponse200 | SetRoleResponse400 | SetRoleResponse401 | SetRoleResponse403 | SetRoleResponse404 | SetRoleResponse429 | SetRoleResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SetRoleBody,
) -> (
    SetRoleResponse200
    | SetRoleResponse400
    | SetRoleResponse401
    | SetRoleResponse403
    | SetRoleResponse404
    | SetRoleResponse429
    | SetRoleResponse500
    | None
):
    """Set the role of a user

    Args:
        body (SetRoleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SetRoleResponse200 | SetRoleResponse400 | SetRoleResponse401 | SetRoleResponse403 | SetRoleResponse404 | SetRoleResponse429 | SetRoleResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
