from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.get_api_remote_tunnel_connect_token_response_200 import GetApiRemoteTunnelConnectTokenResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    target: UUID,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_target = str(target)
    params["target"] = json_target

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/remote/tunnel/connect-token",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | GetApiRemoteTunnelConnectTokenResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApiRemoteTunnelConnectTokenResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiError.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ApiError.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | GetApiRemoteTunnelConnectTokenResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    target: UUID,
) -> Response[ApiError | GetApiRemoteTunnelConnectTokenResponse200]:
    """
    Args:
        target (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | GetApiRemoteTunnelConnectTokenResponse200]
    """

    kwargs = _get_kwargs(
        target=target,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    target: UUID,
) -> ApiError | GetApiRemoteTunnelConnectTokenResponse200 | None:
    """
    Args:
        target (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | GetApiRemoteTunnelConnectTokenResponse200
    """

    return sync_detailed(
        client=client,
        target=target,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    target: UUID,
) -> Response[ApiError | GetApiRemoteTunnelConnectTokenResponse200]:
    """
    Args:
        target (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | GetApiRemoteTunnelConnectTokenResponse200]
    """

    kwargs = _get_kwargs(
        target=target,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    target: UUID,
) -> ApiError | GetApiRemoteTunnelConnectTokenResponse200 | None:
    """
    Args:
        target (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | GetApiRemoteTunnelConnectTokenResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            target=target,
        )
    ).parsed
