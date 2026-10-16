from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.response_version_history_extensions import ResponseVersionHistoryExtensions
    from ..models.version_history_entry import VersionHistoryEntry


T = TypeVar("T", bound="ResponseVersionHistory")


@_attrs_define
class ResponseVersionHistory:
    """
    Attributes:
        panel (list[VersionHistoryEntry]):
        extensions (ResponseVersionHistoryExtensions):
    """

    panel: list[VersionHistoryEntry]
    extensions: ResponseVersionHistoryExtensions
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        panel = []
        for panel_item_data in self.panel:
            panel_item = panel_item_data.to_dict()
            panel.append(panel_item)

        extensions = self.extensions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "panel": panel,
                "extensions": extensions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.response_version_history_extensions import ResponseVersionHistoryExtensions  # noqa: PLC0415
        from ..models.version_history_entry import VersionHistoryEntry  # noqa: PLC0415

        d = dict(src_dict)
        panel = []
        _panel = d.pop("panel")
        for panel_item_data in _panel:
            panel_item = VersionHistoryEntry.from_dict(panel_item_data)

            panel.append(panel_item)

        extensions = ResponseVersionHistoryExtensions.from_dict(d.pop("extensions"))

        response_version_history = cls(
            panel=panel,
            extensions=extensions,
        )

        response_version_history.additional_properties = d
        return response_version_history

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
