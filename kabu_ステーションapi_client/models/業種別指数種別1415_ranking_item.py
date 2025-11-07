from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="業種別指数種別1415RankingItem")


@_attrs_define
class 業種別指数種別1415RankingItem:
    """
    Attributes:
        no (int | Unset): 順位<br>※ランキング内で同じ順位が返却される場合があります（10位が2件など）
        trend (str | Unset): トレンド
            <table>
              <thead>
                  <tr>
                      <th>定義値</th>
                      <th>内容</th>
                  </tr>
              </thead>
              <tbody>
                  <tr>
                      <td>0</td>
                      <td>対象データ無し</td>
                  </tr>
                  <tr>
                      <td>1</td>
                      <td>過去10営業日より20位以上上昇</td>
                  </tr>
                  <tr>
                      <td>2</td>
                      <td>過去10営業日より1～19位上昇</td>
                  </tr>
                  <tr>
                      <td>3</td>
                      <td>過去10営業日と変わらず</td>
                  </tr>
                  <tr>
                      <td>4</td>
                      <td>過去10営業日より1～19位下落</td>
                  </tr>
                  <tr>
                      <td>5</td>
                      <td>過去10営業日より20位以上下落</td>
                  </tr>
              </tbody>
            </table>
        average_ranking (float | Unset): 平均順位<br>※100位以下は「999」となります
        category (str | Unset): 業種コード
        category_name (str | Unset): 業種名
        current_price (float | Unset): 現在値
        change_ratio (float | Unset): 前日比
        current_price_time (str | Unset): 時刻<br>HH:mm<br>※日付は返しません
        change_percentage (float | Unset): 騰落率（%）
    """

    no: int | Unset = UNSET
    trend: str | Unset = UNSET
    average_ranking: float | Unset = UNSET
    category: str | Unset = UNSET
    category_name: str | Unset = UNSET
    current_price: float | Unset = UNSET
    change_ratio: float | Unset = UNSET
    current_price_time: str | Unset = UNSET
    change_percentage: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        no = self.no

        trend = self.trend

        average_ranking = self.average_ranking

        category = self.category

        category_name = self.category_name

        current_price = self.current_price

        change_ratio = self.change_ratio

        current_price_time = self.current_price_time

        change_percentage = self.change_percentage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if no is not UNSET:
            field_dict["No"] = no
        if trend is not UNSET:
            field_dict["Trend"] = trend
        if average_ranking is not UNSET:
            field_dict["AverageRanking"] = average_ranking
        if category is not UNSET:
            field_dict["Category"] = category
        if category_name is not UNSET:
            field_dict["CategoryName"] = category_name
        if current_price is not UNSET:
            field_dict["CurrentPrice"] = current_price
        if change_ratio is not UNSET:
            field_dict["ChangeRatio"] = change_ratio
        if current_price_time is not UNSET:
            field_dict["CurrentPriceTime"] = current_price_time
        if change_percentage is not UNSET:
            field_dict["ChangePercentage"] = change_percentage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        no = d.pop("No", UNSET)

        trend = d.pop("Trend", UNSET)

        average_ranking = d.pop("AverageRanking", UNSET)

        category = d.pop("Category", UNSET)

        category_name = d.pop("CategoryName", UNSET)

        current_price = d.pop("CurrentPrice", UNSET)

        change_ratio = d.pop("ChangeRatio", UNSET)

        current_price_time = d.pop("CurrentPriceTime", UNSET)

        change_percentage = d.pop("ChangePercentage", UNSET)

        業種別指数種別1415_ranking_item = cls(
            no=no,
            trend=trend,
            average_ranking=average_ranking,
            category=category,
            category_name=category_name,
            current_price=current_price,
            change_ratio=change_ratio,
            current_price_time=current_price_time,
            change_percentage=change_percentage,
        )

        業種別指数種別1415_ranking_item.additional_properties = d
        return 業種別指数種別1415_ranking_item

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
