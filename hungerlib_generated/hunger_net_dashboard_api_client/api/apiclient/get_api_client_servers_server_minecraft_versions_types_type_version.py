from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_client_servers_server_minecraft_versions_types_type_version_response_200 import (
    GetApiClientServersServerMinecraftVersionsTypesTypeVersionResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    server: UUID,
    type_: str,
    version: str,
    *,
    page: int,
    per_page: int,
    search: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params["search"] = search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/client/servers/{server}/minecraft/versions/types/{type_}/{version}".format(
            server=quote(str(server), safe=""),
            type_=quote(str(type_), safe=""),
            version=quote(str(version), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApiClientServersServerMinecraftVersionsTypesTypeVersionResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApiClientServersServerMinecraftVersionsTypesTypeVersionResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApiClientServersServerMinecraftVersionsTypesTypeVersionResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    server: UUID,
    type_: str,
    version: str,
    *,
    client: AuthenticatedClient | Client,
    page: int,
    per_page: int,
    search: str | Unset = UNSET,
) -> Response[GetApiClientServersServerMinecraftVersionsTypesTypeVersionResponse200]:
    """
    Args:
        server (UUID):
        type_ (str):
        version (str):
        page (int):
        per_page (int):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiClientServersServerMinecraftVersionsTypesTypeVersionResponse200]
    """

    kwargs = _get_kwargs(
        server=server,
        type_=type_,
        version=version,
        page=page,
        per_page=per_page,
        search=search,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    server: UUID,
    type_: str,
    version: str,
    *,
    client: AuthenticatedClient | Client,
    page: int,
    per_page: int,
    search: str | Unset = UNSET,
) -> GetApiClientServersServerMinecraftVersionsTypesTypeVersionResponse200 | None:
    """
    Args:
        server (UUID):
        type_ (str):
        version (str):
        page (int):
        per_page (int):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiClientServersServerMinecraftVersionsTypesTypeVersionResponse200
    """

    return sync_detailed(
        server=server,
        type_=type_,
        version=version,
        client=client,
        page=page,
        per_page=per_page,
        search=search,
    ).parsed


async def asyncio_detailed(
    server: UUID,
    type_: str,
    version: str,
    *,
    client: AuthenticatedClient | Client,
    page: int,
    per_page: int,
    search: str | Unset = UNSET,
) -> Response[GetApiClientServersServerMinecraftVersionsTypesTypeVersionResponse200]:
    """
    Args:
        server (UUID):
        type_ (str):
        version (str):
        page (int):
        per_page (int):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiClientServersServerMinecraftVersionsTypesTypeVersionResponse200]
    """

    kwargs = _get_kwargs(
        server=server,
        type_=type_,
        version=version,
        page=page,
        per_page=per_page,
        search=search,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    server: UUID,
    type_: str,
    version: str,
    *,
    client: AuthenticatedClient | Client,
    page: int,
    per_page: int,
    search: str | Unset = UNSET,
) -> GetApiClientServersServerMinecraftVersionsTypesTypeVersionResponse200 | None:
    """
    Args:
        server (UUID):
        type_ (str):
        version (str):
        page (int):
        per_page (int):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiClientServersServerMinecraftVersionsTypesTypeVersionResponse200
    """

    return (
        await asyncio_detailed(
            server=server,
            type_=type_,
            version=version,
            client=client,
            page=page,
            per_page=per_page,
            search=search,
        )
    ).parsed
