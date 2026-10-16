from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.resource_usage import ResourceUsage


T = TypeVar("T", bound="GetApiClientServersServerResourcesResponse200")


@_attrs_define
class GetApiClientServersServerResourcesResponse200:
    """
    Attributes:
        resources (ResourceUsage):
    """

    resources: ResourceUsage
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resources = self.resources.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resources": resources,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_usage import ResourceUsage  # noqa: PLC0415

        d = dict(src_dict)
        resources = ResourceUsage.from_dict(d.pop("resources"))

        get_api_client_servers_server_resources_response_200 = cls(
            resources=resources,
        )

        get_api_client_servers_server_resources_response_200.additional_properties = d
        return get_api_client_servers_server_resources_response_200

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
