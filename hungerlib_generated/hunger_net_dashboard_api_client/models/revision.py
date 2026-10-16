from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user import User


T = TypeVar("T", bound="Revision")


@_attrs_define
class Revision:
    """
    Attributes:
        id (int):
        size (int):
        is_snapshot (bool):
        created (datetime.datetime):
        user (None | Unset | User):
    """

    id: int
    size: int
    is_snapshot: bool
    created: datetime.datetime
    user: None | Unset | User = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user import User  # noqa: PLC0415

        id = self.id

        size = self.size

        is_snapshot = self.is_snapshot

        created = self.created.isoformat()

        user: dict[str, Any] | None | Unset
        if isinstance(self.user, Unset):
            user = UNSET
        elif isinstance(self.user, User):
            user = self.user.to_dict()
        else:
            user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "size": size,
                "is_snapshot": is_snapshot,
                "created": created,
            }
        )
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user import User  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        size = d.pop("size")

        is_snapshot = d.pop("is_snapshot")

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

        revision = cls(
            id=id,
            size=size,
            is_snapshot=is_snapshot,
            created=created,
            user=user,
        )

        revision.additional_properties = d
        return revision

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
