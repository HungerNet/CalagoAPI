from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.get_api_client_servers_server_backups_backup_query_response_200 import (
    GetApiClientServersServerBackupsBackupQueryResponse200,
)
from ...types import Response


def _get_kwargs(
    server: UUID,
    backup: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/client/servers/{server}/backups/{backup}/query".format(
            server=quote(str(server), safe=""),
            backup=quote(str(backup), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | GetApiClientServersServerBackupsBackupQueryResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApiClientServersServerBackupsBackupQueryResponse200.from_dict(response.json())

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
) -> Response[ApiError | GetApiClientServersServerBackupsBackupQueryResponse200]:
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
) -> Response[ApiError | GetApiClientServersServerBackupsBackupQueryResponse200]:
    """
    Args:
        server (UUID):
        backup (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | GetApiClientServersServerBackupsBackupQueryResponse200]
    """

    kwargs = _get_kwargs(
        server=server,
        backup=backup,
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
) -> ApiError | GetApiClientServersServerBackupsBackupQueryResponse200 | None:
    """
    Args:
        server (UUID):
        backup (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | GetApiClientServersServerBackupsBackupQueryResponse200
    """

    return sync_detailed(
        server=server,
        backup=backup,
        client=client,
    ).parsed


async def asyncio_detailed(
    server: UUID,
    backup: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiError | GetApiClientServersServerBackupsBackupQueryResponse200]:
    """
    Args:
        server (UUID):
        backup (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | GetApiClientServersServerBackupsBackupQueryResponse200]
    """

    kwargs = _get_kwargs(
        server=server,
        backup=backup,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    server: UUID,
    backup: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ApiError | GetApiClientServersServerBackupsBackupQueryResponse200 | None:
    """
    Args:
        server (UUID):
        backup (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | GetApiClientServersServerBackupsBackupQueryResponse200
    """

    return (
        await asyncio_detailed(
            server=server,
            backup=backup,
            client=client,
        )
    ).parsed
