from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.get_api_admin_users_user_response_200 import GetApiAdminUsersUserResponse200
from ...types import Response


def _get_kwargs(
    user: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/admin/users/{user}".format(
            user=quote(str(user), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | GetApiAdminUsersUserResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApiAdminUsersUserResponse200.from_dict(response.json())

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
) -> Response[ApiError | GetApiAdminUsersUserResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiError | GetApiAdminUsersUserResponse200]:
    """
    Args:
        user (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | GetApiAdminUsersUserResponse200]
    """

    kwargs = _get_kwargs(
        user=user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ApiError | GetApiAdminUsersUserResponse200 | None:
    """
    Args:
        user (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | GetApiAdminUsersUserResponse200
    """

    return sync_detailed(
        user=user,
        client=client,
    ).parsed


async def asyncio_detailed(
    user: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiError | GetApiAdminUsersUserResponse200]:
    """
    Args:
        user (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | GetApiAdminUsersUserResponse200]
    """

    kwargs = _get_kwargs(
        user=user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ApiError | GetApiAdminUsersUserResponse200 | None:
    """
    Args:
        user (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | GetApiAdminUsersUserResponse200
    """

    return (
        await asyncio_detailed(
            user=user,
            client=client,
        )
    ).parsed
