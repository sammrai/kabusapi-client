from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.positions import Positions
    from ..models.request_send_order_reverse_limit_order import RequestSendOrderReverseLimitOrder


T = TypeVar("T", bound="RequestSendOrder")


@_attrs_define
class RequestSendOrder:
    """
    Example:
        {'Symbol': '9433', 'Exchange': 1, 'SecurityType': 1, 'Side': '1', 'CashMargin': 3, 'MarginTradeType': 3,
            'MarginPremiumUnit': 12.34, 'DelivType': 2, 'AccountType': 4, 'Qty': 500, 'ClosePositions': [{'HoldID':
            'E20200702xxxxx', 'Qty': 500}], 'FrontOrderType': 30, 'ExpireDay': 20200903, 'ReverseLimitOrder': {'TriggerSec':
            1, 'TriggerPrice': 40000, 'UnderOver': 2, 'AfterHitOrderType': 1, 'AfterHitPrice': 0}}

    Attributes:
        symbol (str): 銘柄コード
        exchange (int): 市場コード
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
                      <td>9</td>
                      <td>SOR</td>
                  </tr>
                  <tr>
                      <td>27</td>
                      <td>東証+</td>
                  </tr>
              </tbody>
            </table>
        security_type (int): 商品種別
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
                      <td>株式</td>
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
        cash_margin (int): 信用区分
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
                      <td>現物</td>
                  </tr>
                  <tr>
                      <td>2</td>
                      <td>新規</td>
                  </tr>
                  <tr>
                      <td>3</td>
                      <td>返済</td>
                  </tr>
              </tbody>
            </table>
        deliv_type (int): 受渡区分<br>※現物買は指定必須。<br>※現物売は「0(指定なし)」を設定<br>※信用新規は「0(指定なし)」を設定<br>※信用返済は指定必須
            <br>※auマネーコネクトが有効の場合にのみ、「3」を設定可能
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
                      <td>指定なし</td>
                  </tr>
                  <tr>
                      <td>2</td>
                      <td>お預り金</td>
                  </tr>
                  <tr>
                      <td>3</td>
                      <td>auマネーコネクト</td>
                  </tr>
              </tbody>
            </table>
        account_type (int): 口座種別
            <table>
              <thead>
                  <tr>
                      <th>定義値</th>
                      <th>説明</th>
                  </tr>
              </thead>
              <tbody>
                  <tr>
                      <td>2</td>
                      <td>一般</td>
                  </tr>
                  <tr>
                      <td>4</td>
                      <td>特定</td>
                  </tr>
                  <tr>
                      <td>12</td>
                      <td>法人</td>
                  </tr>
              </tbody>
            </table>
        qty (int): 注文数量<br>※信用一括返済の場合、返済したい合計数量を入力してください。
        front_order_type (int): 執行条件
            ※SOR以外は以下、全て指定可能です。
            <table>
              <thead>
                  <tr>
                      <th>定義値</th>
                      <th>説明</th>
                      <th>”Price"の指定</th>
                      <th>SORで発注可</th>
                  </tr>
              </thead>
              <tbody>
                  <tr>
                      <td>10</td>
                      <td>成行</td>
                      <td>0</td>
                      <td>〇</td>
                  </tr>
                  <tr>
                      <td>13</td>
                      <td>寄成（前場）</td>
                      <td>0</td>
                      <td>　</td>
                  </tr>
                  <tr>
                      <td>14</td>
                      <td>寄成（後場）</td>
                      <td>0</td>
                      <td>　</td>
                  </tr>
                  <tr>
                      <td>15</td>
                      <td>引成（前場）</td>
                      <td>0</td>
                      <td>　</td>
                  </tr>
                  <tr>
                      <td>16</td>
                      <td>引成（後場）</td>
                      <td>0</td>
                      <td>　</td>
                  </tr>
                  <tr>
                      <td>17</td>
                      <td>IOC成行</td>
                      <td>0</td>
                      <td>　</td>
                  </tr>
                  <tr>
                      <td>20</td>
                      <td>指値</td>
                      <td>発注したい金額</td>
                      <td>〇</td>
                  </tr>
                  <tr>
                      <td>21</td>
                      <td>寄指（前場）</td>
                      <td>発注したい金額</td>
                      <td>　</td>
                  </tr>
                  <tr>
                      <td>22</td>
                      <td>寄指（後場）</td>
                      <td>発注したい金額</td>
                      <td>　</td>
                  </tr>
                  <tr>
                      <td>23</td>
                      <td>引指（前場）</td>
                      <td>発注したい金額</td>
                      <td>　</td>
                  </tr>
                  <tr>
                      <td>24</td>
                      <td>引指（後場）</td>
                      <td>発注したい金額</td>
                      <td>　</td>
                  </tr>
                  <tr>
                      <td>25</td>
                      <td>不成（前場）</td>
                      <td>発注したい金額</td>
                      <td>　</td>
                  </tr>
                  <tr>
                      <td>26</td>
                      <td>不成（後場）</td>
                      <td>発注したい金額</td>
                      <td>　</td>
                  </tr>
                  <tr>
                      <td>27</td>
                      <td>IOC指値</td>
                      <td>発注したい金額</td>
                      <td>　</td>
                  </tr>
                  <tr>
                      <td>30</td>
                      <td>逆指値</td>
                      <td>指定なし<br>※AfterHitPriceで指定ください</td>
                      <td>〇</td>
                  </tr>
              </tbody>
            </table>
        price (float): 注文価格<br>※FrontOrderTypeで成行を指定した場合、0を指定する。<br>※詳細について、”FrontOrderType”をご確認ください。
        expire_day (int): 注文有効期限<br>
            yyyyMMdd形式。<br>
            「0」を指定すると、kabuステーション上の発注画面の「本日」に対応する日付として扱います。<br>
            「本日」は直近の注文可能日となり、以下のように設定されます。<br>
            引けまでの間 : 当日<br>
            引け後       : 翌取引所営業日<br>
            休前日       : 休日明けの取引所営業日<br>
            ※ 日替わりはkabuステーションが日付変更通知を受信したタイミングです。
        margin_trade_type (int | Unset): 信用取引区分<br>※現物取引の場合は指定不要。<br>※信用取引の場合、必須。
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
                      <td>制度信用</td>
                  </tr>
                  <tr>
                      <td>2</td>
                      <td>一般信用（長期）</td>
                  </tr>
                  <tr>
                      <td>3</td>
                      <td>一般信用（デイトレ）</td>
                  </tr>
              </tbody>
            </table>
        margin_premium_unit (float | Unset): １株あたりのプレミアム料(円)<br>
            ※プレミアム料の刻値は、プレミアム料取得APIのレスポンスにある"TickMarginPremium"にてご確認ください。<br>
            ※入札受付中(19:30～20:30)プレミアム料入札可能銘柄の場合、「MarginPremiumUnit」は必須となります。<br>
            ※入札受付中(19:30～20:30)のプレミアム料入札可能銘柄以外の場合は、「MarginPremiumUnit」の記載は無視されます。<br>
            ※入札受付中以外の時間帯では、「MarginPremiumUnit」の記載は無視されます。
        fund_type (str | Unset): 資産区分（預り区分）<br>※現物買は、指定必須。<br>※現物売は、「'  '」
            半角スペース2つを指定必須。<br>※信用新規と信用返済は、「11」を指定するか、または指定なしでも可。指定しない場合は「11」が自動的にセットされます。
            <table>
              <thead>
                  <tr>
                      <th>定義値</th>
                      <th>説明</th>
                  </tr>
              </thead>
              <tbody>
                  <tr>
                      <td>(半角スペース2つ)</td>
                      <td>現物売の場合</td>
                  </tr>
                  <tr>
                      <td>02</td>
                      <td>保護</td>
                  </tr>
                  <tr>
                      <td>AA</td>
                      <td>信用代用</td>
                  </tr>
                  <tr>
                      <td>11</td>
                      <td>信用取引</td>
                  </tr>
              </tbody>
            </table>
        close_position_order (int | Unset): 決済順序<br>※信用返済の場合、必須。<br>※ClosePositionOrderとClosePositionsはどちらか一方のみ指定可能。<br>
            ※ClosePositionOrderとClosePositionsを両方指定した場合、エラー。
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
        close_positions (list[Positions] | Unset): 返済建玉指定<br>※信用返済の場合、必須。<br>※ClosePositionOrderとClosePositionsはどちらか一方のみ
            指定可能。<br>※ClosePositionOrderとClosePositionsを両方指定した場合、エラー。<br>※信用一括返済の場合、各建玉IDと返済したい数量を入力してください。<br>※建玉IDは「E」から始ま
            る番号です。
        reverse_limit_order (RequestSendOrderReverseLimitOrder | Unset): 逆指値条件<br>
            ※FrontOrderTypeで逆指値を指定した場合のみ必須。
    """

    symbol: str
    exchange: int
    security_type: int
    side: str
    cash_margin: int
    deliv_type: int
    account_type: int
    qty: int
    front_order_type: int
    price: float
    expire_day: int
    margin_trade_type: int | Unset = UNSET
    margin_premium_unit: float | Unset = UNSET
    fund_type: str | Unset = UNSET
    close_position_order: int | Unset = UNSET
    close_positions: list[Positions] | Unset = UNSET
    reverse_limit_order: RequestSendOrderReverseLimitOrder | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        symbol = self.symbol

        exchange = self.exchange

        security_type = self.security_type

        side = self.side

        cash_margin = self.cash_margin

        deliv_type = self.deliv_type

        account_type = self.account_type

        qty = self.qty

        front_order_type = self.front_order_type

        price = self.price

        expire_day = self.expire_day

        margin_trade_type = self.margin_trade_type

        margin_premium_unit = self.margin_premium_unit

        fund_type = self.fund_type

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
                "SecurityType": security_type,
                "Side": side,
                "CashMargin": cash_margin,
                "DelivType": deliv_type,
                "AccountType": account_type,
                "Qty": qty,
                "FrontOrderType": front_order_type,
                "Price": price,
                "ExpireDay": expire_day,
            }
        )
        if margin_trade_type is not UNSET:
            field_dict["MarginTradeType"] = margin_trade_type
        if margin_premium_unit is not UNSET:
            field_dict["MarginPremiumUnit"] = margin_premium_unit
        if fund_type is not UNSET:
            field_dict["FundType"] = fund_type
        if close_position_order is not UNSET:
            field_dict["ClosePositionOrder"] = close_position_order
        if close_positions is not UNSET:
            field_dict["ClosePositions"] = close_positions
        if reverse_limit_order is not UNSET:
            field_dict["ReverseLimitOrder"] = reverse_limit_order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.positions import Positions
        from ..models.request_send_order_reverse_limit_order import RequestSendOrderReverseLimitOrder

        d = dict(src_dict)
        symbol = d.pop("Symbol")

        exchange = d.pop("Exchange")

        security_type = d.pop("SecurityType")

        side = d.pop("Side")

        cash_margin = d.pop("CashMargin")

        deliv_type = d.pop("DelivType")

        account_type = d.pop("AccountType")

        qty = d.pop("Qty")

        front_order_type = d.pop("FrontOrderType")

        price = d.pop("Price")

        expire_day = d.pop("ExpireDay")

        margin_trade_type = d.pop("MarginTradeType", UNSET)

        margin_premium_unit = d.pop("MarginPremiumUnit", UNSET)

        fund_type = d.pop("FundType", UNSET)

        close_position_order = d.pop("ClosePositionOrder", UNSET)

        _close_positions = d.pop("ClosePositions", UNSET)
        close_positions: list[Positions] | Unset = UNSET
        if _close_positions is not UNSET:
            close_positions = []
            for close_positions_item_data in _close_positions:
                close_positions_item = Positions.from_dict(close_positions_item_data)

                close_positions.append(close_positions_item)

        _reverse_limit_order = d.pop("ReverseLimitOrder", UNSET)
        reverse_limit_order: RequestSendOrderReverseLimitOrder | Unset
        if isinstance(_reverse_limit_order, Unset):
            reverse_limit_order = UNSET
        else:
            reverse_limit_order = RequestSendOrderReverseLimitOrder.from_dict(_reverse_limit_order)

        request_send_order = cls(
            symbol=symbol,
            exchange=exchange,
            security_type=security_type,
            side=side,
            cash_margin=cash_margin,
            deliv_type=deliv_type,
            account_type=account_type,
            qty=qty,
            front_order_type=front_order_type,
            price=price,
            expire_day=expire_day,
            margin_trade_type=margin_trade_type,
            margin_premium_unit=margin_premium_unit,
            fund_type=fund_type,
            close_position_order=close_position_order,
            close_positions=close_positions,
            reverse_limit_order=reverse_limit_order,
        )

        request_send_order.additional_properties = d
        return request_send_order

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
