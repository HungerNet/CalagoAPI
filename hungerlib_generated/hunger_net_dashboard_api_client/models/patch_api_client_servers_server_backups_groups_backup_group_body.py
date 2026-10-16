from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_retention import BackupRetention


T = TypeVar("T", bound="PatchApiClientServersServerBackupsGroupsBackupGroupBody")


@_attrs_define
class PatchApiClientServersServerBackupsGroupsBackupGroupBody:
    """
    Attributes:
        name (None | str | Unset):
        retention (BackupRetention | Unset):
    """

    name: None | str | Unset = UNSET
    retention: BackupRetention | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        retention: dict[str, Any] | Unset = UNSET
        if not isinstance(self.retention, Unset):
            retention = self.retention.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if retention is not UNSET:
            field_dict["retention"] = retention

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_retention import BackupRetention  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _retention = d.pop("retention", UNSET)
        retention: BackupRetention | Unset
        if isinstance(_retention, Unset):
            retention = UNSET
        else:
            retention = BackupRetention.from_dict(_retention)

        patch_api_client_servers_server_backups_groups_backup_group_body = cls(
            name=name,
            retention=retention,
        )

        patch_api_client_servers_server_backups_groups_backup_group_body.additional_properties = d
        return patch_api_client_servers_server_backups_groups_backup_group_body

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
