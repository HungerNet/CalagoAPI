from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_api_admin_database_agent_templates_database_agent_template_body_docker_images_type_0 import (
        PatchApiAdminDatabaseAgentTemplatesDatabaseAgentTemplateBodyDockerImagesType0,
    )
    from ..models.patch_api_admin_database_agent_templates_database_agent_template_body_env_type_0 import (
        PatchApiAdminDatabaseAgentTemplatesDatabaseAgentTemplateBodyEnvType0,
    )
    from ..models.patch_api_admin_database_agent_templates_database_agent_template_body_volumes_type_0 import (
        PatchApiAdminDatabaseAgentTemplatesDatabaseAgentTemplateBodyVolumesType0,
    )


T = TypeVar("T", bound="PatchApiAdminDatabaseAgentTemplatesDatabaseAgentTemplateBody")


@_attrs_define
class PatchApiAdminDatabaseAgentTemplatesDatabaseAgentTemplateBody:
    """
    Attributes:
        name (None | str | Unset):
        description (None | str | Unset):
        deployment_enabled (bool | None | Unset):
        docker_images (None | PatchApiAdminDatabaseAgentTemplatesDatabaseAgentTemplateBodyDockerImagesType0 | Unset):
        env (None | PatchApiAdminDatabaseAgentTemplatesDatabaseAgentTemplateBodyEnvType0 | Unset):
        image_uid (int | None | Unset):
        image_gid (int | None | Unset):
        cmd (list[str] | None | Unset):
        volumes (None | PatchApiAdminDatabaseAgentTemplatesDatabaseAgentTemplateBodyVolumesType0 | Unset):
        socket_path (None | str | Unset):
        memory (int | None | Unset):
        swap (int | None | Unset):
        disk (int | None | Unset):
        io_weight (int | None | Unset):
        cpu (int | None | Unset):
    """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    deployment_enabled: bool | None | Unset = UNSET
    docker_images: None | PatchApiAdminDatabaseAgentTemplatesDatabaseAgentTemplateBodyDockerImagesType0 | Unset = UNSET
    env: None | PatchApiAdminDatabaseAgentTemplatesDatabaseAgentTemplateBodyEnvType0 | Unset = UNSET
    image_uid: int | None | Unset = UNSET
    image_gid: int | None | Unset = UNSET
    cmd: list[str] | None | Unset = UNSET
    volumes: None | PatchApiAdminDatabaseAgentTemplatesDatabaseAgentTemplateBodyVolumesType0 | Unset = UNSET
    socket_path: None | str | Unset = UNSET
    memory: int | None | Unset = UNSET
    swap: int | None | Unset = UNSET
    disk: int | None | Unset = UNSET
    io_weight: int | None | Unset = UNSET
    cpu: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.patch_api_admin_database_agent_templates_database_agent_template_body_docker_images_type_0 import (
            PatchApiAdminDatabaseAgentTemplatesDatabaseAgentTemplateBodyDockerImagesType0,  # noqa: PLC0415
        )
        from ..models.patch_api_admin_database_agent_templates_database_agent_template_body_env_type_0 import (
            PatchApiAdminDatabaseAgentTemplatesDatabaseAgentTemplateBodyEnvType0,  # noqa: PLC0415
        )
        from ..models.patch_api_admin_database_agent_templates_database_agent_template_body_volumes_type_0 import (
            PatchApiAdminDatabaseAgentTemplatesDatabaseAgentTemplateBodyVolumesType0,  # noqa: PLC0415
        )

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        deployment_enabled: bool | None | Unset
        if isinstance(self.deployment_enabled, Unset):
            deployment_enabled = UNSET
        else:
            deployment_enabled = self.deployment_enabled

        docker_images: dict[str, Any] | None | Unset
        if isinstance(self.docker_images, Unset):
            docker_images = UNSET
        elif isinstance(
            self.docker_images, PatchApiAdminDatabaseAgentTemplatesDatabaseAgentTemplateBodyDockerImagesType0
        ):
            docker_images = self.docker_images.to_dict()
        else:
            docker_images = self.docker_images

        env: dict[str, Any] | None | Unset
        if isinstance(self.env, Unset):
            env = UNSET
        elif isinstance(self.env, PatchApiAdminDatabaseAgentTemplatesDatabaseAgentTemplateBodyEnvType0):
            env = self.env.to_dict()
        else:
            env = self.env

        image_uid: int | None | Unset
        if isinstance(self.image_uid, Unset):
            image_uid = UNSET
        else:
            image_uid = self.image_uid

        image_gid: int | None | Unset
        if isinstance(self.image_gid, Unset):
            image_gid = UNSET
        else:
            image_gid = self.image_gid

        cmd: list[str] | None | Unset
        if isinstance(self.cmd, Unset):
            cmd = UNSET
        elif isinstance(self.cmd, list):
            cmd = self.cmd

        else:
            cmd = self.cmd

        volumes: dict[str, Any] | None | Unset
        if isinstance(self.volumes, Unset):
            volumes = UNSET
        elif isinstance(self.volumes, PatchApiAdminDatabaseAgentTemplatesDatabaseAgentTemplateBodyVolumesType0):
            volumes = self.volumes.to_dict()
        else:
            volumes = self.volumes

        socket_path: None | str | Unset
        if isinstance(self.socket_path, Unset):
            socket_path = UNSET
        else:
            socket_path = self.socket_path

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
        if description is not UNSET:
            field_dict["description"] = description
        if deployment_enabled is not UNSET:
            field_dict["deployment_enabled"] = deployment_enabled
        if docker_images is not UNSET:
            field_dict["docker_images"] = docker_images
        if env is not UNSET:
            field_dict["env"] = env
        if image_uid is not UNSET:
            field_dict["image_uid"] = image_uid
        if image_gid is not UNSET:
            field_dict["image_gid"] = image_gid
        if cmd is not UNSET:
            field_dict["cmd"] = cmd
        if volumes is not UNSET:
            field_dict["volumes"] = volumes
        if socket_path is not UNSET:
            field_dict["socket_path"] = socket_path
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
        from ..models.patch_api_admin_database_agent_templates_database_agent_template_body_docker_images_type_0 import (
            PatchApiAdminDatabaseAgentTemplatesDatabaseAgentTemplateBodyDockerImagesType0,  # noqa: PLC0415
        )
        from ..models.patch_api_admin_database_agent_templates_database_agent_template_body_env_type_0 import (
            PatchApiAdminDatabaseAgentTemplatesDatabaseAgentTemplateBodyEnvType0,  # noqa: PLC0415
        )
        from ..models.patch_api_admin_database_agent_templates_database_agent_template_body_volumes_type_0 import (
            PatchApiAdminDatabaseAgentTemplatesDatabaseAgentTemplateBodyVolumesType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_deployment_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        deployment_enabled = _parse_deployment_enabled(d.pop("deployment_enabled", UNSET))

        def _parse_docker_images(
            data: object,
        ) -> None | PatchApiAdminDatabaseAgentTemplatesDatabaseAgentTemplateBodyDockerImagesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                docker_images_type_0 = (
                    PatchApiAdminDatabaseAgentTemplatesDatabaseAgentTemplateBodyDockerImagesType0.from_dict(data)
                )

                return docker_images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | PatchApiAdminDatabaseAgentTemplatesDatabaseAgentTemplateBodyDockerImagesType0 | Unset, data
            )

        docker_images = _parse_docker_images(d.pop("docker_images", UNSET))

        def _parse_env(
            data: object,
        ) -> None | PatchApiAdminDatabaseAgentTemplatesDatabaseAgentTemplateBodyEnvType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                env_type_0 = PatchApiAdminDatabaseAgentTemplatesDatabaseAgentTemplateBodyEnvType0.from_dict(data)

                return env_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PatchApiAdminDatabaseAgentTemplatesDatabaseAgentTemplateBodyEnvType0 | Unset, data)

        env = _parse_env(d.pop("env", UNSET))

        def _parse_image_uid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        image_uid = _parse_image_uid(d.pop("image_uid", UNSET))

        def _parse_image_gid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        image_gid = _parse_image_gid(d.pop("image_gid", UNSET))

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

        def _parse_volumes(
            data: object,
        ) -> None | PatchApiAdminDatabaseAgentTemplatesDatabaseAgentTemplateBodyVolumesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                volumes_type_0 = PatchApiAdminDatabaseAgentTemplatesDatabaseAgentTemplateBodyVolumesType0.from_dict(
                    data
                )

                return volumes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PatchApiAdminDatabaseAgentTemplatesDatabaseAgentTemplateBodyVolumesType0 | Unset, data)

        volumes = _parse_volumes(d.pop("volumes", UNSET))

        def _parse_socket_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        socket_path = _parse_socket_path(d.pop("socket_path", UNSET))

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

        patch_api_admin_database_agent_templates_database_agent_template_body = cls(
            name=name,
            description=description,
            deployment_enabled=deployment_enabled,
            docker_images=docker_images,
            env=env,
            image_uid=image_uid,
            image_gid=image_gid,
            cmd=cmd,
            volumes=volumes,
            socket_path=socket_path,
            memory=memory,
            swap=swap,
            disk=disk,
            io_weight=io_weight,
            cpu=cpu,
        )

        patch_api_admin_database_agent_templates_database_agent_template_body.additional_properties = d
        return patch_api_admin_database_agent_templates_database_agent_template_body

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
