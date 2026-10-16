from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_configuration_allocations_default_type_1 import ServerConfigurationAllocationsDefaultType1
    from ..models.server_configuration_allocations_mappings import ServerConfigurationAllocationsMappings


T = TypeVar("T", bound="ServerConfigurationAllocations")


@_attrs_define
class ServerConfigurationAllocations:
    """
    Attributes:
        force_outgoing_ip (bool):
        mappings (ServerConfigurationAllocationsMappings):
        default (None | ServerConfigurationAllocationsDefaultType1 | Unset):
    """

    force_outgoing_ip: bool
    mappings: ServerConfigurationAllocationsMappings
    default: None | ServerConfigurationAllocationsDefaultType1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.server_configuration_allocations_default_type_1 import ServerConfigurationAllocationsDefaultType1  # noqa: PLC0415

        force_outgoing_ip = self.force_outgoing_ip

        mappings = self.mappings.to_dict()

        default: dict[str, Any] | None | Unset
        if isinstance(self.default, Unset):
            default = UNSET
        elif isinstance(self.default, ServerConfigurationAllocationsDefaultType1):
            default = self.default.to_dict()
        else:
            default = self.default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "force_outgoing_ip": force_outgoing_ip,
                "mappings": mappings,
            }
        )
        if default is not UNSET:
            field_dict["default"] = default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_configuration_allocations_default_type_1 import ServerConfigurationAllocationsDefaultType1  # noqa: PLC0415
        from ..models.server_configuration_allocations_mappings import ServerConfigurationAllocationsMappings  # noqa: PLC0415

        d = dict(src_dict)
        force_outgoing_ip = d.pop("force_outgoing_ip")

        mappings = ServerConfigurationAllocationsMappings.from_dict(d.pop("mappings"))

        def _parse_default(data: object) -> None | ServerConfigurationAllocationsDefaultType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                default_type_1 = ServerConfigurationAllocationsDefaultType1.from_dict(data)

                return default_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ServerConfigurationAllocationsDefaultType1 | Unset, data)

        default = _parse_default(d.pop("default", UNSET))

        server_configuration_allocations = cls(
            force_outgoing_ip=force_outgoing_ip,
            mappings=mappings,
            default=default,
        )

        server_configuration_allocations.additional_properties = d
        return server_configuration_allocations

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
