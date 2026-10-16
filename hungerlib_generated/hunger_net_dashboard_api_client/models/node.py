from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_configuration import BackupConfiguration
    from ..models.location import Location


T = TypeVar("T", bound="Node")


@_attrs_define
class Node:
    """
    Attributes:
        uuid (UUID):
        location (Location):
        name (str):
        deployment_enabled (bool):
        maintenance_enabled (bool):
        url (str):
        sftp_port (int):
        memory (int):
        disk (int):
        created (datetime.datetime):
        backup_configuration (BackupConfiguration | None | Unset):
        description (None | str | Unset):
        public_url (None | str | Unset):
        sftp_host (None | str | Unset):
    """

    uuid: UUID
    location: Location
    name: str
    deployment_enabled: bool
    maintenance_enabled: bool
    url: str
    sftp_port: int
    memory: int
    disk: int
    created: datetime.datetime
    backup_configuration: BackupConfiguration | None | Unset = UNSET
    description: None | str | Unset = UNSET
    public_url: None | str | Unset = UNSET
    sftp_host: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.backup_configuration import BackupConfiguration  # noqa: PLC0415

        uuid = str(self.uuid)

        location = self.location.to_dict()

        name = self.name

        deployment_enabled = self.deployment_enabled

        maintenance_enabled = self.maintenance_enabled

        url = self.url

        sftp_port = self.sftp_port

        memory = self.memory

        disk = self.disk

        created = self.created.isoformat()

        backup_configuration: dict[str, Any] | None | Unset
        if isinstance(self.backup_configuration, Unset):
            backup_configuration = UNSET
        elif isinstance(self.backup_configuration, BackupConfiguration):
            backup_configuration = self.backup_configuration.to_dict()
        else:
            backup_configuration = self.backup_configuration

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
                "uuid": uuid,
                "location": location,
                "name": name,
                "deployment_enabled": deployment_enabled,
                "maintenance_enabled": maintenance_enabled,
                "url": url,
                "sftp_port": sftp_port,
                "memory": memory,
                "disk": disk,
                "created": created,
            }
        )
        if backup_configuration is not UNSET:
            field_dict["backup_configuration"] = backup_configuration
        if description is not UNSET:
            field_dict["description"] = description
        if public_url is not UNSET:
            field_dict["public_url"] = public_url
        if sftp_host is not UNSET:
            field_dict["sftp_host"] = sftp_host

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_configuration import BackupConfiguration  # noqa: PLC0415
        from ..models.location import Location  # noqa: PLC0415

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        location = Location.from_dict(d.pop("location"))

        name = d.pop("name")

        deployment_enabled = d.pop("deployment_enabled")

        maintenance_enabled = d.pop("maintenance_enabled")

        url = d.pop("url")

        sftp_port = d.pop("sftp_port")

        memory = d.pop("memory")

        disk = d.pop("disk")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        def _parse_backup_configuration(data: object) -> BackupConfiguration | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                backup_configuration_type_1 = BackupConfiguration.from_dict(data)

                return backup_configuration_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BackupConfiguration | None | Unset, data)

        backup_configuration = _parse_backup_configuration(d.pop("backup_configuration", UNSET))

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

        node = cls(
            uuid=uuid,
            location=location,
            name=name,
            deployment_enabled=deployment_enabled,
            maintenance_enabled=maintenance_enabled,
            url=url,
            sftp_port=sftp_port,
            memory=memory,
            disk=disk,
            created=created,
            backup_configuration=backup_configuration,
            description=description,
            public_url=public_url,
            sftp_host=sftp_host,
        )

        node.additional_properties = d
        return node

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
