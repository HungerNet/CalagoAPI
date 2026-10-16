from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mail_mode_type_3_type import MailModeType3Type
from ..types import UNSET, Unset

T = TypeVar("T", bound="MailModeType3")


@_attrs_define
class MailModeType3:
    """
    Attributes:
        path (str):
        from_address (str):
        type_ (MailModeType3Type):
        from_name (None | str | Unset):
    """

    path: str
    from_address: str
    type_: MailModeType3Type
    from_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        from_address = self.from_address

        type_ = self.type_.value

        from_name: None | str | Unset
        if isinstance(self.from_name, Unset):
            from_name = UNSET
        else:
            from_name = self.from_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "from_address": from_address,
                "type": type_,
            }
        )
        if from_name is not UNSET:
            field_dict["from_name"] = from_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path")

        from_address = d.pop("from_address")

        type_ = MailModeType3Type(d.pop("type"))

        def _parse_from_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_name = _parse_from_name(d.pop("from_name", UNSET))

        mail_mode_type_3 = cls(
            path=path,
            from_address=from_address,
            type_=type_,
            from_name=from_name,
        )

        mail_mode_type_3.additional_properties = d
        return mail_mode_type_3

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
