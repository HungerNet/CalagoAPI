from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.post_api_admin_nodes_node_backups_backup_reattach_body import (
    PostApiAdminNodesNodeBackupsBackupReattachBody,
)
from ...models.post_api_admin_nodes_node_backups_backup_reattach_response_200 import (
    PostApiAdminNodesNodeBackupsBackupReattachResponse200,
)
from ...types import Response


def _get_kwargs(
    node: UUID,
    backup: UUID,
    *,
    body: PostApiAdminNodesNodeBackupsBackupReattachBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/admin/nodes/{node}/backups/{backup}/reattach".format(
            node=quote(str(node), safe=""),
            backup=quote(str(backup), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PostApiAdminNodesNodeBackupsBackupReattachResponse200 | None:
    if response.status_code == 200:
        response_200 = PostApiAdminNodesNodeBackupsBackupReattachResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiError.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ApiError.from_dict(response.json())

        return response_404

    if response.status_code == 417:
        response_417 = ApiError.from_dict(response.json())

        return response_417

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | PostApiAdminNodesNodeBackupsBackupReattachResponse200]:
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
    body: PostApiAdminNodesNodeBackupsBackupReattachBody,
) -> Response[ApiError | PostApiAdminNodesNodeBackupsBackupReattachResponse200]:
    """
    Args:
        node (UUID):
        backup (UUID):
        body (PostApiAdminNodesNodeBackupsBackupReattachBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiAdminNodesNodeBackupsBackupReattachResponse200]
    """

    kwargs = _get_kwargs(
        node=node,
        backup=backup,
        body=body,
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
    body: PostApiAdminNodesNodeBackupsBackupReattachBody,
) -> ApiError | PostApiAdminNodesNodeBackupsBackupReattachResponse200 | None:
    """
    Args:
        node (UUID):
        backup (UUID):
        body (PostApiAdminNodesNodeBackupsBackupReattachBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiAdminNodesNodeBackupsBackupReattachResponse200
    """

    return sync_detailed(
        node=node,
        backup=backup,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    node: UUID,
    backup: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiAdminNodesNodeBackupsBackupReattachBody,
) -> Response[ApiError | PostApiAdminNodesNodeBackupsBackupReattachResponse200]:
    """
    Args:
        node (UUID):
        backup (UUID):
        body (PostApiAdminNodesNodeBackupsBackupReattachBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiAdminNodesNodeBackupsBackupReattachResponse200]
    """

    kwargs = _get_kwargs(
        node=node,
        backup=backup,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    node: UUID,
    backup: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiAdminNodesNodeBackupsBackupReattachBody,
) -> ApiError | PostApiAdminNodesNodeBackupsBackupReattachResponse200 | None:
    """
    Args:
        node (UUID):
        backup (UUID):
        body (PostApiAdminNodesNodeBackupsBackupReattachBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiAdminNodesNodeBackupsBackupReattachResponse200
    """

    return (
        await asyncio_detailed(
            node=node,
            backup=backup,
            client=client,
            body=body,
        )
    ).parsed
