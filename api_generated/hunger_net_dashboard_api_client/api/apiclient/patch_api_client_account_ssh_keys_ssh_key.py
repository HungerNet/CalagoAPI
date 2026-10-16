from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.patch_api_client_account_ssh_keys_ssh_key_body import PatchApiClientAccountSshKeysSshKeyBody
from ...models.patch_api_client_account_ssh_keys_ssh_key_response_200 import (
    PatchApiClientAccountSshKeysSshKeyResponse200,
)
from ...types import Response


def _get_kwargs(
    ssh_key: UUID,
    *,
    body: PatchApiClientAccountSshKeysSshKeyBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/client/account/ssh-keys/{ssh_key}".format(
            ssh_key=quote(str(ssh_key), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PatchApiClientAccountSshKeysSshKeyResponse200 | None:
    if response.status_code == 200:
        response_200 = PatchApiClientAccountSshKeysSshKeyResponse200.from_dict(response.json())

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
) -> Response[ApiError | PatchApiClientAccountSshKeysSshKeyResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ssh_key: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PatchApiClientAccountSshKeysSshKeyBody,
) -> Response[ApiError | PatchApiClientAccountSshKeysSshKeyResponse200]:
    """
    Args:
        ssh_key (UUID):
        body (PatchApiClientAccountSshKeysSshKeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PatchApiClientAccountSshKeysSshKeyResponse200]
    """

    kwargs = _get_kwargs(
        ssh_key=ssh_key,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ssh_key: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PatchApiClientAccountSshKeysSshKeyBody,
) -> ApiError | PatchApiClientAccountSshKeysSshKeyResponse200 | None:
    """
    Args:
        ssh_key (UUID):
        body (PatchApiClientAccountSshKeysSshKeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PatchApiClientAccountSshKeysSshKeyResponse200
    """

    return sync_detailed(
        ssh_key=ssh_key,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    ssh_key: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PatchApiClientAccountSshKeysSshKeyBody,
) -> Response[ApiError | PatchApiClientAccountSshKeysSshKeyResponse200]:
    """
    Args:
        ssh_key (UUID):
        body (PatchApiClientAccountSshKeysSshKeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PatchApiClientAccountSshKeysSshKeyResponse200]
    """

    kwargs = _get_kwargs(
        ssh_key=ssh_key,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ssh_key: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PatchApiClientAccountSshKeysSshKeyBody,
) -> ApiError | PatchApiClientAccountSshKeysSshKeyResponse200 | None:
    """
    Args:
        ssh_key (UUID):
        body (PatchApiClientAccountSshKeysSshKeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PatchApiClientAccountSshKeysSshKeyResponse200
    """

    return (
        await asyncio_detailed(
            ssh_key=ssh_key,
            client=client,
            body=body,
        )
    ).parsed
