from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.minecraft_build import MinecraftBuild


T = TypeVar("T", bound="GetApiClientServersServerMinecraftVersionsInstalledResponse200BuildType1")


@_attrs_define
class GetApiClientServersServerMinecraftVersionsInstalledResponse200BuildType1:
    """
    Attributes:
        build (MinecraftBuild):
        latest (MinecraftBuild):
    """

    build: MinecraftBuild
    latest: MinecraftBuild
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        build = self.build.to_dict()

        latest = self.latest.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "build": build,
                "latest": latest,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.minecraft_build import MinecraftBuild  # noqa: PLC0415

        d = dict(src_dict)
        build = MinecraftBuild.from_dict(d.pop("build"))

        latest = MinecraftBuild.from_dict(d.pop("latest"))

        get_api_client_servers_server_minecraft_versions_installed_response_200_build_type_1 = cls(
            build=build,
            latest=latest,
        )

        get_api_client_servers_server_minecraft_versions_installed_response_200_build_type_1.additional_properties = d
        return get_api_client_servers_server_minecraft_versions_installed_response_200_build_type_1

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
