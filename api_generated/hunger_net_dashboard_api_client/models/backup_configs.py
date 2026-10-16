from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_config_kopia import BackupConfigKopia
    from ..models.backup_configs_pbs import BackupConfigsPbs
    from ..models.backup_configs_restic import BackupConfigsRestic
    from ..models.backup_configs_s3 import BackupConfigsS3


T = TypeVar("T", bound="BackupConfigs")


@_attrs_define
class BackupConfigs:
    """
    Attributes:
        s3 (BackupConfigsS3 | None | Unset):
        restic (BackupConfigsRestic | None | Unset):
        pbs (BackupConfigsPbs | None | Unset):
        kopia (BackupConfigKopia | None | Unset):
    """

    s3: BackupConfigsS3 | None | Unset = UNSET
    restic: BackupConfigsRestic | None | Unset = UNSET
    pbs: BackupConfigsPbs | None | Unset = UNSET
    kopia: BackupConfigKopia | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.backup_config_kopia import BackupConfigKopia  # noqa: PLC0415
        from ..models.backup_configs_pbs import BackupConfigsPbs  # noqa: PLC0415
        from ..models.backup_configs_restic import BackupConfigsRestic  # noqa: PLC0415
        from ..models.backup_configs_s3 import BackupConfigsS3  # noqa: PLC0415

        s3: dict[str, Any] | None | Unset
        if isinstance(self.s3, Unset):
            s3 = UNSET
        elif isinstance(self.s3, BackupConfigsS3):
            s3 = self.s3.to_dict()
        else:
            s3 = self.s3

        restic: dict[str, Any] | None | Unset
        if isinstance(self.restic, Unset):
            restic = UNSET
        elif isinstance(self.restic, BackupConfigsRestic):
            restic = self.restic.to_dict()
        else:
            restic = self.restic

        pbs: dict[str, Any] | None | Unset
        if isinstance(self.pbs, Unset):
            pbs = UNSET
        elif isinstance(self.pbs, BackupConfigsPbs):
            pbs = self.pbs.to_dict()
        else:
            pbs = self.pbs

        kopia: dict[str, Any] | None | Unset
        if isinstance(self.kopia, Unset):
            kopia = UNSET
        elif isinstance(self.kopia, BackupConfigKopia):
            kopia = self.kopia.to_dict()
        else:
            kopia = self.kopia

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if s3 is not UNSET:
            field_dict["s3"] = s3
        if restic is not UNSET:
            field_dict["restic"] = restic
        if pbs is not UNSET:
            field_dict["pbs"] = pbs
        if kopia is not UNSET:
            field_dict["kopia"] = kopia

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_config_kopia import BackupConfigKopia  # noqa: PLC0415
        from ..models.backup_configs_pbs import BackupConfigsPbs  # noqa: PLC0415
        from ..models.backup_configs_restic import BackupConfigsRestic  # noqa: PLC0415
        from ..models.backup_configs_s3 import BackupConfigsS3  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_s3(data: object) -> BackupConfigsS3 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                s3_type_1 = BackupConfigsS3.from_dict(data)

                return s3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BackupConfigsS3 | None | Unset, data)

        s3 = _parse_s3(d.pop("s3", UNSET))

        def _parse_restic(data: object) -> BackupConfigsRestic | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                restic_type_1 = BackupConfigsRestic.from_dict(data)

                return restic_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BackupConfigsRestic | None | Unset, data)

        restic = _parse_restic(d.pop("restic", UNSET))

        def _parse_pbs(data: object) -> BackupConfigsPbs | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pbs_type_1 = BackupConfigsPbs.from_dict(data)

                return pbs_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BackupConfigsPbs | None | Unset, data)

        pbs = _parse_pbs(d.pop("pbs", UNSET))

        def _parse_kopia(data: object) -> BackupConfigKopia | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                kopia_type_1 = BackupConfigKopia.from_dict(data)

                return kopia_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BackupConfigKopia | None | Unset, data)

        kopia = _parse_kopia(d.pop("kopia", UNSET))

        backup_configs = cls(
            s3=s3,
            restic=restic,
            pbs=pbs,
            kopia=kopia,
        )

        backup_configs.additional_properties = d
        return backup_configs

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
