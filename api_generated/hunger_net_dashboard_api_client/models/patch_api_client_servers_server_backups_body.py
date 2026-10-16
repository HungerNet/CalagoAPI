from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_backup_selector_type_0 import ServerBackupSelectorType0


T = TypeVar("T", bound="PatchApiClientServersServerBackupsBody")


@_attrs_define
class PatchApiClientServersServerBackupsBody:
    """
    Attributes:
        selector (ServerBackupSelectorType0):
        backup_group_uuid (None | Unset | UUID):
        locked (bool | None | Unset):
    """

    selector: ServerBackupSelectorType0
    backup_group_uuid: None | Unset | UUID = UNSET
    locked: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.server_backup_selector_type_0 import ServerBackupSelectorType0  # noqa: PLC0415

        selector: dict[str, Any]
        if isinstance(self.selector, ServerBackupSelectorType0):
            selector = self.selector.to_dict()

        backup_group_uuid: None | str | Unset
        if isinstance(self.backup_group_uuid, Unset):
            backup_group_uuid = UNSET
        elif isinstance(self.backup_group_uuid, UUID):
            backup_group_uuid = str(self.backup_group_uuid)
        else:
            backup_group_uuid = self.backup_group_uuid

        locked: bool | None | Unset
        if isinstance(self.locked, Unset):
            locked = UNSET
        else:
            locked = self.locked

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "selector": selector,
            }
        )
        if backup_group_uuid is not UNSET:
            field_dict["backup_group_uuid"] = backup_group_uuid
        if locked is not UNSET:
            field_dict["locked"] = locked

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_backup_selector_type_0 import ServerBackupSelectorType0  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_selector(data: object) -> ServerBackupSelectorType0:
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_server_backup_selector_type_0 = ServerBackupSelectorType0.from_dict(data)

            return componentsschemas_server_backup_selector_type_0

        selector = _parse_selector(d.pop("selector"))

        def _parse_backup_group_uuid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                backup_group_uuid_type_0 = UUID(data)

                return backup_group_uuid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        backup_group_uuid = _parse_backup_group_uuid(d.pop("backup_group_uuid", UNSET))

        def _parse_locked(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        locked = _parse_locked(d.pop("locked", UNSET))

        patch_api_client_servers_server_backups_body = cls(
            selector=selector,
            backup_group_uuid=backup_group_uuid,
            locked=locked,
        )

        patch_api_client_servers_server_backups_body.additional_properties = d
        return patch_api_client_servers_server_backups_body

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
