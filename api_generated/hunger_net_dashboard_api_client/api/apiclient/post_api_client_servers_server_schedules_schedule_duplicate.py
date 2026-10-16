from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.post_api_client_servers_server_schedules_schedule_duplicate_body import (
    PostApiClientServersServerSchedulesScheduleDuplicateBody,
)
from ...types import Response


def _get_kwargs(
    server: UUID,
    schedule: UUID,
    *,
    body: PostApiClientServersServerSchedulesScheduleDuplicateBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/client/servers/{server}/schedules/{schedule}/duplicate".format(
            server=quote(str(server), safe=""),
            schedule=quote(str(schedule), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiError | None:
    if response.status_code == 400:
        response_400 = ApiError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiError.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ApiError.from_dict(response.json())

        return response_404

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    server: UUID,
    schedule: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiClientServersServerSchedulesScheduleDuplicateBody,
) -> Response[ApiError]:
    """
    Args:
        server (UUID):
        schedule (UUID):
        body (PostApiClientServersServerSchedulesScheduleDuplicateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError]
    """

    kwargs = _get_kwargs(
        server=server,
        schedule=schedule,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    server: UUID,
    schedule: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiClientServersServerSchedulesScheduleDuplicateBody,
) -> ApiError | None:
    """
    Args:
        server (UUID):
        schedule (UUID):
        body (PostApiClientServersServerSchedulesScheduleDuplicateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError
    """

    return sync_detailed(
        server=server,
        schedule=schedule,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    server: UUID,
    schedule: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiClientServersServerSchedulesScheduleDuplicateBody,
) -> Response[ApiError]:
    """
    Args:
        server (UUID):
        schedule (UUID):
        body (PostApiClientServersServerSchedulesScheduleDuplicateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError]
    """

    kwargs = _get_kwargs(
        server=server,
        schedule=schedule,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    server: UUID,
    schedule: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiClientServersServerSchedulesScheduleDuplicateBody,
) -> ApiError | None:
    """
    Args:
        server (UUID):
        schedule (UUID):
        body (PostApiClientServersServerSchedulesScheduleDuplicateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError
    """

    return (
        await asyncio_detailed(
            server=server,
            schedule=schedule,
            client=client,
            body=body,
        )
    ).parsed
