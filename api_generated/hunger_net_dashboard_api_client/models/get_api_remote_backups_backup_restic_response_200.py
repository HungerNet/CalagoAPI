from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_remote_backups_backup_restic_response_200_environment import (
        GetApiRemoteBackupsBackupResticResponse200Environment,
    )


T = TypeVar("T", bound="GetApiRemoteBackupsBackupResticResponse200")


@_attrs_define
class GetApiRemoteBackupsBackupResticResponse200:
    """
    Attributes:
        repository (str):
        retry_lock_seconds (int):
        environment (GetApiRemoteBackupsBackupResticResponse200Environment):
    """

    repository: str
    retry_lock_seconds: int
    environment: GetApiRemoteBackupsBackupResticResponse200Environment
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repository = self.repository

        retry_lock_seconds = self.retry_lock_seconds

        environment = self.environment.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repository": repository,
                "retry_lock_seconds": retry_lock_seconds,
                "environment": environment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_remote_backups_backup_restic_response_200_environment import (
            GetApiRemoteBackupsBackupResticResponse200Environment,  # noqa: PLC0415
        )

        d = dict(src_dict)
        repository = d.pop("repository")

        retry_lock_seconds = d.pop("retry_lock_seconds")

        environment = GetApiRemoteBackupsBackupResticResponse200Environment.from_dict(d.pop("environment"))

        get_api_remote_backups_backup_restic_response_200 = cls(
            repository=repository,
            retry_lock_seconds=retry_lock_seconds,
            environment=environment,
        )

        get_api_remote_backups_backup_restic_response_200.additional_properties = d
        return get_api_remote_backups_backup_restic_response_200

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
