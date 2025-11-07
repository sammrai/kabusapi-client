from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="BoardSuccessBuy1")


@_attrs_define
class BoardSuccessBuy1:
    """買気配数量1本目

    Attributes:
        time (datetime.datetime | Unset): 時刻<br>※株式銘柄の場合のみ
        sign (str | Unset): 気配フラグ<br>※株式・先物・オプション銘柄の場合のみ
            <table>
              <thead>
                  <tr>
                      <th>定義値</th>
                      <th>説明</th>
                  </tr>
              </thead>
              <tbody>
                  <tr>
                      <td>0000</td>
                      <td>事象なし</td>
                  </tr>
                  <tr>
                      <td>0101</td>
                      <td>一般気配</td>
                  </tr>
                  <tr>
                      <td>0102</td>
                      <td>特別気配</td>
                  </tr>
                  <tr>
                      <td>0103</td>
                      <td>注意気配</td>
                  </tr>
                  <tr>
                      <td>0107</td>
                      <td>寄前気配</td>
                  </tr>
                  <tr>
                      <td>0108</td>
                      <td>停止前特別気配</td>
                  </tr>
                  <tr>
                      <td>0109</td>
                      <td>引け後気配</td>
                  </tr>
                  <tr>
                      <td>0116</td>
                      <td>寄前気配約定成立ポイントなし</td>
                  </tr>
                  <tr>
                      <td>0117</td>
                      <td>寄前気配約定成立ポイントあり</td>
                  </tr>
                  <tr>
                      <td>0118</td>
                      <td>連続約定気配</td>
                  </tr>
                  <tr>
                      <td>0119</td>
                      <td>停止前の連続約定気配</td>
                  </tr>
                  <tr>
                      <td>0120</td>
                      <td>買い上がり売り下がり中</td>
                  </tr>
              </tbody>
            </table>
        price (float | Unset): 値段<br>※株式・先物・オプション銘柄の場合のみ
        qty (float | Unset): 数量<br>※株式・先物・オプション銘柄の場合のみ
    """

    time: datetime.datetime | Unset = UNSET
    sign: str | Unset = UNSET
    price: float | Unset = UNSET
    qty: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time: str | Unset = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        sign = self.sign

        price = self.price

        qty = self.qty

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["Time"] = time
        if sign is not UNSET:
            field_dict["Sign"] = sign
        if price is not UNSET:
            field_dict["Price"] = price
        if qty is not UNSET:
            field_dict["Qty"] = qty

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _time = d.pop("Time", UNSET)
        time: datetime.datetime | Unset
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = isoparse(_time)

        sign = d.pop("Sign", UNSET)

        price = d.pop("Price", UNSET)

        qty = d.pop("Qty", UNSET)

        board_success_buy_1 = cls(
            time=time,
            sign=sign,
            price=price,
            qty=qty,
        )

        board_success_buy_1.additional_properties = d
        return board_success_buy_1

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
