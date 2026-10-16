from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupConfigsPbs")


@_attrs_define
class BackupConfigsPbs:
    """
    Attributes:
        url (str):
        datastore (str):
        token_id (str):
        token_secret (str):
        namespace (None | str | Unset):
        fingerprint (None | str | Unset):
        backup_id_prefix (None | str | Unset):
    """

    url: str
    datastore: str
    token_id: str
    token_secret: str
    namespace: None | str | Unset = UNSET
    fingerprint: None | str | Unset = UNSET
    backup_id_prefix: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        datastore = self.datastore

        token_id = self.token_id

        token_secret = self.token_secret

        namespace: None | str | Unset
        if isinstance(self.namespace, Unset):
            namespace = UNSET
        else:
            namespace = self.namespace

        fingerprint: None | str | Unset
        if isinstance(self.fingerprint, Unset):
            fingerprint = UNSET
        else:
            fingerprint = self.fingerprint

        backup_id_prefix: None | str | Unset
        if isinstance(self.backup_id_prefix, Unset):
            backup_id_prefix = UNSET
        else:
            backup_id_prefix = self.backup_id_prefix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "datastore": datastore,
                "token_id": token_id,
                "token_secret": token_secret,
            }
        )
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if fingerprint is not UNSET:
            field_dict["fingerprint"] = fingerprint
        if backup_id_prefix is not UNSET:
            field_dict["backup_id_prefix"] = backup_id_prefix

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        datastore = d.pop("datastore")

        token_id = d.pop("token_id")

        token_secret = d.pop("token_secret")

        def _parse_namespace(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        namespace = _parse_namespace(d.pop("namespace", UNSET))

        def _parse_fingerprint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fingerprint = _parse_fingerprint(d.pop("fingerprint", UNSET))

        def _parse_backup_id_prefix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        backup_id_prefix = _parse_backup_id_prefix(d.pop("backup_id_prefix", UNSET))

        backup_configs_pbs = cls(
            url=url,
            datastore=datastore,
            token_id=token_id,
            token_secret=token_secret,
            namespace=namespace,
            fingerprint=fingerprint,
            backup_id_prefix=backup_id_prefix,
        )

        backup_configs_pbs.additional_properties = d
        return backup_configs_pbs

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
