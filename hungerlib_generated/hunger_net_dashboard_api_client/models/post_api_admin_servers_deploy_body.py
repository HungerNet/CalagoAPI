from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.admin_api_server_limits import AdminApiServerLimits
    from ..models.api_server_feature_limits import ApiServerFeatureLimits
    from ..models.post_api_admin_servers_deploy_body_deployment import PostApiAdminServersDeployBodyDeployment
    from ..models.post_api_admin_servers_deploy_body_labels import PostApiAdminServersDeployBodyLabels
    from ..models.post_api_admin_servers_deploy_body_variables_item import PostApiAdminServersDeployBodyVariablesItem


T = TypeVar("T", bound="PostApiAdminServersDeployBody")


@_attrs_define
class PostApiAdminServersDeployBody:
    """
    Attributes:
        deployment (PostApiAdminServersDeployBodyDeployment):
        owner_uuid (UUID):
        egg_uuid (UUID):
        start_on_completion (bool):
        skip_installer (bool):
        name (str):
        limits (AdminApiServerLimits):
        pinned_cpus (list[int]):
        startup (str):
        image (str):
        hugepages_passthrough_enabled (bool):
        kvm_passthrough_enabled (bool):
        feature_limits (ApiServerFeatureLimits):
        variables (list[PostApiAdminServersDeployBodyVariablesItem]):
        backup_configuration_uuid (None | Unset | UUID):
        allocation_uuid (None | Unset | UUID):
        allocation_uuids (list[UUID] | None | Unset):
        external_id (None | str | Unset):
        description (None | str | Unset):
        labels (PostApiAdminServersDeployBodyLabels | Unset):
        timezone (None | str | Unset):
    """

    deployment: PostApiAdminServersDeployBodyDeployment
    owner_uuid: UUID
    egg_uuid: UUID
    start_on_completion: bool
    skip_installer: bool
    name: str
    limits: AdminApiServerLimits
    pinned_cpus: list[int]
    startup: str
    image: str
    hugepages_passthrough_enabled: bool
    kvm_passthrough_enabled: bool
    feature_limits: ApiServerFeatureLimits
    variables: list[PostApiAdminServersDeployBodyVariablesItem]
    backup_configuration_uuid: None | Unset | UUID = UNSET
    allocation_uuid: None | Unset | UUID = UNSET
    allocation_uuids: list[UUID] | None | Unset = UNSET
    external_id: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    labels: PostApiAdminServersDeployBodyLabels | Unset = UNSET
    timezone: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deployment = self.deployment.to_dict()

        owner_uuid = str(self.owner_uuid)

        egg_uuid = str(self.egg_uuid)

        start_on_completion = self.start_on_completion

        skip_installer = self.skip_installer

        name = self.name

        limits = self.limits.to_dict()

        pinned_cpus = self.pinned_cpus

        startup = self.startup

        image = self.image

        hugepages_passthrough_enabled = self.hugepages_passthrough_enabled

        kvm_passthrough_enabled = self.kvm_passthrough_enabled

        feature_limits = self.feature_limits.to_dict()

        variables = []
        for variables_item_data in self.variables:
            variables_item = variables_item_data.to_dict()
            variables.append(variables_item)

        backup_configuration_uuid: None | str | Unset
        if isinstance(self.backup_configuration_uuid, Unset):
            backup_configuration_uuid = UNSET
        elif isinstance(self.backup_configuration_uuid, UUID):
            backup_configuration_uuid = str(self.backup_configuration_uuid)
        else:
            backup_configuration_uuid = self.backup_configuration_uuid

        allocation_uuid: None | str | Unset
        if isinstance(self.allocation_uuid, Unset):
            allocation_uuid = UNSET
        elif isinstance(self.allocation_uuid, UUID):
            allocation_uuid = str(self.allocation_uuid)
        else:
            allocation_uuid = self.allocation_uuid

        allocation_uuids: list[str] | None | Unset
        if isinstance(self.allocation_uuids, Unset):
            allocation_uuids = UNSET
        elif isinstance(self.allocation_uuids, list):
            allocation_uuids = []
            for allocation_uuids_type_0_item_data in self.allocation_uuids:
                allocation_uuids_type_0_item = str(allocation_uuids_type_0_item_data)
                allocation_uuids.append(allocation_uuids_type_0_item)

        else:
            allocation_uuids = self.allocation_uuids

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        timezone: None | str | Unset
        if isinstance(self.timezone, Unset):
            timezone = UNSET
        else:
            timezone = self.timezone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deployment": deployment,
                "owner_uuid": owner_uuid,
                "egg_uuid": egg_uuid,
                "start_on_completion": start_on_completion,
                "skip_installer": skip_installer,
                "name": name,
                "limits": limits,
                "pinned_cpus": pinned_cpus,
                "startup": startup,
                "image": image,
                "hugepages_passthrough_enabled": hugepages_passthrough_enabled,
                "kvm_passthrough_enabled": kvm_passthrough_enabled,
                "feature_limits": feature_limits,
                "variables": variables,
            }
        )
        if backup_configuration_uuid is not UNSET:
            field_dict["backup_configuration_uuid"] = backup_configuration_uuid
        if allocation_uuid is not UNSET:
            field_dict["allocation_uuid"] = allocation_uuid
        if allocation_uuids is not UNSET:
            field_dict["allocation_uuids"] = allocation_uuids
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if description is not UNSET:
            field_dict["description"] = description
        if labels is not UNSET:
            field_dict["labels"] = labels
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.admin_api_server_limits import AdminApiServerLimits  # noqa: PLC0415
        from ..models.api_server_feature_limits import ApiServerFeatureLimits  # noqa: PLC0415
        from ..models.post_api_admin_servers_deploy_body_deployment import PostApiAdminServersDeployBodyDeployment  # noqa: PLC0415
        from ..models.post_api_admin_servers_deploy_body_labels import PostApiAdminServersDeployBodyLabels  # noqa: PLC0415
        from ..models.post_api_admin_servers_deploy_body_variables_item import (
            PostApiAdminServersDeployBodyVariablesItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        deployment = PostApiAdminServersDeployBodyDeployment.from_dict(d.pop("deployment"))

        owner_uuid = UUID(d.pop("owner_uuid"))

        egg_uuid = UUID(d.pop("egg_uuid"))

        start_on_completion = d.pop("start_on_completion")

        skip_installer = d.pop("skip_installer")

        name = d.pop("name")

        limits = AdminApiServerLimits.from_dict(d.pop("limits"))

        pinned_cpus = cast(list[int], d.pop("pinned_cpus"))

        startup = d.pop("startup")

        image = d.pop("image")

        hugepages_passthrough_enabled = d.pop("hugepages_passthrough_enabled")

        kvm_passthrough_enabled = d.pop("kvm_passthrough_enabled")

        feature_limits = ApiServerFeatureLimits.from_dict(d.pop("feature_limits"))

        variables = []
        _variables = d.pop("variables")
        for variables_item_data in _variables:
            variables_item = PostApiAdminServersDeployBodyVariablesItem.from_dict(variables_item_data)

            variables.append(variables_item)

        def _parse_backup_configuration_uuid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                backup_configuration_uuid_type_0 = UUID(data)

                return backup_configuration_uuid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        backup_configuration_uuid = _parse_backup_configuration_uuid(d.pop("backup_configuration_uuid", UNSET))

        def _parse_allocation_uuid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                allocation_uuid_type_0 = UUID(data)

                return allocation_uuid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        allocation_uuid = _parse_allocation_uuid(d.pop("allocation_uuid", UNSET))

        def _parse_allocation_uuids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allocation_uuids_type_0 = []
                _allocation_uuids_type_0 = data
                for allocation_uuids_type_0_item_data in _allocation_uuids_type_0:
                    allocation_uuids_type_0_item = UUID(allocation_uuids_type_0_item_data)

                    allocation_uuids_type_0.append(allocation_uuids_type_0_item)

                return allocation_uuids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        allocation_uuids = _parse_allocation_uuids(d.pop("allocation_uuids", UNSET))

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _labels = d.pop("labels", UNSET)
        labels: PostApiAdminServersDeployBodyLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = PostApiAdminServersDeployBodyLabels.from_dict(_labels)

        def _parse_timezone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        timezone = _parse_timezone(d.pop("timezone", UNSET))

        post_api_admin_servers_deploy_body = cls(
            deployment=deployment,
            owner_uuid=owner_uuid,
            egg_uuid=egg_uuid,
            start_on_completion=start_on_completion,
            skip_installer=skip_installer,
            name=name,
            limits=limits,
            pinned_cpus=pinned_cpus,
            startup=startup,
            image=image,
            hugepages_passthrough_enabled=hugepages_passthrough_enabled,
            kvm_passthrough_enabled=kvm_passthrough_enabled,
            feature_limits=feature_limits,
            variables=variables,
            backup_configuration_uuid=backup_configuration_uuid,
            allocation_uuid=allocation_uuid,
            allocation_uuids=allocation_uuids,
            external_id=external_id,
            description=description,
            labels=labels,
            timezone=timezone,
        )

        post_api_admin_servers_deploy_body.additional_properties = d
        return post_api_admin_servers_deploy_body

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
