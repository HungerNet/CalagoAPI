from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApiClientAccountSshKeysResponse200SshKeysUserSshKey")


@_attrs_define
class GetApiClientAccountSshKeysResponse200SshKeysUserSshKey:
    """
    Attributes:
        uuid (UUID):
        name (str):
        fingerprint (str):
        created (datetime.datetime):
    """

    uuid: UUID
    name: str
    fingerprint: str
    created: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        fingerprint = self.fingerprint

        created = self.created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "fingerprint": fingerprint,
                "created": created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        fingerprint = d.pop("fingerprint")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        get_api_client_account_ssh_keys_response_200_ssh_keys_user_ssh_key = cls(
            uuid=uuid,
            name=name,
            fingerprint=fingerprint,
            created=created,
        )

        get_api_client_account_ssh_keys_response_200_ssh_keys_user_ssh_key.additional_properties = d
        return get_api_client_account_ssh_keys_response_200_ssh_keys_user_ssh_key

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
