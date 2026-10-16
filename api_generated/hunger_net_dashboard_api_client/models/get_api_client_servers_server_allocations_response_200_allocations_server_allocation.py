from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetApiClientServersServerAllocationsResponse200AllocationsServerAllocation")


@_attrs_define
class GetApiClientServersServerAllocationsResponse200AllocationsServerAllocation:
    """
    Attributes:
        uuid (UUID):
        ip (str):
        port (int):
        is_primary (bool):
        created (datetime.datetime):
        ip_alias (None | str | Unset):
        notes (None | str | Unset):
    """

    uuid: UUID
    ip: str
    port: int
    is_primary: bool
    created: datetime.datetime
    ip_alias: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        ip = self.ip

        port = self.port

        is_primary = self.is_primary

        created = self.created.isoformat()

        ip_alias: None | str | Unset
        if isinstance(self.ip_alias, Unset):
            ip_alias = UNSET
        else:
            ip_alias = self.ip_alias

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "ip": ip,
                "port": port,
                "is_primary": is_primary,
                "created": created,
            }
        )
        if ip_alias is not UNSET:
            field_dict["ip_alias"] = ip_alias
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        ip = d.pop("ip")

        port = d.pop("port")

        is_primary = d.pop("is_primary")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        def _parse_ip_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ip_alias = _parse_ip_alias(d.pop("ip_alias", UNSET))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        get_api_client_servers_server_allocations_response_200_allocations_server_allocation = cls(
            uuid=uuid,
            ip=ip,
            port=port,
            is_primary=is_primary,
            created=created,
            ip_alias=ip_alias,
            notes=notes,
        )

        get_api_client_servers_server_allocations_response_200_allocations_server_allocation.additional_properties = d
        return get_api_client_servers_server_allocations_response_200_allocations_server_allocation

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
