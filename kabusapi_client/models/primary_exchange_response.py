from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PrimaryExchangeResponse")


@_attrs_define
class PrimaryExchangeResponse:
    """
    Example:
        {'Symbol': '2928', 'Exchange': 6}

    Attributes:
        symbol (str | Unset): 銘柄コード<br>※対象商品は、株式のみ
        primary_exchange (int | Unset): 優先市場
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
              </tbody>
            </table>
    """

    symbol: str | Unset = UNSET
    primary_exchange: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        symbol = self.symbol

        primary_exchange = self.primary_exchange

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if symbol is not UNSET:
            field_dict["Symbol"] = symbol
        if primary_exchange is not UNSET:
            field_dict["PrimaryExchange"] = primary_exchange

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        symbol = d.pop("Symbol", UNSET)

        primary_exchange = d.pop("PrimaryExchange", UNSET)

        primary_exchange_response = cls(
            symbol=symbol,
            primary_exchange=primary_exchange,
        )

        primary_exchange_response.additional_properties = d
        return primary_exchange_response

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
