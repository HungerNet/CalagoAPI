from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.get_api_admin_backup_configurations_backup_configuration_locations_response_200 import (
    GetApiAdminBackupConfigurationsBackupConfigurationLocationsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    backup_configuration: UUID,
    *,
    page: int,
    per_page: int,
    search: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params["search"] = search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/admin/backup-configurations/{backup_configuration}/locations".format(
            backup_configuration=quote(str(backup_configuration), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | GetApiAdminBackupConfigurationsBackupConfigurationLocationsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApiAdminBackupConfigurationsBackupConfigurationLocationsResponse200.from_dict(response.json())

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
) -> Response[ApiError | GetApiAdminBackupConfigurationsBackupConfigurationLocationsResponse200]:
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
    page: int,
    per_page: int,
    search: str | Unset = UNSET,
) -> Response[ApiError | GetApiAdminBackupConfigurationsBackupConfigurationLocationsResponse200]:
    """
    Args:
        backup_configuration (UUID):
        page (int):
        per_page (int):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | GetApiAdminBackupConfigurationsBackupConfigurationLocationsResponse200]
    """

    kwargs = _get_kwargs(
        backup_configuration=backup_configuration,
        page=page,
        per_page=per_page,
        search=search,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    backup_configuration: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int,
    per_page: int,
    search: str | Unset = UNSET,
) -> ApiError | GetApiAdminBackupConfigurationsBackupConfigurationLocationsResponse200 | None:
    """
    Args:
        backup_configuration (UUID):
        page (int):
        per_page (int):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | GetApiAdminBackupConfigurationsBackupConfigurationLocationsResponse200
    """

    return sync_detailed(
        backup_configuration=backup_configuration,
        client=client,
        page=page,
        per_page=per_page,
        search=search,
    ).parsed


async def asyncio_detailed(
    backup_configuration: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int,
    per_page: int,
    search: str | Unset = UNSET,
) -> Response[ApiError | GetApiAdminBackupConfigurationsBackupConfigurationLocationsResponse200]:
    """
    Args:
        backup_configuration (UUID):
        page (int):
        per_page (int):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | GetApiAdminBackupConfigurationsBackupConfigurationLocationsResponse200]
    """

    kwargs = _get_kwargs(
        backup_configuration=backup_configuration,
        page=page,
        per_page=per_page,
        search=search,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    backup_configuration: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int,
    per_page: int,
    search: str | Unset = UNSET,
) -> ApiError | GetApiAdminBackupConfigurationsBackupConfigurationLocationsResponse200 | None:
    """
    Args:
        backup_configuration (UUID):
        page (int):
        per_page (int):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | GetApiAdminBackupConfigurationsBackupConfigurationLocationsResponse200
    """

    return (
        await asyncio_detailed(
            backup_configuration=backup_configuration,
            client=client,
            page=page,
            per_page=per_page,
            search=search,
        )
    ).parsed
