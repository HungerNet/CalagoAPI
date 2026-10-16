from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Response200")


@_attrs_define
class Response200:
    """
    Attributes:
        content (str):
        eof (bool):
        start_line (int | None | Unset):
        end_line (int | None | Unset):
    """

    content: str
    eof: bool
    start_line: int | None | Unset = UNSET
    end_line: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        eof = self.eof

        start_line: int | None | Unset
        if isinstance(self.start_line, Unset):
            start_line = UNSET
        else:
            start_line = self.start_line

        end_line: int | None | Unset
        if isinstance(self.end_line, Unset):
            end_line = UNSET
        else:
            end_line = self.end_line

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "eof": eof,
            }
        )
        if start_line is not UNSET:
            field_dict["start_line"] = start_line
        if end_line is not UNSET:
            field_dict["end_line"] = end_line

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content")

        eof = d.pop("eof")

        def _parse_start_line(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        start_line = _parse_start_line(d.pop("start_line", UNSET))

        def _parse_end_line(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        end_line = _parse_end_line(d.pop("end_line", UNSET))

        response_200 = cls(
            content=content,
            eof=eof,
            start_line=start_line,
            end_line=end_line,
        )

        response_200.additional_properties = d
        return response_200

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
