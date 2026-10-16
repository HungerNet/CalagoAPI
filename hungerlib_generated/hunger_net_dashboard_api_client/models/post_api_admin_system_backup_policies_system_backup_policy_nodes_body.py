from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApiAdminSystemBackupPoliciesSystemBackupPolicyNodesBody")


@_attrs_define
class PostApiAdminSystemBackupPoliciesSystemBackupPolicyNodesBody:
    """
    Attributes:
        node_uuid (UUID):
    """

    node_uuid: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_uuid = str(self.node_uuid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node_uuid": node_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        node_uuid = UUID(d.pop("node_uuid"))

        post_api_admin_system_backup_policies_system_backup_policy_nodes_body = cls(
            node_uuid=node_uuid,
        )

        post_api_admin_system_backup_policies_system_backup_policy_nodes_body.additional_properties = d
        return post_api_admin_system_backup_policies_system_backup_policy_nodes_body

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
