from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_api_client_servers_eggs_response_200_nest_eggs_nest_egg_docker_images import (
        GetApiClientServersEggsResponse200NestEggsNestEggDockerImages,
    )
    from ..models.get_api_client_servers_eggs_response_200_nest_eggs_nest_egg_startup_commands import (
        GetApiClientServersEggsResponse200NestEggsNestEggStartupCommands,
    )


T = TypeVar("T", bound="GetApiClientServersEggsResponse200NestEggsNestEgg")


@_attrs_define
class GetApiClientServersEggsResponse200NestEggsNestEgg:
    """
    Attributes:
        uuid (UUID):
        name (str):
        startup_commands (GetApiClientServersEggsResponse200NestEggsNestEggStartupCommands):
        separate_port (bool):
        features (list[str]):
        docker_images (GetApiClientServersEggsResponse200NestEggsNestEggDockerImages):
        created (datetime.datetime):
        description (None | str | Unset):
    """

    uuid: UUID
    name: str
    startup_commands: GetApiClientServersEggsResponse200NestEggsNestEggStartupCommands
    separate_port: bool
    features: list[str]
    docker_images: GetApiClientServersEggsResponse200NestEggsNestEggDockerImages
    created: datetime.datetime
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        startup_commands = self.startup_commands.to_dict()

        separate_port = self.separate_port

        features = self.features

        docker_images = self.docker_images.to_dict()

        created = self.created.isoformat()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "startup_commands": startup_commands,
                "separate_port": separate_port,
                "features": features,
                "docker_images": docker_images,
                "created": created,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_client_servers_eggs_response_200_nest_eggs_nest_egg_docker_images import (
            GetApiClientServersEggsResponse200NestEggsNestEggDockerImages,  # noqa: PLC0415
        )
        from ..models.get_api_client_servers_eggs_response_200_nest_eggs_nest_egg_startup_commands import (
            GetApiClientServersEggsResponse200NestEggsNestEggStartupCommands,  # noqa: PLC0415
        )

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        startup_commands = GetApiClientServersEggsResponse200NestEggsNestEggStartupCommands.from_dict(
            d.pop("startup_commands")
        )

        separate_port = d.pop("separate_port")

        features = cast(list[str], d.pop("features"))

        docker_images = GetApiClientServersEggsResponse200NestEggsNestEggDockerImages.from_dict(d.pop("docker_images"))

        created = datetime.datetime.fromisoformat(d.pop("created"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        get_api_client_servers_eggs_response_200_nest_eggs_nest_egg = cls(
            uuid=uuid,
            name=name,
            startup_commands=startup_commands,
            separate_port=separate_port,
            features=features,
            docker_images=docker_images,
            created=created,
            description=description,
        )

        get_api_client_servers_eggs_response_200_nest_eggs_nest_egg.additional_properties = d
        return get_api_client_servers_eggs_response_200_nest_eggs_nest_egg

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
