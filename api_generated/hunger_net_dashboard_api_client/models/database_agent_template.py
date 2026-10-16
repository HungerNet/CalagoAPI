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
    from ..models.database_agent_template_docker_images import DatabaseAgentTemplateDockerImages


T = TypeVar("T", bound="DatabaseAgentTemplate")


@_attrs_define
class DatabaseAgentTemplate:
    """
    Attributes:
        uuid (UUID):
        name (str):
        type_ (DatabaseAgentType):
        docker_images (DatabaseAgentTemplateDockerImages):
        memory (int):
        swap (int):
        disk (int):
        cpu (int):
        version (int):
        created (datetime.datetime):
        description (None | str | Unset):
        io_weight (int | None | Unset):
    """

    uuid: UUID
    name: str
    type_: DatabaseAgentType
    docker_images: DatabaseAgentTemplateDockerImages
    memory: int
    swap: int
    disk: int
    cpu: int
    version: int
    created: datetime.datetime
    description: None | str | Unset = UNSET
    io_weight: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        type_ = self.type_.value

        docker_images = self.docker_images.to_dict()

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
                "docker_images": docker_images,
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
        if io_weight is not UNSET:
            field_dict["io_weight"] = io_weight

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_agent_template_docker_images import DatabaseAgentTemplateDockerImages  # noqa: PLC0415

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        type_ = DatabaseAgentType(d.pop("type"))

        docker_images = DatabaseAgentTemplateDockerImages.from_dict(d.pop("docker_images"))

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

        def _parse_io_weight(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        io_weight = _parse_io_weight(d.pop("io_weight", UNSET))

        database_agent_template = cls(
            uuid=uuid,
            name=name,
            type_=type_,
            docker_images=docker_images,
            memory=memory,
            swap=swap,
            disk=disk,
            cpu=cpu,
            version=version,
            created=created,
            description=description,
            io_weight=io_weight,
        )

        database_agent_template.additional_properties = d
        return database_agent_template

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
