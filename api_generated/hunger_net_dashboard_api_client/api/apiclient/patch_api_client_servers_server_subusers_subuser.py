from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.patch_api_client_servers_server_subusers_subuser_body import (
    PatchApiClientServersServerSubusersSubuserBody,
)
from ...models.patch_api_client_servers_server_subusers_subuser_response_200 import (
    PatchApiClientServersServerSubusersSubuserResponse200,
)
from ...types import Response


def _get_kwargs(
    server: UUID,
    subuser: UUID,
    *,
    body: PatchApiClientServersServerSubusersSubuserBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/client/servers/{server}/subusers/{subuser}".format(
            server=quote(str(server), safe=""),
            subuser=quote(str(subuser), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PatchApiClientServersServerSubusersSubuserResponse200 | None:
    if response.status_code == 200:
        response_200 = PatchApiClientServersServerSubusersSubuserResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiError.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ApiError.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | PatchApiClientServersServerSubusersSubuserResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    server: UUID,
    subuser: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PatchApiClientServersServerSubusersSubuserBody,
) -> Response[ApiError | PatchApiClientServersServerSubusersSubuserResponse200]:
    """
    Args:
        server (UUID):
        subuser (UUID):
        body (PatchApiClientServersServerSubusersSubuserBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PatchApiClientServersServerSubusersSubuserResponse200]
    """

    kwargs = _get_kwargs(
        server=server,
        subuser=subuser,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    server: UUID,
    subuser: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PatchApiClientServersServerSubusersSubuserBody,
) -> ApiError | PatchApiClientServersServerSubusersSubuserResponse200 | None:
    """
    Args:
        server (UUID):
        subuser (UUID):
        body (PatchApiClientServersServerSubusersSubuserBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PatchApiClientServersServerSubusersSubuserResponse200
    """

    return sync_detailed(
        server=server,
        subuser=subuser,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    server: UUID,
    subuser: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PatchApiClientServersServerSubusersSubuserBody,
) -> Response[ApiError | PatchApiClientServersServerSubusersSubuserResponse200]:
    """
    Args:
        server (UUID):
        subuser (UUID):
        body (PatchApiClientServersServerSubusersSubuserBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PatchApiClientServersServerSubusersSubuserResponse200]
    """

    kwargs = _get_kwargs(
        server=server,
        subuser=subuser,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    server: UUID,
    subuser: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PatchApiClientServersServerSubusersSubuserBody,
) -> ApiError | PatchApiClientServersServerSubusersSubuserResponse200 | None:
    """
    Args:
        server (UUID):
        subuser (UUID):
        body (PatchApiClientServersServerSubusersSubuserBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PatchApiClientServersServerSubusersSubuserResponse200
    """

    return (
        await asyncio_detailed(
            server=server,
            subuser=subuser,
            client=client,
            body=body,
        )
    ).parsed
