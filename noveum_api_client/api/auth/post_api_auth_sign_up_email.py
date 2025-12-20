from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_auth_sign_up_email_body import PostApiAuthSignUpEmailBody
from ...models.post_api_auth_sign_up_email_response_200 import PostApiAuthSignUpEmailResponse200
from ...models.post_api_auth_sign_up_email_response_400 import PostApiAuthSignUpEmailResponse400
from ...models.post_api_auth_sign_up_email_response_401 import PostApiAuthSignUpEmailResponse401
from ...models.post_api_auth_sign_up_email_response_403 import PostApiAuthSignUpEmailResponse403
from ...models.post_api_auth_sign_up_email_response_404 import PostApiAuthSignUpEmailResponse404
from ...models.post_api_auth_sign_up_email_response_429 import PostApiAuthSignUpEmailResponse429
from ...models.post_api_auth_sign_up_email_response_500 import PostApiAuthSignUpEmailResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApiAuthSignUpEmailBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/sign-up/email",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostApiAuthSignUpEmailResponse200
    | PostApiAuthSignUpEmailResponse400
    | PostApiAuthSignUpEmailResponse401
    | PostApiAuthSignUpEmailResponse403
    | PostApiAuthSignUpEmailResponse404
    | PostApiAuthSignUpEmailResponse429
    | PostApiAuthSignUpEmailResponse500
    | None
):
    if response.status_code == 200:
        response_200 = PostApiAuthSignUpEmailResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PostApiAuthSignUpEmailResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostApiAuthSignUpEmailResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostApiAuthSignUpEmailResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostApiAuthSignUpEmailResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = PostApiAuthSignUpEmailResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PostApiAuthSignUpEmailResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostApiAuthSignUpEmailResponse200
    | PostApiAuthSignUpEmailResponse400
    | PostApiAuthSignUpEmailResponse401
    | PostApiAuthSignUpEmailResponse403
    | PostApiAuthSignUpEmailResponse404
    | PostApiAuthSignUpEmailResponse429
    | PostApiAuthSignUpEmailResponse500
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
    body: PostApiAuthSignUpEmailBody | Unset = UNSET,
) -> Response[
    PostApiAuthSignUpEmailResponse200
    | PostApiAuthSignUpEmailResponse400
    | PostApiAuthSignUpEmailResponse401
    | PostApiAuthSignUpEmailResponse403
    | PostApiAuthSignUpEmailResponse404
    | PostApiAuthSignUpEmailResponse429
    | PostApiAuthSignUpEmailResponse500
]:
    """Sign up a user using email and password

    Args:
        body (PostApiAuthSignUpEmailBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthSignUpEmailResponse200 | PostApiAuthSignUpEmailResponse400 | PostApiAuthSignUpEmailResponse401 | PostApiAuthSignUpEmailResponse403 | PostApiAuthSignUpEmailResponse404 | PostApiAuthSignUpEmailResponse429 | PostApiAuthSignUpEmailResponse500]
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
    body: PostApiAuthSignUpEmailBody | Unset = UNSET,
) -> (
    PostApiAuthSignUpEmailResponse200
    | PostApiAuthSignUpEmailResponse400
    | PostApiAuthSignUpEmailResponse401
    | PostApiAuthSignUpEmailResponse403
    | PostApiAuthSignUpEmailResponse404
    | PostApiAuthSignUpEmailResponse429
    | PostApiAuthSignUpEmailResponse500
    | None
):
    """Sign up a user using email and password

    Args:
        body (PostApiAuthSignUpEmailBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthSignUpEmailResponse200 | PostApiAuthSignUpEmailResponse400 | PostApiAuthSignUpEmailResponse401 | PostApiAuthSignUpEmailResponse403 | PostApiAuthSignUpEmailResponse404 | PostApiAuthSignUpEmailResponse429 | PostApiAuthSignUpEmailResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthSignUpEmailBody | Unset = UNSET,
) -> Response[
    PostApiAuthSignUpEmailResponse200
    | PostApiAuthSignUpEmailResponse400
    | PostApiAuthSignUpEmailResponse401
    | PostApiAuthSignUpEmailResponse403
    | PostApiAuthSignUpEmailResponse404
    | PostApiAuthSignUpEmailResponse429
    | PostApiAuthSignUpEmailResponse500
]:
    """Sign up a user using email and password

    Args:
        body (PostApiAuthSignUpEmailBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthSignUpEmailResponse200 | PostApiAuthSignUpEmailResponse400 | PostApiAuthSignUpEmailResponse401 | PostApiAuthSignUpEmailResponse403 | PostApiAuthSignUpEmailResponse404 | PostApiAuthSignUpEmailResponse429 | PostApiAuthSignUpEmailResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthSignUpEmailBody | Unset = UNSET,
) -> (
    PostApiAuthSignUpEmailResponse200
    | PostApiAuthSignUpEmailResponse400
    | PostApiAuthSignUpEmailResponse401
    | PostApiAuthSignUpEmailResponse403
    | PostApiAuthSignUpEmailResponse404
    | PostApiAuthSignUpEmailResponse429
    | PostApiAuthSignUpEmailResponse500
    | None
):
    """Sign up a user using email and password

    Args:
        body (PostApiAuthSignUpEmailBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthSignUpEmailResponse200 | PostApiAuthSignUpEmailResponse400 | PostApiAuthSignUpEmailResponse401 | PostApiAuthSignUpEmailResponse403 | PostApiAuthSignUpEmailResponse404 | PostApiAuthSignUpEmailResponse429 | PostApiAuthSignUpEmailResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
