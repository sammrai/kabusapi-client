from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="株価情報種別5RankingItem")


@_attrs_define
class 株価情報種別5RankingItem:
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
        symbol (str | Unset): 銘柄コード
        symbol_name (str | Unset): 銘柄名称
        current_price (float | Unset): 現在値
        change_ratio (float | Unset): 前日比
        tick_count (int | Unset): TICK回数
        up_count (int | Unset): UP
        down_count (int | Unset): DOWN
        change_percentage (float | Unset): 騰落率（%）
        trading_volume (float | Unset): 売買高<br>売買高を千株単位で表示する<br>※百株の位を四捨五入
        turnover (float | Unset): 売買代金<br>売買代金を百万円単位で表示する<br>※十万円の位を四捨五入
        exchange_name (str | Unset): 市場名
        category_name (str | Unset): 業種名
    """

    no: int | Unset = UNSET
    trend: str | Unset = UNSET
    average_ranking: float | Unset = UNSET
    symbol: str | Unset = UNSET
    symbol_name: str | Unset = UNSET
    current_price: float | Unset = UNSET
    change_ratio: float | Unset = UNSET
    tick_count: int | Unset = UNSET
    up_count: int | Unset = UNSET
    down_count: int | Unset = UNSET
    change_percentage: float | Unset = UNSET
    trading_volume: float | Unset = UNSET
    turnover: float | Unset = UNSET
    exchange_name: str | Unset = UNSET
    category_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        no = self.no

        trend = self.trend

        average_ranking = self.average_ranking

        symbol = self.symbol

        symbol_name = self.symbol_name

        current_price = self.current_price

        change_ratio = self.change_ratio

        tick_count = self.tick_count

        up_count = self.up_count

        down_count = self.down_count

        change_percentage = self.change_percentage

        trading_volume = self.trading_volume

        turnover = self.turnover

        exchange_name = self.exchange_name

        category_name = self.category_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if no is not UNSET:
            field_dict["No"] = no
        if trend is not UNSET:
            field_dict["Trend"] = trend
        if average_ranking is not UNSET:
            field_dict["AverageRanking"] = average_ranking
        if symbol is not UNSET:
            field_dict["Symbol"] = symbol
        if symbol_name is not UNSET:
            field_dict["SymbolName"] = symbol_name
        if current_price is not UNSET:
            field_dict["CurrentPrice"] = current_price
        if change_ratio is not UNSET:
            field_dict["ChangeRatio"] = change_ratio
        if tick_count is not UNSET:
            field_dict["TickCount"] = tick_count
        if up_count is not UNSET:
            field_dict["UpCount"] = up_count
        if down_count is not UNSET:
            field_dict["DownCount"] = down_count
        if change_percentage is not UNSET:
            field_dict["ChangePercentage"] = change_percentage
        if trading_volume is not UNSET:
            field_dict["TradingVolume"] = trading_volume
        if turnover is not UNSET:
            field_dict["Turnover"] = turnover
        if exchange_name is not UNSET:
            field_dict["ExchangeName"] = exchange_name
        if category_name is not UNSET:
            field_dict["CategoryName"] = category_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        no = d.pop("No", UNSET)

        trend = d.pop("Trend", UNSET)

        average_ranking = d.pop("AverageRanking", UNSET)

        symbol = d.pop("Symbol", UNSET)

        symbol_name = d.pop("SymbolName", UNSET)

        current_price = d.pop("CurrentPrice", UNSET)

        change_ratio = d.pop("ChangeRatio", UNSET)

        tick_count = d.pop("TickCount", UNSET)

        up_count = d.pop("UpCount", UNSET)

        down_count = d.pop("DownCount", UNSET)

        change_percentage = d.pop("ChangePercentage", UNSET)

        trading_volume = d.pop("TradingVolume", UNSET)

        turnover = d.pop("Turnover", UNSET)

        exchange_name = d.pop("ExchangeName", UNSET)

        category_name = d.pop("CategoryName", UNSET)

        株価情報種別5_ranking_item = cls(
            no=no,
            trend=trend,
            average_ranking=average_ranking,
            symbol=symbol,
            symbol_name=symbol_name,
            current_price=current_price,
            change_ratio=change_ratio,
            tick_count=tick_count,
            up_count=up_count,
            down_count=down_count,
            change_percentage=change_percentage,
            trading_volume=trading_volume,
            turnover=turnover,
            exchange_name=exchange_name,
            category_name=category_name,
        )

        株価情報種別5_ranking_item.additional_properties = d
        return 株価情報種別5_ranking_item

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
