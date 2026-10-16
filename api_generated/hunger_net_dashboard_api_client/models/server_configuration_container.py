from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_configuration_container_seccomp import ServerConfigurationContainerSeccomp


T = TypeVar("T", bound="ServerConfigurationContainer")


@_attrs_define
class ServerConfigurationContainer:
    """
    Attributes:
        image (str):
        hugepages_passthrough_enabled (bool):
        kvm_passthrough_enabled (bool):
        seccomp (ServerConfigurationContainerSeccomp):
        timezone (None | str | Unset):
    """

    image: str
    hugepages_passthrough_enabled: bool
    kvm_passthrough_enabled: bool
    seccomp: ServerConfigurationContainerSeccomp
    timezone: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image = self.image

        hugepages_passthrough_enabled = self.hugepages_passthrough_enabled

        kvm_passthrough_enabled = self.kvm_passthrough_enabled

        seccomp = self.seccomp.to_dict()

        timezone: None | str | Unset
        if isinstance(self.timezone, Unset):
            timezone = UNSET
        else:
            timezone = self.timezone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "image": image,
                "hugepages_passthrough_enabled": hugepages_passthrough_enabled,
                "kvm_passthrough_enabled": kvm_passthrough_enabled,
                "seccomp": seccomp,
            }
        )
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_configuration_container_seccomp import ServerConfigurationContainerSeccomp  # noqa: PLC0415

        d = dict(src_dict)
        image = d.pop("image")

        hugepages_passthrough_enabled = d.pop("hugepages_passthrough_enabled")

        kvm_passthrough_enabled = d.pop("kvm_passthrough_enabled")

        seccomp = ServerConfigurationContainerSeccomp.from_dict(d.pop("seccomp"))

        def _parse_timezone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        timezone = _parse_timezone(d.pop("timezone", UNSET))

        server_configuration_container = cls(
            image=image,
            hugepages_passthrough_enabled=hugepages_passthrough_enabled,
            kvm_passthrough_enabled=kvm_passthrough_enabled,
            seccomp=seccomp,
            timezone=timezone,
        )

        server_configuration_container.additional_properties = d
        return server_configuration_container

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
