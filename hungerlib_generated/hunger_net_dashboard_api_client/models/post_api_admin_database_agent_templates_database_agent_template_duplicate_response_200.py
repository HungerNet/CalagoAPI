from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.admin_database_agent_template import AdminDatabaseAgentTemplate


T = TypeVar("T", bound="PostApiAdminDatabaseAgentTemplatesDatabaseAgentTemplateDuplicateResponse200")


@_attrs_define
class PostApiAdminDatabaseAgentTemplatesDatabaseAgentTemplateDuplicateResponse200:
    """
    Attributes:
        database_agent_template (AdminDatabaseAgentTemplate):
    """

    database_agent_template: AdminDatabaseAgentTemplate
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        database_agent_template = self.database_agent_template.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "database_agent_template": database_agent_template,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.admin_database_agent_template import AdminDatabaseAgentTemplate  # noqa: PLC0415

        d = dict(src_dict)
        database_agent_template = AdminDatabaseAgentTemplate.from_dict(d.pop("database_agent_template"))

        post_api_admin_database_agent_templates_database_agent_template_duplicate_response_200 = cls(
            database_agent_template=database_agent_template,
        )

        post_api_admin_database_agent_templates_database_agent_template_duplicate_response_200.additional_properties = d
        return post_api_admin_database_agent_templates_database_agent_template_duplicate_response_200

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
