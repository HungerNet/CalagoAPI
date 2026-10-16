from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.post_api_client_servers_server_databases_instances_database_instance_import_response_200 import (
    PostApiClientServersServerDatabasesInstancesDatabaseInstanceImportResponse200,
)
from ...types import UNSET, Response


def _get_kwargs(
    server: UUID,
    database_instance: UUID,
    *,
    body: list[int],
    wipe: bool,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["wipe"] = wipe

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/client/servers/{server}/databases/instances/{database_instance}/import".format(
            server=quote(str(server), safe=""),
            database_instance=quote(str(database_instance), safe=""),
        ),
        "params": params,
    }

    _kwargs["content"] = body.payload
    headers["Content-Type"] = "application/octet-stream"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PostApiClientServersServerDatabasesInstancesDatabaseInstanceImportResponse200 | None:
    if response.status_code == 200:
        response_200 = PostApiClientServersServerDatabasesInstancesDatabaseInstanceImportResponse200.from_dict(
            response.json()
        )

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

    if response.status_code == 409:
        response_409 = ApiError.from_dict(response.json())

        return response_409

    if response.status_code == 417:
        response_417 = ApiError.from_dict(response.json())

        return response_417

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | PostApiClientServersServerDatabasesInstancesDatabaseInstanceImportResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    server: UUID,
    database_instance: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: list[int],
    wipe: bool,
) -> Response[ApiError | PostApiClientServersServerDatabasesInstancesDatabaseInstanceImportResponse200]:
    """
    Args:
        server (UUID):
        database_instance (UUID):
        wipe (bool):
        body (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiClientServersServerDatabasesInstancesDatabaseInstanceImportResponse200]
    """

    kwargs = _get_kwargs(
        server=server,
        database_instance=database_instance,
        body=body,
        wipe=wipe,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    server: UUID,
    database_instance: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: list[int],
    wipe: bool,
) -> ApiError | PostApiClientServersServerDatabasesInstancesDatabaseInstanceImportResponse200 | None:
    """
    Args:
        server (UUID):
        database_instance (UUID):
        wipe (bool):
        body (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiClientServersServerDatabasesInstancesDatabaseInstanceImportResponse200
    """

    return sync_detailed(
        server=server,
        database_instance=database_instance,
        client=client,
        body=body,
        wipe=wipe,
    ).parsed


async def asyncio_detailed(
    server: UUID,
    database_instance: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: list[int],
    wipe: bool,
) -> Response[ApiError | PostApiClientServersServerDatabasesInstancesDatabaseInstanceImportResponse200]:
    """
    Args:
        server (UUID):
        database_instance (UUID):
        wipe (bool):
        body (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiClientServersServerDatabasesInstancesDatabaseInstanceImportResponse200]
    """

    kwargs = _get_kwargs(
        server=server,
        database_instance=database_instance,
        body=body,
        wipe=wipe,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    server: UUID,
    database_instance: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: list[int],
    wipe: bool,
) -> ApiError | PostApiClientServersServerDatabasesInstancesDatabaseInstanceImportResponse200 | None:
    """
    Args:
        server (UUID):
        database_instance (UUID):
        wipe (bool):
        body (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiClientServersServerDatabasesInstancesDatabaseInstanceImportResponse200
    """

    return (
        await asyncio_detailed(
            server=server,
            database_instance=database_instance,
            client=client,
            body=body,
            wipe=wipe,
        )
    ).parsed
