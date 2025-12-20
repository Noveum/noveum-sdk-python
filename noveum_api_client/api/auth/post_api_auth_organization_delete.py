from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_auth_organization_delete_body import PostApiAuthOrganizationDeleteBody
from ...models.post_api_auth_organization_delete_response_400 import PostApiAuthOrganizationDeleteResponse400
from ...models.post_api_auth_organization_delete_response_401 import PostApiAuthOrganizationDeleteResponse401
from ...models.post_api_auth_organization_delete_response_403 import PostApiAuthOrganizationDeleteResponse403
from ...models.post_api_auth_organization_delete_response_404 import PostApiAuthOrganizationDeleteResponse404
from ...models.post_api_auth_organization_delete_response_429 import PostApiAuthOrganizationDeleteResponse429
from ...models.post_api_auth_organization_delete_response_500 import PostApiAuthOrganizationDeleteResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: PostApiAuthOrganizationDeleteBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/organization/delete",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostApiAuthOrganizationDeleteResponse400
    | PostApiAuthOrganizationDeleteResponse401
    | PostApiAuthOrganizationDeleteResponse403
    | PostApiAuthOrganizationDeleteResponse404
    | PostApiAuthOrganizationDeleteResponse429
    | PostApiAuthOrganizationDeleteResponse500
    | str
    | None
):
    if response.status_code == 200:
        response_200 = cast(str, response.json())
        return response_200

    if response.status_code == 400:
        response_400 = PostApiAuthOrganizationDeleteResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostApiAuthOrganizationDeleteResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostApiAuthOrganizationDeleteResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostApiAuthOrganizationDeleteResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = PostApiAuthOrganizationDeleteResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PostApiAuthOrganizationDeleteResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostApiAuthOrganizationDeleteResponse400
    | PostApiAuthOrganizationDeleteResponse401
    | PostApiAuthOrganizationDeleteResponse403
    | PostApiAuthOrganizationDeleteResponse404
    | PostApiAuthOrganizationDeleteResponse429
    | PostApiAuthOrganizationDeleteResponse500
    | str
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
    body: PostApiAuthOrganizationDeleteBody,
) -> Response[
    PostApiAuthOrganizationDeleteResponse400
    | PostApiAuthOrganizationDeleteResponse401
    | PostApiAuthOrganizationDeleteResponse403
    | PostApiAuthOrganizationDeleteResponse404
    | PostApiAuthOrganizationDeleteResponse429
    | PostApiAuthOrganizationDeleteResponse500
    | str
]:
    """Delete an organization

    Args:
        body (PostApiAuthOrganizationDeleteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthOrganizationDeleteResponse400 | PostApiAuthOrganizationDeleteResponse401 | PostApiAuthOrganizationDeleteResponse403 | PostApiAuthOrganizationDeleteResponse404 | PostApiAuthOrganizationDeleteResponse429 | PostApiAuthOrganizationDeleteResponse500 | str]
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
    body: PostApiAuthOrganizationDeleteBody,
) -> (
    PostApiAuthOrganizationDeleteResponse400
    | PostApiAuthOrganizationDeleteResponse401
    | PostApiAuthOrganizationDeleteResponse403
    | PostApiAuthOrganizationDeleteResponse404
    | PostApiAuthOrganizationDeleteResponse429
    | PostApiAuthOrganizationDeleteResponse500
    | str
    | None
):
    """Delete an organization

    Args:
        body (PostApiAuthOrganizationDeleteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthOrganizationDeleteResponse400 | PostApiAuthOrganizationDeleteResponse401 | PostApiAuthOrganizationDeleteResponse403 | PostApiAuthOrganizationDeleteResponse404 | PostApiAuthOrganizationDeleteResponse429 | PostApiAuthOrganizationDeleteResponse500 | str
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthOrganizationDeleteBody,
) -> Response[
    PostApiAuthOrganizationDeleteResponse400
    | PostApiAuthOrganizationDeleteResponse401
    | PostApiAuthOrganizationDeleteResponse403
    | PostApiAuthOrganizationDeleteResponse404
    | PostApiAuthOrganizationDeleteResponse429
    | PostApiAuthOrganizationDeleteResponse500
    | str
]:
    """Delete an organization

    Args:
        body (PostApiAuthOrganizationDeleteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthOrganizationDeleteResponse400 | PostApiAuthOrganizationDeleteResponse401 | PostApiAuthOrganizationDeleteResponse403 | PostApiAuthOrganizationDeleteResponse404 | PostApiAuthOrganizationDeleteResponse429 | PostApiAuthOrganizationDeleteResponse500 | str]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthOrganizationDeleteBody,
) -> (
    PostApiAuthOrganizationDeleteResponse400
    | PostApiAuthOrganizationDeleteResponse401
    | PostApiAuthOrganizationDeleteResponse403
    | PostApiAuthOrganizationDeleteResponse404
    | PostApiAuthOrganizationDeleteResponse429
    | PostApiAuthOrganizationDeleteResponse500
    | str
    | None
):
    """Delete an organization

    Args:
        body (PostApiAuthOrganizationDeleteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthOrganizationDeleteResponse400 | PostApiAuthOrganizationDeleteResponse401 | PostApiAuthOrganizationDeleteResponse403 | PostApiAuthOrganizationDeleteResponse404 | PostApiAuthOrganizationDeleteResponse429 | PostApiAuthOrganizationDeleteResponse500 | str
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
