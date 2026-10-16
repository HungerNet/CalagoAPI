from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApiRemoteEnrollResponse200")


@_attrs_define
class PostApiRemoteEnrollResponse200:
    """
    Attributes:
        uuid (UUID):
        token_id (str):
        token (str):
        remote (str):
        allowed_origins (list[str]):
        api_port (int):
        sftp_port (int):
    """

    uuid: UUID
    token_id: str
    token: str
    remote: str
    allowed_origins: list[str]
    api_port: int
    sftp_port: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        token_id = self.token_id

        token = self.token

        remote = self.remote

        allowed_origins = self.allowed_origins

        api_port = self.api_port

        sftp_port = self.sftp_port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "token_id": token_id,
                "token": token,
                "remote": remote,
                "allowed_origins": allowed_origins,
                "api_port": api_port,
                "sftp_port": sftp_port,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        token_id = d.pop("token_id")

        token = d.pop("token")

        remote = d.pop("remote")

        allowed_origins = cast(list[str], d.pop("allowed_origins"))

        api_port = d.pop("api_port")

        sftp_port = d.pop("sftp_port")

        post_api_remote_enroll_response_200 = cls(
            uuid=uuid,
            token_id=token_id,
            token=token,
            remote=remote,
            allowed_origins=allowed_origins,
            api_port=api_port,
            sftp_port=sftp_port,
        )

        post_api_remote_enroll_response_200.additional_properties = d
        return post_api_remote_enroll_response_200

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
