from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.system_backup_policy import SystemBackupPolicy


T = TypeVar("T", bound="PostApiAdminSystemBackupPoliciesResponse200")


@_attrs_define
class PostApiAdminSystemBackupPoliciesResponse200:
    """
    Attributes:
        system_backup_policy (SystemBackupPolicy):
    """

    system_backup_policy: SystemBackupPolicy
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        system_backup_policy = self.system_backup_policy.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "system_backup_policy": system_backup_policy,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.system_backup_policy import SystemBackupPolicy  # noqa: PLC0415

        d = dict(src_dict)
        system_backup_policy = SystemBackupPolicy.from_dict(d.pop("system_backup_policy"))

        post_api_admin_system_backup_policies_response_200 = cls(
            system_backup_policy=system_backup_policy,
        )

        post_api_admin_system_backup_policies_response_200.additional_properties = d
        return post_api_admin_system_backup_policies_response_200

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
