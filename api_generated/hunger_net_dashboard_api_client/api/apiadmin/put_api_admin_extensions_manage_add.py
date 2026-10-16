from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_api_admin_extensions_manage_add_response_200 import PutApiAdminExtensionsManageAddResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    accept_license: bool,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accept_license"] = accept_license

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/admin/extensions/manage/add",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PutApiAdminExtensionsManageAddResponse200 | None:
    if response.status_code == 200:
        response_200 = PutApiAdminExtensionsManageAddResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PutApiAdminExtensionsManageAddResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    accept_license: bool,
) -> Response[PutApiAdminExtensionsManageAddResponse200]:
    """
    Args:
        accept_license (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutApiAdminExtensionsManageAddResponse200]
    """

    kwargs = _get_kwargs(
        accept_license=accept_license,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    accept_license: bool,
) -> PutApiAdminExtensionsManageAddResponse200 | None:
    """
    Args:
        accept_license (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutApiAdminExtensionsManageAddResponse200
    """

    return sync_detailed(
        client=client,
        accept_license=accept_license,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    accept_license: bool,
) -> Response[PutApiAdminExtensionsManageAddResponse200]:
    """
    Args:
        accept_license (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutApiAdminExtensionsManageAddResponse200]
    """

    kwargs = _get_kwargs(
        accept_license=accept_license,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    accept_license: bool,
) -> PutApiAdminExtensionsManageAddResponse200 | None:
    """
    Args:
        accept_license (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutApiAdminExtensionsManageAddResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            accept_license=accept_license,
        )
    ).parsed
