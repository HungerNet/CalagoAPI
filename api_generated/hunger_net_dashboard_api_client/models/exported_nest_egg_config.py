from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.exported_nest_egg_config_files import ExportedNestEggConfigFiles
    from ..models.exported_nest_egg_config_startup import ExportedNestEggConfigStartup
    from ..models.exported_nest_egg_config_stop import ExportedNestEggConfigStop


T = TypeVar("T", bound="ExportedNestEggConfig")


@_attrs_define
class ExportedNestEggConfig:
    """
    Attributes:
        files (ExportedNestEggConfigFiles | Unset):
        startup (ExportedNestEggConfigStartup | Unset):
        stop (ExportedNestEggConfigStop | Unset):
    """

    files: ExportedNestEggConfigFiles | Unset = UNSET
    startup: ExportedNestEggConfigStartup | Unset = UNSET
    stop: ExportedNestEggConfigStop | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        files: dict[str, Any] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = self.files.to_dict()

        startup: dict[str, Any] | Unset = UNSET
        if not isinstance(self.startup, Unset):
            startup = self.startup.to_dict()

        stop: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stop, Unset):
            stop = self.stop.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if files is not UNSET:
            field_dict["files"] = files
        if startup is not UNSET:
            field_dict["startup"] = startup
        if stop is not UNSET:
            field_dict["stop"] = stop

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exported_nest_egg_config_files import ExportedNestEggConfigFiles  # noqa: PLC0415
        from ..models.exported_nest_egg_config_startup import ExportedNestEggConfigStartup  # noqa: PLC0415
        from ..models.exported_nest_egg_config_stop import ExportedNestEggConfigStop  # noqa: PLC0415

        d = dict(src_dict)
        _files = d.pop("files", UNSET)
        files: ExportedNestEggConfigFiles | Unset
        if isinstance(_files, Unset):
            files = UNSET
        else:
            files = ExportedNestEggConfigFiles.from_dict(_files)

        _startup = d.pop("startup", UNSET)
        startup: ExportedNestEggConfigStartup | Unset
        if isinstance(_startup, Unset):
            startup = UNSET
        else:
            startup = ExportedNestEggConfigStartup.from_dict(_startup)

        _stop = d.pop("stop", UNSET)
        stop: ExportedNestEggConfigStop | Unset
        if isinstance(_stop, Unset):
            stop = UNSET
        else:
            stop = ExportedNestEggConfigStop.from_dict(_stop)

        exported_nest_egg_config = cls(
            files=files,
            startup=startup,
            stop=stop,
        )

        exported_nest_egg_config.additional_properties = d
        return exported_nest_egg_config

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
