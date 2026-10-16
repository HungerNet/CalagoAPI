from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="PostApiClientServersServerDatabasesInstancesDatabaseInstanceDatabasesDatabaseExplorerTablesColumnsDeleteBody",
)


@_attrs_define
class PostApiClientServersServerDatabasesInstancesDatabaseInstanceDatabasesDatabaseExplorerTablesColumnsDeleteBody:
    """
    Attributes:
        table (str):
        column (str):
        schema (None | str | Unset):
    """

    table: str
    column: str
    schema: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        table = self.table

        column = self.column

        schema: None | str | Unset
        if isinstance(self.schema, Unset):
            schema = UNSET
        else:
            schema = self.schema

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "table": table,
                "column": column,
            }
        )
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        table = d.pop("table")

        column = d.pop("column")

        def _parse_schema(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        schema = _parse_schema(d.pop("schema", UNSET))

        post_api_client_servers_server_databases_instances_database_instance_databases_database_explorer_tables_columns_delete_body = cls(
            table=table,
            column=column,
            schema=schema,
        )

        post_api_client_servers_server_databases_instances_database_instance_databases_database_explorer_tables_columns_delete_body.additional_properties = d
        return post_api_client_servers_server_databases_instances_database_instance_databases_database_explorer_tables_columns_delete_body

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
