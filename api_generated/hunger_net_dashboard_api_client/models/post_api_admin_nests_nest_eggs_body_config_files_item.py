from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_admin_nests_nest_eggs_body_config_files_item_parser import (
    PostApiAdminNestsNestEggsBodyConfigFilesItemParser,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_admin_nests_nest_eggs_body_config_files_item_replace_item import (
        PostApiAdminNestsNestEggsBodyConfigFilesItemReplaceItem,
    )


T = TypeVar("T", bound="PostApiAdminNestsNestEggsBodyConfigFilesItem")


@_attrs_define
class PostApiAdminNestsNestEggsBodyConfigFilesItem:
    """
    Attributes:
        file (str):
        parser (PostApiAdminNestsNestEggsBodyConfigFilesItemParser):
        replace (list[PostApiAdminNestsNestEggsBodyConfigFilesItemReplaceItem]):
        create_new (bool | Unset):
    """

    file: str
    parser: PostApiAdminNestsNestEggsBodyConfigFilesItemParser
    replace: list[PostApiAdminNestsNestEggsBodyConfigFilesItemReplaceItem]
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
        from ..models.post_api_admin_nests_nest_eggs_body_config_files_item_replace_item import (
            PostApiAdminNestsNestEggsBodyConfigFilesItemReplaceItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        file = d.pop("file")

        parser = PostApiAdminNestsNestEggsBodyConfigFilesItemParser(d.pop("parser"))

        replace = []
        _replace = d.pop("replace")
        for replace_item_data in _replace:
            replace_item = PostApiAdminNestsNestEggsBodyConfigFilesItemReplaceItem.from_dict(replace_item_data)

            replace.append(replace_item)

        create_new = d.pop("create_new", UNSET)

        post_api_admin_nests_nest_eggs_body_config_files_item = cls(
            file=file,
            parser=parser,
            replace=replace,
            create_new=create_new,
        )

        post_api_admin_nests_nest_eggs_body_config_files_item.additional_properties = d
        return post_api_admin_nests_nest_eggs_body_config_files_item

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
