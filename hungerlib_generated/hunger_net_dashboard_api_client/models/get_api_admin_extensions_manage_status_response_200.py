from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pending_extension import PendingExtension
    from ..models.status import Status


T = TypeVar("T", bound="GetApiAdminExtensionsManageStatusResponse200")


@_attrs_define
class GetApiAdminExtensionsManageStatusResponse200:
    """
    Attributes:
        is_building (bool):
        running_panel_version (str):
        pending_extensions (list[PendingExtension]):
        removed_extensions (list[PendingExtension]):
        supervisor (None | Status | Unset):
    """

    is_building: bool
    running_panel_version: str
    pending_extensions: list[PendingExtension]
    removed_extensions: list[PendingExtension]
    supervisor: None | Status | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.status import Status  # noqa: PLC0415

        is_building = self.is_building

        running_panel_version = self.running_panel_version

        pending_extensions = []
        for pending_extensions_item_data in self.pending_extensions:
            pending_extensions_item = pending_extensions_item_data.to_dict()
            pending_extensions.append(pending_extensions_item)

        removed_extensions = []
        for removed_extensions_item_data in self.removed_extensions:
            removed_extensions_item = removed_extensions_item_data.to_dict()
            removed_extensions.append(removed_extensions_item)

        supervisor: dict[str, Any] | None | Unset
        if isinstance(self.supervisor, Unset):
            supervisor = UNSET
        elif isinstance(self.supervisor, Status):
            supervisor = self.supervisor.to_dict()
        else:
            supervisor = self.supervisor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "is_building": is_building,
                "running_panel_version": running_panel_version,
                "pending_extensions": pending_extensions,
                "removed_extensions": removed_extensions,
            }
        )
        if supervisor is not UNSET:
            field_dict["supervisor"] = supervisor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pending_extension import PendingExtension  # noqa: PLC0415
        from ..models.status import Status  # noqa: PLC0415

        d = dict(src_dict)
        is_building = d.pop("is_building")

        running_panel_version = d.pop("running_panel_version")

        pending_extensions = []
        _pending_extensions = d.pop("pending_extensions")
        for pending_extensions_item_data in _pending_extensions:
            pending_extensions_item = PendingExtension.from_dict(pending_extensions_item_data)

            pending_extensions.append(pending_extensions_item)

        removed_extensions = []
        _removed_extensions = d.pop("removed_extensions")
        for removed_extensions_item_data in _removed_extensions:
            removed_extensions_item = PendingExtension.from_dict(removed_extensions_item_data)

            removed_extensions.append(removed_extensions_item)

        def _parse_supervisor(data: object) -> None | Status | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                supervisor_type_1 = Status.from_dict(data)

                return supervisor_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Status | Unset, data)

        supervisor = _parse_supervisor(d.pop("supervisor", UNSET))

        get_api_admin_extensions_manage_status_response_200 = cls(
            is_building=is_building,
            running_panel_version=running_panel_version,
            pending_extensions=pending_extensions,
            removed_extensions=removed_extensions,
            supervisor=supervisor,
        )

        get_api_admin_extensions_manage_status_response_200.additional_properties = d
        return get_api_admin_extensions_manage_status_response_200

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
