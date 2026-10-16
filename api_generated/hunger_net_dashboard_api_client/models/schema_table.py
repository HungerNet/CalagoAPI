from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema_column import SchemaColumn


T = TypeVar("T", bound="SchemaTable")


@_attrs_define
class SchemaTable:
    """
    Attributes:
        name (str):
        view (bool):
        columns (list[SchemaColumn]):
        schema (None | str | Unset):
        row_estimate (int | None | Unset):
    """

    name: str
    view: bool
    columns: list[SchemaColumn]
    schema: None | str | Unset = UNSET
    row_estimate: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        view = self.view

        columns = []
        for columns_item_data in self.columns:
            columns_item = columns_item_data.to_dict()
            columns.append(columns_item)

        schema: None | str | Unset
        if isinstance(self.schema, Unset):
            schema = UNSET
        else:
            schema = self.schema

        row_estimate: int | None | Unset
        if isinstance(self.row_estimate, Unset):
            row_estimate = UNSET
        else:
            row_estimate = self.row_estimate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "view": view,
                "columns": columns,
            }
        )
        if schema is not UNSET:
            field_dict["schema"] = schema
        if row_estimate is not UNSET:
            field_dict["row_estimate"] = row_estimate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_column import SchemaColumn  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        view = d.pop("view")

        columns = []
        _columns = d.pop("columns")
        for columns_item_data in _columns:
            columns_item = SchemaColumn.from_dict(columns_item_data)

            columns.append(columns_item)

        def _parse_schema(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        schema = _parse_schema(d.pop("schema", UNSET))

        def _parse_row_estimate(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        row_estimate = _parse_row_estimate(d.pop("row_estimate", UNSET))

        schema_table = cls(
            name=name,
            view=view,
            columns=columns,
            schema=schema,
            row_estimate=row_estimate,
        )

        schema_table.additional_properties = d
        return schema_table

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
