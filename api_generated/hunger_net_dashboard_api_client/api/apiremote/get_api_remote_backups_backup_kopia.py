from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.get_api_remote_backups_backup_kopia_response_200 import GetApiRemoteBackupsBackupKopiaResponse200
from ...types import Response


def _get_kwargs(
    backup: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/remote/backups/{backup}/kopia".format(
            backup=quote(str(backup), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | GetApiRemoteBackupsBackupKopiaResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApiRemoteBackupsBackupKopiaResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 417:
        response_417 = ApiError.from_dict(response.json())

        return response_417

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | GetApiRemoteBackupsBackupKopiaResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    backup: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiError | GetApiRemoteBackupsBackupKopiaResponse200]:
    """
    Args:
        backup (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | GetApiRemoteBackupsBackupKopiaResponse200]
    """

    kwargs = _get_kwargs(
        backup=backup,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    backup: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ApiError | GetApiRemoteBackupsBackupKopiaResponse200 | None:
    """
    Args:
        backup (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | GetApiRemoteBackupsBackupKopiaResponse200
    """

    return sync_detailed(
        backup=backup,
        client=client,
    ).parsed


async def asyncio_detailed(
    backup: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiError | GetApiRemoteBackupsBackupKopiaResponse200]:
    """
    Args:
        backup (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | GetApiRemoteBackupsBackupKopiaResponse200]
    """

    kwargs = _get_kwargs(
        backup=backup,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    backup: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ApiError | GetApiRemoteBackupsBackupKopiaResponse200 | None:
    """
    Args:
        backup (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | GetApiRemoteBackupsBackupKopiaResponse200
    """

    return (
        await asyncio_detailed(
            backup=backup,
            client=client,
        )
    ).parsed
