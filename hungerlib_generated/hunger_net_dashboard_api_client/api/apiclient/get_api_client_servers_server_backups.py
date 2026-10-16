from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.database_agent_type import DatabaseAgentType
from ...models.get_api_client_servers_server_backups_response_200 import GetApiClientServersServerBackupsResponse200
from ...models.server_backup_kind import ServerBackupKind
from ...types import UNSET, Response, Unset


def _get_kwargs(
    server: UUID,
    *,
    page: int,
    per_page: int,
    search: str | Unset = UNSET,
    ungrouped: bool,
    kind: ServerBackupKind | Unset = UNSET,
    database_instance_uuid: UUID | Unset = UNSET,
    database_type: DatabaseAgentType | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params["search"] = search

    params["ungrouped"] = ungrouped

    json_kind: str | Unset = UNSET
    if not isinstance(kind, Unset):
        json_kind = kind.value

    params["kind"] = json_kind

    json_database_instance_uuid: str | Unset = UNSET
    if not isinstance(database_instance_uuid, Unset):
        json_database_instance_uuid = str(database_instance_uuid)
    params["database_instance_uuid"] = json_database_instance_uuid

    json_database_type: str | Unset = UNSET
    if not isinstance(database_type, Unset):
        json_database_type = database_type.value

    params["database_type"] = json_database_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/client/servers/{server}/backups".format(
            server=quote(str(server), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | GetApiClientServersServerBackupsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApiClientServersServerBackupsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ApiError.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | GetApiClientServersServerBackupsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    server: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int,
    per_page: int,
    search: str | Unset = UNSET,
    ungrouped: bool,
    kind: ServerBackupKind | Unset = UNSET,
    database_instance_uuid: UUID | Unset = UNSET,
    database_type: DatabaseAgentType | Unset = UNSET,
) -> Response[ApiError | GetApiClientServersServerBackupsResponse200]:
    """
    Args:
        server (UUID):
        page (int):
        per_page (int):
        search (str | Unset):
        ungrouped (bool):
        kind (ServerBackupKind | Unset):
        database_instance_uuid (UUID | Unset):
        database_type (DatabaseAgentType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | GetApiClientServersServerBackupsResponse200]
    """

    kwargs = _get_kwargs(
        server=server,
        page=page,
        per_page=per_page,
        search=search,
        ungrouped=ungrouped,
        kind=kind,
        database_instance_uuid=database_instance_uuid,
        database_type=database_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    server: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int,
    per_page: int,
    search: str | Unset = UNSET,
    ungrouped: bool,
    kind: ServerBackupKind | Unset = UNSET,
    database_instance_uuid: UUID | Unset = UNSET,
    database_type: DatabaseAgentType | Unset = UNSET,
) -> ApiError | GetApiClientServersServerBackupsResponse200 | None:
    """
    Args:
        server (UUID):
        page (int):
        per_page (int):
        search (str | Unset):
        ungrouped (bool):
        kind (ServerBackupKind | Unset):
        database_instance_uuid (UUID | Unset):
        database_type (DatabaseAgentType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | GetApiClientServersServerBackupsResponse200
    """

    return sync_detailed(
        server=server,
        client=client,
        page=page,
        per_page=per_page,
        search=search,
        ungrouped=ungrouped,
        kind=kind,
        database_instance_uuid=database_instance_uuid,
        database_type=database_type,
    ).parsed


async def asyncio_detailed(
    server: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int,
    per_page: int,
    search: str | Unset = UNSET,
    ungrouped: bool,
    kind: ServerBackupKind | Unset = UNSET,
    database_instance_uuid: UUID | Unset = UNSET,
    database_type: DatabaseAgentType | Unset = UNSET,
) -> Response[ApiError | GetApiClientServersServerBackupsResponse200]:
    """
    Args:
        server (UUID):
        page (int):
        per_page (int):
        search (str | Unset):
        ungrouped (bool):
        kind (ServerBackupKind | Unset):
        database_instance_uuid (UUID | Unset):
        database_type (DatabaseAgentType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | GetApiClientServersServerBackupsResponse200]
    """

    kwargs = _get_kwargs(
        server=server,
        page=page,
        per_page=per_page,
        search=search,
        ungrouped=ungrouped,
        kind=kind,
        database_instance_uuid=database_instance_uuid,
        database_type=database_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    server: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int,
    per_page: int,
    search: str | Unset = UNSET,
    ungrouped: bool,
    kind: ServerBackupKind | Unset = UNSET,
    database_instance_uuid: UUID | Unset = UNSET,
    database_type: DatabaseAgentType | Unset = UNSET,
) -> ApiError | GetApiClientServersServerBackupsResponse200 | None:
    """
    Args:
        server (UUID):
        page (int):
        per_page (int):
        search (str | Unset):
        ungrouped (bool):
        kind (ServerBackupKind | Unset):
        database_instance_uuid (UUID | Unset):
        database_type (DatabaseAgentType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | GetApiClientServersServerBackupsResponse200
    """

    return (
        await asyncio_detailed(
            server=server,
            client=client,
            page=page,
            per_page=per_page,
            search=search,
            ungrouped=ungrouped,
            kind=kind,
            database_instance_uuid=database_instance_uuid,
            database_type=database_type,
        )
    ).parsed
