from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.業種別指数種別1415_ranking_item import 業種別指数種別1415RankingItem


T = TypeVar("T", bound="業種別指数種別1415")


@_attrs_define
class 業種別指数種別1415:
    """
    Example:
        {'Type': 7, 'ExchangeDivision': 'ALL', 'Ranking': [{'No': 1, 'Trend': '2', 'AverageRanking': 15, 'Category':
            345, 'CategoryName': 'IS 情報・通信', 'CurrentPrice': 4796.67, 'ChangeRatio': 130.81, 'CurrentPriceTime': '15:00',
            'ChangePercentage': 2.8}, {'No': 2, 'Trend': 2, 'AverageRanking': 19, 'Category': 321, 'CategoryName': 'IS 水産',
            'CurrentPrice': 431.45, 'ChangeRatio': 3.98, 'CurrentPriceTime': '15:00', 'ChangePercentage': 0.93}]}

    Attributes:
        type_ (str | Unset): 種別<br> ※業種別値上がり率、業種別値下がり率の場合、市場は「null」になります
        exchange_division (str | Unset): 市場
        ranking (list[業種別指数種別1415RankingItem] | Unset): ランキング
    """

    type_: str | Unset = UNSET
    exchange_division: str | Unset = UNSET
    ranking: list[業種別指数種別1415RankingItem] | Unset = UNSET
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
        from ..models.業種別指数種別1415_ranking_item import 業種別指数種別1415RankingItem

        d = dict(src_dict)
        type_ = d.pop("Type", UNSET)

        exchange_division = d.pop("ExchangeDivision", UNSET)

        _ranking = d.pop("Ranking", UNSET)
        ranking: list[業種別指数種別1415RankingItem] | Unset = UNSET
        if _ranking is not UNSET:
            ranking = []
            for ranking_item_data in _ranking:
                ranking_item = 業種別指数種別1415RankingItem.from_dict(ranking_item_data)

                ranking.append(ranking_item)

        業種別指数種別1415 = cls(
            type_=type_,
            exchange_division=exchange_division,
            ranking=ranking,
        )

        業種別指数種別1415.additional_properties = d
        return 業種別指数種別1415

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
