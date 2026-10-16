from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar(
    "T",
    bound="GetApiAdminExtensionsDev0X7D8Minecraftversionchanger2038Response200ExtensionChangelogsAdditionalProperty",
)


@_attrs_define
class GetApiAdminExtensionsDev0X7D8Minecraftversionchanger2038Response200ExtensionChangelogsAdditionalProperty:
    """
    Attributes:
        content (str):
        created (datetime.datetime):
    """

    content: str
    created: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        created = self.created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "created": created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_2038_response_200_extension_changelogs_additional_property = cls(
            content=content,
            created=created,
        )

        get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_2038_response_200_extension_changelogs_additional_property.additional_properties = d
        return get_api_admin_extensions_dev_0x7d8_minecraftversionchanger_2038_response_200_extension_changelogs_additional_property

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
