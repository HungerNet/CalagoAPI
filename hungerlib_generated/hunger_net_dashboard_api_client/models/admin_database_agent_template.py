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
    from ..models.admin_database_agent_template_docker_images import AdminDatabaseAgentTemplateDockerImages
    from ..models.admin_database_agent_template_env import AdminDatabaseAgentTemplateEnv
    from ..models.admin_database_agent_template_volumes import AdminDatabaseAgentTemplateVolumes


T = TypeVar("T", bound="AdminDatabaseAgentTemplate")


@_attrs_define
class AdminDatabaseAgentTemplate:
    """
    Attributes:
        uuid (UUID):
        name (str):
        type_ (DatabaseAgentType):
        deployment_enabled (bool):
        docker_images (AdminDatabaseAgentTemplateDockerImages):
        env (AdminDatabaseAgentTemplateEnv):
        image_uid (int):
        image_gid (int):
        volumes (AdminDatabaseAgentTemplateVolumes):
        socket_path (str):
        memory (int):
        swap (int):
        disk (int):
        cpu (int):
        version (int):
        created (datetime.datetime):
        description (None | str | Unset):
        cmd (list[str] | None | Unset):
        io_weight (int | None | Unset):
    """

    uuid: UUID
    name: str
    type_: DatabaseAgentType
    deployment_enabled: bool
    docker_images: AdminDatabaseAgentTemplateDockerImages
    env: AdminDatabaseAgentTemplateEnv
    image_uid: int
    image_gid: int
    volumes: AdminDatabaseAgentTemplateVolumes
    socket_path: str
    memory: int
    swap: int
    disk: int
    cpu: int
    version: int
    created: datetime.datetime
    description: None | str | Unset = UNSET
    cmd: list[str] | None | Unset = UNSET
    io_weight: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        type_ = self.type_.value

        deployment_enabled = self.deployment_enabled

        docker_images = self.docker_images.to_dict()

        env = self.env.to_dict()

        image_uid = self.image_uid

        image_gid = self.image_gid

        volumes = self.volumes.to_dict()

        socket_path = self.socket_path

        memory = self.memory

        swap = self.swap

        disk = self.disk

        cpu = self.cpu

        version = self.version

        created = self.created.isoformat()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        cmd: list[str] | None | Unset
        if isinstance(self.cmd, Unset):
            cmd = UNSET
        elif isinstance(self.cmd, list):
            cmd = self.cmd

        else:
            cmd = self.cmd

        io_weight: int | None | Unset
        if isinstance(self.io_weight, Unset):
            io_weight = UNSET
        else:
            io_weight = self.io_weight

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "type": type_,
                "deployment_enabled": deployment_enabled,
                "docker_images": docker_images,
                "env": env,
                "image_uid": image_uid,
                "image_gid": image_gid,
                "volumes": volumes,
                "socket_path": socket_path,
                "memory": memory,
                "swap": swap,
                "disk": disk,
                "cpu": cpu,
                "version": version,
                "created": created,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if cmd is not UNSET:
            field_dict["cmd"] = cmd
        if io_weight is not UNSET:
            field_dict["io_weight"] = io_weight

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.admin_database_agent_template_docker_images import AdminDatabaseAgentTemplateDockerImages  # noqa: PLC0415
        from ..models.admin_database_agent_template_env import AdminDatabaseAgentTemplateEnv  # noqa: PLC0415
        from ..models.admin_database_agent_template_volumes import AdminDatabaseAgentTemplateVolumes  # noqa: PLC0415

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        type_ = DatabaseAgentType(d.pop("type"))

        deployment_enabled = d.pop("deployment_enabled")

        docker_images = AdminDatabaseAgentTemplateDockerImages.from_dict(d.pop("docker_images"))

        env = AdminDatabaseAgentTemplateEnv.from_dict(d.pop("env"))

        image_uid = d.pop("image_uid")

        image_gid = d.pop("image_gid")

        volumes = AdminDatabaseAgentTemplateVolumes.from_dict(d.pop("volumes"))

        socket_path = d.pop("socket_path")

        memory = d.pop("memory")

        swap = d.pop("swap")

        disk = d.pop("disk")

        cpu = d.pop("cpu")

        version = d.pop("version")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_cmd(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cmd_type_0 = cast(list[str], data)

                return cmd_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        cmd = _parse_cmd(d.pop("cmd", UNSET))

        def _parse_io_weight(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        io_weight = _parse_io_weight(d.pop("io_weight", UNSET))

        admin_database_agent_template = cls(
            uuid=uuid,
            name=name,
            type_=type_,
            deployment_enabled=deployment_enabled,
            docker_images=docker_images,
            env=env,
            image_uid=image_uid,
            image_gid=image_gid,
            volumes=volumes,
            socket_path=socket_path,
            memory=memory,
            swap=swap,
            disk=disk,
            cpu=cpu,
            version=version,
            created=created,
            description=description,
            cmd=cmd,
            io_weight=io_weight,
        )

        admin_database_agent_template.additional_properties = d
        return admin_database_agent_template

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
