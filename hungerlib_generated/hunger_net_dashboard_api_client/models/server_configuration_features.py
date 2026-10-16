from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_configuration_features_runtime_cpu_boost_type_1 import (
        ServerConfigurationFeaturesRuntimeCpuBoostType1,
    )
    from ..models.server_configuration_features_startup_cpu_boost_type_1 import (
        ServerConfigurationFeaturesStartupCpuBoostType1,
    )


T = TypeVar("T", bound="ServerConfigurationFeatures")


@_attrs_define
class ServerConfigurationFeatures:
    """
    Attributes:
        startup_cpu_boost (None | ServerConfigurationFeaturesStartupCpuBoostType1 | Unset):
        runtime_cpu_boost (None | ServerConfigurationFeaturesRuntimeCpuBoostType1 | Unset):
    """

    startup_cpu_boost: None | ServerConfigurationFeaturesStartupCpuBoostType1 | Unset = UNSET
    runtime_cpu_boost: None | ServerConfigurationFeaturesRuntimeCpuBoostType1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.server_configuration_features_runtime_cpu_boost_type_1 import (
            ServerConfigurationFeaturesRuntimeCpuBoostType1,  # noqa: PLC0415
        )
        from ..models.server_configuration_features_startup_cpu_boost_type_1 import (
            ServerConfigurationFeaturesStartupCpuBoostType1,  # noqa: PLC0415
        )

        startup_cpu_boost: dict[str, Any] | None | Unset
        if isinstance(self.startup_cpu_boost, Unset):
            startup_cpu_boost = UNSET
        elif isinstance(self.startup_cpu_boost, ServerConfigurationFeaturesStartupCpuBoostType1):
            startup_cpu_boost = self.startup_cpu_boost.to_dict()
        else:
            startup_cpu_boost = self.startup_cpu_boost

        runtime_cpu_boost: dict[str, Any] | None | Unset
        if isinstance(self.runtime_cpu_boost, Unset):
            runtime_cpu_boost = UNSET
        elif isinstance(self.runtime_cpu_boost, ServerConfigurationFeaturesRuntimeCpuBoostType1):
            runtime_cpu_boost = self.runtime_cpu_boost.to_dict()
        else:
            runtime_cpu_boost = self.runtime_cpu_boost

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if startup_cpu_boost is not UNSET:
            field_dict["startup_cpu_boost"] = startup_cpu_boost
        if runtime_cpu_boost is not UNSET:
            field_dict["runtime_cpu_boost"] = runtime_cpu_boost

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_configuration_features_runtime_cpu_boost_type_1 import (
            ServerConfigurationFeaturesRuntimeCpuBoostType1,  # noqa: PLC0415
        )
        from ..models.server_configuration_features_startup_cpu_boost_type_1 import (
            ServerConfigurationFeaturesStartupCpuBoostType1,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_startup_cpu_boost(data: object) -> None | ServerConfigurationFeaturesStartupCpuBoostType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                startup_cpu_boost_type_1 = ServerConfigurationFeaturesStartupCpuBoostType1.from_dict(data)

                return startup_cpu_boost_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ServerConfigurationFeaturesStartupCpuBoostType1 | Unset, data)

        startup_cpu_boost = _parse_startup_cpu_boost(d.pop("startup_cpu_boost", UNSET))

        def _parse_runtime_cpu_boost(data: object) -> None | ServerConfigurationFeaturesRuntimeCpuBoostType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                runtime_cpu_boost_type_1 = ServerConfigurationFeaturesRuntimeCpuBoostType1.from_dict(data)

                return runtime_cpu_boost_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ServerConfigurationFeaturesRuntimeCpuBoostType1 | Unset, data)

        runtime_cpu_boost = _parse_runtime_cpu_boost(d.pop("runtime_cpu_boost", UNSET))

        server_configuration_features = cls(
            startup_cpu_boost=startup_cpu_boost,
            runtime_cpu_boost=runtime_cpu_boost,
        )

        server_configuration_features.additional_properties = d
        return server_configuration_features

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
