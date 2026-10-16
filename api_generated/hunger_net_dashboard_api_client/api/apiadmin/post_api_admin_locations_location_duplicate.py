from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.post_api_admin_locations_location_duplicate_body import PostApiAdminLocationsLocationDuplicateBody
from ...models.post_api_admin_locations_location_duplicate_response_200 import (
    PostApiAdminLocationsLocationDuplicateResponse200,
)
from ...types import Response


def _get_kwargs(
    location: UUID,
    *,
    body: PostApiAdminLocationsLocationDuplicateBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/admin/locations/{location}/duplicate".format(
            location=quote(str(location), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PostApiAdminLocationsLocationDuplicateResponse200 | None:
    if response.status_code == 200:
        response_200 = PostApiAdminLocationsLocationDuplicateResponse200.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | PostApiAdminLocationsLocationDuplicateResponse200]:
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
    body: PostApiAdminLocationsLocationDuplicateBody,
) -> Response[ApiError | PostApiAdminLocationsLocationDuplicateResponse200]:
    """
    Args:
        location (UUID):
        body (PostApiAdminLocationsLocationDuplicateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiAdminLocationsLocationDuplicateResponse200]
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
    body: PostApiAdminLocationsLocationDuplicateBody,
) -> ApiError | PostApiAdminLocationsLocationDuplicateResponse200 | None:
    """
    Args:
        location (UUID):
        body (PostApiAdminLocationsLocationDuplicateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiAdminLocationsLocationDuplicateResponse200
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
    body: PostApiAdminLocationsLocationDuplicateBody,
) -> Response[ApiError | PostApiAdminLocationsLocationDuplicateResponse200]:
    """
    Args:
        location (UUID):
        body (PostApiAdminLocationsLocationDuplicateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiAdminLocationsLocationDuplicateResponse200]
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
    body: PostApiAdminLocationsLocationDuplicateBody,
) -> ApiError | PostApiAdminLocationsLocationDuplicateResponse200 | None:
    """
    Args:
        location (UUID):
        body (PostApiAdminLocationsLocationDuplicateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiAdminLocationsLocationDuplicateResponse200
    """

    return (
        await asyncio_detailed(
            location=location,
            client=client,
            body=body,
        )
    ).parsed
