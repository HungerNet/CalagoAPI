from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_agent_host_types import DatabaseAgentHostTypes


T = TypeVar("T", bound="PatchApiAdminDatabaseAgentHostsDatabaseAgentHostBody")


@_attrs_define
class PatchApiAdminDatabaseAgentHostsDatabaseAgentHostBody:
    """
    Attributes:
        name (None | str | Unset):
        description (None | str | Unset):
        deployment_enabled (bool | None | Unset):
        maintenance_enabled (bool | None | Unset):
        url (None | str | Unset):
        memory (int | None | Unset):
        disk (int | None | Unset):
        types (DatabaseAgentHostTypes | None | Unset):
    """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    deployment_enabled: bool | None | Unset = UNSET
    maintenance_enabled: bool | None | Unset = UNSET
    url: None | str | Unset = UNSET
    memory: int | None | Unset = UNSET
    disk: int | None | Unset = UNSET
    types: DatabaseAgentHostTypes | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.database_agent_host_types import DatabaseAgentHostTypes  # noqa: PLC0415

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        deployment_enabled: bool | None | Unset
        if isinstance(self.deployment_enabled, Unset):
            deployment_enabled = UNSET
        else:
            deployment_enabled = self.deployment_enabled

        maintenance_enabled: bool | None | Unset
        if isinstance(self.maintenance_enabled, Unset):
            maintenance_enabled = UNSET
        else:
            maintenance_enabled = self.maintenance_enabled

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        memory: int | None | Unset
        if isinstance(self.memory, Unset):
            memory = UNSET
        else:
            memory = self.memory

        disk: int | None | Unset
        if isinstance(self.disk, Unset):
            disk = UNSET
        else:
            disk = self.disk

        types: dict[str, Any] | None | Unset
        if isinstance(self.types, Unset):
            types = UNSET
        elif isinstance(self.types, DatabaseAgentHostTypes):
            types = self.types.to_dict()
        else:
            types = self.types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if deployment_enabled is not UNSET:
            field_dict["deployment_enabled"] = deployment_enabled
        if maintenance_enabled is not UNSET:
            field_dict["maintenance_enabled"] = maintenance_enabled
        if url is not UNSET:
            field_dict["url"] = url
        if memory is not UNSET:
            field_dict["memory"] = memory
        if disk is not UNSET:
            field_dict["disk"] = disk
        if types is not UNSET:
            field_dict["types"] = types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_agent_host_types import DatabaseAgentHostTypes  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_deployment_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        deployment_enabled = _parse_deployment_enabled(d.pop("deployment_enabled", UNSET))

        def _parse_maintenance_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        maintenance_enabled = _parse_maintenance_enabled(d.pop("maintenance_enabled", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_memory(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        memory = _parse_memory(d.pop("memory", UNSET))

        def _parse_disk(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        disk = _parse_disk(d.pop("disk", UNSET))

        def _parse_types(data: object) -> DatabaseAgentHostTypes | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                types_type_1 = DatabaseAgentHostTypes.from_dict(data)

                return types_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatabaseAgentHostTypes | None | Unset, data)

        types = _parse_types(d.pop("types", UNSET))

        patch_api_admin_database_agent_hosts_database_agent_host_body = cls(
            name=name,
            description=description,
            deployment_enabled=deployment_enabled,
            maintenance_enabled=maintenance_enabled,
            url=url,
            memory=memory,
            disk=disk,
            types=types,
        )

        patch_api_admin_database_agent_hosts_database_agent_host_body.additional_properties = d
        return patch_api_admin_database_agent_hosts_database_agent_host_body

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
