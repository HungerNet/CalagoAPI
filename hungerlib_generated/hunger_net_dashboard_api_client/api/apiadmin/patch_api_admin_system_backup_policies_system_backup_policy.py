from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.patch_api_admin_system_backup_policies_system_backup_policy_body import (
    PatchApiAdminSystemBackupPoliciesSystemBackupPolicyBody,
)
from ...models.patch_api_admin_system_backup_policies_system_backup_policy_response_200 import (
    PatchApiAdminSystemBackupPoliciesSystemBackupPolicyResponse200,
)
from ...types import Response


def _get_kwargs(
    system_backup_policy: UUID,
    *,
    body: PatchApiAdminSystemBackupPoliciesSystemBackupPolicyBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/admin/system-backup-policies/{system_backup_policy}".format(
            system_backup_policy=quote(str(system_backup_policy), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PatchApiAdminSystemBackupPoliciesSystemBackupPolicyResponse200 | None:
    if response.status_code == 200:
        response_200 = PatchApiAdminSystemBackupPoliciesSystemBackupPolicyResponse200.from_dict(response.json())

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
) -> Response[ApiError | PatchApiAdminSystemBackupPoliciesSystemBackupPolicyResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    system_backup_policy: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PatchApiAdminSystemBackupPoliciesSystemBackupPolicyBody,
) -> Response[ApiError | PatchApiAdminSystemBackupPoliciesSystemBackupPolicyResponse200]:
    """
    Args:
        system_backup_policy (UUID):
        body (PatchApiAdminSystemBackupPoliciesSystemBackupPolicyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PatchApiAdminSystemBackupPoliciesSystemBackupPolicyResponse200]
    """

    kwargs = _get_kwargs(
        system_backup_policy=system_backup_policy,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    system_backup_policy: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PatchApiAdminSystemBackupPoliciesSystemBackupPolicyBody,
) -> ApiError | PatchApiAdminSystemBackupPoliciesSystemBackupPolicyResponse200 | None:
    """
    Args:
        system_backup_policy (UUID):
        body (PatchApiAdminSystemBackupPoliciesSystemBackupPolicyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PatchApiAdminSystemBackupPoliciesSystemBackupPolicyResponse200
    """

    return sync_detailed(
        system_backup_policy=system_backup_policy,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    system_backup_policy: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PatchApiAdminSystemBackupPoliciesSystemBackupPolicyBody,
) -> Response[ApiError | PatchApiAdminSystemBackupPoliciesSystemBackupPolicyResponse200]:
    """
    Args:
        system_backup_policy (UUID):
        body (PatchApiAdminSystemBackupPoliciesSystemBackupPolicyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PatchApiAdminSystemBackupPoliciesSystemBackupPolicyResponse200]
    """

    kwargs = _get_kwargs(
        system_backup_policy=system_backup_policy,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    system_backup_policy: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PatchApiAdminSystemBackupPoliciesSystemBackupPolicyBody,
) -> ApiError | PatchApiAdminSystemBackupPoliciesSystemBackupPolicyResponse200 | None:
    """
    Args:
        system_backup_policy (UUID):
        body (PatchApiAdminSystemBackupPoliciesSystemBackupPolicyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PatchApiAdminSystemBackupPoliciesSystemBackupPolicyResponse200
    """

    return (
        await asyncio_detailed(
            system_backup_policy=system_backup_policy,
            client=client,
            body=body,
        )
    ).parsed
