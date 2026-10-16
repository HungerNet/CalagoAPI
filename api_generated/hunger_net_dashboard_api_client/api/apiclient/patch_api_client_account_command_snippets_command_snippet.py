from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_api_client_account_command_snippets_command_snippet_body import (
    PatchApiClientAccountCommandSnippetsCommandSnippetBody,
)
from ...models.patch_api_client_account_command_snippets_command_snippet_response_200 import (
    PatchApiClientAccountCommandSnippetsCommandSnippetResponse200,
)
from ...types import Response


def _get_kwargs(
    command_snippet: UUID,
    *,
    body: PatchApiClientAccountCommandSnippetsCommandSnippetBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/client/account/command-snippets/{command_snippet}".format(
            command_snippet=quote(str(command_snippet), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PatchApiClientAccountCommandSnippetsCommandSnippetResponse200 | None:
    if response.status_code == 200:
        response_200 = PatchApiClientAccountCommandSnippetsCommandSnippetResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PatchApiClientAccountCommandSnippetsCommandSnippetResponse200]:
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
    body: PatchApiClientAccountCommandSnippetsCommandSnippetBody,
) -> Response[PatchApiClientAccountCommandSnippetsCommandSnippetResponse200]:
    """
    Args:
        command_snippet (UUID):
        body (PatchApiClientAccountCommandSnippetsCommandSnippetBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchApiClientAccountCommandSnippetsCommandSnippetResponse200]
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
    body: PatchApiClientAccountCommandSnippetsCommandSnippetBody,
) -> PatchApiClientAccountCommandSnippetsCommandSnippetResponse200 | None:
    """
    Args:
        command_snippet (UUID):
        body (PatchApiClientAccountCommandSnippetsCommandSnippetBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchApiClientAccountCommandSnippetsCommandSnippetResponse200
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
    body: PatchApiClientAccountCommandSnippetsCommandSnippetBody,
) -> Response[PatchApiClientAccountCommandSnippetsCommandSnippetResponse200]:
    """
    Args:
        command_snippet (UUID):
        body (PatchApiClientAccountCommandSnippetsCommandSnippetBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchApiClientAccountCommandSnippetsCommandSnippetResponse200]
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
    body: PatchApiClientAccountCommandSnippetsCommandSnippetBody,
) -> PatchApiClientAccountCommandSnippetsCommandSnippetResponse200 | None:
    """
    Args:
        command_snippet (UUID):
        body (PatchApiClientAccountCommandSnippetsCommandSnippetBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchApiClientAccountCommandSnippetsCommandSnippetResponse200
    """

    return (
        await asyncio_detailed(
            command_snippet=command_snippet,
            client=client,
            body=body,
        )
    ).parsed
