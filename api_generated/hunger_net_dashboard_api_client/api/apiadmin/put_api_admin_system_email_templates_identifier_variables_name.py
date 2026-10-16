from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.put_api_admin_system_email_templates_identifier_variables_name_body import (
    PutApiAdminSystemEmailTemplatesIdentifierVariablesNameBody,
)
from ...models.put_api_admin_system_email_templates_identifier_variables_name_response_200 import (
    PutApiAdminSystemEmailTemplatesIdentifierVariablesNameResponse200,
)
from ...types import Response


def _get_kwargs(
    identifier: str,
    name: str,
    *,
    body: PutApiAdminSystemEmailTemplatesIdentifierVariablesNameBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/admin/system/email/templates/{identifier}/variables/{name}".format(
            identifier=quote(str(identifier), safe=""),
            name=quote(str(name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PutApiAdminSystemEmailTemplatesIdentifierVariablesNameResponse200 | None:
    if response.status_code == 200:
        response_200 = PutApiAdminSystemEmailTemplatesIdentifierVariablesNameResponse200.from_dict(response.json())

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
) -> Response[ApiError | PutApiAdminSystemEmailTemplatesIdentifierVariablesNameResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    identifier: str,
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutApiAdminSystemEmailTemplatesIdentifierVariablesNameBody,
) -> Response[ApiError | PutApiAdminSystemEmailTemplatesIdentifierVariablesNameResponse200]:
    """
    Args:
        identifier (str):
        name (str):
        body (PutApiAdminSystemEmailTemplatesIdentifierVariablesNameBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PutApiAdminSystemEmailTemplatesIdentifierVariablesNameResponse200]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        name=name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    identifier: str,
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutApiAdminSystemEmailTemplatesIdentifierVariablesNameBody,
) -> ApiError | PutApiAdminSystemEmailTemplatesIdentifierVariablesNameResponse200 | None:
    """
    Args:
        identifier (str):
        name (str):
        body (PutApiAdminSystemEmailTemplatesIdentifierVariablesNameBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PutApiAdminSystemEmailTemplatesIdentifierVariablesNameResponse200
    """

    return sync_detailed(
        identifier=identifier,
        name=name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    identifier: str,
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutApiAdminSystemEmailTemplatesIdentifierVariablesNameBody,
) -> Response[ApiError | PutApiAdminSystemEmailTemplatesIdentifierVariablesNameResponse200]:
    """
    Args:
        identifier (str):
        name (str):
        body (PutApiAdminSystemEmailTemplatesIdentifierVariablesNameBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PutApiAdminSystemEmailTemplatesIdentifierVariablesNameResponse200]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        name=name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    identifier: str,
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: PutApiAdminSystemEmailTemplatesIdentifierVariablesNameBody,
) -> ApiError | PutApiAdminSystemEmailTemplatesIdentifierVariablesNameResponse200 | None:
    """
    Args:
        identifier (str):
        name (str):
        body (PutApiAdminSystemEmailTemplatesIdentifierVariablesNameBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PutApiAdminSystemEmailTemplatesIdentifierVariablesNameResponse200
    """

    return (
        await asyncio_detailed(
            identifier=identifier,
            name=name,
            client=client,
            body=body,
        )
    ).parsed
