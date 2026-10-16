from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.post_api_client_account_api_keys_api_key_duplicate_body import (
    PostApiClientAccountApiKeysApiKeyDuplicateBody,
)
from ...models.post_api_client_account_api_keys_api_key_duplicate_response_200 import (
    PostApiClientAccountApiKeysApiKeyDuplicateResponse200,
)
from ...types import Response


def _get_kwargs(
    api_key: UUID,
    *,
    body: PostApiClientAccountApiKeysApiKeyDuplicateBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/client/account/api-keys/{api_key}/duplicate".format(
            api_key=quote(str(api_key), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PostApiClientAccountApiKeysApiKeyDuplicateResponse200 | None:
    if response.status_code == 200:
        response_200 = PostApiClientAccountApiKeysApiKeyDuplicateResponse200.from_dict(response.json())

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

    if response.status_code == 417:
        response_417 = ApiError.from_dict(response.json())

        return response_417

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | PostApiClientAccountApiKeysApiKeyDuplicateResponse200]:
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
    body: PostApiClientAccountApiKeysApiKeyDuplicateBody,
) -> Response[ApiError | PostApiClientAccountApiKeysApiKeyDuplicateResponse200]:
    """
    Args:
        api_key (UUID):
        body (PostApiClientAccountApiKeysApiKeyDuplicateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiClientAccountApiKeysApiKeyDuplicateResponse200]
    """

    kwargs = _get_kwargs(
        api_key=api_key,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    api_key: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiClientAccountApiKeysApiKeyDuplicateBody,
) -> ApiError | PostApiClientAccountApiKeysApiKeyDuplicateResponse200 | None:
    """
    Args:
        api_key (UUID):
        body (PostApiClientAccountApiKeysApiKeyDuplicateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiClientAccountApiKeysApiKeyDuplicateResponse200
    """

    return sync_detailed(
        api_key=api_key,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    api_key: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiClientAccountApiKeysApiKeyDuplicateBody,
) -> Response[ApiError | PostApiClientAccountApiKeysApiKeyDuplicateResponse200]:
    """
    Args:
        api_key (UUID):
        body (PostApiClientAccountApiKeysApiKeyDuplicateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiClientAccountApiKeysApiKeyDuplicateResponse200]
    """

    kwargs = _get_kwargs(
        api_key=api_key,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    api_key: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiClientAccountApiKeysApiKeyDuplicateBody,
) -> ApiError | PostApiClientAccountApiKeysApiKeyDuplicateResponse200 | None:
    """
    Args:
        api_key (UUID):
        body (PostApiClientAccountApiKeysApiKeyDuplicateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiClientAccountApiKeysApiKeyDuplicateResponse200
    """

    return (
        await asyncio_detailed(
            api_key=api_key,
            client=client,
            body=body,
        )
    ).parsed
