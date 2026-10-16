from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.minecraft_build_installation_step_type_0 import MinecraftBuildInstallationStepType0
    from ..models.minecraft_build_installation_step_type_1 import MinecraftBuildInstallationStepType1
    from ..models.minecraft_build_installation_step_type_2 import MinecraftBuildInstallationStepType2


T = TypeVar("T", bound="MinecraftBuild")


@_attrs_define
class MinecraftBuild:
    """
    Attributes:
        uuid (UUID):
        type_ (str):
        experimental (bool):
        name (str):
        installation (list[list[MinecraftBuildInstallationStepType0 | MinecraftBuildInstallationStepType1 |
            MinecraftBuildInstallationStepType2]]):
        version_id (None | str | Unset):
        project_version_id (None | str | Unset):
        created (datetime.datetime | None | Unset):
    """

    uuid: UUID
    type_: str
    experimental: bool
    name: str
    installation: list[
        list[
            MinecraftBuildInstallationStepType0
            | MinecraftBuildInstallationStepType1
            | MinecraftBuildInstallationStepType2
        ]
    ]
    version_id: None | str | Unset = UNSET
    project_version_id: None | str | Unset = UNSET
    created: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.minecraft_build_installation_step_type_0 import MinecraftBuildInstallationStepType0  # noqa: PLC0415
        from ..models.minecraft_build_installation_step_type_1 import MinecraftBuildInstallationStepType1  # noqa: PLC0415

        uuid = str(self.uuid)

        type_ = self.type_

        experimental = self.experimental

        name = self.name

        installation = []
        for installation_item_data in self.installation:
            installation_item = []
            for installation_item_item_data in installation_item_data:
                installation_item_item: dict[str, Any]
                if isinstance(installation_item_item_data, MinecraftBuildInstallationStepType0):
                    installation_item_item = installation_item_item_data.to_dict()
                elif isinstance(installation_item_item_data, MinecraftBuildInstallationStepType1):
                    installation_item_item = installation_item_item_data.to_dict()
                else:
                    installation_item_item = installation_item_item_data.to_dict()

                installation_item.append(installation_item_item)

            installation.append(installation_item)

        version_id: None | str | Unset
        if isinstance(self.version_id, Unset):
            version_id = UNSET
        else:
            version_id = self.version_id

        project_version_id: None | str | Unset
        if isinstance(self.project_version_id, Unset):
            project_version_id = UNSET
        else:
            project_version_id = self.project_version_id

        created: None | str | Unset
        if isinstance(self.created, Unset):
            created = UNSET
        elif isinstance(self.created, datetime.datetime):
            created = self.created.isoformat()
        else:
            created = self.created

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "type": type_,
                "experimental": experimental,
                "name": name,
                "installation": installation,
            }
        )
        if version_id is not UNSET:
            field_dict["version_id"] = version_id
        if project_version_id is not UNSET:
            field_dict["project_version_id"] = project_version_id
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.minecraft_build_installation_step_type_0 import MinecraftBuildInstallationStepType0  # noqa: PLC0415
        from ..models.minecraft_build_installation_step_type_1 import MinecraftBuildInstallationStepType1  # noqa: PLC0415
        from ..models.minecraft_build_installation_step_type_2 import MinecraftBuildInstallationStepType2  # noqa: PLC0415

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        type_ = d.pop("type")

        experimental = d.pop("experimental")

        name = d.pop("name")

        installation = []
        _installation = d.pop("installation")
        for installation_item_data in _installation:
            installation_item = []
            _installation_item = installation_item_data
            for installation_item_item_data in _installation_item:

                def _parse_installation_item_item(
                    data: object,
                ) -> (
                    MinecraftBuildInstallationStepType0
                    | MinecraftBuildInstallationStepType1
                    | MinecraftBuildInstallationStepType2
                ):
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_minecraft_build_installation_step_type_0 = (
                            MinecraftBuildInstallationStepType0.from_dict(data)
                        )

                        return componentsschemas_minecraft_build_installation_step_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_minecraft_build_installation_step_type_1 = (
                            MinecraftBuildInstallationStepType1.from_dict(data)
                        )

                        return componentsschemas_minecraft_build_installation_step_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_minecraft_build_installation_step_type_2 = (
                        MinecraftBuildInstallationStepType2.from_dict(data)
                    )

                    return componentsschemas_minecraft_build_installation_step_type_2

                installation_item_item = _parse_installation_item_item(installation_item_item_data)

                installation_item.append(installation_item_item)

            installation.append(installation_item)

        def _parse_version_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version_id = _parse_version_id(d.pop("version_id", UNSET))

        def _parse_project_version_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_version_id = _parse_project_version_id(d.pop("project_version_id", UNSET))

        def _parse_created(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_type_0 = datetime.datetime.fromisoformat(data)

                return created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created = _parse_created(d.pop("created", UNSET))

        minecraft_build = cls(
            uuid=uuid,
            type_=type_,
            experimental=experimental,
            name=name,
            installation=installation,
            version_id=version_id,
            project_version_id=project_version_id,
            created=created,
        )

        minecraft_build.additional_properties = d
        return minecraft_build

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
