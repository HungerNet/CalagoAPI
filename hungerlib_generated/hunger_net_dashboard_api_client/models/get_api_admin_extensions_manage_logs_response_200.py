from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApiAdminExtensionsManageLogsResponse200")


@_attrs_define
class GetApiAdminExtensionsManageLogsResponse200:
    """
    Attributes:
        offset (int):
        data (str):
        eof (bool):
    """

    offset: int
    data: str
    eof: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offset = self.offset

        data = self.data

        eof = self.eof

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "offset": offset,
                "data": data,
                "eof": eof,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        offset = d.pop("offset")

        data = d.pop("data")

        eof = d.pop("eof")

        get_api_admin_extensions_manage_logs_response_200 = cls(
            offset=offset,
            data=data,
            eof=eof,
        )

        get_api_admin_extensions_manage_logs_response_200.additional_properties = d
        return get_api_admin_extensions_manage_logs_response_200

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
