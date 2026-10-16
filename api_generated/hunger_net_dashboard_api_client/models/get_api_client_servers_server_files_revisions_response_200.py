from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.revision import Revision


T = TypeVar("T", bound="GetApiClientServersServerFilesRevisionsResponse200")


@_attrs_define
class GetApiClientServersServerFilesRevisionsResponse200:
    """
    Attributes:
        revisions (list[Revision]):
    """

    revisions: list[Revision]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        revisions = []
        for revisions_item_data in self.revisions:
            revisions_item = revisions_item_data.to_dict()
            revisions.append(revisions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "revisions": revisions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.revision import Revision  # noqa: PLC0415

        d = dict(src_dict)
        revisions = []
        _revisions = d.pop("revisions")
        for revisions_item_data in _revisions:
            revisions_item = Revision.from_dict(revisions_item_data)

            revisions.append(revisions_item)

        get_api_client_servers_server_files_revisions_response_200 = cls(
            revisions=revisions,
        )

        get_api_client_servers_server_files_revisions_response_200.additional_properties = d
        return get_api_client_servers_server_files_revisions_response_200

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
