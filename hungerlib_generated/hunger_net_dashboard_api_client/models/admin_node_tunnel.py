from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminNodeTunnel")


@_attrs_define
class AdminNodeTunnel:
    """
    Attributes:
        host (str):
        port (int):
        created (datetime.datetime):
        cert_sha256 (None | str | Unset):
    """

    host: str
    port: int
    created: datetime.datetime
    cert_sha256: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        host = self.host

        port = self.port

        created = self.created.isoformat()

        cert_sha256: None | str | Unset
        if isinstance(self.cert_sha256, Unset):
            cert_sha256 = UNSET
        else:
            cert_sha256 = self.cert_sha256

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "host": host,
                "port": port,
                "created": created,
            }
        )
        if cert_sha256 is not UNSET:
            field_dict["cert_sha256"] = cert_sha256

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        host = d.pop("host")

        port = d.pop("port")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        def _parse_cert_sha256(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cert_sha256 = _parse_cert_sha256(d.pop("cert_sha256", UNSET))

        admin_node_tunnel = cls(
            host=host,
            port=port,
            created=created,
            cert_sha256=cert_sha256,
        )

        admin_node_tunnel.additional_properties = d
        return admin_node_tunnel

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
