from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.post_api_admin_oauth_providers_discover_body import PostApiAdminOauthProvidersDiscoverBody
from ...models.post_api_admin_oauth_providers_discover_response_200 import PostApiAdminOauthProvidersDiscoverResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: PostApiAdminOauthProvidersDiscoverBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/admin/oauth-providers/discover",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PostApiAdminOauthProvidersDiscoverResponse200 | None:
    if response.status_code == 200:
        response_200 = PostApiAdminOauthProvidersDiscoverResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiError.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | PostApiAdminOauthProvidersDiscoverResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostApiAdminOauthProvidersDiscoverBody,
) -> Response[ApiError | PostApiAdminOauthProvidersDiscoverResponse200]:
    """
    Args:
        body (PostApiAdminOauthProvidersDiscoverBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiAdminOauthProvidersDiscoverResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: PostApiAdminOauthProvidersDiscoverBody,
) -> ApiError | PostApiAdminOauthProvidersDiscoverResponse200 | None:
    """
    Args:
        body (PostApiAdminOauthProvidersDiscoverBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiAdminOauthProvidersDiscoverResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostApiAdminOauthProvidersDiscoverBody,
) -> Response[ApiError | PostApiAdminOauthProvidersDiscoverResponse200]:
    """
    Args:
        body (PostApiAdminOauthProvidersDiscoverBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiAdminOauthProvidersDiscoverResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostApiAdminOauthProvidersDiscoverBody,
) -> ApiError | PostApiAdminOauthProvidersDiscoverResponse200 | None:
    """
    Args:
        body (PostApiAdminOauthProvidersDiscoverBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiAdminOauthProvidersDiscoverResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
