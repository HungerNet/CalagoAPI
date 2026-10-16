from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.supervisor_state_type_0 import SupervisorStateType0
    from ..models.supervisor_state_type_1 import SupervisorStateType1
    from ..models.supervisor_state_type_2 import SupervisorStateType2
    from ..models.supervisor_state_type_3 import SupervisorStateType3
    from ..models.supervisor_state_type_4 import SupervisorStateType4


T = TypeVar("T", bound="Status")


@_attrs_define
class Status:
    """
    Attributes:
        state (SupervisorStateType0 | SupervisorStateType1 | SupervisorStateType2 | SupervisorStateType3 |
            SupervisorStateType4):
        panel_version (str):
        cache_key (str):
        bin_name (str):
        log_len (int):
        build_id (int | None | Unset):
        started_at (None | str | Unset):
        finished_at (None | str | Unset):
        exit_code (int | None | Unset):
        failure_reason (None | str | Unset):
    """

    state: (
        SupervisorStateType0 | SupervisorStateType1 | SupervisorStateType2 | SupervisorStateType3 | SupervisorStateType4
    )
    panel_version: str
    cache_key: str
    bin_name: str
    log_len: int
    build_id: int | None | Unset = UNSET
    started_at: None | str | Unset = UNSET
    finished_at: None | str | Unset = UNSET
    exit_code: int | None | Unset = UNSET
    failure_reason: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.supervisor_state_type_0 import SupervisorStateType0  # noqa: PLC0415
        from ..models.supervisor_state_type_1 import SupervisorStateType1  # noqa: PLC0415
        from ..models.supervisor_state_type_2 import SupervisorStateType2  # noqa: PLC0415
        from ..models.supervisor_state_type_3 import SupervisorStateType3  # noqa: PLC0415

        state: dict[str, Any]
        if isinstance(self.state, SupervisorStateType0):
            state = self.state.to_dict()
        elif isinstance(self.state, SupervisorStateType1):
            state = self.state.to_dict()
        elif isinstance(self.state, SupervisorStateType2):
            state = self.state.to_dict()
        elif isinstance(self.state, SupervisorStateType3):
            state = self.state.to_dict()
        else:
            state = self.state.to_dict()

        panel_version = self.panel_version

        cache_key = self.cache_key

        bin_name = self.bin_name

        log_len = self.log_len

        build_id: int | None | Unset
        if isinstance(self.build_id, Unset):
            build_id = UNSET
        else:
            build_id = self.build_id

        started_at: None | str | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        else:
            started_at = self.started_at

        finished_at: None | str | Unset
        if isinstance(self.finished_at, Unset):
            finished_at = UNSET
        else:
            finished_at = self.finished_at

        exit_code: int | None | Unset
        if isinstance(self.exit_code, Unset):
            exit_code = UNSET
        else:
            exit_code = self.exit_code

        failure_reason: None | str | Unset
        if isinstance(self.failure_reason, Unset):
            failure_reason = UNSET
        else:
            failure_reason = self.failure_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
                "panel_version": panel_version,
                "cache_key": cache_key,
                "bin_name": bin_name,
                "log_len": log_len,
            }
        )
        if build_id is not UNSET:
            field_dict["build_id"] = build_id
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at
        if exit_code is not UNSET:
            field_dict["exit_code"] = exit_code
        if failure_reason is not UNSET:
            field_dict["failure_reason"] = failure_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.supervisor_state_type_0 import SupervisorStateType0  # noqa: PLC0415
        from ..models.supervisor_state_type_1 import SupervisorStateType1  # noqa: PLC0415
        from ..models.supervisor_state_type_2 import SupervisorStateType2  # noqa: PLC0415
        from ..models.supervisor_state_type_3 import SupervisorStateType3  # noqa: PLC0415
        from ..models.supervisor_state_type_4 import SupervisorStateType4  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_state(
            data: object,
        ) -> (
            SupervisorStateType0
            | SupervisorStateType1
            | SupervisorStateType2
            | SupervisorStateType3
            | SupervisorStateType4
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_supervisor_state_type_0 = SupervisorStateType0.from_dict(data)

                return componentsschemas_supervisor_state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_supervisor_state_type_1 = SupervisorStateType1.from_dict(data)

                return componentsschemas_supervisor_state_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_supervisor_state_type_2 = SupervisorStateType2.from_dict(data)

                return componentsschemas_supervisor_state_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_supervisor_state_type_3 = SupervisorStateType3.from_dict(data)

                return componentsschemas_supervisor_state_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_supervisor_state_type_4 = SupervisorStateType4.from_dict(data)

            return componentsschemas_supervisor_state_type_4

        state = _parse_state(d.pop("state"))

        panel_version = d.pop("panel_version")

        cache_key = d.pop("cache_key")

        bin_name = d.pop("bin_name")

        log_len = d.pop("log_len")

        def _parse_build_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        build_id = _parse_build_id(d.pop("build_id", UNSET))

        def _parse_started_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))

        def _parse_finished_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        finished_at = _parse_finished_at(d.pop("finished_at", UNSET))

        def _parse_exit_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        exit_code = _parse_exit_code(d.pop("exit_code", UNSET))

        def _parse_failure_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        failure_reason = _parse_failure_reason(d.pop("failure_reason", UNSET))

        status = cls(
            state=state,
            panel_version=panel_version,
            cache_key=cache_key,
            bin_name=bin_name,
            log_len=log_len,
            build_id=build_id,
            started_at=started_at,
            finished_at=finished_at,
            exit_code=exit_code,
            failure_reason=failure_reason,
        )

        status.additional_properties = d
        return status

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
