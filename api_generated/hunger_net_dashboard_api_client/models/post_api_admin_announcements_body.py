from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.announcement_type import AnnouncementType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_admin_announcements_body_content_translations import (
        PostApiAdminAnnouncementsBodyContentTranslations,
    )
    from ..models.post_api_admin_announcements_body_title_translations import (
        PostApiAdminAnnouncementsBodyTitleTranslations,
    )


T = TypeVar("T", bound="PostApiAdminAnnouncementsBody")


@_attrs_define
class PostApiAdminAnnouncementsBody:
    """
    Attributes:
        type_ (AnnouncementType):
        enabled (bool):
        dismissible (bool):
        title (str):
        title_translations (PostApiAdminAnnouncementsBodyTitleTranslations):
        content (str):
        content_translations (PostApiAdminAnnouncementsBodyContentTranslations):
        locations (list[UUID]):
        nodes (list[UUID]):
        backup_configurations (list[UUID]):
        eggs (list[UUID]):
        enabled_start (datetime.datetime | None | Unset):
        enabled_end (datetime.datetime | None | Unset):
        dismissible_end (datetime.datetime | None | Unset):
    """

    type_: AnnouncementType
    enabled: bool
    dismissible: bool
    title: str
    title_translations: PostApiAdminAnnouncementsBodyTitleTranslations
    content: str
    content_translations: PostApiAdminAnnouncementsBodyContentTranslations
    locations: list[UUID]
    nodes: list[UUID]
    backup_configurations: list[UUID]
    eggs: list[UUID]
    enabled_start: datetime.datetime | None | Unset = UNSET
    enabled_end: datetime.datetime | None | Unset = UNSET
    dismissible_end: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        enabled = self.enabled

        dismissible = self.dismissible

        title = self.title

        title_translations = self.title_translations.to_dict()

        content = self.content

        content_translations = self.content_translations.to_dict()

        locations = []
        for locations_item_data in self.locations:
            locations_item = str(locations_item_data)
            locations.append(locations_item)

        nodes = []
        for nodes_item_data in self.nodes:
            nodes_item = str(nodes_item_data)
            nodes.append(nodes_item)

        backup_configurations = []
        for backup_configurations_item_data in self.backup_configurations:
            backup_configurations_item = str(backup_configurations_item_data)
            backup_configurations.append(backup_configurations_item)

        eggs = []
        for eggs_item_data in self.eggs:
            eggs_item = str(eggs_item_data)
            eggs.append(eggs_item)

        enabled_start: None | str | Unset
        if isinstance(self.enabled_start, Unset):
            enabled_start = UNSET
        elif isinstance(self.enabled_start, datetime.datetime):
            enabled_start = self.enabled_start.isoformat()
        else:
            enabled_start = self.enabled_start

        enabled_end: None | str | Unset
        if isinstance(self.enabled_end, Unset):
            enabled_end = UNSET
        elif isinstance(self.enabled_end, datetime.datetime):
            enabled_end = self.enabled_end.isoformat()
        else:
            enabled_end = self.enabled_end

        dismissible_end: None | str | Unset
        if isinstance(self.dismissible_end, Unset):
            dismissible_end = UNSET
        elif isinstance(self.dismissible_end, datetime.datetime):
            dismissible_end = self.dismissible_end.isoformat()
        else:
            dismissible_end = self.dismissible_end

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "enabled": enabled,
                "dismissible": dismissible,
                "title": title,
                "title_translations": title_translations,
                "content": content,
                "content_translations": content_translations,
                "locations": locations,
                "nodes": nodes,
                "backup_configurations": backup_configurations,
                "eggs": eggs,
            }
        )
        if enabled_start is not UNSET:
            field_dict["enabled_start"] = enabled_start
        if enabled_end is not UNSET:
            field_dict["enabled_end"] = enabled_end
        if dismissible_end is not UNSET:
            field_dict["dismissible_end"] = dismissible_end

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_admin_announcements_body_content_translations import (
            PostApiAdminAnnouncementsBodyContentTranslations,  # noqa: PLC0415
        )
        from ..models.post_api_admin_announcements_body_title_translations import (
            PostApiAdminAnnouncementsBodyTitleTranslations,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = AnnouncementType(d.pop("type"))

        enabled = d.pop("enabled")

        dismissible = d.pop("dismissible")

        title = d.pop("title")

        title_translations = PostApiAdminAnnouncementsBodyTitleTranslations.from_dict(d.pop("title_translations"))

        content = d.pop("content")

        content_translations = PostApiAdminAnnouncementsBodyContentTranslations.from_dict(d.pop("content_translations"))

        locations = []
        _locations = d.pop("locations")
        for locations_item_data in _locations:
            locations_item = UUID(locations_item_data)

            locations.append(locations_item)

        nodes = []
        _nodes = d.pop("nodes")
        for nodes_item_data in _nodes:
            nodes_item = UUID(nodes_item_data)

            nodes.append(nodes_item)

        backup_configurations = []
        _backup_configurations = d.pop("backup_configurations")
        for backup_configurations_item_data in _backup_configurations:
            backup_configurations_item = UUID(backup_configurations_item_data)

            backup_configurations.append(backup_configurations_item)

        eggs = []
        _eggs = d.pop("eggs")
        for eggs_item_data in _eggs:
            eggs_item = UUID(eggs_item_data)

            eggs.append(eggs_item)

        def _parse_enabled_start(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                enabled_start_type_0 = datetime.datetime.fromisoformat(data)

                return enabled_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        enabled_start = _parse_enabled_start(d.pop("enabled_start", UNSET))

        def _parse_enabled_end(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                enabled_end_type_0 = datetime.datetime.fromisoformat(data)

                return enabled_end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        enabled_end = _parse_enabled_end(d.pop("enabled_end", UNSET))

        def _parse_dismissible_end(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dismissible_end_type_0 = datetime.datetime.fromisoformat(data)

                return dismissible_end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        dismissible_end = _parse_dismissible_end(d.pop("dismissible_end", UNSET))

        post_api_admin_announcements_body = cls(
            type_=type_,
            enabled=enabled,
            dismissible=dismissible,
            title=title,
            title_translations=title_translations,
            content=content,
            content_translations=content_translations,
            locations=locations,
            nodes=nodes,
            backup_configurations=backup_configurations,
            eggs=eggs,
            enabled_start=enabled_start,
            enabled_end=enabled_end,
            dismissible_end=dismissible_end,
        )

        post_api_admin_announcements_body.additional_properties = d
        return post_api_admin_announcements_body

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
