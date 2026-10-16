from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_config_kopia_tags import BackupConfigKopiaTags


T = TypeVar("T", bound="BackupConfigKopia")


@_attrs_define
class BackupConfigKopia:
    """
    Attributes:
        url (str):
        username (str):
        password (str):
        tags (BackupConfigKopiaTags):
        fingerprint (None | str | Unset):
    """

    url: str
    username: str
    password: str
    tags: BackupConfigKopiaTags
    fingerprint: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        username = self.username

        password = self.password

        tags = self.tags.to_dict()

        fingerprint: None | str | Unset
        if isinstance(self.fingerprint, Unset):
            fingerprint = UNSET
        else:
            fingerprint = self.fingerprint

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "username": username,
                "password": password,
                "tags": tags,
            }
        )
        if fingerprint is not UNSET:
            field_dict["fingerprint"] = fingerprint

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_config_kopia_tags import BackupConfigKopiaTags  # noqa: PLC0415

        d = dict(src_dict)
        url = d.pop("url")

        username = d.pop("username")

        password = d.pop("password")

        tags = BackupConfigKopiaTags.from_dict(d.pop("tags"))

        def _parse_fingerprint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fingerprint = _parse_fingerprint(d.pop("fingerprint", UNSET))

        backup_config_kopia = cls(
            url=url,
            username=username,
            password=password,
            tags=tags,
            fingerprint=fingerprint,
        )

        backup_config_kopia.additional_properties = d
        return backup_config_kopia

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
