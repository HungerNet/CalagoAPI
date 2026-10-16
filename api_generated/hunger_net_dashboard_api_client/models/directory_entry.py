from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DirectoryEntry")


@_attrs_define
class DirectoryEntry:
    """
    Attributes:
        name (str):
        mode (str):
        mode_bits (str):
        size (int):
        size_physical (int):
        editable (bool):
        inner_editable (bool):
        directory (bool):
        file (bool):
        symlink (bool):
        virtual (bool):
        mime (str):
        created (datetime.datetime):
        modified (datetime.datetime):
    """

    name: str
    mode: str
    mode_bits: str
    size: int
    size_physical: int
    editable: bool
    inner_editable: bool
    directory: bool
    file: bool
    symlink: bool
    virtual: bool
    mime: str
    created: datetime.datetime
    modified: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mode = self.mode

        mode_bits = self.mode_bits

        size = self.size

        size_physical = self.size_physical

        editable = self.editable

        inner_editable = self.inner_editable

        directory = self.directory

        file = self.file

        symlink = self.symlink

        virtual = self.virtual

        mime = self.mime

        created = self.created.isoformat()

        modified = self.modified.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "mode": mode,
                "mode_bits": mode_bits,
                "size": size,
                "size_physical": size_physical,
                "editable": editable,
                "inner_editable": inner_editable,
                "directory": directory,
                "file": file,
                "symlink": symlink,
                "virtual": virtual,
                "mime": mime,
                "created": created,
                "modified": modified,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        mode = d.pop("mode")

        mode_bits = d.pop("mode_bits")

        size = d.pop("size")

        size_physical = d.pop("size_physical")

        editable = d.pop("editable")

        inner_editable = d.pop("inner_editable")

        directory = d.pop("directory")

        file = d.pop("file")

        symlink = d.pop("symlink")

        virtual = d.pop("virtual")

        mime = d.pop("mime")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        modified = datetime.datetime.fromisoformat(d.pop("modified"))

        directory_entry = cls(
            name=name,
            mode=mode,
            mode_bits=mode_bits,
            size=size,
            size_physical=size_physical,
            editable=editable,
            inner_editable=inner_editable,
            directory=directory,
            file=file,
            symlink=symlink,
            virtual=virtual,
            mime=mime,
            created=created,
            modified=modified,
        )

        directory_entry.additional_properties = d
        return directory_entry

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
