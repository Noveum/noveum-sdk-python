from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_telemetry_metrics_dashboard_interval import GetApiTelemetryMetricsDashboardInterval
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    organization_id: str,
    start_time: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    project: str | Unset = UNSET,
    interval: GetApiTelemetryMetricsDashboardInterval | Unset = UNSET,
    time_zone: str | Unset = UNSET,
    auto_detect_interval: bool | Unset = UNSET,
    provider: str | Unset = UNSET,
    model: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["organizationId"] = organization_id

    params["startTime"] = start_time

    params["endTime"] = end_time

    params["project"] = project

    json_interval: str | Unset = UNSET
    if not isinstance(interval, Unset):
        json_interval = interval.value

    params["interval"] = json_interval

    params["timeZone"] = time_zone

    params["autoDetectInterval"] = auto_detect_interval

    params["provider"] = provider

    params["model"] = model

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/telemetry/metrics/dashboard",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 403:
        return None

    if response.status_code == 408:
        return None

    if response.status_code == 500:
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
    organization_id: str,
    start_time: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    project: str | Unset = UNSET,
    interval: GetApiTelemetryMetricsDashboardInterval | Unset = UNSET,
    time_zone: str | Unset = UNSET,
    auto_detect_interval: bool | Unset = UNSET,
    provider: str | Unset = UNSET,
    model: str | Unset = UNSET,
) -> Response[Any]:
    """Get dashboard metrics

    Args:
        organization_id (str):
        start_time (str | Unset):
        end_time (str | Unset):
        project (str | Unset):
        interval (GetApiTelemetryMetricsDashboardInterval | Unset):
        time_zone (str | Unset):
        auto_detect_interval (bool | Unset):
        provider (str | Unset):
        model (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        start_time=start_time,
        end_time=end_time,
        project=project,
        interval=interval,
        time_zone=time_zone,
        auto_detect_interval=auto_detect_interval,
        provider=provider,
        model=model,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    organization_id: str,
    start_time: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    project: str | Unset = UNSET,
    interval: GetApiTelemetryMetricsDashboardInterval | Unset = UNSET,
    time_zone: str | Unset = UNSET,
    auto_detect_interval: bool | Unset = UNSET,
    provider: str | Unset = UNSET,
    model: str | Unset = UNSET,
) -> Response[Any]:
    """Get dashboard metrics

    Args:
        organization_id (str):
        start_time (str | Unset):
        end_time (str | Unset):
        project (str | Unset):
        interval (GetApiTelemetryMetricsDashboardInterval | Unset):
        time_zone (str | Unset):
        auto_detect_interval (bool | Unset):
        provider (str | Unset):
        model (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        start_time=start_time,
        end_time=end_time,
        project=project,
        interval=interval,
        time_zone=time_zone,
        auto_detect_interval=auto_detect_interval,
        provider=provider,
        model=model,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
