from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.delete_api_client_account_two_factor_email_body import DeleteApiClientAccountTwoFactorEmailBody
from ...models.delete_api_client_account_two_factor_email_response_200 import (
    DeleteApiClientAccountTwoFactorEmailResponse200,
)
from ...types import Response


def _get_kwargs(
    *,
    body: DeleteApiClientAccountTwoFactorEmailBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/client/account/two-factor/email",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | DeleteApiClientAccountTwoFactorEmailResponse200 | None:
    if response.status_code == 200:
        response_200 = DeleteApiClientAccountTwoFactorEmailResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiError.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = ApiError.from_dict(response.json())

        return response_403

    if response.status_code == 409:
        response_409 = ApiError.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | DeleteApiClientAccountTwoFactorEmailResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DeleteApiClientAccountTwoFactorEmailBody,
) -> Response[ApiError | DeleteApiClientAccountTwoFactorEmailResponse200]:
    """
    Args:
        body (DeleteApiClientAccountTwoFactorEmailBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DeleteApiClientAccountTwoFactorEmailResponse200]
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
    body: DeleteApiClientAccountTwoFactorEmailBody,
) -> ApiError | DeleteApiClientAccountTwoFactorEmailResponse200 | None:
    """
    Args:
        body (DeleteApiClientAccountTwoFactorEmailBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DeleteApiClientAccountTwoFactorEmailResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DeleteApiClientAccountTwoFactorEmailBody,
) -> Response[ApiError | DeleteApiClientAccountTwoFactorEmailResponse200]:
    """
    Args:
        body (DeleteApiClientAccountTwoFactorEmailBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DeleteApiClientAccountTwoFactorEmailResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DeleteApiClientAccountTwoFactorEmailBody,
) -> ApiError | DeleteApiClientAccountTwoFactorEmailResponse200 | None:
    """
    Args:
        body (DeleteApiClientAccountTwoFactorEmailBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DeleteApiClientAccountTwoFactorEmailResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
