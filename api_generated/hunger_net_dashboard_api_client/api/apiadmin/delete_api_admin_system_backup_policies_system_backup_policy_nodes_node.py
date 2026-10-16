from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.delete_api_admin_system_backup_policies_system_backup_policy_nodes_node_response_200 import (
    DeleteApiAdminSystemBackupPoliciesSystemBackupPolicyNodesNodeResponse200,
)
from ...types import Response


def _get_kwargs(
    system_backup_policy: UUID,
    node: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/admin/system-backup-policies/{system_backup_policy}/nodes/{node}".format(
            system_backup_policy=quote(str(system_backup_policy), safe=""),
            node=quote(str(node), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | DeleteApiAdminSystemBackupPoliciesSystemBackupPolicyNodesNodeResponse200 | None:
    if response.status_code == 200:
        response_200 = DeleteApiAdminSystemBackupPoliciesSystemBackupPolicyNodesNodeResponse200.from_dict(
            response.json()
        )

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
) -> Response[ApiError | DeleteApiAdminSystemBackupPoliciesSystemBackupPolicyNodesNodeResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    system_backup_policy: UUID,
    node: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiError | DeleteApiAdminSystemBackupPoliciesSystemBackupPolicyNodesNodeResponse200]:
    """
    Args:
        system_backup_policy (UUID):
        node (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DeleteApiAdminSystemBackupPoliciesSystemBackupPolicyNodesNodeResponse200]
    """

    kwargs = _get_kwargs(
        system_backup_policy=system_backup_policy,
        node=node,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    system_backup_policy: UUID,
    node: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ApiError | DeleteApiAdminSystemBackupPoliciesSystemBackupPolicyNodesNodeResponse200 | None:
    """
    Args:
        system_backup_policy (UUID):
        node (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DeleteApiAdminSystemBackupPoliciesSystemBackupPolicyNodesNodeResponse200
    """

    return sync_detailed(
        system_backup_policy=system_backup_policy,
        node=node,
        client=client,
    ).parsed


async def asyncio_detailed(
    system_backup_policy: UUID,
    node: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiError | DeleteApiAdminSystemBackupPoliciesSystemBackupPolicyNodesNodeResponse200]:
    """
    Args:
        system_backup_policy (UUID):
        node (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DeleteApiAdminSystemBackupPoliciesSystemBackupPolicyNodesNodeResponse200]
    """

    kwargs = _get_kwargs(
        system_backup_policy=system_backup_policy,
        node=node,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    system_backup_policy: UUID,
    node: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ApiError | DeleteApiAdminSystemBackupPoliciesSystemBackupPolicyNodesNodeResponse200 | None:
    """
    Args:
        system_backup_policy (UUID):
        node (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DeleteApiAdminSystemBackupPoliciesSystemBackupPolicyNodesNodeResponse200
    """

    return (
        await asyncio_detailed(
            system_backup_policy=system_backup_policy,
            node=node,
            client=client,
        )
    ).parsed
