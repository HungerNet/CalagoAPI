from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiClientServersServerDatabasesInstancesDatabaseInstanceDatabasesDatabaseImportRemoteBody")


@_attrs_define
class PostApiClientServersServerDatabasesInstancesDatabaseInstanceDatabasesDatabaseImportRemoteBody:
    """
    Attributes:
        url (str):
        source_db (None | str | Unset):
        wipe (bool | Unset):
    """

    url: str
    source_db: None | str | Unset = UNSET
    wipe: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        source_db: None | str | Unset
        if isinstance(self.source_db, Unset):
            source_db = UNSET
        else:
            source_db = self.source_db

        wipe = self.wipe

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if source_db is not UNSET:
            field_dict["source_db"] = source_db
        if wipe is not UNSET:
            field_dict["wipe"] = wipe

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        def _parse_source_db(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_db = _parse_source_db(d.pop("source_db", UNSET))

        wipe = d.pop("wipe", UNSET)

        post_api_client_servers_server_databases_instances_database_instance_databases_database_import_remote_body = (
            cls(
                url=url,
                source_db=source_db,
                wipe=wipe,
            )
        )

        post_api_client_servers_server_databases_instances_database_instance_databases_database_import_remote_body.additional_properties = d
        return (
            post_api_client_servers_server_databases_instances_database_instance_databases_database_import_remote_body
        )

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
