from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.株価情報種別5_ranking_item import 株価情報種別5RankingItem


T = TypeVar("T", bound="株価情報種別5")


@_attrs_define
class 株価情報種別5:
    """
    Example:
        {'Type': 5, 'ExchangeDivision': 'ALL', 'Ranking': [{'No': 1, 'Trend': '2', 'AverageRanking': 2, 'Symbol':
            '9984', 'SymbolName': 'ｿﾌﾄﾊﾞﾝｸG', 'CurrentPrice': 8306, 'ChangeRatio': 817, 'TickCount': 132907, 'UpCount':
            41144, 'DownCount': 40276, 'ChangePercentage': 10.9, 'TradingVolume': 68384.4, 'Turnover': 557485,
            'ExchangeName': '東証プ', 'CategoryName': '情報・通信業'}, {'No': 2, 'Trend': '1', 'AverageRanking': 999, 'Symbol':
            '6400', 'SymbolName': '不二精機', 'CurrentPrice': 1357, 'ChangeRatio': 4, 'TickCount': 42016, 'UpCount': 14735,
            'DownCount': 14698, 'ChangePercentage': 0.29, 'TradingVolume': 11803.4, 'Turnover': 17228.4096, 'ExchangeName':
            '東証ス', 'CategoryName': '機械'}]}

    Attributes:
        type_ (str | Unset): 種別
        exchange_division (str | Unset): 市場
        ranking (list[株価情報種別5RankingItem] | Unset): ランキング
    """

    type_: str | Unset = UNSET
    exchange_division: str | Unset = UNSET
    ranking: list[株価情報種別5RankingItem] | Unset = UNSET
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
        from ..models.株価情報種別5_ranking_item import 株価情報種別5RankingItem

        d = dict(src_dict)
        type_ = d.pop("Type", UNSET)

        exchange_division = d.pop("ExchangeDivision", UNSET)

        _ranking = d.pop("Ranking", UNSET)
        ranking: list[株価情報種別5RankingItem] | Unset = UNSET
        if _ranking is not UNSET:
            ranking = []
            for ranking_item_data in _ranking:
                ranking_item = 株価情報種別5RankingItem.from_dict(ranking_item_data)

                ranking.append(ranking_item)

        株価情報種別5 = cls(
            type_=type_,
            exchange_division=exchange_division,
            ranking=ranking,
        )

        株価情報種別5.additional_properties = d
        return 株価情報種別5

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
