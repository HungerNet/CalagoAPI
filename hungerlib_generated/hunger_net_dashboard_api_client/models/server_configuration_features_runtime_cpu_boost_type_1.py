from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServerConfigurationFeaturesRuntimeCpuBoostType1")


@_attrs_define
class ServerConfigurationFeaturesRuntimeCpuBoostType1:
    """
    Attributes:
        enabled (bool):
        threshold (int):
        sustained (int):
        multiple (float):
        duration (int):
        cooldown (int):
    """

    enabled: bool
    threshold: int
    sustained: int
    multiple: float
    duration: int
    cooldown: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        threshold = self.threshold

        sustained = self.sustained

        multiple = self.multiple

        duration = self.duration

        cooldown = self.cooldown

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "threshold": threshold,
                "sustained": sustained,
                "multiple": multiple,
                "duration": duration,
                "cooldown": cooldown,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        threshold = d.pop("threshold")

        sustained = d.pop("sustained")

        multiple = d.pop("multiple")

        duration = d.pop("duration")

        cooldown = d.pop("cooldown")

        server_configuration_features_runtime_cpu_boost_type_1 = cls(
            enabled=enabled,
            threshold=threshold,
            sustained=sustained,
            multiple=multiple,
            duration=duration,
            cooldown=cooldown,
        )

        server_configuration_features_runtime_cpu_boost_type_1.additional_properties = d
        return server_configuration_features_runtime_cpu_boost_type_1

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
