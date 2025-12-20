from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_auth_sign_in_email_body import PostApiAuthSignInEmailBody
from ...models.post_api_auth_sign_in_email_response_200 import PostApiAuthSignInEmailResponse200
from ...models.post_api_auth_sign_in_email_response_400 import PostApiAuthSignInEmailResponse400
from ...models.post_api_auth_sign_in_email_response_401 import PostApiAuthSignInEmailResponse401
from ...models.post_api_auth_sign_in_email_response_403 import PostApiAuthSignInEmailResponse403
from ...models.post_api_auth_sign_in_email_response_404 import PostApiAuthSignInEmailResponse404
from ...models.post_api_auth_sign_in_email_response_429 import PostApiAuthSignInEmailResponse429
from ...models.post_api_auth_sign_in_email_response_500 import PostApiAuthSignInEmailResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: PostApiAuthSignInEmailBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/sign-in/email",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostApiAuthSignInEmailResponse200
    | PostApiAuthSignInEmailResponse400
    | PostApiAuthSignInEmailResponse401
    | PostApiAuthSignInEmailResponse403
    | PostApiAuthSignInEmailResponse404
    | PostApiAuthSignInEmailResponse429
    | PostApiAuthSignInEmailResponse500
    | None
):
    if response.status_code == 200:
        response_200 = PostApiAuthSignInEmailResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PostApiAuthSignInEmailResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostApiAuthSignInEmailResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostApiAuthSignInEmailResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostApiAuthSignInEmailResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = PostApiAuthSignInEmailResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PostApiAuthSignInEmailResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostApiAuthSignInEmailResponse200
    | PostApiAuthSignInEmailResponse400
    | PostApiAuthSignInEmailResponse401
    | PostApiAuthSignInEmailResponse403
    | PostApiAuthSignInEmailResponse404
    | PostApiAuthSignInEmailResponse429
    | PostApiAuthSignInEmailResponse500
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
    body: PostApiAuthSignInEmailBody,
) -> Response[
    PostApiAuthSignInEmailResponse200
    | PostApiAuthSignInEmailResponse400
    | PostApiAuthSignInEmailResponse401
    | PostApiAuthSignInEmailResponse403
    | PostApiAuthSignInEmailResponse404
    | PostApiAuthSignInEmailResponse429
    | PostApiAuthSignInEmailResponse500
]:
    """Sign in with email and password

    Args:
        body (PostApiAuthSignInEmailBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthSignInEmailResponse200 | PostApiAuthSignInEmailResponse400 | PostApiAuthSignInEmailResponse401 | PostApiAuthSignInEmailResponse403 | PostApiAuthSignInEmailResponse404 | PostApiAuthSignInEmailResponse429 | PostApiAuthSignInEmailResponse500]
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
    body: PostApiAuthSignInEmailBody,
) -> (
    PostApiAuthSignInEmailResponse200
    | PostApiAuthSignInEmailResponse400
    | PostApiAuthSignInEmailResponse401
    | PostApiAuthSignInEmailResponse403
    | PostApiAuthSignInEmailResponse404
    | PostApiAuthSignInEmailResponse429
    | PostApiAuthSignInEmailResponse500
    | None
):
    """Sign in with email and password

    Args:
        body (PostApiAuthSignInEmailBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthSignInEmailResponse200 | PostApiAuthSignInEmailResponse400 | PostApiAuthSignInEmailResponse401 | PostApiAuthSignInEmailResponse403 | PostApiAuthSignInEmailResponse404 | PostApiAuthSignInEmailResponse429 | PostApiAuthSignInEmailResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthSignInEmailBody,
) -> Response[
    PostApiAuthSignInEmailResponse200
    | PostApiAuthSignInEmailResponse400
    | PostApiAuthSignInEmailResponse401
    | PostApiAuthSignInEmailResponse403
    | PostApiAuthSignInEmailResponse404
    | PostApiAuthSignInEmailResponse429
    | PostApiAuthSignInEmailResponse500
]:
    """Sign in with email and password

    Args:
        body (PostApiAuthSignInEmailBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthSignInEmailResponse200 | PostApiAuthSignInEmailResponse400 | PostApiAuthSignInEmailResponse401 | PostApiAuthSignInEmailResponse403 | PostApiAuthSignInEmailResponse404 | PostApiAuthSignInEmailResponse429 | PostApiAuthSignInEmailResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthSignInEmailBody,
) -> (
    PostApiAuthSignInEmailResponse200
    | PostApiAuthSignInEmailResponse400
    | PostApiAuthSignInEmailResponse401
    | PostApiAuthSignInEmailResponse403
    | PostApiAuthSignInEmailResponse404
    | PostApiAuthSignInEmailResponse429
    | PostApiAuthSignInEmailResponse500
    | None
):
    """Sign in with email and password

    Args:
        body (PostApiAuthSignInEmailBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthSignInEmailResponse200 | PostApiAuthSignInEmailResponse400 | PostApiAuthSignInEmailResponse401 | PostApiAuthSignInEmailResponse403 | PostApiAuthSignInEmailResponse404 | PostApiAuthSignInEmailResponse429 | PostApiAuthSignInEmailResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
