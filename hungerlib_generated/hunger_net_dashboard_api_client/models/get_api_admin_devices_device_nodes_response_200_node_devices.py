from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_admin_devices_device_nodes_response_200_node_devices_admin_node_node_device import (
        GetApiAdminDevicesDeviceNodesResponse200NodeDevicesAdminNodeNodeDevice,
    )


T = TypeVar("T", bound="GetApiAdminDevicesDeviceNodesResponse200NodeDevices")


@_attrs_define
class GetApiAdminDevicesDeviceNodesResponse200NodeDevices:
    """
    Attributes:
        total (int):
        per_page (int):
        page (int):
        data (list[GetApiAdminDevicesDeviceNodesResponse200NodeDevicesAdminNodeNodeDevice]):
    """

    total: int
    per_page: int
    page: int
    data: list[GetApiAdminDevicesDeviceNodesResponse200NodeDevicesAdminNodeNodeDevice]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        per_page = self.per_page

        page = self.page

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "per_page": per_page,
                "page": page,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_admin_devices_device_nodes_response_200_node_devices_admin_node_node_device import (
            GetApiAdminDevicesDeviceNodesResponse200NodeDevicesAdminNodeNodeDevice,  # noqa: PLC0415
        )

        d = dict(src_dict)
        total = d.pop("total")

        per_page = d.pop("per_page")

        page = d.pop("page")

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = GetApiAdminDevicesDeviceNodesResponse200NodeDevicesAdminNodeNodeDevice.from_dict(data_item_data)

            data.append(data_item)

        get_api_admin_devices_device_nodes_response_200_node_devices = cls(
            total=total,
            per_page=per_page,
            page=page,
            data=data,
        )

        get_api_admin_devices_device_nodes_response_200_node_devices.additional_properties = d
        return get_api_admin_devices_device_nodes_response_200_node_devices

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
