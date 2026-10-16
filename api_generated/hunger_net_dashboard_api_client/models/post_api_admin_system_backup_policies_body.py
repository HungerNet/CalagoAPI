from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.server_backup_kind import ServerBackupKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_retention import BackupRetention


T = TypeVar("T", bound="PostApiAdminSystemBackupPoliciesBody")


@_attrs_define
class PostApiAdminSystemBackupPoliciesBody:
    """
    Attributes:
        name (str):
        enabled (bool):
        cron (str):  Example: 0 0 0 * * *.
        parallelism (int):
        description (None | str | Unset):
        backup_configuration_uuid (None | Unset | UUID):
        kind (ServerBackupKind | Unset):
        retention (BackupRetention | Unset):
    """

    name: str
    enabled: bool
    cron: str
    parallelism: int
    description: None | str | Unset = UNSET
    backup_configuration_uuid: None | Unset | UUID = UNSET
    kind: ServerBackupKind | Unset = UNSET
    retention: BackupRetention | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        enabled = self.enabled

        cron = self.cron

        parallelism = self.parallelism

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        backup_configuration_uuid: None | str | Unset
        if isinstance(self.backup_configuration_uuid, Unset):
            backup_configuration_uuid = UNSET
        elif isinstance(self.backup_configuration_uuid, UUID):
            backup_configuration_uuid = str(self.backup_configuration_uuid)
        else:
            backup_configuration_uuid = self.backup_configuration_uuid

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        retention: dict[str, Any] | Unset = UNSET
        if not isinstance(self.retention, Unset):
            retention = self.retention.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "enabled": enabled,
                "cron": cron,
                "parallelism": parallelism,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if backup_configuration_uuid is not UNSET:
            field_dict["backup_configuration_uuid"] = backup_configuration_uuid
        if kind is not UNSET:
            field_dict["kind"] = kind
        if retention is not UNSET:
            field_dict["retention"] = retention

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_retention import BackupRetention  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        enabled = d.pop("enabled")

        cron = d.pop("cron")

        parallelism = d.pop("parallelism")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

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

        _kind = d.pop("kind", UNSET)
        kind: ServerBackupKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = ServerBackupKind(_kind)

        _retention = d.pop("retention", UNSET)
        retention: BackupRetention | Unset
        if isinstance(_retention, Unset):
            retention = UNSET
        else:
            retention = BackupRetention.from_dict(_retention)

        post_api_admin_system_backup_policies_body = cls(
            name=name,
            enabled=enabled,
            cron=cron,
            parallelism=parallelism,
            description=description,
            backup_configuration_uuid=backup_configuration_uuid,
            kind=kind,
            retention=retention,
        )

        post_api_admin_system_backup_policies_body.additional_properties = d
        return post_api_admin_system_backup_policies_body

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
