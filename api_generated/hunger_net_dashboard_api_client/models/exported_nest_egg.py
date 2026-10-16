from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.exported_nest_egg_config import ExportedNestEggConfig
    from ..models.exported_nest_egg_docker_images import ExportedNestEggDockerImages
    from ..models.exported_nest_egg_scripts import ExportedNestEggScripts
    from ..models.exported_nest_egg_startup_commands import ExportedNestEggStartupCommands
    from ..models.exported_nest_egg_variables_item import ExportedNestEggVariablesItem


T = TypeVar("T", bound="ExportedNestEgg")


@_attrs_define
class ExportedNestEgg:
    """
    Attributes:
        name (str):
        author (str):
        config (ExportedNestEggConfig):
        scripts (ExportedNestEggScripts):
        startup_commands (ExportedNestEggStartupCommands):
        docker_images (ExportedNestEggDockerImages):
        variables (list[ExportedNestEggVariablesItem]):
        uuid (UUID | Unset):
        description (None | str | Unset):
        force_outgoing_ip (bool | Unset):
        separate_port (bool | Unset):
        features (list[str] | Unset):
        file_denylist (list[str] | Unset):
    """

    name: str
    author: str
    config: ExportedNestEggConfig
    scripts: ExportedNestEggScripts
    startup_commands: ExportedNestEggStartupCommands
    docker_images: ExportedNestEggDockerImages
    variables: list[ExportedNestEggVariablesItem]
    uuid: UUID | Unset = UNSET
    description: None | str | Unset = UNSET
    force_outgoing_ip: bool | Unset = UNSET
    separate_port: bool | Unset = UNSET
    features: list[str] | Unset = UNSET
    file_denylist: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        author = self.author

        config = self.config.to_dict()

        scripts = self.scripts.to_dict()

        startup_commands = self.startup_commands.to_dict()

        docker_images = self.docker_images.to_dict()

        variables = []
        for variables_item_data in self.variables:
            variables_item = variables_item_data.to_dict()
            variables.append(variables_item)

        uuid: str | Unset = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        force_outgoing_ip = self.force_outgoing_ip

        separate_port = self.separate_port

        features: list[str] | Unset = UNSET
        if not isinstance(self.features, Unset):
            features = self.features

        file_denylist: list[str] | Unset = UNSET
        if not isinstance(self.file_denylist, Unset):
            file_denylist = self.file_denylist

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "author": author,
                "config": config,
                "scripts": scripts,
                "startup_commands": startup_commands,
                "docker_images": docker_images,
                "variables": variables,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if description is not UNSET:
            field_dict["description"] = description
        if force_outgoing_ip is not UNSET:
            field_dict["force_outgoing_ip"] = force_outgoing_ip
        if separate_port is not UNSET:
            field_dict["separate_port"] = separate_port
        if features is not UNSET:
            field_dict["features"] = features
        if file_denylist is not UNSET:
            field_dict["file_denylist"] = file_denylist

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exported_nest_egg_config import ExportedNestEggConfig  # noqa: PLC0415
        from ..models.exported_nest_egg_docker_images import ExportedNestEggDockerImages  # noqa: PLC0415
        from ..models.exported_nest_egg_scripts import ExportedNestEggScripts  # noqa: PLC0415
        from ..models.exported_nest_egg_startup_commands import ExportedNestEggStartupCommands  # noqa: PLC0415
        from ..models.exported_nest_egg_variables_item import ExportedNestEggVariablesItem  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        author = d.pop("author")

        config = ExportedNestEggConfig.from_dict(d.pop("config"))

        scripts = ExportedNestEggScripts.from_dict(d.pop("scripts"))

        startup_commands = ExportedNestEggStartupCommands.from_dict(d.pop("startup_commands"))

        docker_images = ExportedNestEggDockerImages.from_dict(d.pop("docker_images"))

        variables = []
        _variables = d.pop("variables")
        for variables_item_data in _variables:
            variables_item = ExportedNestEggVariablesItem.from_dict(variables_item_data)

            variables.append(variables_item)

        _uuid = d.pop("uuid", UNSET)
        uuid: UUID | Unset
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        force_outgoing_ip = d.pop("force_outgoing_ip", UNSET)

        separate_port = d.pop("separate_port", UNSET)

        features = cast(list[str], d.pop("features", UNSET))

        file_denylist = cast(list[str], d.pop("file_denylist", UNSET))

        exported_nest_egg = cls(
            name=name,
            author=author,
            config=config,
            scripts=scripts,
            startup_commands=startup_commands,
            docker_images=docker_images,
            variables=variables,
            uuid=uuid,
            description=description,
            force_outgoing_ip=force_outgoing_ip,
            separate_port=separate_port,
            features=features,
            file_denylist=file_denylist,
        )

        exported_nest_egg.additional_properties = d
        return exported_nest_egg

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
