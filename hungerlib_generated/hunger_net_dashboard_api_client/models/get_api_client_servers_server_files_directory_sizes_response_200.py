from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.directory_sizes import DirectorySizes


T = TypeVar("T", bound="GetApiClientServersServerFilesDirectorySizesResponse200")


@_attrs_define
class GetApiClientServersServerFilesDirectorySizesResponse200:
    """
    Attributes:
        directory_sizes (DirectorySizes):
    """

    directory_sizes: DirectorySizes
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        directory_sizes = self.directory_sizes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "directory_sizes": directory_sizes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.directory_sizes import DirectorySizes  # noqa: PLC0415

        d = dict(src_dict)
        directory_sizes = DirectorySizes.from_dict(d.pop("directory_sizes"))

        get_api_client_servers_server_files_directory_sizes_response_200 = cls(
            directory_sizes=directory_sizes,
        )

        get_api_client_servers_server_files_directory_sizes_response_200.additional_properties = d
        return get_api_client_servers_server_files_directory_sizes_response_200

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
