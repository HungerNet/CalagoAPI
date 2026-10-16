from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_api_remote_schedule_body_data_item_errors import PostApiRemoteScheduleBodyDataItemErrors


T = TypeVar("T", bound="PostApiRemoteScheduleBodyDataItem")


@_attrs_define
class PostApiRemoteScheduleBodyDataItem:
    """
    Attributes:
        uuid (UUID):
        successful (bool):
        errors (PostApiRemoteScheduleBodyDataItemErrors):
        timestamp (datetime.datetime):
    """

    uuid: UUID
    successful: bool
    errors: PostApiRemoteScheduleBodyDataItemErrors
    timestamp: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        successful = self.successful

        errors = self.errors.to_dict()

        timestamp = self.timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "successful": successful,
                "errors": errors,
                "timestamp": timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_remote_schedule_body_data_item_errors import PostApiRemoteScheduleBodyDataItemErrors  # noqa: PLC0415

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        successful = d.pop("successful")

        errors = PostApiRemoteScheduleBodyDataItemErrors.from_dict(d.pop("errors"))

        timestamp = datetime.datetime.fromisoformat(d.pop("timestamp"))

        post_api_remote_schedule_body_data_item = cls(
            uuid=uuid,
            successful=successful,
            errors=errors,
            timestamp=timestamp,
        )

        post_api_remote_schedule_body_data_item.additional_properties = d
        return post_api_remote_schedule_body_data_item

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
