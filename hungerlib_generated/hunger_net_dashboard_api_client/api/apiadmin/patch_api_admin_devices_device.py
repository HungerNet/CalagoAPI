from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.patch_api_admin_devices_device_body import PatchApiAdminDevicesDeviceBody
from ...models.patch_api_admin_devices_device_response_200 import PatchApiAdminDevicesDeviceResponse200
from ...types import Response


def _get_kwargs(
    device: UUID,
    *,
    body: PatchApiAdminDevicesDeviceBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/admin/devices/{device}".format(
            device=quote(str(device), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PatchApiAdminDevicesDeviceResponse200 | None:
    if response.status_code == 200:
        response_200 = PatchApiAdminDevicesDeviceResponse200.from_dict(response.json())

        return response_200

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


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | PatchApiAdminDevicesDeviceResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    device: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PatchApiAdminDevicesDeviceBody,
) -> Response[ApiError | PatchApiAdminDevicesDeviceResponse200]:
    """
    Args:
        device (UUID):
        body (PatchApiAdminDevicesDeviceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PatchApiAdminDevicesDeviceResponse200]
    """

    kwargs = _get_kwargs(
        device=device,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    device: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PatchApiAdminDevicesDeviceBody,
) -> ApiError | PatchApiAdminDevicesDeviceResponse200 | None:
    """
    Args:
        device (UUID):
        body (PatchApiAdminDevicesDeviceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PatchApiAdminDevicesDeviceResponse200
    """

    return sync_detailed(
        device=device,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    device: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PatchApiAdminDevicesDeviceBody,
) -> Response[ApiError | PatchApiAdminDevicesDeviceResponse200]:
    """
    Args:
        device (UUID):
        body (PatchApiAdminDevicesDeviceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PatchApiAdminDevicesDeviceResponse200]
    """

    kwargs = _get_kwargs(
        device=device,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    device: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PatchApiAdminDevicesDeviceBody,
) -> ApiError | PatchApiAdminDevicesDeviceResponse200 | None:
    """
    Args:
        device (UUID):
        body (PatchApiAdminDevicesDeviceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PatchApiAdminDevicesDeviceResponse200
    """

    return (
        await asyncio_detailed(
            device=device,
            client=client,
            body=body,
        )
    ).parsed
