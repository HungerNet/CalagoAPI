from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.admin_user import AdminUser


T = TypeVar("T", bound="AdminUserOAuthLink")


@_attrs_define
class AdminUserOAuthLink:
    """
    Attributes:
        uuid (UUID):
        user (AdminUser):
        identifier (str):
        created (datetime.datetime):
        last_used (datetime.datetime | None | Unset):
    """

    uuid: UUID
    user: AdminUser
    identifier: str
    created: datetime.datetime
    last_used: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        user = self.user.to_dict()

        identifier = self.identifier

        created = self.created.isoformat()

        last_used: None | str | Unset
        if isinstance(self.last_used, Unset):
            last_used = UNSET
        elif isinstance(self.last_used, datetime.datetime):
            last_used = self.last_used.isoformat()
        else:
            last_used = self.last_used

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "user": user,
                "identifier": identifier,
                "created": created,
            }
        )
        if last_used is not UNSET:
            field_dict["last_used"] = last_used

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.admin_user import AdminUser  # noqa: PLC0415

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        user = AdminUser.from_dict(d.pop("user"))

        identifier = d.pop("identifier")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        def _parse_last_used(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_used_type_0 = datetime.datetime.fromisoformat(data)

                return last_used_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_used = _parse_last_used(d.pop("last_used", UNSET))

        admin_user_o_auth_link = cls(
            uuid=uuid,
            user=user,
            identifier=identifier,
            created=created,
            last_used=last_used,
        )

        admin_user_o_auth_link.additional_properties = d
        return admin_user_o_auth_link

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
