from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_admin_extensions_manage_logs_response_200 import GetApiAdminExtensionsManageLogsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    build_id: int | Unset = UNSET,
    from_offset: int,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["build_id"] = build_id

    params["from_offset"] = from_offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/admin/extensions/manage/logs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApiAdminExtensionsManageLogsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApiAdminExtensionsManageLogsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApiAdminExtensionsManageLogsResponse200]:
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
    from_offset: int,
) -> Response[GetApiAdminExtensionsManageLogsResponse200]:
    """
    Args:
        build_id (int | Unset):
        from_offset (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiAdminExtensionsManageLogsResponse200]
    """

    kwargs = _get_kwargs(
        build_id=build_id,
        from_offset=from_offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    build_id: int | Unset = UNSET,
    from_offset: int,
) -> GetApiAdminExtensionsManageLogsResponse200 | None:
    """
    Args:
        build_id (int | Unset):
        from_offset (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiAdminExtensionsManageLogsResponse200
    """

    return sync_detailed(
        client=client,
        build_id=build_id,
        from_offset=from_offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    build_id: int | Unset = UNSET,
    from_offset: int,
) -> Response[GetApiAdminExtensionsManageLogsResponse200]:
    """
    Args:
        build_id (int | Unset):
        from_offset (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiAdminExtensionsManageLogsResponse200]
    """

    kwargs = _get_kwargs(
        build_id=build_id,
        from_offset=from_offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    build_id: int | Unset = UNSET,
    from_offset: int,
) -> GetApiAdminExtensionsManageLogsResponse200 | None:
    """
    Args:
        build_id (int | Unset):
        from_offset (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiAdminExtensionsManageLogsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            build_id=build_id,
            from_offset=from_offset,
        )
    ).parsed
