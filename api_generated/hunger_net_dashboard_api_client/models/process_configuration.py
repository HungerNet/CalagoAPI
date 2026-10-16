from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.process_configuration_configs_item import ProcessConfigurationConfigsItem
    from ..models.process_configuration_startup import ProcessConfigurationStartup
    from ..models.process_configuration_stop import ProcessConfigurationStop


T = TypeVar("T", bound="ProcessConfiguration")


@_attrs_define
class ProcessConfiguration:
    """
    Attributes:
        startup (ProcessConfigurationStartup):
        stop (ProcessConfigurationStop):
        configs (list[ProcessConfigurationConfigsItem]):
    """

    startup: ProcessConfigurationStartup
    stop: ProcessConfigurationStop
    configs: list[ProcessConfigurationConfigsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        startup = self.startup.to_dict()

        stop = self.stop.to_dict()

        configs = []
        for configs_item_data in self.configs:
            configs_item = configs_item_data.to_dict()
            configs.append(configs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "startup": startup,
                "stop": stop,
                "configs": configs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.process_configuration_configs_item import ProcessConfigurationConfigsItem  # noqa: PLC0415
        from ..models.process_configuration_startup import ProcessConfigurationStartup  # noqa: PLC0415
        from ..models.process_configuration_stop import ProcessConfigurationStop  # noqa: PLC0415

        d = dict(src_dict)
        startup = ProcessConfigurationStartup.from_dict(d.pop("startup"))

        stop = ProcessConfigurationStop.from_dict(d.pop("stop"))

        configs = []
        _configs = d.pop("configs")
        for configs_item_data in _configs:
            configs_item = ProcessConfigurationConfigsItem.from_dict(configs_item_data)

            configs.append(configs_item)

        process_configuration = cls(
            startup=startup,
            stop=stop,
            configs=configs,
        )

        process_configuration.additional_properties = d
        return process_configuration

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
