from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.exported_nest_egg import ExportedNestEgg
from ...models.post_api_admin_nests_nest_eggs_egg_update_import_response_200 import (
    PostApiAdminNestsNestEggsEggUpdateImportResponse200,
)
from ...types import Response


def _get_kwargs(
    nest: UUID,
    egg: UUID,
    *,
    body: ExportedNestEgg,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/admin/nests/{nest}/eggs/{egg}/update/import".format(
            nest=quote(str(nest), safe=""),
            egg=quote(str(egg), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PostApiAdminNestsNestEggsEggUpdateImportResponse200 | None:
    if response.status_code == 200:
        response_200 = PostApiAdminNestsNestEggsEggUpdateImportResponse200.from_dict(response.json())

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
) -> Response[ApiError | PostApiAdminNestsNestEggsEggUpdateImportResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    nest: UUID,
    egg: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: ExportedNestEgg,
) -> Response[ApiError | PostApiAdminNestsNestEggsEggUpdateImportResponse200]:
    """
    Args:
        nest (UUID):
        egg (UUID):
        body (ExportedNestEgg):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiAdminNestsNestEggsEggUpdateImportResponse200]
    """

    kwargs = _get_kwargs(
        nest=nest,
        egg=egg,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    nest: UUID,
    egg: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: ExportedNestEgg,
) -> ApiError | PostApiAdminNestsNestEggsEggUpdateImportResponse200 | None:
    """
    Args:
        nest (UUID):
        egg (UUID):
        body (ExportedNestEgg):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiAdminNestsNestEggsEggUpdateImportResponse200
    """

    return sync_detailed(
        nest=nest,
        egg=egg,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    nest: UUID,
    egg: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: ExportedNestEgg,
) -> Response[ApiError | PostApiAdminNestsNestEggsEggUpdateImportResponse200]:
    """
    Args:
        nest (UUID):
        egg (UUID):
        body (ExportedNestEgg):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiAdminNestsNestEggsEggUpdateImportResponse200]
    """

    kwargs = _get_kwargs(
        nest=nest,
        egg=egg,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    nest: UUID,
    egg: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: ExportedNestEgg,
) -> ApiError | PostApiAdminNestsNestEggsEggUpdateImportResponse200 | None:
    """
    Args:
        nest (UUID):
        egg (UUID):
        body (ExportedNestEgg):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiAdminNestsNestEggsEggUpdateImportResponse200
    """

    return (
        await asyncio_detailed(
            nest=nest,
            egg=egg,
            client=client,
            body=body,
        )
    ).parsed
