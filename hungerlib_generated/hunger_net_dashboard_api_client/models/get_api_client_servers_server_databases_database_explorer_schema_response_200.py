from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.schema_table import SchemaTable


T = TypeVar("T", bound="GetApiClientServersServerDatabasesDatabaseExplorerSchemaResponse200")


@_attrs_define
class GetApiClientServersServerDatabasesDatabaseExplorerSchemaResponse200:
    """
    Attributes:
        tables (list[SchemaTable]):
        truncated (bool):
    """

    tables: list[SchemaTable]
    truncated: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tables = []
        for tables_item_data in self.tables:
            tables_item = tables_item_data.to_dict()
            tables.append(tables_item)

        truncated = self.truncated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tables": tables,
                "truncated": truncated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_table import SchemaTable  # noqa: PLC0415

        d = dict(src_dict)
        tables = []
        _tables = d.pop("tables")
        for tables_item_data in _tables:
            tables_item = SchemaTable.from_dict(tables_item_data)

            tables.append(tables_item)

        truncated = d.pop("truncated")

        get_api_client_servers_server_databases_database_explorer_schema_response_200 = cls(
            tables=tables,
            truncated=truncated,
        )

        get_api_client_servers_server_databases_database_explorer_schema_response_200.additional_properties = d
        return get_api_client_servers_server_databases_database_explorer_schema_response_200

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
