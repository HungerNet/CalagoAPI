from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseAgentHostTypeSettings")


@_attrs_define
class DatabaseAgentHostTypeSettings:
    """
    Attributes:
        enabled (bool | Unset):
        public_host (None | str | Unset):
        public_port (int | None | Unset):
    """

    enabled: bool | Unset = UNSET
    public_host: None | str | Unset = UNSET
    public_port: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        public_host: None | str | Unset
        if isinstance(self.public_host, Unset):
            public_host = UNSET
        else:
            public_host = self.public_host

        public_port: int | None | Unset
        if isinstance(self.public_port, Unset):
            public_port = UNSET
        else:
            public_port = self.public_port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if public_host is not UNSET:
            field_dict["public_host"] = public_host
        if public_port is not UNSET:
            field_dict["public_port"] = public_port

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        def _parse_public_host(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_host = _parse_public_host(d.pop("public_host", UNSET))

        def _parse_public_port(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        public_port = _parse_public_port(d.pop("public_port", UNSET))

        database_agent_host_type_settings = cls(
            enabled=enabled,
            public_host=public_host,
            public_port=public_port,
        )

        database_agent_host_type_settings.additional_properties = d
        return database_agent_host_type_settings

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
