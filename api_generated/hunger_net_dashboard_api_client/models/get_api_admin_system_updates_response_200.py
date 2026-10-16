from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_information import UpdateInformation


T = TypeVar("T", bound="GetApiAdminSystemUpdatesResponse200")


@_attrs_define
class GetApiAdminSystemUpdatesResponse200:
    """
    Attributes:
        update_information (None | Unset | UpdateInformation):
    """

    update_information: None | Unset | UpdateInformation = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_information import UpdateInformation  # noqa: PLC0415

        update_information: dict[str, Any] | None | Unset
        if isinstance(self.update_information, Unset):
            update_information = UNSET
        elif isinstance(self.update_information, UpdateInformation):
            update_information = self.update_information.to_dict()
        else:
            update_information = self.update_information

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if update_information is not UNSET:
            field_dict["update_information"] = update_information

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_information import UpdateInformation  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_update_information(data: object) -> None | Unset | UpdateInformation:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                update_information_type_1 = UpdateInformation.from_dict(data)

                return update_information_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateInformation, data)

        update_information = _parse_update_information(d.pop("update_information", UNSET))

        get_api_admin_system_updates_response_200 = cls(
            update_information=update_information,
        )

        get_api_admin_system_updates_response_200.additional_properties = d
        return get_api_admin_system_updates_response_200

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
