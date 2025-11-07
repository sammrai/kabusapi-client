from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.orders_success_details_item import OrdersSuccessDetailsItem


T = TypeVar("T", bound="OrdersSuccess")


@_attrs_define
class OrdersSuccess:
    """
    Example:
        {'ID': '20220404A02N04738436', 'State': 5, 'OrderState': 5, 'OrdType': 1, 'RecvTime':
            '2022-04-04T18:00:51.763683+09:00', 'Symbol': '8306', 'SymbolName': '三菱ＵＦＪフィナンシャル・グループ', 'Exchange': 1,
            'ExchangeName': '東証プ', 'TimeInForce': 1, 'Price': 704.5, 'OrderQty': 1500, 'CumQty': 1500, 'Side': '1',
            'CashMargin': 2, 'AccountType': 4, 'DelivType': 2, 'ExpireDay': 20220404, 'MarginTradeType': 1, 'MarginPremium':
            None, 'Details': [{'SeqNum': 1, 'ID': '20220404A02N04738436', 'RecType': 1, 'ExchangeID':
            '00000000-0000-0000-0000-00000000', 'State': 3, 'TransactTime': '2022-04-04T18:00:51.763683+09:00', 'OrdType':
            1, 'Price': 704.5, 'Qty': 1500, 'ExecutionID': '', 'ExecutionDay': '2022-04-04T18:02:00+09:00', 'DelivDay':
            20220406, 'Commission': 0, 'CommissionTax': 0}]}

    Attributes:
        id (str | Unset): 注文番号
        state (int | Unset): 状態<br>
            ※OrderStateと同一である
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
                      <td>処理中（発注送信中）</td>
                  </tr>
                  <tr>
                      <td>3</td>
                      <td>処理済（発注済・訂正済）</td>
                  </tr>
                  <tr>
                      <td>4</td>
                      <td>訂正取消送信中</td>
                  </tr>
                  <tr>
                      <td>5</td>
                      <td>終了（発注エラー・取消済・全約定・失効・期限切れ）</td>
                  </tr>
              </tbody>
            </table>
        order_state (int | Unset): 注文状態<br>
            ※Stateと同一である
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
                      <td>処理中（発注送信中）</td>
                  </tr>
                  <tr>
                      <td>3</td>
                      <td>処理済（発注済・訂正済）</td>
                  </tr>
                  <tr>
                      <td>4</td>
                      <td>訂正取消送信中</td>
                  </tr>
                  <tr>
                      <td>5</td>
                      <td>終了（発注エラー・取消済・全約定・失効・期限切れ）</td>
                  </tr>
              </tbody>
            </table>
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
        recv_time (str | Unset): 受注日時
        symbol (str | Unset): 銘柄コード
        symbol_name (str | Unset): 銘柄名
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
                      <td>9</td>
                      <td>SOR</td>
                  </tr>
                  <tr>
                      <td>27</td>
                      <td>東証+</td>
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
        exchange_name (str | Unset): 市場名
        time_in_force (int | Unset): 有効期間条件<br>※先物・オプション銘柄の場合のみ
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
        price (float | Unset): 値段
        order_qty (float | Unset): 発注数量<br>
            ※注文期限切れと失効の場合、OrderQtyはゼロになりません。<br>
            ※期限切れと失効の確認方法としては、DetailsのRecType（3: 期限切れ、7: 失効）にてご確認ください。
        cum_qty (float | Unset): 約定数量
        side (str | Unset): 売買区分
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
        cash_margin (int | Unset): 取引区分
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
                      <td>新規</td>
                  </tr>
                  <tr>
                      <td>3</td>
                      <td>返済</td>
                  </tr>
              </tbody>
            </table>
        account_type (int | Unset): 口座種別
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
        deliv_type (int | Unset): 受渡区分
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
                      <td>お預り金</td>
                  </tr>
                  <tr>
                      <td>3</td>
                      <td>auマネーコネクト</td>
                  </tr>
              </tbody>
            </table>
        expire_day (int | Unset): 注文有効期限<br>yyyyMMdd形式
        margin_trade_type (int | Unset): 信用取引区分<br>
            ※信用を注文した際に表示されます。
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
        margin_premium (float | Unset): プレミアム料<br>
            ※（注文中数量＋約定済数量）×１株あたりプレミアム料として計算されます。<br>
            ※信用を注文した際に表示されます。<br>
            ※制度信用売/買、一般（長期）買、一般（デイトレ）買の場合は、Noneと返されます。<br>
            一般（長期）売、一般（デイトレ）売の場合は、プレミアム料=0の場合、0（ゼロ）と返されます。
        details (list[OrdersSuccessDetailsItem] | Unset): 注文詳細
    """

    id: str | Unset = UNSET
    state: int | Unset = UNSET
    order_state: int | Unset = UNSET
    ord_type: int | Unset = UNSET
    recv_time: str | Unset = UNSET
    symbol: str | Unset = UNSET
    symbol_name: str | Unset = UNSET
    exchange: int | Unset = UNSET
    exchange_name: str | Unset = UNSET
    time_in_force: int | Unset = UNSET
    price: float | Unset = UNSET
    order_qty: float | Unset = UNSET
    cum_qty: float | Unset = UNSET
    side: str | Unset = UNSET
    cash_margin: int | Unset = UNSET
    account_type: int | Unset = UNSET
    deliv_type: int | Unset = UNSET
    expire_day: int | Unset = UNSET
    margin_trade_type: int | Unset = UNSET
    margin_premium: float | Unset = UNSET
    details: list[OrdersSuccessDetailsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        state = self.state

        order_state = self.order_state

        ord_type = self.ord_type

        recv_time = self.recv_time

        symbol = self.symbol

        symbol_name = self.symbol_name

        exchange = self.exchange

        exchange_name = self.exchange_name

        time_in_force = self.time_in_force

        price = self.price

        order_qty = self.order_qty

        cum_qty = self.cum_qty

        side = self.side

        cash_margin = self.cash_margin

        account_type = self.account_type

        deliv_type = self.deliv_type

        expire_day = self.expire_day

        margin_trade_type = self.margin_trade_type

        margin_premium = self.margin_premium

        details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = []
            for details_item_data in self.details:
                details_item = details_item_data.to_dict()
                details.append(details_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["ID"] = id
        if state is not UNSET:
            field_dict["State"] = state
        if order_state is not UNSET:
            field_dict["OrderState"] = order_state
        if ord_type is not UNSET:
            field_dict["OrdType"] = ord_type
        if recv_time is not UNSET:
            field_dict["RecvTime"] = recv_time
        if symbol is not UNSET:
            field_dict["Symbol"] = symbol
        if symbol_name is not UNSET:
            field_dict["SymbolName"] = symbol_name
        if exchange is not UNSET:
            field_dict["Exchange"] = exchange
        if exchange_name is not UNSET:
            field_dict["ExchangeName"] = exchange_name
        if time_in_force is not UNSET:
            field_dict["TimeInForce"] = time_in_force
        if price is not UNSET:
            field_dict["Price"] = price
        if order_qty is not UNSET:
            field_dict["OrderQty"] = order_qty
        if cum_qty is not UNSET:
            field_dict["CumQty"] = cum_qty
        if side is not UNSET:
            field_dict["Side"] = side
        if cash_margin is not UNSET:
            field_dict["CashMargin"] = cash_margin
        if account_type is not UNSET:
            field_dict["AccountType"] = account_type
        if deliv_type is not UNSET:
            field_dict["DelivType"] = deliv_type
        if expire_day is not UNSET:
            field_dict["ExpireDay"] = expire_day
        if margin_trade_type is not UNSET:
            field_dict["MarginTradeType"] = margin_trade_type
        if margin_premium is not UNSET:
            field_dict["MarginPremium"] = margin_premium
        if details is not UNSET:
            field_dict["Details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.orders_success_details_item import OrdersSuccessDetailsItem

        d = dict(src_dict)
        id = d.pop("ID", UNSET)

        state = d.pop("State", UNSET)

        order_state = d.pop("OrderState", UNSET)

        ord_type = d.pop("OrdType", UNSET)

        recv_time = d.pop("RecvTime", UNSET)

        symbol = d.pop("Symbol", UNSET)

        symbol_name = d.pop("SymbolName", UNSET)

        exchange = d.pop("Exchange", UNSET)

        exchange_name = d.pop("ExchangeName", UNSET)

        time_in_force = d.pop("TimeInForce", UNSET)

        price = d.pop("Price", UNSET)

        order_qty = d.pop("OrderQty", UNSET)

        cum_qty = d.pop("CumQty", UNSET)

        side = d.pop("Side", UNSET)

        cash_margin = d.pop("CashMargin", UNSET)

        account_type = d.pop("AccountType", UNSET)

        deliv_type = d.pop("DelivType", UNSET)

        expire_day = d.pop("ExpireDay", UNSET)

        margin_trade_type = d.pop("MarginTradeType", UNSET)

        margin_premium = d.pop("MarginPremium", UNSET)

        _details = d.pop("Details", UNSET)
        details: list[OrdersSuccessDetailsItem] | Unset = UNSET
        if _details is not UNSET:
            details = []
            for details_item_data in _details:
                details_item = OrdersSuccessDetailsItem.from_dict(details_item_data)

                details.append(details_item)

        orders_success = cls(
            id=id,
            state=state,
            order_state=order_state,
            ord_type=ord_type,
            recv_time=recv_time,
            symbol=symbol,
            symbol_name=symbol_name,
            exchange=exchange,
            exchange_name=exchange_name,
            time_in_force=time_in_force,
            price=price,
            order_qty=order_qty,
            cum_qty=cum_qty,
            side=side,
            cash_margin=cash_margin,
            account_type=account_type,
            deliv_type=deliv_type,
            expire_day=expire_day,
            margin_trade_type=margin_trade_type,
            margin_premium=margin_premium,
            details=details,
        )

        orders_success.additional_properties = d
        return orders_success

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
