from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_configuration import BackupConfiguration


T = TypeVar("T", bound="GetApiAdminBackupConfigurationsBackupConfigurationLocationsResponse200LocationsLocation")


@_attrs_define
class GetApiAdminBackupConfigurationsBackupConfigurationLocationsResponse200LocationsLocation:
    """
    Attributes:
        uuid (UUID):
        name (str):
        created (datetime.datetime):
        backup_configuration (BackupConfiguration | None | Unset):
        description (None | str | Unset):
        flag (None | str | Unset):
    """

    uuid: UUID
    name: str
    created: datetime.datetime
    backup_configuration: BackupConfiguration | None | Unset = UNSET
    description: None | str | Unset = UNSET
    flag: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.backup_configuration import BackupConfiguration  # noqa: PLC0415

        uuid = str(self.uuid)

        name = self.name

        created = self.created.isoformat()

        backup_configuration: dict[str, Any] | None | Unset
        if isinstance(self.backup_configuration, Unset):
            backup_configuration = UNSET
        elif isinstance(self.backup_configuration, BackupConfiguration):
            backup_configuration = self.backup_configuration.to_dict()
        else:
            backup_configuration = self.backup_configuration

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        flag: None | str | Unset
        if isinstance(self.flag, Unset):
            flag = UNSET
        else:
            flag = self.flag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "created": created,
            }
        )
        if backup_configuration is not UNSET:
            field_dict["backup_configuration"] = backup_configuration
        if description is not UNSET:
            field_dict["description"] = description
        if flag is not UNSET:
            field_dict["flag"] = flag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_configuration import BackupConfiguration  # noqa: PLC0415

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        def _parse_backup_configuration(data: object) -> BackupConfiguration | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                backup_configuration_type_1 = BackupConfiguration.from_dict(data)

                return backup_configuration_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BackupConfiguration | None | Unset, data)

        backup_configuration = _parse_backup_configuration(d.pop("backup_configuration", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_flag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        flag = _parse_flag(d.pop("flag", UNSET))

        get_api_admin_backup_configurations_backup_configuration_locations_response_200_locations_location = cls(
            uuid=uuid,
            name=name,
            created=created,
            backup_configuration=backup_configuration,
            description=description,
            flag=flag,
        )

        get_api_admin_backup_configurations_backup_configuration_locations_response_200_locations_location.additional_properties = d
        return get_api_admin_backup_configurations_backup_configuration_locations_response_200_locations_location

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
