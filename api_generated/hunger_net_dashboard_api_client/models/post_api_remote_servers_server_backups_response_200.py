from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_adapter import BackupAdapter
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiRemoteServersServerBackupsResponse200")


@_attrs_define
class PostApiRemoteServersServerBackupsResponse200:
    """
    Attributes:
        adapter (BackupAdapter):
        uuid (UUID):
        extension (None | str | Unset):
    """

    adapter: BackupAdapter
    uuid: UUID
    extension: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        adapter = self.adapter.value

        uuid = str(self.uuid)

        extension: None | str | Unset
        if isinstance(self.extension, Unset):
            extension = UNSET
        else:
            extension = self.extension

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "adapter": adapter,
                "uuid": uuid,
            }
        )
        if extension is not UNSET:
            field_dict["extension"] = extension

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        adapter = BackupAdapter(d.pop("adapter"))

        uuid = UUID(d.pop("uuid"))

        def _parse_extension(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        extension = _parse_extension(d.pop("extension", UNSET))

        post_api_remote_servers_server_backups_response_200 = cls(
            adapter=adapter,
            uuid=uuid,
            extension=extension,
        )

        post_api_remote_servers_server_backups_response_200.additional_properties = d
        return post_api_remote_servers_server_backups_response_200

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
