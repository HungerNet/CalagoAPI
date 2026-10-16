from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_client_account_oauth_links_response_200 import GetApiClientAccountOauthLinksResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    page: int,
    per_page: int,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/client/account/oauth-links",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetApiClientAccountOauthLinksResponse200 | None:
    if response.status_code == 200:
        response_200 = GetApiClientAccountOauthLinksResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetApiClientAccountOauthLinksResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int,
    per_page: int,
) -> Response[GetApiClientAccountOauthLinksResponse200]:
    """
    Args:
        page (int):
        per_page (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiClientAccountOauthLinksResponse200]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page: int,
    per_page: int,
) -> GetApiClientAccountOauthLinksResponse200 | None:
    """
    Args:
        page (int):
        per_page (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiClientAccountOauthLinksResponse200
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int,
    per_page: int,
) -> Response[GetApiClientAccountOauthLinksResponse200]:
    """
    Args:
        page (int):
        per_page (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiClientAccountOauthLinksResponse200]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int,
    per_page: int,
) -> GetApiClientAccountOauthLinksResponse200 | None:
    """
    Args:
        page (int):
        per_page (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiClientAccountOauthLinksResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
        )
    ).parsed
