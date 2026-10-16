from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MetadataToml")


@_attrs_define
class MetadataToml:
    """
    Attributes:
        package_name (str):
        name (str):
        panel_version (str):
        license_text (None | str | Unset):
    """

    package_name: str
    name: str
    panel_version: str
    license_text: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        package_name = self.package_name

        name = self.name

        panel_version = self.panel_version

        license_text: None | str | Unset
        if isinstance(self.license_text, Unset):
            license_text = UNSET
        else:
            license_text = self.license_text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "package_name": package_name,
                "name": name,
                "panel_version": panel_version,
            }
        )
        if license_text is not UNSET:
            field_dict["license_text"] = license_text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        package_name = d.pop("package_name")

        name = d.pop("name")

        panel_version = d.pop("panel_version")

        def _parse_license_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        license_text = _parse_license_text(d.pop("license_text", UNSET))

        metadata_toml = cls(
            package_name=package_name,
            name=name,
            panel_version=panel_version,
            license_text=license_text,
        )

        metadata_toml.additional_properties = d
        return metadata_toml

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
