from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApiAdminEggRepositoriesEggRepositoryEggsInstallBody")


@_attrs_define
class PostApiAdminEggRepositoriesEggRepositoryEggsInstallBody:
    """
    Attributes:
        egg_uuids (list[UUID]):
        nest_uuid (UUID):
    """

    egg_uuids: list[UUID]
    nest_uuid: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        egg_uuids = []
        for egg_uuids_item_data in self.egg_uuids:
            egg_uuids_item = str(egg_uuids_item_data)
            egg_uuids.append(egg_uuids_item)

        nest_uuid = str(self.nest_uuid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "egg_uuids": egg_uuids,
                "nest_uuid": nest_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        egg_uuids = []
        _egg_uuids = d.pop("egg_uuids")
        for egg_uuids_item_data in _egg_uuids:
            egg_uuids_item = UUID(egg_uuids_item_data)

            egg_uuids.append(egg_uuids_item)

        nest_uuid = UUID(d.pop("nest_uuid"))

        post_api_admin_egg_repositories_egg_repository_eggs_install_body = cls(
            egg_uuids=egg_uuids,
            nest_uuid=nest_uuid,
        )

        post_api_admin_egg_repositories_egg_repository_eggs_install_body.additional_properties = d
        return post_api_admin_egg_repositories_egg_repository_eggs_install_body

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
