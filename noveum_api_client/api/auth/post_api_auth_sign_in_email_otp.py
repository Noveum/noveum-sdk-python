from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_auth_sign_in_email_otp_body import PostApiAuthSignInEmailOtpBody
from ...models.post_api_auth_sign_in_email_otp_response_200 import PostApiAuthSignInEmailOtpResponse200
from ...models.post_api_auth_sign_in_email_otp_response_400 import PostApiAuthSignInEmailOtpResponse400
from ...models.post_api_auth_sign_in_email_otp_response_401 import PostApiAuthSignInEmailOtpResponse401
from ...models.post_api_auth_sign_in_email_otp_response_403 import PostApiAuthSignInEmailOtpResponse403
from ...models.post_api_auth_sign_in_email_otp_response_404 import PostApiAuthSignInEmailOtpResponse404
from ...models.post_api_auth_sign_in_email_otp_response_429 import PostApiAuthSignInEmailOtpResponse429
from ...models.post_api_auth_sign_in_email_otp_response_500 import PostApiAuthSignInEmailOtpResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: PostApiAuthSignInEmailOtpBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/sign-in/email-otp",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostApiAuthSignInEmailOtpResponse200
    | PostApiAuthSignInEmailOtpResponse400
    | PostApiAuthSignInEmailOtpResponse401
    | PostApiAuthSignInEmailOtpResponse403
    | PostApiAuthSignInEmailOtpResponse404
    | PostApiAuthSignInEmailOtpResponse429
    | PostApiAuthSignInEmailOtpResponse500
    | None
):
    if response.status_code == 200:
        response_200 = PostApiAuthSignInEmailOtpResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PostApiAuthSignInEmailOtpResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostApiAuthSignInEmailOtpResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostApiAuthSignInEmailOtpResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostApiAuthSignInEmailOtpResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = PostApiAuthSignInEmailOtpResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PostApiAuthSignInEmailOtpResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostApiAuthSignInEmailOtpResponse200
    | PostApiAuthSignInEmailOtpResponse400
    | PostApiAuthSignInEmailOtpResponse401
    | PostApiAuthSignInEmailOtpResponse403
    | PostApiAuthSignInEmailOtpResponse404
    | PostApiAuthSignInEmailOtpResponse429
    | PostApiAuthSignInEmailOtpResponse500
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
    body: PostApiAuthSignInEmailOtpBody,
) -> Response[
    PostApiAuthSignInEmailOtpResponse200
    | PostApiAuthSignInEmailOtpResponse400
    | PostApiAuthSignInEmailOtpResponse401
    | PostApiAuthSignInEmailOtpResponse403
    | PostApiAuthSignInEmailOtpResponse404
    | PostApiAuthSignInEmailOtpResponse429
    | PostApiAuthSignInEmailOtpResponse500
]:
    """Sign in with email OTP

    Args:
        body (PostApiAuthSignInEmailOtpBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthSignInEmailOtpResponse200 | PostApiAuthSignInEmailOtpResponse400 | PostApiAuthSignInEmailOtpResponse401 | PostApiAuthSignInEmailOtpResponse403 | PostApiAuthSignInEmailOtpResponse404 | PostApiAuthSignInEmailOtpResponse429 | PostApiAuthSignInEmailOtpResponse500]
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
    body: PostApiAuthSignInEmailOtpBody,
) -> (
    PostApiAuthSignInEmailOtpResponse200
    | PostApiAuthSignInEmailOtpResponse400
    | PostApiAuthSignInEmailOtpResponse401
    | PostApiAuthSignInEmailOtpResponse403
    | PostApiAuthSignInEmailOtpResponse404
    | PostApiAuthSignInEmailOtpResponse429
    | PostApiAuthSignInEmailOtpResponse500
    | None
):
    """Sign in with email OTP

    Args:
        body (PostApiAuthSignInEmailOtpBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthSignInEmailOtpResponse200 | PostApiAuthSignInEmailOtpResponse400 | PostApiAuthSignInEmailOtpResponse401 | PostApiAuthSignInEmailOtpResponse403 | PostApiAuthSignInEmailOtpResponse404 | PostApiAuthSignInEmailOtpResponse429 | PostApiAuthSignInEmailOtpResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthSignInEmailOtpBody,
) -> Response[
    PostApiAuthSignInEmailOtpResponse200
    | PostApiAuthSignInEmailOtpResponse400
    | PostApiAuthSignInEmailOtpResponse401
    | PostApiAuthSignInEmailOtpResponse403
    | PostApiAuthSignInEmailOtpResponse404
    | PostApiAuthSignInEmailOtpResponse429
    | PostApiAuthSignInEmailOtpResponse500
]:
    """Sign in with email OTP

    Args:
        body (PostApiAuthSignInEmailOtpBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthSignInEmailOtpResponse200 | PostApiAuthSignInEmailOtpResponse400 | PostApiAuthSignInEmailOtpResponse401 | PostApiAuthSignInEmailOtpResponse403 | PostApiAuthSignInEmailOtpResponse404 | PostApiAuthSignInEmailOtpResponse429 | PostApiAuthSignInEmailOtpResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthSignInEmailOtpBody,
) -> (
    PostApiAuthSignInEmailOtpResponse200
    | PostApiAuthSignInEmailOtpResponse400
    | PostApiAuthSignInEmailOtpResponse401
    | PostApiAuthSignInEmailOtpResponse403
    | PostApiAuthSignInEmailOtpResponse404
    | PostApiAuthSignInEmailOtpResponse429
    | PostApiAuthSignInEmailOtpResponse500
    | None
):
    """Sign in with email OTP

    Args:
        body (PostApiAuthSignInEmailOtpBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthSignInEmailOtpResponse200 | PostApiAuthSignInEmailOtpResponse400 | PostApiAuthSignInEmailOtpResponse401 | PostApiAuthSignInEmailOtpResponse403 | PostApiAuthSignInEmailOtpResponse404 | PostApiAuthSignInEmailOtpResponse429 | PostApiAuthSignInEmailOtpResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
