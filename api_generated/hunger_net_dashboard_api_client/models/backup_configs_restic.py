from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_configs_restic_environment import BackupConfigsResticEnvironment
    from ..models.backup_configs_restic_prune_jobs_item import BackupConfigsResticPruneJobsItem


T = TypeVar("T", bound="BackupConfigsRestic")


@_attrs_define
class BackupConfigsRestic:
    """
    Attributes:
        repository (str):
        retry_lock_seconds (int):
        environment (BackupConfigsResticEnvironment):
        prune_jobs (list[BackupConfigsResticPruneJobsItem] | Unset):
    """

    repository: str
    retry_lock_seconds: int
    environment: BackupConfigsResticEnvironment
    prune_jobs: list[BackupConfigsResticPruneJobsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repository = self.repository

        retry_lock_seconds = self.retry_lock_seconds

        environment = self.environment.to_dict()

        prune_jobs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.prune_jobs, Unset):
            prune_jobs = []
            for prune_jobs_item_data in self.prune_jobs:
                prune_jobs_item = prune_jobs_item_data.to_dict()
                prune_jobs.append(prune_jobs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repository": repository,
                "retry_lock_seconds": retry_lock_seconds,
                "environment": environment,
            }
        )
        if prune_jobs is not UNSET:
            field_dict["prune_jobs"] = prune_jobs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_configs_restic_environment import BackupConfigsResticEnvironment  # noqa: PLC0415
        from ..models.backup_configs_restic_prune_jobs_item import BackupConfigsResticPruneJobsItem  # noqa: PLC0415

        d = dict(src_dict)
        repository = d.pop("repository")

        retry_lock_seconds = d.pop("retry_lock_seconds")

        environment = BackupConfigsResticEnvironment.from_dict(d.pop("environment"))

        _prune_jobs = d.pop("prune_jobs", UNSET)
        prune_jobs: list[BackupConfigsResticPruneJobsItem] | Unset = UNSET
        if _prune_jobs is not UNSET:
            prune_jobs = []
            for prune_jobs_item_data in _prune_jobs:
                prune_jobs_item = BackupConfigsResticPruneJobsItem.from_dict(prune_jobs_item_data)

                prune_jobs.append(prune_jobs_item)

        backup_configs_restic = cls(
            repository=repository,
            retry_lock_seconds=retry_lock_seconds,
            environment=environment,
            prune_jobs=prune_jobs,
        )

        backup_configs_restic.additional_properties = d
        return backup_configs_restic

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
