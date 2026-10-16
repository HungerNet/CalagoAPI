from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.delete_api_client_account_api_keys_api_key_response_200 import (
    DeleteApiClientAccountApiKeysApiKeyResponse200,
)
from ...types import Response


def _get_kwargs(
    api_key: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/client/account/api-keys/{api_key}".format(
            api_key=quote(str(api_key), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | DeleteApiClientAccountApiKeysApiKeyResponse200 | None:
    if response.status_code == 200:
        response_200 = DeleteApiClientAccountApiKeysApiKeyResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = ApiError.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ApiError.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | DeleteApiClientAccountApiKeysApiKeyResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    api_key: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiError | DeleteApiClientAccountApiKeysApiKeyResponse200]:
    """
    Args:
        api_key (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DeleteApiClientAccountApiKeysApiKeyResponse200]
    """

    kwargs = _get_kwargs(
        api_key=api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    api_key: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ApiError | DeleteApiClientAccountApiKeysApiKeyResponse200 | None:
    """
    Args:
        api_key (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DeleteApiClientAccountApiKeysApiKeyResponse200
    """

    return sync_detailed(
        api_key=api_key,
        client=client,
    ).parsed


async def asyncio_detailed(
    api_key: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiError | DeleteApiClientAccountApiKeysApiKeyResponse200]:
    """
    Args:
        api_key (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DeleteApiClientAccountApiKeysApiKeyResponse200]
    """

    kwargs = _get_kwargs(
        api_key=api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    api_key: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ApiError | DeleteApiClientAccountApiKeysApiKeyResponse200 | None:
    """
    Args:
        api_key (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DeleteApiClientAccountApiKeysApiKeyResponse200
    """

    return (
        await asyncio_detailed(
            api_key=api_key,
            client=client,
        )
    ).parsed
