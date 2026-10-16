from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_credentials_type_0 import DatabaseCredentialsType0
    from ..models.database_credentials_type_1 import DatabaseCredentialsType1


T = TypeVar("T", bound="PatchApiAdminDatabaseHostsDatabaseHostBody")


@_attrs_define
class PatchApiAdminDatabaseHostsDatabaseHostBody:
    """
    Attributes:
        name (None | str | Unset):
        deployment_enabled (bool | None | Unset):
        maintenance_enabled (bool | None | Unset):
        public_host (None | str | Unset):
        public_port (int | None | Unset):
        credentials (DatabaseCredentialsType0 | DatabaseCredentialsType1 | None | Unset):
    """

    name: None | str | Unset = UNSET
    deployment_enabled: bool | None | Unset = UNSET
    maintenance_enabled: bool | None | Unset = UNSET
    public_host: None | str | Unset = UNSET
    public_port: int | None | Unset = UNSET
    credentials: DatabaseCredentialsType0 | DatabaseCredentialsType1 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.database_credentials_type_0 import DatabaseCredentialsType0  # noqa: PLC0415
        from ..models.database_credentials_type_1 import DatabaseCredentialsType1  # noqa: PLC0415

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        deployment_enabled: bool | None | Unset
        if isinstance(self.deployment_enabled, Unset):
            deployment_enabled = UNSET
        else:
            deployment_enabled = self.deployment_enabled

        maintenance_enabled: bool | None | Unset
        if isinstance(self.maintenance_enabled, Unset):
            maintenance_enabled = UNSET
        else:
            maintenance_enabled = self.maintenance_enabled

        public_host: None | str | Unset
        if isinstance(self.public_host, Unset):
            public_host = UNSET
        else:
            public_host = self.public_host

        public_port: int | None | Unset
        if isinstance(self.public_port, Unset):
            public_port = UNSET
        else:
            public_port = self.public_port

        credentials: dict[str, Any] | None | Unset
        if isinstance(self.credentials, Unset):
            credentials = UNSET
        elif isinstance(self.credentials, DatabaseCredentialsType0):
            credentials = self.credentials.to_dict()
        elif isinstance(self.credentials, DatabaseCredentialsType1):
            credentials = self.credentials.to_dict()
        else:
            credentials = self.credentials

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if deployment_enabled is not UNSET:
            field_dict["deployment_enabled"] = deployment_enabled
        if maintenance_enabled is not UNSET:
            field_dict["maintenance_enabled"] = maintenance_enabled
        if public_host is not UNSET:
            field_dict["public_host"] = public_host
        if public_port is not UNSET:
            field_dict["public_port"] = public_port
        if credentials is not UNSET:
            field_dict["credentials"] = credentials

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_credentials_type_0 import DatabaseCredentialsType0  # noqa: PLC0415
        from ..models.database_credentials_type_1 import DatabaseCredentialsType1  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_deployment_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        deployment_enabled = _parse_deployment_enabled(d.pop("deployment_enabled", UNSET))

        def _parse_maintenance_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        maintenance_enabled = _parse_maintenance_enabled(d.pop("maintenance_enabled", UNSET))

        def _parse_public_host(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_host = _parse_public_host(d.pop("public_host", UNSET))

        def _parse_public_port(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        public_port = _parse_public_port(d.pop("public_port", UNSET))

        def _parse_credentials(data: object) -> DatabaseCredentialsType0 | DatabaseCredentialsType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_database_credentials_type_0 = DatabaseCredentialsType0.from_dict(data)

                return componentsschemas_database_credentials_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_database_credentials_type_1 = DatabaseCredentialsType1.from_dict(data)

                return componentsschemas_database_credentials_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatabaseCredentialsType0 | DatabaseCredentialsType1 | None | Unset, data)

        credentials = _parse_credentials(d.pop("credentials", UNSET))

        patch_api_admin_database_hosts_database_host_body = cls(
            name=name,
            deployment_enabled=deployment_enabled,
            maintenance_enabled=maintenance_enabled,
            public_host=public_host,
            public_port=public_port,
            credentials=credentials,
        )

        patch_api_admin_database_hosts_database_host_body.additional_properties = d
        return patch_api_admin_database_hosts_database_host_body

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
