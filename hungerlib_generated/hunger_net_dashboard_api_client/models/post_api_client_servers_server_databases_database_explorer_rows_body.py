from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.browse_filter import BrowseFilter


T = TypeVar("T", bound="PostApiClientServersServerDatabasesDatabaseExplorerRowsBody")


@_attrs_define
class PostApiClientServersServerDatabasesDatabaseExplorerRowsBody:
    """
    Attributes:
        table (str):
        schema (None | str | Unset):
        order_by (None | str | Unset):
        descending (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):
        filters (list[BrowseFilter] | Unset):
    """

    table: str
    schema: None | str | Unset = UNSET
    order_by: None | str | Unset = UNSET
    descending: bool | Unset = UNSET
    limit: int | Unset = UNSET
    offset: int | Unset = UNSET
    filters: list[BrowseFilter] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        table = self.table

        schema: None | str | Unset
        if isinstance(self.schema, Unset):
            schema = UNSET
        else:
            schema = self.schema

        order_by: None | str | Unset
        if isinstance(self.order_by, Unset):
            order_by = UNSET
        else:
            order_by = self.order_by

        descending = self.descending

        limit = self.limit

        offset = self.offset

        filters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = []
            for filters_item_data in self.filters:
                filters_item = filters_item_data.to_dict()
                filters.append(filters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "table": table,
            }
        )
        if schema is not UNSET:
            field_dict["schema"] = schema
        if order_by is not UNSET:
            field_dict["order_by"] = order_by
        if descending is not UNSET:
            field_dict["descending"] = descending
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset
        if filters is not UNSET:
            field_dict["filters"] = filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.browse_filter import BrowseFilter  # noqa: PLC0415

        d = dict(src_dict)
        table = d.pop("table")

        def _parse_schema(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        schema = _parse_schema(d.pop("schema", UNSET))

        def _parse_order_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        order_by = _parse_order_by(d.pop("order_by", UNSET))

        descending = d.pop("descending", UNSET)

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        _filters = d.pop("filters", UNSET)
        filters: list[BrowseFilter] | Unset = UNSET
        if _filters is not UNSET:
            filters = []
            for filters_item_data in _filters:
                filters_item = BrowseFilter.from_dict(filters_item_data)

                filters.append(filters_item)

        post_api_client_servers_server_databases_database_explorer_rows_body = cls(
            table=table,
            schema=schema,
            order_by=order_by,
            descending=descending,
            limit=limit,
            offset=offset,
            filters=filters,
        )

        post_api_client_servers_server_databases_database_explorer_rows_body.additional_properties = d
        return post_api_client_servers_server_databases_database_explorer_rows_body

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
