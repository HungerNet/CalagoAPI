from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetApiClientAccountSessionsResponse200SessionsUserSession")


@_attrs_define
class GetApiClientAccountSessionsResponse200SessionsUserSession:
    """
    Attributes:
        uuid (UUID):
        ip (str):
        user_agent (str):
        is_using (bool):
        last_used (datetime.datetime):
        created (datetime.datetime):
    """

    uuid: UUID
    ip: str
    user_agent: str
    is_using: bool
    last_used: datetime.datetime
    created: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        ip = self.ip

        user_agent = self.user_agent

        is_using = self.is_using

        last_used = self.last_used.isoformat()

        created = self.created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "ip": ip,
                "user_agent": user_agent,
                "is_using": is_using,
                "last_used": last_used,
                "created": created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        ip = d.pop("ip")

        user_agent = d.pop("user_agent")

        is_using = d.pop("is_using")

        last_used = datetime.datetime.fromisoformat(d.pop("last_used"))

        created = datetime.datetime.fromisoformat(d.pop("created"))

        get_api_client_account_sessions_response_200_sessions_user_session = cls(
            uuid=uuid,
            ip=ip,
            user_agent=user_agent,
            is_using=is_using,
            last_used=last_used,
            created=created,
        )

        get_api_client_account_sessions_response_200_sessions_user_session.additional_properties = d
        return get_api_client_account_sessions_response_200_sessions_user_session

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
