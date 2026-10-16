from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_api_admin_system_overview_response_200_cache_coalesced_waits import (
        GetApiAdminSystemOverviewResponse200CacheCoalescedWaits,
    )
    from ..models.get_api_admin_system_overview_response_200_cache_local_hits import (
        GetApiAdminSystemOverviewResponse200CacheLocalHits,
    )
    from ..models.get_api_admin_system_overview_response_200_cache_remote_hits import (
        GetApiAdminSystemOverviewResponse200CacheRemoteHits,
    )


T = TypeVar("T", bound="GetApiAdminSystemOverviewResponse200Cache")


@_attrs_define
class GetApiAdminSystemOverviewResponse200Cache:
    """
    Attributes:
        version (str):
        total_calls (int):
        total_hits (int):
        total_misses (int):
        average_hit_latency_ns (int):
        average_miss_latency_ns (int):
        max_call_latency_ns (int):
        local_hits (GetApiAdminSystemOverviewResponse200CacheLocalHits):
        remote_hits (GetApiAdminSystemOverviewResponse200CacheRemoteHits):
        coalesced_waits (GetApiAdminSystemOverviewResponse200CacheCoalescedWaits):
    """

    version: str
    total_calls: int
    total_hits: int
    total_misses: int
    average_hit_latency_ns: int
    average_miss_latency_ns: int
    max_call_latency_ns: int
    local_hits: GetApiAdminSystemOverviewResponse200CacheLocalHits
    remote_hits: GetApiAdminSystemOverviewResponse200CacheRemoteHits
    coalesced_waits: GetApiAdminSystemOverviewResponse200CacheCoalescedWaits
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        total_calls = self.total_calls

        total_hits = self.total_hits

        total_misses = self.total_misses

        average_hit_latency_ns = self.average_hit_latency_ns

        average_miss_latency_ns = self.average_miss_latency_ns

        max_call_latency_ns = self.max_call_latency_ns

        local_hits = self.local_hits.to_dict()

        remote_hits = self.remote_hits.to_dict()

        coalesced_waits = self.coalesced_waits.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
                "total_calls": total_calls,
                "total_hits": total_hits,
                "total_misses": total_misses,
                "average_hit_latency_ns": average_hit_latency_ns,
                "average_miss_latency_ns": average_miss_latency_ns,
                "max_call_latency_ns": max_call_latency_ns,
                "local_hits": local_hits,
                "remote_hits": remote_hits,
                "coalesced_waits": coalesced_waits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_admin_system_overview_response_200_cache_coalesced_waits import (
            GetApiAdminSystemOverviewResponse200CacheCoalescedWaits,  # noqa: PLC0415
        )
        from ..models.get_api_admin_system_overview_response_200_cache_local_hits import (
            GetApiAdminSystemOverviewResponse200CacheLocalHits,  # noqa: PLC0415
        )
        from ..models.get_api_admin_system_overview_response_200_cache_remote_hits import (
            GetApiAdminSystemOverviewResponse200CacheRemoteHits,  # noqa: PLC0415
        )

        d = dict(src_dict)
        version = d.pop("version")

        total_calls = d.pop("total_calls")

        total_hits = d.pop("total_hits")

        total_misses = d.pop("total_misses")

        average_hit_latency_ns = d.pop("average_hit_latency_ns")

        average_miss_latency_ns = d.pop("average_miss_latency_ns")

        max_call_latency_ns = d.pop("max_call_latency_ns")

        local_hits = GetApiAdminSystemOverviewResponse200CacheLocalHits.from_dict(d.pop("local_hits"))

        remote_hits = GetApiAdminSystemOverviewResponse200CacheRemoteHits.from_dict(d.pop("remote_hits"))

        coalesced_waits = GetApiAdminSystemOverviewResponse200CacheCoalescedWaits.from_dict(d.pop("coalesced_waits"))

        get_api_admin_system_overview_response_200_cache = cls(
            version=version,
            total_calls=total_calls,
            total_hits=total_hits,
            total_misses=total_misses,
            average_hit_latency_ns=average_hit_latency_ns,
            average_miss_latency_ns=average_miss_latency_ns,
            max_call_latency_ns=max_call_latency_ns,
            local_hits=local_hits,
            remote_hits=remote_hits,
            coalesced_waits=coalesced_waits,
        )

        get_api_admin_system_overview_response_200_cache.additional_properties = d
        return get_api_admin_system_overview_response_200_cache

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
