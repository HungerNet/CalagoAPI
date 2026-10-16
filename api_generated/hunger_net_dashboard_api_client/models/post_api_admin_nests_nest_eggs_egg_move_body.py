from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApiAdminNestsNestEggsEggMoveBody")


@_attrs_define
class PostApiAdminNestsNestEggsEggMoveBody:
    """
    Attributes:
        destination_nest_uuid (UUID):
    """

    destination_nest_uuid: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination_nest_uuid = str(self.destination_nest_uuid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "destination_nest_uuid": destination_nest_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        destination_nest_uuid = UUID(d.pop("destination_nest_uuid"))

        post_api_admin_nests_nest_eggs_egg_move_body = cls(
            destination_nest_uuid=destination_nest_uuid,
        )

        post_api_admin_nests_nest_eggs_egg_move_body.additional_properties = d
        return post_api_admin_nests_nest_eggs_egg_move_body

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
