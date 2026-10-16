from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.storage_driver_type_1_type import StorageDriverType1Type

T = TypeVar("T", bound="StorageDriverType1")


@_attrs_define
class StorageDriverType1:
    """
    Attributes:
        public_url (str):
        access_key (str):
        secret_key (str):
        bucket (str):
        region (str):
        endpoint (str):
        path_style (bool):
        type_ (StorageDriverType1Type):
    """

    public_url: str
    access_key: str
    secret_key: str
    bucket: str
    region: str
    endpoint: str
    path_style: bool
    type_: StorageDriverType1Type
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        public_url = self.public_url

        access_key = self.access_key

        secret_key = self.secret_key

        bucket = self.bucket

        region = self.region

        endpoint = self.endpoint

        path_style = self.path_style

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "public_url": public_url,
                "access_key": access_key,
                "secret_key": secret_key,
                "bucket": bucket,
                "region": region,
                "endpoint": endpoint,
                "path_style": path_style,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        public_url = d.pop("public_url")

        access_key = d.pop("access_key")

        secret_key = d.pop("secret_key")

        bucket = d.pop("bucket")

        region = d.pop("region")

        endpoint = d.pop("endpoint")

        path_style = d.pop("path_style")

        type_ = StorageDriverType1Type(d.pop("type"))

        storage_driver_type_1 = cls(
            public_url=public_url,
            access_key=access_key,
            secret_key=secret_key,
            bucket=bucket,
            region=region,
            endpoint=endpoint,
            path_style=path_style,
            type_=type_,
        )

        storage_driver_type_1.additional_properties = d
        return storage_driver_type_1

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
