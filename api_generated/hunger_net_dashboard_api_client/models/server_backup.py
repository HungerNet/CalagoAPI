from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.database_agent_type import DatabaseAgentType
from ..models.server_backup_deletion_status import ServerBackupDeletionStatus
from ..models.server_backup_kind import ServerBackupKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_backup_retention_status import ServerBackupRetentionStatus


T = TypeVar("T", bound="ServerBackup")


@_attrs_define
class ServerBackup:
    """
    Attributes:
        uuid (UUID):
        kind (ServerBackupKind):
        name (str):
        ignored_files (list[str]):
        is_successful (bool):
        is_locked (bool):
        is_browsable (bool):
        is_streaming (bool):
        bytes_ (int):
        files (int):
        metadata (Any):
        created (datetime.datetime):
        backup_group_uuid (None | Unset | UUID):
        database_instance_uuid (None | Unset | UUID):
        database_type (DatabaseAgentType | None | Unset):
        checksum (None | str | Unset):
        deletion_status (None | ServerBackupDeletionStatus | Unset):
        retention_status (None | ServerBackupRetentionStatus | Unset):
        completed (datetime.datetime | None | Unset):
    """

    uuid: UUID
    kind: ServerBackupKind
    name: str
    ignored_files: list[str]
    is_successful: bool
    is_locked: bool
    is_browsable: bool
    is_streaming: bool
    bytes_: int
    files: int
    metadata: Any
    created: datetime.datetime
    backup_group_uuid: None | Unset | UUID = UNSET
    database_instance_uuid: None | Unset | UUID = UNSET
    database_type: DatabaseAgentType | None | Unset = UNSET
    checksum: None | str | Unset = UNSET
    deletion_status: None | ServerBackupDeletionStatus | Unset = UNSET
    retention_status: None | ServerBackupRetentionStatus | Unset = UNSET
    completed: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.server_backup_retention_status import ServerBackupRetentionStatus  # noqa: PLC0415

        uuid = str(self.uuid)

        kind = self.kind.value

        name = self.name

        ignored_files = self.ignored_files

        is_successful = self.is_successful

        is_locked = self.is_locked

        is_browsable = self.is_browsable

        is_streaming = self.is_streaming

        bytes_ = self.bytes_

        files = self.files

        metadata = self.metadata

        created = self.created.isoformat()

        backup_group_uuid: None | str | Unset
        if isinstance(self.backup_group_uuid, Unset):
            backup_group_uuid = UNSET
        elif isinstance(self.backup_group_uuid, UUID):
            backup_group_uuid = str(self.backup_group_uuid)
        else:
            backup_group_uuid = self.backup_group_uuid

        database_instance_uuid: None | str | Unset
        if isinstance(self.database_instance_uuid, Unset):
            database_instance_uuid = UNSET
        elif isinstance(self.database_instance_uuid, UUID):
            database_instance_uuid = str(self.database_instance_uuid)
        else:
            database_instance_uuid = self.database_instance_uuid

        database_type: None | str | Unset
        if isinstance(self.database_type, Unset):
            database_type = UNSET
        elif isinstance(self.database_type, DatabaseAgentType):
            database_type = self.database_type.value
        else:
            database_type = self.database_type

        checksum: None | str | Unset
        if isinstance(self.checksum, Unset):
            checksum = UNSET
        else:
            checksum = self.checksum

        deletion_status: None | str | Unset
        if isinstance(self.deletion_status, Unset):
            deletion_status = UNSET
        elif isinstance(self.deletion_status, ServerBackupDeletionStatus):
            deletion_status = self.deletion_status.value
        else:
            deletion_status = self.deletion_status

        retention_status: dict[str, Any] | None | Unset
        if isinstance(self.retention_status, Unset):
            retention_status = UNSET
        elif isinstance(self.retention_status, ServerBackupRetentionStatus):
            retention_status = self.retention_status.to_dict()
        else:
            retention_status = self.retention_status

        completed: None | str | Unset
        if isinstance(self.completed, Unset):
            completed = UNSET
        elif isinstance(self.completed, datetime.datetime):
            completed = self.completed.isoformat()
        else:
            completed = self.completed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "kind": kind,
                "name": name,
                "ignored_files": ignored_files,
                "is_successful": is_successful,
                "is_locked": is_locked,
                "is_browsable": is_browsable,
                "is_streaming": is_streaming,
                "bytes": bytes_,
                "files": files,
                "metadata": metadata,
                "created": created,
            }
        )
        if backup_group_uuid is not UNSET:
            field_dict["backup_group_uuid"] = backup_group_uuid
        if database_instance_uuid is not UNSET:
            field_dict["database_instance_uuid"] = database_instance_uuid
        if database_type is not UNSET:
            field_dict["database_type"] = database_type
        if checksum is not UNSET:
            field_dict["checksum"] = checksum
        if deletion_status is not UNSET:
            field_dict["deletion_status"] = deletion_status
        if retention_status is not UNSET:
            field_dict["retention_status"] = retention_status
        if completed is not UNSET:
            field_dict["completed"] = completed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_backup_retention_status import ServerBackupRetentionStatus  # noqa: PLC0415

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        kind = ServerBackupKind(d.pop("kind"))

        name = d.pop("name")

        ignored_files = cast(list[str], d.pop("ignored_files"))

        is_successful = d.pop("is_successful")

        is_locked = d.pop("is_locked")

        is_browsable = d.pop("is_browsable")

        is_streaming = d.pop("is_streaming")

        bytes_ = d.pop("bytes")

        files = d.pop("files")

        metadata = d.pop("metadata")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        def _parse_backup_group_uuid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                backup_group_uuid_type_0 = UUID(data)

                return backup_group_uuid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        backup_group_uuid = _parse_backup_group_uuid(d.pop("backup_group_uuid", UNSET))

        def _parse_database_instance_uuid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                database_instance_uuid_type_0 = UUID(data)

                return database_instance_uuid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        database_instance_uuid = _parse_database_instance_uuid(d.pop("database_instance_uuid", UNSET))

        def _parse_database_type(data: object) -> DatabaseAgentType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                database_type_type_1 = DatabaseAgentType(data)

                return database_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatabaseAgentType | None | Unset, data)

        database_type = _parse_database_type(d.pop("database_type", UNSET))

        def _parse_checksum(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        checksum = _parse_checksum(d.pop("checksum", UNSET))

        def _parse_deletion_status(data: object) -> None | ServerBackupDeletionStatus | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deletion_status_type_1 = ServerBackupDeletionStatus(data)

                return deletion_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ServerBackupDeletionStatus | Unset, data)

        deletion_status = _parse_deletion_status(d.pop("deletion_status", UNSET))

        def _parse_retention_status(data: object) -> None | ServerBackupRetentionStatus | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                retention_status_type_1 = ServerBackupRetentionStatus.from_dict(data)

                return retention_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ServerBackupRetentionStatus | Unset, data)

        retention_status = _parse_retention_status(d.pop("retention_status", UNSET))

        def _parse_completed(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_type_0 = datetime.datetime.fromisoformat(data)

                return completed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        completed = _parse_completed(d.pop("completed", UNSET))

        server_backup = cls(
            uuid=uuid,
            kind=kind,
            name=name,
            ignored_files=ignored_files,
            is_successful=is_successful,
            is_locked=is_locked,
            is_browsable=is_browsable,
            is_streaming=is_streaming,
            bytes_=bytes_,
            files=files,
            metadata=metadata,
            created=created,
            backup_group_uuid=backup_group_uuid,
            database_instance_uuid=database_instance_uuid,
            database_type=database_type,
            checksum=checksum,
            deletion_status=deletion_status,
            retention_status=retention_status,
            completed=completed,
        )

        server_backup.additional_properties = d
        return server_backup

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
