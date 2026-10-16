from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.setup_probe_docker import SetupProbeDocker


T = TypeVar("T", bound="SetupProbe")


@_attrs_define
class SetupProbe:
    """
    Attributes:
        version (str):
        container (bool):
        architecture (str):
        cpu_count (int):
        memory_bytes (int):
        disk_bytes (int):
        ips (list[str]):
        api_port (int):
        sftp_port (int):
        docker (SetupProbeDocker):
    """

    version: str
    container: bool
    architecture: str
    cpu_count: int
    memory_bytes: int
    disk_bytes: int
    ips: list[str]
    api_port: int
    sftp_port: int
    docker: SetupProbeDocker
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        container = self.container

        architecture = self.architecture

        cpu_count = self.cpu_count

        memory_bytes = self.memory_bytes

        disk_bytes = self.disk_bytes

        ips = self.ips

        api_port = self.api_port

        sftp_port = self.sftp_port

        docker = self.docker.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
                "container": container,
                "architecture": architecture,
                "cpu_count": cpu_count,
                "memory_bytes": memory_bytes,
                "disk_bytes": disk_bytes,
                "ips": ips,
                "api_port": api_port,
                "sftp_port": sftp_port,
                "docker": docker,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.setup_probe_docker import SetupProbeDocker  # noqa: PLC0415

        d = dict(src_dict)
        version = d.pop("version")

        container = d.pop("container")

        architecture = d.pop("architecture")

        cpu_count = d.pop("cpu_count")

        memory_bytes = d.pop("memory_bytes")

        disk_bytes = d.pop("disk_bytes")

        ips = cast(list[str], d.pop("ips"))

        api_port = d.pop("api_port")

        sftp_port = d.pop("sftp_port")

        docker = SetupProbeDocker.from_dict(d.pop("docker"))

        setup_probe = cls(
            version=version,
            container=container,
            architecture=architecture,
            cpu_count=cpu_count,
            memory_bytes=memory_bytes,
            disk_bytes=disk_bytes,
            ips=ips,
            api_port=api_port,
            sftp_port=sftp_port,
            docker=docker,
        )

        setup_probe.additional_properties = d
        return setup_probe

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
