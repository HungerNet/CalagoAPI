from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApiClientServersServerMinecraftVersionsInstallBody")


@_attrs_define
class PostApiClientServersServerMinecraftVersionsInstallBody:
    """
    Attributes:
        build_uuid (UUID):
        truncate_directory (bool):
        accept_eula (bool):
    """

    build_uuid: UUID
    truncate_directory: bool
    accept_eula: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        build_uuid = str(self.build_uuid)

        truncate_directory = self.truncate_directory

        accept_eula = self.accept_eula

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "build_uuid": build_uuid,
                "truncate_directory": truncate_directory,
                "accept_eula": accept_eula,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        build_uuid = UUID(d.pop("build_uuid"))

        truncate_directory = d.pop("truncate_directory")

        accept_eula = d.pop("accept_eula")

        post_api_client_servers_server_minecraft_versions_install_body = cls(
            build_uuid=build_uuid,
            truncate_directory=truncate_directory,
            accept_eula=accept_eula,
        )

        post_api_client_servers_server_minecraft_versions_install_body.additional_properties = d
        return post_api_client_servers_server_minecraft_versions_install_body

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
