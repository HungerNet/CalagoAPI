from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.post_api_client_servers_server_files_copy_many_body import PostApiClientServersServerFilesCopyManyBody
from ...models.post_api_client_servers_server_files_copy_many_response_200 import (
    PostApiClientServersServerFilesCopyManyResponse200,
)
from ...models.post_api_client_servers_server_files_copy_many_response_202 import (
    PostApiClientServersServerFilesCopyManyResponse202,
)
from ...types import Response


def _get_kwargs(
    server: UUID,
    *,
    body: PostApiClientServersServerFilesCopyManyBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/client/servers/{server}/files/copy-many".format(
            server=quote(str(server), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ApiError
    | PostApiClientServersServerFilesCopyManyResponse200
    | PostApiClientServersServerFilesCopyManyResponse202
    | None
):
    if response.status_code == 200:
        response_200 = PostApiClientServersServerFilesCopyManyResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = PostApiClientServersServerFilesCopyManyResponse202.from_dict(response.json())

        return response_202

    if response.status_code == 401:
        response_401 = ApiError.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ApiError.from_dict(response.json())

        return response_404

    if response.status_code == 417:
        response_417 = ApiError.from_dict(response.json())

        return response_417

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ApiError | PostApiClientServersServerFilesCopyManyResponse200 | PostApiClientServersServerFilesCopyManyResponse202
]:
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
    body: PostApiClientServersServerFilesCopyManyBody,
) -> Response[
    ApiError | PostApiClientServersServerFilesCopyManyResponse200 | PostApiClientServersServerFilesCopyManyResponse202
]:
    """
    Args:
        server (UUID):
        body (PostApiClientServersServerFilesCopyManyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiClientServersServerFilesCopyManyResponse200 | PostApiClientServersServerFilesCopyManyResponse202]
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
    body: PostApiClientServersServerFilesCopyManyBody,
) -> (
    ApiError
    | PostApiClientServersServerFilesCopyManyResponse200
    | PostApiClientServersServerFilesCopyManyResponse202
    | None
):
    """
    Args:
        server (UUID):
        body (PostApiClientServersServerFilesCopyManyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiClientServersServerFilesCopyManyResponse200 | PostApiClientServersServerFilesCopyManyResponse202
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
    body: PostApiClientServersServerFilesCopyManyBody,
) -> Response[
    ApiError | PostApiClientServersServerFilesCopyManyResponse200 | PostApiClientServersServerFilesCopyManyResponse202
]:
    """
    Args:
        server (UUID):
        body (PostApiClientServersServerFilesCopyManyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiClientServersServerFilesCopyManyResponse200 | PostApiClientServersServerFilesCopyManyResponse202]
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
    body: PostApiClientServersServerFilesCopyManyBody,
) -> (
    ApiError
    | PostApiClientServersServerFilesCopyManyResponse200
    | PostApiClientServersServerFilesCopyManyResponse202
    | None
):
    """
    Args:
        server (UUID):
        body (PostApiClientServersServerFilesCopyManyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiClientServersServerFilesCopyManyResponse200 | PostApiClientServersServerFilesCopyManyResponse202
    """

    return (
        await asyncio_detailed(
            server=server,
            client=client,
            body=body,
        )
    ).parsed
