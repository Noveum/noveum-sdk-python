from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_auth_verify_email_response_200 import GetApiAuthVerifyEmailResponse200
from ...models.get_api_auth_verify_email_response_400 import GetApiAuthVerifyEmailResponse400
from ...models.get_api_auth_verify_email_response_401 import GetApiAuthVerifyEmailResponse401
from ...models.get_api_auth_verify_email_response_403 import GetApiAuthVerifyEmailResponse403
from ...models.get_api_auth_verify_email_response_404 import GetApiAuthVerifyEmailResponse404
from ...models.get_api_auth_verify_email_response_429 import GetApiAuthVerifyEmailResponse429
from ...models.get_api_auth_verify_email_response_500 import GetApiAuthVerifyEmailResponse500
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
        "url": "/api/auth/verify-email",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetApiAuthVerifyEmailResponse200
    | GetApiAuthVerifyEmailResponse400
    | GetApiAuthVerifyEmailResponse401
    | GetApiAuthVerifyEmailResponse403
    | GetApiAuthVerifyEmailResponse404
    | GetApiAuthVerifyEmailResponse429
    | GetApiAuthVerifyEmailResponse500
    | None
):
    if response.status_code == 200:
        response_200 = GetApiAuthVerifyEmailResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetApiAuthVerifyEmailResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetApiAuthVerifyEmailResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetApiAuthVerifyEmailResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetApiAuthVerifyEmailResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = GetApiAuthVerifyEmailResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetApiAuthVerifyEmailResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetApiAuthVerifyEmailResponse200
    | GetApiAuthVerifyEmailResponse400
    | GetApiAuthVerifyEmailResponse401
    | GetApiAuthVerifyEmailResponse403
    | GetApiAuthVerifyEmailResponse404
    | GetApiAuthVerifyEmailResponse429
    | GetApiAuthVerifyEmailResponse500
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
    GetApiAuthVerifyEmailResponse200
    | GetApiAuthVerifyEmailResponse400
    | GetApiAuthVerifyEmailResponse401
    | GetApiAuthVerifyEmailResponse403
    | GetApiAuthVerifyEmailResponse404
    | GetApiAuthVerifyEmailResponse429
    | GetApiAuthVerifyEmailResponse500
]:
    """Verify the email of the user

    Args:
        token (str | Unset): The token to verify the email
        callback_url (str | Unset): The URL to redirect to after email verification

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiAuthVerifyEmailResponse200 | GetApiAuthVerifyEmailResponse400 | GetApiAuthVerifyEmailResponse401 | GetApiAuthVerifyEmailResponse403 | GetApiAuthVerifyEmailResponse404 | GetApiAuthVerifyEmailResponse429 | GetApiAuthVerifyEmailResponse500]
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
    GetApiAuthVerifyEmailResponse200
    | GetApiAuthVerifyEmailResponse400
    | GetApiAuthVerifyEmailResponse401
    | GetApiAuthVerifyEmailResponse403
    | GetApiAuthVerifyEmailResponse404
    | GetApiAuthVerifyEmailResponse429
    | GetApiAuthVerifyEmailResponse500
    | None
):
    """Verify the email of the user

    Args:
        token (str | Unset): The token to verify the email
        callback_url (str | Unset): The URL to redirect to after email verification

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiAuthVerifyEmailResponse200 | GetApiAuthVerifyEmailResponse400 | GetApiAuthVerifyEmailResponse401 | GetApiAuthVerifyEmailResponse403 | GetApiAuthVerifyEmailResponse404 | GetApiAuthVerifyEmailResponse429 | GetApiAuthVerifyEmailResponse500
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
    GetApiAuthVerifyEmailResponse200
    | GetApiAuthVerifyEmailResponse400
    | GetApiAuthVerifyEmailResponse401
    | GetApiAuthVerifyEmailResponse403
    | GetApiAuthVerifyEmailResponse404
    | GetApiAuthVerifyEmailResponse429
    | GetApiAuthVerifyEmailResponse500
]:
    """Verify the email of the user

    Args:
        token (str | Unset): The token to verify the email
        callback_url (str | Unset): The URL to redirect to after email verification

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiAuthVerifyEmailResponse200 | GetApiAuthVerifyEmailResponse400 | GetApiAuthVerifyEmailResponse401 | GetApiAuthVerifyEmailResponse403 | GetApiAuthVerifyEmailResponse404 | GetApiAuthVerifyEmailResponse429 | GetApiAuthVerifyEmailResponse500]
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
    GetApiAuthVerifyEmailResponse200
    | GetApiAuthVerifyEmailResponse400
    | GetApiAuthVerifyEmailResponse401
    | GetApiAuthVerifyEmailResponse403
    | GetApiAuthVerifyEmailResponse404
    | GetApiAuthVerifyEmailResponse429
    | GetApiAuthVerifyEmailResponse500
    | None
):
    """Verify the email of the user

    Args:
        token (str | Unset): The token to verify the email
        callback_url (str | Unset): The URL to redirect to after email verification

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiAuthVerifyEmailResponse200 | GetApiAuthVerifyEmailResponse400 | GetApiAuthVerifyEmailResponse401 | GetApiAuthVerifyEmailResponse403 | GetApiAuthVerifyEmailResponse404 | GetApiAuthVerifyEmailResponse429 | GetApiAuthVerifyEmailResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            token=token,
            callback_url=callback_url,
        )
    ).parsed
