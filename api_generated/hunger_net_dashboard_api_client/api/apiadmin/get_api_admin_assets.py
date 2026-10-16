from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.get_api_admin_assets_response_200 import GetApiAdminAssetsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int,
    per_page: int,
    directory: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params["directory"] = directory

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/admin/assets",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | GetApiAdminAssetsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApiAdminAssetsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiError.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | GetApiAdminAssetsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int,
    per_page: int,
    directory: str | Unset = UNSET,
) -> Response[ApiError | GetApiAdminAssetsResponse200]:
    """
    Args:
        page (int):
        per_page (int):
        directory (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | GetApiAdminAssetsResponse200]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        directory=directory,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page: int,
    per_page: int,
    directory: str | Unset = UNSET,
) -> ApiError | GetApiAdminAssetsResponse200 | None:
    """
    Args:
        page (int):
        per_page (int):
        directory (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | GetApiAdminAssetsResponse200
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        directory=directory,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int,
    per_page: int,
    directory: str | Unset = UNSET,
) -> Response[ApiError | GetApiAdminAssetsResponse200]:
    """
    Args:
        page (int):
        per_page (int):
        directory (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | GetApiAdminAssetsResponse200]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        directory=directory,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int,
    per_page: int,
    directory: str | Unset = UNSET,
) -> ApiError | GetApiAdminAssetsResponse200 | None:
    """
    Args:
        page (int):
        per_page (int):
        directory (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | GetApiAdminAssetsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            directory=directory,
        )
    ).parsed
