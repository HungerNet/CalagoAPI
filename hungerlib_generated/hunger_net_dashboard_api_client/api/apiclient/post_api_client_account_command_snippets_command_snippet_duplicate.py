from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.post_api_client_account_command_snippets_command_snippet_duplicate_body import (
    PostApiClientAccountCommandSnippetsCommandSnippetDuplicateBody,
)
from ...models.post_api_client_account_command_snippets_command_snippet_duplicate_response_200 import (
    PostApiClientAccountCommandSnippetsCommandSnippetDuplicateResponse200,
)
from ...types import Response


def _get_kwargs(
    command_snippet: UUID,
    *,
    body: PostApiClientAccountCommandSnippetsCommandSnippetDuplicateBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/client/account/command-snippets/{command_snippet}/duplicate".format(
            command_snippet=quote(str(command_snippet), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PostApiClientAccountCommandSnippetsCommandSnippetDuplicateResponse200 | None:
    if response.status_code == 200:
        response_200 = PostApiClientAccountCommandSnippetsCommandSnippetDuplicateResponse200.from_dict(response.json())

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

    if response.status_code == 417:
        response_417 = ApiError.from_dict(response.json())

        return response_417

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | PostApiClientAccountCommandSnippetsCommandSnippetDuplicateResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    command_snippet: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiClientAccountCommandSnippetsCommandSnippetDuplicateBody,
) -> Response[ApiError | PostApiClientAccountCommandSnippetsCommandSnippetDuplicateResponse200]:
    """
    Args:
        command_snippet (UUID):
        body (PostApiClientAccountCommandSnippetsCommandSnippetDuplicateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiClientAccountCommandSnippetsCommandSnippetDuplicateResponse200]
    """

    kwargs = _get_kwargs(
        command_snippet=command_snippet,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    command_snippet: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiClientAccountCommandSnippetsCommandSnippetDuplicateBody,
) -> ApiError | PostApiClientAccountCommandSnippetsCommandSnippetDuplicateResponse200 | None:
    """
    Args:
        command_snippet (UUID):
        body (PostApiClientAccountCommandSnippetsCommandSnippetDuplicateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiClientAccountCommandSnippetsCommandSnippetDuplicateResponse200
    """

    return sync_detailed(
        command_snippet=command_snippet,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    command_snippet: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiClientAccountCommandSnippetsCommandSnippetDuplicateBody,
) -> Response[ApiError | PostApiClientAccountCommandSnippetsCommandSnippetDuplicateResponse200]:
    """
    Args:
        command_snippet (UUID):
        body (PostApiClientAccountCommandSnippetsCommandSnippetDuplicateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiClientAccountCommandSnippetsCommandSnippetDuplicateResponse200]
    """

    kwargs = _get_kwargs(
        command_snippet=command_snippet,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    command_snippet: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiClientAccountCommandSnippetsCommandSnippetDuplicateBody,
) -> ApiError | PostApiClientAccountCommandSnippetsCommandSnippetDuplicateResponse200 | None:
    """
    Args:
        command_snippet (UUID):
        body (PostApiClientAccountCommandSnippetsCommandSnippetDuplicateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiClientAccountCommandSnippetsCommandSnippetDuplicateResponse200
    """

    return (
        await asyncio_detailed(
            command_snippet=command_snippet,
            client=client,
            body=body,
        )
    ).parsed
