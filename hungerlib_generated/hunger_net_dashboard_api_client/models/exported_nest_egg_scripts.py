from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.exported_nest_egg_scripts_installation import ExportedNestEggScriptsInstallation


T = TypeVar("T", bound="ExportedNestEggScripts")


@_attrs_define
class ExportedNestEggScripts:
    """
    Attributes:
        installation (ExportedNestEggScriptsInstallation):
    """

    installation: ExportedNestEggScriptsInstallation
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        installation = self.installation.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "installation": installation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exported_nest_egg_scripts_installation import ExportedNestEggScriptsInstallation  # noqa: PLC0415

        d = dict(src_dict)
        installation = ExportedNestEggScriptsInstallation.from_dict(d.pop("installation"))

        exported_nest_egg_scripts = cls(
            installation=installation,
        )

        exported_nest_egg_scripts.additional_properties = d
        return exported_nest_egg_scripts

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
