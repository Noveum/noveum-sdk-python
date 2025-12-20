from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_api_payments_purchases_response_200_item_type import GetApiPaymentsPurchasesResponse200ItemType

T = TypeVar("T", bound="GetApiPaymentsPurchasesResponse200Item")


@_attrs_define
class GetApiPaymentsPurchasesResponse200Item:
    """
    Attributes:
        type_ (GetApiPaymentsPurchasesResponse200ItemType):
        id (str):
        organization_id (None | str):
        user_id (None | str):
        customer_id (str):
        subscription_id (None | str):
        product_id (str):
        status (None | str):
        created_at (str):
        updated_at (str):
    """

    type_: GetApiPaymentsPurchasesResponse200ItemType
    id: str
    organization_id: None | str
    user_id: None | str
    customer_id: str
    subscription_id: None | str
    product_id: str
    status: None | str
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        id = self.id

        organization_id: None | str
        organization_id = self.organization_id

        user_id: None | str
        user_id = self.user_id

        customer_id = self.customer_id

        subscription_id: None | str
        subscription_id = self.subscription_id

        product_id = self.product_id

        status: None | str
        status = self.status

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "id": id,
                "organizationId": organization_id,
                "userId": user_id,
                "customerId": customer_id,
                "subscriptionId": subscription_id,
                "productId": product_id,
                "status": status,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = GetApiPaymentsPurchasesResponse200ItemType(d.pop("type"))

        id = d.pop("id")

        def _parse_organization_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        organization_id = _parse_organization_id(d.pop("organizationId"))

        def _parse_user_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        user_id = _parse_user_id(d.pop("userId"))

        customer_id = d.pop("customerId")

        def _parse_subscription_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        subscription_id = _parse_subscription_id(d.pop("subscriptionId"))

        product_id = d.pop("productId")

        def _parse_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status = _parse_status(d.pop("status"))

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        get_api_payments_purchases_response_200_item = cls(
            type_=type_,
            id=id,
            organization_id=organization_id,
            user_id=user_id,
            customer_id=customer_id,
            subscription_id=subscription_id,
            product_id=product_id,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
        )

        get_api_payments_purchases_response_200_item.additional_properties = d
        return get_api_payments_purchases_response_200_item

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
