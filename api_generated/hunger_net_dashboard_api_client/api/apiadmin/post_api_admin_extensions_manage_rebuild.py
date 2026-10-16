from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_admin_extensions_manage_rebuild_response_200 import (
    PostApiAdminExtensionsManageRebuildResponse200,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    force: bool,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["force"] = force

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/admin/extensions/manage/rebuild",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PostApiAdminExtensionsManageRebuildResponse200 | None:
    if response.status_code == 200:
        response_200 = PostApiAdminExtensionsManageRebuildResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PostApiAdminExtensionsManageRebuildResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    force: bool,
) -> Response[PostApiAdminExtensionsManageRebuildResponse200]:
    """
    Args:
        force (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAdminExtensionsManageRebuildResponse200]
    """

    kwargs = _get_kwargs(
        force=force,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    force: bool,
) -> PostApiAdminExtensionsManageRebuildResponse200 | None:
    """
    Args:
        force (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAdminExtensionsManageRebuildResponse200
    """

    return sync_detailed(
        client=client,
        force=force,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    force: bool,
) -> Response[PostApiAdminExtensionsManageRebuildResponse200]:
    """
    Args:
        force (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiAdminExtensionsManageRebuildResponse200]
    """

    kwargs = _get_kwargs(
        force=force,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    force: bool,
) -> PostApiAdminExtensionsManageRebuildResponse200 | None:
    """
    Args:
        force (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiAdminExtensionsManageRebuildResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            force=force,
        )
    ).parsed
