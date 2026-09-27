from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeAndSalesResponseTradingPriceItem")


@_attrs_define
class TimeAndSalesResponseTradingPriceItem:
    """
    Attributes:
        time (str | Unset): 出来時刻
        volume (int | Unset): 出来高
        price (int | Unset): 出来値
    """

    time: str | Unset = UNSET
    volume: int | Unset = UNSET
    price: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        volume = self.volume

        price = self.price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["Time"] = time
        if volume is not UNSET:
            field_dict["Volume"] = volume
        if price is not UNSET:
            field_dict["Price"] = price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        time = d.pop("Time", UNSET)

        volume = d.pop("Volume", UNSET)

        price = d.pop("Price", UNSET)

        time_and_sales_response_trading_price_item = cls(
            time=time,
            volume=volume,
            price=price,
        )

        time_and_sales_response_trading_price_item.additional_properties = d
        return time_and_sales_response_trading_price_item

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
