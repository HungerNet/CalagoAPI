from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.database_type import DatabaseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_credentials_type_0 import DatabaseCredentialsType0
    from ..models.database_credentials_type_1 import DatabaseCredentialsType1


T = TypeVar("T", bound="PostApiAdminDatabaseHostsBody")


@_attrs_define
class PostApiAdminDatabaseHostsBody:
    """
    Attributes:
        name (str):
        type_ (DatabaseType):
        deployment_enabled (bool):
        maintenance_enabled (bool):
        credentials (DatabaseCredentialsType0 | DatabaseCredentialsType1):
        public_host (None | str | Unset):
        public_port (int | None | Unset):
    """

    name: str
    type_: DatabaseType
    deployment_enabled: bool
    maintenance_enabled: bool
    credentials: DatabaseCredentialsType0 | DatabaseCredentialsType1
    public_host: None | str | Unset = UNSET
    public_port: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.database_credentials_type_0 import DatabaseCredentialsType0  # noqa: PLC0415

        name = self.name

        type_ = self.type_.value

        deployment_enabled = self.deployment_enabled

        maintenance_enabled = self.maintenance_enabled

        credentials: dict[str, Any]
        if isinstance(self.credentials, DatabaseCredentialsType0):
            credentials = self.credentials.to_dict()
        else:
            credentials = self.credentials.to_dict()

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
                "deployment_enabled": deployment_enabled,
                "maintenance_enabled": maintenance_enabled,
                "credentials": credentials,
            }
        )
        if public_host is not UNSET:
            field_dict["public_host"] = public_host
        if public_port is not UNSET:
            field_dict["public_port"] = public_port

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_credentials_type_0 import DatabaseCredentialsType0  # noqa: PLC0415
        from ..models.database_credentials_type_1 import DatabaseCredentialsType1  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        type_ = DatabaseType(d.pop("type"))

        deployment_enabled = d.pop("deployment_enabled")

        maintenance_enabled = d.pop("maintenance_enabled")

        def _parse_credentials(data: object) -> DatabaseCredentialsType0 | DatabaseCredentialsType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_database_credentials_type_0 = DatabaseCredentialsType0.from_dict(data)

                return componentsschemas_database_credentials_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_database_credentials_type_1 = DatabaseCredentialsType1.from_dict(data)

            return componentsschemas_database_credentials_type_1

        credentials = _parse_credentials(d.pop("credentials"))

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

        post_api_admin_database_hosts_body = cls(
            name=name,
            type_=type_,
            deployment_enabled=deployment_enabled,
            maintenance_enabled=maintenance_enabled,
            credentials=credentials,
            public_host=public_host,
            public_port=public_port,
        )

        post_api_admin_database_hosts_body.additional_properties = d
        return post_api_admin_database_hosts_body

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
