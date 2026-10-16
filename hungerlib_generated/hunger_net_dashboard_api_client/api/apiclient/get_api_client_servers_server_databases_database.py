from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.get_api_client_servers_server_databases_database_response_200 import (
    GetApiClientServersServerDatabasesDatabaseResponse200,
)
from ...types import UNSET, Response


def _get_kwargs(
    server: UUID,
    database: UUID,
    *,
    include_password: bool,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["include_password"] = include_password

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/client/servers/{server}/databases/{database}".format(
            server=quote(str(server), safe=""),
            database=quote(str(database), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | GetApiClientServersServerDatabasesDatabaseResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApiClientServersServerDatabasesDatabaseResponse200.from_dict(response.json())

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
) -> Response[ApiError | GetApiClientServersServerDatabasesDatabaseResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    server: UUID,
    database: UUID,
    *,
    client: AuthenticatedClient | Client,
    include_password: bool,
) -> Response[ApiError | GetApiClientServersServerDatabasesDatabaseResponse200]:
    """
    Args:
        server (UUID):
        database (UUID):
        include_password (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | GetApiClientServersServerDatabasesDatabaseResponse200]
    """

    kwargs = _get_kwargs(
        server=server,
        database=database,
        include_password=include_password,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    server: UUID,
    database: UUID,
    *,
    client: AuthenticatedClient | Client,
    include_password: bool,
) -> ApiError | GetApiClientServersServerDatabasesDatabaseResponse200 | None:
    """
    Args:
        server (UUID):
        database (UUID):
        include_password (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | GetApiClientServersServerDatabasesDatabaseResponse200
    """

    return sync_detailed(
        server=server,
        database=database,
        client=client,
        include_password=include_password,
    ).parsed


async def asyncio_detailed(
    server: UUID,
    database: UUID,
    *,
    client: AuthenticatedClient | Client,
    include_password: bool,
) -> Response[ApiError | GetApiClientServersServerDatabasesDatabaseResponse200]:
    """
    Args:
        server (UUID):
        database (UUID):
        include_password (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | GetApiClientServersServerDatabasesDatabaseResponse200]
    """

    kwargs = _get_kwargs(
        server=server,
        database=database,
        include_password=include_password,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    server: UUID,
    database: UUID,
    *,
    client: AuthenticatedClient | Client,
    include_password: bool,
) -> ApiError | GetApiClientServersServerDatabasesDatabaseResponse200 | None:
    """
    Args:
        server (UUID):
        database (UUID):
        include_password (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | GetApiClientServersServerDatabasesDatabaseResponse200
    """

    return (
        await asyncio_detailed(
            server=server,
            database=database,
            client=client,
            include_password=include_password,
        )
    ).parsed
