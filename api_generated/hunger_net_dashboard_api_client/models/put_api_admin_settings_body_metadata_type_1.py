from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.twitter_card import TwitterCard
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutApiAdminSettingsBodyMetadataType1")


@_attrs_define
class PutApiAdminSettingsBodyMetadataType1:
    """
    Attributes:
        description (None | str | Unset):
        theme_color (None | str | Unset):
        og_image (None | str | Unset):
        twitter_card (None | TwitterCard | Unset):
        indexable (bool | None | Unset):
    """

    description: None | str | Unset = UNSET
    theme_color: None | str | Unset = UNSET
    og_image: None | str | Unset = UNSET
    twitter_card: None | TwitterCard | Unset = UNSET
    indexable: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        theme_color: None | str | Unset
        if isinstance(self.theme_color, Unset):
            theme_color = UNSET
        else:
            theme_color = self.theme_color

        og_image: None | str | Unset
        if isinstance(self.og_image, Unset):
            og_image = UNSET
        else:
            og_image = self.og_image

        twitter_card: None | str | Unset
        if isinstance(self.twitter_card, Unset):
            twitter_card = UNSET
        elif isinstance(self.twitter_card, TwitterCard):
            twitter_card = self.twitter_card.value
        else:
            twitter_card = self.twitter_card

        indexable: bool | None | Unset
        if isinstance(self.indexable, Unset):
            indexable = UNSET
        else:
            indexable = self.indexable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if theme_color is not UNSET:
            field_dict["theme_color"] = theme_color
        if og_image is not UNSET:
            field_dict["og_image"] = og_image
        if twitter_card is not UNSET:
            field_dict["twitter_card"] = twitter_card
        if indexable is not UNSET:
            field_dict["indexable"] = indexable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_theme_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        theme_color = _parse_theme_color(d.pop("theme_color", UNSET))

        def _parse_og_image(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        og_image = _parse_og_image(d.pop("og_image", UNSET))

        def _parse_twitter_card(data: object) -> None | TwitterCard | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                twitter_card_type_1 = TwitterCard(data)

                return twitter_card_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TwitterCard | Unset, data)

        twitter_card = _parse_twitter_card(d.pop("twitter_card", UNSET))

        def _parse_indexable(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        indexable = _parse_indexable(d.pop("indexable", UNSET))

        put_api_admin_settings_body_metadata_type_1 = cls(
            description=description,
            theme_color=theme_color,
            og_image=og_image,
            twitter_card=twitter_card,
            indexable=indexable,
        )

        put_api_admin_settings_body_metadata_type_1.additional_properties = d
        return put_api_admin_settings_body_metadata_type_1

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
