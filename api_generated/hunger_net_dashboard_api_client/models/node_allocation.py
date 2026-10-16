from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.admin_server import AdminServer


T = TypeVar("T", bound="NodeAllocation")


@_attrs_define
class NodeAllocation:
    """
    Attributes:
        uuid (UUID):
        ip (str):
        port (int):
        created (datetime.datetime):
        server (AdminServer | None | Unset):
        ip_alias (None | str | Unset):
    """

    uuid: UUID
    ip: str
    port: int
    created: datetime.datetime
    server: AdminServer | None | Unset = UNSET
    ip_alias: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.admin_server import AdminServer  # noqa: PLC0415

        uuid = str(self.uuid)

        ip = self.ip

        port = self.port

        created = self.created.isoformat()

        server: dict[str, Any] | None | Unset
        if isinstance(self.server, Unset):
            server = UNSET
        elif isinstance(self.server, AdminServer):
            server = self.server.to_dict()
        else:
            server = self.server

        ip_alias: None | str | Unset
        if isinstance(self.ip_alias, Unset):
            ip_alias = UNSET
        else:
            ip_alias = self.ip_alias

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "ip": ip,
                "port": port,
                "created": created,
            }
        )
        if server is not UNSET:
            field_dict["server"] = server
        if ip_alias is not UNSET:
            field_dict["ip_alias"] = ip_alias

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.admin_server import AdminServer  # noqa: PLC0415

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        ip = d.pop("ip")

        port = d.pop("port")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        def _parse_server(data: object) -> AdminServer | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                server_type_1 = AdminServer.from_dict(data)

                return server_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AdminServer | None | Unset, data)

        server = _parse_server(d.pop("server", UNSET))

        def _parse_ip_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ip_alias = _parse_ip_alias(d.pop("ip_alias", UNSET))

        node_allocation = cls(
            uuid=uuid,
            ip=ip,
            port=port,
            created=created,
            server=server,
            ip_alias=ip_alias,
        )

        node_allocation.additional_properties = d
        return node_allocation

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
