from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.compression_type import CompressionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupConfigsS3")


@_attrs_define
class BackupConfigsS3:
    """
    Attributes:
        access_key (str):
        secret_key (str):
        bucket (str):
        region (str):
        endpoint (str):
        path_style (bool):
        part_size (int):
        compression_type (CompressionType | Unset):
    """

    access_key: str
    secret_key: str
    bucket: str
    region: str
    endpoint: str
    path_style: bool
    part_size: int
    compression_type: CompressionType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_key = self.access_key

        secret_key = self.secret_key

        bucket = self.bucket

        region = self.region

        endpoint = self.endpoint

        path_style = self.path_style

        part_size = self.part_size

        compression_type: str | Unset = UNSET
        if not isinstance(self.compression_type, Unset):
            compression_type = self.compression_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access_key": access_key,
                "secret_key": secret_key,
                "bucket": bucket,
                "region": region,
                "endpoint": endpoint,
                "path_style": path_style,
                "part_size": part_size,
            }
        )
        if compression_type is not UNSET:
            field_dict["compression_type"] = compression_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_key = d.pop("access_key")

        secret_key = d.pop("secret_key")

        bucket = d.pop("bucket")

        region = d.pop("region")

        endpoint = d.pop("endpoint")

        path_style = d.pop("path_style")

        part_size = d.pop("part_size")

        _compression_type = d.pop("compression_type", UNSET)
        compression_type: CompressionType | Unset
        if isinstance(_compression_type, Unset):
            compression_type = UNSET
        else:
            compression_type = CompressionType(_compression_type)

        backup_configs_s3 = cls(
            access_key=access_key,
            secret_key=secret_key,
            bucket=bucket,
            region=region,
            endpoint=endpoint,
            path_style=path_style,
            part_size=part_size,
            compression_type=compression_type,
        )

        backup_configs_s3.additional_properties = d
        return backup_configs_s3

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
