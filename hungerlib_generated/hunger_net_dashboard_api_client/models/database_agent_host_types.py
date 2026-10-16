from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_agent_host_type_settings import DatabaseAgentHostTypeSettings


T = TypeVar("T", bound="DatabaseAgentHostTypes")


@_attrs_define
class DatabaseAgentHostTypes:
    """
    Attributes:
        postgres (DatabaseAgentHostTypeSettings | Unset):
        mariadb (DatabaseAgentHostTypeSettings | Unset):
        mongodb (DatabaseAgentHostTypeSettings | Unset):
        redis (DatabaseAgentHostTypeSettings | Unset):
    """

    postgres: DatabaseAgentHostTypeSettings | Unset = UNSET
    mariadb: DatabaseAgentHostTypeSettings | Unset = UNSET
    mongodb: DatabaseAgentHostTypeSettings | Unset = UNSET
    redis: DatabaseAgentHostTypeSettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        postgres: dict[str, Any] | Unset = UNSET
        if not isinstance(self.postgres, Unset):
            postgres = self.postgres.to_dict()

        mariadb: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mariadb, Unset):
            mariadb = self.mariadb.to_dict()

        mongodb: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mongodb, Unset):
            mongodb = self.mongodb.to_dict()

        redis: dict[str, Any] | Unset = UNSET
        if not isinstance(self.redis, Unset):
            redis = self.redis.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if postgres is not UNSET:
            field_dict["postgres"] = postgres
        if mariadb is not UNSET:
            field_dict["mariadb"] = mariadb
        if mongodb is not UNSET:
            field_dict["mongodb"] = mongodb
        if redis is not UNSET:
            field_dict["redis"] = redis

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_agent_host_type_settings import DatabaseAgentHostTypeSettings  # noqa: PLC0415

        d = dict(src_dict)
        _postgres = d.pop("postgres", UNSET)
        postgres: DatabaseAgentHostTypeSettings | Unset
        if isinstance(_postgres, Unset):
            postgres = UNSET
        else:
            postgres = DatabaseAgentHostTypeSettings.from_dict(_postgres)

        _mariadb = d.pop("mariadb", UNSET)
        mariadb: DatabaseAgentHostTypeSettings | Unset
        if isinstance(_mariadb, Unset):
            mariadb = UNSET
        else:
            mariadb = DatabaseAgentHostTypeSettings.from_dict(_mariadb)

        _mongodb = d.pop("mongodb", UNSET)
        mongodb: DatabaseAgentHostTypeSettings | Unset
        if isinstance(_mongodb, Unset):
            mongodb = UNSET
        else:
            mongodb = DatabaseAgentHostTypeSettings.from_dict(_mongodb)

        _redis = d.pop("redis", UNSET)
        redis: DatabaseAgentHostTypeSettings | Unset
        if isinstance(_redis, Unset):
            redis = UNSET
        else:
            redis = DatabaseAgentHostTypeSettings.from_dict(_redis)

        database_agent_host_types = cls(
            postgres=postgres,
            mariadb=mariadb,
            mongodb=mongodb,
            redis=redis,
        )

        database_agent_host_types.additional_properties = d
        return database_agent_host_types

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
