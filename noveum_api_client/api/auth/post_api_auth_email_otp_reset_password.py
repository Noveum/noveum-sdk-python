from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_auth_email_otp_reset_password_body import PostApiAuthEmailOtpResetPasswordBody
from ...models.post_api_auth_email_otp_reset_password_response_200 import PostApiAuthEmailOtpResetPasswordResponse200
from ...models.post_api_auth_email_otp_reset_password_response_400 import PostApiAuthEmailOtpResetPasswordResponse400
from ...models.post_api_auth_email_otp_reset_password_response_401 import PostApiAuthEmailOtpResetPasswordResponse401
from ...models.post_api_auth_email_otp_reset_password_response_403 import PostApiAuthEmailOtpResetPasswordResponse403
from ...models.post_api_auth_email_otp_reset_password_response_404 import PostApiAuthEmailOtpResetPasswordResponse404
from ...models.post_api_auth_email_otp_reset_password_response_429 import PostApiAuthEmailOtpResetPasswordResponse429
from ...models.post_api_auth_email_otp_reset_password_response_500 import PostApiAuthEmailOtpResetPasswordResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: PostApiAuthEmailOtpResetPasswordBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/email-otp/reset-password",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostApiAuthEmailOtpResetPasswordResponse200
    | PostApiAuthEmailOtpResetPasswordResponse400
    | PostApiAuthEmailOtpResetPasswordResponse401
    | PostApiAuthEmailOtpResetPasswordResponse403
    | PostApiAuthEmailOtpResetPasswordResponse404
    | PostApiAuthEmailOtpResetPasswordResponse429
    | PostApiAuthEmailOtpResetPasswordResponse500
    | None
):
    if response.status_code == 200:
        response_200 = PostApiAuthEmailOtpResetPasswordResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PostApiAuthEmailOtpResetPasswordResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostApiAuthEmailOtpResetPasswordResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostApiAuthEmailOtpResetPasswordResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostApiAuthEmailOtpResetPasswordResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = PostApiAuthEmailOtpResetPasswordResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PostApiAuthEmailOtpResetPasswordResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostApiAuthEmailOtpResetPasswordResponse200
    | PostApiAuthEmailOtpResetPasswordResponse400
    | PostApiAuthEmailOtpResetPasswordResponse401
    | PostApiAuthEmailOtpResetPasswordResponse403
    | PostApiAuthEmailOtpResetPasswordResponse404
    | PostApiAuthEmailOtpResetPasswordResponse429
    | PostApiAuthEmailOtpResetPasswordResponse500
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
    body: PostApiAuthEmailOtpResetPasswordBody,
) -> Response[
    PostApiAuthEmailOtpResetPasswordResponse200
    | PostApiAuthEmailOtpResetPasswordResponse400
    | PostApiAuthEmailOtpResetPasswordResponse401
    | PostApiAuthEmailOtpResetPasswordResponse403
    | PostApiAuthEmailOtpResetPasswordResponse404
    | PostApiAuthEmailOtpResetPasswordResponse429
    | PostApiAuthEmailOtpResetPasswordResponse500
]:
    """Reset password with email OTP

    Args:
        body (PostApiAuthEmailOtpResetPasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthEmailOtpResetPasswordResponse200 | PostApiAuthEmailOtpResetPasswordResponse400 | PostApiAuthEmailOtpResetPasswordResponse401 | PostApiAuthEmailOtpResetPasswordResponse403 | PostApiAuthEmailOtpResetPasswordResponse404 | PostApiAuthEmailOtpResetPasswordResponse429 | PostApiAuthEmailOtpResetPasswordResponse500]
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
    body: PostApiAuthEmailOtpResetPasswordBody,
) -> (
    PostApiAuthEmailOtpResetPasswordResponse200
    | PostApiAuthEmailOtpResetPasswordResponse400
    | PostApiAuthEmailOtpResetPasswordResponse401
    | PostApiAuthEmailOtpResetPasswordResponse403
    | PostApiAuthEmailOtpResetPasswordResponse404
    | PostApiAuthEmailOtpResetPasswordResponse429
    | PostApiAuthEmailOtpResetPasswordResponse500
    | None
):
    """Reset password with email OTP

    Args:
        body (PostApiAuthEmailOtpResetPasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthEmailOtpResetPasswordResponse200 | PostApiAuthEmailOtpResetPasswordResponse400 | PostApiAuthEmailOtpResetPasswordResponse401 | PostApiAuthEmailOtpResetPasswordResponse403 | PostApiAuthEmailOtpResetPasswordResponse404 | PostApiAuthEmailOtpResetPasswordResponse429 | PostApiAuthEmailOtpResetPasswordResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthEmailOtpResetPasswordBody,
) -> Response[
    PostApiAuthEmailOtpResetPasswordResponse200
    | PostApiAuthEmailOtpResetPasswordResponse400
    | PostApiAuthEmailOtpResetPasswordResponse401
    | PostApiAuthEmailOtpResetPasswordResponse403
    | PostApiAuthEmailOtpResetPasswordResponse404
    | PostApiAuthEmailOtpResetPasswordResponse429
    | PostApiAuthEmailOtpResetPasswordResponse500
]:
    """Reset password with email OTP

    Args:
        body (PostApiAuthEmailOtpResetPasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthEmailOtpResetPasswordResponse200 | PostApiAuthEmailOtpResetPasswordResponse400 | PostApiAuthEmailOtpResetPasswordResponse401 | PostApiAuthEmailOtpResetPasswordResponse403 | PostApiAuthEmailOtpResetPasswordResponse404 | PostApiAuthEmailOtpResetPasswordResponse429 | PostApiAuthEmailOtpResetPasswordResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthEmailOtpResetPasswordBody,
) -> (
    PostApiAuthEmailOtpResetPasswordResponse200
    | PostApiAuthEmailOtpResetPasswordResponse400
    | PostApiAuthEmailOtpResetPasswordResponse401
    | PostApiAuthEmailOtpResetPasswordResponse403
    | PostApiAuthEmailOtpResetPasswordResponse404
    | PostApiAuthEmailOtpResetPasswordResponse429
    | PostApiAuthEmailOtpResetPasswordResponse500
    | None
):
    """Reset password with email OTP

    Args:
        body (PostApiAuthEmailOtpResetPasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthEmailOtpResetPasswordResponse200 | PostApiAuthEmailOtpResetPasswordResponse400 | PostApiAuthEmailOtpResetPasswordResponse401 | PostApiAuthEmailOtpResetPasswordResponse403 | PostApiAuthEmailOtpResetPasswordResponse404 | PostApiAuthEmailOtpResetPasswordResponse429 | PostApiAuthEmailOtpResetPasswordResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
