from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.put_api_admin_system_email_templates_identifier_body import PutApiAdminSystemEmailTemplatesIdentifierBody
from ...models.put_api_admin_system_email_templates_identifier_response_200 import (
    PutApiAdminSystemEmailTemplatesIdentifierResponse200,
)
from ...types import Response


def _get_kwargs(
    identifier: str,
    *,
    body: PutApiAdminSystemEmailTemplatesIdentifierBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/admin/system/email/templates/{identifier}".format(
            identifier=quote(str(identifier), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PutApiAdminSystemEmailTemplatesIdentifierResponse200 | None:
    if response.status_code == 200:
        response_200 = PutApiAdminSystemEmailTemplatesIdentifierResponse200.from_dict(response.json())

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
) -> Response[ApiError | PutApiAdminSystemEmailTemplatesIdentifierResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutApiAdminSystemEmailTemplatesIdentifierBody,
) -> Response[ApiError | PutApiAdminSystemEmailTemplatesIdentifierResponse200]:
    """
    Args:
        identifier (str):
        body (PutApiAdminSystemEmailTemplatesIdentifierBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PutApiAdminSystemEmailTemplatesIdentifierResponse200]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutApiAdminSystemEmailTemplatesIdentifierBody,
) -> ApiError | PutApiAdminSystemEmailTemplatesIdentifierResponse200 | None:
    """
    Args:
        identifier (str):
        body (PutApiAdminSystemEmailTemplatesIdentifierBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PutApiAdminSystemEmailTemplatesIdentifierResponse200
    """

    return sync_detailed(
        identifier=identifier,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutApiAdminSystemEmailTemplatesIdentifierBody,
) -> Response[ApiError | PutApiAdminSystemEmailTemplatesIdentifierResponse200]:
    """
    Args:
        identifier (str):
        body (PutApiAdminSystemEmailTemplatesIdentifierBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PutApiAdminSystemEmailTemplatesIdentifierResponse200]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutApiAdminSystemEmailTemplatesIdentifierBody,
) -> ApiError | PutApiAdminSystemEmailTemplatesIdentifierResponse200 | None:
    """
    Args:
        identifier (str):
        body (PutApiAdminSystemEmailTemplatesIdentifierBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PutApiAdminSystemEmailTemplatesIdentifierResponse200
    """

    return (
        await asyncio_detailed(
            identifier=identifier,
            client=client,
            body=body,
        )
    ).parsed
