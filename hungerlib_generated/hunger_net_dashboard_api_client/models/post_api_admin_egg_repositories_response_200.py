from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.egg_repository import EggRepository


T = TypeVar("T", bound="PostApiAdminEggRepositoriesResponse200")


@_attrs_define
class PostApiAdminEggRepositoriesResponse200:
    """
    Attributes:
        egg_repository (EggRepository):
    """

    egg_repository: EggRepository
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        egg_repository = self.egg_repository.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "egg_repository": egg_repository,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.egg_repository import EggRepository  # noqa: PLC0415

        d = dict(src_dict)
        egg_repository = EggRepository.from_dict(d.pop("egg_repository"))

        post_api_admin_egg_repositories_response_200 = cls(
            egg_repository=egg_repository,
        )

        post_api_admin_egg_repositories_response_200.additional_properties = d
        return post_api_admin_egg_repositories_response_200

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
