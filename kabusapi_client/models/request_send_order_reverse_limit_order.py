from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RequestSendOrderReverseLimitOrder")


@_attrs_define
class RequestSendOrderReverseLimitOrder:
    """逆指値条件<br>
    ※FrontOrderTypeで逆指値を指定した場合のみ必須。

        Attributes:
            trigger_sec (int): トリガ銘柄<br>
                ※未設定の場合はエラーになります。
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
                      <td>発注銘柄</td>
                    </tr>
                    <tr>
                      <td>2</td>
                      <td>NK225指数</td>
                    </tr>
                    <tr>
                      <td>3</td>
                      <td>TOPIX指数</td>
                    </tr>
                  </tbody>
                </table>
            trigger_price (float): トリガ価格<br>
                ※未設定の場合はエラーになります。<br>
                ※数字以外が設定された場合はエラーになります。
            under_over (int): 以上／以下<br>
                ※未設定の場合はエラーになります。<br>
                ※1、2以外が指定された場合はエラーになります。
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
                      <td>以下</td>
                    </tr>
                    <tr>
                      <td>2</td>
                      <td>以上</td>
                    </tr>
                  </tbody>
                </table>
            after_hit_order_type (int): ヒット後執行条件<br>
                ※未設定の場合はエラーになります。<br>
                ※1、2、3以外が指定された場合はエラーになります。
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
                      <td>成行</td>
                    </tr>
                    <tr>
                      <td>2</td>
                      <td>指値</td>
                    </tr>
                    <tr>
                      <td>3</td>
                      <td>不成</td>
                    </tr>
                  </tbody>
                </table>
            after_hit_price (float): ヒット後注文価格<br>
                ※未設定の場合はエラーになります。<br>
                ※数字以外が設定された場合はエラーになります。<br><br>
                ヒット後執行条件に従い、下記のようにヒット後注文価格を設定してください。
                <table>
                  <thead>
                      <tr>
                          <th>ヒット後執行条件</th>
                          <th>設定価格</th>
                      </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>成行</td>
                      <td>0</td>
                    </tr>
                    <tr>
                      <td>指値</td>
                      <td>指値の単価</td>
                    </tr>
                    <tr>
                      <td>不成</td>
                      <td>不成の単価</td>
                    </tr>
                  </tbody>
                </table>
    """

    trigger_sec: int
    trigger_price: float
    under_over: int
    after_hit_order_type: int
    after_hit_price: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trigger_sec = self.trigger_sec

        trigger_price = self.trigger_price

        under_over = self.under_over

        after_hit_order_type = self.after_hit_order_type

        after_hit_price = self.after_hit_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "TriggerSec": trigger_sec,
                "TriggerPrice": trigger_price,
                "UnderOver": under_over,
                "AfterHitOrderType": after_hit_order_type,
                "AfterHitPrice": after_hit_price,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        trigger_sec = d.pop("TriggerSec")

        trigger_price = d.pop("TriggerPrice")

        under_over = d.pop("UnderOver")

        after_hit_order_type = d.pop("AfterHitOrderType")

        after_hit_price = d.pop("AfterHitPrice")

        request_send_order_reverse_limit_order = cls(
            trigger_sec=trigger_sec,
            trigger_price=trigger_price,
            under_over=under_over,
            after_hit_order_type=after_hit_order_type,
            after_hit_price=after_hit_price,
        )

        request_send_order_reverse_limit_order.additional_properties = d
        return request_send_order_reverse_limit_order

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
