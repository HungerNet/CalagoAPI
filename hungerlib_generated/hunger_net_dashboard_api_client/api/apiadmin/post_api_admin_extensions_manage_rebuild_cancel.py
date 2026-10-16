from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_admin_extensions_manage_rebuild_cancel_response_200 import (
    PostApiAdminExtensionsManageRebuildCancelResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    build_id: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["build_id"] = build_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/admin/extensions/manage/rebuild/cancel",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PostApiAdminExtensionsManageRebuildCancelResponse200 | None:
    if response.status_code == 200:
        response_200 = PostApiAdminExtensionsManageRebuildCancelResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PostApiAdminExtensionsManageRebuildCancelResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    build_id: int | Unset = UNSET,
) -> Response[PostApiAdminExtensionsManageRebuildCancelResponse200]:
    """
    Args:
        build_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAdminExtensionsManageRebuildCancelResponse200]
    """

    kwargs = _get_kwargs(
        build_id=build_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    build_id: int | Unset = UNSET,
) -> PostApiAdminExtensionsManageRebuildCancelResponse200 | None:
    """
    Args:
        build_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAdminExtensionsManageRebuildCancelResponse200
    """

    return sync_detailed(
        client=client,
        build_id=build_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    build_id: int | Unset = UNSET,
) -> Response[PostApiAdminExtensionsManageRebuildCancelResponse200]:
    """
    Args:
        build_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAdminExtensionsManageRebuildCancelResponse200]
    """

    kwargs = _get_kwargs(
        build_id=build_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    build_id: int | Unset = UNSET,
) -> PostApiAdminExtensionsManageRebuildCancelResponse200 | None:
    """
    Args:
        build_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAdminExtensionsManageRebuildCancelResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            build_id=build_id,
        )
    ).parsed
