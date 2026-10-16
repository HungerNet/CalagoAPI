from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_admin_nests_nest_eggs_body_config_files_item import (
        PostApiAdminNestsNestEggsBodyConfigFilesItem,
    )
    from ..models.post_api_admin_nests_nest_eggs_body_config_script import PostApiAdminNestsNestEggsBodyConfigScript
    from ..models.post_api_admin_nests_nest_eggs_body_config_startup import PostApiAdminNestsNestEggsBodyConfigStartup
    from ..models.post_api_admin_nests_nest_eggs_body_config_stop import PostApiAdminNestsNestEggsBodyConfigStop
    from ..models.post_api_admin_nests_nest_eggs_body_docker_images import PostApiAdminNestsNestEggsBodyDockerImages
    from ..models.post_api_admin_nests_nest_eggs_body_startup_commands import (
        PostApiAdminNestsNestEggsBodyStartupCommands,
    )


T = TypeVar("T", bound="PostApiAdminNestsNestEggsBody")


@_attrs_define
class PostApiAdminNestsNestEggsBody:
    """
    Attributes:
        author (str):
        name (str):
        config_files (list[PostApiAdminNestsNestEggsBodyConfigFilesItem]):
        config_startup (PostApiAdminNestsNestEggsBodyConfigStartup):
        config_stop (PostApiAdminNestsNestEggsBodyConfigStop):
        config_script (PostApiAdminNestsNestEggsBodyConfigScript):
        startup_commands (PostApiAdminNestsNestEggsBodyStartupCommands):
        force_outgoing_ip (bool):
        separate_port (bool):
        features (list[str]):
        docker_images (PostApiAdminNestsNestEggsBodyDockerImages):
        file_denylist (list[str]):
        egg_repository_egg_uuid (None | Unset | UUID):
        description (None | str | Unset):
    """

    author: str
    name: str
    config_files: list[PostApiAdminNestsNestEggsBodyConfigFilesItem]
    config_startup: PostApiAdminNestsNestEggsBodyConfigStartup
    config_stop: PostApiAdminNestsNestEggsBodyConfigStop
    config_script: PostApiAdminNestsNestEggsBodyConfigScript
    startup_commands: PostApiAdminNestsNestEggsBodyStartupCommands
    force_outgoing_ip: bool
    separate_port: bool
    features: list[str]
    docker_images: PostApiAdminNestsNestEggsBodyDockerImages
    file_denylist: list[str]
    egg_repository_egg_uuid: None | Unset | UUID = UNSET
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author = self.author

        name = self.name

        config_files = []
        for config_files_item_data in self.config_files:
            config_files_item = config_files_item_data.to_dict()
            config_files.append(config_files_item)

        config_startup = self.config_startup.to_dict()

        config_stop = self.config_stop.to_dict()

        config_script = self.config_script.to_dict()

        startup_commands = self.startup_commands.to_dict()

        force_outgoing_ip = self.force_outgoing_ip

        separate_port = self.separate_port

        features = self.features

        docker_images = self.docker_images.to_dict()

        file_denylist = self.file_denylist

        egg_repository_egg_uuid: None | str | Unset
        if isinstance(self.egg_repository_egg_uuid, Unset):
            egg_repository_egg_uuid = UNSET
        elif isinstance(self.egg_repository_egg_uuid, UUID):
            egg_repository_egg_uuid = str(self.egg_repository_egg_uuid)
        else:
            egg_repository_egg_uuid = self.egg_repository_egg_uuid

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "author": author,
                "name": name,
                "config_files": config_files,
                "config_startup": config_startup,
                "config_stop": config_stop,
                "config_script": config_script,
                "startup_commands": startup_commands,
                "force_outgoing_ip": force_outgoing_ip,
                "separate_port": separate_port,
                "features": features,
                "docker_images": docker_images,
                "file_denylist": file_denylist,
            }
        )
        if egg_repository_egg_uuid is not UNSET:
            field_dict["egg_repository_egg_uuid"] = egg_repository_egg_uuid
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_admin_nests_nest_eggs_body_config_files_item import (
            PostApiAdminNestsNestEggsBodyConfigFilesItem,  # noqa: PLC0415
        )
        from ..models.post_api_admin_nests_nest_eggs_body_config_script import PostApiAdminNestsNestEggsBodyConfigScript  # noqa: PLC0415
        from ..models.post_api_admin_nests_nest_eggs_body_config_startup import (
            PostApiAdminNestsNestEggsBodyConfigStartup,  # noqa: PLC0415
        )
        from ..models.post_api_admin_nests_nest_eggs_body_config_stop import PostApiAdminNestsNestEggsBodyConfigStop  # noqa: PLC0415
        from ..models.post_api_admin_nests_nest_eggs_body_docker_images import PostApiAdminNestsNestEggsBodyDockerImages  # noqa: PLC0415
        from ..models.post_api_admin_nests_nest_eggs_body_startup_commands import (
            PostApiAdminNestsNestEggsBodyStartupCommands,  # noqa: PLC0415
        )

        d = dict(src_dict)
        author = d.pop("author")

        name = d.pop("name")

        config_files = []
        _config_files = d.pop("config_files")
        for config_files_item_data in _config_files:
            config_files_item = PostApiAdminNestsNestEggsBodyConfigFilesItem.from_dict(config_files_item_data)

            config_files.append(config_files_item)

        config_startup = PostApiAdminNestsNestEggsBodyConfigStartup.from_dict(d.pop("config_startup"))

        config_stop = PostApiAdminNestsNestEggsBodyConfigStop.from_dict(d.pop("config_stop"))

        config_script = PostApiAdminNestsNestEggsBodyConfigScript.from_dict(d.pop("config_script"))

        startup_commands = PostApiAdminNestsNestEggsBodyStartupCommands.from_dict(d.pop("startup_commands"))

        force_outgoing_ip = d.pop("force_outgoing_ip")

        separate_port = d.pop("separate_port")

        features = cast(list[str], d.pop("features"))

        docker_images = PostApiAdminNestsNestEggsBodyDockerImages.from_dict(d.pop("docker_images"))

        file_denylist = cast(list[str], d.pop("file_denylist"))

        def _parse_egg_repository_egg_uuid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                egg_repository_egg_uuid_type_0 = UUID(data)

                return egg_repository_egg_uuid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        egg_repository_egg_uuid = _parse_egg_repository_egg_uuid(d.pop("egg_repository_egg_uuid", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        post_api_admin_nests_nest_eggs_body = cls(
            author=author,
            name=name,
            config_files=config_files,
            config_startup=config_startup,
            config_stop=config_stop,
            config_script=config_script,
            startup_commands=startup_commands,
            force_outgoing_ip=force_outgoing_ip,
            separate_port=separate_port,
            features=features,
            docker_images=docker_images,
            file_denylist=file_denylist,
            egg_repository_egg_uuid=egg_repository_egg_uuid,
            description=description,
        )

        post_api_admin_nests_nest_eggs_body.additional_properties = d
        return post_api_admin_nests_nest_eggs_body

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
