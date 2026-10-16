from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.server_backup_kind import ServerBackupKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetApiRemoteBackupsBackupPbsResponse200")


@_attrs_define
class GetApiRemoteBackupsBackupPbsResponse200:
    """
    Attributes:
        url (str):
        datastore (str):
        token_id (str):
        token_secret (str):
        kind (ServerBackupKind):
        backup_created (datetime.datetime):
        namespace (None | str | Unset):
        fingerprint (None | str | Unset):
        backup_id_prefix (None | str | Unset):
        server_uuid (None | Unset | UUID):
    """

    url: str
    datastore: str
    token_id: str
    token_secret: str
    kind: ServerBackupKind
    backup_created: datetime.datetime
    namespace: None | str | Unset = UNSET
    fingerprint: None | str | Unset = UNSET
    backup_id_prefix: None | str | Unset = UNSET
    server_uuid: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        datastore = self.datastore

        token_id = self.token_id

        token_secret = self.token_secret

        kind = self.kind.value

        backup_created = self.backup_created.isoformat()

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

        server_uuid: None | str | Unset
        if isinstance(self.server_uuid, Unset):
            server_uuid = UNSET
        elif isinstance(self.server_uuid, UUID):
            server_uuid = str(self.server_uuid)
        else:
            server_uuid = self.server_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "datastore": datastore,
                "token_id": token_id,
                "token_secret": token_secret,
                "kind": kind,
                "backup_created": backup_created,
            }
        )
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if fingerprint is not UNSET:
            field_dict["fingerprint"] = fingerprint
        if backup_id_prefix is not UNSET:
            field_dict["backup_id_prefix"] = backup_id_prefix
        if server_uuid is not UNSET:
            field_dict["server_uuid"] = server_uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        datastore = d.pop("datastore")

        token_id = d.pop("token_id")

        token_secret = d.pop("token_secret")

        kind = ServerBackupKind(d.pop("kind"))

        backup_created = datetime.datetime.fromisoformat(d.pop("backup_created"))

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

        def _parse_server_uuid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                server_uuid_type_0 = UUID(data)

                return server_uuid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        server_uuid = _parse_server_uuid(d.pop("server_uuid", UNSET))

        get_api_remote_backups_backup_pbs_response_200 = cls(
            url=url,
            datastore=datastore,
            token_id=token_id,
            token_secret=token_secret,
            kind=kind,
            backup_created=backup_created,
            namespace=namespace,
            fingerprint=fingerprint,
            backup_id_prefix=backup_id_prefix,
            server_uuid=server_uuid,
        )

        get_api_remote_backups_backup_pbs_response_200.additional_properties = d
        return get_api_remote_backups_backup_pbs_response_200

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
