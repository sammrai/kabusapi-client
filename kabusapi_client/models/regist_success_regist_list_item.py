from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RegistSuccessRegistListItem")


@_attrs_define
class RegistSuccessRegistListItem:
    """
    Attributes:
        symbol (str | Unset): 銘柄コード Example: 9433.
        exchange (int | Unset): 市場コード
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
            </table> Example: 1.
    """

    symbol: str | Unset = UNSET
    exchange: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        symbol = self.symbol

        exchange = self.exchange

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if symbol is not UNSET:
            field_dict["Symbol"] = symbol
        if exchange is not UNSET:
            field_dict["Exchange"] = exchange

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        symbol = d.pop("Symbol", UNSET)

        exchange = d.pop("Exchange", UNSET)

        regist_success_regist_list_item = cls(
            symbol=symbol,
            exchange=exchange,
        )

        regist_success_regist_list_item.additional_properties = d
        return regist_success_regist_list_item

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
