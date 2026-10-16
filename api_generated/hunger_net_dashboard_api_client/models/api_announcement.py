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
    from ..models.api_announcement_content_translations import ApiAnnouncementContentTranslations
    from ..models.api_announcement_title_translations import ApiAnnouncementTitleTranslations


T = TypeVar("T", bound="ApiAnnouncement")


@_attrs_define
class ApiAnnouncement:
    """
    Attributes:
        uuid (UUID):
        type_ (AnnouncementType):
        dismissible (bool):
        title (str):
        title_translations (ApiAnnouncementTitleTranslations):
        content (str):
        content_translations (ApiAnnouncementContentTranslations):
        dismissible_end (datetime.datetime | None | Unset):
    """

    uuid: UUID
    type_: AnnouncementType
    dismissible: bool
    title: str
    title_translations: ApiAnnouncementTitleTranslations
    content: str
    content_translations: ApiAnnouncementContentTranslations
    dismissible_end: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        type_ = self.type_.value

        dismissible = self.dismissible

        title = self.title

        title_translations = self.title_translations.to_dict()

        content = self.content

        content_translations = self.content_translations.to_dict()

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
                "uuid": uuid,
                "type": type_,
                "dismissible": dismissible,
                "title": title,
                "title_translations": title_translations,
                "content": content,
                "content_translations": content_translations,
            }
        )
        if dismissible_end is not UNSET:
            field_dict["dismissible_end"] = dismissible_end

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_announcement_content_translations import ApiAnnouncementContentTranslations  # noqa: PLC0415
        from ..models.api_announcement_title_translations import ApiAnnouncementTitleTranslations  # noqa: PLC0415

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        type_ = AnnouncementType(d.pop("type"))

        dismissible = d.pop("dismissible")

        title = d.pop("title")

        title_translations = ApiAnnouncementTitleTranslations.from_dict(d.pop("title_translations"))

        content = d.pop("content")

        content_translations = ApiAnnouncementContentTranslations.from_dict(d.pop("content_translations"))

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

        api_announcement = cls(
            uuid=uuid,
            type_=type_,
            dismissible=dismissible,
            title=title,
            title_translations=title_translations,
            content=content,
            content_translations=content_translations,
            dismissible_end=dismissible_end,
        )

        api_announcement.additional_properties = d
        return api_announcement

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
