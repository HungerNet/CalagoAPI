from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mail_mode_type_1_type import MailModeType1Type
from ..models.tls_mode import TlsMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="MailModeType1")


@_attrs_define
class MailModeType1:
    """
    Attributes:
        host (str):
        port (int):
        tls_mode (TlsMode):
        from_address (str):
        type_ (MailModeType1Type):
        username (None | str | Unset):
        password (None | str | Unset):
        skip_cert_validation (bool | Unset):
        helo_domain (None | str | Unset):
        from_name (None | str | Unset):
    """

    host: str
    port: int
    tls_mode: TlsMode
    from_address: str
    type_: MailModeType1Type
    username: None | str | Unset = UNSET
    password: None | str | Unset = UNSET
    skip_cert_validation: bool | Unset = UNSET
    helo_domain: None | str | Unset = UNSET
    from_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        host = self.host

        port = self.port

        tls_mode = self.tls_mode.value

        from_address = self.from_address

        type_ = self.type_.value

        username: None | str | Unset
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        skip_cert_validation = self.skip_cert_validation

        helo_domain: None | str | Unset
        if isinstance(self.helo_domain, Unset):
            helo_domain = UNSET
        else:
            helo_domain = self.helo_domain

        from_name: None | str | Unset
        if isinstance(self.from_name, Unset):
            from_name = UNSET
        else:
            from_name = self.from_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "host": host,
                "port": port,
                "tls_mode": tls_mode,
                "from_address": from_address,
                "type": type_,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if skip_cert_validation is not UNSET:
            field_dict["skip_cert_validation"] = skip_cert_validation
        if helo_domain is not UNSET:
            field_dict["helo_domain"] = helo_domain
        if from_name is not UNSET:
            field_dict["from_name"] = from_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        host = d.pop("host")

        port = d.pop("port")

        tls_mode = TlsMode(d.pop("tls_mode"))

        from_address = d.pop("from_address")

        type_ = MailModeType1Type(d.pop("type"))

        def _parse_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        username = _parse_username(d.pop("username", UNSET))

        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))

        skip_cert_validation = d.pop("skip_cert_validation", UNSET)

        def _parse_helo_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        helo_domain = _parse_helo_domain(d.pop("helo_domain", UNSET))

        def _parse_from_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_name = _parse_from_name(d.pop("from_name", UNSET))

        mail_mode_type_1 = cls(
            host=host,
            port=port,
            tls_mode=tls_mode,
            from_address=from_address,
            type_=type_,
            username=username,
            password=password,
            skip_cert_validation=skip_cert_validation,
            helo_domain=helo_domain,
            from_name=from_name,
        )

        mail_mode_type_1.additional_properties = d
        return mail_mode_type_1

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
