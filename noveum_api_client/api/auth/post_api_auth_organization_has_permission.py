from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_auth_organization_has_permission_body import PostApiAuthOrganizationHasPermissionBody
from ...models.post_api_auth_organization_has_permission_response_200 import (
    PostApiAuthOrganizationHasPermissionResponse200,
)
from ...models.post_api_auth_organization_has_permission_response_400 import (
    PostApiAuthOrganizationHasPermissionResponse400,
)
from ...models.post_api_auth_organization_has_permission_response_401 import (
    PostApiAuthOrganizationHasPermissionResponse401,
)
from ...models.post_api_auth_organization_has_permission_response_403 import (
    PostApiAuthOrganizationHasPermissionResponse403,
)
from ...models.post_api_auth_organization_has_permission_response_404 import (
    PostApiAuthOrganizationHasPermissionResponse404,
)
from ...models.post_api_auth_organization_has_permission_response_429 import (
    PostApiAuthOrganizationHasPermissionResponse429,
)
from ...models.post_api_auth_organization_has_permission_response_500 import (
    PostApiAuthOrganizationHasPermissionResponse500,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApiAuthOrganizationHasPermissionBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/organization/has-permission",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostApiAuthOrganizationHasPermissionResponse200
    | PostApiAuthOrganizationHasPermissionResponse400
    | PostApiAuthOrganizationHasPermissionResponse401
    | PostApiAuthOrganizationHasPermissionResponse403
    | PostApiAuthOrganizationHasPermissionResponse404
    | PostApiAuthOrganizationHasPermissionResponse429
    | PostApiAuthOrganizationHasPermissionResponse500
    | None
):
    if response.status_code == 200:
        response_200 = PostApiAuthOrganizationHasPermissionResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PostApiAuthOrganizationHasPermissionResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostApiAuthOrganizationHasPermissionResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostApiAuthOrganizationHasPermissionResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostApiAuthOrganizationHasPermissionResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = PostApiAuthOrganizationHasPermissionResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PostApiAuthOrganizationHasPermissionResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostApiAuthOrganizationHasPermissionResponse200
    | PostApiAuthOrganizationHasPermissionResponse400
    | PostApiAuthOrganizationHasPermissionResponse401
    | PostApiAuthOrganizationHasPermissionResponse403
    | PostApiAuthOrganizationHasPermissionResponse404
    | PostApiAuthOrganizationHasPermissionResponse429
    | PostApiAuthOrganizationHasPermissionResponse500
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
    body: PostApiAuthOrganizationHasPermissionBody | Unset = UNSET,
) -> Response[
    PostApiAuthOrganizationHasPermissionResponse200
    | PostApiAuthOrganizationHasPermissionResponse400
    | PostApiAuthOrganizationHasPermissionResponse401
    | PostApiAuthOrganizationHasPermissionResponse403
    | PostApiAuthOrganizationHasPermissionResponse404
    | PostApiAuthOrganizationHasPermissionResponse429
    | PostApiAuthOrganizationHasPermissionResponse500
]:
    """Check if the user has permission

    Args:
        body (PostApiAuthOrganizationHasPermissionBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthOrganizationHasPermissionResponse200 | PostApiAuthOrganizationHasPermissionResponse400 | PostApiAuthOrganizationHasPermissionResponse401 | PostApiAuthOrganizationHasPermissionResponse403 | PostApiAuthOrganizationHasPermissionResponse404 | PostApiAuthOrganizationHasPermissionResponse429 | PostApiAuthOrganizationHasPermissionResponse500]
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
    body: PostApiAuthOrganizationHasPermissionBody | Unset = UNSET,
) -> (
    PostApiAuthOrganizationHasPermissionResponse200
    | PostApiAuthOrganizationHasPermissionResponse400
    | PostApiAuthOrganizationHasPermissionResponse401
    | PostApiAuthOrganizationHasPermissionResponse403
    | PostApiAuthOrganizationHasPermissionResponse404
    | PostApiAuthOrganizationHasPermissionResponse429
    | PostApiAuthOrganizationHasPermissionResponse500
    | None
):
    """Check if the user has permission

    Args:
        body (PostApiAuthOrganizationHasPermissionBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthOrganizationHasPermissionResponse200 | PostApiAuthOrganizationHasPermissionResponse400 | PostApiAuthOrganizationHasPermissionResponse401 | PostApiAuthOrganizationHasPermissionResponse403 | PostApiAuthOrganizationHasPermissionResponse404 | PostApiAuthOrganizationHasPermissionResponse429 | PostApiAuthOrganizationHasPermissionResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthOrganizationHasPermissionBody | Unset = UNSET,
) -> Response[
    PostApiAuthOrganizationHasPermissionResponse200
    | PostApiAuthOrganizationHasPermissionResponse400
    | PostApiAuthOrganizationHasPermissionResponse401
    | PostApiAuthOrganizationHasPermissionResponse403
    | PostApiAuthOrganizationHasPermissionResponse404
    | PostApiAuthOrganizationHasPermissionResponse429
    | PostApiAuthOrganizationHasPermissionResponse500
]:
    """Check if the user has permission

    Args:
        body (PostApiAuthOrganizationHasPermissionBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAuthOrganizationHasPermissionResponse200 | PostApiAuthOrganizationHasPermissionResponse400 | PostApiAuthOrganizationHasPermissionResponse401 | PostApiAuthOrganizationHasPermissionResponse403 | PostApiAuthOrganizationHasPermissionResponse404 | PostApiAuthOrganizationHasPermissionResponse429 | PostApiAuthOrganizationHasPermissionResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApiAuthOrganizationHasPermissionBody | Unset = UNSET,
) -> (
    PostApiAuthOrganizationHasPermissionResponse200
    | PostApiAuthOrganizationHasPermissionResponse400
    | PostApiAuthOrganizationHasPermissionResponse401
    | PostApiAuthOrganizationHasPermissionResponse403
    | PostApiAuthOrganizationHasPermissionResponse404
    | PostApiAuthOrganizationHasPermissionResponse429
    | PostApiAuthOrganizationHasPermissionResponse500
    | None
):
    """Check if the user has permission

    Args:
        body (PostApiAuthOrganizationHasPermissionBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAuthOrganizationHasPermissionResponse200 | PostApiAuthOrganizationHasPermissionResponse400 | PostApiAuthOrganizationHasPermissionResponse401 | PostApiAuthOrganizationHasPermissionResponse403 | PostApiAuthOrganizationHasPermissionResponse404 | PostApiAuthOrganizationHasPermissionResponse429 | PostApiAuthOrganizationHasPermissionResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
