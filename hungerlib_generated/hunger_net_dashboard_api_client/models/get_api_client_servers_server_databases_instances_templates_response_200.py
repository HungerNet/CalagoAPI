from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.database_agent_template import DatabaseAgentTemplate


T = TypeVar("T", bound="GetApiClientServersServerDatabasesInstancesTemplatesResponse200")


@_attrs_define
class GetApiClientServersServerDatabasesInstancesTemplatesResponse200:
    """
    Attributes:
        templates (list[DatabaseAgentTemplate]):
    """

    templates: list[DatabaseAgentTemplate]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        templates = []
        for templates_item_data in self.templates:
            templates_item = templates_item_data.to_dict()
            templates.append(templates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "templates": templates,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_agent_template import DatabaseAgentTemplate  # noqa: PLC0415

        d = dict(src_dict)
        templates = []
        _templates = d.pop("templates")
        for templates_item_data in _templates:
            templates_item = DatabaseAgentTemplate.from_dict(templates_item_data)

            templates.append(templates_item)

        get_api_client_servers_server_databases_instances_templates_response_200 = cls(
            templates=templates,
        )

        get_api_client_servers_server_databases_instances_templates_response_200.additional_properties = d
        return get_api_client_servers_server_databases_instances_templates_response_200

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
