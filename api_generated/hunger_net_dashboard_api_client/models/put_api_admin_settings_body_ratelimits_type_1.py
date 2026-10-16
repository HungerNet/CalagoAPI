from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ratelimit_configuration import RatelimitConfiguration


T = TypeVar("T", bound="PutApiAdminSettingsBodyRatelimitsType1")


@_attrs_define
class PutApiAdminSettingsBodyRatelimitsType1:
    """
    Attributes:
        auth_register (None | RatelimitConfiguration | Unset):
        auth_login (None | RatelimitConfiguration | Unset):
        auth_login_checkpoint (None | RatelimitConfiguration | Unset):
        auth_login_checkpoint_email (None | RatelimitConfiguration | Unset):
        auth_login_security_key (None | RatelimitConfiguration | Unset):
        auth_password_forgot (None | RatelimitConfiguration | Unset):
        auth_password_reset (None | RatelimitConfiguration | Unset):
        auth_email_verification (None | RatelimitConfiguration | Unset):
        client (None | RatelimitConfiguration | Unset):
        client_account_email_resend_verification (None | RatelimitConfiguration | Unset):
        client_servers_backups_create (None | RatelimitConfiguration | Unset):
        client_servers_files_pull (None | RatelimitConfiguration | Unset):
        client_servers_files_pull_query (None | RatelimitConfiguration | Unset):
        remote (None | RatelimitConfiguration | Unset):
        remote_sftp_auth (None | RatelimitConfiguration | Unset):
        remote_enroll (None | RatelimitConfiguration | Unset):
        exempt_ips (list[str] | None | Unset):
        exempt_api_keys (list[UUID] | None | Unset):
    """

    auth_register: None | RatelimitConfiguration | Unset = UNSET
    auth_login: None | RatelimitConfiguration | Unset = UNSET
    auth_login_checkpoint: None | RatelimitConfiguration | Unset = UNSET
    auth_login_checkpoint_email: None | RatelimitConfiguration | Unset = UNSET
    auth_login_security_key: None | RatelimitConfiguration | Unset = UNSET
    auth_password_forgot: None | RatelimitConfiguration | Unset = UNSET
    auth_password_reset: None | RatelimitConfiguration | Unset = UNSET
    auth_email_verification: None | RatelimitConfiguration | Unset = UNSET
    client: None | RatelimitConfiguration | Unset = UNSET
    client_account_email_resend_verification: None | RatelimitConfiguration | Unset = UNSET
    client_servers_backups_create: None | RatelimitConfiguration | Unset = UNSET
    client_servers_files_pull: None | RatelimitConfiguration | Unset = UNSET
    client_servers_files_pull_query: None | RatelimitConfiguration | Unset = UNSET
    remote: None | RatelimitConfiguration | Unset = UNSET
    remote_sftp_auth: None | RatelimitConfiguration | Unset = UNSET
    remote_enroll: None | RatelimitConfiguration | Unset = UNSET
    exempt_ips: list[str] | None | Unset = UNSET
    exempt_api_keys: list[UUID] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ratelimit_configuration import RatelimitConfiguration  # noqa: PLC0415

        auth_register: dict[str, Any] | None | Unset
        if isinstance(self.auth_register, Unset):
            auth_register = UNSET
        elif isinstance(self.auth_register, RatelimitConfiguration):
            auth_register = self.auth_register.to_dict()
        else:
            auth_register = self.auth_register

        auth_login: dict[str, Any] | None | Unset
        if isinstance(self.auth_login, Unset):
            auth_login = UNSET
        elif isinstance(self.auth_login, RatelimitConfiguration):
            auth_login = self.auth_login.to_dict()
        else:
            auth_login = self.auth_login

        auth_login_checkpoint: dict[str, Any] | None | Unset
        if isinstance(self.auth_login_checkpoint, Unset):
            auth_login_checkpoint = UNSET
        elif isinstance(self.auth_login_checkpoint, RatelimitConfiguration):
            auth_login_checkpoint = self.auth_login_checkpoint.to_dict()
        else:
            auth_login_checkpoint = self.auth_login_checkpoint

        auth_login_checkpoint_email: dict[str, Any] | None | Unset
        if isinstance(self.auth_login_checkpoint_email, Unset):
            auth_login_checkpoint_email = UNSET
        elif isinstance(self.auth_login_checkpoint_email, RatelimitConfiguration):
            auth_login_checkpoint_email = self.auth_login_checkpoint_email.to_dict()
        else:
            auth_login_checkpoint_email = self.auth_login_checkpoint_email

        auth_login_security_key: dict[str, Any] | None | Unset
        if isinstance(self.auth_login_security_key, Unset):
            auth_login_security_key = UNSET
        elif isinstance(self.auth_login_security_key, RatelimitConfiguration):
            auth_login_security_key = self.auth_login_security_key.to_dict()
        else:
            auth_login_security_key = self.auth_login_security_key

        auth_password_forgot: dict[str, Any] | None | Unset
        if isinstance(self.auth_password_forgot, Unset):
            auth_password_forgot = UNSET
        elif isinstance(self.auth_password_forgot, RatelimitConfiguration):
            auth_password_forgot = self.auth_password_forgot.to_dict()
        else:
            auth_password_forgot = self.auth_password_forgot

        auth_password_reset: dict[str, Any] | None | Unset
        if isinstance(self.auth_password_reset, Unset):
            auth_password_reset = UNSET
        elif isinstance(self.auth_password_reset, RatelimitConfiguration):
            auth_password_reset = self.auth_password_reset.to_dict()
        else:
            auth_password_reset = self.auth_password_reset

        auth_email_verification: dict[str, Any] | None | Unset
        if isinstance(self.auth_email_verification, Unset):
            auth_email_verification = UNSET
        elif isinstance(self.auth_email_verification, RatelimitConfiguration):
            auth_email_verification = self.auth_email_verification.to_dict()
        else:
            auth_email_verification = self.auth_email_verification

        client: dict[str, Any] | None | Unset
        if isinstance(self.client, Unset):
            client = UNSET
        elif isinstance(self.client, RatelimitConfiguration):
            client = self.client.to_dict()
        else:
            client = self.client

        client_account_email_resend_verification: dict[str, Any] | None | Unset
        if isinstance(self.client_account_email_resend_verification, Unset):
            client_account_email_resend_verification = UNSET
        elif isinstance(self.client_account_email_resend_verification, RatelimitConfiguration):
            client_account_email_resend_verification = self.client_account_email_resend_verification.to_dict()
        else:
            client_account_email_resend_verification = self.client_account_email_resend_verification

        client_servers_backups_create: dict[str, Any] | None | Unset
        if isinstance(self.client_servers_backups_create, Unset):
            client_servers_backups_create = UNSET
        elif isinstance(self.client_servers_backups_create, RatelimitConfiguration):
            client_servers_backups_create = self.client_servers_backups_create.to_dict()
        else:
            client_servers_backups_create = self.client_servers_backups_create

        client_servers_files_pull: dict[str, Any] | None | Unset
        if isinstance(self.client_servers_files_pull, Unset):
            client_servers_files_pull = UNSET
        elif isinstance(self.client_servers_files_pull, RatelimitConfiguration):
            client_servers_files_pull = self.client_servers_files_pull.to_dict()
        else:
            client_servers_files_pull = self.client_servers_files_pull

        client_servers_files_pull_query: dict[str, Any] | None | Unset
        if isinstance(self.client_servers_files_pull_query, Unset):
            client_servers_files_pull_query = UNSET
        elif isinstance(self.client_servers_files_pull_query, RatelimitConfiguration):
            client_servers_files_pull_query = self.client_servers_files_pull_query.to_dict()
        else:
            client_servers_files_pull_query = self.client_servers_files_pull_query

        remote: dict[str, Any] | None | Unset
        if isinstance(self.remote, Unset):
            remote = UNSET
        elif isinstance(self.remote, RatelimitConfiguration):
            remote = self.remote.to_dict()
        else:
            remote = self.remote

        remote_sftp_auth: dict[str, Any] | None | Unset
        if isinstance(self.remote_sftp_auth, Unset):
            remote_sftp_auth = UNSET
        elif isinstance(self.remote_sftp_auth, RatelimitConfiguration):
            remote_sftp_auth = self.remote_sftp_auth.to_dict()
        else:
            remote_sftp_auth = self.remote_sftp_auth

        remote_enroll: dict[str, Any] | None | Unset
        if isinstance(self.remote_enroll, Unset):
            remote_enroll = UNSET
        elif isinstance(self.remote_enroll, RatelimitConfiguration):
            remote_enroll = self.remote_enroll.to_dict()
        else:
            remote_enroll = self.remote_enroll

        exempt_ips: list[str] | None | Unset
        if isinstance(self.exempt_ips, Unset):
            exempt_ips = UNSET
        elif isinstance(self.exempt_ips, list):
            exempt_ips = self.exempt_ips

        else:
            exempt_ips = self.exempt_ips

        exempt_api_keys: list[str] | None | Unset
        if isinstance(self.exempt_api_keys, Unset):
            exempt_api_keys = UNSET
        elif isinstance(self.exempt_api_keys, list):
            exempt_api_keys = []
            for exempt_api_keys_type_0_item_data in self.exempt_api_keys:
                exempt_api_keys_type_0_item = str(exempt_api_keys_type_0_item_data)
                exempt_api_keys.append(exempt_api_keys_type_0_item)

        else:
            exempt_api_keys = self.exempt_api_keys

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_register is not UNSET:
            field_dict["auth_register"] = auth_register
        if auth_login is not UNSET:
            field_dict["auth_login"] = auth_login
        if auth_login_checkpoint is not UNSET:
            field_dict["auth_login_checkpoint"] = auth_login_checkpoint
        if auth_login_checkpoint_email is not UNSET:
            field_dict["auth_login_checkpoint_email"] = auth_login_checkpoint_email
        if auth_login_security_key is not UNSET:
            field_dict["auth_login_security_key"] = auth_login_security_key
        if auth_password_forgot is not UNSET:
            field_dict["auth_password_forgot"] = auth_password_forgot
        if auth_password_reset is not UNSET:
            field_dict["auth_password_reset"] = auth_password_reset
        if auth_email_verification is not UNSET:
            field_dict["auth_email_verification"] = auth_email_verification
        if client is not UNSET:
            field_dict["client"] = client
        if client_account_email_resend_verification is not UNSET:
            field_dict["client_account_email_resend_verification"] = client_account_email_resend_verification
        if client_servers_backups_create is not UNSET:
            field_dict["client_servers_backups_create"] = client_servers_backups_create
        if client_servers_files_pull is not UNSET:
            field_dict["client_servers_files_pull"] = client_servers_files_pull
        if client_servers_files_pull_query is not UNSET:
            field_dict["client_servers_files_pull_query"] = client_servers_files_pull_query
        if remote is not UNSET:
            field_dict["remote"] = remote
        if remote_sftp_auth is not UNSET:
            field_dict["remote_sftp_auth"] = remote_sftp_auth
        if remote_enroll is not UNSET:
            field_dict["remote_enroll"] = remote_enroll
        if exempt_ips is not UNSET:
            field_dict["exempt_ips"] = exempt_ips
        if exempt_api_keys is not UNSET:
            field_dict["exempt_api_keys"] = exempt_api_keys

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ratelimit_configuration import RatelimitConfiguration  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_auth_register(data: object) -> None | RatelimitConfiguration | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                auth_register_type_1 = RatelimitConfiguration.from_dict(data)

                return auth_register_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RatelimitConfiguration | Unset, data)

        auth_register = _parse_auth_register(d.pop("auth_register", UNSET))

        def _parse_auth_login(data: object) -> None | RatelimitConfiguration | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                auth_login_type_1 = RatelimitConfiguration.from_dict(data)

                return auth_login_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RatelimitConfiguration | Unset, data)

        auth_login = _parse_auth_login(d.pop("auth_login", UNSET))

        def _parse_auth_login_checkpoint(data: object) -> None | RatelimitConfiguration | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                auth_login_checkpoint_type_1 = RatelimitConfiguration.from_dict(data)

                return auth_login_checkpoint_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RatelimitConfiguration | Unset, data)

        auth_login_checkpoint = _parse_auth_login_checkpoint(d.pop("auth_login_checkpoint", UNSET))

        def _parse_auth_login_checkpoint_email(data: object) -> None | RatelimitConfiguration | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                auth_login_checkpoint_email_type_1 = RatelimitConfiguration.from_dict(data)

                return auth_login_checkpoint_email_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RatelimitConfiguration | Unset, data)

        auth_login_checkpoint_email = _parse_auth_login_checkpoint_email(d.pop("auth_login_checkpoint_email", UNSET))

        def _parse_auth_login_security_key(data: object) -> None | RatelimitConfiguration | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                auth_login_security_key_type_1 = RatelimitConfiguration.from_dict(data)

                return auth_login_security_key_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RatelimitConfiguration | Unset, data)

        auth_login_security_key = _parse_auth_login_security_key(d.pop("auth_login_security_key", UNSET))

        def _parse_auth_password_forgot(data: object) -> None | RatelimitConfiguration | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                auth_password_forgot_type_1 = RatelimitConfiguration.from_dict(data)

                return auth_password_forgot_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RatelimitConfiguration | Unset, data)

        auth_password_forgot = _parse_auth_password_forgot(d.pop("auth_password_forgot", UNSET))

        def _parse_auth_password_reset(data: object) -> None | RatelimitConfiguration | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                auth_password_reset_type_1 = RatelimitConfiguration.from_dict(data)

                return auth_password_reset_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RatelimitConfiguration | Unset, data)

        auth_password_reset = _parse_auth_password_reset(d.pop("auth_password_reset", UNSET))

        def _parse_auth_email_verification(data: object) -> None | RatelimitConfiguration | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                auth_email_verification_type_1 = RatelimitConfiguration.from_dict(data)

                return auth_email_verification_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RatelimitConfiguration | Unset, data)

        auth_email_verification = _parse_auth_email_verification(d.pop("auth_email_verification", UNSET))

        def _parse_client(data: object) -> None | RatelimitConfiguration | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                client_type_1 = RatelimitConfiguration.from_dict(data)

                return client_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RatelimitConfiguration | Unset, data)

        client = _parse_client(d.pop("client", UNSET))

        def _parse_client_account_email_resend_verification(data: object) -> None | RatelimitConfiguration | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                client_account_email_resend_verification_type_1 = RatelimitConfiguration.from_dict(data)

                return client_account_email_resend_verification_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RatelimitConfiguration | Unset, data)

        client_account_email_resend_verification = _parse_client_account_email_resend_verification(
            d.pop("client_account_email_resend_verification", UNSET)
        )

        def _parse_client_servers_backups_create(data: object) -> None | RatelimitConfiguration | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                client_servers_backups_create_type_1 = RatelimitConfiguration.from_dict(data)

                return client_servers_backups_create_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RatelimitConfiguration | Unset, data)

        client_servers_backups_create = _parse_client_servers_backups_create(
            d.pop("client_servers_backups_create", UNSET)
        )

        def _parse_client_servers_files_pull(data: object) -> None | RatelimitConfiguration | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                client_servers_files_pull_type_1 = RatelimitConfiguration.from_dict(data)

                return client_servers_files_pull_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RatelimitConfiguration | Unset, data)

        client_servers_files_pull = _parse_client_servers_files_pull(d.pop("client_servers_files_pull", UNSET))

        def _parse_client_servers_files_pull_query(data: object) -> None | RatelimitConfiguration | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                client_servers_files_pull_query_type_1 = RatelimitConfiguration.from_dict(data)

                return client_servers_files_pull_query_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RatelimitConfiguration | Unset, data)

        client_servers_files_pull_query = _parse_client_servers_files_pull_query(
            d.pop("client_servers_files_pull_query", UNSET)
        )

        def _parse_remote(data: object) -> None | RatelimitConfiguration | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                remote_type_1 = RatelimitConfiguration.from_dict(data)

                return remote_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RatelimitConfiguration | Unset, data)

        remote = _parse_remote(d.pop("remote", UNSET))

        def _parse_remote_sftp_auth(data: object) -> None | RatelimitConfiguration | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                remote_sftp_auth_type_1 = RatelimitConfiguration.from_dict(data)

                return remote_sftp_auth_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RatelimitConfiguration | Unset, data)

        remote_sftp_auth = _parse_remote_sftp_auth(d.pop("remote_sftp_auth", UNSET))

        def _parse_remote_enroll(data: object) -> None | RatelimitConfiguration | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                remote_enroll_type_1 = RatelimitConfiguration.from_dict(data)

                return remote_enroll_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RatelimitConfiguration | Unset, data)

        remote_enroll = _parse_remote_enroll(d.pop("remote_enroll", UNSET))

        def _parse_exempt_ips(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exempt_ips_type_0 = cast(list[str], data)

                return exempt_ips_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        exempt_ips = _parse_exempt_ips(d.pop("exempt_ips", UNSET))

        def _parse_exempt_api_keys(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exempt_api_keys_type_0 = []
                _exempt_api_keys_type_0 = data
                for exempt_api_keys_type_0_item_data in _exempt_api_keys_type_0:
                    exempt_api_keys_type_0_item = UUID(exempt_api_keys_type_0_item_data)

                    exempt_api_keys_type_0.append(exempt_api_keys_type_0_item)

                return exempt_api_keys_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        exempt_api_keys = _parse_exempt_api_keys(d.pop("exempt_api_keys", UNSET))

        put_api_admin_settings_body_ratelimits_type_1 = cls(
            auth_register=auth_register,
            auth_login=auth_login,
            auth_login_checkpoint=auth_login_checkpoint,
            auth_login_checkpoint_email=auth_login_checkpoint_email,
            auth_login_security_key=auth_login_security_key,
            auth_password_forgot=auth_password_forgot,
            auth_password_reset=auth_password_reset,
            auth_email_verification=auth_email_verification,
            client=client,
            client_account_email_resend_verification=client_account_email_resend_verification,
            client_servers_backups_create=client_servers_backups_create,
            client_servers_files_pull=client_servers_files_pull,
            client_servers_files_pull_query=client_servers_files_pull_query,
            remote=remote,
            remote_sftp_auth=remote_sftp_auth,
            remote_enroll=remote_enroll,
            exempt_ips=exempt_ips,
            exempt_api_keys=exempt_api_keys,
        )

        put_api_admin_settings_body_ratelimits_type_1.additional_properties = d
        return put_api_admin_settings_body_ratelimits_type_1

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
