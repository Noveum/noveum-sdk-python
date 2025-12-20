from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_users_response_200 import ListUsersResponse200
from ...models.list_users_response_400 import ListUsersResponse400
from ...models.list_users_response_401 import ListUsersResponse401
from ...models.list_users_response_403 import ListUsersResponse403
from ...models.list_users_response_404 import ListUsersResponse404
from ...models.list_users_response_429 import ListUsersResponse429
from ...models.list_users_response_500 import ListUsersResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    search_value: str | Unset = UNSET,
    search_field: str | Unset = UNSET,
    search_operator: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    offset: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_direction: str | Unset = UNSET,
    filter_field: str | Unset = UNSET,
    filter_value: str | Unset = UNSET,
    filter_operator: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["searchValue"] = search_value

    params["searchField"] = search_field

    params["searchOperator"] = search_operator

    params["limit"] = limit

    params["offset"] = offset

    params["sortBy"] = sort_by

    params["sortDirection"] = sort_direction

    params["filterField"] = filter_field

    params["filterValue"] = filter_value

    params["filterOperator"] = filter_operator

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/auth/admin/list-users",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ListUsersResponse200
    | ListUsersResponse400
    | ListUsersResponse401
    | ListUsersResponse403
    | ListUsersResponse404
    | ListUsersResponse429
    | ListUsersResponse500
    | None
):
    if response.status_code == 200:
        response_200 = ListUsersResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ListUsersResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ListUsersResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ListUsersResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ListUsersResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ListUsersResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ListUsersResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ListUsersResponse200
    | ListUsersResponse400
    | ListUsersResponse401
    | ListUsersResponse403
    | ListUsersResponse404
    | ListUsersResponse429
    | ListUsersResponse500
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
    search_value: str | Unset = UNSET,
    search_field: str | Unset = UNSET,
    search_operator: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    offset: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_direction: str | Unset = UNSET,
    filter_field: str | Unset = UNSET,
    filter_value: str | Unset = UNSET,
    filter_operator: str | Unset = UNSET,
) -> Response[
    ListUsersResponse200
    | ListUsersResponse400
    | ListUsersResponse401
    | ListUsersResponse403
    | ListUsersResponse404
    | ListUsersResponse429
    | ListUsersResponse500
]:
    """List users

    Args:
        search_value (str | Unset): The value to search for
        search_field (str | Unset): The field to search in, defaults to email. Can be `email` or
            `name`
        search_operator (str | Unset): The operator to use for the search. Can be `contains`,
            `starts_with` or `ends_with`
        limit (str | Unset): The number of users to return
        offset (str | Unset): The offset to start from
        sort_by (str | Unset): The field to sort by
        sort_direction (str | Unset): The direction to sort by
        filter_field (str | Unset): The field to filter by
        filter_value (str | Unset): The value to filter by
        filter_operator (str | Unset): The operator to use for the filter

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListUsersResponse200 | ListUsersResponse400 | ListUsersResponse401 | ListUsersResponse403 | ListUsersResponse404 | ListUsersResponse429 | ListUsersResponse500]
    """

    kwargs = _get_kwargs(
        search_value=search_value,
        search_field=search_field,
        search_operator=search_operator,
        limit=limit,
        offset=offset,
        sort_by=sort_by,
        sort_direction=sort_direction,
        filter_field=filter_field,
        filter_value=filter_value,
        filter_operator=filter_operator,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    search_value: str | Unset = UNSET,
    search_field: str | Unset = UNSET,
    search_operator: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    offset: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_direction: str | Unset = UNSET,
    filter_field: str | Unset = UNSET,
    filter_value: str | Unset = UNSET,
    filter_operator: str | Unset = UNSET,
) -> (
    ListUsersResponse200
    | ListUsersResponse400
    | ListUsersResponse401
    | ListUsersResponse403
    | ListUsersResponse404
    | ListUsersResponse429
    | ListUsersResponse500
    | None
):
    """List users

    Args:
        search_value (str | Unset): The value to search for
        search_field (str | Unset): The field to search in, defaults to email. Can be `email` or
            `name`
        search_operator (str | Unset): The operator to use for the search. Can be `contains`,
            `starts_with` or `ends_with`
        limit (str | Unset): The number of users to return
        offset (str | Unset): The offset to start from
        sort_by (str | Unset): The field to sort by
        sort_direction (str | Unset): The direction to sort by
        filter_field (str | Unset): The field to filter by
        filter_value (str | Unset): The value to filter by
        filter_operator (str | Unset): The operator to use for the filter

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListUsersResponse200 | ListUsersResponse400 | ListUsersResponse401 | ListUsersResponse403 | ListUsersResponse404 | ListUsersResponse429 | ListUsersResponse500
    """

    return sync_detailed(
        client=client,
        search_value=search_value,
        search_field=search_field,
        search_operator=search_operator,
        limit=limit,
        offset=offset,
        sort_by=sort_by,
        sort_direction=sort_direction,
        filter_field=filter_field,
        filter_value=filter_value,
        filter_operator=filter_operator,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    search_value: str | Unset = UNSET,
    search_field: str | Unset = UNSET,
    search_operator: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    offset: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_direction: str | Unset = UNSET,
    filter_field: str | Unset = UNSET,
    filter_value: str | Unset = UNSET,
    filter_operator: str | Unset = UNSET,
) -> Response[
    ListUsersResponse200
    | ListUsersResponse400
    | ListUsersResponse401
    | ListUsersResponse403
    | ListUsersResponse404
    | ListUsersResponse429
    | ListUsersResponse500
]:
    """List users

    Args:
        search_value (str | Unset): The value to search for
        search_field (str | Unset): The field to search in, defaults to email. Can be `email` or
            `name`
        search_operator (str | Unset): The operator to use for the search. Can be `contains`,
            `starts_with` or `ends_with`
        limit (str | Unset): The number of users to return
        offset (str | Unset): The offset to start from
        sort_by (str | Unset): The field to sort by
        sort_direction (str | Unset): The direction to sort by
        filter_field (str | Unset): The field to filter by
        filter_value (str | Unset): The value to filter by
        filter_operator (str | Unset): The operator to use for the filter

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListUsersResponse200 | ListUsersResponse400 | ListUsersResponse401 | ListUsersResponse403 | ListUsersResponse404 | ListUsersResponse429 | ListUsersResponse500]
    """

    kwargs = _get_kwargs(
        search_value=search_value,
        search_field=search_field,
        search_operator=search_operator,
        limit=limit,
        offset=offset,
        sort_by=sort_by,
        sort_direction=sort_direction,
        filter_field=filter_field,
        filter_value=filter_value,
        filter_operator=filter_operator,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    search_value: str | Unset = UNSET,
    search_field: str | Unset = UNSET,
    search_operator: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    offset: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    sort_direction: str | Unset = UNSET,
    filter_field: str | Unset = UNSET,
    filter_value: str | Unset = UNSET,
    filter_operator: str | Unset = UNSET,
) -> (
    ListUsersResponse200
    | ListUsersResponse400
    | ListUsersResponse401
    | ListUsersResponse403
    | ListUsersResponse404
    | ListUsersResponse429
    | ListUsersResponse500
    | None
):
    """List users

    Args:
        search_value (str | Unset): The value to search for
        search_field (str | Unset): The field to search in, defaults to email. Can be `email` or
            `name`
        search_operator (str | Unset): The operator to use for the search. Can be `contains`,
            `starts_with` or `ends_with`
        limit (str | Unset): The number of users to return
        offset (str | Unset): The offset to start from
        sort_by (str | Unset): The field to sort by
        sort_direction (str | Unset): The direction to sort by
        filter_field (str | Unset): The field to filter by
        filter_value (str | Unset): The value to filter by
        filter_operator (str | Unset): The operator to use for the filter

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListUsersResponse200 | ListUsersResponse400 | ListUsersResponse401 | ListUsersResponse403 | ListUsersResponse404 | ListUsersResponse429 | ListUsersResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            search_value=search_value,
            search_field=search_field,
            search_operator=search_operator,
            limit=limit,
            offset=offset,
            sort_by=sort_by,
            sort_direction=sort_direction,
            filter_field=filter_field,
            filter_value=filter_value,
            filter_operator=filter_operator,
        )
    ).parsed
