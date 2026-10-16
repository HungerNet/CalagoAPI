from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.server_subuser import ServerSubuser


T = TypeVar("T", bound="PostApiClientServersServerSubusersResponse200")


@_attrs_define
class PostApiClientServersServerSubusersResponse200:
    """
    Attributes:
        subuser (ServerSubuser):
    """

    subuser: ServerSubuser
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subuser = self.subuser.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subuser": subuser,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_subuser import ServerSubuser  # noqa: PLC0415

        d = dict(src_dict)
        subuser = ServerSubuser.from_dict(d.pop("subuser"))

        post_api_client_servers_server_subusers_response_200 = cls(
            subuser=subuser,
        )

        post_api_client_servers_server_subusers_response_200.additional_properties = d
        return post_api_client_servers_server_subusers_response_200

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
