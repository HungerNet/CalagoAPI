from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.egg_config_allocations_deployment import EggConfigAllocationsDeployment


T = TypeVar("T", bound="PostApiAdminServersDeployBodyDeployment")


@_attrs_define
class PostApiAdminServersDeployBodyDeployment:
    """
    Attributes:
        location_uuids (list[UUID]):
        allow_overallocation (bool):
        suspension_penalty (float | Unset):  Default: 0.5.
        randomness (float | Unset):  Default: 0.5.
        allocations (EggConfigAllocationsDeployment | None | Unset):
    """

    location_uuids: list[UUID]
    allow_overallocation: bool
    suspension_penalty: float | Unset = 0.5
    randomness: float | Unset = 0.5
    allocations: EggConfigAllocationsDeployment | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.egg_config_allocations_deployment import EggConfigAllocationsDeployment  # noqa: PLC0415

        location_uuids = []
        for location_uuids_item_data in self.location_uuids:
            location_uuids_item = str(location_uuids_item_data)
            location_uuids.append(location_uuids_item)

        allow_overallocation = self.allow_overallocation

        suspension_penalty = self.suspension_penalty

        randomness = self.randomness

        allocations: dict[str, Any] | None | Unset
        if isinstance(self.allocations, Unset):
            allocations = UNSET
        elif isinstance(self.allocations, EggConfigAllocationsDeployment):
            allocations = self.allocations.to_dict()
        else:
            allocations = self.allocations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "location_uuids": location_uuids,
                "allow_overallocation": allow_overallocation,
            }
        )
        if suspension_penalty is not UNSET:
            field_dict["suspension_penalty"] = suspension_penalty
        if randomness is not UNSET:
            field_dict["randomness"] = randomness
        if allocations is not UNSET:
            field_dict["allocations"] = allocations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.egg_config_allocations_deployment import EggConfigAllocationsDeployment  # noqa: PLC0415

        d = dict(src_dict)
        location_uuids = []
        _location_uuids = d.pop("location_uuids")
        for location_uuids_item_data in _location_uuids:
            location_uuids_item = UUID(location_uuids_item_data)

            location_uuids.append(location_uuids_item)

        allow_overallocation = d.pop("allow_overallocation")

        suspension_penalty = d.pop("suspension_penalty", UNSET)

        randomness = d.pop("randomness", UNSET)

        def _parse_allocations(data: object) -> EggConfigAllocationsDeployment | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                allocations_type_1 = EggConfigAllocationsDeployment.from_dict(data)

                return allocations_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EggConfigAllocationsDeployment | None | Unset, data)

        allocations = _parse_allocations(d.pop("allocations", UNSET))

        post_api_admin_servers_deploy_body_deployment = cls(
            location_uuids=location_uuids,
            allow_overallocation=allow_overallocation,
            suspension_penalty=suspension_penalty,
            randomness=randomness,
            allocations=allocations,
        )

        post_api_admin_servers_deploy_body_deployment.additional_properties = d
        return post_api_admin_servers_deploy_body_deployment

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
