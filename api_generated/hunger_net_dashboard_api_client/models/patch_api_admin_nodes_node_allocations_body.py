from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.allocation_selector_type_0 import AllocationSelectorType0
    from ..models.allocation_selector_type_1 import AllocationSelectorType1
    from ..models.allocation_selector_type_2 import AllocationSelectorType2


T = TypeVar("T", bound="PatchApiAdminNodesNodeAllocationsBody")


@_attrs_define
class PatchApiAdminNodesNodeAllocationsBody:
    """
    Attributes:
        selector (AllocationSelectorType0 | AllocationSelectorType1 | AllocationSelectorType2):
        ip (str):
        ip_alias (None | str | Unset):
    """

    selector: AllocationSelectorType0 | AllocationSelectorType1 | AllocationSelectorType2
    ip: str
    ip_alias: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.allocation_selector_type_0 import AllocationSelectorType0  # noqa: PLC0415
        from ..models.allocation_selector_type_1 import AllocationSelectorType1  # noqa: PLC0415

        selector: dict[str, Any]
        if isinstance(self.selector, AllocationSelectorType0):
            selector = self.selector.to_dict()
        elif isinstance(self.selector, AllocationSelectorType1):
            selector = self.selector.to_dict()
        else:
            selector = self.selector.to_dict()

        ip = self.ip

        ip_alias: None | str | Unset
        if isinstance(self.ip_alias, Unset):
            ip_alias = UNSET
        else:
            ip_alias = self.ip_alias

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "selector": selector,
                "ip": ip,
            }
        )
        if ip_alias is not UNSET:
            field_dict["ip_alias"] = ip_alias

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.allocation_selector_type_0 import AllocationSelectorType0  # noqa: PLC0415
        from ..models.allocation_selector_type_1 import AllocationSelectorType1  # noqa: PLC0415
        from ..models.allocation_selector_type_2 import AllocationSelectorType2  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_selector(
            data: object,
        ) -> AllocationSelectorType0 | AllocationSelectorType1 | AllocationSelectorType2:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_allocation_selector_type_0 = AllocationSelectorType0.from_dict(data)

                return componentsschemas_allocation_selector_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_allocation_selector_type_1 = AllocationSelectorType1.from_dict(data)

                return componentsschemas_allocation_selector_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_allocation_selector_type_2 = AllocationSelectorType2.from_dict(data)

            return componentsschemas_allocation_selector_type_2

        selector = _parse_selector(d.pop("selector"))

        ip = d.pop("ip")

        def _parse_ip_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ip_alias = _parse_ip_alias(d.pop("ip_alias", UNSET))

        patch_api_admin_nodes_node_allocations_body = cls(
            selector=selector,
            ip=ip,
            ip_alias=ip_alias,
        )

        patch_api_admin_nodes_node_allocations_body.additional_properties = d
        return patch_api_admin_nodes_node_allocations_body

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
