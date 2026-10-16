from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ratelimit_configuration import RatelimitConfiguration


T = TypeVar("T", bound="GetApiAdminSettingsResponse200SettingsRatelimits")


@_attrs_define
class GetApiAdminSettingsResponse200SettingsRatelimits:
    """
    Attributes:
        auth_register (RatelimitConfiguration):
        auth_login (RatelimitConfiguration):
        auth_login_checkpoint (RatelimitConfiguration):
        auth_login_checkpoint_email (RatelimitConfiguration):
        auth_login_security_key (RatelimitConfiguration):
        auth_password_forgot (RatelimitConfiguration):
        auth_password_reset (RatelimitConfiguration):
        auth_email_verification (RatelimitConfiguration):
        client (RatelimitConfiguration):
        client_account_email_resend_verification (RatelimitConfiguration):
        client_servers_backups_create (RatelimitConfiguration):
        client_servers_files_pull (RatelimitConfiguration):
        client_servers_files_pull_query (RatelimitConfiguration):
        remote (RatelimitConfiguration):
        remote_sftp_auth (RatelimitConfiguration):
        remote_enroll (RatelimitConfiguration):
        exempt_ips (list[str]):
        exempt_api_keys (list[UUID]):
    """

    auth_register: RatelimitConfiguration
    auth_login: RatelimitConfiguration
    auth_login_checkpoint: RatelimitConfiguration
    auth_login_checkpoint_email: RatelimitConfiguration
    auth_login_security_key: RatelimitConfiguration
    auth_password_forgot: RatelimitConfiguration
    auth_password_reset: RatelimitConfiguration
    auth_email_verification: RatelimitConfiguration
    client: RatelimitConfiguration
    client_account_email_resend_verification: RatelimitConfiguration
    client_servers_backups_create: RatelimitConfiguration
    client_servers_files_pull: RatelimitConfiguration
    client_servers_files_pull_query: RatelimitConfiguration
    remote: RatelimitConfiguration
    remote_sftp_auth: RatelimitConfiguration
    remote_enroll: RatelimitConfiguration
    exempt_ips: list[str]
    exempt_api_keys: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_register = self.auth_register.to_dict()

        auth_login = self.auth_login.to_dict()

        auth_login_checkpoint = self.auth_login_checkpoint.to_dict()

        auth_login_checkpoint_email = self.auth_login_checkpoint_email.to_dict()

        auth_login_security_key = self.auth_login_security_key.to_dict()

        auth_password_forgot = self.auth_password_forgot.to_dict()

        auth_password_reset = self.auth_password_reset.to_dict()

        auth_email_verification = self.auth_email_verification.to_dict()

        client = self.client.to_dict()

        client_account_email_resend_verification = self.client_account_email_resend_verification.to_dict()

        client_servers_backups_create = self.client_servers_backups_create.to_dict()

        client_servers_files_pull = self.client_servers_files_pull.to_dict()

        client_servers_files_pull_query = self.client_servers_files_pull_query.to_dict()

        remote = self.remote.to_dict()

        remote_sftp_auth = self.remote_sftp_auth.to_dict()

        remote_enroll = self.remote_enroll.to_dict()

        exempt_ips = self.exempt_ips

        exempt_api_keys = []
        for exempt_api_keys_item_data in self.exempt_api_keys:
            exempt_api_keys_item = str(exempt_api_keys_item_data)
            exempt_api_keys.append(exempt_api_keys_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "auth_register": auth_register,
                "auth_login": auth_login,
                "auth_login_checkpoint": auth_login_checkpoint,
                "auth_login_checkpoint_email": auth_login_checkpoint_email,
                "auth_login_security_key": auth_login_security_key,
                "auth_password_forgot": auth_password_forgot,
                "auth_password_reset": auth_password_reset,
                "auth_email_verification": auth_email_verification,
                "client": client,
                "client_account_email_resend_verification": client_account_email_resend_verification,
                "client_servers_backups_create": client_servers_backups_create,
                "client_servers_files_pull": client_servers_files_pull,
                "client_servers_files_pull_query": client_servers_files_pull_query,
                "remote": remote,
                "remote_sftp_auth": remote_sftp_auth,
                "remote_enroll": remote_enroll,
                "exempt_ips": exempt_ips,
                "exempt_api_keys": exempt_api_keys,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ratelimit_configuration import RatelimitConfiguration  # noqa: PLC0415

        d = dict(src_dict)
        auth_register = RatelimitConfiguration.from_dict(d.pop("auth_register"))

        auth_login = RatelimitConfiguration.from_dict(d.pop("auth_login"))

        auth_login_checkpoint = RatelimitConfiguration.from_dict(d.pop("auth_login_checkpoint"))

        auth_login_checkpoint_email = RatelimitConfiguration.from_dict(d.pop("auth_login_checkpoint_email"))

        auth_login_security_key = RatelimitConfiguration.from_dict(d.pop("auth_login_security_key"))

        auth_password_forgot = RatelimitConfiguration.from_dict(d.pop("auth_password_forgot"))

        auth_password_reset = RatelimitConfiguration.from_dict(d.pop("auth_password_reset"))

        auth_email_verification = RatelimitConfiguration.from_dict(d.pop("auth_email_verification"))

        client = RatelimitConfiguration.from_dict(d.pop("client"))

        client_account_email_resend_verification = RatelimitConfiguration.from_dict(
            d.pop("client_account_email_resend_verification")
        )

        client_servers_backups_create = RatelimitConfiguration.from_dict(d.pop("client_servers_backups_create"))

        client_servers_files_pull = RatelimitConfiguration.from_dict(d.pop("client_servers_files_pull"))

        client_servers_files_pull_query = RatelimitConfiguration.from_dict(d.pop("client_servers_files_pull_query"))

        remote = RatelimitConfiguration.from_dict(d.pop("remote"))

        remote_sftp_auth = RatelimitConfiguration.from_dict(d.pop("remote_sftp_auth"))

        remote_enroll = RatelimitConfiguration.from_dict(d.pop("remote_enroll"))

        exempt_ips = cast(list[str], d.pop("exempt_ips"))

        exempt_api_keys = []
        _exempt_api_keys = d.pop("exempt_api_keys")
        for exempt_api_keys_item_data in _exempt_api_keys:
            exempt_api_keys_item = UUID(exempt_api_keys_item_data)

            exempt_api_keys.append(exempt_api_keys_item)

        get_api_admin_settings_response_200_settings_ratelimits = cls(
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

        get_api_admin_settings_response_200_settings_ratelimits.additional_properties = d
        return get_api_admin_settings_response_200_settings_ratelimits

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
