from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.get_api_admin_nodes_node_devices_device_allowed_response_200 import (
    GetApiAdminNodesNodeDevicesDeviceAllowedResponse200,
)
from ...types import Response


def _get_kwargs(
    node: UUID,
    device: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/admin/nodes/{node}/devices/{device}/allowed".format(
            node=quote(str(node), safe=""),
            device=quote(str(device), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | GetApiAdminNodesNodeDevicesDeviceAllowedResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApiAdminNodesNodeDevicesDeviceAllowedResponse200.from_dict(response.json())

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
) -> Response[ApiError | GetApiAdminNodesNodeDevicesDeviceAllowedResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    node: UUID,
    device: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiError | GetApiAdminNodesNodeDevicesDeviceAllowedResponse200]:
    """
    Args:
        node (UUID):
        device (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | GetApiAdminNodesNodeDevicesDeviceAllowedResponse200]
    """

    kwargs = _get_kwargs(
        node=node,
        device=device,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    node: UUID,
    device: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ApiError | GetApiAdminNodesNodeDevicesDeviceAllowedResponse200 | None:
    """
    Args:
        node (UUID):
        device (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | GetApiAdminNodesNodeDevicesDeviceAllowedResponse200
    """

    return sync_detailed(
        node=node,
        device=device,
        client=client,
    ).parsed


async def asyncio_detailed(
    node: UUID,
    device: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiError | GetApiAdminNodesNodeDevicesDeviceAllowedResponse200]:
    """
    Args:
        node (UUID):
        device (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | GetApiAdminNodesNodeDevicesDeviceAllowedResponse200]
    """

    kwargs = _get_kwargs(
        node=node,
        device=device,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    node: UUID,
    device: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ApiError | GetApiAdminNodesNodeDevicesDeviceAllowedResponse200 | None:
    """
    Args:
        node (UUID):
        device (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | GetApiAdminNodesNodeDevicesDeviceAllowedResponse200
    """

    return (
        await asyncio_detailed(
            node=node,
            device=device,
            client=client,
        )
    ).parsed
