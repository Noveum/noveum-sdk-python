from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_payments_create_checkout_link_type import PostApiPaymentsCreateCheckoutLinkType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    type_: PostApiPaymentsCreateCheckoutLinkType,
    product_id: str,
    redirect_url: str | Unset = UNSET,
    organization_id: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_type_ = type_.value
    params["type"] = json_type_

    params["productId"] = product_id

    params["redirectUrl"] = redirect_url

    params["organizationId"] = organization_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/payments/create-checkout-link",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    type_: PostApiPaymentsCreateCheckoutLinkType,
    product_id: str,
    redirect_url: str | Unset = UNSET,
    organization_id: str | Unset = UNSET,
) -> Response[Any]:
    """Create a checkout link

     Creates a checkout link for a one-time or subscription product

    Args:
        type_ (PostApiPaymentsCreateCheckoutLinkType):
        product_id (str):
        redirect_url (str | Unset):
        organization_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        type_=type_,
        product_id=product_id,
        redirect_url=redirect_url,
        organization_id=organization_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    type_: PostApiPaymentsCreateCheckoutLinkType,
    product_id: str,
    redirect_url: str | Unset = UNSET,
    organization_id: str | Unset = UNSET,
) -> Response[Any]:
    """Create a checkout link

     Creates a checkout link for a one-time or subscription product

    Args:
        type_ (PostApiPaymentsCreateCheckoutLinkType):
        product_id (str):
        redirect_url (str | Unset):
        organization_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        type_=type_,
        product_id=product_id,
        redirect_url=redirect_url,
        organization_id=organization_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
