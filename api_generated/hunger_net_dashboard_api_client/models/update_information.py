from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.update_information_extensions import UpdateInformationExtensions


T = TypeVar("T", bound="UpdateInformation")


@_attrs_define
class UpdateInformation:
    """
    Attributes:
        panel_version (str):
        latest_panel_version (str):
        latest_wings_version (str):
        latest_db_agent_version (str):
        extensions (UpdateInformationExtensions):
    """

    panel_version: str
    latest_panel_version: str
    latest_wings_version: str
    latest_db_agent_version: str
    extensions: UpdateInformationExtensions
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        panel_version = self.panel_version

        latest_panel_version = self.latest_panel_version

        latest_wings_version = self.latest_wings_version

        latest_db_agent_version = self.latest_db_agent_version

        extensions = self.extensions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "panel_version": panel_version,
                "latest_panel_version": latest_panel_version,
                "latest_wings_version": latest_wings_version,
                "latest_db_agent_version": latest_db_agent_version,
                "extensions": extensions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_information_extensions import UpdateInformationExtensions  # noqa: PLC0415

        d = dict(src_dict)
        panel_version = d.pop("panel_version")

        latest_panel_version = d.pop("latest_panel_version")

        latest_wings_version = d.pop("latest_wings_version")

        latest_db_agent_version = d.pop("latest_db_agent_version")

        extensions = UpdateInformationExtensions.from_dict(d.pop("extensions"))

        update_information = cls(
            panel_version=panel_version,
            latest_panel_version=latest_panel_version,
            latest_wings_version=latest_wings_version,
            latest_db_agent_version=latest_db_agent_version,
            extensions=extensions,
        )

        update_information.additional_properties = d
        return update_information

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
