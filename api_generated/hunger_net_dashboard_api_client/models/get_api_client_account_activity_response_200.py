from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_client_account_activity_response_200_activities import (
        GetApiClientAccountActivityResponse200Activities,
    )


T = TypeVar("T", bound="GetApiClientAccountActivityResponse200")


@_attrs_define
class GetApiClientAccountActivityResponse200:
    """
    Attributes:
        activities (GetApiClientAccountActivityResponse200Activities):
    """

    activities: GetApiClientAccountActivityResponse200Activities
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activities = self.activities.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "activities": activities,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_client_account_activity_response_200_activities import (
            GetApiClientAccountActivityResponse200Activities,  # noqa: PLC0415
        )

        d = dict(src_dict)
        activities = GetApiClientAccountActivityResponse200Activities.from_dict(d.pop("activities"))

        get_api_client_account_activity_response_200 = cls(
            activities=activities,
        )

        get_api_client_account_activity_response_200.additional_properties = d
        return get_api_client_account_activity_response_200

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
