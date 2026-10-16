from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiRemoteServersServerBackupsRestoreDatabaseResponse200")


@_attrs_define
class PostApiRemoteServersServerBackupsRestoreDatabaseResponse200:
    """
    Attributes:
        uuid (UUID):
        database_instance_uuid (UUID):
        request_uuid (None | Unset | UUID):
    """

    uuid: UUID
    database_instance_uuid: UUID
    request_uuid: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        database_instance_uuid = str(self.database_instance_uuid)

        request_uuid: None | str | Unset
        if isinstance(self.request_uuid, Unset):
            request_uuid = UNSET
        elif isinstance(self.request_uuid, UUID):
            request_uuid = str(self.request_uuid)
        else:
            request_uuid = self.request_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "database_instance_uuid": database_instance_uuid,
            }
        )
        if request_uuid is not UNSET:
            field_dict["request_uuid"] = request_uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        database_instance_uuid = UUID(d.pop("database_instance_uuid"))

        def _parse_request_uuid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                request_uuid_type_0 = UUID(data)

                return request_uuid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        request_uuid = _parse_request_uuid(d.pop("request_uuid", UNSET))

        post_api_remote_servers_server_backups_restore_database_response_200 = cls(
            uuid=uuid,
            database_instance_uuid=database_instance_uuid,
            request_uuid=request_uuid,
        )

        post_api_remote_servers_server_backups_restore_database_response_200.additional_properties = d
        return post_api_remote_servers_server_backups_restore_database_response_200

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
