from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.patch_api_client_servers_server_subdomains_subdomain_body import (
    PatchApiClientServersServerSubdomainsSubdomainBody,
)
from ...models.patch_api_client_servers_server_subdomains_subdomain_response_200 import (
    PatchApiClientServersServerSubdomainsSubdomainResponse200,
)
from ...types import Response


def _get_kwargs(
    server: UUID,
    subdomain: UUID,
    *,
    body: PatchApiClientServersServerSubdomainsSubdomainBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/client/servers/{server}/subdomains/{subdomain}".format(
            server=quote(str(server), safe=""),
            subdomain=quote(str(subdomain), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PatchApiClientServersServerSubdomainsSubdomainResponse200 | None:
    if response.status_code == 200:
        response_200 = PatchApiClientServersServerSubdomainsSubdomainResponse200.from_dict(response.json())

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
) -> Response[ApiError | PatchApiClientServersServerSubdomainsSubdomainResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    server: UUID,
    subdomain: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PatchApiClientServersServerSubdomainsSubdomainBody,
) -> Response[ApiError | PatchApiClientServersServerSubdomainsSubdomainResponse200]:
    """
    Args:
        server (UUID):
        subdomain (UUID):
        body (PatchApiClientServersServerSubdomainsSubdomainBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PatchApiClientServersServerSubdomainsSubdomainResponse200]
    """

    kwargs = _get_kwargs(
        server=server,
        subdomain=subdomain,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    server: UUID,
    subdomain: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PatchApiClientServersServerSubdomainsSubdomainBody,
) -> ApiError | PatchApiClientServersServerSubdomainsSubdomainResponse200 | None:
    """
    Args:
        server (UUID):
        subdomain (UUID):
        body (PatchApiClientServersServerSubdomainsSubdomainBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PatchApiClientServersServerSubdomainsSubdomainResponse200
    """

    return sync_detailed(
        server=server,
        subdomain=subdomain,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    server: UUID,
    subdomain: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PatchApiClientServersServerSubdomainsSubdomainBody,
) -> Response[ApiError | PatchApiClientServersServerSubdomainsSubdomainResponse200]:
    """
    Args:
        server (UUID):
        subdomain (UUID):
        body (PatchApiClientServersServerSubdomainsSubdomainBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PatchApiClientServersServerSubdomainsSubdomainResponse200]
    """

    kwargs = _get_kwargs(
        server=server,
        subdomain=subdomain,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    server: UUID,
    subdomain: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PatchApiClientServersServerSubdomainsSubdomainBody,
) -> ApiError | PatchApiClientServersServerSubdomainsSubdomainResponse200 | None:
    """
    Args:
        server (UUID):
        subdomain (UUID):
        body (PatchApiClientServersServerSubdomainsSubdomainBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PatchApiClientServersServerSubdomainsSubdomainResponse200
    """

    return (
        await asyncio_detailed(
            server=server,
            subdomain=subdomain,
            client=client,
            body=body,
        )
    ).parsed
