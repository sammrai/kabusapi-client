from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SymbolSuccess")


@_attrs_define
class SymbolSuccess:
    """
    Example:
        {'Symbol': '166090018', 'SymbolName': '日経平均先物 21/09', 'DisplayName': '日経平均先物 09', 'Exchange': 23,
            'ExchangeName': '大阪日中', 'TradingUnit': 1.0, 'PriceRangeGroup': '10118', 'UpperLimit': 29870.0, 'LowerLimit':
            25290.0, 'Underlyer': 'NK225', 'DerivMonth': '2021/09', 'TradeEnd': 20210909, 'TradeStart': 20200313,
            'ClearingPrice': None}

    Attributes:
        symbol (str | Unset): 銘柄コード
        symbol_name (str | Unset): 銘柄名
        display_name (str | Unset): 銘柄略称<br>※株式・先物・オプション銘柄の場合のみ
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
        exchange_name (str | Unset): 市場名称<br>※株式・先物・オプション銘柄の場合のみ
        bis_category (str | Unset): 業種コード名<br>※株式銘柄の場合のみ
            <table>
              <thead>
                  <tr>
                      <th>定義値</th>
                      <th>説明</th>
                  </tr>
              </thead>
              <tbody>
                  <tr>
                      <td>0050</td>
                      <td>水産・農林業</td>
                  </tr>
                  <tr>
                      <td>1050</td>
                      <td>鉱業</td>
                  </tr>
                  <tr>
                      <td>2050</td>
                      <td>建設業</td>
                  </tr>
                  <tr>
                      <td>3050</td>
                      <td>食料品</td>
                  </tr>
                  <tr>
                      <td>3100</td>
                      <td>繊維製品</td>
                  </tr>
                  <tr>
                      <td>3150</td>
                      <td>パルプ・紙</td>
                  </tr>
                  <tr>
                      <td>3200</td>
                      <td>化学</td>
                  </tr>
                  <tr>
                      <td>3250</td>
                      <td>医薬品</td>
                  </tr>
                  <tr>
                      <td>3300</td>
                      <td>石油・石炭製品</td>
                  </tr>
                  <tr>
                      <td>3350</td>
                      <td>ゴム製品</td>
                  </tr>
                  <tr>
                      <td>3400</td>
                      <td>ガラス・土石製品</td>
                  </tr>
                  <tr>
                      <td>3450</td>
                      <td>鉄鋼</td>
                  </tr>
                  <tr>
                      <td>3500</td>
                      <td>非鉄金属</td>
                  </tr>
                  <tr>
                      <td>3550</td>
                      <td>金属製品</td>
                  </tr>
                  <tr>
                      <td>3600</td>
                      <td>機械</td>
                  </tr>
                  <tr>
                      <td>3650</td>
                      <td>電気機器</td>
                  </tr>
                  <tr>
                      <td>3700</td>
                      <td>輸送用機器</td>
                  </tr>
                  <tr>
                      <td>3750</td>
                      <td>精密機器</td>
                  </tr>
                  <tr>
                      <td>3800</td>
                      <td>その他製品</td>
                  </tr>
                  <tr>
                      <td>4050</td>
                      <td>電気・ガス業</td>
                  </tr>
                  <tr>
                      <td>5050</td>
                      <td>陸運業</td>
                  </tr>
                  <tr>
                      <td>5100</td>
                      <td>海運業</td>
                  </tr>
                  <tr>
                      <td>5150</td>
                      <td>空運業</td>
                  </tr>
                  <tr>
                      <td>5200</td>
                      <td>倉庫・運輸関連業</td>
                  </tr>
                  <tr>
                      <td>5250</td>
                      <td>情報・通信業</td>
                  </tr>
                  <tr>
                      <td>6050</td>
                      <td>卸売業</td>
                  </tr>
                  <tr>
                      <td>6100</td>
                      <td>小売業</td>
                  </tr>
                  <tr>
                      <td>7050</td>
                      <td>銀行業</td>
                  </tr>
                  <tr>
                      <td>7100</td>
                      <td>証券、商品先物取引業</td>
                  </tr>
                  <tr>
                      <td>7150</td>
                      <td>保険業</td>
                  </tr>
                  <tr>
                      <td>7200</td>
                      <td>その他金融業</td>
                  </tr>
                  <tr>
                      <td>8050</td>
                      <td>不動産業</td>
                  </tr>
                  <tr>
                      <td>9050</td>
                      <td>サービス業</td>
                  </tr>
                  <tr>
                      <td>9999</td>
                      <td>その他</td>
                  </tr>
              </tbody>
            </table>
        total_market_value (float | Unset): 時価総額<br>※株式銘柄の場合のみ<br>追加情報出力フラグ：falseの場合、null
        total_stocks (float | Unset): 発行済み株式数（千株）<br>※株式銘柄の場合のみ<br>追加情報出力フラグ：falseの場合、null
        trading_unit (float | Unset): 売買単位<br>※株式・先物・オプション銘柄の場合のみ
        fiscal_year_end_basic (int | Unset): 決算期日<br>※株式銘柄の場合のみ<br>追加情報出力フラグ：falseの場合、null
        price_range_group (str | Unset): 呼値グループ<br>
            ※株式・先物・オプション銘柄の場合のみ<br>
            ※各呼値コードが対応する商品は以下となります。<BR>
            株式の呼値の単位の詳細は [JPXページ](https://www.jpx.co.jp/equities/trading/domestic/07.html) をご覧ください。<BR>
            10000：株式(通常の呼値単位の銘柄)　<br>
            10003：株式(TOPIX500構成銘柄※売買単位が10口以上のETF等含む)<br>
            10004：株式(売買単位が1口のETF等)<br>
            10118 : 日経平均先物<br>
            10119 : 日経225mini<br>
            10318 : 日経平均オプション<br>
            10706 : ﾐﾆTOPIX先物<br>
            10718 : TOPIX先物<br>
            12122 : JPX日経400指数先物<br>
            14473 : NYダウ先物<br>
            14515 : 日経平均VI先物<br>
            15411 : グロース250先物<br>
            15569 : 東証REIT指数先物<br>
            17163 : TOPIXCore30指数先物<br>
            <table>
              <thead>
                  <tr>
                      <th>呼値コード</th>
                      <th>値段の水準</th>
                      <th>呼値単位</th>
                  </tr>
              </thead>
              <tbody>
                  <tr>
                      <td>10000</td>
                      <td>3000円以下</td>
                      <td>1</td>
                  </tr>
                  <tr>
                      <td>10000</td>
                      <td>5000円以下</td>
                      <td>5</td>
                  </tr>
                  <tr>
                      <td>10000</td>
                      <td>30000円以下</td>
                      <td>10</td>
                  </tr>
                  <tr>
                      <td>10000</td>
                      <td>50000円以下</td>
                      <td>50</td>
                  </tr>
                  <tr>
                      <td>10000</td>
                      <td>300000円以下</td>
                      <td>100</td>
                  </tr>
                  <tr>
                      <td>10000</td>
                      <td>500000円以下</td>
                      <td>500</td>
                  </tr>
                  <tr>
                      <td>10000</td>
                      <td>3000000円以下</td>
                      <td>1000</td>
                  </tr>
                  <tr>
                      <td>10000</td>
                      <td>5000000円以下</td>
                      <td>5000</td>
                  </tr>
                  <tr>
                      <td>10000</td>
                      <td>30000000円以下</td>
                      <td>10000</td>
                  </tr>
                  <tr>
                      <td>10000</td>
                      <td>50000000円以下</td>
                      <td>50000</td>
                  </tr>
                  <tr>
                      <td>10000</td>
                      <td>50000000円超</td>
                      <td>100000</td>
                  </tr>
                  <tr>
                      <td>10003</td>
                      <td>1000円以下</td>
                      <td>0.1</td>
                  </tr>
                  <tr>
                      <td>10003</td>
                      <td>3000円以下</td>
                      <td>0.5</td>
                  </tr>
                  <tr>
                      <td>10003</td>
                      <td>10000円以下</td>
                      <td>1</td>
                  </tr>
                  <tr>
                      <td>10003</td>
                      <td>30000円以下</td>
                      <td>5</td>
                  </tr>
                  <tr>
                      <td>10003</td>
                      <td>100000円以下</td>
                      <td>10</td>
                  </tr>
                  <tr>
                      <td>10003</td>
                      <td>300000円以下</td>
                      <td>50</td>
                  </tr>
                  <tr>
                      <td>10003</td>
                      <td>1000000円以下</td>
                      <td>100</td>
                  </tr>
                  <tr>
                      <td>10003</td>
                      <td>3000000円以下</td>
                      <td>500</td>
                  </tr>
                  <tr>
                      <td>10003</td>
                      <td>10000000円以下</td>
                      <td>1000</td>
                  </tr>
                  <tr>
                      <td>10003</td>
                      <td>30000000円以下</td>
                      <td>5000</td>
                  </tr>
                  <tr>
                      <td>10003</td>
                      <td>30000000円超</td>
                      <td>10000</td>
                  </tr>
                  <tr>
                      <td>10004</td>
                      <td>10000円以下</td>
                      <td>1</td>
                  </tr>
                  <tr>
                      <td>10004</td>
                      <td>30000円以下</td>
                      <td>5</td>
                  </tr>
                  <tr>
                      <td>10004</td>
                      <td>100000円以下</td>
                      <td>10</td>
                  </tr>
                  <tr>
                      <td>10004</td>
                      <td>300000円以下</td>
                      <td>50</td>
                  </tr>
                  <tr>
                      <td>10004</td>
                      <td>1000000円以下</td>
                      <td>100</td>
                  </tr>
                  <tr>
                      <td>10004</td>
                      <td>3000000円以下</td>
                      <td>500</td>
                  </tr>
                  <tr>
                      <td>10004</td>
                      <td>10000000円以下</td>
                      <td>1000</td>
                  </tr>
                  <tr>
                      <td>10004</td>
                      <td>30000000円以下</td>
                      <td>5000</td>
                  </tr>
                  <tr>
                      <td>10004</td>
                      <td>30000000円超</td>
                      <td>10000</td>
                  </tr>
                  <tr>
                      <td>10118</td>
                      <td>-</td>
                      <td>10</td>
                  </tr>
                  <tr>
                      <td>10119</td>
                      <td>-</td>
                      <td>5</td>
                  </tr>
                  <tr>
                      <td>10318</td>
                      <td>100円以下</td>
                      <td>1</td>
                  </tr>
                  <tr>
                      <td>10318</td>
                      <td>1000円以下</td>
                      <td>5</td>
                  </tr>
                  <tr>
                      <td>10318</td>
                      <td>1000円超</td>
                      <td>10</td>
                  </tr>
                  <tr>
                      <td>10706</td>
                      <td>-</td>
                      <td>0.25</td>
                  </tr>
                  <tr>
                      <td>10718</td>
                      <td>-</td>
                      <td>0.5</td>
                  </tr>
                  <tr>
                      <td>12122</td>
                      <td>-</td>
                      <td>5</td>
                  </tr>
                  <tr>
                      <td>14473</td>
                      <td>-</td>
                      <td>1</td>
                  </tr>
                  <tr>
                      <td>14515</td>
                      <td>-</td>
                      <td>0.05</td>
                  </tr>
                  <tr>
                      <td>15411</td>
                      <td>-</td>
                      <td>1</td>
                  </tr>
                  <tr>
                      <td>15569</td>
                      <td>-</td>
                      <td>0.5</td>
                  </tr>
                  <tr>
                      <td>17163</td>
                      <td>-</td>
                      <td>0.5</td>
                  </tr>
              </tbody>
            </table>
        kc_margin_buy (bool | Unset): 一般信用買建フラグ<br>※trueのとき、一般信用(長期)または一般信用(デイトレ)が買建可能<br>※株式銘柄の場合のみ
        kc_margin_sell (bool | Unset): 一般信用売建フラグ<br>※trueのとき、一般信用(長期)または一般信用(デイトレ)が売建可能<br>※株式銘柄の場合のみ
        margin_buy (bool | Unset): 制度信用買建フラグ<br>※trueのとき制度信用買建可能<br>※株式銘柄の場合のみ
        margin_sell (bool | Unset): 制度信用売建フラグ<br>※trueのとき制度信用売建可能<br>※株式銘柄の場合のみ
        upper_limit (float | Unset): 値幅上限<br>※株式・先物・オプション銘柄の場合のみ
        lower_limit (float | Unset): 値幅下限<br>※株式・先物・オプション銘柄の場合のみ
        underlyer (str | Unset): 原資産コード<br>※先物・オプション銘柄の場合のみ
            <table>
              <thead>
                  <tr>
                      <th>定義値</th>
                      <th>説明</th>
                  </tr>
              </thead>
              <tbody>
                  <tr>
                      <td>NK225</td>
                      <td>日経225</td>
                  </tr>
                  <tr>
                      <td>NK300</td>
                      <td>日経300</td>
                  </tr>
                  <tr>
                      <td>GROWTH</td>
                      <td>グロース250先物</td>
                  </tr>
                  <tr>
                      <td>JPX400</td>
                      <td>JPX日経400</td>
                  </tr>
                  <tr>
                      <td>TOPIX</td>
                      <td>TOPIX</td>
                  </tr>
                  <tr>
                      <td>NKVI</td>
                      <td>日経平均VI</td>
                  </tr>
                  <tr>
                      <td>DJIA</td>
                      <td>NYダウ</td>
                  </tr>
                  <tr>
                      <td>TSEREITINDEX</td>
                      <td>東証REIT指数</td>
                  </tr>
                  <tr>
                      <td>TOPIXCORE30</td>
                      <td>TOPIX Core30</td>
                  </tr>
              </tbody>
            </table>
        deriv_month (str | Unset): 限月-年月<br>※「限月-年月」は「年(yyyy)/月(MM)」で表示します。<br>※先物・オプション銘柄の場合のみ
        trade_start (int | Unset): 取引開始日<br>※先物・オプション銘柄の場合のみ
        trade_end (int | Unset): 取引終了日<br>※先物・オプション銘柄の場合のみ
        strike_price (float | Unset): 権利行使価格<br>※オプション銘柄の場合のみ
        put_or_call (int | Unset): プット/コール区分<br>※オプション銘柄の場合のみ
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
                      <td>プット</td>
                  </tr>
                  <tr>
                      <td>2</td>
                      <td>コール</td>
                  </tr>
              </tbody>
            </table>
        clearing_price (float | Unset): 清算値<br>※先物銘柄の場合のみ<br>追加情報出力フラグ：falseの場合、null
    """

    symbol: str | Unset = UNSET
    symbol_name: str | Unset = UNSET
    display_name: str | Unset = UNSET
    exchange: int | Unset = UNSET
    exchange_name: str | Unset = UNSET
    bis_category: str | Unset = UNSET
    total_market_value: float | Unset = UNSET
    total_stocks: float | Unset = UNSET
    trading_unit: float | Unset = UNSET
    fiscal_year_end_basic: int | Unset = UNSET
    price_range_group: str | Unset = UNSET
    kc_margin_buy: bool | Unset = UNSET
    kc_margin_sell: bool | Unset = UNSET
    margin_buy: bool | Unset = UNSET
    margin_sell: bool | Unset = UNSET
    upper_limit: float | Unset = UNSET
    lower_limit: float | Unset = UNSET
    underlyer: str | Unset = UNSET
    deriv_month: str | Unset = UNSET
    trade_start: int | Unset = UNSET
    trade_end: int | Unset = UNSET
    strike_price: float | Unset = UNSET
    put_or_call: int | Unset = UNSET
    clearing_price: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        symbol = self.symbol

        symbol_name = self.symbol_name

        display_name = self.display_name

        exchange = self.exchange

        exchange_name = self.exchange_name

        bis_category = self.bis_category

        total_market_value = self.total_market_value

        total_stocks = self.total_stocks

        trading_unit = self.trading_unit

        fiscal_year_end_basic = self.fiscal_year_end_basic

        price_range_group = self.price_range_group

        kc_margin_buy = self.kc_margin_buy

        kc_margin_sell = self.kc_margin_sell

        margin_buy = self.margin_buy

        margin_sell = self.margin_sell

        upper_limit = self.upper_limit

        lower_limit = self.lower_limit

        underlyer = self.underlyer

        deriv_month = self.deriv_month

        trade_start = self.trade_start

        trade_end = self.trade_end

        strike_price = self.strike_price

        put_or_call = self.put_or_call

        clearing_price = self.clearing_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if symbol is not UNSET:
            field_dict["Symbol"] = symbol
        if symbol_name is not UNSET:
            field_dict["SymbolName"] = symbol_name
        if display_name is not UNSET:
            field_dict["DisplayName"] = display_name
        if exchange is not UNSET:
            field_dict["Exchange"] = exchange
        if exchange_name is not UNSET:
            field_dict["ExchangeName"] = exchange_name
        if bis_category is not UNSET:
            field_dict["BisCategory"] = bis_category
        if total_market_value is not UNSET:
            field_dict["TotalMarketValue"] = total_market_value
        if total_stocks is not UNSET:
            field_dict["TotalStocks"] = total_stocks
        if trading_unit is not UNSET:
            field_dict["TradingUnit"] = trading_unit
        if fiscal_year_end_basic is not UNSET:
            field_dict["FiscalYearEndBasic"] = fiscal_year_end_basic
        if price_range_group is not UNSET:
            field_dict["PriceRangeGroup"] = price_range_group
        if kc_margin_buy is not UNSET:
            field_dict["KCMarginBuy"] = kc_margin_buy
        if kc_margin_sell is not UNSET:
            field_dict["KCMarginSell"] = kc_margin_sell
        if margin_buy is not UNSET:
            field_dict["MarginBuy"] = margin_buy
        if margin_sell is not UNSET:
            field_dict["MarginSell"] = margin_sell
        if upper_limit is not UNSET:
            field_dict["UpperLimit"] = upper_limit
        if lower_limit is not UNSET:
            field_dict["LowerLimit"] = lower_limit
        if underlyer is not UNSET:
            field_dict["Underlyer"] = underlyer
        if deriv_month is not UNSET:
            field_dict["DerivMonth"] = deriv_month
        if trade_start is not UNSET:
            field_dict["TradeStart"] = trade_start
        if trade_end is not UNSET:
            field_dict["TradeEnd"] = trade_end
        if strike_price is not UNSET:
            field_dict["StrikePrice"] = strike_price
        if put_or_call is not UNSET:
            field_dict["PutOrCall"] = put_or_call
        if clearing_price is not UNSET:
            field_dict["ClearingPrice"] = clearing_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        symbol = d.pop("Symbol", UNSET)

        symbol_name = d.pop("SymbolName", UNSET)

        display_name = d.pop("DisplayName", UNSET)

        exchange = d.pop("Exchange", UNSET)

        exchange_name = d.pop("ExchangeName", UNSET)

        bis_category = d.pop("BisCategory", UNSET)

        total_market_value = d.pop("TotalMarketValue", UNSET)

        total_stocks = d.pop("TotalStocks", UNSET)

        trading_unit = d.pop("TradingUnit", UNSET)

        fiscal_year_end_basic = d.pop("FiscalYearEndBasic", UNSET)

        price_range_group = d.pop("PriceRangeGroup", UNSET)

        kc_margin_buy = d.pop("KCMarginBuy", UNSET)

        kc_margin_sell = d.pop("KCMarginSell", UNSET)

        margin_buy = d.pop("MarginBuy", UNSET)

        margin_sell = d.pop("MarginSell", UNSET)

        upper_limit = d.pop("UpperLimit", UNSET)

        lower_limit = d.pop("LowerLimit", UNSET)

        underlyer = d.pop("Underlyer", UNSET)

        deriv_month = d.pop("DerivMonth", UNSET)

        trade_start = d.pop("TradeStart", UNSET)

        trade_end = d.pop("TradeEnd", UNSET)

        strike_price = d.pop("StrikePrice", UNSET)

        put_or_call = d.pop("PutOrCall", UNSET)

        clearing_price = d.pop("ClearingPrice", UNSET)

        symbol_success = cls(
            symbol=symbol,
            symbol_name=symbol_name,
            display_name=display_name,
            exchange=exchange,
            exchange_name=exchange_name,
            bis_category=bis_category,
            total_market_value=total_market_value,
            total_stocks=total_stocks,
            trading_unit=trading_unit,
            fiscal_year_end_basic=fiscal_year_end_basic,
            price_range_group=price_range_group,
            kc_margin_buy=kc_margin_buy,
            kc_margin_sell=kc_margin_sell,
            margin_buy=margin_buy,
            margin_sell=margin_sell,
            upper_limit=upper_limit,
            lower_limit=lower_limit,
            underlyer=underlyer,
            deriv_month=deriv_month,
            trade_start=trade_start,
            trade_end=trade_end,
            strike_price=strike_price,
            put_or_call=put_or_call,
            clearing_price=clearing_price,
        )

        symbol_success.additional_properties = d
        return symbol_success

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
