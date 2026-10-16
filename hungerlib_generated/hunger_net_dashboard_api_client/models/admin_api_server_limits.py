from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_server_bandwidth import ApiServerBandwidth


T = TypeVar("T", bound="AdminApiServerLimits")


@_attrs_define
class AdminApiServerLimits:
    """
    Attributes:
        cpu (int):
        memory (int):
        memory_overhead (int):
        swap (int):
        disk (int):
        io_weight (int | None | Unset):
        bandwidth (ApiServerBandwidth | None | Unset):
    """

    cpu: int
    memory: int
    memory_overhead: int
    swap: int
    disk: int
    io_weight: int | None | Unset = UNSET
    bandwidth: ApiServerBandwidth | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_server_bandwidth import ApiServerBandwidth  # noqa: PLC0415

        cpu = self.cpu

        memory = self.memory

        memory_overhead = self.memory_overhead

        swap = self.swap

        disk = self.disk

        io_weight: int | None | Unset
        if isinstance(self.io_weight, Unset):
            io_weight = UNSET
        else:
            io_weight = self.io_weight

        bandwidth: dict[str, Any] | None | Unset
        if isinstance(self.bandwidth, Unset):
            bandwidth = UNSET
        elif isinstance(self.bandwidth, ApiServerBandwidth):
            bandwidth = self.bandwidth.to_dict()
        else:
            bandwidth = self.bandwidth

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cpu": cpu,
                "memory": memory,
                "memory_overhead": memory_overhead,
                "swap": swap,
                "disk": disk,
            }
        )
        if io_weight is not UNSET:
            field_dict["io_weight"] = io_weight
        if bandwidth is not UNSET:
            field_dict["bandwidth"] = bandwidth

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_server_bandwidth import ApiServerBandwidth  # noqa: PLC0415

        d = dict(src_dict)
        cpu = d.pop("cpu")

        memory = d.pop("memory")

        memory_overhead = d.pop("memory_overhead")

        swap = d.pop("swap")

        disk = d.pop("disk")

        def _parse_io_weight(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        io_weight = _parse_io_weight(d.pop("io_weight", UNSET))

        def _parse_bandwidth(data: object) -> ApiServerBandwidth | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                bandwidth_type_1 = ApiServerBandwidth.from_dict(data)

                return bandwidth_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApiServerBandwidth | None | Unset, data)

        bandwidth = _parse_bandwidth(d.pop("bandwidth", UNSET))

        admin_api_server_limits = cls(
            cpu=cpu,
            memory=memory,
            memory_overhead=memory_overhead,
            swap=swap,
            disk=disk,
            io_weight=io_weight,
            bandwidth=bandwidth,
        )

        admin_api_server_limits.additional_properties = d
        return admin_api_server_limits

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
