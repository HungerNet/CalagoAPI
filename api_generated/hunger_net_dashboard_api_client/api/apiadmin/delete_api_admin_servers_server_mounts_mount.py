from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.delete_api_admin_servers_server_mounts_mount_response_200 import (
    DeleteApiAdminServersServerMountsMountResponse200,
)
from ...types import Response


def _get_kwargs(
    server: UUID,
    mount: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/admin/servers/{server}/mounts/{mount}".format(
            server=quote(str(server), safe=""),
            mount=quote(str(mount), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | DeleteApiAdminServersServerMountsMountResponse200 | None:
    if response.status_code == 200:
        response_200 = DeleteApiAdminServersServerMountsMountResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ApiError.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | DeleteApiAdminServersServerMountsMountResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    server: UUID,
    mount: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiError | DeleteApiAdminServersServerMountsMountResponse200]:
    """
    Args:
        server (UUID):
        mount (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DeleteApiAdminServersServerMountsMountResponse200]
    """

    kwargs = _get_kwargs(
        server=server,
        mount=mount,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    server: UUID,
    mount: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ApiError | DeleteApiAdminServersServerMountsMountResponse200 | None:
    """
    Args:
        server (UUID):
        mount (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DeleteApiAdminServersServerMountsMountResponse200
    """

    return sync_detailed(
        server=server,
        mount=mount,
        client=client,
    ).parsed


async def asyncio_detailed(
    server: UUID,
    mount: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiError | DeleteApiAdminServersServerMountsMountResponse200]:
    """
    Args:
        server (UUID):
        mount (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DeleteApiAdminServersServerMountsMountResponse200]
    """

    kwargs = _get_kwargs(
        server=server,
        mount=mount,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    server: UUID,
    mount: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ApiError | DeleteApiAdminServersServerMountsMountResponse200 | None:
    """
    Args:
        server (UUID):
        mount (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DeleteApiAdminServersServerMountsMountResponse200
    """

    return (
        await asyncio_detailed(
            server=server,
            mount=mount,
            client=client,
        )
    ).parsed
