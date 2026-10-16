from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.process_configuration import ProcessConfiguration
    from ..models.server_configuration import ServerConfiguration


T = TypeVar("T", bound="RemoteServer")


@_attrs_define
class RemoteServer:
    """
    Attributes:
        settings (ServerConfiguration):
        process_configuration (ProcessConfiguration):
    """

    settings: ServerConfiguration
    process_configuration: ProcessConfiguration
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        settings = self.settings.to_dict()

        process_configuration = self.process_configuration.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "settings": settings,
                "process_configuration": process_configuration,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.process_configuration import ProcessConfiguration  # noqa: PLC0415
        from ..models.server_configuration import ServerConfiguration  # noqa: PLC0415

        d = dict(src_dict)
        settings = ServerConfiguration.from_dict(d.pop("settings"))

        process_configuration = ProcessConfiguration.from_dict(d.pop("process_configuration"))

        remote_server = cls(
            settings=settings,
            process_configuration=process_configuration,
        )

        remote_server.additional_properties = d
        return remote_server

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
