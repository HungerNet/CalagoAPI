from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadEntry")


@_attrs_define
class UploadEntry:
    """
    Attributes:
        name (str):
        target_name (str):
        directory (str):
        uploaded (int):
        resumable (bool):
        active (bool):
        user (None | Unset | UUID):
        user_name (None | str | Unset):
        total (int | None | Unset):
        started (datetime.datetime | None | Unset):
        updated (datetime.datetime | None | Unset):
    """

    name: str
    target_name: str
    directory: str
    uploaded: int
    resumable: bool
    active: bool
    user: None | Unset | UUID = UNSET
    user_name: None | str | Unset = UNSET
    total: int | None | Unset = UNSET
    started: datetime.datetime | None | Unset = UNSET
    updated: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        target_name = self.target_name

        directory = self.directory

        uploaded = self.uploaded

        resumable = self.resumable

        active = self.active

        user: None | str | Unset
        if isinstance(self.user, Unset):
            user = UNSET
        elif isinstance(self.user, UUID):
            user = str(self.user)
        else:
            user = self.user

        user_name: None | str | Unset
        if isinstance(self.user_name, Unset):
            user_name = UNSET
        else:
            user_name = self.user_name

        total: int | None | Unset
        if isinstance(self.total, Unset):
            total = UNSET
        else:
            total = self.total

        started: None | str | Unset
        if isinstance(self.started, Unset):
            started = UNSET
        elif isinstance(self.started, datetime.datetime):
            started = self.started.isoformat()
        else:
            started = self.started

        updated: None | str | Unset
        if isinstance(self.updated, Unset):
            updated = UNSET
        elif isinstance(self.updated, datetime.datetime):
            updated = self.updated.isoformat()
        else:
            updated = self.updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "target_name": target_name,
                "directory": directory,
                "uploaded": uploaded,
                "resumable": resumable,
                "active": active,
            }
        )
        if user is not UNSET:
            field_dict["user"] = user
        if user_name is not UNSET:
            field_dict["user_name"] = user_name
        if total is not UNSET:
            field_dict["total"] = total
        if started is not UNSET:
            field_dict["started"] = started
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        target_name = d.pop("target_name")

        directory = d.pop("directory")

        uploaded = d.pop("uploaded")

        resumable = d.pop("resumable")

        active = d.pop("active")

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

        def _parse_user_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_name = _parse_user_name(d.pop("user_name", UNSET))

        def _parse_total(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total = _parse_total(d.pop("total", UNSET))

        def _parse_started(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_type_0 = datetime.datetime.fromisoformat(data)

                return started_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        started = _parse_started(d.pop("started", UNSET))

        def _parse_updated(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_type_0 = datetime.datetime.fromisoformat(data)

                return updated_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated = _parse_updated(d.pop("updated", UNSET))

        upload_entry = cls(
            name=name,
            target_name=target_name,
            directory=directory,
            uploaded=uploaded,
            resumable=resumable,
            active=active,
            user=user,
            user_name=user_name,
            total=total,
            started=started,
            updated=updated,
        )

        upload_entry.additional_properties = d
        return upload_entry

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
