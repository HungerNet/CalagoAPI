from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.metadata_toml import MetadataToml


T = TypeVar("T", bound="PendingExtension")


@_attrs_define
class PendingExtension:
    """
    Attributes:
        metadata_toml (MetadataToml):
        package_name (str):
        description (str):
        authors (list[str]):
        version (str):
    """

    metadata_toml: MetadataToml
    package_name: str
    description: str
    authors: list[str]
    version: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metadata_toml = self.metadata_toml.to_dict()

        package_name = self.package_name

        description = self.description

        authors = self.authors

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metadata_toml": metadata_toml,
                "package_name": package_name,
                "description": description,
                "authors": authors,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata_toml import MetadataToml  # noqa: PLC0415

        d = dict(src_dict)
        metadata_toml = MetadataToml.from_dict(d.pop("metadata_toml"))

        package_name = d.pop("package_name")

        description = d.pop("description")

        authors = cast(list[str], d.pop("authors"))

        version = d.pop("version")

        pending_extension = cls(
            metadata_toml=metadata_toml,
            package_name=package_name,
            description=description,
            authors=authors,
            version=version,
        )

        pending_extension.additional_properties = d
        return pending_extension

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
