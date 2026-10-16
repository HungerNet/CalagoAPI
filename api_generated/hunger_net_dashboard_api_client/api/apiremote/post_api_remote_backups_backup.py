from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.post_api_remote_backups_backup_body import PostApiRemoteBackupsBackupBody
from ...models.post_api_remote_backups_backup_response_200 import PostApiRemoteBackupsBackupResponse200
from ...types import Response


def _get_kwargs(
    backup: UUID,
    *,
    body: PostApiRemoteBackupsBackupBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/remote/backups/{backup}".format(
            backup=quote(str(backup), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PostApiRemoteBackupsBackupResponse200 | None:
    if response.status_code == 200:
        response_200 = PostApiRemoteBackupsBackupResponse200.from_dict(response.json())

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
) -> Response[ApiError | PostApiRemoteBackupsBackupResponse200]:
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
    body: PostApiRemoteBackupsBackupBody,
) -> Response[ApiError | PostApiRemoteBackupsBackupResponse200]:
    """
    Args:
        backup (UUID):
        body (PostApiRemoteBackupsBackupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiRemoteBackupsBackupResponse200]
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
    body: PostApiRemoteBackupsBackupBody,
) -> ApiError | PostApiRemoteBackupsBackupResponse200 | None:
    """
    Args:
        backup (UUID):
        body (PostApiRemoteBackupsBackupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiRemoteBackupsBackupResponse200
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
    body: PostApiRemoteBackupsBackupBody,
) -> Response[ApiError | PostApiRemoteBackupsBackupResponse200]:
    """
    Args:
        backup (UUID):
        body (PostApiRemoteBackupsBackupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiRemoteBackupsBackupResponse200]
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
    body: PostApiRemoteBackupsBackupBody,
) -> ApiError | PostApiRemoteBackupsBackupResponse200 | None:
    """
    Args:
        backup (UUID):
        body (PostApiRemoteBackupsBackupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiRemoteBackupsBackupResponse200
    """

    return (
        await asyncio_detailed(
            backup=backup,
            client=client,
            body=body,
        )
    ).parsed
