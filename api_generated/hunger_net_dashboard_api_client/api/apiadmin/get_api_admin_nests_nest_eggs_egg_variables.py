from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_admin_nests_nest_eggs_egg_variables_response_200 import (
    GetApiAdminNestsNestEggsEggVariablesResponse200,
)
from ...types import Response


def _get_kwargs(
    nest: UUID,
    egg: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/admin/nests/{nest}/eggs/{egg}/variables".format(
            nest=quote(str(nest), safe=""),
            egg=quote(str(egg), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApiAdminNestsNestEggsEggVariablesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApiAdminNestsNestEggsEggVariablesResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApiAdminNestsNestEggsEggVariablesResponse200]:
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
) -> Response[GetApiAdminNestsNestEggsEggVariablesResponse200]:
    """
    Args:
        nest (UUID):
        egg (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiAdminNestsNestEggsEggVariablesResponse200]
    """

    kwargs = _get_kwargs(
        nest=nest,
        egg=egg,
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
) -> GetApiAdminNestsNestEggsEggVariablesResponse200 | None:
    """
    Args:
        nest (UUID):
        egg (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiAdminNestsNestEggsEggVariablesResponse200
    """

    return sync_detailed(
        nest=nest,
        egg=egg,
        client=client,
    ).parsed


async def asyncio_detailed(
    nest: UUID,
    egg: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetApiAdminNestsNestEggsEggVariablesResponse200]:
    """
    Args:
        nest (UUID):
        egg (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiAdminNestsNestEggsEggVariablesResponse200]
    """

    kwargs = _get_kwargs(
        nest=nest,
        egg=egg,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    nest: UUID,
    egg: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> GetApiAdminNestsNestEggsEggVariablesResponse200 | None:
    """
    Args:
        nest (UUID):
        egg (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiAdminNestsNestEggsEggVariablesResponse200
    """

    return (
        await asyncio_detailed(
            nest=nest,
            egg=egg,
            client=client,
        )
    ).parsed
