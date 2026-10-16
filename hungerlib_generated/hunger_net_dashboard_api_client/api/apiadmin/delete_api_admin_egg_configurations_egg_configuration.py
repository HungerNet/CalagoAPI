from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.delete_api_admin_egg_configurations_egg_configuration_response_200 import (
    DeleteApiAdminEggConfigurationsEggConfigurationResponse200,
)
from ...types import Response


def _get_kwargs(
    egg_configuration: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/admin/egg-configurations/{egg_configuration}".format(
            egg_configuration=quote(str(egg_configuration), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | DeleteApiAdminEggConfigurationsEggConfigurationResponse200 | None:
    if response.status_code == 200:
        response_200 = DeleteApiAdminEggConfigurationsEggConfigurationResponse200.from_dict(response.json())

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
) -> Response[ApiError | DeleteApiAdminEggConfigurationsEggConfigurationResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    egg_configuration: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiError | DeleteApiAdminEggConfigurationsEggConfigurationResponse200]:
    """
    Args:
        egg_configuration (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DeleteApiAdminEggConfigurationsEggConfigurationResponse200]
    """

    kwargs = _get_kwargs(
        egg_configuration=egg_configuration,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    egg_configuration: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ApiError | DeleteApiAdminEggConfigurationsEggConfigurationResponse200 | None:
    """
    Args:
        egg_configuration (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DeleteApiAdminEggConfigurationsEggConfigurationResponse200
    """

    return sync_detailed(
        egg_configuration=egg_configuration,
        client=client,
    ).parsed


async def asyncio_detailed(
    egg_configuration: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiError | DeleteApiAdminEggConfigurationsEggConfigurationResponse200]:
    """
    Args:
        egg_configuration (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DeleteApiAdminEggConfigurationsEggConfigurationResponse200]
    """

    kwargs = _get_kwargs(
        egg_configuration=egg_configuration,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    egg_configuration: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ApiError | DeleteApiAdminEggConfigurationsEggConfigurationResponse200 | None:
    """
    Args:
        egg_configuration (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DeleteApiAdminEggConfigurationsEggConfigurationResponse200
    """

    return (
        await asyncio_detailed(
            egg_configuration=egg_configuration,
            client=client,
        )
    ).parsed
