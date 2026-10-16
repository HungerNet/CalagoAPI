from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_api_client_servers_groups_server_group_body import PatchApiClientServersGroupsServerGroupBody
from ...models.patch_api_client_servers_groups_server_group_response_200 import (
    PatchApiClientServersGroupsServerGroupResponse200,
)
from ...types import Response


def _get_kwargs(
    server_group: UUID,
    *,
    body: PatchApiClientServersGroupsServerGroupBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/client/servers/groups/{server_group}".format(
            server_group=quote(str(server_group), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PatchApiClientServersGroupsServerGroupResponse200 | None:
    if response.status_code == 200:
        response_200 = PatchApiClientServersGroupsServerGroupResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PatchApiClientServersGroupsServerGroupResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    server_group: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PatchApiClientServersGroupsServerGroupBody,
) -> Response[PatchApiClientServersGroupsServerGroupResponse200]:
    """
    Args:
        server_group (UUID):
        body (PatchApiClientServersGroupsServerGroupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchApiClientServersGroupsServerGroupResponse200]
    """

    kwargs = _get_kwargs(
        server_group=server_group,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    server_group: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PatchApiClientServersGroupsServerGroupBody,
) -> PatchApiClientServersGroupsServerGroupResponse200 | None:
    """
    Args:
        server_group (UUID):
        body (PatchApiClientServersGroupsServerGroupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchApiClientServersGroupsServerGroupResponse200
    """

    return sync_detailed(
        server_group=server_group,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    server_group: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PatchApiClientServersGroupsServerGroupBody,
) -> Response[PatchApiClientServersGroupsServerGroupResponse200]:
    """
    Args:
        server_group (UUID):
        body (PatchApiClientServersGroupsServerGroupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchApiClientServersGroupsServerGroupResponse200]
    """

    kwargs = _get_kwargs(
        server_group=server_group,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    server_group: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PatchApiClientServersGroupsServerGroupBody,
) -> PatchApiClientServersGroupsServerGroupResponse200 | None:
    """
    Args:
        server_group (UUID):
        body (PatchApiClientServersGroupsServerGroupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchApiClientServersGroupsServerGroupResponse200
    """

    return (
        await asyncio_detailed(
            server_group=server_group,
            client=client,
            body=body,
        )
    ).parsed
