from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.route_order_item_type_0 import RouteOrderItemType0
    from ..models.route_order_item_type_1 import RouteOrderItemType1
    from ..models.route_order_item_type_2 import RouteOrderItemType2


T = TypeVar("T", bound="PutApiAdminSettingsBodyUserType1")


@_attrs_define
class PutApiAdminSettingsBodyUserType1:
    """
    Attributes:
        max_server_group_count (int | None | Unset):
        max_api_key_count (int | None | Unset):
        max_command_snippet_count (int | None | Unset):
        max_security_key_count (int | None | Unset):
        max_ssh_key_count (int | None | Unset):
        max_settings_count (int | None | Unset):
        max_settings_value_bytes (int | None | Unset):
        allow_changing_language (bool | None | Unset):
        route_order (list[RouteOrderItemType0 | RouteOrderItemType1 | RouteOrderItemType2] | None | Unset):
    """

    max_server_group_count: int | None | Unset = UNSET
    max_api_key_count: int | None | Unset = UNSET
    max_command_snippet_count: int | None | Unset = UNSET
    max_security_key_count: int | None | Unset = UNSET
    max_ssh_key_count: int | None | Unset = UNSET
    max_settings_count: int | None | Unset = UNSET
    max_settings_value_bytes: int | None | Unset = UNSET
    allow_changing_language: bool | None | Unset = UNSET
    route_order: list[RouteOrderItemType0 | RouteOrderItemType1 | RouteOrderItemType2] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.route_order_item_type_0 import RouteOrderItemType0  # noqa: PLC0415
        from ..models.route_order_item_type_1 import RouteOrderItemType1  # noqa: PLC0415

        max_server_group_count: int | None | Unset
        if isinstance(self.max_server_group_count, Unset):
            max_server_group_count = UNSET
        else:
            max_server_group_count = self.max_server_group_count

        max_api_key_count: int | None | Unset
        if isinstance(self.max_api_key_count, Unset):
            max_api_key_count = UNSET
        else:
            max_api_key_count = self.max_api_key_count

        max_command_snippet_count: int | None | Unset
        if isinstance(self.max_command_snippet_count, Unset):
            max_command_snippet_count = UNSET
        else:
            max_command_snippet_count = self.max_command_snippet_count

        max_security_key_count: int | None | Unset
        if isinstance(self.max_security_key_count, Unset):
            max_security_key_count = UNSET
        else:
            max_security_key_count = self.max_security_key_count

        max_ssh_key_count: int | None | Unset
        if isinstance(self.max_ssh_key_count, Unset):
            max_ssh_key_count = UNSET
        else:
            max_ssh_key_count = self.max_ssh_key_count

        max_settings_count: int | None | Unset
        if isinstance(self.max_settings_count, Unset):
            max_settings_count = UNSET
        else:
            max_settings_count = self.max_settings_count

        max_settings_value_bytes: int | None | Unset
        if isinstance(self.max_settings_value_bytes, Unset):
            max_settings_value_bytes = UNSET
        else:
            max_settings_value_bytes = self.max_settings_value_bytes

        allow_changing_language: bool | None | Unset
        if isinstance(self.allow_changing_language, Unset):
            allow_changing_language = UNSET
        else:
            allow_changing_language = self.allow_changing_language

        route_order: list[dict[str, Any]] | None | Unset
        if isinstance(self.route_order, Unset):
            route_order = UNSET
        elif isinstance(self.route_order, list):
            route_order = []
            for route_order_type_0_item_data in self.route_order:
                route_order_type_0_item: dict[str, Any]
                if isinstance(route_order_type_0_item_data, RouteOrderItemType0):
                    route_order_type_0_item = route_order_type_0_item_data.to_dict()
                elif isinstance(route_order_type_0_item_data, RouteOrderItemType1):
                    route_order_type_0_item = route_order_type_0_item_data.to_dict()
                else:
                    route_order_type_0_item = route_order_type_0_item_data.to_dict()

                route_order.append(route_order_type_0_item)

        else:
            route_order = self.route_order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_server_group_count is not UNSET:
            field_dict["max_server_group_count"] = max_server_group_count
        if max_api_key_count is not UNSET:
            field_dict["max_api_key_count"] = max_api_key_count
        if max_command_snippet_count is not UNSET:
            field_dict["max_command_snippet_count"] = max_command_snippet_count
        if max_security_key_count is not UNSET:
            field_dict["max_security_key_count"] = max_security_key_count
        if max_ssh_key_count is not UNSET:
            field_dict["max_ssh_key_count"] = max_ssh_key_count
        if max_settings_count is not UNSET:
            field_dict["max_settings_count"] = max_settings_count
        if max_settings_value_bytes is not UNSET:
            field_dict["max_settings_value_bytes"] = max_settings_value_bytes
        if allow_changing_language is not UNSET:
            field_dict["allow_changing_language"] = allow_changing_language
        if route_order is not UNSET:
            field_dict["route_order"] = route_order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.route_order_item_type_0 import RouteOrderItemType0  # noqa: PLC0415
        from ..models.route_order_item_type_1 import RouteOrderItemType1  # noqa: PLC0415
        from ..models.route_order_item_type_2 import RouteOrderItemType2  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_max_server_group_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_server_group_count = _parse_max_server_group_count(d.pop("max_server_group_count", UNSET))

        def _parse_max_api_key_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_api_key_count = _parse_max_api_key_count(d.pop("max_api_key_count", UNSET))

        def _parse_max_command_snippet_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_command_snippet_count = _parse_max_command_snippet_count(d.pop("max_command_snippet_count", UNSET))

        def _parse_max_security_key_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_security_key_count = _parse_max_security_key_count(d.pop("max_security_key_count", UNSET))

        def _parse_max_ssh_key_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_ssh_key_count = _parse_max_ssh_key_count(d.pop("max_ssh_key_count", UNSET))

        def _parse_max_settings_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_settings_count = _parse_max_settings_count(d.pop("max_settings_count", UNSET))

        def _parse_max_settings_value_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_settings_value_bytes = _parse_max_settings_value_bytes(d.pop("max_settings_value_bytes", UNSET))

        def _parse_allow_changing_language(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_changing_language = _parse_allow_changing_language(d.pop("allow_changing_language", UNSET))

        def _parse_route_order(
            data: object,
        ) -> list[RouteOrderItemType0 | RouteOrderItemType1 | RouteOrderItemType2] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                route_order_type_0 = []
                _route_order_type_0 = data
                for route_order_type_0_item_data in _route_order_type_0:

                    def _parse_route_order_type_0_item(
                        data: object,
                    ) -> RouteOrderItemType0 | RouteOrderItemType1 | RouteOrderItemType2:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_route_order_item_type_0 = RouteOrderItemType0.from_dict(data)

                            return componentsschemas_route_order_item_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_route_order_item_type_1 = RouteOrderItemType1.from_dict(data)

                            return componentsschemas_route_order_item_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_route_order_item_type_2 = RouteOrderItemType2.from_dict(data)

                        return componentsschemas_route_order_item_type_2

                    route_order_type_0_item = _parse_route_order_type_0_item(route_order_type_0_item_data)

                    route_order_type_0.append(route_order_type_0_item)

                return route_order_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RouteOrderItemType0 | RouteOrderItemType1 | RouteOrderItemType2] | None | Unset, data)

        route_order = _parse_route_order(d.pop("route_order", UNSET))

        put_api_admin_settings_body_user_type_1 = cls(
            max_server_group_count=max_server_group_count,
            max_api_key_count=max_api_key_count,
            max_command_snippet_count=max_command_snippet_count,
            max_security_key_count=max_security_key_count,
            max_ssh_key_count=max_ssh_key_count,
            max_settings_count=max_settings_count,
            max_settings_value_bytes=max_settings_value_bytes,
            allow_changing_language=allow_changing_language,
            route_order=route_order,
        )

        put_api_admin_settings_body_user_type_1.additional_properties = d
        return put_api_admin_settings_body_user_type_1

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
