from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_auth_email_otp_send_verification_otp_body import PostApiAuthEmailOtpSendVerificationOtpBody
from ...models.post_api_auth_email_otp_send_verification_otp_response_200 import (
    PostApiAuthEmailOtpSendVerificationOtpResponse200,
)
from ...models.post_api_auth_email_otp_send_verification_otp_response_400 import (
    PostApiAuthEmailOtpSendVerificationOtpResponse400,
)
from ...models.post_api_auth_email_otp_send_verification_otp_response_401 import (
    PostApiAuthEmailOtpSendVerificationOtpResponse401,
)
from ...models.post_api_auth_email_otp_send_verification_otp_response_403 import (
    PostApiAuthEmailOtpSendVerificationOtpResponse403,
)
from ...models.post_api_auth_email_otp_send_verification_otp_response_404 import (
    PostApiAuthEmailOtpSendVerificationOtpResponse404,
)
from ...models.post_api_auth_email_otp_send_verification_otp_response_429 import (
    PostApiAuthEmailOtpSendVerificationOtpResponse429,
)
from ...models.post_api_auth_email_otp_send_verification_otp_response_500 import (
    PostApiAuthEmailOtpSendVerificationOtpResponse500,
)
from ...types import Response


def _get_kwargs(
    *,
    body: PostApiAuthEmailOtpSendVerificationOtpBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/email-otp/send-verification-otp",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostApiAuthEmailOtpSendVerificationOtpResponse200
    | PostApiAuthEmailOtpSendVerificationOtpResponse400
    | PostApiAuthEmailOtpSendVerificationOtpResponse401
    | PostApiAuthEmailOtpSendVerificationOtpResponse403
    | PostApiAuthEmailOtpSendVerificationOtpResponse404
    | PostApiAuthEmailOtpSendVerificationOtpResponse429
    | PostApiAuthEmailOtpSendVerificationOtpResponse500
    | None
):
    if response.status_code == 200:
        response_200 = PostApiAuthEmailOtpSendVerificationOtpResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PostApiAuthEmailOtpSendVerificationOtpResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostApiAuthEmailOtpSendVerificationOtpResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostApiAuthEmailOtpSendVerificationOtpResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostApiAuthEmailOtpSendVerificationOtpResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = PostApiAuthEmailOtpSendVerificationOtpResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PostApiAuthEmailOtpSendVerificationOtpResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostApiAuthEmailOtpSendVerificationOtpResponse200
    | PostApiAuthEmailOtpSendVerificationOtpResponse400
    | PostApiAuthEmailOtpSendVerificationOtpResponse401
    | PostApiAuthEmailOtpSendVerificationOtpResponse403
    | PostApiAuthEmailOtpSendVerificationOtpResponse404
    | PostApiAuthEmailOtpSendVerificationOtpResponse429
    | PostApiAuthEmailOtpSendVerificationOtpResponse500
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
    body: PostApiAuthEmailOtpSendVerificationOtpBody,
) -> Response[
    PostApiAuthEmailOtpSendVerificationOtpResponse200
    | PostApiAuthEmailOtpSendVerificationOtpResponse400
    | PostApiAuthEmailOtpSendVerificationOtpResponse401
    | PostApiAuthEmailOtpSendVerificationOtpResponse403
    | PostApiAuthEmailOtpSendVerificationOtpResponse404
    | PostApiAuthEmailOtpSendVerificationOtpResponse429
    | PostApiAuthEmailOtpSendVerificationOtpResponse500
]:
    """Send verification OTP

    Args:
        body (PostApiAuthEmailOtpSendVerificationOtpBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthEmailOtpSendVerificationOtpResponse200 | PostApiAuthEmailOtpSendVerificationOtpResponse400 | PostApiAuthEmailOtpSendVerificationOtpResponse401 | PostApiAuthEmailOtpSendVerificationOtpResponse403 | PostApiAuthEmailOtpSendVerificationOtpResponse404 | PostApiAuthEmailOtpSendVerificationOtpResponse429 | PostApiAuthEmailOtpSendVerificationOtpResponse500]
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
    body: PostApiAuthEmailOtpSendVerificationOtpBody,
) -> (
    PostApiAuthEmailOtpSendVerificationOtpResponse200
    | PostApiAuthEmailOtpSendVerificationOtpResponse400
    | PostApiAuthEmailOtpSendVerificationOtpResponse401
    | PostApiAuthEmailOtpSendVerificationOtpResponse403
    | PostApiAuthEmailOtpSendVerificationOtpResponse404
    | PostApiAuthEmailOtpSendVerificationOtpResponse429
    | PostApiAuthEmailOtpSendVerificationOtpResponse500
    | None
):
    """Send verification OTP

    Args:
        body (PostApiAuthEmailOtpSendVerificationOtpBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthEmailOtpSendVerificationOtpResponse200 | PostApiAuthEmailOtpSendVerificationOtpResponse400 | PostApiAuthEmailOtpSendVerificationOtpResponse401 | PostApiAuthEmailOtpSendVerificationOtpResponse403 | PostApiAuthEmailOtpSendVerificationOtpResponse404 | PostApiAuthEmailOtpSendVerificationOtpResponse429 | PostApiAuthEmailOtpSendVerificationOtpResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthEmailOtpSendVerificationOtpBody,
) -> Response[
    PostApiAuthEmailOtpSendVerificationOtpResponse200
    | PostApiAuthEmailOtpSendVerificationOtpResponse400
    | PostApiAuthEmailOtpSendVerificationOtpResponse401
    | PostApiAuthEmailOtpSendVerificationOtpResponse403
    | PostApiAuthEmailOtpSendVerificationOtpResponse404
    | PostApiAuthEmailOtpSendVerificationOtpResponse429
    | PostApiAuthEmailOtpSendVerificationOtpResponse500
]:
    """Send verification OTP

    Args:
        body (PostApiAuthEmailOtpSendVerificationOtpBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthEmailOtpSendVerificationOtpResponse200 | PostApiAuthEmailOtpSendVerificationOtpResponse400 | PostApiAuthEmailOtpSendVerificationOtpResponse401 | PostApiAuthEmailOtpSendVerificationOtpResponse403 | PostApiAuthEmailOtpSendVerificationOtpResponse404 | PostApiAuthEmailOtpSendVerificationOtpResponse429 | PostApiAuthEmailOtpSendVerificationOtpResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthEmailOtpSendVerificationOtpBody,
) -> (
    PostApiAuthEmailOtpSendVerificationOtpResponse200
    | PostApiAuthEmailOtpSendVerificationOtpResponse400
    | PostApiAuthEmailOtpSendVerificationOtpResponse401
    | PostApiAuthEmailOtpSendVerificationOtpResponse403
    | PostApiAuthEmailOtpSendVerificationOtpResponse404
    | PostApiAuthEmailOtpSendVerificationOtpResponse429
    | PostApiAuthEmailOtpSendVerificationOtpResponse500
    | None
):
    """Send verification OTP

    Args:
        body (PostApiAuthEmailOtpSendVerificationOtpBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthEmailOtpSendVerificationOtpResponse200 | PostApiAuthEmailOtpSendVerificationOtpResponse400 | PostApiAuthEmailOtpSendVerificationOtpResponse401 | PostApiAuthEmailOtpSendVerificationOtpResponse403 | PostApiAuthEmailOtpSendVerificationOtpResponse404 | PostApiAuthEmailOtpSendVerificationOtpResponse429 | PostApiAuthEmailOtpSendVerificationOtpResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
