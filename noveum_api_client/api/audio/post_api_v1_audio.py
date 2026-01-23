from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import File, Response


def _get_kwargs(
    *,
    file: File,
    trace_id: str,
    span_id: str,
    audio_uuid: str,
) -> dict[str, Any]:
    # Build multipart form data
    files = {
        "file": file.to_tuple(),
    }

    data = {
        "traceId": trace_id,
        "spanId": span_id,
        "audio_uuid": audio_uuid,
    }

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/audio",
        "files": files,
        "data": data,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 201:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 401:
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
    file: File,
    trace_id: str,
    span_id: str,
    audio_uuid: str,
) -> Response[Any]:
    """Upload audio file

     Upload an audio file. Supports various audio formats including MP3, WAV, AAC, OGG, FLAC, and M4A.
    Maximum file size is 50MB.

    Args:
        file (File): Audio file to upload (File object with payload, file_name, mime_type)
        trace_id (str): Trace ID for observability tracking
        span_id (str): Span ID for observability tracking
        audio_uuid (str): Unique identifier for this audio file

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        file=file,
        trace_id=trace_id,
        span_id=span_id,
        audio_uuid=audio_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    file: File,
    trace_id: str,
    span_id: str,
    audio_uuid: str,
) -> Response[Any]:
    """Upload audio file

     Upload an audio file. Supports various audio formats including MP3, WAV, AAC, OGG, FLAC, and M4A.
    Maximum file size is 50MB.

    Args:
        file (File): Audio file to upload (File object with payload, file_name, mime_type)
        trace_id (str): Trace ID for observability tracking
        span_id (str): Span ID for observability tracking
        audio_uuid (str): Unique identifier for this audio file

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        file=file,
        trace_id=trace_id,
        span_id=span_id,
        audio_uuid=audio_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
