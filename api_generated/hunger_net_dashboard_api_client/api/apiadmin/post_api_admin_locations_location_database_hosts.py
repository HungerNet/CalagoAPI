from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.post_api_admin_locations_location_database_hosts_body import (
    PostApiAdminLocationsLocationDatabaseHostsBody,
)
from ...models.post_api_admin_locations_location_database_hosts_response_200 import (
    PostApiAdminLocationsLocationDatabaseHostsResponse200,
)
from ...types import Response


def _get_kwargs(
    location: UUID,
    *,
    body: PostApiAdminLocationsLocationDatabaseHostsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/admin/locations/{location}/database-hosts".format(
            location=quote(str(location), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PostApiAdminLocationsLocationDatabaseHostsResponse200 | None:
    if response.status_code == 200:
        response_200 = PostApiAdminLocationsLocationDatabaseHostsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ApiError.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | PostApiAdminLocationsLocationDatabaseHostsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    location: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiAdminLocationsLocationDatabaseHostsBody,
) -> Response[ApiError | PostApiAdminLocationsLocationDatabaseHostsResponse200]:
    """
    Args:
        location (UUID):
        body (PostApiAdminLocationsLocationDatabaseHostsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiAdminLocationsLocationDatabaseHostsResponse200]
    """

    kwargs = _get_kwargs(
        location=location,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    location: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiAdminLocationsLocationDatabaseHostsBody,
) -> ApiError | PostApiAdminLocationsLocationDatabaseHostsResponse200 | None:
    """
    Args:
        location (UUID):
        body (PostApiAdminLocationsLocationDatabaseHostsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiAdminLocationsLocationDatabaseHostsResponse200
    """

    return sync_detailed(
        location=location,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    location: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiAdminLocationsLocationDatabaseHostsBody,
) -> Response[ApiError | PostApiAdminLocationsLocationDatabaseHostsResponse200]:
    """
    Args:
        location (UUID):
        body (PostApiAdminLocationsLocationDatabaseHostsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiAdminLocationsLocationDatabaseHostsResponse200]
    """

    kwargs = _get_kwargs(
        location=location,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    location: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiAdminLocationsLocationDatabaseHostsBody,
) -> ApiError | PostApiAdminLocationsLocationDatabaseHostsResponse200 | None:
    """
    Args:
        location (UUID):
        body (PostApiAdminLocationsLocationDatabaseHostsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiAdminLocationsLocationDatabaseHostsResponse200
    """

    return (
        await asyncio_detailed(
            location=location,
            client=client,
            body=body,
        )
    ).parsed
