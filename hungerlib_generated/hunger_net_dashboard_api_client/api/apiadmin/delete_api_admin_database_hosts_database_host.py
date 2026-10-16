from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.delete_api_admin_database_hosts_database_host_body import DeleteApiAdminDatabaseHostsDatabaseHostBody
from ...models.delete_api_admin_database_hosts_database_host_response_200 import (
    DeleteApiAdminDatabaseHostsDatabaseHostResponse200,
)
from ...types import Response


def _get_kwargs(
    database_host: UUID,
    *,
    body: DeleteApiAdminDatabaseHostsDatabaseHostBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/admin/database-hosts/{database_host}".format(
            database_host=quote(str(database_host), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | DeleteApiAdminDatabaseHostsDatabaseHostResponse200 | None:
    if response.status_code == 200:
        response_200 = DeleteApiAdminDatabaseHostsDatabaseHostResponse200.from_dict(response.json())

        return response_200

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
) -> Response[ApiError | DeleteApiAdminDatabaseHostsDatabaseHostResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    database_host: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: DeleteApiAdminDatabaseHostsDatabaseHostBody,
) -> Response[ApiError | DeleteApiAdminDatabaseHostsDatabaseHostResponse200]:
    """
    Args:
        database_host (UUID):
        body (DeleteApiAdminDatabaseHostsDatabaseHostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DeleteApiAdminDatabaseHostsDatabaseHostResponse200]
    """

    kwargs = _get_kwargs(
        database_host=database_host,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    database_host: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: DeleteApiAdminDatabaseHostsDatabaseHostBody,
) -> ApiError | DeleteApiAdminDatabaseHostsDatabaseHostResponse200 | None:
    """
    Args:
        database_host (UUID):
        body (DeleteApiAdminDatabaseHostsDatabaseHostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DeleteApiAdminDatabaseHostsDatabaseHostResponse200
    """

    return sync_detailed(
        database_host=database_host,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    database_host: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: DeleteApiAdminDatabaseHostsDatabaseHostBody,
) -> Response[ApiError | DeleteApiAdminDatabaseHostsDatabaseHostResponse200]:
    """
    Args:
        database_host (UUID):
        body (DeleteApiAdminDatabaseHostsDatabaseHostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DeleteApiAdminDatabaseHostsDatabaseHostResponse200]
    """

    kwargs = _get_kwargs(
        database_host=database_host,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    database_host: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: DeleteApiAdminDatabaseHostsDatabaseHostBody,
) -> ApiError | DeleteApiAdminDatabaseHostsDatabaseHostResponse200 | None:
    """
    Args:
        database_host (UUID):
        body (DeleteApiAdminDatabaseHostsDatabaseHostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DeleteApiAdminDatabaseHostsDatabaseHostResponse200
    """

    return (
        await asyncio_detailed(
            database_host=database_host,
            client=client,
            body=body,
        )
    ).parsed
