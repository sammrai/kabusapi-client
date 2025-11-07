from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrdersSuccessDetailsItem")


@_attrs_define
class OrdersSuccessDetailsItem:
    """
    Attributes:
        seq_num (int | Unset): ※注文明細レコードの生成順序です。<br>※通番であるとは限りませんが、大小による順序は保たれています。
        id (str | Unset): 注文詳細番号
        rec_type (int | Unset): 明細種別
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
                      <td>受付</td>
                  </tr>
                  <tr>
                      <td>2</td>
                      <td>繰越</td>
                  </tr>
                  <tr>
                      <td>3</td>
                      <td>期限切れ</td>
                  </tr>
                  <tr>
                      <td>4</td>
                      <td>発注</td>
                  </tr>
                  <tr>
                      <td>5</td>
                      <td>訂正</td>
                  </tr>
                  <tr>
                      <td>6</td>
                      <td>取消</td>
                  </tr>
                  <tr>
                      <td>7</td>
                      <td>失効</td>
                  </tr>
                  <tr>
                      <td>8</td>
                      <td>約定</td>
                  </tr>
              </tbody>
            </table> Example: 1.
        exchange_id (str | Unset): 取引所番号
        state (int | Unset): 状態
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
                      <td>待機（発注待機）</td>
                  </tr>
                  <tr>
                      <td>2</td>
                      <td>処理中（発注送信中・訂正送信中・取消送信中）</td>
                  </tr>
                  <tr>
                      <td>3</td>
                      <td>処理済（発注済・訂正済・取消済・全約定・期限切れ）</td>
                  </tr>
                  <tr>
                      <td>4</td>
                      <td>エラー</td>
                  </tr>
                  <tr>
                      <td>5</td>
                      <td>削除済み</td>
                  </tr>
              </tbody>
            </table>
        transact_time (str | Unset): 処理時刻
        ord_type (int | Unset): 執行条件
            <table>
              <thead>
                  <tr>
                      <th>定義値</th>
                      <th>説明</th>
                  </tr>
              </thead>
              <tbody>
                  <tr>
                      <td>null</td>
                      <td>RecType=[6] 取消 の場合</td>
                  </tr>
                  <tr>
                      <td>0</td>
                      <td>RecType=[3] 期限切れ, [7] 失効, [8] 約定 の場合</td>
                  </tr>
                  <tr>
                      <td>1</td>
                      <td>ザラバ</td>
                  </tr>
                  <tr>
                      <td>2</td>
                      <td>寄り</td>
                  </tr>
                  <tr>
                      <td>3</td>
                      <td>引け</td>
                  </tr>
                  <tr>
                      <td>4</td>
                      <td>不成</td>
                  </tr>
                  <tr>
                      <td>5</td>
                      <td>対当指値</td>
                  </tr>
                  <tr>
                      <td>6</td>
                      <td>IOC</td>
                  </tr>
              </tbody>
            </table>
        price (float | Unset): 値段
        qty (float | Unset): 数量
        execution_id (str | Unset): 約定番号
        execution_day (datetime.datetime | Unset): 約定日時
        deliv_day (int | Unset): 受渡日
        commission (float | Unset): 手数料<br>※注文詳細の明細種別が約定（RecType=8)の場合に設定。
        commission_tax (float | Unset): 手数料消費税<br>※明細種別は約定（RecType=8）の場合にのみ表示されます。
    """

    seq_num: int | Unset = UNSET
    id: str | Unset = UNSET
    rec_type: int | Unset = UNSET
    exchange_id: str | Unset = UNSET
    state: int | Unset = UNSET
    transact_time: str | Unset = UNSET
    ord_type: int | Unset = UNSET
    price: float | Unset = UNSET
    qty: float | Unset = UNSET
    execution_id: str | Unset = UNSET
    execution_day: datetime.datetime | Unset = UNSET
    deliv_day: int | Unset = UNSET
    commission: float | Unset = UNSET
    commission_tax: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        seq_num = self.seq_num

        id = self.id

        rec_type = self.rec_type

        exchange_id = self.exchange_id

        state = self.state

        transact_time = self.transact_time

        ord_type = self.ord_type

        price = self.price

        qty = self.qty

        execution_id = self.execution_id

        execution_day: str | Unset = UNSET
        if not isinstance(self.execution_day, Unset):
            execution_day = self.execution_day.isoformat()

        deliv_day = self.deliv_day

        commission = self.commission

        commission_tax = self.commission_tax

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if seq_num is not UNSET:
            field_dict["SeqNum"] = seq_num
        if id is not UNSET:
            field_dict["ID"] = id
        if rec_type is not UNSET:
            field_dict["RecType"] = rec_type
        if exchange_id is not UNSET:
            field_dict["ExchangeID"] = exchange_id
        if state is not UNSET:
            field_dict["State"] = state
        if transact_time is not UNSET:
            field_dict["TransactTime"] = transact_time
        if ord_type is not UNSET:
            field_dict["OrdType"] = ord_type
        if price is not UNSET:
            field_dict["Price"] = price
        if qty is not UNSET:
            field_dict["Qty"] = qty
        if execution_id is not UNSET:
            field_dict["ExecutionID"] = execution_id
        if execution_day is not UNSET:
            field_dict["ExecutionDay"] = execution_day
        if deliv_day is not UNSET:
            field_dict["DelivDay"] = deliv_day
        if commission is not UNSET:
            field_dict["Commission"] = commission
        if commission_tax is not UNSET:
            field_dict["CommissionTax"] = commission_tax

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        seq_num = d.pop("SeqNum", UNSET)

        id = d.pop("ID", UNSET)

        rec_type = d.pop("RecType", UNSET)

        exchange_id = d.pop("ExchangeID", UNSET)

        state = d.pop("State", UNSET)

        transact_time = d.pop("TransactTime", UNSET)

        ord_type = d.pop("OrdType", UNSET)

        price = d.pop("Price", UNSET)

        qty = d.pop("Qty", UNSET)

        execution_id = d.pop("ExecutionID", UNSET)

        _execution_day = d.pop("ExecutionDay", UNSET)
        execution_day: datetime.datetime | Unset
        if isinstance(_execution_day, Unset):
            execution_day = UNSET
        else:
            execution_day = isoparse(_execution_day)

        deliv_day = d.pop("DelivDay", UNSET)

        commission = d.pop("Commission", UNSET)

        commission_tax = d.pop("CommissionTax", UNSET)

        orders_success_details_item = cls(
            seq_num=seq_num,
            id=id,
            rec_type=rec_type,
            exchange_id=exchange_id,
            state=state,
            transact_time=transact_time,
            ord_type=ord_type,
            price=price,
            qty=qty,
            execution_id=execution_id,
            execution_day=execution_day,
            deliv_day=deliv_day,
            commission=commission,
            commission_tax=commission_tax,
        )

        orders_success_details_item.additional_properties = d
        return orders_success_details_item

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
