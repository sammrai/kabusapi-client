from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.positions_deriv import PositionsDeriv
    from ..models.request_send_order_deriv_future_reverse_limit_order import (
        RequestSendOrderDerivFutureReverseLimitOrder,
    )


T = TypeVar("T", bound="RequestSendOrderDerivFuture")


@_attrs_define
class RequestSendOrderDerivFuture:
    """
    Example:
        {'Symbol': '165120019', 'Exchange': 23, 'TradeType': 2, 'TimeInForce': 2, 'Side': '1', 'Qty': 1,
            'ClosePositions': [{'HoldID': 'E20200903xxxxx', 'Qty': 1}], 'FrontOrderType': 30, 'ExpireDay': 20200903,
            'ReverseLimitOrder': {'TriggerPrice': 100, 'UnderOver': 1, 'AfterHitOrderType': 1, 'AfterHitPrice': 0}}

    Attributes:
        symbol (str): 銘柄コード<br>※取引最終日に「先物銘柄コード取得」でDerivMonthに0（直近限月）を指定した場合、日中・夜間の時間帯に関わらず、取引最終日を迎える限月の銘柄コードを返します。取引最終日を
            迎える銘柄の取引は日中取引をもって終了となりますので、ご注意ください。 Example: 165120019.
        exchange (int): 市場コード <table> <thead> <tr> <th>定義値</th> <th>説明</th> </tr> </thead> <tbody> <tr> <td>2</td>
            <td>日通し</td> </tr> <tr> <td>23</td> <td>日中</td> </tr> <tr> <td>24</td> <td>夜間</td> </tr> <tr> <td>32</td>
            <td>SOR日通し</td> </tr> <tr> <td>33</td> <td>SOR日中</td> </tr> <tr> <td>34</td> <td>SOR夜間</td> </tr> </tbody>
            </table>
            SOR日中、SOR夜間、SOR日通しは一部銘柄のみ対象となります。<br> SOR対象銘柄は以下をご参照ください。 <table> <thead> <tr> <th>先物SOR取扱銘柄</th> <th>有効限月</th>
            </tr> </thead> <tbody> <tr> <td>日経225先物ラージ</td> <td>直近2限月</td> </tr> <tr> <td>日経225先物ミニ</td> <td>直近4限月</td>
            </tr> <tr> <td>TOPIX先物ラージ</td> <td>直近2限月</td> </tr> <tr> <td>TOPIX先物ミニ </td> <td>直近3限月</td> </tr> <tr>
            <td>東証マザーズ指数先物</td> <td>直近2限月</td> </tr> <tr> <td>JPX日経400先物</td> <td>直近2限月</td> </tr> <tr> <td>NYダウ先物</td>
            <td>直近2限月</td> </tr> </tbody> </table>
        trade_type (int): 取引区分
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
                      <td>新規</td>
                  </tr>
                  <tr>
                      <td>2</td>
                      <td>返済</td>
                  </tr>
              </tbody>
            </table>
        time_in_force (int): 有効期間条件
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
                      <td>FAS</td>
                  </tr>
                  <tr>
                      <td>2</td>
                      <td>FAK</td>
                  </tr>
                  <tr>
                      <td>3</td>
                      <td>FOK</td>
                  </tr>
              </tbody>
            </table>

            ※執行条件(FrontOrderType)、有効期限条件(TimeInForce)、市場コード(Exchange)で選択できる組み合わせは下表のようになります。<br>

            <br>■日中、夜間、日通し対応表
            <table>
              <thead>
                <tr>
                  <th rowspan="2">執行条件</th>
                  <th rowspan="2">有効<br>期間条件</th>
                  <th colspan="3">市場コード</th>
                </tr>
                <tr>
                  <th>日中</th>
                  <th>夜間</th>
                  <th>日通し</th>
                </tr>
              </thead>

              <tbody>
                <tr>
                  <td>指値</td>
                  <td>FAS</td>
                  <td>●</td>
                  <td>●</td>
                  <td>●</td>
                </tr>
                <tr>
                  <td>指値</td>
                  <td>FAK</td>
                  <td>●</td>
                  <td>●</td>
                  <td>-</td>
                </tr>
                <tr>
                  <td>指値</td>
                  <td>FOK</td>
                  <td>●</td>
                  <td>●</td>
                  <td>-</td>
                </tr>
                <tr>
                  <td>成行</td>
                  <td>FAK</td>
                  <td>●</td>
                  <td>●</td>
                  <td>-</td>
                </tr>
                <tr>
                  <td>成行</td>
                  <td>FOK</td>
                  <td>●</td>
                  <td>●</td>
                  <td>-</td>
                </tr>
                <tr>
                  <td>逆指値（指値）</td>
                  <td>FAK</td>
                  <td>●</td>
                  <td>●</td>
                  <td>●</td>
                </tr>
                <tr>
                  <td>逆指値（成行）</td>
                  <td>FAK</td>
                  <td>●</td>
                  <td>●</td>
                  <td>-</td>
                </tr>
                <tr>
                  <td>引成</td>
                  <td>FAK</td>
                  <td>●</td>
                  <td>●</td>
                  <td>-</td>
                </tr>
                <tr>
                  <td>引指</td>
                  <td>FAS</td>
                  <td>●</td>
                  <td>●</td>
                  <td>-</td>
                </tr>
              </tbody>
            </table>

            <br>■SOR日中、SOR夜間、SOR日通し対応表
            <table>
              <thead>
                <tr>
                  <th rowspan="2">執行条件</th>
                  <th rowspan="2">有効<br>期間条件</th>
                  <th colspan="3">市場コード</th>
                </tr>
                <tr>
                  <th>SOR日中</th>
                  <th>SOR夜間</th>
                  <th>SOR日通し</th>
                </tr>
              </thead>

              <tbody>
                <tr>
                  <td>指値</td>
                  <td>FAS</td>
                  <td>●</td>
                  <td>●</td>
                  <td>●</td>
                </tr>
                <tr>
                  <td>指値</td>
                  <td>FAK</td>
                  <td>●</td>
                  <td>●</td>
                  <td>-</td>
                </tr>
                <tr>
                  <td>指値</td>
                  <td>FOK</td>
                  <td>●</td>
                  <td>●</td>
                  <td>-</td>
                </tr>
                <tr>
                  <td>成行</td>
                  <td>FAK</td>
                  <td>●</td>
                  <td>●</td>
                  <td>-</td>
                </tr>
                <tr>
                  <td>成行</td>
                  <td>FOK</td>
                  <td>●</td>
                  <td>●</td>
                  <td>-</td>
                </tr>
                <tr>
                  <td>逆指値（指値）</td>
                  <td>FAK</td>
                  <td>●</td>
                  <td>●</td>
                  <td>●</td>
                </tr>
                <tr>
                  <td>逆指値（成行）</td>
                  <td>FAK</td>
                  <td>●</td>
                  <td>●</td>
                  <td>-</td>
                </tr>
                <tr>
                  <td>引成</td>
                  <td>FAK</td>
                  <td>-</td>
                  <td>-</td>
                  <td>-</td>
                </tr>
                <tr>
                  <td>引指</td>
                  <td>FAS</td>
                  <td>-</td>
                  <td>-</td>
                  <td>-</td>
                </tr>
              </tbody>
            </table>
        side (str): 売買区分
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
                      <td>売</td>
                  </tr>
                  <tr>
                      <td>2</td>
                      <td>買</td>
                  </tr>
              </tbody>
            </table>
        qty (int): 注文数量
        front_order_type (int): 執行条件
            <table>
              <thead>
                  <tr>
                      <th>定義値</th>
                      <th>説明</th>
                      <th>”Price”の指定</th>
                  </tr>
              </thead>
              <tbody>
                  <tr>
                      <td>18</td>
                      <td>引成（派生）<br>※TimeInForceは、「FAK」のみ有効</td>
                      <td>0</td>
                  </tr>
                  <tr>
                      <td>20</td>
                      <td>指値</td>
                      <td>発注したい金額</td>
                  </tr>
                  <tr>
                      <td>28</td>
                      <td>引指（派生）<br>※TimeInForceは、「FAS」のみ有効</td>
                      <td>発注したい金額</td>
                  </tr>
                  <tr>
                      <td>30</td>
                      <td>逆指値</td>
                      <td>指定なし<br>※AfterHitPriceで指定ください</td>
                  </tr>
                  <tr>
                      <td>120</td>
                      <td>成行（マーケットオーダー）</td>
                      <td>0</td>
                  </tr>
              </tbody>
            </table>
        price (float): 注文価格<br>※FrontOrderTypeで成行を指定した場合、0を指定する。<br>※詳細について、”FrontOrderType”をご確認ください。
        expire_day (int): 注文有効期限<br>
            yyyyMMdd形式。<br>
            「0」を指定すると、kabuステーション上の発注画面の「本日」に対応する日付として扱います。<br>
            「本日」は直近の注文可能日となり、以下のように設定されます。<br>
            その市場の引けまでの間 : 当日<br>
            その市場の引け後       : 翌取引所営業日<br>
            その市場の休前日       : 休日明けの取引所営業日<br>
            ※ 日替わりはkabuステーションが日付変更通知を受信したタイミングです。<br>
            ※ 日通しの場合、夜間取引の引け後に日付が更新されます。
        close_position_order (int | Unset):
            決済順序<br>※ClosePositionOrderとClosePositionsはどちらか一方のみ指定可能。<br>※ClosePositionOrderとClosePositionsを両方指定した場合、エラー。
            <table>
              <thead>
                  <tr>
                      <th>定義値</th>
                      <th>説明</th>
                  </tr>
              </thead>
              <tbody>
                  <tr>
                      <td>0</td>
                      <td>日付（古い順）、損益（高い順）</td>
                  </tr>
                  <tr>
                      <td>1</td>
                      <td>日付（古い順）、損益（低い順）</td>
                  </tr>
                  <tr>
                      <td>2</td>
                      <td>日付（新しい順）、損益（高い順）</td>
                  </tr>
                  <tr>
                      <td>3</td>
                      <td>日付（新しい順）、損益（低い順）</td>
                  </tr>
                  <tr>
                      <td>4</td>
                      <td>損益（高い順）、日付（古い順）</td>
                  </tr>
                  <tr>
                      <td>5</td>
                      <td>損益（高い順）、日付（新しい順）</td>
                  </tr>
                  <tr>
                      <td>6</td>
                      <td>損益（低い順）、日付（古い順）</td>
                  </tr>
                  <tr>
                      <td>7</td>
                      <td>損益（低い順）、日付（新しい順）</td>
                  </tr>
              </tbody>
            </table>
        close_positions (list[PositionsDeriv] | Unset):
            返済建玉指定<br>※ClosePositionOrderとClosePositionsはどちらか一方のみ指定可能。<br>※ClosePositionOrderとClosePositionsを両方指定した場合、エラー。
        reverse_limit_order (RequestSendOrderDerivFutureReverseLimitOrder | Unset): 逆指値条件<br>
            ※FrontOrderTypeで逆指値を指定した場合のみ必須。
    """

    symbol: str
    exchange: int
    trade_type: int
    time_in_force: int
    side: str
    qty: int
    front_order_type: int
    price: float
    expire_day: int
    close_position_order: int | Unset = UNSET
    close_positions: list[PositionsDeriv] | Unset = UNSET
    reverse_limit_order: RequestSendOrderDerivFutureReverseLimitOrder | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        symbol = self.symbol

        exchange = self.exchange

        trade_type = self.trade_type

        time_in_force = self.time_in_force

        side = self.side

        qty = self.qty

        front_order_type = self.front_order_type

        price = self.price

        expire_day = self.expire_day

        close_position_order = self.close_position_order

        close_positions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.close_positions, Unset):
            close_positions = []
            for close_positions_item_data in self.close_positions:
                close_positions_item = close_positions_item_data.to_dict()
                close_positions.append(close_positions_item)

        reverse_limit_order: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reverse_limit_order, Unset):
            reverse_limit_order = self.reverse_limit_order.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Symbol": symbol,
                "Exchange": exchange,
                "TradeType": trade_type,
                "TimeInForce": time_in_force,
                "Side": side,
                "Qty": qty,
                "FrontOrderType": front_order_type,
                "Price": price,
                "ExpireDay": expire_day,
            }
        )
        if close_position_order is not UNSET:
            field_dict["ClosePositionOrder"] = close_position_order
        if close_positions is not UNSET:
            field_dict["ClosePositions"] = close_positions
        if reverse_limit_order is not UNSET:
            field_dict["ReverseLimitOrder"] = reverse_limit_order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.positions_deriv import PositionsDeriv
        from ..models.request_send_order_deriv_future_reverse_limit_order import (
            RequestSendOrderDerivFutureReverseLimitOrder,
        )

        d = dict(src_dict)
        symbol = d.pop("Symbol")

        exchange = d.pop("Exchange")

        trade_type = d.pop("TradeType")

        time_in_force = d.pop("TimeInForce")

        side = d.pop("Side")

        qty = d.pop("Qty")

        front_order_type = d.pop("FrontOrderType")

        price = d.pop("Price")

        expire_day = d.pop("ExpireDay")

        close_position_order = d.pop("ClosePositionOrder", UNSET)

        _close_positions = d.pop("ClosePositions", UNSET)
        close_positions: list[PositionsDeriv] | Unset = UNSET
        if _close_positions is not UNSET:
            close_positions = []
            for close_positions_item_data in _close_positions:
                close_positions_item = PositionsDeriv.from_dict(close_positions_item_data)

                close_positions.append(close_positions_item)

        _reverse_limit_order = d.pop("ReverseLimitOrder", UNSET)
        reverse_limit_order: RequestSendOrderDerivFutureReverseLimitOrder | Unset
        if isinstance(_reverse_limit_order, Unset):
            reverse_limit_order = UNSET
        else:
            reverse_limit_order = RequestSendOrderDerivFutureReverseLimitOrder.from_dict(_reverse_limit_order)

        request_send_order_deriv_future = cls(
            symbol=symbol,
            exchange=exchange,
            trade_type=trade_type,
            time_in_force=time_in_force,
            side=side,
            qty=qty,
            front_order_type=front_order_type,
            price=price,
            expire_day=expire_day,
            close_position_order=close_position_order,
            close_positions=close_positions,
            reverse_limit_order=reverse_limit_order,
        )

        request_send_order_deriv_future.additional_properties = d
        return request_send_order_deriv_future

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
