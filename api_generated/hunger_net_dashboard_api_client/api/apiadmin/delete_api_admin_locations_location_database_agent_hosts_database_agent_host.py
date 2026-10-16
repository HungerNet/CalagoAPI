from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.delete_api_admin_locations_location_database_agent_hosts_database_agent_host_response_200 import (
    DeleteApiAdminLocationsLocationDatabaseAgentHostsDatabaseAgentHostResponse200,
)
from ...types import Response


def _get_kwargs(
    location: UUID,
    database_agent_host: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/admin/locations/{location}/database-agent-hosts/{database_agent_host}".format(
            location=quote(str(location), safe=""),
            database_agent_host=quote(str(database_agent_host), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | DeleteApiAdminLocationsLocationDatabaseAgentHostsDatabaseAgentHostResponse200 | None:
    if response.status_code == 200:
        response_200 = DeleteApiAdminLocationsLocationDatabaseAgentHostsDatabaseAgentHostResponse200.from_dict(
            response.json()
        )

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
) -> Response[ApiError | DeleteApiAdminLocationsLocationDatabaseAgentHostsDatabaseAgentHostResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    location: UUID,
    database_agent_host: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiError | DeleteApiAdminLocationsLocationDatabaseAgentHostsDatabaseAgentHostResponse200]:
    """
    Args:
        location (UUID):
        database_agent_host (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DeleteApiAdminLocationsLocationDatabaseAgentHostsDatabaseAgentHostResponse200]
    """

    kwargs = _get_kwargs(
        location=location,
        database_agent_host=database_agent_host,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    location: UUID,
    database_agent_host: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ApiError | DeleteApiAdminLocationsLocationDatabaseAgentHostsDatabaseAgentHostResponse200 | None:
    """
    Args:
        location (UUID):
        database_agent_host (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DeleteApiAdminLocationsLocationDatabaseAgentHostsDatabaseAgentHostResponse200
    """

    return sync_detailed(
        location=location,
        database_agent_host=database_agent_host,
        client=client,
    ).parsed


async def asyncio_detailed(
    location: UUID,
    database_agent_host: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiError | DeleteApiAdminLocationsLocationDatabaseAgentHostsDatabaseAgentHostResponse200]:
    """
    Args:
        location (UUID):
        database_agent_host (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DeleteApiAdminLocationsLocationDatabaseAgentHostsDatabaseAgentHostResponse200]
    """

    kwargs = _get_kwargs(
        location=location,
        database_agent_host=database_agent_host,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    location: UUID,
    database_agent_host: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ApiError | DeleteApiAdminLocationsLocationDatabaseAgentHostsDatabaseAgentHostResponse200 | None:
    """
    Args:
        location (UUID):
        database_agent_host (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DeleteApiAdminLocationsLocationDatabaseAgentHostsDatabaseAgentHostResponse200
    """

    return (
        await asyncio_detailed(
            location=location,
            database_agent_host=database_agent_host,
            client=client,
        )
    ).parsed
