from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.egg_repository_credentials_type_0 import EggRepositoryCredentialsType0
    from ..models.egg_repository_credentials_type_1 import EggRepositoryCredentialsType1
    from ..models.egg_repository_credentials_type_2 import EggRepositoryCredentialsType2


T = TypeVar("T", bound="PatchApiAdminEggRepositoriesEggRepositoryBody")


@_attrs_define
class PatchApiAdminEggRepositoriesEggRepositoryBody:
    """
    Attributes:
        name (None | str | Unset):
        description (None | str | Unset):
        git_repository (None | str | Unset):
        credentials (EggRepositoryCredentialsType0 | EggRepositoryCredentialsType1 | EggRepositoryCredentialsType2 |
            None | Unset):
    """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    git_repository: None | str | Unset = UNSET
    credentials: (
        EggRepositoryCredentialsType0 | EggRepositoryCredentialsType1 | EggRepositoryCredentialsType2 | None | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.egg_repository_credentials_type_0 import EggRepositoryCredentialsType0  # noqa: PLC0415
        from ..models.egg_repository_credentials_type_1 import EggRepositoryCredentialsType1  # noqa: PLC0415
        from ..models.egg_repository_credentials_type_2 import EggRepositoryCredentialsType2  # noqa: PLC0415

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

        git_repository: None | str | Unset
        if isinstance(self.git_repository, Unset):
            git_repository = UNSET
        else:
            git_repository = self.git_repository

        credentials: dict[str, Any] | None | Unset
        if isinstance(self.credentials, Unset):
            credentials = UNSET
        elif isinstance(self.credentials, EggRepositoryCredentialsType0):
            credentials = self.credentials.to_dict()
        elif isinstance(self.credentials, EggRepositoryCredentialsType1):
            credentials = self.credentials.to_dict()
        elif isinstance(self.credentials, EggRepositoryCredentialsType2):
            credentials = self.credentials.to_dict()
        else:
            credentials = self.credentials

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if git_repository is not UNSET:
            field_dict["git_repository"] = git_repository
        if credentials is not UNSET:
            field_dict["credentials"] = credentials

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.egg_repository_credentials_type_0 import EggRepositoryCredentialsType0  # noqa: PLC0415
        from ..models.egg_repository_credentials_type_1 import EggRepositoryCredentialsType1  # noqa: PLC0415
        from ..models.egg_repository_credentials_type_2 import EggRepositoryCredentialsType2  # noqa: PLC0415

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

        def _parse_git_repository(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        git_repository = _parse_git_repository(d.pop("git_repository", UNSET))

        def _parse_credentials(
            data: object,
        ) -> (
            EggRepositoryCredentialsType0 | EggRepositoryCredentialsType1 | EggRepositoryCredentialsType2 | None | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
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
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_egg_repository_credentials_type_2 = EggRepositoryCredentialsType2.from_dict(data)

                return componentsschemas_egg_repository_credentials_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                EggRepositoryCredentialsType0
                | EggRepositoryCredentialsType1
                | EggRepositoryCredentialsType2
                | None
                | Unset,
                data,
            )

        credentials = _parse_credentials(d.pop("credentials", UNSET))

        patch_api_admin_egg_repositories_egg_repository_body = cls(
            name=name,
            description=description,
            git_repository=git_repository,
            credentials=credentials,
        )

        patch_api_admin_egg_repositories_egg_repository_body.additional_properties = d
        return patch_api_admin_egg_repositories_egg_repository_body

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
