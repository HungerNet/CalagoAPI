from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_admin_servers_server_databases_instances_response_200_instances import (
        GetApiAdminServersServerDatabasesInstancesResponse200Instances,
    )


T = TypeVar("T", bound="GetApiAdminServersServerDatabasesInstancesResponse200")


@_attrs_define
class GetApiAdminServersServerDatabasesInstancesResponse200:
    """
    Attributes:
        instances (GetApiAdminServersServerDatabasesInstancesResponse200Instances):
    """

    instances: GetApiAdminServersServerDatabasesInstancesResponse200Instances
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instances = self.instances.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instances": instances,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_admin_servers_server_databases_instances_response_200_instances import (
            GetApiAdminServersServerDatabasesInstancesResponse200Instances,  # noqa: PLC0415
        )

        d = dict(src_dict)
        instances = GetApiAdminServersServerDatabasesInstancesResponse200Instances.from_dict(d.pop("instances"))

        get_api_admin_servers_server_databases_instances_response_200 = cls(
            instances=instances,
        )

        get_api_admin_servers_server_databases_instances_response_200.additional_properties = d
        return get_api_admin_servers_server_databases_instances_response_200

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
