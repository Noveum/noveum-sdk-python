from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_auth_delete_user_callback_response_400 import GetApiAuthDeleteUserCallbackResponse400
from ...models.get_api_auth_delete_user_callback_response_401 import GetApiAuthDeleteUserCallbackResponse401
from ...models.get_api_auth_delete_user_callback_response_403 import GetApiAuthDeleteUserCallbackResponse403
from ...models.get_api_auth_delete_user_callback_response_404 import GetApiAuthDeleteUserCallbackResponse404
from ...models.get_api_auth_delete_user_callback_response_429 import GetApiAuthDeleteUserCallbackResponse429
from ...models.get_api_auth_delete_user_callback_response_500 import GetApiAuthDeleteUserCallbackResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    token: str | Unset = UNSET,
    callback_url: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["token"] = token

    params["callbackURL"] = callback_url

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/auth/delete-user/callback",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetApiAuthDeleteUserCallbackResponse400
    | GetApiAuthDeleteUserCallbackResponse401
    | GetApiAuthDeleteUserCallbackResponse403
    | GetApiAuthDeleteUserCallbackResponse404
    | GetApiAuthDeleteUserCallbackResponse429
    | GetApiAuthDeleteUserCallbackResponse500
    | None
):
    if response.status_code == 400:
        response_400 = GetApiAuthDeleteUserCallbackResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetApiAuthDeleteUserCallbackResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetApiAuthDeleteUserCallbackResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetApiAuthDeleteUserCallbackResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = GetApiAuthDeleteUserCallbackResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetApiAuthDeleteUserCallbackResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetApiAuthDeleteUserCallbackResponse400
    | GetApiAuthDeleteUserCallbackResponse401
    | GetApiAuthDeleteUserCallbackResponse403
    | GetApiAuthDeleteUserCallbackResponse404
    | GetApiAuthDeleteUserCallbackResponse429
    | GetApiAuthDeleteUserCallbackResponse500
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
    token: str | Unset = UNSET,
    callback_url: str | Unset = UNSET,
) -> Response[
    GetApiAuthDeleteUserCallbackResponse400
    | GetApiAuthDeleteUserCallbackResponse401
    | GetApiAuthDeleteUserCallbackResponse403
    | GetApiAuthDeleteUserCallbackResponse404
    | GetApiAuthDeleteUserCallbackResponse429
    | GetApiAuthDeleteUserCallbackResponse500
]:
    """
    Args:
        token (str | Unset):
        callback_url (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiAuthDeleteUserCallbackResponse400 | GetApiAuthDeleteUserCallbackResponse401 | GetApiAuthDeleteUserCallbackResponse403 | GetApiAuthDeleteUserCallbackResponse404 | GetApiAuthDeleteUserCallbackResponse429 | GetApiAuthDeleteUserCallbackResponse500]
    """

    kwargs = _get_kwargs(
        token=token,
        callback_url=callback_url,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    callback_url: str | Unset = UNSET,
) -> (
    GetApiAuthDeleteUserCallbackResponse400
    | GetApiAuthDeleteUserCallbackResponse401
    | GetApiAuthDeleteUserCallbackResponse403
    | GetApiAuthDeleteUserCallbackResponse404
    | GetApiAuthDeleteUserCallbackResponse429
    | GetApiAuthDeleteUserCallbackResponse500
    | None
):
    """
    Args:
        token (str | Unset):
        callback_url (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiAuthDeleteUserCallbackResponse400 | GetApiAuthDeleteUserCallbackResponse401 | GetApiAuthDeleteUserCallbackResponse403 | GetApiAuthDeleteUserCallbackResponse404 | GetApiAuthDeleteUserCallbackResponse429 | GetApiAuthDeleteUserCallbackResponse500
    """

    return sync_detailed(
        client=client,
        token=token,
        callback_url=callback_url,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    callback_url: str | Unset = UNSET,
) -> Response[
    GetApiAuthDeleteUserCallbackResponse400
    | GetApiAuthDeleteUserCallbackResponse401
    | GetApiAuthDeleteUserCallbackResponse403
    | GetApiAuthDeleteUserCallbackResponse404
    | GetApiAuthDeleteUserCallbackResponse429
    | GetApiAuthDeleteUserCallbackResponse500
]:
    """
    Args:
        token (str | Unset):
        callback_url (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiAuthDeleteUserCallbackResponse400 | GetApiAuthDeleteUserCallbackResponse401 | GetApiAuthDeleteUserCallbackResponse403 | GetApiAuthDeleteUserCallbackResponse404 | GetApiAuthDeleteUserCallbackResponse429 | GetApiAuthDeleteUserCallbackResponse500]
    """

    kwargs = _get_kwargs(
        token=token,
        callback_url=callback_url,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    token: str | Unset = UNSET,
    callback_url: str | Unset = UNSET,
) -> (
    GetApiAuthDeleteUserCallbackResponse400
    | GetApiAuthDeleteUserCallbackResponse401
    | GetApiAuthDeleteUserCallbackResponse403
    | GetApiAuthDeleteUserCallbackResponse404
    | GetApiAuthDeleteUserCallbackResponse429
    | GetApiAuthDeleteUserCallbackResponse500
    | None
):
    """
    Args:
        token (str | Unset):
        callback_url (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiAuthDeleteUserCallbackResponse400 | GetApiAuthDeleteUserCallbackResponse401 | GetApiAuthDeleteUserCallbackResponse403 | GetApiAuthDeleteUserCallbackResponse404 | GetApiAuthDeleteUserCallbackResponse429 | GetApiAuthDeleteUserCallbackResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            token=token,
            callback_url=callback_url,
        )
    ).parsed
