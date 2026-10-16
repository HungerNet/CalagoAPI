from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.get_api_admin_nodes_node_backups_backup_response_200 import GetApiAdminNodesNodeBackupsBackupResponse200
from ...types import Response


def _get_kwargs(
    node: UUID,
    backup: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/admin/nodes/{node}/backups/{backup}".format(
            node=quote(str(node), safe=""),
            backup=quote(str(backup), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | GetApiAdminNodesNodeBackupsBackupResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApiAdminNodesNodeBackupsBackupResponse200.from_dict(response.json())

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
) -> Response[ApiError | GetApiAdminNodesNodeBackupsBackupResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    node: UUID,
    backup: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiError | GetApiAdminNodesNodeBackupsBackupResponse200]:
    """
    Args:
        node (UUID):
        backup (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | GetApiAdminNodesNodeBackupsBackupResponse200]
    """

    kwargs = _get_kwargs(
        node=node,
        backup=backup,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    node: UUID,
    backup: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ApiError | GetApiAdminNodesNodeBackupsBackupResponse200 | None:
    """
    Args:
        node (UUID):
        backup (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | GetApiAdminNodesNodeBackupsBackupResponse200
    """

    return sync_detailed(
        node=node,
        backup=backup,
        client=client,
    ).parsed


async def asyncio_detailed(
    node: UUID,
    backup: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiError | GetApiAdminNodesNodeBackupsBackupResponse200]:
    """
    Args:
        node (UUID):
        backup (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | GetApiAdminNodesNodeBackupsBackupResponse200]
    """

    kwargs = _get_kwargs(
        node=node,
        backup=backup,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    node: UUID,
    backup: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ApiError | GetApiAdminNodesNodeBackupsBackupResponse200 | None:
    """
    Args:
        node (UUID):
        backup (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | GetApiAdminNodesNodeBackupsBackupResponse200
    """

    return (
        await asyncio_detailed(
            node=node,
            backup=backup,
            client=client,
        )
    ).parsed
