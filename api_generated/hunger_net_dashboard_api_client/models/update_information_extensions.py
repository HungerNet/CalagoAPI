from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.extension_update_check_result_type_0 import ExtensionUpdateCheckResultType0
    from ..models.extension_update_check_result_type_1 import ExtensionUpdateCheckResultType1
    from ..models.extension_update_check_result_type_2 import ExtensionUpdateCheckResultType2


T = TypeVar("T", bound="UpdateInformationExtensions")


@_attrs_define
class UpdateInformationExtensions:
    additional_properties: dict[
        str, ExtensionUpdateCheckResultType0 | ExtensionUpdateCheckResultType1 | ExtensionUpdateCheckResultType2
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.extension_update_check_result_type_0 import ExtensionUpdateCheckResultType0  # noqa: PLC0415
        from ..models.extension_update_check_result_type_1 import ExtensionUpdateCheckResultType1  # noqa: PLC0415

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, ExtensionUpdateCheckResultType0):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ExtensionUpdateCheckResultType1):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.extension_update_check_result_type_0 import ExtensionUpdateCheckResultType0  # noqa: PLC0415
        from ..models.extension_update_check_result_type_1 import ExtensionUpdateCheckResultType1  # noqa: PLC0415
        from ..models.extension_update_check_result_type_2 import ExtensionUpdateCheckResultType2  # noqa: PLC0415

        d = dict(src_dict)
        update_information_extensions = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(
                data: object,
            ) -> ExtensionUpdateCheckResultType0 | ExtensionUpdateCheckResultType1 | ExtensionUpdateCheckResultType2:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_extension_update_check_result_type_0 = ExtensionUpdateCheckResultType0.from_dict(
                        data
                    )

                    return componentsschemas_extension_update_check_result_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_extension_update_check_result_type_1 = ExtensionUpdateCheckResultType1.from_dict(
                        data
                    )

                    return componentsschemas_extension_update_check_result_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_extension_update_check_result_type_2 = ExtensionUpdateCheckResultType2.from_dict(data)

                return componentsschemas_extension_update_check_result_type_2

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        update_information_extensions.additional_properties = additional_properties
        return update_information_extensions

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> ExtensionUpdateCheckResultType0 | ExtensionUpdateCheckResultType1 | ExtensionUpdateCheckResultType2:
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: ExtensionUpdateCheckResultType0 | ExtensionUpdateCheckResultType1 | ExtensionUpdateCheckResultType2,
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
