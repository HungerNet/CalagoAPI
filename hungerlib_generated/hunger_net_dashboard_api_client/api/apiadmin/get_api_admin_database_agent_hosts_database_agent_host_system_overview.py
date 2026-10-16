from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_admin_database_agent_hosts_database_agent_host_system_overview_response_200 import (
    GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemOverviewResponse200,
)
from ...types import Response


def _get_kwargs(
    database_agent_host: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/admin/database-agent-hosts/{database_agent_host}/system/overview".format(
            database_agent_host=quote(str(database_agent_host), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemOverviewResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemOverviewResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemOverviewResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    database_agent_host: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemOverviewResponse200]:
    """
    Args:
        database_agent_host (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemOverviewResponse200]
    """

    kwargs = _get_kwargs(
        database_agent_host=database_agent_host,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    database_agent_host: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemOverviewResponse200 | None:
    """
    Args:
        database_agent_host (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemOverviewResponse200
    """

    return sync_detailed(
        database_agent_host=database_agent_host,
        client=client,
    ).parsed


async def asyncio_detailed(
    database_agent_host: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemOverviewResponse200]:
    """
    Args:
        database_agent_host (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemOverviewResponse200]
    """

    kwargs = _get_kwargs(
        database_agent_host=database_agent_host,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    database_agent_host: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemOverviewResponse200 | None:
    """
    Args:
        database_agent_host (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiAdminDatabaseAgentHostsDatabaseAgentHostSystemOverviewResponse200
    """

    return (
        await asyncio_detailed(
            database_agent_host=database_agent_host,
            client=client,
        )
    ).parsed
