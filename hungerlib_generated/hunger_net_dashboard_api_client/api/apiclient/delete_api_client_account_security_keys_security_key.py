from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.delete_api_client_account_security_keys_security_key_body import (
    DeleteApiClientAccountSecurityKeysSecurityKeyBody,
)
from ...models.delete_api_client_account_security_keys_security_key_response_200 import (
    DeleteApiClientAccountSecurityKeysSecurityKeyResponse200,
)
from ...types import Response


def _get_kwargs(
    security_key: UUID,
    *,
    body: DeleteApiClientAccountSecurityKeysSecurityKeyBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/client/account/security-keys/{security_key}".format(
            security_key=quote(str(security_key), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | DeleteApiClientAccountSecurityKeysSecurityKeyResponse200 | None:
    if response.status_code == 200:
        response_200 = DeleteApiClientAccountSecurityKeysSecurityKeyResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiError.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = ApiError.from_dict(response.json())

        return response_403

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
) -> Response[ApiError | DeleteApiClientAccountSecurityKeysSecurityKeyResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    security_key: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: DeleteApiClientAccountSecurityKeysSecurityKeyBody,
) -> Response[ApiError | DeleteApiClientAccountSecurityKeysSecurityKeyResponse200]:
    """
    Args:
        security_key (UUID):
        body (DeleteApiClientAccountSecurityKeysSecurityKeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DeleteApiClientAccountSecurityKeysSecurityKeyResponse200]
    """

    kwargs = _get_kwargs(
        security_key=security_key,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    security_key: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: DeleteApiClientAccountSecurityKeysSecurityKeyBody,
) -> ApiError | DeleteApiClientAccountSecurityKeysSecurityKeyResponse200 | None:
    """
    Args:
        security_key (UUID):
        body (DeleteApiClientAccountSecurityKeysSecurityKeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DeleteApiClientAccountSecurityKeysSecurityKeyResponse200
    """

    return sync_detailed(
        security_key=security_key,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    security_key: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: DeleteApiClientAccountSecurityKeysSecurityKeyBody,
) -> Response[ApiError | DeleteApiClientAccountSecurityKeysSecurityKeyResponse200]:
    """
    Args:
        security_key (UUID):
        body (DeleteApiClientAccountSecurityKeysSecurityKeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DeleteApiClientAccountSecurityKeysSecurityKeyResponse200]
    """

    kwargs = _get_kwargs(
        security_key=security_key,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    security_key: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: DeleteApiClientAccountSecurityKeysSecurityKeyBody,
) -> ApiError | DeleteApiClientAccountSecurityKeysSecurityKeyResponse200 | None:
    """
    Args:
        security_key (UUID):
        body (DeleteApiClientAccountSecurityKeysSecurityKeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DeleteApiClientAccountSecurityKeysSecurityKeyResponse200
    """

    return (
        await asyncio_detailed(
            security_key=security_key,
            client=client,
            body=body,
        )
    ).parsed
