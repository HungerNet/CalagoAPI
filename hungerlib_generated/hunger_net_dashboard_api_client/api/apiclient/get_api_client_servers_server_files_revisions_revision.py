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
    server: UUID,
    revision: int,
    *,
    file: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["file"] = file

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/client/servers/{server}/files/revisions/{revision}".format(
            server=quote(str(server), safe=""),
            revision=quote(str(revision), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiError | str | None:
    if response.status_code == 200:
        response_200 = response.text
        return response_200

    if response.status_code == 401:
        response_401 = ApiError.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ApiError.from_dict(response.json())

        return response_404

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
    server: UUID,
    revision: int,
    *,
    client: AuthenticatedClient | Client,
    file: str,
) -> Response[ApiError | str]:
    """
    Args:
        server (UUID):
        revision (int):
        file (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | str]
    """

    kwargs = _get_kwargs(
        server=server,
        revision=revision,
        file=file,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    server: UUID,
    revision: int,
    *,
    client: AuthenticatedClient | Client,
    file: str,
) -> ApiError | str | None:
    """
    Args:
        server (UUID):
        revision (int):
        file (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | str
    """

    return sync_detailed(
        server=server,
        revision=revision,
        client=client,
        file=file,
    ).parsed


async def asyncio_detailed(
    server: UUID,
    revision: int,
    *,
    client: AuthenticatedClient | Client,
    file: str,
) -> Response[ApiError | str]:
    """
    Args:
        server (UUID):
        revision (int):
        file (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | str]
    """

    kwargs = _get_kwargs(
        server=server,
        revision=revision,
        file=file,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    server: UUID,
    revision: int,
    *,
    client: AuthenticatedClient | Client,
    file: str,
) -> ApiError | str | None:
    """
    Args:
        server (UUID):
        revision (int):
        file (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | str
    """

    return (
        await asyncio_detailed(
            server=server,
            revision=revision,
            client=client,
            file=file,
        )
    ).parsed
