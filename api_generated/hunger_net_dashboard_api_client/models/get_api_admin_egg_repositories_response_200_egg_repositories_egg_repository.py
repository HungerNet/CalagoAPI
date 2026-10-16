from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.egg_repository_credentials_type_0 import EggRepositoryCredentialsType0
    from ..models.egg_repository_credentials_type_1 import EggRepositoryCredentialsType1
    from ..models.egg_repository_credentials_type_2 import EggRepositoryCredentialsType2


T = TypeVar("T", bound="GetApiAdminEggRepositoriesResponse200EggRepositoriesEggRepository")


@_attrs_define
class GetApiAdminEggRepositoriesResponse200EggRepositoriesEggRepository:
    """
    Attributes:
        uuid (UUID):
        name (str):
        git_repository (str):
        credentials (EggRepositoryCredentialsType0 | EggRepositoryCredentialsType1 | EggRepositoryCredentialsType2):
        created (datetime.datetime):
        description (None | str | Unset):
        last_synced (datetime.datetime | None | Unset):
    """

    uuid: UUID
    name: str
    git_repository: str
    credentials: EggRepositoryCredentialsType0 | EggRepositoryCredentialsType1 | EggRepositoryCredentialsType2
    created: datetime.datetime
    description: None | str | Unset = UNSET
    last_synced: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.egg_repository_credentials_type_0 import EggRepositoryCredentialsType0  # noqa: PLC0415
        from ..models.egg_repository_credentials_type_1 import EggRepositoryCredentialsType1  # noqa: PLC0415

        uuid = str(self.uuid)

        name = self.name

        git_repository = self.git_repository

        credentials: dict[str, Any]
        if isinstance(self.credentials, EggRepositoryCredentialsType0):
            credentials = self.credentials.to_dict()
        elif isinstance(self.credentials, EggRepositoryCredentialsType1):
            credentials = self.credentials.to_dict()
        else:
            credentials = self.credentials.to_dict()

        created = self.created.isoformat()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        last_synced: None | str | Unset
        if isinstance(self.last_synced, Unset):
            last_synced = UNSET
        elif isinstance(self.last_synced, datetime.datetime):
            last_synced = self.last_synced.isoformat()
        else:
            last_synced = self.last_synced

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "git_repository": git_repository,
                "credentials": credentials,
                "created": created,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if last_synced is not UNSET:
            field_dict["last_synced"] = last_synced

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.egg_repository_credentials_type_0 import EggRepositoryCredentialsType0  # noqa: PLC0415
        from ..models.egg_repository_credentials_type_1 import EggRepositoryCredentialsType1  # noqa: PLC0415
        from ..models.egg_repository_credentials_type_2 import EggRepositoryCredentialsType2  # noqa: PLC0415

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        git_repository = d.pop("git_repository")

        def _parse_credentials(
            data: object,
        ) -> EggRepositoryCredentialsType0 | EggRepositoryCredentialsType1 | EggRepositoryCredentialsType2:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_egg_repository_credentials_type_0 = EggRepositoryCredentialsType0.from_dict(data)

                return componentsschemas_egg_repository_credentials_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_egg_repository_credentials_type_1 = EggRepositoryCredentialsType1.from_dict(data)

                return componentsschemas_egg_repository_credentials_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_egg_repository_credentials_type_2 = EggRepositoryCredentialsType2.from_dict(data)

            return componentsschemas_egg_repository_credentials_type_2

        credentials = _parse_credentials(d.pop("credentials"))

        created = datetime.datetime.fromisoformat(d.pop("created"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_last_synced(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_synced_type_0 = datetime.datetime.fromisoformat(data)

                return last_synced_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_synced = _parse_last_synced(d.pop("last_synced", UNSET))

        get_api_admin_egg_repositories_response_200_egg_repositories_egg_repository = cls(
            uuid=uuid,
            name=name,
            git_repository=git_repository,
            credentials=credentials,
            created=created,
            description=description,
            last_synced=last_synced,
        )

        get_api_admin_egg_repositories_response_200_egg_repositories_egg_repository.additional_properties = d
        return get_api_admin_egg_repositories_response_200_egg_repositories_egg_repository

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
