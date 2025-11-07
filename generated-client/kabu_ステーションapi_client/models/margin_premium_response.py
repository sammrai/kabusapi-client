from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.margin_premium_response_day_trade import MarginPremiumResponseDayTrade
    from ..models.margin_premium_response_general_margin import MarginPremiumResponseGeneralMargin


T = TypeVar("T", bound="MarginPremiumResponse")


@_attrs_define
class MarginPremiumResponse:
    """
    Example:
        {'Symbol': '9433', 'GeneralMargin': {'MarginPremiumType': None, 'MarginPremium': None, 'UpperMarginPremium':
            None, 'LowerMarginPremium': None, 'TickMarginPremium': None}, 'DayTrade': {'MarginPremiumType': 2,
            'MarginPremium': 0.55, 'UpperMarginPremium': 1, 'LowerMarginPremium': 0.3, 'TickMarginPremium': 0.01}}

    Attributes:
        symbol (str | Unset): 銘柄コード
        general_margin (MarginPremiumResponseGeneralMargin | Unset): 一般信用（長期）
        day_trade (MarginPremiumResponseDayTrade | Unset): 一般信用（デイトレ）
    """

    symbol: str | Unset = UNSET
    general_margin: MarginPremiumResponseGeneralMargin | Unset = UNSET
    day_trade: MarginPremiumResponseDayTrade | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        symbol = self.symbol

        general_margin: dict[str, Any] | Unset = UNSET
        if not isinstance(self.general_margin, Unset):
            general_margin = self.general_margin.to_dict()

        day_trade: dict[str, Any] | Unset = UNSET
        if not isinstance(self.day_trade, Unset):
            day_trade = self.day_trade.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if symbol is not UNSET:
            field_dict["Symbol"] = symbol
        if general_margin is not UNSET:
            field_dict["GeneralMargin"] = general_margin
        if day_trade is not UNSET:
            field_dict["DayTrade"] = day_trade

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.margin_premium_response_day_trade import MarginPremiumResponseDayTrade
        from ..models.margin_premium_response_general_margin import MarginPremiumResponseGeneralMargin

        d = dict(src_dict)
        symbol = d.pop("Symbol", UNSET)

        _general_margin = d.pop("GeneralMargin", UNSET)
        general_margin: MarginPremiumResponseGeneralMargin | Unset
        if isinstance(_general_margin, Unset):
            general_margin = UNSET
        else:
            general_margin = MarginPremiumResponseGeneralMargin.from_dict(_general_margin)

        _day_trade = d.pop("DayTrade", UNSET)
        day_trade: MarginPremiumResponseDayTrade | Unset
        if isinstance(_day_trade, Unset):
            day_trade = UNSET
        else:
            day_trade = MarginPremiumResponseDayTrade.from_dict(_day_trade)

        margin_premium_response = cls(
            symbol=symbol,
            general_margin=general_margin,
            day_trade=day_trade,
        )

        margin_premium_response.additional_properties = d
        return margin_premium_response

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
