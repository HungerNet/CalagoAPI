from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchApiAdminNodesNodeBody")


@_attrs_define
class PatchApiAdminNodesNodeBody:
    """
    Attributes:
        location_uuid (None | Unset | UUID):
        backup_configuration_uuid (None | Unset | UUID):
        name (None | str | Unset):
        description (None | str | Unset):
        deployment_enabled (bool | None | Unset):
        maintenance_enabled (bool | None | Unset):
        public_url (None | str | Unset):
        url (None | str | Unset):
        sftp_host (None | str | Unset):
        sftp_port (int | None | Unset):
        memory (int | None | Unset):
        disk (int | None | Unset):
    """

    location_uuid: None | Unset | UUID = UNSET
    backup_configuration_uuid: None | Unset | UUID = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    deployment_enabled: bool | None | Unset = UNSET
    maintenance_enabled: bool | None | Unset = UNSET
    public_url: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    sftp_host: None | str | Unset = UNSET
    sftp_port: int | None | Unset = UNSET
    memory: int | None | Unset = UNSET
    disk: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location_uuid: None | str | Unset
        if isinstance(self.location_uuid, Unset):
            location_uuid = UNSET
        elif isinstance(self.location_uuid, UUID):
            location_uuid = str(self.location_uuid)
        else:
            location_uuid = self.location_uuid

        backup_configuration_uuid: None | str | Unset
        if isinstance(self.backup_configuration_uuid, Unset):
            backup_configuration_uuid = UNSET
        elif isinstance(self.backup_configuration_uuid, UUID):
            backup_configuration_uuid = str(self.backup_configuration_uuid)
        else:
            backup_configuration_uuid = self.backup_configuration_uuid

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

        public_url: None | str | Unset
        if isinstance(self.public_url, Unset):
            public_url = UNSET
        else:
            public_url = self.public_url

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        sftp_host: None | str | Unset
        if isinstance(self.sftp_host, Unset):
            sftp_host = UNSET
        else:
            sftp_host = self.sftp_host

        sftp_port: int | None | Unset
        if isinstance(self.sftp_port, Unset):
            sftp_port = UNSET
        else:
            sftp_port = self.sftp_port

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if location_uuid is not UNSET:
            field_dict["location_uuid"] = location_uuid
        if backup_configuration_uuid is not UNSET:
            field_dict["backup_configuration_uuid"] = backup_configuration_uuid
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if deployment_enabled is not UNSET:
            field_dict["deployment_enabled"] = deployment_enabled
        if maintenance_enabled is not UNSET:
            field_dict["maintenance_enabled"] = maintenance_enabled
        if public_url is not UNSET:
            field_dict["public_url"] = public_url
        if url is not UNSET:
            field_dict["url"] = url
        if sftp_host is not UNSET:
            field_dict["sftp_host"] = sftp_host
        if sftp_port is not UNSET:
            field_dict["sftp_port"] = sftp_port
        if memory is not UNSET:
            field_dict["memory"] = memory
        if disk is not UNSET:
            field_dict["disk"] = disk

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_location_uuid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                location_uuid_type_0 = UUID(data)

                return location_uuid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        location_uuid = _parse_location_uuid(d.pop("location_uuid", UNSET))

        def _parse_backup_configuration_uuid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                backup_configuration_uuid_type_0 = UUID(data)

                return backup_configuration_uuid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        backup_configuration_uuid = _parse_backup_configuration_uuid(d.pop("backup_configuration_uuid", UNSET))

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

        def _parse_public_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_url = _parse_public_url(d.pop("public_url", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_sftp_host(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sftp_host = _parse_sftp_host(d.pop("sftp_host", UNSET))

        def _parse_sftp_port(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sftp_port = _parse_sftp_port(d.pop("sftp_port", UNSET))

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

        patch_api_admin_nodes_node_body = cls(
            location_uuid=location_uuid,
            backup_configuration_uuid=backup_configuration_uuid,
            name=name,
            description=description,
            deployment_enabled=deployment_enabled,
            maintenance_enabled=maintenance_enabled,
            public_url=public_url,
            url=url,
            sftp_host=sftp_host,
            sftp_port=sftp_port,
            memory=memory,
            disk=disk,
        )

        patch_api_admin_nodes_node_body.additional_properties = d
        return patch_api_admin_nodes_node_body

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
