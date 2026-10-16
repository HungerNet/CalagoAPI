from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user import User


T = TypeVar("T", bound="GetApiClientServersServerActivityResponse200ActivitiesServerActivity")


@_attrs_define
class GetApiClientServersServerActivityResponse200ActivitiesServerActivity:
    """
    Attributes:
        event (str):
        data (Any):
        is_api (bool):
        is_schedule (bool):
        created (datetime.datetime):
        user (None | Unset | User):
        impersonator (None | Unset | User):
        ip (None | str | Unset):
    """

    event: str
    data: Any
    is_api: bool
    is_schedule: bool
    created: datetime.datetime
    user: None | Unset | User = UNSET
    impersonator: None | Unset | User = UNSET
    ip: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user import User  # noqa: PLC0415

        event = self.event

        data = self.data

        is_api = self.is_api

        is_schedule = self.is_schedule

        created = self.created.isoformat()

        user: dict[str, Any] | None | Unset
        if isinstance(self.user, Unset):
            user = UNSET
        elif isinstance(self.user, User):
            user = self.user.to_dict()
        else:
            user = self.user

        impersonator: dict[str, Any] | None | Unset
        if isinstance(self.impersonator, Unset):
            impersonator = UNSET
        elif isinstance(self.impersonator, User):
            impersonator = self.impersonator.to_dict()
        else:
            impersonator = self.impersonator

        ip: None | str | Unset
        if isinstance(self.ip, Unset):
            ip = UNSET
        else:
            ip = self.ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event": event,
                "data": data,
                "is_api": is_api,
                "is_schedule": is_schedule,
                "created": created,
            }
        )
        if user is not UNSET:
            field_dict["user"] = user
        if impersonator is not UNSET:
            field_dict["impersonator"] = impersonator
        if ip is not UNSET:
            field_dict["ip"] = ip

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user import User  # noqa: PLC0415

        d = dict(src_dict)
        event = d.pop("event")

        data = d.pop("data")

        is_api = d.pop("is_api")

        is_schedule = d.pop("is_schedule")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        def _parse_user(data: object) -> None | Unset | User:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_type_1 = User.from_dict(data)

                return user_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | User, data)

        user = _parse_user(d.pop("user", UNSET))

        def _parse_impersonator(data: object) -> None | Unset | User:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                impersonator_type_1 = User.from_dict(data)

                return impersonator_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | User, data)

        impersonator = _parse_impersonator(d.pop("impersonator", UNSET))

        def _parse_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ip = _parse_ip(d.pop("ip", UNSET))

        get_api_client_servers_server_activity_response_200_activities_server_activity = cls(
            event=event,
            data=data,
            is_api=is_api,
            is_schedule=is_schedule,
            created=created,
            user=user,
            impersonator=impersonator,
            ip=ip,
        )

        get_api_client_servers_server_activity_response_200_activities_server_activity.additional_properties = d
        return get_api_client_servers_server_activity_response_200_activities_server_activity

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
