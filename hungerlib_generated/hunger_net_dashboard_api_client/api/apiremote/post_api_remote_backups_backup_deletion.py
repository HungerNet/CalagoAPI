from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.post_api_remote_backups_backup_deletion_body import PostApiRemoteBackupsBackupDeletionBody
from ...models.post_api_remote_backups_backup_deletion_response_200 import PostApiRemoteBackupsBackupDeletionResponse200
from ...types import Response


def _get_kwargs(
    backup: UUID,
    *,
    body: PostApiRemoteBackupsBackupDeletionBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/remote/backups/{backup}/deletion".format(
            backup=quote(str(backup), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PostApiRemoteBackupsBackupDeletionResponse200 | None:
    if response.status_code == 200:
        response_200 = PostApiRemoteBackupsBackupDeletionResponse200.from_dict(response.json())

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
) -> Response[ApiError | PostApiRemoteBackupsBackupDeletionResponse200]:
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
    body: PostApiRemoteBackupsBackupDeletionBody,
) -> Response[ApiError | PostApiRemoteBackupsBackupDeletionResponse200]:
    """
    Args:
        backup (UUID):
        body (PostApiRemoteBackupsBackupDeletionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiRemoteBackupsBackupDeletionResponse200]
    """

    kwargs = _get_kwargs(
        backup=backup,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    backup: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiRemoteBackupsBackupDeletionBody,
) -> ApiError | PostApiRemoteBackupsBackupDeletionResponse200 | None:
    """
    Args:
        backup (UUID):
        body (PostApiRemoteBackupsBackupDeletionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiRemoteBackupsBackupDeletionResponse200
    """

    return sync_detailed(
        backup=backup,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    backup: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiRemoteBackupsBackupDeletionBody,
) -> Response[ApiError | PostApiRemoteBackupsBackupDeletionResponse200]:
    """
    Args:
        backup (UUID):
        body (PostApiRemoteBackupsBackupDeletionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiRemoteBackupsBackupDeletionResponse200]
    """

    kwargs = _get_kwargs(
        backup=backup,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    backup: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiRemoteBackupsBackupDeletionBody,
) -> ApiError | PostApiRemoteBackupsBackupDeletionResponse200 | None:
    """
    Args:
        backup (UUID):
        body (PostApiRemoteBackupsBackupDeletionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiRemoteBackupsBackupDeletionResponse200
    """

    return (
        await asyncio_detailed(
            backup=backup,
            client=client,
            body=body,
        )
    ).parsed
