from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...types import UNSET, Response


def _get_kwargs(
    backup: UUID,
    *,
    instance: UUID,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_instance = str(instance)
    params["instance"] = json_instance

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/remote/backups/{backup}/database/source".format(
            backup=quote(str(backup), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiError | str | None:
    if response.status_code == 200:
        response_200 = response.text
        return response_200

    if response.status_code == 400:
        response_400 = ApiError.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ApiError.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ApiError.from_dict(response.json())

        return response_409

    if response.status_code == 417:
        response_417 = ApiError.from_dict(response.json())

        return response_417

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiError | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    backup: UUID,
    *,
    client: AuthenticatedClient | Client,
    instance: UUID,
) -> Response[ApiError | str]:
    """
    Args:
        backup (UUID):
        instance (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | str]
    """

    kwargs = _get_kwargs(
        backup=backup,
        instance=instance,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    backup: UUID,
    *,
    client: AuthenticatedClient | Client,
    instance: UUID,
) -> ApiError | str | None:
    """
    Args:
        backup (UUID):
        instance (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | str
    """

    return sync_detailed(
        backup=backup,
        client=client,
        instance=instance,
    ).parsed


async def asyncio_detailed(
    backup: UUID,
    *,
    client: AuthenticatedClient | Client,
    instance: UUID,
) -> Response[ApiError | str]:
    """
    Args:
        backup (UUID):
        instance (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | str]
    """

    kwargs = _get_kwargs(
        backup=backup,
        instance=instance,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    backup: UUID,
    *,
    client: AuthenticatedClient | Client,
    instance: UUID,
) -> ApiError | str | None:
    """
    Args:
        backup (UUID):
        instance (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | str
    """

    return (
        await asyncio_detailed(
            backup=backup,
            client=client,
            instance=instance,
        )
    ).parsed
