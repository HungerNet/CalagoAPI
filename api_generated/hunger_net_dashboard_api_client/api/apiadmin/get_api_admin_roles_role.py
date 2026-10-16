from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.get_api_admin_roles_role_response_200 import GetApiAdminRolesRoleResponse200
from ...types import Response


def _get_kwargs(
    role: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/admin/roles/{role}".format(
            role=quote(str(role), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | GetApiAdminRolesRoleResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApiAdminRolesRoleResponse200.from_dict(response.json())

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
) -> Response[ApiError | GetApiAdminRolesRoleResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    role: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiError | GetApiAdminRolesRoleResponse200]:
    """
    Args:
        role (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | GetApiAdminRolesRoleResponse200]
    """

    kwargs = _get_kwargs(
        role=role,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    role: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ApiError | GetApiAdminRolesRoleResponse200 | None:
    """
    Args:
        role (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | GetApiAdminRolesRoleResponse200
    """

    return sync_detailed(
        role=role,
        client=client,
    ).parsed


async def asyncio_detailed(
    role: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiError | GetApiAdminRolesRoleResponse200]:
    """
    Args:
        role (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | GetApiAdminRolesRoleResponse200]
    """

    kwargs = _get_kwargs(
        role=role,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    role: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ApiError | GetApiAdminRolesRoleResponse200 | None:
    """
    Args:
        role (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | GetApiAdminRolesRoleResponse200
    """

    return (
        await asyncio_detailed(
            role=role,
            client=client,
        )
    ).parsed
