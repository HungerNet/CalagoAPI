from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.twitter_card import TwitterCard
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetApiAdminSettingsResponse200SettingsMetadata")


@_attrs_define
class GetApiAdminSettingsResponse200SettingsMetadata:
    """
    Attributes:
        theme_color (str):
        twitter_card (TwitterCard):
        indexable (bool):
        description (None | str | Unset):
        og_image (None | str | Unset):
    """

    theme_color: str
    twitter_card: TwitterCard
    indexable: bool
    description: None | str | Unset = UNSET
    og_image: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        theme_color = self.theme_color

        twitter_card = self.twitter_card.value

        indexable = self.indexable

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        og_image: None | str | Unset
        if isinstance(self.og_image, Unset):
            og_image = UNSET
        else:
            og_image = self.og_image

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "theme_color": theme_color,
                "twitter_card": twitter_card,
                "indexable": indexable,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if og_image is not UNSET:
            field_dict["og_image"] = og_image

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        theme_color = d.pop("theme_color")

        twitter_card = TwitterCard(d.pop("twitter_card"))

        indexable = d.pop("indexable")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_og_image(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        og_image = _parse_og_image(d.pop("og_image", UNSET))

        get_api_admin_settings_response_200_settings_metadata = cls(
            theme_color=theme_color,
            twitter_card=twitter_card,
            indexable=indexable,
            description=description,
            og_image=og_image,
        )

        get_api_admin_settings_response_200_settings_metadata.additional_properties = d
        return get_api_admin_settings_response_200_settings_metadata

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
