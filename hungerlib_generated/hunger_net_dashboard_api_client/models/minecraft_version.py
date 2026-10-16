from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.minecraft_build import MinecraftBuild


T = TypeVar("T", bound="MinecraftVersion")


@_attrs_define
class MinecraftVersion:
    """
    Attributes:
        id (str):
        type_ (str):
        supported (bool):
        java (int):
        builds (int):
        created (datetime.datetime):
        latest (MinecraftBuild):
    """

    id: str
    type_: str
    supported: bool
    java: int
    builds: int
    created: datetime.datetime
    latest: MinecraftBuild
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        supported = self.supported

        java = self.java

        builds = self.builds

        created = self.created.isoformat()

        latest = self.latest.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "supported": supported,
                "java": java,
                "builds": builds,
                "created": created,
                "latest": latest,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.minecraft_build import MinecraftBuild  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        type_ = d.pop("type")

        supported = d.pop("supported")

        java = d.pop("java")

        builds = d.pop("builds")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        latest = MinecraftBuild.from_dict(d.pop("latest"))

        minecraft_version = cls(
            id=id,
            type_=type_,
            supported=supported,
            java=java,
            builds=builds,
            created=created,
            latest=latest,
        )

        minecraft_version.additional_properties = d
        return minecraft_version

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
