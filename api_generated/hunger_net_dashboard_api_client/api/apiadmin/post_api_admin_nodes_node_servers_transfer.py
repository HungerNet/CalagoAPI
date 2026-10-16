from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.post_api_admin_nodes_node_servers_transfer_body import PostApiAdminNodesNodeServersTransferBody
from ...models.post_api_admin_nodes_node_servers_transfer_response_202 import (
    PostApiAdminNodesNodeServersTransferResponse202,
)
from ...types import Response


def _get_kwargs(
    node: UUID,
    *,
    body: PostApiAdminNodesNodeServersTransferBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/admin/nodes/{node}/servers/transfer".format(
            node=quote(str(node), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PostApiAdminNodesNodeServersTransferResponse202 | None:
    if response.status_code == 202:
        response_202 = PostApiAdminNodesNodeServersTransferResponse202.from_dict(response.json())

        return response_202

    if response.status_code == 401:
        response_401 = ApiError.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | PostApiAdminNodesNodeServersTransferResponse202]:
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
    body: PostApiAdminNodesNodeServersTransferBody,
) -> Response[ApiError | PostApiAdminNodesNodeServersTransferResponse202]:
    """
    Args:
        node (UUID):
        body (PostApiAdminNodesNodeServersTransferBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiAdminNodesNodeServersTransferResponse202]
    """

    kwargs = _get_kwargs(
        node=node,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    node: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiAdminNodesNodeServersTransferBody,
) -> ApiError | PostApiAdminNodesNodeServersTransferResponse202 | None:
    """
    Args:
        node (UUID):
        body (PostApiAdminNodesNodeServersTransferBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiAdminNodesNodeServersTransferResponse202
    """

    return sync_detailed(
        node=node,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    node: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiAdminNodesNodeServersTransferBody,
) -> Response[ApiError | PostApiAdminNodesNodeServersTransferResponse202]:
    """
    Args:
        node (UUID):
        body (PostApiAdminNodesNodeServersTransferBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiAdminNodesNodeServersTransferResponse202]
    """

    kwargs = _get_kwargs(
        node=node,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    node: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiAdminNodesNodeServersTransferBody,
) -> ApiError | PostApiAdminNodesNodeServersTransferResponse202 | None:
    """
    Args:
        node (UUID):
        body (PostApiAdminNodesNodeServersTransferBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiAdminNodesNodeServersTransferResponse202
    """

    return (
        await asyncio_detailed(
            node=node,
            client=client,
            body=body,
        )
    ).parsed
