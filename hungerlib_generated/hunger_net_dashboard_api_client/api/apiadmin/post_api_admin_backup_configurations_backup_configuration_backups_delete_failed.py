from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.post_api_admin_backup_configurations_backup_configuration_backups_delete_failed_body import (
    PostApiAdminBackupConfigurationsBackupConfigurationBackupsDeleteFailedBody,
)
from ...models.post_api_admin_backup_configurations_backup_configuration_backups_delete_failed_response_200 import (
    PostApiAdminBackupConfigurationsBackupConfigurationBackupsDeleteFailedResponse200,
)
from ...types import Response


def _get_kwargs(
    backup_configuration: UUID,
    *,
    body: PostApiAdminBackupConfigurationsBackupConfigurationBackupsDeleteFailedBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/admin/backup-configurations/{backup_configuration}/backups/delete-failed".format(
            backup_configuration=quote(str(backup_configuration), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PostApiAdminBackupConfigurationsBackupConfigurationBackupsDeleteFailedResponse200 | None:
    if response.status_code == 200:
        response_200 = PostApiAdminBackupConfigurationsBackupConfigurationBackupsDeleteFailedResponse200.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 401:
        response_401 = ApiError.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ApiError.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | PostApiAdminBackupConfigurationsBackupConfigurationBackupsDeleteFailedResponse200]:
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
    body: PostApiAdminBackupConfigurationsBackupConfigurationBackupsDeleteFailedBody,
) -> Response[ApiError | PostApiAdminBackupConfigurationsBackupConfigurationBackupsDeleteFailedResponse200]:
    """
    Args:
        backup_configuration (UUID):
        body (PostApiAdminBackupConfigurationsBackupConfigurationBackupsDeleteFailedBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiAdminBackupConfigurationsBackupConfigurationBackupsDeleteFailedResponse200]
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
    body: PostApiAdminBackupConfigurationsBackupConfigurationBackupsDeleteFailedBody,
) -> ApiError | PostApiAdminBackupConfigurationsBackupConfigurationBackupsDeleteFailedResponse200 | None:
    """
    Args:
        backup_configuration (UUID):
        body (PostApiAdminBackupConfigurationsBackupConfigurationBackupsDeleteFailedBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiAdminBackupConfigurationsBackupConfigurationBackupsDeleteFailedResponse200
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
    body: PostApiAdminBackupConfigurationsBackupConfigurationBackupsDeleteFailedBody,
) -> Response[ApiError | PostApiAdminBackupConfigurationsBackupConfigurationBackupsDeleteFailedResponse200]:
    """
    Args:
        backup_configuration (UUID):
        body (PostApiAdminBackupConfigurationsBackupConfigurationBackupsDeleteFailedBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiAdminBackupConfigurationsBackupConfigurationBackupsDeleteFailedResponse200]
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
    body: PostApiAdminBackupConfigurationsBackupConfigurationBackupsDeleteFailedBody,
) -> ApiError | PostApiAdminBackupConfigurationsBackupConfigurationBackupsDeleteFailedResponse200 | None:
    """
    Args:
        backup_configuration (UUID):
        body (PostApiAdminBackupConfigurationsBackupConfigurationBackupsDeleteFailedBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiAdminBackupConfigurationsBackupConfigurationBackupsDeleteFailedResponse200
    """

    return (
        await asyncio_detailed(
            backup_configuration=backup_configuration,
            client=client,
            body=body,
        )
    ).parsed
