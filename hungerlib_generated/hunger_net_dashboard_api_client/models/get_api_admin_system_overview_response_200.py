from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_container_type import AppContainerType

if TYPE_CHECKING:
    from ..models.get_api_admin_system_overview_response_200_cache import GetApiAdminSystemOverviewResponse200Cache
    from ..models.get_api_admin_system_overview_response_200_cpu import GetApiAdminSystemOverviewResponse200Cpu
    from ..models.get_api_admin_system_overview_response_200_database import (
        GetApiAdminSystemOverviewResponse200Database,
    )
    from ..models.get_api_admin_system_overview_response_200_memory import GetApiAdminSystemOverviewResponse200Memory


T = TypeVar("T", bound="GetApiAdminSystemOverviewResponse200")


@_attrs_define
class GetApiAdminSystemOverviewResponse200:
    """
    Attributes:
        version (str):
        container_type (AppContainerType):
        cpu (GetApiAdminSystemOverviewResponse200Cpu):
        memory (GetApiAdminSystemOverviewResponse200Memory):
        cache (GetApiAdminSystemOverviewResponse200Cache):
        database (GetApiAdminSystemOverviewResponse200Database):
        architecture (str):
        kernel_version (str):
    """

    version: str
    container_type: AppContainerType
    cpu: GetApiAdminSystemOverviewResponse200Cpu
    memory: GetApiAdminSystemOverviewResponse200Memory
    cache: GetApiAdminSystemOverviewResponse200Cache
    database: GetApiAdminSystemOverviewResponse200Database
    architecture: str
    kernel_version: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        container_type = self.container_type.value

        cpu = self.cpu.to_dict()

        memory = self.memory.to_dict()

        cache = self.cache.to_dict()

        database = self.database.to_dict()

        architecture = self.architecture

        kernel_version = self.kernel_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
                "container_type": container_type,
                "cpu": cpu,
                "memory": memory,
                "cache": cache,
                "database": database,
                "architecture": architecture,
                "kernel_version": kernel_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_admin_system_overview_response_200_cache import GetApiAdminSystemOverviewResponse200Cache  # noqa: PLC0415
        from ..models.get_api_admin_system_overview_response_200_cpu import GetApiAdminSystemOverviewResponse200Cpu  # noqa: PLC0415
        from ..models.get_api_admin_system_overview_response_200_database import (
            GetApiAdminSystemOverviewResponse200Database,  # noqa: PLC0415
        )
        from ..models.get_api_admin_system_overview_response_200_memory import (
            GetApiAdminSystemOverviewResponse200Memory,  # noqa: PLC0415
        )

        d = dict(src_dict)
        version = d.pop("version")

        container_type = AppContainerType(d.pop("container_type"))

        cpu = GetApiAdminSystemOverviewResponse200Cpu.from_dict(d.pop("cpu"))

        memory = GetApiAdminSystemOverviewResponse200Memory.from_dict(d.pop("memory"))

        cache = GetApiAdminSystemOverviewResponse200Cache.from_dict(d.pop("cache"))

        database = GetApiAdminSystemOverviewResponse200Database.from_dict(d.pop("database"))

        architecture = d.pop("architecture")

        kernel_version = d.pop("kernel_version")

        get_api_admin_system_overview_response_200 = cls(
            version=version,
            container_type=container_type,
            cpu=cpu,
            memory=memory,
            cache=cache,
            database=database,
            architecture=architecture,
            kernel_version=kernel_version,
        )

        get_api_admin_system_overview_response_200.additional_properties = d
        return get_api_admin_system_overview_response_200

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
