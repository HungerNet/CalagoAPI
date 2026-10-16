from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApiRemoteServersServerStartupVariablesBody")


@_attrs_define
class PutApiRemoteServersServerStartupVariablesBody:
    """
    Attributes:
        env_variable (str):
        value (str):
        schedule_uuid (None | Unset | UUID):
    """

    env_variable: str
    value: str
    schedule_uuid: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        env_variable = self.env_variable

        value = self.value

        schedule_uuid: None | str | Unset
        if isinstance(self.schedule_uuid, Unset):
            schedule_uuid = UNSET
        elif isinstance(self.schedule_uuid, UUID):
            schedule_uuid = str(self.schedule_uuid)
        else:
            schedule_uuid = self.schedule_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "env_variable": env_variable,
                "value": value,
            }
        )
        if schedule_uuid is not UNSET:
            field_dict["schedule_uuid"] = schedule_uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        env_variable = d.pop("env_variable")

        value = d.pop("value")

        def _parse_schedule_uuid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                schedule_uuid_type_0 = UUID(data)

                return schedule_uuid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        schedule_uuid = _parse_schedule_uuid(d.pop("schedule_uuid", UNSET))

        put_api_remote_servers_server_startup_variables_body = cls(
            env_variable=env_variable,
            value=value,
            schedule_uuid=schedule_uuid,
        )

        put_api_remote_servers_server_startup_variables_body.additional_properties = d
        return put_api_remote_servers_server_startup_variables_body

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
