from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_auth_forget_password_email_otp_body import PostApiAuthForgetPasswordEmailOtpBody
from ...models.post_api_auth_forget_password_email_otp_response_200 import PostApiAuthForgetPasswordEmailOtpResponse200
from ...models.post_api_auth_forget_password_email_otp_response_400 import PostApiAuthForgetPasswordEmailOtpResponse400
from ...models.post_api_auth_forget_password_email_otp_response_401 import PostApiAuthForgetPasswordEmailOtpResponse401
from ...models.post_api_auth_forget_password_email_otp_response_403 import PostApiAuthForgetPasswordEmailOtpResponse403
from ...models.post_api_auth_forget_password_email_otp_response_404 import PostApiAuthForgetPasswordEmailOtpResponse404
from ...models.post_api_auth_forget_password_email_otp_response_429 import PostApiAuthForgetPasswordEmailOtpResponse429
from ...models.post_api_auth_forget_password_email_otp_response_500 import PostApiAuthForgetPasswordEmailOtpResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: PostApiAuthForgetPasswordEmailOtpBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/forget-password/email-otp",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostApiAuthForgetPasswordEmailOtpResponse200
    | PostApiAuthForgetPasswordEmailOtpResponse400
    | PostApiAuthForgetPasswordEmailOtpResponse401
    | PostApiAuthForgetPasswordEmailOtpResponse403
    | PostApiAuthForgetPasswordEmailOtpResponse404
    | PostApiAuthForgetPasswordEmailOtpResponse429
    | PostApiAuthForgetPasswordEmailOtpResponse500
    | None
):
    if response.status_code == 200:
        response_200 = PostApiAuthForgetPasswordEmailOtpResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PostApiAuthForgetPasswordEmailOtpResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostApiAuthForgetPasswordEmailOtpResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostApiAuthForgetPasswordEmailOtpResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostApiAuthForgetPasswordEmailOtpResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = PostApiAuthForgetPasswordEmailOtpResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PostApiAuthForgetPasswordEmailOtpResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostApiAuthForgetPasswordEmailOtpResponse200
    | PostApiAuthForgetPasswordEmailOtpResponse400
    | PostApiAuthForgetPasswordEmailOtpResponse401
    | PostApiAuthForgetPasswordEmailOtpResponse403
    | PostApiAuthForgetPasswordEmailOtpResponse404
    | PostApiAuthForgetPasswordEmailOtpResponse429
    | PostApiAuthForgetPasswordEmailOtpResponse500
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
    body: PostApiAuthForgetPasswordEmailOtpBody,
) -> Response[
    PostApiAuthForgetPasswordEmailOtpResponse200
    | PostApiAuthForgetPasswordEmailOtpResponse400
    | PostApiAuthForgetPasswordEmailOtpResponse401
    | PostApiAuthForgetPasswordEmailOtpResponse403
    | PostApiAuthForgetPasswordEmailOtpResponse404
    | PostApiAuthForgetPasswordEmailOtpResponse429
    | PostApiAuthForgetPasswordEmailOtpResponse500
]:
    """Forget password with email OTP

    Args:
        body (PostApiAuthForgetPasswordEmailOtpBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthForgetPasswordEmailOtpResponse200 | PostApiAuthForgetPasswordEmailOtpResponse400 | PostApiAuthForgetPasswordEmailOtpResponse401 | PostApiAuthForgetPasswordEmailOtpResponse403 | PostApiAuthForgetPasswordEmailOtpResponse404 | PostApiAuthForgetPasswordEmailOtpResponse429 | PostApiAuthForgetPasswordEmailOtpResponse500]
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
    body: PostApiAuthForgetPasswordEmailOtpBody,
) -> (
    PostApiAuthForgetPasswordEmailOtpResponse200
    | PostApiAuthForgetPasswordEmailOtpResponse400
    | PostApiAuthForgetPasswordEmailOtpResponse401
    | PostApiAuthForgetPasswordEmailOtpResponse403
    | PostApiAuthForgetPasswordEmailOtpResponse404
    | PostApiAuthForgetPasswordEmailOtpResponse429
    | PostApiAuthForgetPasswordEmailOtpResponse500
    | None
):
    """Forget password with email OTP

    Args:
        body (PostApiAuthForgetPasswordEmailOtpBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthForgetPasswordEmailOtpResponse200 | PostApiAuthForgetPasswordEmailOtpResponse400 | PostApiAuthForgetPasswordEmailOtpResponse401 | PostApiAuthForgetPasswordEmailOtpResponse403 | PostApiAuthForgetPasswordEmailOtpResponse404 | PostApiAuthForgetPasswordEmailOtpResponse429 | PostApiAuthForgetPasswordEmailOtpResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthForgetPasswordEmailOtpBody,
) -> Response[
    PostApiAuthForgetPasswordEmailOtpResponse200
    | PostApiAuthForgetPasswordEmailOtpResponse400
    | PostApiAuthForgetPasswordEmailOtpResponse401
    | PostApiAuthForgetPasswordEmailOtpResponse403
    | PostApiAuthForgetPasswordEmailOtpResponse404
    | PostApiAuthForgetPasswordEmailOtpResponse429
    | PostApiAuthForgetPasswordEmailOtpResponse500
]:
    """Forget password with email OTP

    Args:
        body (PostApiAuthForgetPasswordEmailOtpBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthForgetPasswordEmailOtpResponse200 | PostApiAuthForgetPasswordEmailOtpResponse400 | PostApiAuthForgetPasswordEmailOtpResponse401 | PostApiAuthForgetPasswordEmailOtpResponse403 | PostApiAuthForgetPasswordEmailOtpResponse404 | PostApiAuthForgetPasswordEmailOtpResponse429 | PostApiAuthForgetPasswordEmailOtpResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthForgetPasswordEmailOtpBody,
) -> (
    PostApiAuthForgetPasswordEmailOtpResponse200
    | PostApiAuthForgetPasswordEmailOtpResponse400
    | PostApiAuthForgetPasswordEmailOtpResponse401
    | PostApiAuthForgetPasswordEmailOtpResponse403
    | PostApiAuthForgetPasswordEmailOtpResponse404
    | PostApiAuthForgetPasswordEmailOtpResponse429
    | PostApiAuthForgetPasswordEmailOtpResponse500
    | None
):
    """Forget password with email OTP

    Args:
        body (PostApiAuthForgetPasswordEmailOtpBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthForgetPasswordEmailOtpResponse200 | PostApiAuthForgetPasswordEmailOtpResponse400 | PostApiAuthForgetPasswordEmailOtpResponse401 | PostApiAuthForgetPasswordEmailOtpResponse403 | PostApiAuthForgetPasswordEmailOtpResponse404 | PostApiAuthForgetPasswordEmailOtpResponse429 | PostApiAuthForgetPasswordEmailOtpResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
