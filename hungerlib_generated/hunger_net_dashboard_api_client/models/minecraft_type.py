from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.minecraft_type_versions import MinecraftTypeVersions


T = TypeVar("T", bound="MinecraftType")


@_attrs_define
class MinecraftType:
    """
    Attributes:
        name (str):
        icon (str):
        color (str):
        homepage (str):
        deprecated (bool):
        experimental (bool):
        description (str):
        builds (int):
        versions (MinecraftTypeVersions):
    """

    name: str
    icon: str
    color: str
    homepage: str
    deprecated: bool
    experimental: bool
    description: str
    builds: int
    versions: MinecraftTypeVersions
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        icon = self.icon

        color = self.color

        homepage = self.homepage

        deprecated = self.deprecated

        experimental = self.experimental

        description = self.description

        builds = self.builds

        versions = self.versions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "icon": icon,
                "color": color,
                "homepage": homepage,
                "deprecated": deprecated,
                "experimental": experimental,
                "description": description,
                "builds": builds,
                "versions": versions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.minecraft_type_versions import MinecraftTypeVersions  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        icon = d.pop("icon")

        color = d.pop("color")

        homepage = d.pop("homepage")

        deprecated = d.pop("deprecated")

        experimental = d.pop("experimental")

        description = d.pop("description")

        builds = d.pop("builds")

        versions = MinecraftTypeVersions.from_dict(d.pop("versions"))

        minecraft_type = cls(
            name=name,
            icon=icon,
            color=color,
            homepage=homepage,
            deprecated=deprecated,
            experimental=experimental,
            description=description,
            builds=builds,
            versions=versions,
        )

        minecraft_type.additional_properties = d
        return minecraft_type

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
