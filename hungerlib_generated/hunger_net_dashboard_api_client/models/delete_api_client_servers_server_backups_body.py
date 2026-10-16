from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.server_backup_selector_type_0 import ServerBackupSelectorType0


T = TypeVar("T", bound="DeleteApiClientServersServerBackupsBody")


@_attrs_define
class DeleteApiClientServersServerBackupsBody:
    """
    Attributes:
        selector (ServerBackupSelectorType0):
    """

    selector: ServerBackupSelectorType0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.server_backup_selector_type_0 import ServerBackupSelectorType0  # noqa: PLC0415

        selector: dict[str, Any]
        if isinstance(self.selector, ServerBackupSelectorType0):
            selector = self.selector.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "selector": selector,
            }
        )

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

        delete_api_client_servers_server_backups_body = cls(
            selector=selector,
        )

        delete_api_client_servers_server_backups_body.additional_properties = d
        return delete_api_client_servers_server_backups_body

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
