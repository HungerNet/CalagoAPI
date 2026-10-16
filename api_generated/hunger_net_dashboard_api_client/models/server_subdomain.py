from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain import Domain
    from ..models.server_allocation import ServerAllocation


T = TypeVar("T", bound="ServerSubdomain")


@_attrs_define
class ServerSubdomain:
    """
    Attributes:
        uuid (UUID):
        domain (Domain):
        subdomain (str):
        created (datetime.datetime):
        allocation (None | ServerAllocation | Unset):
    """

    uuid: UUID
    domain: Domain
    subdomain: str
    created: datetime.datetime
    allocation: None | ServerAllocation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.server_allocation import ServerAllocation  # noqa: PLC0415

        uuid = str(self.uuid)

        domain = self.domain.to_dict()

        subdomain = self.subdomain

        created = self.created.isoformat()

        allocation: dict[str, Any] | None | Unset
        if isinstance(self.allocation, Unset):
            allocation = UNSET
        elif isinstance(self.allocation, ServerAllocation):
            allocation = self.allocation.to_dict()
        else:
            allocation = self.allocation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "domain": domain,
                "subdomain": subdomain,
                "created": created,
            }
        )
        if allocation is not UNSET:
            field_dict["allocation"] = allocation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domain import Domain  # noqa: PLC0415
        from ..models.server_allocation import ServerAllocation  # noqa: PLC0415

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        domain = Domain.from_dict(d.pop("domain"))

        subdomain = d.pop("subdomain")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        def _parse_allocation(data: object) -> None | ServerAllocation | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                allocation_type_1 = ServerAllocation.from_dict(data)

                return allocation_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ServerAllocation | Unset, data)

        allocation = _parse_allocation(d.pop("allocation", UNSET))

        server_subdomain = cls(
            uuid=uuid,
            domain=domain,
            subdomain=subdomain,
            created=created,
            allocation=allocation,
        )

        server_subdomain.additional_properties = d
        return server_subdomain

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
