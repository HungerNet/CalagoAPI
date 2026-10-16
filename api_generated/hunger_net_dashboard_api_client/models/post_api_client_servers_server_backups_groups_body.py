from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_retention import BackupRetention


T = TypeVar("T", bound="PostApiClientServersServerBackupsGroupsBody")


@_attrs_define
class PostApiClientServersServerBackupsGroupsBody:
    """
    Attributes:
        name (str):
        retention (BackupRetention | Unset):
    """

    name: str
    retention: BackupRetention | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        retention: dict[str, Any] | Unset = UNSET
        if not isinstance(self.retention, Unset):
            retention = self.retention.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if retention is not UNSET:
            field_dict["retention"] = retention

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_retention import BackupRetention  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        _retention = d.pop("retention", UNSET)
        retention: BackupRetention | Unset
        if isinstance(_retention, Unset):
            retention = UNSET
        else:
            retention = BackupRetention.from_dict(_retention)

        post_api_client_servers_server_backups_groups_body = cls(
            name=name,
            retention=retention,
        )

        post_api_client_servers_server_backups_groups_body.additional_properties = d
        return post_api_client_servers_server_backups_groups_body

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
