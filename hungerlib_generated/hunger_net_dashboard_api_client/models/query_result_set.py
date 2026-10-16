from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.query_column import QueryColumn
    from ..models.query_value_type_0 import QueryValueType0
    from ..models.query_value_type_1 import QueryValueType1
    from ..models.query_value_type_2 import QueryValueType2


T = TypeVar("T", bound="QueryResultSet")


@_attrs_define
class QueryResultSet:
    """
    Attributes:
        columns (list[QueryColumn]):
        rows (list[list[QueryValueType0 | QueryValueType1 | QueryValueType2]]):
        rows_affected (int):
        truncated (bool):
    """

    columns: list[QueryColumn]
    rows: list[list[QueryValueType0 | QueryValueType1 | QueryValueType2]]
    rows_affected: int
    truncated: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.query_value_type_0 import QueryValueType0  # noqa: PLC0415
        from ..models.query_value_type_1 import QueryValueType1  # noqa: PLC0415

        columns = []
        for columns_item_data in self.columns:
            columns_item = columns_item_data.to_dict()
            columns.append(columns_item)

        rows = []
        for rows_item_data in self.rows:
            rows_item = []
            for rows_item_item_data in rows_item_data:
                rows_item_item: dict[str, Any]
                if isinstance(rows_item_item_data, QueryValueType0):
                    rows_item_item = rows_item_item_data.to_dict()
                elif isinstance(rows_item_item_data, QueryValueType1):
                    rows_item_item = rows_item_item_data.to_dict()
                else:
                    rows_item_item = rows_item_item_data.to_dict()

                rows_item.append(rows_item_item)

            rows.append(rows_item)

        rows_affected = self.rows_affected

        truncated = self.truncated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "columns": columns,
                "rows": rows,
                "rows_affected": rows_affected,
                "truncated": truncated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_column import QueryColumn  # noqa: PLC0415
        from ..models.query_value_type_0 import QueryValueType0  # noqa: PLC0415
        from ..models.query_value_type_1 import QueryValueType1  # noqa: PLC0415
        from ..models.query_value_type_2 import QueryValueType2  # noqa: PLC0415

        d = dict(src_dict)
        columns = []
        _columns = d.pop("columns")
        for columns_item_data in _columns:
            columns_item = QueryColumn.from_dict(columns_item_data)

            columns.append(columns_item)

        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = []
            _rows_item = rows_item_data
            for rows_item_item_data in _rows_item:

                def _parse_rows_item_item(data: object) -> QueryValueType0 | QueryValueType1 | QueryValueType2:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_query_value_type_0 = QueryValueType0.from_dict(data)

                        return componentsschemas_query_value_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_query_value_type_1 = QueryValueType1.from_dict(data)

                        return componentsschemas_query_value_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_query_value_type_2 = QueryValueType2.from_dict(data)

                    return componentsschemas_query_value_type_2

                rows_item_item = _parse_rows_item_item(rows_item_item_data)

                rows_item.append(rows_item_item)

            rows.append(rows_item)

        rows_affected = d.pop("rows_affected")

        truncated = d.pop("truncated")

        query_result_set = cls(
            columns=columns,
            rows=rows,
            rows_affected=rows_affected,
            truncated=truncated,
        )

        query_result_set.additional_properties = d
        return query_result_set

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
