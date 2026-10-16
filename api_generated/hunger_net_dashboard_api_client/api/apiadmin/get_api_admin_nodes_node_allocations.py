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
    node: UUID,
    *,
    page: int,
    per_page: int,
    search: str | Unset = UNSET,
    ip: str | Unset = UNSET,
    port_from: int | Unset = UNSET,
    port_to: int | Unset = UNSET,
    assigned: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params["search"] = search

    params["ip"] = ip

    params["port_from"] = port_from

    params["port_to"] = port_to

    params["assigned"] = assigned

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/admin/nodes/{node}/allocations".format(
            node=quote(str(node), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiError | None:
    if response.status_code == 404:
        response_404 = ApiError.from_dict(response.json())

        return response_404

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
    node: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int,
    per_page: int,
    search: str | Unset = UNSET,
    ip: str | Unset = UNSET,
    port_from: int | Unset = UNSET,
    port_to: int | Unset = UNSET,
    assigned: bool | Unset = UNSET,
) -> Response[ApiError]:
    """
    Args:
        node (UUID):
        page (int):
        per_page (int):
        search (str | Unset):
        ip (str | Unset):
        port_from (int | Unset):
        port_to (int | Unset):
        assigned (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError]
    """

    kwargs = _get_kwargs(
        node=node,
        page=page,
        per_page=per_page,
        search=search,
        ip=ip,
        port_from=port_from,
        port_to=port_to,
        assigned=assigned,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    node: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int,
    per_page: int,
    search: str | Unset = UNSET,
    ip: str | Unset = UNSET,
    port_from: int | Unset = UNSET,
    port_to: int | Unset = UNSET,
    assigned: bool | Unset = UNSET,
) -> ApiError | None:
    """
    Args:
        node (UUID):
        page (int):
        per_page (int):
        search (str | Unset):
        ip (str | Unset):
        port_from (int | Unset):
        port_to (int | Unset):
        assigned (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError
    """

    return sync_detailed(
        node=node,
        client=client,
        page=page,
        per_page=per_page,
        search=search,
        ip=ip,
        port_from=port_from,
        port_to=port_to,
        assigned=assigned,
    ).parsed


async def asyncio_detailed(
    node: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int,
    per_page: int,
    search: str | Unset = UNSET,
    ip: str | Unset = UNSET,
    port_from: int | Unset = UNSET,
    port_to: int | Unset = UNSET,
    assigned: bool | Unset = UNSET,
) -> Response[ApiError]:
    """
    Args:
        node (UUID):
        page (int):
        per_page (int):
        search (str | Unset):
        ip (str | Unset):
        port_from (int | Unset):
        port_to (int | Unset):
        assigned (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError]
    """

    kwargs = _get_kwargs(
        node=node,
        page=page,
        per_page=per_page,
        search=search,
        ip=ip,
        port_from=port_from,
        port_to=port_to,
        assigned=assigned,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    node: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int,
    per_page: int,
    search: str | Unset = UNSET,
    ip: str | Unset = UNSET,
    port_from: int | Unset = UNSET,
    port_to: int | Unset = UNSET,
    assigned: bool | Unset = UNSET,
) -> ApiError | None:
    """
    Args:
        node (UUID):
        page (int):
        per_page (int):
        search (str | Unset):
        ip (str | Unset):
        port_from (int | Unset):
        port_to (int | Unset):
        assigned (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError
    """

    return (
        await asyncio_detailed(
            node=node,
            client=client,
            page=page,
            per_page=per_page,
            search=search,
            ip=ip,
            port_from=port_from,
            port_to=port_to,
            assigned=assigned,
        )
    ).parsed
