from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_api_telemetry_plugins_body_environment import PostApiTelemetryPluginsBodyEnvironment
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_telemetry_plugins_body_config import PostApiTelemetryPluginsBodyConfig


T = TypeVar("T", bound="PostApiTelemetryPluginsBody")


@_attrs_define
class PostApiTelemetryPluginsBody:
    """
    Attributes:
        name (str):
        type_ (Literal['clickhouse']):
        config (PostApiTelemetryPluginsBodyConfig):
        enabled (bool | Unset):  Default: True.
        is_default (bool | Unset):  Default: False.
        environment (PostApiTelemetryPluginsBodyEnvironment | Unset):  Default:
            PostApiTelemetryPluginsBodyEnvironment.PRODUCTION.
    """

    name: str
    type_: Literal["clickhouse"]
    config: PostApiTelemetryPluginsBodyConfig
    enabled: bool | Unset = True
    is_default: bool | Unset = False
    environment: PostApiTelemetryPluginsBodyEnvironment | Unset = PostApiTelemetryPluginsBodyEnvironment.PRODUCTION
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        config = self.config.to_dict()

        enabled = self.enabled

        is_default = self.is_default

        environment: str | Unset = UNSET
        if not isinstance(self.environment, Unset):
            environment = self.environment.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
                "config": config,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if environment is not UNSET:
            field_dict["environment"] = environment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_telemetry_plugins_body_config import PostApiTelemetryPluginsBodyConfig

        d = dict(src_dict)
        name = d.pop("name")

        type_ = cast(Literal["clickhouse"], d.pop("type"))
        if type_ != "clickhouse":
            raise ValueError(f"type must match const 'clickhouse', got '{type_}'")

        config = PostApiTelemetryPluginsBodyConfig.from_dict(d.pop("config"))

        enabled = d.pop("enabled", UNSET)

        is_default = d.pop("isDefault", UNSET)

        _environment = d.pop("environment", UNSET)
        environment: PostApiTelemetryPluginsBodyEnvironment | Unset
        if isinstance(_environment, Unset):
            environment = UNSET
        else:
            environment = PostApiTelemetryPluginsBodyEnvironment(_environment)

        post_api_telemetry_plugins_body = cls(
            name=name,
            type_=type_,
            config=config,
            enabled=enabled,
            is_default=is_default,
            environment=environment,
        )

        post_api_telemetry_plugins_body.additional_properties = d
        return post_api_telemetry_plugins_body

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
