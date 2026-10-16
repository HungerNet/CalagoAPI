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
    from ..models.patch_api_admin_announcements_announcement_body_content_translations_type_0 import (
        PatchApiAdminAnnouncementsAnnouncementBodyContentTranslationsType0,
    )
    from ..models.patch_api_admin_announcements_announcement_body_title_translations_type_0 import (
        PatchApiAdminAnnouncementsAnnouncementBodyTitleTranslationsType0,
    )


T = TypeVar("T", bound="PatchApiAdminAnnouncementsAnnouncementBody")


@_attrs_define
class PatchApiAdminAnnouncementsAnnouncementBody:
    """
    Attributes:
        type_ (AnnouncementType | None | Unset):
        enabled (bool | None | Unset):
        enabled_start (datetime.datetime | None | Unset):
        enabled_end (datetime.datetime | None | Unset):
        dismissible (bool | None | Unset):
        dismissible_end (datetime.datetime | None | Unset):
        title (None | str | Unset):
        title_translations (None | PatchApiAdminAnnouncementsAnnouncementBodyTitleTranslationsType0 | Unset):
        content (None | str | Unset):
        content_translations (None | PatchApiAdminAnnouncementsAnnouncementBodyContentTranslationsType0 | Unset):
        locations (list[UUID] | None | Unset):
        nodes (list[UUID] | None | Unset):
        backup_configurations (list[UUID] | None | Unset):
        eggs (list[UUID] | None | Unset):
    """

    type_: AnnouncementType | None | Unset = UNSET
    enabled: bool | None | Unset = UNSET
    enabled_start: datetime.datetime | None | Unset = UNSET
    enabled_end: datetime.datetime | None | Unset = UNSET
    dismissible: bool | None | Unset = UNSET
    dismissible_end: datetime.datetime | None | Unset = UNSET
    title: None | str | Unset = UNSET
    title_translations: None | PatchApiAdminAnnouncementsAnnouncementBodyTitleTranslationsType0 | Unset = UNSET
    content: None | str | Unset = UNSET
    content_translations: None | PatchApiAdminAnnouncementsAnnouncementBodyContentTranslationsType0 | Unset = UNSET
    locations: list[UUID] | None | Unset = UNSET
    nodes: list[UUID] | None | Unset = UNSET
    backup_configurations: list[UUID] | None | Unset = UNSET
    eggs: list[UUID] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.patch_api_admin_announcements_announcement_body_content_translations_type_0 import (
            PatchApiAdminAnnouncementsAnnouncementBodyContentTranslationsType0,  # noqa: PLC0415
        )
        from ..models.patch_api_admin_announcements_announcement_body_title_translations_type_0 import (
            PatchApiAdminAnnouncementsAnnouncementBodyTitleTranslationsType0,  # noqa: PLC0415
        )

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, AnnouncementType):
            type_ = self.type_.value
        else:
            type_ = self.type_

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

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

        dismissible: bool | None | Unset
        if isinstance(self.dismissible, Unset):
            dismissible = UNSET
        else:
            dismissible = self.dismissible

        dismissible_end: None | str | Unset
        if isinstance(self.dismissible_end, Unset):
            dismissible_end = UNSET
        elif isinstance(self.dismissible_end, datetime.datetime):
            dismissible_end = self.dismissible_end.isoformat()
        else:
            dismissible_end = self.dismissible_end

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        title_translations: dict[str, Any] | None | Unset
        if isinstance(self.title_translations, Unset):
            title_translations = UNSET
        elif isinstance(self.title_translations, PatchApiAdminAnnouncementsAnnouncementBodyTitleTranslationsType0):
            title_translations = self.title_translations.to_dict()
        else:
            title_translations = self.title_translations

        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        content_translations: dict[str, Any] | None | Unset
        if isinstance(self.content_translations, Unset):
            content_translations = UNSET
        elif isinstance(self.content_translations, PatchApiAdminAnnouncementsAnnouncementBodyContentTranslationsType0):
            content_translations = self.content_translations.to_dict()
        else:
            content_translations = self.content_translations

        locations: list[str] | None | Unset
        if isinstance(self.locations, Unset):
            locations = UNSET
        elif isinstance(self.locations, list):
            locations = []
            for locations_type_0_item_data in self.locations:
                locations_type_0_item = str(locations_type_0_item_data)
                locations.append(locations_type_0_item)

        else:
            locations = self.locations

        nodes: list[str] | None | Unset
        if isinstance(self.nodes, Unset):
            nodes = UNSET
        elif isinstance(self.nodes, list):
            nodes = []
            for nodes_type_0_item_data in self.nodes:
                nodes_type_0_item = str(nodes_type_0_item_data)
                nodes.append(nodes_type_0_item)

        else:
            nodes = self.nodes

        backup_configurations: list[str] | None | Unset
        if isinstance(self.backup_configurations, Unset):
            backup_configurations = UNSET
        elif isinstance(self.backup_configurations, list):
            backup_configurations = []
            for backup_configurations_type_0_item_data in self.backup_configurations:
                backup_configurations_type_0_item = str(backup_configurations_type_0_item_data)
                backup_configurations.append(backup_configurations_type_0_item)

        else:
            backup_configurations = self.backup_configurations

        eggs: list[str] | None | Unset
        if isinstance(self.eggs, Unset):
            eggs = UNSET
        elif isinstance(self.eggs, list):
            eggs = []
            for eggs_type_0_item_data in self.eggs:
                eggs_type_0_item = str(eggs_type_0_item_data)
                eggs.append(eggs_type_0_item)

        else:
            eggs = self.eggs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if enabled_start is not UNSET:
            field_dict["enabled_start"] = enabled_start
        if enabled_end is not UNSET:
            field_dict["enabled_end"] = enabled_end
        if dismissible is not UNSET:
            field_dict["dismissible"] = dismissible
        if dismissible_end is not UNSET:
            field_dict["dismissible_end"] = dismissible_end
        if title is not UNSET:
            field_dict["title"] = title
        if title_translations is not UNSET:
            field_dict["title_translations"] = title_translations
        if content is not UNSET:
            field_dict["content"] = content
        if content_translations is not UNSET:
            field_dict["content_translations"] = content_translations
        if locations is not UNSET:
            field_dict["locations"] = locations
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if backup_configurations is not UNSET:
            field_dict["backup_configurations"] = backup_configurations
        if eggs is not UNSET:
            field_dict["eggs"] = eggs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_api_admin_announcements_announcement_body_content_translations_type_0 import (
            PatchApiAdminAnnouncementsAnnouncementBodyContentTranslationsType0,  # noqa: PLC0415
        )
        from ..models.patch_api_admin_announcements_announcement_body_title_translations_type_0 import (
            PatchApiAdminAnnouncementsAnnouncementBodyTitleTranslationsType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_type_(data: object) -> AnnouncementType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_1 = AnnouncementType(data)

                return type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AnnouncementType | None | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

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

        def _parse_dismissible(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        dismissible = _parse_dismissible(d.pop("dismissible", UNSET))

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

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_title_translations(
            data: object,
        ) -> None | PatchApiAdminAnnouncementsAnnouncementBodyTitleTranslationsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                title_translations_type_0 = PatchApiAdminAnnouncementsAnnouncementBodyTitleTranslationsType0.from_dict(
                    data
                )

                return title_translations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PatchApiAdminAnnouncementsAnnouncementBodyTitleTranslationsType0 | Unset, data)

        title_translations = _parse_title_translations(d.pop("title_translations", UNSET))

        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))

        def _parse_content_translations(
            data: object,
        ) -> None | PatchApiAdminAnnouncementsAnnouncementBodyContentTranslationsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_translations_type_0 = (
                    PatchApiAdminAnnouncementsAnnouncementBodyContentTranslationsType0.from_dict(data)
                )

                return content_translations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PatchApiAdminAnnouncementsAnnouncementBodyContentTranslationsType0 | Unset, data)

        content_translations = _parse_content_translations(d.pop("content_translations", UNSET))

        def _parse_locations(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                locations_type_0 = []
                _locations_type_0 = data
                for locations_type_0_item_data in _locations_type_0:
                    locations_type_0_item = UUID(locations_type_0_item_data)

                    locations_type_0.append(locations_type_0_item)

                return locations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        locations = _parse_locations(d.pop("locations", UNSET))

        def _parse_nodes(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                nodes_type_0 = []
                _nodes_type_0 = data
                for nodes_type_0_item_data in _nodes_type_0:
                    nodes_type_0_item = UUID(nodes_type_0_item_data)

                    nodes_type_0.append(nodes_type_0_item)

                return nodes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        nodes = _parse_nodes(d.pop("nodes", UNSET))

        def _parse_backup_configurations(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                backup_configurations_type_0 = []
                _backup_configurations_type_0 = data
                for backup_configurations_type_0_item_data in _backup_configurations_type_0:
                    backup_configurations_type_0_item = UUID(backup_configurations_type_0_item_data)

                    backup_configurations_type_0.append(backup_configurations_type_0_item)

                return backup_configurations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        backup_configurations = _parse_backup_configurations(d.pop("backup_configurations", UNSET))

        def _parse_eggs(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                eggs_type_0 = []
                _eggs_type_0 = data
                for eggs_type_0_item_data in _eggs_type_0:
                    eggs_type_0_item = UUID(eggs_type_0_item_data)

                    eggs_type_0.append(eggs_type_0_item)

                return eggs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        eggs = _parse_eggs(d.pop("eggs", UNSET))

        patch_api_admin_announcements_announcement_body = cls(
            type_=type_,
            enabled=enabled,
            enabled_start=enabled_start,
            enabled_end=enabled_end,
            dismissible=dismissible,
            dismissible_end=dismissible_end,
            title=title,
            title_translations=title_translations,
            content=content,
            content_translations=content_translations,
            locations=locations,
            nodes=nodes,
            backup_configurations=backup_configurations,
            eggs=eggs,
        )

        patch_api_admin_announcements_announcement_body.additional_properties = d
        return patch_api_admin_announcements_announcement_body

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
