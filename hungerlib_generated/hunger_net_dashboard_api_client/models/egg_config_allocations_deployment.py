from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.egg_config_allocations_deployment_additional_item import EggConfigAllocationsDeploymentAdditionalItem
    from ..models.egg_config_allocations_deployment_primary_type_1 import EggConfigAllocationsDeploymentPrimaryType1


T = TypeVar("T", bound="EggConfigAllocationsDeployment")


@_attrs_define
class EggConfigAllocationsDeployment:
    """
    Attributes:
        dedicated (bool):
        additional (list[EggConfigAllocationsDeploymentAdditionalItem]):
        primary (EggConfigAllocationsDeploymentPrimaryType1 | None | Unset):
    """

    dedicated: bool
    additional: list[EggConfigAllocationsDeploymentAdditionalItem]
    primary: EggConfigAllocationsDeploymentPrimaryType1 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.egg_config_allocations_deployment_primary_type_1 import EggConfigAllocationsDeploymentPrimaryType1  # noqa: PLC0415

        dedicated = self.dedicated

        additional = []
        for additional_item_data in self.additional:
            additional_item = additional_item_data.to_dict()
            additional.append(additional_item)

        primary: dict[str, Any] | None | Unset
        if isinstance(self.primary, Unset):
            primary = UNSET
        elif isinstance(self.primary, EggConfigAllocationsDeploymentPrimaryType1):
            primary = self.primary.to_dict()
        else:
            primary = self.primary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dedicated": dedicated,
                "additional": additional,
            }
        )
        if primary is not UNSET:
            field_dict["primary"] = primary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.egg_config_allocations_deployment_additional_item import (
            EggConfigAllocationsDeploymentAdditionalItem,  # noqa: PLC0415
        )
        from ..models.egg_config_allocations_deployment_primary_type_1 import EggConfigAllocationsDeploymentPrimaryType1  # noqa: PLC0415

        d = dict(src_dict)
        dedicated = d.pop("dedicated")

        additional = []
        _additional = d.pop("additional")
        for additional_item_data in _additional:
            additional_item = EggConfigAllocationsDeploymentAdditionalItem.from_dict(additional_item_data)

            additional.append(additional_item)

        def _parse_primary(data: object) -> EggConfigAllocationsDeploymentPrimaryType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                primary_type_1 = EggConfigAllocationsDeploymentPrimaryType1.from_dict(data)

                return primary_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EggConfigAllocationsDeploymentPrimaryType1 | None | Unset, data)

        primary = _parse_primary(d.pop("primary", UNSET))

        egg_config_allocations_deployment = cls(
            dedicated=dedicated,
            additional=additional,
            primary=primary,
        )

        egg_config_allocations_deployment.additional_properties = d
        return egg_config_allocations_deployment

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
