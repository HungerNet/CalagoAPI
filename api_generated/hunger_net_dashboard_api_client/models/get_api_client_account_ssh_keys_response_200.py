from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_client_account_ssh_keys_response_200_ssh_keys import (
        GetApiClientAccountSshKeysResponse200SshKeys,
    )


T = TypeVar("T", bound="GetApiClientAccountSshKeysResponse200")


@_attrs_define
class GetApiClientAccountSshKeysResponse200:
    """
    Attributes:
        ssh_keys (GetApiClientAccountSshKeysResponse200SshKeys):
    """

    ssh_keys: GetApiClientAccountSshKeysResponse200SshKeys
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ssh_keys = self.ssh_keys.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ssh_keys": ssh_keys,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_client_account_ssh_keys_response_200_ssh_keys import (
            GetApiClientAccountSshKeysResponse200SshKeys,  # noqa: PLC0415
        )

        d = dict(src_dict)
        ssh_keys = GetApiClientAccountSshKeysResponse200SshKeys.from_dict(d.pop("ssh_keys"))

        get_api_client_account_ssh_keys_response_200 = cls(
            ssh_keys=ssh_keys,
        )

        get_api_client_account_ssh_keys_response_200.additional_properties = d
        return get_api_client_account_ssh_keys_response_200

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
