from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiAdminLocationsBody")


@_attrs_define
class PostApiAdminLocationsBody:
    """
    Attributes:
        name (str):
        backup_configuration_uuid (None | Unset | UUID):
        description (None | str | Unset):
        flag (None | str | Unset):
    """

    name: str
    backup_configuration_uuid: None | Unset | UUID = UNSET
    description: None | str | Unset = UNSET
    flag: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        backup_configuration_uuid: None | str | Unset
        if isinstance(self.backup_configuration_uuid, Unset):
            backup_configuration_uuid = UNSET
        elif isinstance(self.backup_configuration_uuid, UUID):
            backup_configuration_uuid = str(self.backup_configuration_uuid)
        else:
            backup_configuration_uuid = self.backup_configuration_uuid

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
                "name": name,
            }
        )
        if backup_configuration_uuid is not UNSET:
            field_dict["backup_configuration_uuid"] = backup_configuration_uuid
        if description is not UNSET:
            field_dict["description"] = description
        if flag is not UNSET:
            field_dict["flag"] = flag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_backup_configuration_uuid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                backup_configuration_uuid_type_0 = UUID(data)

                return backup_configuration_uuid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        backup_configuration_uuid = _parse_backup_configuration_uuid(d.pop("backup_configuration_uuid", UNSET))

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

        post_api_admin_locations_body = cls(
            name=name,
            backup_configuration_uuid=backup_configuration_uuid,
            description=description,
            flag=flag,
        )

        post_api_admin_locations_body.additional_properties = d
        return post_api_admin_locations_body

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
