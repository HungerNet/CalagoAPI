from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.delete_api_admin_nodes_node_allocations_body import DeleteApiAdminNodesNodeAllocationsBody
from ...models.delete_api_admin_nodes_node_allocations_response_200 import DeleteApiAdminNodesNodeAllocationsResponse200
from ...types import Response


def _get_kwargs(
    node: UUID,
    *,
    body: DeleteApiAdminNodesNodeAllocationsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/admin/nodes/{node}/allocations".format(
            node=quote(str(node), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | DeleteApiAdminNodesNodeAllocationsResponse200 | None:
    if response.status_code == 200:
        response_200 = DeleteApiAdminNodesNodeAllocationsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ApiError.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ApiError.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | DeleteApiAdminNodesNodeAllocationsResponse200]:
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
    body: DeleteApiAdminNodesNodeAllocationsBody,
) -> Response[ApiError | DeleteApiAdminNodesNodeAllocationsResponse200]:
    """
    Args:
        node (UUID):
        body (DeleteApiAdminNodesNodeAllocationsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DeleteApiAdminNodesNodeAllocationsResponse200]
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
    body: DeleteApiAdminNodesNodeAllocationsBody,
) -> ApiError | DeleteApiAdminNodesNodeAllocationsResponse200 | None:
    """
    Args:
        node (UUID):
        body (DeleteApiAdminNodesNodeAllocationsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DeleteApiAdminNodesNodeAllocationsResponse200
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
    body: DeleteApiAdminNodesNodeAllocationsBody,
) -> Response[ApiError | DeleteApiAdminNodesNodeAllocationsResponse200]:
    """
    Args:
        node (UUID):
        body (DeleteApiAdminNodesNodeAllocationsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DeleteApiAdminNodesNodeAllocationsResponse200]
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
    body: DeleteApiAdminNodesNodeAllocationsBody,
) -> ApiError | DeleteApiAdminNodesNodeAllocationsResponse200 | None:
    """
    Args:
        node (UUID):
        body (DeleteApiAdminNodesNodeAllocationsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DeleteApiAdminNodesNodeAllocationsResponse200
    """

    return (
        await asyncio_detailed(
            node=node,
            client=client,
            body=body,
        )
    ).parsed
