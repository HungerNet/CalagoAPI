from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.column_definition import ColumnDefinition


T = TypeVar(
    "T", bound="PostApiClientServersServerDatabasesInstancesDatabaseInstanceDatabasesDatabaseExplorerTablesColumnsBody"
)


@_attrs_define
class PostApiClientServersServerDatabasesInstancesDatabaseInstanceDatabasesDatabaseExplorerTablesColumnsBody:
    """
    Attributes:
        table (str):
        column (ColumnDefinition):
        schema (None | str | Unset):
    """

    table: str
    column: ColumnDefinition
    schema: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        table = self.table

        column = self.column.to_dict()

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
        from ..models.column_definition import ColumnDefinition  # noqa: PLC0415

        d = dict(src_dict)
        table = d.pop("table")

        column = ColumnDefinition.from_dict(d.pop("column"))

        def _parse_schema(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        schema = _parse_schema(d.pop("schema", UNSET))

        post_api_client_servers_server_databases_instances_database_instance_databases_database_explorer_tables_columns_body = cls(
            table=table,
            column=column,
            schema=schema,
        )

        post_api_client_servers_server_databases_instances_database_instance_databases_database_explorer_tables_columns_body.additional_properties = d
        return post_api_client_servers_server_databases_instances_database_instance_databases_database_explorer_tables_columns_body

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
