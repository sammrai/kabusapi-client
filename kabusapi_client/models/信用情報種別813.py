from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.信用情報種別813_ranking_item import 信用情報種別813RankingItem


T = TypeVar("T", bound="信用情報種別813")


@_attrs_define
class 信用情報種別813:
    """
    Example:
        {'Type': 7, 'ExchangeDivision': 'ALL', 'Ranking': [{'No': 1, 'Symbol': '7888', 'SymbolName': '三光合成',
            'SellRapidPaymentPercentage': 1410.9, 'SellLastWeekRatio': 1343.4, 'BuyRapidPaymentPercentage': 1108.2,
            'BuyLastWeekRatio': 832.7, 'Ratio': 0.79, 'ExchangeName': '東証プ', 'CategoryName': '化学'}, {'No': 2, 'Symbol':
            '4564', 'SymbolName': 'ＯＴＳ', 'SellRapidPaymentPercentage': 6588, 'SellLastWeekRatio': 1315.7,
            'BuyRapidPaymentPercentage': 22180.5, 'BuyLastWeekRatio': -223.4, 'Ratio': 3.37, 'ExchangeName': '東証グ',
            'CategoryName': '医薬品'}]}

    Attributes:
        type_ (str | Unset): 種別
        exchange_division (str | Unset): 市場
        ranking (list[信用情報種別813RankingItem] | Unset): ランキング
    """

    type_: str | Unset = UNSET
    exchange_division: str | Unset = UNSET
    ranking: list[信用情報種別813RankingItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        exchange_division = self.exchange_division

        ranking: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ranking, Unset):
            ranking = []
            for ranking_item_data in self.ranking:
                ranking_item = ranking_item_data.to_dict()
                ranking.append(ranking_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["Type"] = type_
        if exchange_division is not UNSET:
            field_dict["ExchangeDivision"] = exchange_division
        if ranking is not UNSET:
            field_dict["Ranking"] = ranking

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.信用情報種別813_ranking_item import 信用情報種別813RankingItem

        d = dict(src_dict)
        type_ = d.pop("Type", UNSET)

        exchange_division = d.pop("ExchangeDivision", UNSET)

        _ranking = d.pop("Ranking", UNSET)
        ranking: list[信用情報種別813RankingItem] | Unset = UNSET
        if _ranking is not UNSET:
            ranking = []
            for ranking_item_data in _ranking:
                ranking_item = 信用情報種別813RankingItem.from_dict(ranking_item_data)

                ranking.append(ranking_item)

        信用情報種別813 = cls(
            type_=type_,
            exchange_division=exchange_division,
            ranking=ranking,
        )

        信用情報種別813.additional_properties = d
        return 信用情報種別813

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
