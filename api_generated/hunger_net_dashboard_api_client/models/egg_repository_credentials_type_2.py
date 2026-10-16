from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.egg_repository_credentials_type_2_type import EggRepositoryCredentialsType2Type
from ..types import UNSET, Unset

T = TypeVar("T", bound="EggRepositoryCredentialsType2")


@_attrs_define
class EggRepositoryCredentialsType2:
    """
    Attributes:
        username (str):
        private_key (str):
        type_ (EggRepositoryCredentialsType2Type):
        passphrase (None | str | Unset):
    """

    username: str
    private_key: str
    type_: EggRepositoryCredentialsType2Type
    passphrase: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        private_key = self.private_key

        type_ = self.type_.value

        passphrase: None | str | Unset
        if isinstance(self.passphrase, Unset):
            passphrase = UNSET
        else:
            passphrase = self.passphrase

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "private_key": private_key,
                "type": type_,
            }
        )
        if passphrase is not UNSET:
            field_dict["passphrase"] = passphrase

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username")

        private_key = d.pop("private_key")

        type_ = EggRepositoryCredentialsType2Type(d.pop("type"))

        def _parse_passphrase(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        passphrase = _parse_passphrase(d.pop("passphrase", UNSET))

        egg_repository_credentials_type_2 = cls(
            username=username,
            private_key=private_key,
            type_=type_,
            passphrase=passphrase,
        )

        egg_repository_credentials_type_2.additional_properties = d
        return egg_repository_credentials_type_2

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
