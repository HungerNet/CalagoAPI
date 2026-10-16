from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.post_api_remote_servers_server_transfer_success_body import PostApiRemoteServersServerTransferSuccessBody
from ...models.post_api_remote_servers_server_transfer_success_response_200 import (
    PostApiRemoteServersServerTransferSuccessResponse200,
)
from ...types import Response


def _get_kwargs(
    server: UUID,
    *,
    body: PostApiRemoteServersServerTransferSuccessBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/remote/servers/{server}/transfer/success".format(
            server=quote(str(server), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PostApiRemoteServersServerTransferSuccessResponse200 | None:
    if response.status_code == 200:
        response_200 = PostApiRemoteServersServerTransferSuccessResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 409:
        response_409 = ApiError.from_dict(response.json())

        return response_409

    if response.status_code == 417:
        response_417 = ApiError.from_dict(response.json())

        return response_417

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | PostApiRemoteServersServerTransferSuccessResponse200]:
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
    body: PostApiRemoteServersServerTransferSuccessBody,
) -> Response[ApiError | PostApiRemoteServersServerTransferSuccessResponse200]:
    """
    Args:
        server (UUID):
        body (PostApiRemoteServersServerTransferSuccessBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiRemoteServersServerTransferSuccessResponse200]
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
    body: PostApiRemoteServersServerTransferSuccessBody,
) -> ApiError | PostApiRemoteServersServerTransferSuccessResponse200 | None:
    """
    Args:
        server (UUID):
        body (PostApiRemoteServersServerTransferSuccessBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiRemoteServersServerTransferSuccessResponse200
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
    body: PostApiRemoteServersServerTransferSuccessBody,
) -> Response[ApiError | PostApiRemoteServersServerTransferSuccessResponse200]:
    """
    Args:
        server (UUID):
        body (PostApiRemoteServersServerTransferSuccessBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiRemoteServersServerTransferSuccessResponse200]
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
    body: PostApiRemoteServersServerTransferSuccessBody,
) -> ApiError | PostApiRemoteServersServerTransferSuccessResponse200 | None:
    """
    Args:
        server (UUID):
        body (PostApiRemoteServersServerTransferSuccessBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiRemoteServersServerTransferSuccessResponse200
    """

    return (
        await asyncio_detailed(
            server=server,
            client=client,
            body=body,
        )
    ).parsed
