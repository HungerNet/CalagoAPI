from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.get_api_admin_oauth_providers_oauth_provider_users_response_200 import (
    GetApiAdminOauthProvidersOauthProviderUsersResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    oauth_provider: UUID,
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
        "url": "/api/admin/oauth-providers/{oauth_provider}/users".format(
            oauth_provider=quote(str(oauth_provider), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | GetApiAdminOauthProvidersOauthProviderUsersResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApiAdminOauthProvidersOauthProviderUsersResponse200.from_dict(response.json())

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
) -> Response[ApiError | GetApiAdminOauthProvidersOauthProviderUsersResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    oauth_provider: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int,
    per_page: int,
    search: str | Unset = UNSET,
) -> Response[ApiError | GetApiAdminOauthProvidersOauthProviderUsersResponse200]:
    """
    Args:
        oauth_provider (UUID):
        page (int):
        per_page (int):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | GetApiAdminOauthProvidersOauthProviderUsersResponse200]
    """

    kwargs = _get_kwargs(
        oauth_provider=oauth_provider,
        page=page,
        per_page=per_page,
        search=search,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    oauth_provider: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int,
    per_page: int,
    search: str | Unset = UNSET,
) -> ApiError | GetApiAdminOauthProvidersOauthProviderUsersResponse200 | None:
    """
    Args:
        oauth_provider (UUID):
        page (int):
        per_page (int):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | GetApiAdminOauthProvidersOauthProviderUsersResponse200
    """

    return sync_detailed(
        oauth_provider=oauth_provider,
        client=client,
        page=page,
        per_page=per_page,
        search=search,
    ).parsed


async def asyncio_detailed(
    oauth_provider: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int,
    per_page: int,
    search: str | Unset = UNSET,
) -> Response[ApiError | GetApiAdminOauthProvidersOauthProviderUsersResponse200]:
    """
    Args:
        oauth_provider (UUID):
        page (int):
        per_page (int):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | GetApiAdminOauthProvidersOauthProviderUsersResponse200]
    """

    kwargs = _get_kwargs(
        oauth_provider=oauth_provider,
        page=page,
        per_page=per_page,
        search=search,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    oauth_provider: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int,
    per_page: int,
    search: str | Unset = UNSET,
) -> ApiError | GetApiAdminOauthProvidersOauthProviderUsersResponse200 | None:
    """
    Args:
        oauth_provider (UUID):
        page (int):
        per_page (int):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | GetApiAdminOauthProvidersOauthProviderUsersResponse200
    """

    return (
        await asyncio_detailed(
            oauth_provider=oauth_provider,
            client=client,
            page=page,
            per_page=per_page,
            search=search,
        )
    ).parsed
