from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.put_api_admin_system_email_variables_name_body import PutApiAdminSystemEmailVariablesNameBody
from ...models.put_api_admin_system_email_variables_name_response_200 import (
    PutApiAdminSystemEmailVariablesNameResponse200,
)
from ...types import Response


def _get_kwargs(
    name: str,
    *,
    body: PutApiAdminSystemEmailVariablesNameBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/admin/system/email/variables/{name}".format(
            name=quote(str(name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PutApiAdminSystemEmailVariablesNameResponse200 | None:
    if response.status_code == 200:
        response_200 = PutApiAdminSystemEmailVariablesNameResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiError.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ApiError.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | PutApiAdminSystemEmailVariablesNameResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutApiAdminSystemEmailVariablesNameBody,
) -> Response[ApiError | PutApiAdminSystemEmailVariablesNameResponse200]:
    """
    Args:
        name (str):
        body (PutApiAdminSystemEmailVariablesNameBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PutApiAdminSystemEmailVariablesNameResponse200]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutApiAdminSystemEmailVariablesNameBody,
) -> ApiError | PutApiAdminSystemEmailVariablesNameResponse200 | None:
    """
    Args:
        name (str):
        body (PutApiAdminSystemEmailVariablesNameBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PutApiAdminSystemEmailVariablesNameResponse200
    """

    return sync_detailed(
        name=name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutApiAdminSystemEmailVariablesNameBody,
) -> Response[ApiError | PutApiAdminSystemEmailVariablesNameResponse200]:
    """
    Args:
        name (str):
        body (PutApiAdminSystemEmailVariablesNameBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PutApiAdminSystemEmailVariablesNameResponse200]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutApiAdminSystemEmailVariablesNameBody,
) -> ApiError | PutApiAdminSystemEmailVariablesNameResponse200 | None:
    """
    Args:
        name (str):
        body (PutApiAdminSystemEmailVariablesNameBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PutApiAdminSystemEmailVariablesNameResponse200
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            body=body,
        )
    ).parsed
