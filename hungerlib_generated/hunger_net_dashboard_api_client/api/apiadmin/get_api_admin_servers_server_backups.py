from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    server: UUID,
    *,
    page: int,
    per_page: int,
    search: str | Unset = UNSET,
    partially_detached: bool,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params["search"] = search

    params["partially_detached"] = partially_detached

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/admin/servers/{server}/backups".format(
            server=quote(str(server), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiError | None:
    if response.status_code == 401:
        response_401 = ApiError.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiError]:
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
    partially_detached: bool,
) -> Response[ApiError]:
    """
    Args:
        server (UUID):
        page (int):
        per_page (int):
        search (str | Unset):
        partially_detached (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError]
    """

    kwargs = _get_kwargs(
        server=server,
        page=page,
        per_page=per_page,
        search=search,
        partially_detached=partially_detached,
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
    partially_detached: bool,
) -> ApiError | None:
    """
    Args:
        server (UUID):
        page (int):
        per_page (int):
        search (str | Unset):
        partially_detached (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError
    """

    return sync_detailed(
        server=server,
        client=client,
        page=page,
        per_page=per_page,
        search=search,
        partially_detached=partially_detached,
    ).parsed


async def asyncio_detailed(
    server: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int,
    per_page: int,
    search: str | Unset = UNSET,
    partially_detached: bool,
) -> Response[ApiError]:
    """
    Args:
        server (UUID):
        page (int):
        per_page (int):
        search (str | Unset):
        partially_detached (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError]
    """

    kwargs = _get_kwargs(
        server=server,
        page=page,
        per_page=per_page,
        search=search,
        partially_detached=partially_detached,
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
    partially_detached: bool,
) -> ApiError | None:
    """
    Args:
        server (UUID):
        page (int):
        per_page (int):
        search (str | Unset):
        partially_detached (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError
    """

    return (
        await asyncio_detailed(
            server=server,
            client=client,
            page=page,
            per_page=per_page,
            search=search,
            partially_detached=partially_detached,
        )
    ).parsed
