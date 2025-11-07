from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="信用情報種別813RankingItem")


@_attrs_define
class 信用情報種別813RankingItem:
    """
    Attributes:
        no (int | Unset): 順位<br>※ランキング内で同じ順位が返却される場合があります（10位が2件など）
        symbol (str | Unset): 銘柄コード
        symbol_name (str | Unset): 銘柄名称
        sell_rapid_payment_percentage (float | Unset): 売残（千株）
        sell_last_week_ratio (float | Unset): 売残前週比
        buy_rapid_payment_percentage (float | Unset): 買残（千株）
        buy_last_week_ratio (float | Unset): 買残前週比
        ratio (float | Unset): 倍率
        exchange_name (str | Unset): 市場名
        category_name (str | Unset): 業種名
    """

    no: int | Unset = UNSET
    symbol: str | Unset = UNSET
    symbol_name: str | Unset = UNSET
    sell_rapid_payment_percentage: float | Unset = UNSET
    sell_last_week_ratio: float | Unset = UNSET
    buy_rapid_payment_percentage: float | Unset = UNSET
    buy_last_week_ratio: float | Unset = UNSET
    ratio: float | Unset = UNSET
    exchange_name: str | Unset = UNSET
    category_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        no = self.no

        symbol = self.symbol

        symbol_name = self.symbol_name

        sell_rapid_payment_percentage = self.sell_rapid_payment_percentage

        sell_last_week_ratio = self.sell_last_week_ratio

        buy_rapid_payment_percentage = self.buy_rapid_payment_percentage

        buy_last_week_ratio = self.buy_last_week_ratio

        ratio = self.ratio

        exchange_name = self.exchange_name

        category_name = self.category_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if no is not UNSET:
            field_dict["No"] = no
        if symbol is not UNSET:
            field_dict["Symbol"] = symbol
        if symbol_name is not UNSET:
            field_dict["SymbolName"] = symbol_name
        if sell_rapid_payment_percentage is not UNSET:
            field_dict["SellRapidPaymentPercentage"] = sell_rapid_payment_percentage
        if sell_last_week_ratio is not UNSET:
            field_dict["SellLastWeekRatio"] = sell_last_week_ratio
        if buy_rapid_payment_percentage is not UNSET:
            field_dict["BuyRapidPaymentPercentage"] = buy_rapid_payment_percentage
        if buy_last_week_ratio is not UNSET:
            field_dict["BuyLastWeekRatio"] = buy_last_week_ratio
        if ratio is not UNSET:
            field_dict["Ratio"] = ratio
        if exchange_name is not UNSET:
            field_dict["ExchangeName"] = exchange_name
        if category_name is not UNSET:
            field_dict["CategoryName"] = category_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        no = d.pop("No", UNSET)

        symbol = d.pop("Symbol", UNSET)

        symbol_name = d.pop("SymbolName", UNSET)

        sell_rapid_payment_percentage = d.pop("SellRapidPaymentPercentage", UNSET)

        sell_last_week_ratio = d.pop("SellLastWeekRatio", UNSET)

        buy_rapid_payment_percentage = d.pop("BuyRapidPaymentPercentage", UNSET)

        buy_last_week_ratio = d.pop("BuyLastWeekRatio", UNSET)

        ratio = d.pop("Ratio", UNSET)

        exchange_name = d.pop("ExchangeName", UNSET)

        category_name = d.pop("CategoryName", UNSET)

        信用情報種別813_ranking_item = cls(
            no=no,
            symbol=symbol,
            symbol_name=symbol_name,
            sell_rapid_payment_percentage=sell_rapid_payment_percentage,
            sell_last_week_ratio=sell_last_week_ratio,
            buy_rapid_payment_percentage=buy_rapid_payment_percentage,
            buy_last_week_ratio=buy_last_week_ratio,
            ratio=ratio,
            exchange_name=exchange_name,
            category_name=category_name,
        )

        信用情報種別813_ranking_item.additional_properties = d
        return 信用情報種別813_ranking_item

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
