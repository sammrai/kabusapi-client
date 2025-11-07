from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PositionsSuccess")


@_attrs_define
class PositionsSuccess:
    """
    Example:
        {'ExecutionID': 'E20220404xxxxx', 'AccountType': 4, 'Symbol': '8306', 'SymbolName': '三菱ＵＦＪフィナンシャル・グループ',
            'Exchange': 1, 'ExchangeName': '東証プ', 'ExecutionDay': 20220404, 'Price': 704, 'LeavesQty': 500, 'HoldQty': 0,
            'Side': '1', 'Expenses': 0, 'Commission': 1620, 'CommissionTax': 162, 'ExpireDay': 20220404, 'MarginTradeType':
            1, 'CurrentPrice': 414.5, 'Valuation': 207250, 'ProfitLoss': 144750, 'ProfitLossRate': 41.12215909090909}

    Attributes:
        execution_id (str | Unset): 約定番号<br>※現物取引では、nullが返ります。
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
        security_type (int | Unset): 銘柄種別<br>※先物・オプション銘柄の場合のみ
        execution_day (int | Unset): 約定日（建玉日）<br>※信用・先物・オプションの場合のみ<br>※現物取引では、nullが返ります。
        price (float | Unset): 値段
        leaves_qty (float | Unset): 残数量（保有数量）
        hold_qty (float | Unset): 拘束数量（返済のために拘束されている数量）
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
        expenses (float | Unset): 諸経費<br>※信用・先物・オプションの場合のみ
        commission (float | Unset): 手数料<br>※信用・先物・オプションの場合のみ
        commission_tax (float | Unset): 手数料消費税<br>※信用・先物・オプションの場合のみ
        expire_day (int | Unset): 返済期日<br>※信用・先物・オプションの場合のみ
        margin_trade_type (int | Unset): 信用取引区分<br>※信用の場合のみ
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
        current_price (float | Unset): 現在値<br>追加情報出力フラグ：falseの場合、null
        valuation (float | Unset): 評価金額<br>追加情報出力フラグ：falseの場合、null
        profit_loss (float | Unset): 評価損益額<br>追加情報出力フラグ：falseの場合、null
        profit_loss_rate (float | Unset): 評価損益率<br>追加情報出力フラグ：falseの場合、null
    """

    execution_id: str | Unset = UNSET
    account_type: int | Unset = UNSET
    symbol: str | Unset = UNSET
    symbol_name: str | Unset = UNSET
    exchange: int | Unset = UNSET
    exchange_name: str | Unset = UNSET
    security_type: int | Unset = UNSET
    execution_day: int | Unset = UNSET
    price: float | Unset = UNSET
    leaves_qty: float | Unset = UNSET
    hold_qty: float | Unset = UNSET
    side: str | Unset = UNSET
    expenses: float | Unset = UNSET
    commission: float | Unset = UNSET
    commission_tax: float | Unset = UNSET
    expire_day: int | Unset = UNSET
    margin_trade_type: int | Unset = UNSET
    current_price: float | Unset = UNSET
    valuation: float | Unset = UNSET
    profit_loss: float | Unset = UNSET
    profit_loss_rate: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        execution_id = self.execution_id

        account_type = self.account_type

        symbol = self.symbol

        symbol_name = self.symbol_name

        exchange = self.exchange

        exchange_name = self.exchange_name

        security_type = self.security_type

        execution_day = self.execution_day

        price = self.price

        leaves_qty = self.leaves_qty

        hold_qty = self.hold_qty

        side = self.side

        expenses = self.expenses

        commission = self.commission

        commission_tax = self.commission_tax

        expire_day = self.expire_day

        margin_trade_type = self.margin_trade_type

        current_price = self.current_price

        valuation = self.valuation

        profit_loss = self.profit_loss

        profit_loss_rate = self.profit_loss_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if execution_id is not UNSET:
            field_dict["ExecutionID"] = execution_id
        if account_type is not UNSET:
            field_dict["AccountType"] = account_type
        if symbol is not UNSET:
            field_dict["Symbol"] = symbol
        if symbol_name is not UNSET:
            field_dict["SymbolName"] = symbol_name
        if exchange is not UNSET:
            field_dict["Exchange"] = exchange
        if exchange_name is not UNSET:
            field_dict["ExchangeName"] = exchange_name
        if security_type is not UNSET:
            field_dict["SecurityType"] = security_type
        if execution_day is not UNSET:
            field_dict["ExecutionDay"] = execution_day
        if price is not UNSET:
            field_dict["Price"] = price
        if leaves_qty is not UNSET:
            field_dict["LeavesQty"] = leaves_qty
        if hold_qty is not UNSET:
            field_dict["HoldQty"] = hold_qty
        if side is not UNSET:
            field_dict["Side"] = side
        if expenses is not UNSET:
            field_dict["Expenses"] = expenses
        if commission is not UNSET:
            field_dict["Commission"] = commission
        if commission_tax is not UNSET:
            field_dict["CommissionTax"] = commission_tax
        if expire_day is not UNSET:
            field_dict["ExpireDay"] = expire_day
        if margin_trade_type is not UNSET:
            field_dict["MarginTradeType"] = margin_trade_type
        if current_price is not UNSET:
            field_dict["CurrentPrice"] = current_price
        if valuation is not UNSET:
            field_dict["Valuation"] = valuation
        if profit_loss is not UNSET:
            field_dict["ProfitLoss"] = profit_loss
        if profit_loss_rate is not UNSET:
            field_dict["ProfitLossRate"] = profit_loss_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        execution_id = d.pop("ExecutionID", UNSET)

        account_type = d.pop("AccountType", UNSET)

        symbol = d.pop("Symbol", UNSET)

        symbol_name = d.pop("SymbolName", UNSET)

        exchange = d.pop("Exchange", UNSET)

        exchange_name = d.pop("ExchangeName", UNSET)

        security_type = d.pop("SecurityType", UNSET)

        execution_day = d.pop("ExecutionDay", UNSET)

        price = d.pop("Price", UNSET)

        leaves_qty = d.pop("LeavesQty", UNSET)

        hold_qty = d.pop("HoldQty", UNSET)

        side = d.pop("Side", UNSET)

        expenses = d.pop("Expenses", UNSET)

        commission = d.pop("Commission", UNSET)

        commission_tax = d.pop("CommissionTax", UNSET)

        expire_day = d.pop("ExpireDay", UNSET)

        margin_trade_type = d.pop("MarginTradeType", UNSET)

        current_price = d.pop("CurrentPrice", UNSET)

        valuation = d.pop("Valuation", UNSET)

        profit_loss = d.pop("ProfitLoss", UNSET)

        profit_loss_rate = d.pop("ProfitLossRate", UNSET)

        positions_success = cls(
            execution_id=execution_id,
            account_type=account_type,
            symbol=symbol,
            symbol_name=symbol_name,
            exchange=exchange,
            exchange_name=exchange_name,
            security_type=security_type,
            execution_day=execution_day,
            price=price,
            leaves_qty=leaves_qty,
            hold_qty=hold_qty,
            side=side,
            expenses=expenses,
            commission=commission,
            commission_tax=commission_tax,
            expire_day=expire_day,
            margin_trade_type=margin_trade_type,
            current_price=current_price,
            valuation=valuation,
            profit_loss=profit_loss,
            profit_loss_rate=profit_loss_rate,
        )

        positions_success.additional_properties = d
        return positions_success

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
