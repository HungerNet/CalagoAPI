from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_admin_system_backup_policies_system_backup_policy_locations_response_200_locations import (
        GetApiAdminSystemBackupPoliciesSystemBackupPolicyLocationsResponse200Locations,
    )


T = TypeVar("T", bound="GetApiAdminSystemBackupPoliciesSystemBackupPolicyLocationsResponse200")


@_attrs_define
class GetApiAdminSystemBackupPoliciesSystemBackupPolicyLocationsResponse200:
    """
    Attributes:
        locations (GetApiAdminSystemBackupPoliciesSystemBackupPolicyLocationsResponse200Locations):
    """

    locations: GetApiAdminSystemBackupPoliciesSystemBackupPolicyLocationsResponse200Locations
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        locations = self.locations.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "locations": locations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_admin_system_backup_policies_system_backup_policy_locations_response_200_locations import (
            GetApiAdminSystemBackupPoliciesSystemBackupPolicyLocationsResponse200Locations,  # noqa: PLC0415
        )

        d = dict(src_dict)
        locations = GetApiAdminSystemBackupPoliciesSystemBackupPolicyLocationsResponse200Locations.from_dict(
            d.pop("locations")
        )

        get_api_admin_system_backup_policies_system_backup_policy_locations_response_200 = cls(
            locations=locations,
        )

        get_api_admin_system_backup_policies_system_backup_policy_locations_response_200.additional_properties = d
        return get_api_admin_system_backup_policies_system_backup_policy_locations_response_200

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
