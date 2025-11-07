from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExchangeResponse")


@_attrs_define
class ExchangeResponse:
    """
    Example:
        {'Symbol': 'USD/JPY', 'BidPrice': 105.502, 'Spread': 0.2, 'AskPrice': 105.504, 'Change': -0.055, 'Time':
            '16:10:45'}

    Attributes:
        symbol (str | Unset): 通貨
        bid_price (float | Unset): BID
        spread (float | Unset): SP
        ask_price (float | Unset): ASK
        change (float | Unset): 前日比
        time (str | Unset): 時刻 <br>※HH:mm:ss形式
    """

    symbol: str | Unset = UNSET
    bid_price: float | Unset = UNSET
    spread: float | Unset = UNSET
    ask_price: float | Unset = UNSET
    change: float | Unset = UNSET
    time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        symbol = self.symbol

        bid_price = self.bid_price

        spread = self.spread

        ask_price = self.ask_price

        change = self.change

        time = self.time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if symbol is not UNSET:
            field_dict["Symbol"] = symbol
        if bid_price is not UNSET:
            field_dict["BidPrice"] = bid_price
        if spread is not UNSET:
            field_dict["Spread"] = spread
        if ask_price is not UNSET:
            field_dict["AskPrice"] = ask_price
        if change is not UNSET:
            field_dict["Change"] = change
        if time is not UNSET:
            field_dict["Time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        symbol = d.pop("Symbol", UNSET)

        bid_price = d.pop("BidPrice", UNSET)

        spread = d.pop("Spread", UNSET)

        ask_price = d.pop("AskPrice", UNSET)

        change = d.pop("Change", UNSET)

        time = d.pop("Time", UNSET)

        exchange_response = cls(
            symbol=symbol,
            bid_price=bid_price,
            spread=spread,
            ask_price=ask_price,
            change=change,
            time=time,
        )

        exchange_response.additional_properties = d
        return exchange_response

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
