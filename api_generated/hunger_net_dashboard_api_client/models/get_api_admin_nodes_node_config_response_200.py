from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.response_200 import Response200


T = TypeVar("T", bound="GetApiAdminNodesNodeConfigResponse200")


@_attrs_define
class GetApiAdminNodesNodeConfigResponse200:
    """
    Attributes:
        config (Response200):
        locked_paths (list[str]):
    """

    config: Response200
    locked_paths: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config = self.config.to_dict()

        locked_paths = self.locked_paths

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config": config,
                "locked_paths": locked_paths,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.response_200 import Response200  # noqa: PLC0415

        d = dict(src_dict)
        config = Response200.from_dict(d.pop("config"))

        locked_paths = cast(list[str], d.pop("locked_paths"))

        get_api_admin_nodes_node_config_response_200 = cls(
            config=config,
            locked_paths=locked_paths,
        )

        get_api_admin_nodes_node_config_response_200.additional_properties = d
        return get_api_admin_nodes_node_config_response_200

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
