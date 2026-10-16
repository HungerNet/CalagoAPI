from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.egg_config_allocations_deployment_additional_item_mode_type_0 import (
        EggConfigAllocationsDeploymentAdditionalItemModeType0,
    )
    from ..models.egg_config_allocations_deployment_additional_item_mode_type_1 import (
        EggConfigAllocationsDeploymentAdditionalItemModeType1,
    )
    from ..models.egg_config_allocations_deployment_additional_item_mode_type_2 import (
        EggConfigAllocationsDeploymentAdditionalItemModeType2,
    )
    from ..models.egg_config_allocations_deployment_additional_item_mode_type_3 import (
        EggConfigAllocationsDeploymentAdditionalItemModeType3,
    )
    from ..models.egg_config_allocations_deployment_additional_item_mode_type_4 import (
        EggConfigAllocationsDeploymentAdditionalItemModeType4,
    )
    from ..models.egg_config_allocations_deployment_additional_item_mode_type_5 import (
        EggConfigAllocationsDeploymentAdditionalItemModeType5,
    )


T = TypeVar("T", bound="EggConfigAllocationsDeploymentAdditionalItem")


@_attrs_define
class EggConfigAllocationsDeploymentAdditionalItem:
    """
    Attributes:
        mode (EggConfigAllocationsDeploymentAdditionalItemModeType0 |
            EggConfigAllocationsDeploymentAdditionalItemModeType1 | EggConfigAllocationsDeploymentAdditionalItemModeType2 |
            EggConfigAllocationsDeploymentAdditionalItemModeType3 | EggConfigAllocationsDeploymentAdditionalItemModeType4 |
            EggConfigAllocationsDeploymentAdditionalItemModeType5):
        assign_to_variable (None | str | Unset):
    """

    mode: (
        EggConfigAllocationsDeploymentAdditionalItemModeType0
        | EggConfigAllocationsDeploymentAdditionalItemModeType1
        | EggConfigAllocationsDeploymentAdditionalItemModeType2
        | EggConfigAllocationsDeploymentAdditionalItemModeType3
        | EggConfigAllocationsDeploymentAdditionalItemModeType4
        | EggConfigAllocationsDeploymentAdditionalItemModeType5
    )
    assign_to_variable: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.egg_config_allocations_deployment_additional_item_mode_type_0 import (
            EggConfigAllocationsDeploymentAdditionalItemModeType0,  # noqa: PLC0415
        )
        from ..models.egg_config_allocations_deployment_additional_item_mode_type_1 import (
            EggConfigAllocationsDeploymentAdditionalItemModeType1,  # noqa: PLC0415
        )
        from ..models.egg_config_allocations_deployment_additional_item_mode_type_2 import (
            EggConfigAllocationsDeploymentAdditionalItemModeType2,  # noqa: PLC0415
        )
        from ..models.egg_config_allocations_deployment_additional_item_mode_type_3 import (
            EggConfigAllocationsDeploymentAdditionalItemModeType3,  # noqa: PLC0415
        )
        from ..models.egg_config_allocations_deployment_additional_item_mode_type_4 import (
            EggConfigAllocationsDeploymentAdditionalItemModeType4,  # noqa: PLC0415
        )

        mode: dict[str, Any]
        if isinstance(self.mode, EggConfigAllocationsDeploymentAdditionalItemModeType0):
            mode = self.mode.to_dict()
        elif isinstance(self.mode, EggConfigAllocationsDeploymentAdditionalItemModeType1):
            mode = self.mode.to_dict()
        elif isinstance(self.mode, EggConfigAllocationsDeploymentAdditionalItemModeType2):
            mode = self.mode.to_dict()
        elif isinstance(self.mode, EggConfigAllocationsDeploymentAdditionalItemModeType3):
            mode = self.mode.to_dict()
        elif isinstance(self.mode, EggConfigAllocationsDeploymentAdditionalItemModeType4):
            mode = self.mode.to_dict()
        else:
            mode = self.mode.to_dict()

        assign_to_variable: None | str | Unset
        if isinstance(self.assign_to_variable, Unset):
            assign_to_variable = UNSET
        else:
            assign_to_variable = self.assign_to_variable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
            }
        )
        if assign_to_variable is not UNSET:
            field_dict["assign_to_variable"] = assign_to_variable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.egg_config_allocations_deployment_additional_item_mode_type_0 import (
            EggConfigAllocationsDeploymentAdditionalItemModeType0,  # noqa: PLC0415
        )
        from ..models.egg_config_allocations_deployment_additional_item_mode_type_1 import (
            EggConfigAllocationsDeploymentAdditionalItemModeType1,  # noqa: PLC0415
        )
        from ..models.egg_config_allocations_deployment_additional_item_mode_type_2 import (
            EggConfigAllocationsDeploymentAdditionalItemModeType2,  # noqa: PLC0415
        )
        from ..models.egg_config_allocations_deployment_additional_item_mode_type_3 import (
            EggConfigAllocationsDeploymentAdditionalItemModeType3,  # noqa: PLC0415
        )
        from ..models.egg_config_allocations_deployment_additional_item_mode_type_4 import (
            EggConfigAllocationsDeploymentAdditionalItemModeType4,  # noqa: PLC0415
        )
        from ..models.egg_config_allocations_deployment_additional_item_mode_type_5 import (
            EggConfigAllocationsDeploymentAdditionalItemModeType5,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_mode(
            data: object,
        ) -> (
            EggConfigAllocationsDeploymentAdditionalItemModeType0
            | EggConfigAllocationsDeploymentAdditionalItemModeType1
            | EggConfigAllocationsDeploymentAdditionalItemModeType2
            | EggConfigAllocationsDeploymentAdditionalItemModeType3
            | EggConfigAllocationsDeploymentAdditionalItemModeType4
            | EggConfigAllocationsDeploymentAdditionalItemModeType5
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mode_type_0 = EggConfigAllocationsDeploymentAdditionalItemModeType0.from_dict(data)

                return mode_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mode_type_1 = EggConfigAllocationsDeploymentAdditionalItemModeType1.from_dict(data)

                return mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mode_type_2 = EggConfigAllocationsDeploymentAdditionalItemModeType2.from_dict(data)

                return mode_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mode_type_3 = EggConfigAllocationsDeploymentAdditionalItemModeType3.from_dict(data)

                return mode_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mode_type_4 = EggConfigAllocationsDeploymentAdditionalItemModeType4.from_dict(data)

                return mode_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            mode_type_5 = EggConfigAllocationsDeploymentAdditionalItemModeType5.from_dict(data)

            return mode_type_5

        mode = _parse_mode(d.pop("mode"))

        def _parse_assign_to_variable(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assign_to_variable = _parse_assign_to_variable(d.pop("assign_to_variable", UNSET))

        egg_config_allocations_deployment_additional_item = cls(
            mode=mode,
            assign_to_variable=assign_to_variable,
        )

        egg_config_allocations_deployment_additional_item.additional_properties = d
        return egg_config_allocations_deployment_additional_item

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
