from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.post_api_admin_egg_configurations_egg_configuration_duplicate_body import (
    PostApiAdminEggConfigurationsEggConfigurationDuplicateBody,
)
from ...types import Response


def _get_kwargs(
    egg_configuration: UUID,
    *,
    body: PostApiAdminEggConfigurationsEggConfigurationDuplicateBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/admin/egg-configurations/{egg_configuration}/duplicate".format(
            egg_configuration=quote(str(egg_configuration), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiError | None:
    if response.status_code == 400:
        response_400 = ApiError.from_dict(response.json())

        return response_400

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    egg_configuration: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiAdminEggConfigurationsEggConfigurationDuplicateBody,
) -> Response[ApiError]:
    """
    Args:
        egg_configuration (UUID):
        body (PostApiAdminEggConfigurationsEggConfigurationDuplicateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError]
    """

    kwargs = _get_kwargs(
        egg_configuration=egg_configuration,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    egg_configuration: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiAdminEggConfigurationsEggConfigurationDuplicateBody,
) -> ApiError | None:
    """
    Args:
        egg_configuration (UUID):
        body (PostApiAdminEggConfigurationsEggConfigurationDuplicateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError
    """

    return sync_detailed(
        egg_configuration=egg_configuration,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    egg_configuration: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiAdminEggConfigurationsEggConfigurationDuplicateBody,
) -> Response[ApiError]:
    """
    Args:
        egg_configuration (UUID):
        body (PostApiAdminEggConfigurationsEggConfigurationDuplicateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError]
    """

    kwargs = _get_kwargs(
        egg_configuration=egg_configuration,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    egg_configuration: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiAdminEggConfigurationsEggConfigurationDuplicateBody,
) -> ApiError | None:
    """
    Args:
        egg_configuration (UUID):
        body (PostApiAdminEggConfigurationsEggConfigurationDuplicateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError
    """

    return (
        await asyncio_detailed(
            egg_configuration=egg_configuration,
            client=client,
            body=body,
        )
    ).parsed
