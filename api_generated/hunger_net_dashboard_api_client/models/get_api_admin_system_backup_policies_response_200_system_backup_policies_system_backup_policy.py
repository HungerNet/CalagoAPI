from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.server_backup_kind import ServerBackupKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_configuration import BackupConfiguration
    from ..models.backup_retention import BackupRetention


T = TypeVar("T", bound="GetApiAdminSystemBackupPoliciesResponse200SystemBackupPoliciesSystemBackupPolicy")


@_attrs_define
class GetApiAdminSystemBackupPoliciesResponse200SystemBackupPoliciesSystemBackupPolicy:
    """
    Attributes:
        uuid (UUID):
        name (str):
        enabled (bool):
        kind (ServerBackupKind):
        cron (str):  Example: 0 0 0 * * *.
        retention (BackupRetention):
        parallelism (int):
        total_nodes (int):
        total_database_agent_hosts (int):
        total_locations (int):
        total_servers (int):
        total_backups (int):
        created (datetime.datetime):
        backup_configuration (BackupConfiguration | None | Unset):
        description (None | str | Unset):
        triggered (datetime.datetime | None | Unset):
    """

    uuid: UUID
    name: str
    enabled: bool
    kind: ServerBackupKind
    cron: str
    retention: BackupRetention
    parallelism: int
    total_nodes: int
    total_database_agent_hosts: int
    total_locations: int
    total_servers: int
    total_backups: int
    created: datetime.datetime
    backup_configuration: BackupConfiguration | None | Unset = UNSET
    description: None | str | Unset = UNSET
    triggered: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.backup_configuration import BackupConfiguration  # noqa: PLC0415

        uuid = str(self.uuid)

        name = self.name

        enabled = self.enabled

        kind = self.kind.value

        cron = self.cron

        retention = self.retention.to_dict()

        parallelism = self.parallelism

        total_nodes = self.total_nodes

        total_database_agent_hosts = self.total_database_agent_hosts

        total_locations = self.total_locations

        total_servers = self.total_servers

        total_backups = self.total_backups

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

        triggered: None | str | Unset
        if isinstance(self.triggered, Unset):
            triggered = UNSET
        elif isinstance(self.triggered, datetime.datetime):
            triggered = self.triggered.isoformat()
        else:
            triggered = self.triggered

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "enabled": enabled,
                "kind": kind,
                "cron": cron,
                "retention": retention,
                "parallelism": parallelism,
                "total_nodes": total_nodes,
                "total_database_agent_hosts": total_database_agent_hosts,
                "total_locations": total_locations,
                "total_servers": total_servers,
                "total_backups": total_backups,
                "created": created,
            }
        )
        if backup_configuration is not UNSET:
            field_dict["backup_configuration"] = backup_configuration
        if description is not UNSET:
            field_dict["description"] = description
        if triggered is not UNSET:
            field_dict["triggered"] = triggered

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_configuration import BackupConfiguration  # noqa: PLC0415
        from ..models.backup_retention import BackupRetention  # noqa: PLC0415

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        enabled = d.pop("enabled")

        kind = ServerBackupKind(d.pop("kind"))

        cron = d.pop("cron")

        retention = BackupRetention.from_dict(d.pop("retention"))

        parallelism = d.pop("parallelism")

        total_nodes = d.pop("total_nodes")

        total_database_agent_hosts = d.pop("total_database_agent_hosts")

        total_locations = d.pop("total_locations")

        total_servers = d.pop("total_servers")

        total_backups = d.pop("total_backups")

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

        def _parse_triggered(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                triggered_type_0 = datetime.datetime.fromisoformat(data)

                return triggered_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        triggered = _parse_triggered(d.pop("triggered", UNSET))

        get_api_admin_system_backup_policies_response_200_system_backup_policies_system_backup_policy = cls(
            uuid=uuid,
            name=name,
            enabled=enabled,
            kind=kind,
            cron=cron,
            retention=retention,
            parallelism=parallelism,
            total_nodes=total_nodes,
            total_database_agent_hosts=total_database_agent_hosts,
            total_locations=total_locations,
            total_servers=total_servers,
            total_backups=total_backups,
            created=created,
            backup_configuration=backup_configuration,
            description=description,
            triggered=triggered,
        )

        get_api_admin_system_backup_policies_response_200_system_backup_policies_system_backup_policy.additional_properties = d
        return get_api_admin_system_backup_policies_response_200_system_backup_policies_system_backup_policy

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
