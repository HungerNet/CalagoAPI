from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.delete_api_client_account_two_factor_body import DeleteApiClientAccountTwoFactorBody
from ...models.delete_api_client_account_two_factor_response_200 import DeleteApiClientAccountTwoFactorResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: DeleteApiClientAccountTwoFactorBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/client/account/two-factor",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | DeleteApiClientAccountTwoFactorResponse200 | None:
    if response.status_code == 200:
        response_200 = DeleteApiClientAccountTwoFactorResponse200.from_dict(response.json())

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
) -> Response[ApiError | DeleteApiClientAccountTwoFactorResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DeleteApiClientAccountTwoFactorBody,
) -> Response[ApiError | DeleteApiClientAccountTwoFactorResponse200]:
    """
    Args:
        body (DeleteApiClientAccountTwoFactorBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DeleteApiClientAccountTwoFactorResponse200]
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
    body: DeleteApiClientAccountTwoFactorBody,
) -> ApiError | DeleteApiClientAccountTwoFactorResponse200 | None:
    """
    Args:
        body (DeleteApiClientAccountTwoFactorBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DeleteApiClientAccountTwoFactorResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DeleteApiClientAccountTwoFactorBody,
) -> Response[ApiError | DeleteApiClientAccountTwoFactorResponse200]:
    """
    Args:
        body (DeleteApiClientAccountTwoFactorBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DeleteApiClientAccountTwoFactorResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DeleteApiClientAccountTwoFactorBody,
) -> ApiError | DeleteApiClientAccountTwoFactorResponse200 | None:
    """
    Args:
        body (DeleteApiClientAccountTwoFactorBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DeleteApiClientAccountTwoFactorResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
