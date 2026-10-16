from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.post_api_admin_servers_server_backups_delete_failed_body import (
    PostApiAdminServersServerBackupsDeleteFailedBody,
)
from ...models.post_api_admin_servers_server_backups_delete_failed_response_200 import (
    PostApiAdminServersServerBackupsDeleteFailedResponse200,
)
from ...types import Response


def _get_kwargs(
    server: UUID,
    *,
    body: PostApiAdminServersServerBackupsDeleteFailedBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/admin/servers/{server}/backups/delete-failed".format(
            server=quote(str(server), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PostApiAdminServersServerBackupsDeleteFailedResponse200 | None:
    if response.status_code == 200:
        response_200 = PostApiAdminServersServerBackupsDeleteFailedResponse200.from_dict(response.json())

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
) -> Response[ApiError | PostApiAdminServersServerBackupsDeleteFailedResponse200]:
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
    body: PostApiAdminServersServerBackupsDeleteFailedBody,
) -> Response[ApiError | PostApiAdminServersServerBackupsDeleteFailedResponse200]:
    """
    Args:
        server (UUID):
        body (PostApiAdminServersServerBackupsDeleteFailedBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiAdminServersServerBackupsDeleteFailedResponse200]
    """

    kwargs = _get_kwargs(
        server=server,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    server: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiAdminServersServerBackupsDeleteFailedBody,
) -> ApiError | PostApiAdminServersServerBackupsDeleteFailedResponse200 | None:
    """
    Args:
        server (UUID):
        body (PostApiAdminServersServerBackupsDeleteFailedBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiAdminServersServerBackupsDeleteFailedResponse200
    """

    return sync_detailed(
        server=server,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    server: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiAdminServersServerBackupsDeleteFailedBody,
) -> Response[ApiError | PostApiAdminServersServerBackupsDeleteFailedResponse200]:
    """
    Args:
        server (UUID):
        body (PostApiAdminServersServerBackupsDeleteFailedBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiAdminServersServerBackupsDeleteFailedResponse200]
    """

    kwargs = _get_kwargs(
        server=server,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    server: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiAdminServersServerBackupsDeleteFailedBody,
) -> ApiError | PostApiAdminServersServerBackupsDeleteFailedResponse200 | None:
    """
    Args:
        server (UUID):
        body (PostApiAdminServersServerBackupsDeleteFailedBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiAdminServersServerBackupsDeleteFailedResponse200
    """

    return (
        await asyncio_detailed(
            server=server,
            client=client,
            body=body,
        )
    ).parsed
