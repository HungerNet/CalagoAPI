from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.patch_api_admin_backup_configurations_backup_configuration_body import (
    PatchApiAdminBackupConfigurationsBackupConfigurationBody,
)
from ...models.patch_api_admin_backup_configurations_backup_configuration_response_200 import (
    PatchApiAdminBackupConfigurationsBackupConfigurationResponse200,
)
from ...types import Response


def _get_kwargs(
    backup_configuration: UUID,
    *,
    body: PatchApiAdminBackupConfigurationsBackupConfigurationBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/admin/backup-configurations/{backup_configuration}".format(
            backup_configuration=quote(str(backup_configuration), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PatchApiAdminBackupConfigurationsBackupConfigurationResponse200 | None:
    if response.status_code == 200:
        response_200 = PatchApiAdminBackupConfigurationsBackupConfigurationResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiError.from_dict(response.json())

        return response_400

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
) -> Response[ApiError | PatchApiAdminBackupConfigurationsBackupConfigurationResponse200]:
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
    body: PatchApiAdminBackupConfigurationsBackupConfigurationBody,
) -> Response[ApiError | PatchApiAdminBackupConfigurationsBackupConfigurationResponse200]:
    """
    Args:
        backup_configuration (UUID):
        body (PatchApiAdminBackupConfigurationsBackupConfigurationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PatchApiAdminBackupConfigurationsBackupConfigurationResponse200]
    """

    kwargs = _get_kwargs(
        backup_configuration=backup_configuration,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    backup_configuration: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PatchApiAdminBackupConfigurationsBackupConfigurationBody,
) -> ApiError | PatchApiAdminBackupConfigurationsBackupConfigurationResponse200 | None:
    """
    Args:
        backup_configuration (UUID):
        body (PatchApiAdminBackupConfigurationsBackupConfigurationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PatchApiAdminBackupConfigurationsBackupConfigurationResponse200
    """

    return sync_detailed(
        backup_configuration=backup_configuration,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    backup_configuration: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PatchApiAdminBackupConfigurationsBackupConfigurationBody,
) -> Response[ApiError | PatchApiAdminBackupConfigurationsBackupConfigurationResponse200]:
    """
    Args:
        backup_configuration (UUID):
        body (PatchApiAdminBackupConfigurationsBackupConfigurationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PatchApiAdminBackupConfigurationsBackupConfigurationResponse200]
    """

    kwargs = _get_kwargs(
        backup_configuration=backup_configuration,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    backup_configuration: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PatchApiAdminBackupConfigurationsBackupConfigurationBody,
) -> ApiError | PatchApiAdminBackupConfigurationsBackupConfigurationResponse200 | None:
    """
    Args:
        backup_configuration (UUID):
        body (PatchApiAdminBackupConfigurationsBackupConfigurationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PatchApiAdminBackupConfigurationsBackupConfigurationResponse200
    """

    return (
        await asyncio_detailed(
            backup_configuration=backup_configuration,
            client=client,
            body=body,
        )
    ).parsed
