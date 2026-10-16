from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_agent_host_types import DatabaseAgentHostTypes


T = TypeVar("T", bound="PostApiAdminDatabaseAgentHostsBody")


@_attrs_define
class PostApiAdminDatabaseAgentHostsBody:
    """
    Attributes:
        name (str):
        deployment_enabled (bool):
        maintenance_enabled (bool):
        url (str):
        memory (int):
        disk (int):
        description (None | str | Unset):
        types (DatabaseAgentHostTypes | Unset):
    """

    name: str
    deployment_enabled: bool
    maintenance_enabled: bool
    url: str
    memory: int
    disk: int
    description: None | str | Unset = UNSET
    types: DatabaseAgentHostTypes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        deployment_enabled = self.deployment_enabled

        maintenance_enabled = self.maintenance_enabled

        url = self.url

        memory = self.memory

        disk = self.disk

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        types: dict[str, Any] | Unset = UNSET
        if not isinstance(self.types, Unset):
            types = self.types.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "deployment_enabled": deployment_enabled,
                "maintenance_enabled": maintenance_enabled,
                "url": url,
                "memory": memory,
                "disk": disk,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if types is not UNSET:
            field_dict["types"] = types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_agent_host_types import DatabaseAgentHostTypes  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        deployment_enabled = d.pop("deployment_enabled")

        maintenance_enabled = d.pop("maintenance_enabled")

        url = d.pop("url")

        memory = d.pop("memory")

        disk = d.pop("disk")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _types = d.pop("types", UNSET)
        types: DatabaseAgentHostTypes | Unset
        if isinstance(_types, Unset):
            types = UNSET
        else:
            types = DatabaseAgentHostTypes.from_dict(_types)

        post_api_admin_database_agent_hosts_body = cls(
            name=name,
            deployment_enabled=deployment_enabled,
            maintenance_enabled=maintenance_enabled,
            url=url,
            memory=memory,
            disk=disk,
            description=description,
            types=types,
        )

        post_api_admin_database_agent_hosts_body.additional_properties = d
        return post_api_admin_database_agent_hosts_body

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
