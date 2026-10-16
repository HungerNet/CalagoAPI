from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...types import Response


def _get_kwargs(
    database_agent_host: UUID,
    database_instance: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/admin/database-agent-hosts/{database_agent_host}/instances/{database_instance}".format(
            database_agent_host=quote(str(database_agent_host), safe=""),
            database_instance=quote(str(database_instance), safe=""),
        ),
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
    database_agent_host: UUID,
    database_instance: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiError]:
    """
    Args:
        database_agent_host (UUID):
        database_instance (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError]
    """

    kwargs = _get_kwargs(
        database_agent_host=database_agent_host,
        database_instance=database_instance,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    database_agent_host: UUID,
    database_instance: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ApiError | None:
    """
    Args:
        database_agent_host (UUID):
        database_instance (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError
    """

    return sync_detailed(
        database_agent_host=database_agent_host,
        database_instance=database_instance,
        client=client,
    ).parsed


async def asyncio_detailed(
    database_agent_host: UUID,
    database_instance: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiError]:
    """
    Args:
        database_agent_host (UUID):
        database_instance (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError]
    """

    kwargs = _get_kwargs(
        database_agent_host=database_agent_host,
        database_instance=database_instance,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    database_agent_host: UUID,
    database_instance: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ApiError | None:
    """
    Args:
        database_agent_host (UUID):
        database_instance (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError
    """

    return (
        await asyncio_detailed(
            database_agent_host=database_agent_host,
            database_instance=database_instance,
            client=client,
        )
    ).parsed
