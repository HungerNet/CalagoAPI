from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.post_api_admin_egg_repositories_egg_repository_eggs_install_body import (
    PostApiAdminEggRepositoriesEggRepositoryEggsInstallBody,
)
from ...models.post_api_admin_egg_repositories_egg_repository_eggs_install_response_200 import (
    PostApiAdminEggRepositoriesEggRepositoryEggsInstallResponse200,
)
from ...types import Response


def _get_kwargs(
    egg_repository: UUID,
    *,
    body: PostApiAdminEggRepositoriesEggRepositoryEggsInstallBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/admin/egg-repositories/{egg_repository}/eggs/install".format(
            egg_repository=quote(str(egg_repository), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PostApiAdminEggRepositoriesEggRepositoryEggsInstallResponse200 | None:
    if response.status_code == 200:
        response_200 = PostApiAdminEggRepositoriesEggRepositoryEggsInstallResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ApiError.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | PostApiAdminEggRepositoriesEggRepositoryEggsInstallResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    egg_repository: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiAdminEggRepositoriesEggRepositoryEggsInstallBody,
) -> Response[ApiError | PostApiAdminEggRepositoriesEggRepositoryEggsInstallResponse200]:
    """
    Args:
        egg_repository (UUID):
        body (PostApiAdminEggRepositoriesEggRepositoryEggsInstallBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiAdminEggRepositoriesEggRepositoryEggsInstallResponse200]
    """

    kwargs = _get_kwargs(
        egg_repository=egg_repository,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    egg_repository: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiAdminEggRepositoriesEggRepositoryEggsInstallBody,
) -> ApiError | PostApiAdminEggRepositoriesEggRepositoryEggsInstallResponse200 | None:
    """
    Args:
        egg_repository (UUID):
        body (PostApiAdminEggRepositoriesEggRepositoryEggsInstallBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiAdminEggRepositoriesEggRepositoryEggsInstallResponse200
    """

    return sync_detailed(
        egg_repository=egg_repository,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    egg_repository: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiAdminEggRepositoriesEggRepositoryEggsInstallBody,
) -> Response[ApiError | PostApiAdminEggRepositoriesEggRepositoryEggsInstallResponse200]:
    """
    Args:
        egg_repository (UUID):
        body (PostApiAdminEggRepositoriesEggRepositoryEggsInstallBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PostApiAdminEggRepositoriesEggRepositoryEggsInstallResponse200]
    """

    kwargs = _get_kwargs(
        egg_repository=egg_repository,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    egg_repository: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiAdminEggRepositoriesEggRepositoryEggsInstallBody,
) -> ApiError | PostApiAdminEggRepositoriesEggRepositoryEggsInstallResponse200 | None:
    """
    Args:
        egg_repository (UUID):
        body (PostApiAdminEggRepositoriesEggRepositoryEggsInstallBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PostApiAdminEggRepositoriesEggRepositoryEggsInstallResponse200
    """

    return (
        await asyncio_detailed(
            egg_repository=egg_repository,
            client=client,
            body=body,
        )
    ).parsed
