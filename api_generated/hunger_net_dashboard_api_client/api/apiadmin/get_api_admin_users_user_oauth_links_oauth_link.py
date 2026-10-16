from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.get_api_admin_users_user_oauth_links_oauth_link_response_200 import (
    GetApiAdminUsersUserOauthLinksOauthLinkResponse200,
)
from ...types import Response


def _get_kwargs(
    user: UUID,
    oauth_link: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/admin/users/{user}/oauth-links/{oauth_link}".format(
            user=quote(str(user), safe=""),
            oauth_link=quote(str(oauth_link), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | GetApiAdminUsersUserOauthLinksOauthLinkResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApiAdminUsersUserOauthLinksOauthLinkResponse200.from_dict(response.json())

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
) -> Response[ApiError | GetApiAdminUsersUserOauthLinksOauthLinkResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user: UUID,
    oauth_link: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiError | GetApiAdminUsersUserOauthLinksOauthLinkResponse200]:
    """
    Args:
        user (UUID):
        oauth_link (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | GetApiAdminUsersUserOauthLinksOauthLinkResponse200]
    """

    kwargs = _get_kwargs(
        user=user,
        oauth_link=oauth_link,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user: UUID,
    oauth_link: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ApiError | GetApiAdminUsersUserOauthLinksOauthLinkResponse200 | None:
    """
    Args:
        user (UUID):
        oauth_link (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | GetApiAdminUsersUserOauthLinksOauthLinkResponse200
    """

    return sync_detailed(
        user=user,
        oauth_link=oauth_link,
        client=client,
    ).parsed


async def asyncio_detailed(
    user: UUID,
    oauth_link: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiError | GetApiAdminUsersUserOauthLinksOauthLinkResponse200]:
    """
    Args:
        user (UUID):
        oauth_link (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | GetApiAdminUsersUserOauthLinksOauthLinkResponse200]
    """

    kwargs = _get_kwargs(
        user=user,
        oauth_link=oauth_link,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user: UUID,
    oauth_link: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ApiError | GetApiAdminUsersUserOauthLinksOauthLinkResponse200 | None:
    """
    Args:
        user (UUID):
        oauth_link (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | GetApiAdminUsersUserOauthLinksOauthLinkResponse200
    """

    return (
        await asyncio_detailed(
            user=user,
            oauth_link=oauth_link,
            client=client,
        )
    ).parsed
