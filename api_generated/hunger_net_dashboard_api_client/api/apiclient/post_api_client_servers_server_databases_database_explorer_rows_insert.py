from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.post_api_client_servers_server_databases_database_explorer_rows_insert_body import (
    PostApiClientServersServerDatabasesDatabaseExplorerRowsInsertBody,
)
from ...models.post_api_client_servers_server_databases_database_explorer_rows_insert_response_200 import (
    PostApiClientServersServerDatabasesDatabaseExplorerRowsInsertResponse200,
)
from ...types import Response


def _get_kwargs(
    server: UUID,
    database: UUID,
    *,
    body: PostApiClientServersServerDatabasesDatabaseExplorerRowsInsertBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/client/servers/{server}/databases/{database}/explorer/rows/insert".format(
            server=quote(str(server), safe=""),
            database=quote(str(database), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PostApiClientServersServerDatabasesDatabaseExplorerRowsInsertResponse200 | None:
    if response.status_code == 200:
        response_200 = PostApiClientServersServerDatabasesDatabaseExplorerRowsInsertResponse200.from_dict(
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

    if response.status_code == 417:
        response_417 = ApiError.from_dict(response.json())

        return response_417

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | PostApiClientServersServerDatabasesDatabaseExplorerRowsInsertResponse200]:
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
    body: PostApiClientServersServerDatabasesDatabaseExplorerRowsInsertBody,
) -> Response[ApiError | PostApiClientServersServerDatabasesDatabaseExplorerRowsInsertResponse200]:
    """
    Args:
        server (UUID):
        database (UUID):
        body (PostApiClientServersServerDatabasesDatabaseExplorerRowsInsertBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiClientServersServerDatabasesDatabaseExplorerRowsInsertResponse200]
    """

    kwargs = _get_kwargs(
        server=server,
        database=database,
        body=body,
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
    body: PostApiClientServersServerDatabasesDatabaseExplorerRowsInsertBody,
) -> ApiError | PostApiClientServersServerDatabasesDatabaseExplorerRowsInsertResponse200 | None:
    """
    Args:
        server (UUID):
        database (UUID):
        body (PostApiClientServersServerDatabasesDatabaseExplorerRowsInsertBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiClientServersServerDatabasesDatabaseExplorerRowsInsertResponse200
    """

    return sync_detailed(
        server=server,
        database=database,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    server: UUID,
    database: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiClientServersServerDatabasesDatabaseExplorerRowsInsertBody,
) -> Response[ApiError | PostApiClientServersServerDatabasesDatabaseExplorerRowsInsertResponse200]:
    """
    Args:
        server (UUID):
        database (UUID):
        body (PostApiClientServersServerDatabasesDatabaseExplorerRowsInsertBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiClientServersServerDatabasesDatabaseExplorerRowsInsertResponse200]
    """

    kwargs = _get_kwargs(
        server=server,
        database=database,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    server: UUID,
    database: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiClientServersServerDatabasesDatabaseExplorerRowsInsertBody,
) -> ApiError | PostApiClientServersServerDatabasesDatabaseExplorerRowsInsertResponse200 | None:
    """
    Args:
        server (UUID):
        database (UUID):
        body (PostApiClientServersServerDatabasesDatabaseExplorerRowsInsertBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiClientServersServerDatabasesDatabaseExplorerRowsInsertResponse200
    """

    return (
        await asyncio_detailed(
            server=server,
            database=database,
            client=client,
            body=body,
        )
    ).parsed
