from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_retention_rule import BackupRetentionRule
from ..models.server_backup_retention_state import ServerBackupRetentionState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_retention import BackupRetention


T = TypeVar("T", bound="ServerBackupRetentionStatus")


@_attrs_define
class ServerBackupRetentionStatus:
    """
    Attributes:
        state (ServerBackupRetentionState):
        retention (BackupRetention):
        rules (list[BackupRetentionRule]):
        rule (BackupRetentionRule | None | Unset):
        expires (datetime.datetime | None | Unset):
    """

    state: ServerBackupRetentionState
    retention: BackupRetention
    rules: list[BackupRetentionRule]
    rule: BackupRetentionRule | None | Unset = UNSET
    expires: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state.value

        retention = self.retention.to_dict()

        rules = []
        for rules_item_data in self.rules:
            rules_item = rules_item_data.value
            rules.append(rules_item)

        rule: None | str | Unset
        if isinstance(self.rule, Unset):
            rule = UNSET
        elif isinstance(self.rule, BackupRetentionRule):
            rule = self.rule.value
        else:
            rule = self.rule

        expires: None | str | Unset
        if isinstance(self.expires, Unset):
            expires = UNSET
        elif isinstance(self.expires, datetime.datetime):
            expires = self.expires.isoformat()
        else:
            expires = self.expires

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
                "retention": retention,
                "rules": rules,
            }
        )
        if rule is not UNSET:
            field_dict["rule"] = rule
        if expires is not UNSET:
            field_dict["expires"] = expires

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_retention import BackupRetention  # noqa: PLC0415

        d = dict(src_dict)
        state = ServerBackupRetentionState(d.pop("state"))

        retention = BackupRetention.from_dict(d.pop("retention"))

        rules = []
        _rules = d.pop("rules")
        for rules_item_data in _rules:
            rules_item = BackupRetentionRule(rules_item_data)

            rules.append(rules_item)

        def _parse_rule(data: object) -> BackupRetentionRule | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rule_type_1 = BackupRetentionRule(data)

                return rule_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BackupRetentionRule | None | Unset, data)

        rule = _parse_rule(d.pop("rule", UNSET))

        def _parse_expires(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_type_0 = datetime.datetime.fromisoformat(data)

                return expires_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires = _parse_expires(d.pop("expires", UNSET))

        server_backup_retention_status = cls(
            state=state,
            retention=retention,
            rules=rules,
            rule=rule,
            expires=expires,
        )

        server_backup_retention_status.additional_properties = d
        return server_backup_retention_status

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
