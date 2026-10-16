from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.database_agent_type import DatabaseAgentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.admin_database_agent_template import AdminDatabaseAgentTemplate
    from ..models.admin_server_server_database_instance_env import AdminServerServerDatabaseInstanceEnv
    from ..models.admin_server_server_database_instance_env_overrides_type_0 import (
        AdminServerServerDatabaseInstanceEnvOverridesType0,
    )
    from ..models.database_agent_host import DatabaseAgentHost


T = TypeVar("T", bound="AdminServerServerDatabaseInstance")


@_attrs_define
class AdminServerServerDatabaseInstance:
    """
    Attributes:
        uuid (UUID):
        database_agent_host (DatabaseAgentHost):
        update_available (bool):
        type_ (DatabaseAgentType):
        name (str):
        is_locked (bool):
        env (AdminServerServerDatabaseInstanceEnv):
        memory (int):
        swap (int):
        disk (int):
        cpu (int):
        created (datetime.datetime):
        database_agent_template (AdminDatabaseAgentTemplate | None | Unset):
        template_version (int | None | Unset):
        host (None | str | Unset):
        port (int | None | Unset):
        image (None | str | Unset):
        image_override (None | str | Unset):
        env_overrides (AdminServerServerDatabaseInstanceEnvOverridesType0 | None | Unset):
        io_weight (int | None | Unset):
        memory_override (int | None | Unset):
        swap_override (int | None | Unset):
        disk_override (int | None | Unset):
        io_weight_override (int | None | Unset):
        cpu_override (int | None | Unset):
    """

    uuid: UUID
    database_agent_host: DatabaseAgentHost
    update_available: bool
    type_: DatabaseAgentType
    name: str
    is_locked: bool
    env: AdminServerServerDatabaseInstanceEnv
    memory: int
    swap: int
    disk: int
    cpu: int
    created: datetime.datetime
    database_agent_template: AdminDatabaseAgentTemplate | None | Unset = UNSET
    template_version: int | None | Unset = UNSET
    host: None | str | Unset = UNSET
    port: int | None | Unset = UNSET
    image: None | str | Unset = UNSET
    image_override: None | str | Unset = UNSET
    env_overrides: AdminServerServerDatabaseInstanceEnvOverridesType0 | None | Unset = UNSET
    io_weight: int | None | Unset = UNSET
    memory_override: int | None | Unset = UNSET
    swap_override: int | None | Unset = UNSET
    disk_override: int | None | Unset = UNSET
    io_weight_override: int | None | Unset = UNSET
    cpu_override: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.admin_database_agent_template import AdminDatabaseAgentTemplate  # noqa: PLC0415
        from ..models.admin_server_server_database_instance_env_overrides_type_0 import (
            AdminServerServerDatabaseInstanceEnvOverridesType0,  # noqa: PLC0415
        )

        uuid = str(self.uuid)

        database_agent_host = self.database_agent_host.to_dict()

        update_available = self.update_available

        type_ = self.type_.value

        name = self.name

        is_locked = self.is_locked

        env = self.env.to_dict()

        memory = self.memory

        swap = self.swap

        disk = self.disk

        cpu = self.cpu

        created = self.created.isoformat()

        database_agent_template: dict[str, Any] | None | Unset
        if isinstance(self.database_agent_template, Unset):
            database_agent_template = UNSET
        elif isinstance(self.database_agent_template, AdminDatabaseAgentTemplate):
            database_agent_template = self.database_agent_template.to_dict()
        else:
            database_agent_template = self.database_agent_template

        template_version: int | None | Unset
        if isinstance(self.template_version, Unset):
            template_version = UNSET
        else:
            template_version = self.template_version

        host: None | str | Unset
        if isinstance(self.host, Unset):
            host = UNSET
        else:
            host = self.host

        port: int | None | Unset
        if isinstance(self.port, Unset):
            port = UNSET
        else:
            port = self.port

        image: None | str | Unset
        if isinstance(self.image, Unset):
            image = UNSET
        else:
            image = self.image

        image_override: None | str | Unset
        if isinstance(self.image_override, Unset):
            image_override = UNSET
        else:
            image_override = self.image_override

        env_overrides: dict[str, Any] | None | Unset
        if isinstance(self.env_overrides, Unset):
            env_overrides = UNSET
        elif isinstance(self.env_overrides, AdminServerServerDatabaseInstanceEnvOverridesType0):
            env_overrides = self.env_overrides.to_dict()
        else:
            env_overrides = self.env_overrides

        io_weight: int | None | Unset
        if isinstance(self.io_weight, Unset):
            io_weight = UNSET
        else:
            io_weight = self.io_weight

        memory_override: int | None | Unset
        if isinstance(self.memory_override, Unset):
            memory_override = UNSET
        else:
            memory_override = self.memory_override

        swap_override: int | None | Unset
        if isinstance(self.swap_override, Unset):
            swap_override = UNSET
        else:
            swap_override = self.swap_override

        disk_override: int | None | Unset
        if isinstance(self.disk_override, Unset):
            disk_override = UNSET
        else:
            disk_override = self.disk_override

        io_weight_override: int | None | Unset
        if isinstance(self.io_weight_override, Unset):
            io_weight_override = UNSET
        else:
            io_weight_override = self.io_weight_override

        cpu_override: int | None | Unset
        if isinstance(self.cpu_override, Unset):
            cpu_override = UNSET
        else:
            cpu_override = self.cpu_override

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "database_agent_host": database_agent_host,
                "update_available": update_available,
                "type": type_,
                "name": name,
                "is_locked": is_locked,
                "env": env,
                "memory": memory,
                "swap": swap,
                "disk": disk,
                "cpu": cpu,
                "created": created,
            }
        )
        if database_agent_template is not UNSET:
            field_dict["database_agent_template"] = database_agent_template
        if template_version is not UNSET:
            field_dict["template_version"] = template_version
        if host is not UNSET:
            field_dict["host"] = host
        if port is not UNSET:
            field_dict["port"] = port
        if image is not UNSET:
            field_dict["image"] = image
        if image_override is not UNSET:
            field_dict["image_override"] = image_override
        if env_overrides is not UNSET:
            field_dict["env_overrides"] = env_overrides
        if io_weight is not UNSET:
            field_dict["io_weight"] = io_weight
        if memory_override is not UNSET:
            field_dict["memory_override"] = memory_override
        if swap_override is not UNSET:
            field_dict["swap_override"] = swap_override
        if disk_override is not UNSET:
            field_dict["disk_override"] = disk_override
        if io_weight_override is not UNSET:
            field_dict["io_weight_override"] = io_weight_override
        if cpu_override is not UNSET:
            field_dict["cpu_override"] = cpu_override

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.admin_database_agent_template import AdminDatabaseAgentTemplate  # noqa: PLC0415
        from ..models.admin_server_server_database_instance_env import AdminServerServerDatabaseInstanceEnv  # noqa: PLC0415
        from ..models.admin_server_server_database_instance_env_overrides_type_0 import (
            AdminServerServerDatabaseInstanceEnvOverridesType0,  # noqa: PLC0415
        )
        from ..models.database_agent_host import DatabaseAgentHost  # noqa: PLC0415

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        database_agent_host = DatabaseAgentHost.from_dict(d.pop("database_agent_host"))

        update_available = d.pop("update_available")

        type_ = DatabaseAgentType(d.pop("type"))

        name = d.pop("name")

        is_locked = d.pop("is_locked")

        env = AdminServerServerDatabaseInstanceEnv.from_dict(d.pop("env"))

        memory = d.pop("memory")

        swap = d.pop("swap")

        disk = d.pop("disk")

        cpu = d.pop("cpu")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        def _parse_database_agent_template(data: object) -> AdminDatabaseAgentTemplate | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                database_agent_template_type_1 = AdminDatabaseAgentTemplate.from_dict(data)

                return database_agent_template_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AdminDatabaseAgentTemplate | None | Unset, data)

        database_agent_template = _parse_database_agent_template(d.pop("database_agent_template", UNSET))

        def _parse_template_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        template_version = _parse_template_version(d.pop("template_version", UNSET))

        def _parse_host(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        host = _parse_host(d.pop("host", UNSET))

        def _parse_port(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        port = _parse_port(d.pop("port", UNSET))

        def _parse_image(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image = _parse_image(d.pop("image", UNSET))

        def _parse_image_override(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_override = _parse_image_override(d.pop("image_override", UNSET))

        def _parse_env_overrides(data: object) -> AdminServerServerDatabaseInstanceEnvOverridesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                env_overrides_type_0 = AdminServerServerDatabaseInstanceEnvOverridesType0.from_dict(data)

                return env_overrides_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AdminServerServerDatabaseInstanceEnvOverridesType0 | None | Unset, data)

        env_overrides = _parse_env_overrides(d.pop("env_overrides", UNSET))

        def _parse_io_weight(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        io_weight = _parse_io_weight(d.pop("io_weight", UNSET))

        def _parse_memory_override(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        memory_override = _parse_memory_override(d.pop("memory_override", UNSET))

        def _parse_swap_override(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        swap_override = _parse_swap_override(d.pop("swap_override", UNSET))

        def _parse_disk_override(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        disk_override = _parse_disk_override(d.pop("disk_override", UNSET))

        def _parse_io_weight_override(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        io_weight_override = _parse_io_weight_override(d.pop("io_weight_override", UNSET))

        def _parse_cpu_override(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cpu_override = _parse_cpu_override(d.pop("cpu_override", UNSET))

        admin_server_server_database_instance = cls(
            uuid=uuid,
            database_agent_host=database_agent_host,
            update_available=update_available,
            type_=type_,
            name=name,
            is_locked=is_locked,
            env=env,
            memory=memory,
            swap=swap,
            disk=disk,
            cpu=cpu,
            created=created,
            database_agent_template=database_agent_template,
            template_version=template_version,
            host=host,
            port=port,
            image=image,
            image_override=image_override,
            env_overrides=env_overrides,
            io_weight=io_weight,
            memory_override=memory_override,
            swap_override=swap_override,
            disk_override=disk_override,
            io_weight_override=io_weight_override,
            cpu_override=cpu_override,
        )

        admin_server_server_database_instance.additional_properties = d
        return admin_server_server_database_instance

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
