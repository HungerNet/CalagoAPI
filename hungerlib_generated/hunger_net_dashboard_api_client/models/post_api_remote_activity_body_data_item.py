from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiRemoteActivityBodyDataItem")


@_attrs_define
class PostApiRemoteActivityBodyDataItem:
    """
    Attributes:
        server (UUID):
        event (str):
        timestamp (datetime.datetime):
        user (None | Unset | UUID):
        schedule (None | Unset | UUID):
        metadata (Any | Unset):
        ip (None | str | Unset):
    """

    server: UUID
    event: str
    timestamp: datetime.datetime
    user: None | Unset | UUID = UNSET
    schedule: None | Unset | UUID = UNSET
    metadata: Any | Unset = UNSET
    ip: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server = str(self.server)

        event = self.event

        timestamp = self.timestamp.isoformat()

        user: None | str | Unset
        if isinstance(self.user, Unset):
            user = UNSET
        elif isinstance(self.user, UUID):
            user = str(self.user)
        else:
            user = self.user

        schedule: None | str | Unset
        if isinstance(self.schedule, Unset):
            schedule = UNSET
        elif isinstance(self.schedule, UUID):
            schedule = str(self.schedule)
        else:
            schedule = self.schedule

        metadata = self.metadata

        ip: None | str | Unset
        if isinstance(self.ip, Unset):
            ip = UNSET
        else:
            ip = self.ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "server": server,
                "event": event,
                "timestamp": timestamp,
            }
        )
        if user is not UNSET:
            field_dict["user"] = user
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if ip is not UNSET:
            field_dict["ip"] = ip

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        server = UUID(d.pop("server"))

        event = d.pop("event")

        timestamp = datetime.datetime.fromisoformat(d.pop("timestamp"))

        def _parse_user(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_type_0 = UUID(data)

                return user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        user = _parse_user(d.pop("user", UNSET))

        def _parse_schedule(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                schedule_type_0 = UUID(data)

                return schedule_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        schedule = _parse_schedule(d.pop("schedule", UNSET))

        metadata = d.pop("metadata", UNSET)

        def _parse_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ip = _parse_ip(d.pop("ip", UNSET))

        post_api_remote_activity_body_data_item = cls(
            server=server,
            event=event,
            timestamp=timestamp,
            user=user,
            schedule=schedule,
            metadata=metadata,
            ip=ip,
        )

        post_api_remote_activity_body_data_item.additional_properties = d
        return post_api_remote_activity_body_data_item

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
