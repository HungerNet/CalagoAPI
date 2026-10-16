from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_api_client_servers_server_minecraft_versions_installed_response_200_build_type_1 import (
        GetApiClientServersServerMinecraftVersionsInstalledResponse200BuildType1,
    )


T = TypeVar("T", bound="GetApiClientServersServerMinecraftVersionsInstalledResponse200")


@_attrs_define
class GetApiClientServersServerMinecraftVersionsInstalledResponse200:
    """
    Attributes:
        build (GetApiClientServersServerMinecraftVersionsInstalledResponse200BuildType1 | None | Unset):
    """

    build: GetApiClientServersServerMinecraftVersionsInstalledResponse200BuildType1 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_api_client_servers_server_minecraft_versions_installed_response_200_build_type_1 import (
            GetApiClientServersServerMinecraftVersionsInstalledResponse200BuildType1,  # noqa: PLC0415
        )

        build: dict[str, Any] | None | Unset
        if isinstance(self.build, Unset):
            build = UNSET
        elif isinstance(self.build, GetApiClientServersServerMinecraftVersionsInstalledResponse200BuildType1):
            build = self.build.to_dict()
        else:
            build = self.build

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if build is not UNSET:
            field_dict["build"] = build

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_client_servers_server_minecraft_versions_installed_response_200_build_type_1 import (
            GetApiClientServersServerMinecraftVersionsInstalledResponse200BuildType1,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_build(
            data: object,
        ) -> GetApiClientServersServerMinecraftVersionsInstalledResponse200BuildType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                build_type_1 = GetApiClientServersServerMinecraftVersionsInstalledResponse200BuildType1.from_dict(data)

                return build_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetApiClientServersServerMinecraftVersionsInstalledResponse200BuildType1 | None | Unset, data)

        build = _parse_build(d.pop("build", UNSET))

        get_api_client_servers_server_minecraft_versions_installed_response_200 = cls(
            build=build,
        )

        get_api_client_servers_server_minecraft_versions_installed_response_200.additional_properties = d
        return get_api_client_servers_server_minecraft_versions_installed_response_200

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
