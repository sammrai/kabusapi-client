from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.time_and_sales_response_trading_price_item import TimeAndSalesResponseTradingPriceItem


T = TypeVar("T", bound="TimeAndSalesResponse")


@_attrs_define
class TimeAndSalesResponse:
    """
    Example:
        {'Symbol': '8306', 'Exchange': '1,', 'TradingPriceCount': 3, 'TradingPrice': [{'Time':
            '2026-06-17T10:57:56+09:00', 'Volume': 2876.0, 'Price': 1901.0}, {'Time': '2026-06-17T10:57:57+09:00', 'Volume':
            2900.0, 'Price': 1910.0}, {'Time': '2026-06-17T10:57:58+09:00', 'Volume': 2920.0, 'Price': 1902.0}]}

    Attributes:
        symbol (str | Unset): 銘柄コード
        exchange (int | Unset): 市場コード<br>※株式・先物・オプション銘柄の場合のみ
            <table>
              <thead>
                  <tr>
                      <th>定義値</th>
                      <th>説明</th>
                  </tr>
              </thead>
              <tbody>
                  <tr>
                      <td>1</td>
                      <td>東証</td>
                  </tr>
                  <tr>
                      <td>3</td>
                      <td>名証</td>
                  </tr>
                  <tr>
                      <td>5</td>
                      <td>福証</td>
                  </tr>
                  <tr>
                      <td>6</td>
                      <td>札証</td>
                  </tr>
                  <tr>
                      <td>2</td>
                      <td>日通し</td>
                  </tr>
                  <tr>
                      <td>23</td>
                      <td>日中</td>
                  </tr>
                  <tr>
                      <td>24</td>
                      <td>夜間</td>
                  </tr>
              </tbody>
            </table>
        trading_price_count (int | Unset): 歩み値合計件数
        trading_price (list[TimeAndSalesResponseTradingPriceItem] | Unset): 歩み値リスト
    """

    symbol: str | Unset = UNSET
    exchange: int | Unset = UNSET
    trading_price_count: int | Unset = UNSET
    trading_price: list[TimeAndSalesResponseTradingPriceItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        symbol = self.symbol

        exchange = self.exchange

        trading_price_count = self.trading_price_count

        trading_price: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.trading_price, Unset):
            trading_price = []
            for trading_price_item_data in self.trading_price:
                trading_price_item = trading_price_item_data.to_dict()
                trading_price.append(trading_price_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if symbol is not UNSET:
            field_dict["Symbol"] = symbol
        if exchange is not UNSET:
            field_dict["Exchange"] = exchange
        if trading_price_count is not UNSET:
            field_dict["TradingPriceCount"] = trading_price_count
        if trading_price is not UNSET:
            field_dict["TradingPrice"] = trading_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.time_and_sales_response_trading_price_item import (
            TimeAndSalesResponseTradingPriceItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        symbol = d.pop("Symbol", UNSET)

        exchange = d.pop("Exchange", UNSET)

        trading_price_count = d.pop("TradingPriceCount", UNSET)

        _trading_price = d.pop("TradingPrice", UNSET)
        trading_price: list[TimeAndSalesResponseTradingPriceItem] | Unset = UNSET
        if _trading_price is not UNSET:
            trading_price = []
            for trading_price_item_data in _trading_price:
                trading_price_item = TimeAndSalesResponseTradingPriceItem.from_dict(trading_price_item_data)

                trading_price.append(trading_price_item)

        time_and_sales_response = cls(
            symbol=symbol,
            exchange=exchange,
            trading_price_count=trading_price_count,
            trading_price=trading_price,
        )

        time_and_sales_response.additional_properties = d
        return time_and_sales_response

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
