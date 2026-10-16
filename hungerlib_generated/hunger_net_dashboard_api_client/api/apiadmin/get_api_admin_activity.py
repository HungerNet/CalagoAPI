from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_admin_activity_response_200 import GetApiAdminActivityResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user: UUID | Unset = UNSET,
    page: int,
    per_page: int,
    search: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_user: str | Unset = UNSET
    if not isinstance(user, Unset):
        json_user = str(user)
    params["user"] = json_user

    params["page"] = page

    params["per_page"] = per_page

    params["search"] = search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/admin/activity",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApiAdminActivityResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApiAdminActivityResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApiAdminActivityResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    user: UUID | Unset = UNSET,
    page: int,
    per_page: int,
    search: str | Unset = UNSET,
) -> Response[GetApiAdminActivityResponse200]:
    """
    Args:
        user (UUID | Unset):
        page (int):
        per_page (int):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiAdminActivityResponse200]
    """

    kwargs = _get_kwargs(
        user=user,
        page=page,
        per_page=per_page,
        search=search,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    user: UUID | Unset = UNSET,
    page: int,
    per_page: int,
    search: str | Unset = UNSET,
) -> GetApiAdminActivityResponse200 | None:
    """
    Args:
        user (UUID | Unset):
        page (int):
        per_page (int):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiAdminActivityResponse200
    """

    return sync_detailed(
        client=client,
        user=user,
        page=page,
        per_page=per_page,
        search=search,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    user: UUID | Unset = UNSET,
    page: int,
    per_page: int,
    search: str | Unset = UNSET,
) -> Response[GetApiAdminActivityResponse200]:
    """
    Args:
        user (UUID | Unset):
        page (int):
        per_page (int):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiAdminActivityResponse200]
    """

    kwargs = _get_kwargs(
        user=user,
        page=page,
        per_page=per_page,
        search=search,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    user: UUID | Unset = UNSET,
    page: int,
    per_page: int,
    search: str | Unset = UNSET,
) -> GetApiAdminActivityResponse200 | None:
    """
    Args:
        user (UUID | Unset):
        page (int):
        per_page (int):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiAdminActivityResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            user=user,
            page=page,
            per_page=per_page,
            search=search,
        )
    ).parsed
