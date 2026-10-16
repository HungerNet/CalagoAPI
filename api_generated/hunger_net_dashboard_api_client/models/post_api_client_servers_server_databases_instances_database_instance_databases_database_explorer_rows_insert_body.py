from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.row_insert import RowInsert


T = TypeVar(
    "T", bound="PostApiClientServersServerDatabasesInstancesDatabaseInstanceDatabasesDatabaseExplorerRowsInsertBody"
)


@_attrs_define
class PostApiClientServersServerDatabasesInstancesDatabaseInstanceDatabasesDatabaseExplorerRowsInsertBody:
    """
    Attributes:
        table (str):
        rows (list[RowInsert]):
        schema (None | str | Unset):
    """

    table: str
    rows: list[RowInsert]
    schema: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        table = self.table

        rows = []
        for rows_item_data in self.rows:
            rows_item = rows_item_data.to_dict()
            rows.append(rows_item)

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
                "rows": rows,
            }
        )
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.row_insert import RowInsert  # noqa: PLC0415

        d = dict(src_dict)
        table = d.pop("table")

        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = RowInsert.from_dict(rows_item_data)

            rows.append(rows_item)

        def _parse_schema(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        schema = _parse_schema(d.pop("schema", UNSET))

        post_api_client_servers_server_databases_instances_database_instance_databases_database_explorer_rows_insert_body = cls(
            table=table,
            rows=rows,
            schema=schema,
        )

        post_api_client_servers_server_databases_instances_database_instance_databases_database_explorer_rows_insert_body.additional_properties = d
        return post_api_client_servers_server_databases_instances_database_instance_databases_database_explorer_rows_insert_body

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
