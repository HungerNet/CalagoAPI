from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.server_auto_start_behavior import ServerAutoStartBehavior

T = TypeVar("T", bound="PutApiClientServersServerSettingsAutoStartBody")


@_attrs_define
class PutApiClientServersServerSettingsAutoStartBody:
    """
    Attributes:
        behavior (ServerAutoStartBehavior):
    """

    behavior: ServerAutoStartBehavior
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        behavior = self.behavior.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "behavior": behavior,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        behavior = ServerAutoStartBehavior(d.pop("behavior"))

        put_api_client_servers_server_settings_auto_start_body = cls(
            behavior=behavior,
        )

        put_api_client_servers_server_settings_auto_start_body.additional_properties = d
        return put_api_client_servers_server_settings_auto_start_body

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
