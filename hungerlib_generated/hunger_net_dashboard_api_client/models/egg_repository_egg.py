from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.exported_nest_egg import ExportedNestEgg


T = TypeVar("T", bound="EggRepositoryEgg")


@_attrs_define
class EggRepositoryEgg:
    """
    Attributes:
        uuid (UUID):
        path (str):
        exported_egg (ExportedNestEgg):
        updated (datetime.datetime):
        readme (None | str | Unset):
    """

    uuid: UUID
    path: str
    exported_egg: ExportedNestEgg
    updated: datetime.datetime
    readme: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        path = self.path

        exported_egg = self.exported_egg.to_dict()

        updated = self.updated.isoformat()

        readme: None | str | Unset
        if isinstance(self.readme, Unset):
            readme = UNSET
        else:
            readme = self.readme

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "path": path,
                "exported_egg": exported_egg,
                "updated": updated,
            }
        )
        if readme is not UNSET:
            field_dict["readme"] = readme

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exported_nest_egg import ExportedNestEgg  # noqa: PLC0415

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        path = d.pop("path")

        exported_egg = ExportedNestEgg.from_dict(d.pop("exported_egg"))

        updated = datetime.datetime.fromisoformat(d.pop("updated"))

        def _parse_readme(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        readme = _parse_readme(d.pop("readme", UNSET))

        egg_repository_egg = cls(
            uuid=uuid,
            path=path,
            exported_egg=exported_egg,
            updated=updated,
            readme=readme,
        )

        egg_repository_egg.additional_properties = d
        return egg_repository_egg

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
