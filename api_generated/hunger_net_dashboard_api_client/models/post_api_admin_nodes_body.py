from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiAdminNodesBody")


@_attrs_define
class PostApiAdminNodesBody:
    """
    Attributes:
        location_uuid (UUID):
        name (str):
        deployment_enabled (bool):
        maintenance_enabled (bool):
        url (str):
        sftp_port (int):
        memory (int):
        disk (int):
        backup_configuration_uuid (None | Unset | UUID):
        description (None | str | Unset):
        public_url (None | str | Unset):
        sftp_host (None | str | Unset):
    """

    location_uuid: UUID
    name: str
    deployment_enabled: bool
    maintenance_enabled: bool
    url: str
    sftp_port: int
    memory: int
    disk: int
    backup_configuration_uuid: None | Unset | UUID = UNSET
    description: None | str | Unset = UNSET
    public_url: None | str | Unset = UNSET
    sftp_host: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location_uuid = str(self.location_uuid)

        name = self.name

        deployment_enabled = self.deployment_enabled

        maintenance_enabled = self.maintenance_enabled

        url = self.url

        sftp_port = self.sftp_port

        memory = self.memory

        disk = self.disk

        backup_configuration_uuid: None | str | Unset
        if isinstance(self.backup_configuration_uuid, Unset):
            backup_configuration_uuid = UNSET
        elif isinstance(self.backup_configuration_uuid, UUID):
            backup_configuration_uuid = str(self.backup_configuration_uuid)
        else:
            backup_configuration_uuid = self.backup_configuration_uuid

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        public_url: None | str | Unset
        if isinstance(self.public_url, Unset):
            public_url = UNSET
        else:
            public_url = self.public_url

        sftp_host: None | str | Unset
        if isinstance(self.sftp_host, Unset):
            sftp_host = UNSET
        else:
            sftp_host = self.sftp_host

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "location_uuid": location_uuid,
                "name": name,
                "deployment_enabled": deployment_enabled,
                "maintenance_enabled": maintenance_enabled,
                "url": url,
                "sftp_port": sftp_port,
                "memory": memory,
                "disk": disk,
            }
        )
        if backup_configuration_uuid is not UNSET:
            field_dict["backup_configuration_uuid"] = backup_configuration_uuid
        if description is not UNSET:
            field_dict["description"] = description
        if public_url is not UNSET:
            field_dict["public_url"] = public_url
        if sftp_host is not UNSET:
            field_dict["sftp_host"] = sftp_host

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        location_uuid = UUID(d.pop("location_uuid"))

        name = d.pop("name")

        deployment_enabled = d.pop("deployment_enabled")

        maintenance_enabled = d.pop("maintenance_enabled")

        url = d.pop("url")

        sftp_port = d.pop("sftp_port")

        memory = d.pop("memory")

        disk = d.pop("disk")

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

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_public_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_url = _parse_public_url(d.pop("public_url", UNSET))

        def _parse_sftp_host(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sftp_host = _parse_sftp_host(d.pop("sftp_host", UNSET))

        post_api_admin_nodes_body = cls(
            location_uuid=location_uuid,
            name=name,
            deployment_enabled=deployment_enabled,
            maintenance_enabled=maintenance_enabled,
            url=url,
            sftp_port=sftp_port,
            memory=memory,
            disk=disk,
            backup_configuration_uuid=backup_configuration_uuid,
            description=description,
            public_url=public_url,
            sftp_host=sftp_host,
        )

        post_api_admin_nodes_body.additional_properties = d
        return post_api_admin_nodes_body

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
