from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_api_admin_database_agent_hosts_database_agent_host_instances_database_instance_body_env_type_0 import (
        PatchApiAdminDatabaseAgentHostsDatabaseAgentHostInstancesDatabaseInstanceBodyEnvType0,
    )


T = TypeVar("T", bound="PatchApiAdminDatabaseAgentHostsDatabaseAgentHostInstancesDatabaseInstanceBody")


@_attrs_define
class PatchApiAdminDatabaseAgentHostsDatabaseAgentHostInstancesDatabaseInstanceBody:
    """
    Attributes:
        name (None | str | Unset):
        locked (bool | None | Unset):
        image (None | str | Unset):
        env (None | PatchApiAdminDatabaseAgentHostsDatabaseAgentHostInstancesDatabaseInstanceBodyEnvType0 | Unset):
        memory (int | None | Unset):
        swap (int | None | Unset):
        disk (int | None | Unset):
        io_weight (int | None | Unset):
        cpu (int | None | Unset):
    """

    name: None | str | Unset = UNSET
    locked: bool | None | Unset = UNSET
    image: None | str | Unset = UNSET
    env: None | PatchApiAdminDatabaseAgentHostsDatabaseAgentHostInstancesDatabaseInstanceBodyEnvType0 | Unset = UNSET
    memory: int | None | Unset = UNSET
    swap: int | None | Unset = UNSET
    disk: int | None | Unset = UNSET
    io_weight: int | None | Unset = UNSET
    cpu: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.patch_api_admin_database_agent_hosts_database_agent_host_instances_database_instance_body_env_type_0 import (
            PatchApiAdminDatabaseAgentHostsDatabaseAgentHostInstancesDatabaseInstanceBodyEnvType0,  # noqa: PLC0415
        )

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        locked: bool | None | Unset
        if isinstance(self.locked, Unset):
            locked = UNSET
        else:
            locked = self.locked

        image: None | str | Unset
        if isinstance(self.image, Unset):
            image = UNSET
        else:
            image = self.image

        env: dict[str, Any] | None | Unset
        if isinstance(self.env, Unset):
            env = UNSET
        elif isinstance(
            self.env, PatchApiAdminDatabaseAgentHostsDatabaseAgentHostInstancesDatabaseInstanceBodyEnvType0
        ):
            env = self.env.to_dict()
        else:
            env = self.env

        memory: int | None | Unset
        if isinstance(self.memory, Unset):
            memory = UNSET
        else:
            memory = self.memory

        swap: int | None | Unset
        if isinstance(self.swap, Unset):
            swap = UNSET
        else:
            swap = self.swap

        disk: int | None | Unset
        if isinstance(self.disk, Unset):
            disk = UNSET
        else:
            disk = self.disk

        io_weight: int | None | Unset
        if isinstance(self.io_weight, Unset):
            io_weight = UNSET
        else:
            io_weight = self.io_weight

        cpu: int | None | Unset
        if isinstance(self.cpu, Unset):
            cpu = UNSET
        else:
            cpu = self.cpu

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if locked is not UNSET:
            field_dict["locked"] = locked
        if image is not UNSET:
            field_dict["image"] = image
        if env is not UNSET:
            field_dict["env"] = env
        if memory is not UNSET:
            field_dict["memory"] = memory
        if swap is not UNSET:
            field_dict["swap"] = swap
        if disk is not UNSET:
            field_dict["disk"] = disk
        if io_weight is not UNSET:
            field_dict["io_weight"] = io_weight
        if cpu is not UNSET:
            field_dict["cpu"] = cpu

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_api_admin_database_agent_hosts_database_agent_host_instances_database_instance_body_env_type_0 import (
            PatchApiAdminDatabaseAgentHostsDatabaseAgentHostInstancesDatabaseInstanceBodyEnvType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_locked(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        locked = _parse_locked(d.pop("locked", UNSET))

        def _parse_image(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image = _parse_image(d.pop("image", UNSET))

        def _parse_env(
            data: object,
        ) -> None | PatchApiAdminDatabaseAgentHostsDatabaseAgentHostInstancesDatabaseInstanceBodyEnvType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                env_type_0 = (
                    PatchApiAdminDatabaseAgentHostsDatabaseAgentHostInstancesDatabaseInstanceBodyEnvType0.from_dict(
                        data
                    )
                )

                return env_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | PatchApiAdminDatabaseAgentHostsDatabaseAgentHostInstancesDatabaseInstanceBodyEnvType0 | Unset,
                data,
            )

        env = _parse_env(d.pop("env", UNSET))

        def _parse_memory(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        memory = _parse_memory(d.pop("memory", UNSET))

        def _parse_swap(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        swap = _parse_swap(d.pop("swap", UNSET))

        def _parse_disk(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        disk = _parse_disk(d.pop("disk", UNSET))

        def _parse_io_weight(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        io_weight = _parse_io_weight(d.pop("io_weight", UNSET))

        def _parse_cpu(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cpu = _parse_cpu(d.pop("cpu", UNSET))

        patch_api_admin_database_agent_hosts_database_agent_host_instances_database_instance_body = cls(
            name=name,
            locked=locked,
            image=image,
            env=env,
            memory=memory,
            swap=swap,
            disk=disk,
            io_weight=io_weight,
            cpu=cpu,
        )

        patch_api_admin_database_agent_hosts_database_agent_host_instances_database_instance_body.additional_properties = d
        return patch_api_admin_database_agent_hosts_database_agent_host_instances_database_instance_body

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
