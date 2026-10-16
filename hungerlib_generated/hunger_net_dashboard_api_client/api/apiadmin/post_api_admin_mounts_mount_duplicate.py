from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.post_api_admin_mounts_mount_duplicate_body import PostApiAdminMountsMountDuplicateBody
from ...models.post_api_admin_mounts_mount_duplicate_response_200 import PostApiAdminMountsMountDuplicateResponse200
from ...types import Response


def _get_kwargs(
    mount: UUID,
    *,
    body: PostApiAdminMountsMountDuplicateBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/admin/mounts/{mount}/duplicate".format(
            mount=quote(str(mount), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PostApiAdminMountsMountDuplicateResponse200 | None:
    if response.status_code == 200:
        response_200 = PostApiAdminMountsMountDuplicateResponse200.from_dict(response.json())

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
) -> Response[ApiError | PostApiAdminMountsMountDuplicateResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    mount: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiAdminMountsMountDuplicateBody,
) -> Response[ApiError | PostApiAdminMountsMountDuplicateResponse200]:
    """
    Args:
        mount (UUID):
        body (PostApiAdminMountsMountDuplicateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiAdminMountsMountDuplicateResponse200]
    """

    kwargs = _get_kwargs(
        mount=mount,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    mount: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiAdminMountsMountDuplicateBody,
) -> ApiError | PostApiAdminMountsMountDuplicateResponse200 | None:
    """
    Args:
        mount (UUID):
        body (PostApiAdminMountsMountDuplicateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiAdminMountsMountDuplicateResponse200
    """

    return sync_detailed(
        mount=mount,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    mount: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiAdminMountsMountDuplicateBody,
) -> Response[ApiError | PostApiAdminMountsMountDuplicateResponse200]:
    """
    Args:
        mount (UUID):
        body (PostApiAdminMountsMountDuplicateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiAdminMountsMountDuplicateResponse200]
    """

    kwargs = _get_kwargs(
        mount=mount,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    mount: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiAdminMountsMountDuplicateBody,
) -> ApiError | PostApiAdminMountsMountDuplicateResponse200 | None:
    """
    Args:
        mount (UUID):
        body (PostApiAdminMountsMountDuplicateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiAdminMountsMountDuplicateResponse200
    """

    return (
        await asyncio_detailed(
            mount=mount,
            client=client,
            body=body,
        )
    ).parsed
