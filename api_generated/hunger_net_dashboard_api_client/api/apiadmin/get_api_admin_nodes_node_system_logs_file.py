from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response


def _get_kwargs(
    node: UUID,
    file: str,
    *,
    lines: int,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["lines"] = lines

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/admin/nodes/{node}/system/logs/{file}".format(
            node=quote(str(node), safe=""),
            file=quote(str(file), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> str | None:
    if response.status_code == 200:
        response_200 = response.text
        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    node: UUID,
    file: str,
    *,
    client: AuthenticatedClient | Client,
    lines: int,
) -> Response[str]:
    """
    Args:
        node (UUID):
        file (str):
        lines (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        node=node,
        file=file,
        lines=lines,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    node: UUID,
    file: str,
    *,
    client: AuthenticatedClient | Client,
    lines: int,
) -> str | None:
    """
    Args:
        node (UUID):
        file (str):
        lines (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return sync_detailed(
        node=node,
        file=file,
        client=client,
        lines=lines,
    ).parsed


async def asyncio_detailed(
    node: UUID,
    file: str,
    *,
    client: AuthenticatedClient | Client,
    lines: int,
) -> Response[str]:
    """
    Args:
        node (UUID):
        file (str):
        lines (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        node=node,
        file=file,
        lines=lines,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    node: UUID,
    file: str,
    *,
    client: AuthenticatedClient | Client,
    lines: int,
) -> str | None:
    """
    Args:
        node (UUID):
        file (str):
        lines (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return (
        await asyncio_detailed(
            node=node,
            file=file,
            client=client,
            lines=lines,
        )
    ).parsed
