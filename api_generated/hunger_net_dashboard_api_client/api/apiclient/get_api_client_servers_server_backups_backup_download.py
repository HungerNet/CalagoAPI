from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.get_api_client_servers_server_backups_backup_download_response_200 import (
    GetApiClientServersServerBackupsBackupDownloadResponse200,
)
from ...models.streamable_archive_format import StreamableArchiveFormat
from ...types import UNSET, Response


def _get_kwargs(
    server: UUID,
    backup: UUID,
    *,
    archive_format: StreamableArchiveFormat,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_archive_format = archive_format.value
    params["archive_format"] = json_archive_format

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/client/servers/{server}/backups/{backup}/download".format(
            server=quote(str(server), safe=""),
            backup=quote(str(backup), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | GetApiClientServersServerBackupsBackupDownloadResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApiClientServersServerBackupsBackupDownloadResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ApiError.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ApiError.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | GetApiClientServersServerBackupsBackupDownloadResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    server: UUID,
    backup: UUID,
    *,
    client: AuthenticatedClient | Client,
    archive_format: StreamableArchiveFormat,
) -> Response[ApiError | GetApiClientServersServerBackupsBackupDownloadResponse200]:
    """
    Args:
        server (UUID):
        backup (UUID):
        archive_format (StreamableArchiveFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | GetApiClientServersServerBackupsBackupDownloadResponse200]
    """

    kwargs = _get_kwargs(
        server=server,
        backup=backup,
        archive_format=archive_format,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    server: UUID,
    backup: UUID,
    *,
    client: AuthenticatedClient | Client,
    archive_format: StreamableArchiveFormat,
) -> ApiError | GetApiClientServersServerBackupsBackupDownloadResponse200 | None:
    """
    Args:
        server (UUID):
        backup (UUID):
        archive_format (StreamableArchiveFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | GetApiClientServersServerBackupsBackupDownloadResponse200
    """

    return sync_detailed(
        server=server,
        backup=backup,
        client=client,
        archive_format=archive_format,
    ).parsed


async def asyncio_detailed(
    server: UUID,
    backup: UUID,
    *,
    client: AuthenticatedClient | Client,
    archive_format: StreamableArchiveFormat,
) -> Response[ApiError | GetApiClientServersServerBackupsBackupDownloadResponse200]:
    """
    Args:
        server (UUID):
        backup (UUID):
        archive_format (StreamableArchiveFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | GetApiClientServersServerBackupsBackupDownloadResponse200]
    """

    kwargs = _get_kwargs(
        server=server,
        backup=backup,
        archive_format=archive_format,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    server: UUID,
    backup: UUID,
    *,
    client: AuthenticatedClient | Client,
    archive_format: StreamableArchiveFormat,
) -> ApiError | GetApiClientServersServerBackupsBackupDownloadResponse200 | None:
    """
    Args:
        server (UUID):
        backup (UUID):
        archive_format (StreamableArchiveFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | GetApiClientServersServerBackupsBackupDownloadResponse200
    """

    return (
        await asyncio_detailed(
            server=server,
            backup=backup,
            client=client,
            archive_format=archive_format,
        )
    ).parsed
