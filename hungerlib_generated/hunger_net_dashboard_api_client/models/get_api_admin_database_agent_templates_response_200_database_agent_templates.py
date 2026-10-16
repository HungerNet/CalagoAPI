from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_admin_database_agent_templates_response_200_database_agent_templates_admin_database_agent_template import (
        GetApiAdminDatabaseAgentTemplatesResponse200DatabaseAgentTemplatesAdminDatabaseAgentTemplate,
    )


T = TypeVar("T", bound="GetApiAdminDatabaseAgentTemplatesResponse200DatabaseAgentTemplates")


@_attrs_define
class GetApiAdminDatabaseAgentTemplatesResponse200DatabaseAgentTemplates:
    """
    Attributes:
        total (int):
        per_page (int):
        page (int):
        data (list[GetApiAdminDatabaseAgentTemplatesResponse200DatabaseAgentTemplatesAdminDatabaseAgentTemplate]):
    """

    total: int
    per_page: int
    page: int
    data: list[GetApiAdminDatabaseAgentTemplatesResponse200DatabaseAgentTemplatesAdminDatabaseAgentTemplate]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        per_page = self.per_page

        page = self.page

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "per_page": per_page,
                "page": page,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_admin_database_agent_templates_response_200_database_agent_templates_admin_database_agent_template import (
            GetApiAdminDatabaseAgentTemplatesResponse200DatabaseAgentTemplatesAdminDatabaseAgentTemplate,  # noqa: PLC0415
        )

        d = dict(src_dict)
        total = d.pop("total")

        per_page = d.pop("per_page")

        page = d.pop("page")

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = (
                GetApiAdminDatabaseAgentTemplatesResponse200DatabaseAgentTemplatesAdminDatabaseAgentTemplate.from_dict(
                    data_item_data
                )
            )

            data.append(data_item)

        get_api_admin_database_agent_templates_response_200_database_agent_templates = cls(
            total=total,
            per_page=per_page,
            page=page,
            data=data,
        )

        get_api_admin_database_agent_templates_response_200_database_agent_templates.additional_properties = d
        return get_api_admin_database_agent_templates_response_200_database_agent_templates

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
