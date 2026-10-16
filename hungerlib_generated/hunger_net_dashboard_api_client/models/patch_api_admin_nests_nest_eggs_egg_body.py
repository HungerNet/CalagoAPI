from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_api_admin_nests_nest_eggs_egg_body_config_files_type_0_item import (
        PatchApiAdminNestsNestEggsEggBodyConfigFilesType0Item,
    )
    from ..models.patch_api_admin_nests_nest_eggs_egg_body_config_script_type_1 import (
        PatchApiAdminNestsNestEggsEggBodyConfigScriptType1,
    )
    from ..models.patch_api_admin_nests_nest_eggs_egg_body_config_startup_type_1 import (
        PatchApiAdminNestsNestEggsEggBodyConfigStartupType1,
    )
    from ..models.patch_api_admin_nests_nest_eggs_egg_body_config_stop_type_1 import (
        PatchApiAdminNestsNestEggsEggBodyConfigStopType1,
    )
    from ..models.patch_api_admin_nests_nest_eggs_egg_body_docker_images_type_0 import (
        PatchApiAdminNestsNestEggsEggBodyDockerImagesType0,
    )
    from ..models.patch_api_admin_nests_nest_eggs_egg_body_startup_commands_type_0 import (
        PatchApiAdminNestsNestEggsEggBodyStartupCommandsType0,
    )


T = TypeVar("T", bound="PatchApiAdminNestsNestEggsEggBody")


@_attrs_define
class PatchApiAdminNestsNestEggsEggBody:
    """
    Attributes:
        egg_repository_egg_uuid (None | Unset | UUID):
        author (None | str | Unset):
        name (None | str | Unset):
        description (None | str | Unset):
        config_files (list[PatchApiAdminNestsNestEggsEggBodyConfigFilesType0Item] | None | Unset):
        config_startup (None | PatchApiAdminNestsNestEggsEggBodyConfigStartupType1 | Unset):
        config_stop (None | PatchApiAdminNestsNestEggsEggBodyConfigStopType1 | Unset):
        config_script (None | PatchApiAdminNestsNestEggsEggBodyConfigScriptType1 | Unset):
        startup_commands (None | PatchApiAdminNestsNestEggsEggBodyStartupCommandsType0 | Unset):
        force_outgoing_ip (bool | None | Unset):
        separate_port (bool | None | Unset):
        features (list[str] | None | Unset):
        docker_images (None | PatchApiAdminNestsNestEggsEggBodyDockerImagesType0 | Unset):
        file_denylist (list[str] | None | Unset):
    """

    egg_repository_egg_uuid: None | Unset | UUID = UNSET
    author: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    config_files: list[PatchApiAdminNestsNestEggsEggBodyConfigFilesType0Item] | None | Unset = UNSET
    config_startup: None | PatchApiAdminNestsNestEggsEggBodyConfigStartupType1 | Unset = UNSET
    config_stop: None | PatchApiAdminNestsNestEggsEggBodyConfigStopType1 | Unset = UNSET
    config_script: None | PatchApiAdminNestsNestEggsEggBodyConfigScriptType1 | Unset = UNSET
    startup_commands: None | PatchApiAdminNestsNestEggsEggBodyStartupCommandsType0 | Unset = UNSET
    force_outgoing_ip: bool | None | Unset = UNSET
    separate_port: bool | None | Unset = UNSET
    features: list[str] | None | Unset = UNSET
    docker_images: None | PatchApiAdminNestsNestEggsEggBodyDockerImagesType0 | Unset = UNSET
    file_denylist: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.patch_api_admin_nests_nest_eggs_egg_body_config_script_type_1 import (
            PatchApiAdminNestsNestEggsEggBodyConfigScriptType1,  # noqa: PLC0415
        )
        from ..models.patch_api_admin_nests_nest_eggs_egg_body_config_startup_type_1 import (
            PatchApiAdminNestsNestEggsEggBodyConfigStartupType1,  # noqa: PLC0415
        )
        from ..models.patch_api_admin_nests_nest_eggs_egg_body_config_stop_type_1 import (
            PatchApiAdminNestsNestEggsEggBodyConfigStopType1,  # noqa: PLC0415
        )
        from ..models.patch_api_admin_nests_nest_eggs_egg_body_docker_images_type_0 import (
            PatchApiAdminNestsNestEggsEggBodyDockerImagesType0,  # noqa: PLC0415
        )
        from ..models.patch_api_admin_nests_nest_eggs_egg_body_startup_commands_type_0 import (
            PatchApiAdminNestsNestEggsEggBodyStartupCommandsType0,  # noqa: PLC0415
        )

        egg_repository_egg_uuid: None | str | Unset
        if isinstance(self.egg_repository_egg_uuid, Unset):
            egg_repository_egg_uuid = UNSET
        elif isinstance(self.egg_repository_egg_uuid, UUID):
            egg_repository_egg_uuid = str(self.egg_repository_egg_uuid)
        else:
            egg_repository_egg_uuid = self.egg_repository_egg_uuid

        author: None | str | Unset
        if isinstance(self.author, Unset):
            author = UNSET
        else:
            author = self.author

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

        config_files: list[dict[str, Any]] | None | Unset
        if isinstance(self.config_files, Unset):
            config_files = UNSET
        elif isinstance(self.config_files, list):
            config_files = []
            for config_files_type_0_item_data in self.config_files:
                config_files_type_0_item = config_files_type_0_item_data.to_dict()
                config_files.append(config_files_type_0_item)

        else:
            config_files = self.config_files

        config_startup: dict[str, Any] | None | Unset
        if isinstance(self.config_startup, Unset):
            config_startup = UNSET
        elif isinstance(self.config_startup, PatchApiAdminNestsNestEggsEggBodyConfigStartupType1):
            config_startup = self.config_startup.to_dict()
        else:
            config_startup = self.config_startup

        config_stop: dict[str, Any] | None | Unset
        if isinstance(self.config_stop, Unset):
            config_stop = UNSET
        elif isinstance(self.config_stop, PatchApiAdminNestsNestEggsEggBodyConfigStopType1):
            config_stop = self.config_stop.to_dict()
        else:
            config_stop = self.config_stop

        config_script: dict[str, Any] | None | Unset
        if isinstance(self.config_script, Unset):
            config_script = UNSET
        elif isinstance(self.config_script, PatchApiAdminNestsNestEggsEggBodyConfigScriptType1):
            config_script = self.config_script.to_dict()
        else:
            config_script = self.config_script

        startup_commands: dict[str, Any] | None | Unset
        if isinstance(self.startup_commands, Unset):
            startup_commands = UNSET
        elif isinstance(self.startup_commands, PatchApiAdminNestsNestEggsEggBodyStartupCommandsType0):
            startup_commands = self.startup_commands.to_dict()
        else:
            startup_commands = self.startup_commands

        force_outgoing_ip: bool | None | Unset
        if isinstance(self.force_outgoing_ip, Unset):
            force_outgoing_ip = UNSET
        else:
            force_outgoing_ip = self.force_outgoing_ip

        separate_port: bool | None | Unset
        if isinstance(self.separate_port, Unset):
            separate_port = UNSET
        else:
            separate_port = self.separate_port

        features: list[str] | None | Unset
        if isinstance(self.features, Unset):
            features = UNSET
        elif isinstance(self.features, list):
            features = self.features

        else:
            features = self.features

        docker_images: dict[str, Any] | None | Unset
        if isinstance(self.docker_images, Unset):
            docker_images = UNSET
        elif isinstance(self.docker_images, PatchApiAdminNestsNestEggsEggBodyDockerImagesType0):
            docker_images = self.docker_images.to_dict()
        else:
            docker_images = self.docker_images

        file_denylist: list[str] | None | Unset
        if isinstance(self.file_denylist, Unset):
            file_denylist = UNSET
        elif isinstance(self.file_denylist, list):
            file_denylist = self.file_denylist

        else:
            file_denylist = self.file_denylist

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if egg_repository_egg_uuid is not UNSET:
            field_dict["egg_repository_egg_uuid"] = egg_repository_egg_uuid
        if author is not UNSET:
            field_dict["author"] = author
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if config_files is not UNSET:
            field_dict["config_files"] = config_files
        if config_startup is not UNSET:
            field_dict["config_startup"] = config_startup
        if config_stop is not UNSET:
            field_dict["config_stop"] = config_stop
        if config_script is not UNSET:
            field_dict["config_script"] = config_script
        if startup_commands is not UNSET:
            field_dict["startup_commands"] = startup_commands
        if force_outgoing_ip is not UNSET:
            field_dict["force_outgoing_ip"] = force_outgoing_ip
        if separate_port is not UNSET:
            field_dict["separate_port"] = separate_port
        if features is not UNSET:
            field_dict["features"] = features
        if docker_images is not UNSET:
            field_dict["docker_images"] = docker_images
        if file_denylist is not UNSET:
            field_dict["file_denylist"] = file_denylist

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_api_admin_nests_nest_eggs_egg_body_config_files_type_0_item import (
            PatchApiAdminNestsNestEggsEggBodyConfigFilesType0Item,  # noqa: PLC0415
        )
        from ..models.patch_api_admin_nests_nest_eggs_egg_body_config_script_type_1 import (
            PatchApiAdminNestsNestEggsEggBodyConfigScriptType1,  # noqa: PLC0415
        )
        from ..models.patch_api_admin_nests_nest_eggs_egg_body_config_startup_type_1 import (
            PatchApiAdminNestsNestEggsEggBodyConfigStartupType1,  # noqa: PLC0415
        )
        from ..models.patch_api_admin_nests_nest_eggs_egg_body_config_stop_type_1 import (
            PatchApiAdminNestsNestEggsEggBodyConfigStopType1,  # noqa: PLC0415
        )
        from ..models.patch_api_admin_nests_nest_eggs_egg_body_docker_images_type_0 import (
            PatchApiAdminNestsNestEggsEggBodyDockerImagesType0,  # noqa: PLC0415
        )
        from ..models.patch_api_admin_nests_nest_eggs_egg_body_startup_commands_type_0 import (
            PatchApiAdminNestsNestEggsEggBodyStartupCommandsType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

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

        def _parse_author(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        author = _parse_author(d.pop("author", UNSET))

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

        def _parse_config_files(
            data: object,
        ) -> list[PatchApiAdminNestsNestEggsEggBodyConfigFilesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                config_files_type_0 = []
                _config_files_type_0 = data
                for config_files_type_0_item_data in _config_files_type_0:
                    config_files_type_0_item = PatchApiAdminNestsNestEggsEggBodyConfigFilesType0Item.from_dict(
                        config_files_type_0_item_data
                    )

                    config_files_type_0.append(config_files_type_0_item)

                return config_files_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PatchApiAdminNestsNestEggsEggBodyConfigFilesType0Item] | None | Unset, data)

        config_files = _parse_config_files(d.pop("config_files", UNSET))

        def _parse_config_startup(data: object) -> None | PatchApiAdminNestsNestEggsEggBodyConfigStartupType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_startup_type_1 = PatchApiAdminNestsNestEggsEggBodyConfigStartupType1.from_dict(data)

                return config_startup_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PatchApiAdminNestsNestEggsEggBodyConfigStartupType1 | Unset, data)

        config_startup = _parse_config_startup(d.pop("config_startup", UNSET))

        def _parse_config_stop(data: object) -> None | PatchApiAdminNestsNestEggsEggBodyConfigStopType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_stop_type_1 = PatchApiAdminNestsNestEggsEggBodyConfigStopType1.from_dict(data)

                return config_stop_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PatchApiAdminNestsNestEggsEggBodyConfigStopType1 | Unset, data)

        config_stop = _parse_config_stop(d.pop("config_stop", UNSET))

        def _parse_config_script(data: object) -> None | PatchApiAdminNestsNestEggsEggBodyConfigScriptType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_script_type_1 = PatchApiAdminNestsNestEggsEggBodyConfigScriptType1.from_dict(data)

                return config_script_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PatchApiAdminNestsNestEggsEggBodyConfigScriptType1 | Unset, data)

        config_script = _parse_config_script(d.pop("config_script", UNSET))

        def _parse_startup_commands(
            data: object,
        ) -> None | PatchApiAdminNestsNestEggsEggBodyStartupCommandsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                startup_commands_type_0 = PatchApiAdminNestsNestEggsEggBodyStartupCommandsType0.from_dict(data)

                return startup_commands_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PatchApiAdminNestsNestEggsEggBodyStartupCommandsType0 | Unset, data)

        startup_commands = _parse_startup_commands(d.pop("startup_commands", UNSET))

        def _parse_force_outgoing_ip(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        force_outgoing_ip = _parse_force_outgoing_ip(d.pop("force_outgoing_ip", UNSET))

        def _parse_separate_port(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        separate_port = _parse_separate_port(d.pop("separate_port", UNSET))

        def _parse_features(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                features_type_0 = cast(list[str], data)

                return features_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        features = _parse_features(d.pop("features", UNSET))

        def _parse_docker_images(data: object) -> None | PatchApiAdminNestsNestEggsEggBodyDockerImagesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                docker_images_type_0 = PatchApiAdminNestsNestEggsEggBodyDockerImagesType0.from_dict(data)

                return docker_images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PatchApiAdminNestsNestEggsEggBodyDockerImagesType0 | Unset, data)

        docker_images = _parse_docker_images(d.pop("docker_images", UNSET))

        def _parse_file_denylist(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                file_denylist_type_0 = cast(list[str], data)

                return file_denylist_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        file_denylist = _parse_file_denylist(d.pop("file_denylist", UNSET))

        patch_api_admin_nests_nest_eggs_egg_body = cls(
            egg_repository_egg_uuid=egg_repository_egg_uuid,
            author=author,
            name=name,
            description=description,
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
        )

        patch_api_admin_nests_nest_eggs_egg_body.additional_properties = d
        return patch_api_admin_nests_nest_eggs_egg_body

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
