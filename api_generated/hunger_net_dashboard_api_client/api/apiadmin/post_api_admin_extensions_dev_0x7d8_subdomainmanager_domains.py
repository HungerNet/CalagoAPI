from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.post_api_admin_extensions_dev_0x7d8_subdomainmanager_domains_body import (
    PostApiAdminExtensionsDev0X7D8SubdomainmanagerDomainsBody,
)
from ...models.post_api_admin_extensions_dev_0x7d8_subdomainmanager_domains_response_200 import (
    PostApiAdminExtensionsDev0X7D8SubdomainmanagerDomainsResponse200,
)
from ...types import Response


def _get_kwargs(
    *,
    body: PostApiAdminExtensionsDev0X7D8SubdomainmanagerDomainsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/admin/extensions/dev.0x7d8.subdomainmanager/domains",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PostApiAdminExtensionsDev0X7D8SubdomainmanagerDomainsResponse200 | None:
    if response.status_code == 200:
        response_200 = PostApiAdminExtensionsDev0X7D8SubdomainmanagerDomainsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiError.from_dict(response.json())

        return response_401

    if response.status_code == 409:
        response_409 = ApiError.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | PostApiAdminExtensionsDev0X7D8SubdomainmanagerDomainsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostApiAdminExtensionsDev0X7D8SubdomainmanagerDomainsBody,
) -> Response[ApiError | PostApiAdminExtensionsDev0X7D8SubdomainmanagerDomainsResponse200]:
    """
    Args:
        body (PostApiAdminExtensionsDev0X7D8SubdomainmanagerDomainsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiAdminExtensionsDev0X7D8SubdomainmanagerDomainsResponse200]
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
    body: PostApiAdminExtensionsDev0X7D8SubdomainmanagerDomainsBody,
) -> ApiError | PostApiAdminExtensionsDev0X7D8SubdomainmanagerDomainsResponse200 | None:
    """
    Args:
        body (PostApiAdminExtensionsDev0X7D8SubdomainmanagerDomainsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiAdminExtensionsDev0X7D8SubdomainmanagerDomainsResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostApiAdminExtensionsDev0X7D8SubdomainmanagerDomainsBody,
) -> Response[ApiError | PostApiAdminExtensionsDev0X7D8SubdomainmanagerDomainsResponse200]:
    """
    Args:
        body (PostApiAdminExtensionsDev0X7D8SubdomainmanagerDomainsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiAdminExtensionsDev0X7D8SubdomainmanagerDomainsResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostApiAdminExtensionsDev0X7D8SubdomainmanagerDomainsBody,
) -> ApiError | PostApiAdminExtensionsDev0X7D8SubdomainmanagerDomainsResponse200 | None:
    """
    Args:
        body (PostApiAdminExtensionsDev0X7D8SubdomainmanagerDomainsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiAdminExtensionsDev0X7D8SubdomainmanagerDomainsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
