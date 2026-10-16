from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.process_configuration_configs_item_parser import ProcessConfigurationConfigsItemParser
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.process_configuration_configs_item_replace_item import ProcessConfigurationConfigsItemReplaceItem


T = TypeVar("T", bound="ProcessConfigurationConfigsItem")


@_attrs_define
class ProcessConfigurationConfigsItem:
    """
    Attributes:
        file (str):
        parser (ProcessConfigurationConfigsItemParser):
        replace (list[ProcessConfigurationConfigsItemReplaceItem]):
        create_new (bool | Unset):
    """

    file: str
    parser: ProcessConfigurationConfigsItemParser
    replace: list[ProcessConfigurationConfigsItemReplaceItem]
    create_new: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file

        parser = self.parser.value

        replace = []
        for replace_item_data in self.replace:
            replace_item = replace_item_data.to_dict()
            replace.append(replace_item)

        create_new = self.create_new

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
                "parser": parser,
                "replace": replace,
            }
        )
        if create_new is not UNSET:
            field_dict["create_new"] = create_new

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.process_configuration_configs_item_replace_item import ProcessConfigurationConfigsItemReplaceItem  # noqa: PLC0415

        d = dict(src_dict)
        file = d.pop("file")

        parser = ProcessConfigurationConfigsItemParser(d.pop("parser"))

        replace = []
        _replace = d.pop("replace")
        for replace_item_data in _replace:
            replace_item = ProcessConfigurationConfigsItemReplaceItem.from_dict(replace_item_data)

            replace.append(replace_item)

        create_new = d.pop("create_new", UNSET)

        process_configuration_configs_item = cls(
            file=file,
            parser=parser,
            replace=replace,
            create_new=create_new,
        )

        process_configuration_configs_item.additional_properties = d
        return process_configuration_configs_item

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
