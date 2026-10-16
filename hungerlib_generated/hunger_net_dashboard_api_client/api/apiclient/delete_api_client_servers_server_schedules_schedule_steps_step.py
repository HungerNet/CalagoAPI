from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.delete_api_client_servers_server_schedules_schedule_steps_step_response_200 import (
    DeleteApiClientServersServerSchedulesScheduleStepsStepResponse200,
)
from ...types import Response


def _get_kwargs(
    server: UUID,
    schedule: UUID,
    step: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/client/servers/{server}/schedules/{schedule}/steps/{step}".format(
            server=quote(str(server), safe=""),
            schedule=quote(str(schedule), safe=""),
            step=quote(str(step), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | DeleteApiClientServersServerSchedulesScheduleStepsStepResponse200 | None:
    if response.status_code == 200:
        response_200 = DeleteApiClientServersServerSchedulesScheduleStepsStepResponse200.from_dict(response.json())

        return response_200

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
) -> Response[ApiError | DeleteApiClientServersServerSchedulesScheduleStepsStepResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    server: UUID,
    schedule: UUID,
    step: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiError | DeleteApiClientServersServerSchedulesScheduleStepsStepResponse200]:
    """
    Args:
        server (UUID):
        schedule (UUID):
        step (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DeleteApiClientServersServerSchedulesScheduleStepsStepResponse200]
    """

    kwargs = _get_kwargs(
        server=server,
        schedule=schedule,
        step=step,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    server: UUID,
    schedule: UUID,
    step: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ApiError | DeleteApiClientServersServerSchedulesScheduleStepsStepResponse200 | None:
    """
    Args:
        server (UUID):
        schedule (UUID):
        step (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DeleteApiClientServersServerSchedulesScheduleStepsStepResponse200
    """

    return sync_detailed(
        server=server,
        schedule=schedule,
        step=step,
        client=client,
    ).parsed


async def asyncio_detailed(
    server: UUID,
    schedule: UUID,
    step: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiError | DeleteApiClientServersServerSchedulesScheduleStepsStepResponse200]:
    """
    Args:
        server (UUID):
        schedule (UUID):
        step (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DeleteApiClientServersServerSchedulesScheduleStepsStepResponse200]
    """

    kwargs = _get_kwargs(
        server=server,
        schedule=schedule,
        step=step,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    server: UUID,
    schedule: UUID,
    step: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ApiError | DeleteApiClientServersServerSchedulesScheduleStepsStepResponse200 | None:
    """
    Args:
        server (UUID):
        schedule (UUID):
        step (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DeleteApiClientServersServerSchedulesScheduleStepsStepResponse200
    """

    return (
        await asyncio_detailed(
            server=server,
            schedule=schedule,
            step=step,
            client=client,
        )
    ).parsed
