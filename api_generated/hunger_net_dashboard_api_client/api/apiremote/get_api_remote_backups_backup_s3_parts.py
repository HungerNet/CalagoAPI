from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.get_api_remote_backups_backup_s3_parts_response_200 import GetApiRemoteBackupsBackupS3PartsResponse200
from ...types import UNSET, Response


def _get_kwargs(
    backup: UUID,
    *,
    from_part: int,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["from_part"] = from_part

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/remote/backups/{backup}/s3/parts".format(
            backup=quote(str(backup), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | GetApiRemoteBackupsBackupS3PartsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApiRemoteBackupsBackupS3PartsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 417:
        response_417 = ApiError.from_dict(response.json())

        return response_417

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | GetApiRemoteBackupsBackupS3PartsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    backup: UUID,
    *,
    client: AuthenticatedClient | Client,
    from_part: int,
) -> Response[ApiError | GetApiRemoteBackupsBackupS3PartsResponse200]:
    """
    Args:
        backup (UUID):
        from_part (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | GetApiRemoteBackupsBackupS3PartsResponse200]
    """

    kwargs = _get_kwargs(
        backup=backup,
        from_part=from_part,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    backup: UUID,
    *,
    client: AuthenticatedClient | Client,
    from_part: int,
) -> ApiError | GetApiRemoteBackupsBackupS3PartsResponse200 | None:
    """
    Args:
        backup (UUID):
        from_part (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | GetApiRemoteBackupsBackupS3PartsResponse200
    """

    return sync_detailed(
        backup=backup,
        client=client,
        from_part=from_part,
    ).parsed


async def asyncio_detailed(
    backup: UUID,
    *,
    client: AuthenticatedClient | Client,
    from_part: int,
) -> Response[ApiError | GetApiRemoteBackupsBackupS3PartsResponse200]:
    """
    Args:
        backup (UUID):
        from_part (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | GetApiRemoteBackupsBackupS3PartsResponse200]
    """

    kwargs = _get_kwargs(
        backup=backup,
        from_part=from_part,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    backup: UUID,
    *,
    client: AuthenticatedClient | Client,
    from_part: int,
) -> ApiError | GetApiRemoteBackupsBackupS3PartsResponse200 | None:
    """
    Args:
        backup (UUID):
        from_part (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | GetApiRemoteBackupsBackupS3PartsResponse200
    """

    return (
        await asyncio_detailed(
            backup=backup,
            client=client,
            from_part=from_part,
        )
    ).parsed
