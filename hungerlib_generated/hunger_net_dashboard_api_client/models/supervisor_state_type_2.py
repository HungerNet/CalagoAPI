from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.supervisor_state_type_2_type import SupervisorStateType2Type

if TYPE_CHECKING:
    from ..models.build_phase_type_0 import BuildPhaseType0
    from ..models.build_phase_type_1 import BuildPhaseType1
    from ..models.build_phase_type_2 import BuildPhaseType2
    from ..models.build_phase_type_3 import BuildPhaseType3
    from ..models.build_phase_type_4 import BuildPhaseType4
    from ..models.build_phase_type_5 import BuildPhaseType5
    from ..models.build_phase_type_6 import BuildPhaseType6
    from ..models.build_phase_type_7 import BuildPhaseType7
    from ..models.build_phase_type_8 import BuildPhaseType8


T = TypeVar("T", bound="SupervisorStateType2")


@_attrs_define
class SupervisorStateType2:
    """
    Attributes:
        phase (BuildPhaseType0 | BuildPhaseType1 | BuildPhaseType2 | BuildPhaseType3 | BuildPhaseType4 | BuildPhaseType5
            | BuildPhaseType6 | BuildPhaseType7 | BuildPhaseType8):
        type_ (SupervisorStateType2Type):
    """

    phase: (
        BuildPhaseType0
        | BuildPhaseType1
        | BuildPhaseType2
        | BuildPhaseType3
        | BuildPhaseType4
        | BuildPhaseType5
        | BuildPhaseType6
        | BuildPhaseType7
        | BuildPhaseType8
    )
    type_: SupervisorStateType2Type
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.build_phase_type_0 import BuildPhaseType0  # noqa: PLC0415
        from ..models.build_phase_type_1 import BuildPhaseType1  # noqa: PLC0415
        from ..models.build_phase_type_2 import BuildPhaseType2  # noqa: PLC0415
        from ..models.build_phase_type_3 import BuildPhaseType3  # noqa: PLC0415
        from ..models.build_phase_type_4 import BuildPhaseType4  # noqa: PLC0415
        from ..models.build_phase_type_5 import BuildPhaseType5  # noqa: PLC0415
        from ..models.build_phase_type_6 import BuildPhaseType6  # noqa: PLC0415
        from ..models.build_phase_type_7 import BuildPhaseType7  # noqa: PLC0415

        phase: dict[str, Any]
        if isinstance(self.phase, BuildPhaseType0):
            phase = self.phase.to_dict()
        elif isinstance(self.phase, BuildPhaseType1):
            phase = self.phase.to_dict()
        elif isinstance(self.phase, BuildPhaseType2):
            phase = self.phase.to_dict()
        elif isinstance(self.phase, BuildPhaseType3):
            phase = self.phase.to_dict()
        elif isinstance(self.phase, BuildPhaseType4):
            phase = self.phase.to_dict()
        elif isinstance(self.phase, BuildPhaseType5):
            phase = self.phase.to_dict()
        elif isinstance(self.phase, BuildPhaseType6):
            phase = self.phase.to_dict()
        elif isinstance(self.phase, BuildPhaseType7):
            phase = self.phase.to_dict()
        else:
            phase = self.phase.to_dict()

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "phase": phase,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.build_phase_type_0 import BuildPhaseType0  # noqa: PLC0415
        from ..models.build_phase_type_1 import BuildPhaseType1  # noqa: PLC0415
        from ..models.build_phase_type_2 import BuildPhaseType2  # noqa: PLC0415
        from ..models.build_phase_type_3 import BuildPhaseType3  # noqa: PLC0415
        from ..models.build_phase_type_4 import BuildPhaseType4  # noqa: PLC0415
        from ..models.build_phase_type_5 import BuildPhaseType5  # noqa: PLC0415
        from ..models.build_phase_type_6 import BuildPhaseType6  # noqa: PLC0415
        from ..models.build_phase_type_7 import BuildPhaseType7  # noqa: PLC0415
        from ..models.build_phase_type_8 import BuildPhaseType8  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_phase(
            data: object,
        ) -> (
            BuildPhaseType0
            | BuildPhaseType1
            | BuildPhaseType2
            | BuildPhaseType3
            | BuildPhaseType4
            | BuildPhaseType5
            | BuildPhaseType6
            | BuildPhaseType7
            | BuildPhaseType8
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_build_phase_type_0 = BuildPhaseType0.from_dict(data)

                return componentsschemas_build_phase_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_build_phase_type_1 = BuildPhaseType1.from_dict(data)

                return componentsschemas_build_phase_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_build_phase_type_2 = BuildPhaseType2.from_dict(data)

                return componentsschemas_build_phase_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_build_phase_type_3 = BuildPhaseType3.from_dict(data)

                return componentsschemas_build_phase_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_build_phase_type_4 = BuildPhaseType4.from_dict(data)

                return componentsschemas_build_phase_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_build_phase_type_5 = BuildPhaseType5.from_dict(data)

                return componentsschemas_build_phase_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_build_phase_type_6 = BuildPhaseType6.from_dict(data)

                return componentsschemas_build_phase_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_build_phase_type_7 = BuildPhaseType7.from_dict(data)

                return componentsschemas_build_phase_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_build_phase_type_8 = BuildPhaseType8.from_dict(data)

            return componentsschemas_build_phase_type_8

        phase = _parse_phase(d.pop("phase"))

        type_ = SupervisorStateType2Type(d.pop("type"))

        supervisor_state_type_2 = cls(
            phase=phase,
            type_=type_,
        )

        supervisor_state_type_2.additional_properties = d
        return supervisor_state_type_2

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
