from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.instance_selector_type_0 import InstanceSelectorType0
    from ..models.instance_selector_type_1 import InstanceSelectorType1


T = TypeVar("T", bound="PostApiAdminDatabaseAgentTemplatesDatabaseAgentTemplateInstancesUpdateBody")


@_attrs_define
class PostApiAdminDatabaseAgentTemplatesDatabaseAgentTemplateInstancesUpdateBody:
    """
    Attributes:
        instances (InstanceSelectorType0 | InstanceSelectorType1):
    """

    instances: InstanceSelectorType0 | InstanceSelectorType1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.instance_selector_type_0 import InstanceSelectorType0  # noqa: PLC0415

        instances: dict[str, Any]
        if isinstance(self.instances, InstanceSelectorType0):
            instances = self.instances.to_dict()
        else:
            instances = self.instances.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instances": instances,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.instance_selector_type_0 import InstanceSelectorType0  # noqa: PLC0415
        from ..models.instance_selector_type_1 import InstanceSelectorType1  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_instances(data: object) -> InstanceSelectorType0 | InstanceSelectorType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_instance_selector_type_0 = InstanceSelectorType0.from_dict(data)

                return componentsschemas_instance_selector_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_instance_selector_type_1 = InstanceSelectorType1.from_dict(data)

            return componentsschemas_instance_selector_type_1

        instances = _parse_instances(d.pop("instances"))

        post_api_admin_database_agent_templates_database_agent_template_instances_update_body = cls(
            instances=instances,
        )

        post_api_admin_database_agent_templates_database_agent_template_instances_update_body.additional_properties = d
        return post_api_admin_database_agent_templates_database_agent_template_instances_update_body

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
