from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_remote_servers_server_install_response_200_environment import (
        GetApiRemoteServersServerInstallResponse200Environment,
    )


T = TypeVar("T", bound="GetApiRemoteServersServerInstallResponse200")


@_attrs_define
class GetApiRemoteServersServerInstallResponse200:
    """
    Attributes:
        container_image (str):
        entrypoint (str):
        script (str):
        environment (GetApiRemoteServersServerInstallResponse200Environment):
    """

    container_image: str
    entrypoint: str
    script: str
    environment: GetApiRemoteServersServerInstallResponse200Environment
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        container_image = self.container_image

        entrypoint = self.entrypoint

        script = self.script

        environment = self.environment.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "container_image": container_image,
                "entrypoint": entrypoint,
                "script": script,
                "environment": environment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_remote_servers_server_install_response_200_environment import (
            GetApiRemoteServersServerInstallResponse200Environment,  # noqa: PLC0415
        )

        d = dict(src_dict)
        container_image = d.pop("container_image")

        entrypoint = d.pop("entrypoint")

        script = d.pop("script")

        environment = GetApiRemoteServersServerInstallResponse200Environment.from_dict(d.pop("environment"))

        get_api_remote_servers_server_install_response_200 = cls(
            container_image=container_image,
            entrypoint=entrypoint,
            script=script,
            environment=environment,
        )

        get_api_remote_servers_server_install_response_200.additional_properties = d
        return get_api_remote_servers_server_install_response_200

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
