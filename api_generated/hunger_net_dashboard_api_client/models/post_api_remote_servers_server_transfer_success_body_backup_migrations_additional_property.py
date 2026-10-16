from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_adapter import BackupAdapter
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiRemoteServersServerTransferSuccessBodyBackupMigrationsAdditionalProperty")


@_attrs_define
class PostApiRemoteServersServerTransferSuccessBodyBackupMigrationsAdditionalProperty:
    """
    Attributes:
        checksum (str):
        checksum_type (str):
        browsable (bool):
        streaming (bool):
        adapter (BackupAdapter | None | Unset):
    """

    checksum: str
    checksum_type: str
    browsable: bool
    streaming: bool
    adapter: BackupAdapter | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        checksum = self.checksum

        checksum_type = self.checksum_type

        browsable = self.browsable

        streaming = self.streaming

        adapter: None | str | Unset
        if isinstance(self.adapter, Unset):
            adapter = UNSET
        elif isinstance(self.adapter, BackupAdapter):
            adapter = self.adapter.value
        else:
            adapter = self.adapter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "checksum": checksum,
                "checksum_type": checksum_type,
                "browsable": browsable,
                "streaming": streaming,
            }
        )
        if adapter is not UNSET:
            field_dict["adapter"] = adapter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        checksum = d.pop("checksum")

        checksum_type = d.pop("checksum_type")

        browsable = d.pop("browsable")

        streaming = d.pop("streaming")

        def _parse_adapter(data: object) -> BackupAdapter | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                adapter_type_1 = BackupAdapter(data)

                return adapter_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BackupAdapter | None | Unset, data)

        adapter = _parse_adapter(d.pop("adapter", UNSET))

        post_api_remote_servers_server_transfer_success_body_backup_migrations_additional_property = cls(
            checksum=checksum,
            checksum_type=checksum_type,
            browsable=browsable,
            streaming=streaming,
            adapter=adapter,
        )

        post_api_remote_servers_server_transfer_success_body_backup_migrations_additional_property.additional_properties = d
        return post_api_remote_servers_server_transfer_success_body_backup_migrations_additional_property

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
