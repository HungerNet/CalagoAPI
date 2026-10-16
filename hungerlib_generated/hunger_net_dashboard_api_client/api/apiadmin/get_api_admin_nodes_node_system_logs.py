from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_admin_nodes_node_system_logs_response_200 import GetApiAdminNodesNodeSystemLogsResponse200
from ...types import Response


def _get_kwargs(
    node: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/admin/nodes/{node}/system/logs".format(
            node=quote(str(node), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApiAdminNodesNodeSystemLogsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApiAdminNodesNodeSystemLogsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApiAdminNodesNodeSystemLogsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    node: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetApiAdminNodesNodeSystemLogsResponse200]:
    """
    Args:
        node (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiAdminNodesNodeSystemLogsResponse200]
    """

    kwargs = _get_kwargs(
        node=node,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    node: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> GetApiAdminNodesNodeSystemLogsResponse200 | None:
    """
    Args:
        node (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiAdminNodesNodeSystemLogsResponse200
    """

    return sync_detailed(
        node=node,
        client=client,
    ).parsed


async def asyncio_detailed(
    node: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetApiAdminNodesNodeSystemLogsResponse200]:
    """
    Args:
        node (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiAdminNodesNodeSystemLogsResponse200]
    """

    kwargs = _get_kwargs(
        node=node,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    node: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> GetApiAdminNodesNodeSystemLogsResponse200 | None:
    """
    Args:
        node (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiAdminNodesNodeSystemLogsResponse200
    """

    return (
        await asyncio_detailed(
            node=node,
            client=client,
        )
    ).parsed
