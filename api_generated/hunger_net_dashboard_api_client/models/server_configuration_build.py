from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_configuration_build_bandwidth import ServerConfigurationBuildBandwidth


T = TypeVar("T", bound="ServerConfigurationBuild")


@_attrs_define
class ServerConfigurationBuild:
    """
    Attributes:
        memory_limit (int):
        overhead_memory (int):
        swap (int):
        cpu_limit (int):
        disk_space (int):
        oom_disabled (bool):
        bandwidth (ServerConfigurationBuildBandwidth):
        io_weight (int | None | Unset):
        threads (None | str | Unset):
    """

    memory_limit: int
    overhead_memory: int
    swap: int
    cpu_limit: int
    disk_space: int
    oom_disabled: bool
    bandwidth: ServerConfigurationBuildBandwidth
    io_weight: int | None | Unset = UNSET
    threads: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        memory_limit = self.memory_limit

        overhead_memory = self.overhead_memory

        swap = self.swap

        cpu_limit = self.cpu_limit

        disk_space = self.disk_space

        oom_disabled = self.oom_disabled

        bandwidth = self.bandwidth.to_dict()

        io_weight: int | None | Unset
        if isinstance(self.io_weight, Unset):
            io_weight = UNSET
        else:
            io_weight = self.io_weight

        threads: None | str | Unset
        if isinstance(self.threads, Unset):
            threads = UNSET
        else:
            threads = self.threads

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "memory_limit": memory_limit,
                "overhead_memory": overhead_memory,
                "swap": swap,
                "cpu_limit": cpu_limit,
                "disk_space": disk_space,
                "oom_disabled": oom_disabled,
                "bandwidth": bandwidth,
            }
        )
        if io_weight is not UNSET:
            field_dict["io_weight"] = io_weight
        if threads is not UNSET:
            field_dict["threads"] = threads

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_configuration_build_bandwidth import ServerConfigurationBuildBandwidth  # noqa: PLC0415

        d = dict(src_dict)
        memory_limit = d.pop("memory_limit")

        overhead_memory = d.pop("overhead_memory")

        swap = d.pop("swap")

        cpu_limit = d.pop("cpu_limit")

        disk_space = d.pop("disk_space")

        oom_disabled = d.pop("oom_disabled")

        bandwidth = ServerConfigurationBuildBandwidth.from_dict(d.pop("bandwidth"))

        def _parse_io_weight(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        io_weight = _parse_io_weight(d.pop("io_weight", UNSET))

        def _parse_threads(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        threads = _parse_threads(d.pop("threads", UNSET))

        server_configuration_build = cls(
            memory_limit=memory_limit,
            overhead_memory=overhead_memory,
            swap=swap,
            cpu_limit=cpu_limit,
            disk_space=disk_space,
            oom_disabled=oom_disabled,
            bandwidth=bandwidth,
            io_weight=io_weight,
            threads=threads,
        )

        server_configuration_build.additional_properties = d
        return server_configuration_build

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
