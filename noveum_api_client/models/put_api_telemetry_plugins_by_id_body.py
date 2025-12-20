from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.put_api_telemetry_plugins_by_id_body_environment import PutApiTelemetryPluginsByIdBodyEnvironment
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_api_telemetry_plugins_by_id_body_config import PutApiTelemetryPluginsByIdBodyConfig


T = TypeVar("T", bound="PutApiTelemetryPluginsByIdBody")


@_attrs_define
class PutApiTelemetryPluginsByIdBody:
    """
    Attributes:
        name (str | Unset):
        type_ (Literal['clickhouse'] | Unset):
        config (PutApiTelemetryPluginsByIdBodyConfig | Unset):
        enabled (bool | Unset):  Default: True.
        is_default (bool | Unset):  Default: False.
        environment (PutApiTelemetryPluginsByIdBodyEnvironment | Unset):  Default:
            PutApiTelemetryPluginsByIdBodyEnvironment.PRODUCTION.
    """

    name: str | Unset = UNSET
    type_: Literal["clickhouse"] | Unset = UNSET
    config: PutApiTelemetryPluginsByIdBodyConfig | Unset = UNSET
    enabled: bool | Unset = True
    is_default: bool | Unset = False
    environment: PutApiTelemetryPluginsByIdBodyEnvironment | Unset = (
        PutApiTelemetryPluginsByIdBodyEnvironment.PRODUCTION
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        enabled = self.enabled

        is_default = self.is_default

        environment: str | Unset = UNSET
        if not isinstance(self.environment, Unset):
            environment = self.environment.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if config is not UNSET:
            field_dict["config"] = config
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if environment is not UNSET:
            field_dict["environment"] = environment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_api_telemetry_plugins_by_id_body_config import PutApiTelemetryPluginsByIdBodyConfig

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        type_ = cast(Literal["clickhouse"] | Unset, d.pop("type", UNSET))
        if type_ != "clickhouse" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'clickhouse', got '{type_}'")

        _config = d.pop("config", UNSET)
        config: PutApiTelemetryPluginsByIdBodyConfig | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = PutApiTelemetryPluginsByIdBodyConfig.from_dict(_config)

        enabled = d.pop("enabled", UNSET)

        is_default = d.pop("isDefault", UNSET)

        _environment = d.pop("environment", UNSET)
        environment: PutApiTelemetryPluginsByIdBodyEnvironment | Unset
        if isinstance(_environment, Unset):
            environment = UNSET
        else:
            environment = PutApiTelemetryPluginsByIdBodyEnvironment(_environment)

        put_api_telemetry_plugins_by_id_body = cls(
            name=name,
            type_=type_,
            config=config,
            enabled=enabled,
            is_default=is_default,
            environment=environment,
        )

        put_api_telemetry_plugins_by_id_body.additional_properties = d
        return put_api_telemetry_plugins_by_id_body

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
