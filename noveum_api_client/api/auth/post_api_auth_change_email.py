from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_auth_change_email_body import PostApiAuthChangeEmailBody
from ...models.post_api_auth_change_email_response_200 import PostApiAuthChangeEmailResponse200
from ...models.post_api_auth_change_email_response_400 import PostApiAuthChangeEmailResponse400
from ...models.post_api_auth_change_email_response_401 import PostApiAuthChangeEmailResponse401
from ...models.post_api_auth_change_email_response_403 import PostApiAuthChangeEmailResponse403
from ...models.post_api_auth_change_email_response_404 import PostApiAuthChangeEmailResponse404
from ...models.post_api_auth_change_email_response_429 import PostApiAuthChangeEmailResponse429
from ...models.post_api_auth_change_email_response_500 import PostApiAuthChangeEmailResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: PostApiAuthChangeEmailBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/change-email",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostApiAuthChangeEmailResponse200
    | PostApiAuthChangeEmailResponse400
    | PostApiAuthChangeEmailResponse401
    | PostApiAuthChangeEmailResponse403
    | PostApiAuthChangeEmailResponse404
    | PostApiAuthChangeEmailResponse429
    | PostApiAuthChangeEmailResponse500
    | None
):
    if response.status_code == 200:
        response_200 = PostApiAuthChangeEmailResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PostApiAuthChangeEmailResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostApiAuthChangeEmailResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostApiAuthChangeEmailResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostApiAuthChangeEmailResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = PostApiAuthChangeEmailResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PostApiAuthChangeEmailResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostApiAuthChangeEmailResponse200
    | PostApiAuthChangeEmailResponse400
    | PostApiAuthChangeEmailResponse401
    | PostApiAuthChangeEmailResponse403
    | PostApiAuthChangeEmailResponse404
    | PostApiAuthChangeEmailResponse429
    | PostApiAuthChangeEmailResponse500
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
    body: PostApiAuthChangeEmailBody,
) -> Response[
    PostApiAuthChangeEmailResponse200
    | PostApiAuthChangeEmailResponse400
    | PostApiAuthChangeEmailResponse401
    | PostApiAuthChangeEmailResponse403
    | PostApiAuthChangeEmailResponse404
    | PostApiAuthChangeEmailResponse429
    | PostApiAuthChangeEmailResponse500
]:
    """
    Args:
        body (PostApiAuthChangeEmailBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthChangeEmailResponse200 | PostApiAuthChangeEmailResponse400 | PostApiAuthChangeEmailResponse401 | PostApiAuthChangeEmailResponse403 | PostApiAuthChangeEmailResponse404 | PostApiAuthChangeEmailResponse429 | PostApiAuthChangeEmailResponse500]
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
    body: PostApiAuthChangeEmailBody,
) -> (
    PostApiAuthChangeEmailResponse200
    | PostApiAuthChangeEmailResponse400
    | PostApiAuthChangeEmailResponse401
    | PostApiAuthChangeEmailResponse403
    | PostApiAuthChangeEmailResponse404
    | PostApiAuthChangeEmailResponse429
    | PostApiAuthChangeEmailResponse500
    | None
):
    """
    Args:
        body (PostApiAuthChangeEmailBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthChangeEmailResponse200 | PostApiAuthChangeEmailResponse400 | PostApiAuthChangeEmailResponse401 | PostApiAuthChangeEmailResponse403 | PostApiAuthChangeEmailResponse404 | PostApiAuthChangeEmailResponse429 | PostApiAuthChangeEmailResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthChangeEmailBody,
) -> Response[
    PostApiAuthChangeEmailResponse200
    | PostApiAuthChangeEmailResponse400
    | PostApiAuthChangeEmailResponse401
    | PostApiAuthChangeEmailResponse403
    | PostApiAuthChangeEmailResponse404
    | PostApiAuthChangeEmailResponse429
    | PostApiAuthChangeEmailResponse500
]:
    """
    Args:
        body (PostApiAuthChangeEmailBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthChangeEmailResponse200 | PostApiAuthChangeEmailResponse400 | PostApiAuthChangeEmailResponse401 | PostApiAuthChangeEmailResponse403 | PostApiAuthChangeEmailResponse404 | PostApiAuthChangeEmailResponse429 | PostApiAuthChangeEmailResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthChangeEmailBody,
) -> (
    PostApiAuthChangeEmailResponse200
    | PostApiAuthChangeEmailResponse400
    | PostApiAuthChangeEmailResponse401
    | PostApiAuthChangeEmailResponse403
    | PostApiAuthChangeEmailResponse404
    | PostApiAuthChangeEmailResponse429
    | PostApiAuthChangeEmailResponse500
    | None
):
    """
    Args:
        body (PostApiAuthChangeEmailBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthChangeEmailResponse200 | PostApiAuthChangeEmailResponse400 | PostApiAuthChangeEmailResponse401 | PostApiAuthChangeEmailResponse403 | PostApiAuthChangeEmailResponse404 | PostApiAuthChangeEmailResponse429 | PostApiAuthChangeEmailResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
