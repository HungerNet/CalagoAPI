from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.delete_api_admin_backup_configurations_backup_configuration_response_200 import (
    DeleteApiAdminBackupConfigurationsBackupConfigurationResponse200,
)
from ...types import Response


def _get_kwargs(
    backup_configuration: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/admin/backup-configurations/{backup_configuration}".format(
            backup_configuration=quote(str(backup_configuration), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | DeleteApiAdminBackupConfigurationsBackupConfigurationResponse200 | None:
    if response.status_code == 200:
        response_200 = DeleteApiAdminBackupConfigurationsBackupConfigurationResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ApiError.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | DeleteApiAdminBackupConfigurationsBackupConfigurationResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    backup_configuration: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiError | DeleteApiAdminBackupConfigurationsBackupConfigurationResponse200]:
    """
    Args:
        backup_configuration (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DeleteApiAdminBackupConfigurationsBackupConfigurationResponse200]
    """

    kwargs = _get_kwargs(
        backup_configuration=backup_configuration,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    backup_configuration: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ApiError | DeleteApiAdminBackupConfigurationsBackupConfigurationResponse200 | None:
    """
    Args:
        backup_configuration (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DeleteApiAdminBackupConfigurationsBackupConfigurationResponse200
    """

    return sync_detailed(
        backup_configuration=backup_configuration,
        client=client,
    ).parsed


async def asyncio_detailed(
    backup_configuration: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiError | DeleteApiAdminBackupConfigurationsBackupConfigurationResponse200]:
    """
    Args:
        backup_configuration (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DeleteApiAdminBackupConfigurationsBackupConfigurationResponse200]
    """

    kwargs = _get_kwargs(
        backup_configuration=backup_configuration,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    backup_configuration: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ApiError | DeleteApiAdminBackupConfigurationsBackupConfigurationResponse200 | None:
    """
    Args:
        backup_configuration (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DeleteApiAdminBackupConfigurationsBackupConfigurationResponse200
    """

    return (
        await asyncio_detailed(
            backup_configuration=backup_configuration,
            client=client,
        )
    ).parsed
