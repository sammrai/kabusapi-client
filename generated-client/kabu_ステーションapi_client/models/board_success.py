from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.board_success_buy_1 import BoardSuccessBuy1
    from ..models.board_success_buy_2 import BoardSuccessBuy2
    from ..models.board_success_buy_3 import BoardSuccessBuy3
    from ..models.board_success_buy_4 import BoardSuccessBuy4
    from ..models.board_success_buy_5 import BoardSuccessBuy5
    from ..models.board_success_buy_6 import BoardSuccessBuy6
    from ..models.board_success_buy_7 import BoardSuccessBuy7
    from ..models.board_success_buy_8 import BoardSuccessBuy8
    from ..models.board_success_buy_9 import BoardSuccessBuy9
    from ..models.board_success_buy_10 import BoardSuccessBuy10
    from ..models.board_success_sell_1 import BoardSuccessSell1
    from ..models.board_success_sell_2 import BoardSuccessSell2
    from ..models.board_success_sell_3 import BoardSuccessSell3
    from ..models.board_success_sell_4 import BoardSuccessSell4
    from ..models.board_success_sell_5 import BoardSuccessSell5
    from ..models.board_success_sell_6 import BoardSuccessSell6
    from ..models.board_success_sell_7 import BoardSuccessSell7
    from ..models.board_success_sell_8 import BoardSuccessSell8
    from ..models.board_success_sell_9 import BoardSuccessSell9
    from ..models.board_success_sell_10 import BoardSuccessSell10


T = TypeVar("T", bound="BoardSuccess")


@_attrs_define
class BoardSuccess:
    """下記にあるBIDとASKとは、トレーダー目線から見た場合の値であるため、BidPrice=Sell1のPrice、AskPrice=Buy1のPriceという数値となります。

    Example:
        {'Symbol': '5401', 'SymbolName': '新日鐵住金', 'Exchange': 1, 'ExchangeName': '東証プ', 'CurrentPrice': 2408.0,
            'CurrentPriceTime': '2022-04-04T15:00:00+09:00', 'CurrentPriceChangeStatus': '0058', 'CurrentPriceStatus': 1,
            'CalcPrice': 343.7, 'PreviousClose': 1048.0, 'PreviousCloseTime': '2022-04-01T00:00:00+09:00',
            'ChangePreviousClose': 1360.0, 'ChangePreviousClosePer': 129.77, 'OpeningPrice': 2380.0, 'OpeningPriceTime':
            '2022-04-04T09:00:00+09:00', 'HighPrice': 2418.0, 'HighPriceTime': '2022-04-04T13:25:47+09:00', 'LowPrice':
            2370.0, 'LowPriceTime': '2022-04-04T10:00:04+09:00', 'TradingVolume': 4571500.0, 'TradingVolumeTime':
            '2022-04-04T15:00:00+09:00', 'VWAP': 2394.4262, 'TradingValue': 10946119350.0, 'BidQty': 100.0, 'BidPrice':
            2408.5, 'BidTime': '2022-04-04T14:59:59+09:00', 'BidSign': '0101', 'MarketOrderSellQty': 0.0, 'Sell1': {'Time':
            '2022-04-04T14:59:59+09:00', 'Sign': '0101', 'Price': 2408.5, 'Qty': 100.0}, 'Sell2': {'Price': 2409.0, 'Qty':
            800.0}, 'Sell3': {'Price': 2409.5, 'Qty': 2100.0}, 'Sell4': {'Price': 2410.0, 'Qty': 800.0}, 'Sell5': {'Price':
            2410.5, 'Qty': 500}, 'Sell6': {'Price': 2411.0, 'Qty': 8400.0}, 'Sell7': {'Price': 2411.5, 'Qty': 1200.0},
            'Sell8': {'Price': 2412.0, 'Qty': 27200.0}, 'Sell9': {'Price': 2412.5, 'Qty': 400.0}, 'Sell10': {'Price':
            2413.0, 'Qty': 16400.0}, 'AskQty': 200.0, 'AskPrice': 2407.5, 'AskTime': '2022-04-04T14:59:59+09:00', 'AskSign':
            '0101', 'MarketOrderBuyQty': 0.0, 'Buy1': {'Time': '2022-04-04T14:59:59+09:00', 'Sign': '0101', 'Price': 2407.5,
            'Qty': 200.0}, 'Buy2': {'Price': 2407.0, 'Qty': 400.0}, 'Buy3': {'Price': 2406.5, 'Qty': 1000.0}, 'Buy4':
            {'Price': 2406.0, 'Qty': 5800.0}, 'Buy5': {'Price': 2405.5, 'Qty': 7500}, 'Buy6': {'Price': 2405.0, 'Qty':
            2200.0}, 'Buy7': {'Price': 2404.5, 'Qty': 16700.0}, 'Buy8': {'Price': 2403.0, 'Qty': 1300.0}, 'Buy9': {'Price':
            2403.5, 'Qty': 1300.0}, 'Buy10': {'Price': 2403.0, 'Qty': 3000.0}, 'OverSellQty': 974900, 'UnderBuyQty': 756000,
            'TotalMarketValue': 3266254659361.4, 'SecurityType': 1}

    Attributes:
        symbol (str | Unset): 銘柄コード
        symbol_name (str | Unset): 銘柄名
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
            </table> Example: 1.
        exchange_name (str | Unset): 市場名称<br>※株式・先物・オプション銘柄の場合のみ
        current_price (float | Unset): 現値
        current_price_time (datetime.datetime | Unset): 現値時刻
        current_price_change_status (str | Unset): 現値前値比較
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
                      <td>0056</td>
                      <td>変わらず</td>
                  </tr>
                  <tr>
                      <td>0057</td>
                      <td>UP</td>
                  </tr>
                  <tr>
                      <td>0058</td>
                      <td>DOWN</td>
                  </tr>
                  <tr>
                      <td>0059</td>
                      <td>中断板寄り後の初値</td>
                  </tr>
                  <tr>
                      <td>0060</td>
                      <td>ザラバ引け</td>
                  </tr>
                  <tr>
                      <td>0061</td>
                      <td>板寄り引け</td>
                  </tr>
                  <tr>
                      <td>0062</td>
                      <td>中断引け</td>
                  </tr>
                  <tr>
                      <td>0063</td>
                      <td>ダウン引け</td>
                  </tr>
                  <tr>
                      <td>0064</td>
                      <td>逆転終値</td>
                  </tr>
                  <tr>
                      <td>0066</td>
                      <td>特別気配引け</td>
                  </tr>
                  <tr>
                      <td>0067</td>
                      <td>一時留保引け</td>
                  </tr>
                  <tr>
                      <td>0068</td>
                      <td>売買停止引け</td>
                  </tr>
                  <tr>
                      <td>0069</td>
                      <td>サーキットブレーカ引け</td>
                  </tr>
                  <tr>
                      <td>0431</td>
                      <td>ダイナミックサーキットブレーカ引け</td>
                  </tr>
              </tbody>
            </table>
        current_price_status (int | Unset): 現値ステータス
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
                      <td>現値</td>
                  </tr>
                  <tr>
                      <td>2</td>
                      <td>不連続歩み</td>
                  </tr>
                  <tr>
                      <td>3</td>
                      <td>板寄せ</td>
                  </tr>
                  <tr>
                      <td>4</td>
                      <td>システム障害</td>
                  </tr>
                  <tr>
                      <td>5</td>
                      <td>中断</td>
                  </tr>
                  <tr>
                      <td>6</td>
                      <td>売買停止</td>
                  </tr>
                  <tr>
                      <td>7</td>
                      <td>売買停止・システム停止解除</td>
                  </tr>
                  <tr>
                      <td>8</td>
                      <td>終値</td>
                  </tr>
                  <tr>
                      <td>9</td>
                      <td>システム停止</td>
                  </tr>
                  <tr>
                      <td>10</td>
                      <td>概算値</td>
                  </tr>
                  <tr>
                      <td>11</td>
                      <td>参考値</td>
                  </tr>
                  <tr>
                      <td>12</td>
                      <td>サーキットブレイク実施中</td>
                  </tr>
                  <tr>
                      <td>13</td>
                      <td>システム障害解除</td>
                  </tr>
                  <tr>
                      <td>14</td>
                      <td>サーキットブレイク解除</td>
                  </tr>
                  <tr>
                      <td>15</td>
                      <td>中断解除</td>
                  </tr>
                  <tr>
                      <td>16</td>
                      <td>一時留保中</td>
                  </tr>
                  <tr>
                      <td>17</td>
                      <td>一時留保解除</td>
                  </tr>
                  <tr>
                      <td>18</td>
                      <td>ファイル障害</td>
                  </tr>
                  <tr>
                      <td>19</td>
                      <td>ファイル障害解除</td>
                  </tr>
                  <tr>
                      <td>20</td>
                      <td>Spread/Strategy</td>
                  </tr>
                  <tr>
                      <td>21</td>
                      <td>ダイナミックサーキットブレイク発動</td>
                  </tr>
                  <tr>
                      <td>22</td>
                      <td>ダイナミックサーキットブレイク解除</td>
                  </tr>
                  <tr>
                      <td>23</td>
                      <td>板寄せ約定</td>
                  </tr>
              </tbody>
            </table>
        calc_price (float | Unset): 計算用現値
        previous_close (float | Unset): 前日終値
        previous_close_time (datetime.datetime | Unset): 前日終値日付
        change_previous_close (float | Unset): 前日比
        change_previous_close_per (float | Unset): 騰落率
        opening_price (float | Unset): 始値
        opening_price_time (datetime.datetime | Unset): 始値時刻
        high_price (float | Unset): 高値
        high_price_time (datetime.datetime | Unset): 高値時刻
        low_price (float | Unset): 安値
        low_price_time (datetime.datetime | Unset): 安値時刻
        trading_volume (float | Unset): 売買高<br>※株式・先物・オプション銘柄の場合のみ
        trading_volume_time (datetime.datetime | Unset): 売買高時刻<br>※株式・先物・オプション銘柄の場合のみ
        vwap (float | Unset): 売買高加重平均価格（VWAP）<br>※株式・先物・オプション銘柄の場合のみ
        trading_value (float | Unset): 売買代金<br>※株式・先物・オプション銘柄の場合のみ
        bid_qty (float | Unset): 最良売気配数量 ※①<br>※株式・先物・オプション銘柄の場合のみ
        bid_price (float | Unset): 最良売気配値段 ※①<br>※株式・先物・オプション銘柄の場合のみ
        bid_time (datetime.datetime | Unset): 最良売気配時刻 ※①<br>※株式銘柄の場合のみ
        bid_sign (str | Unset): 最良売気配フラグ ※①<br>※株式・先物・オプション銘柄の場合のみ
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
        market_order_sell_qty (float | Unset): 売成行数量<br>※株式銘柄の場合のみ
        sell_1 (BoardSuccessSell1 | Unset): 売気配数量1本目
        sell_2 (BoardSuccessSell2 | Unset): 売気配数量2本目
        sell_3 (BoardSuccessSell3 | Unset): 売気配数量3本目
        sell_4 (BoardSuccessSell4 | Unset): 売気配数量4本目
        sell_5 (BoardSuccessSell5 | Unset): 売気配数量5本目
        sell_6 (BoardSuccessSell6 | Unset): 売気配数量6本目
        sell_7 (BoardSuccessSell7 | Unset): 売気配数量7本目
        sell_8 (BoardSuccessSell8 | Unset): 売気配数量8本目
        sell_9 (BoardSuccessSell9 | Unset): 売気配数量9本目
        sell_10 (BoardSuccessSell10 | Unset): 売気配数量10本目
        ask_qty (float | Unset): 最良買気配数量 ※①<br>※株式・先物・オプション銘柄の場合のみ
        ask_price (float | Unset): 最良買気配値段 ※①<br>※株式・先物・オプション銘柄の場合のみ
        ask_time (datetime.datetime | Unset): 最良買気配時刻 ※①<br>※株式銘柄の場合のみ
        ask_sign (str | Unset): 最良買気配フラグ ※①<br>※株式・先物・オプション銘柄の場合のみ
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
        market_order_buy_qty (float | Unset): 買成行数量<br>※株式銘柄の場合のみ
        buy_1 (BoardSuccessBuy1 | Unset): 買気配数量1本目
        buy_2 (BoardSuccessBuy2 | Unset): 買気配数量2本目
        buy_3 (BoardSuccessBuy3 | Unset): 買気配数量3本目
        buy_4 (BoardSuccessBuy4 | Unset): 買気配数量4本目
        buy_5 (BoardSuccessBuy5 | Unset): 買気配数量5本目
        buy_6 (BoardSuccessBuy6 | Unset): 買気配数量6本目
        buy_7 (BoardSuccessBuy7 | Unset): 買気配数量7本目
        buy_8 (BoardSuccessBuy8 | Unset): 買気配数量8本目
        buy_9 (BoardSuccessBuy9 | Unset): 買気配数量9本目
        buy_10 (BoardSuccessBuy10 | Unset): 買気配数量10本目
        over_sell_qty (float | Unset): OVER気配数量<br>※株式銘柄の場合のみ
        under_buy_qty (float | Unset): UNDER気配数量<br>※株式銘柄の場合のみ
        total_market_value (float | Unset): 時価総額<br>※株式銘柄の場合のみ
        clearing_price (float | Unset): 清算値<br>※先物銘柄の場合のみ
        iv (float | Unset): インプライド・ボラティリティ<br>※オプション銘柄かつ日通しの場合のみ
        gamma (float | Unset): ガンマ<br>※オプション銘柄かつ日通しの場合のみ
        theta (float | Unset): セータ<br>※オプション銘柄かつ日通しの場合のみ
        vega (float | Unset): ベガ<br>※オプション銘柄かつ日通しの場合のみ
        delta (float | Unset): デルタ<br>※オプション銘柄かつ日通しの場合のみ
        security_type (int | Unset): 銘柄種別
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
                  <td>指数</td>
                </tr>
                <tr>
                  <td>1</td>
                  <td>現物</td>
                </tr>
                <tr>
                  <td>101</td>
                  <td>日経225先物</td>
                </tr>
                <tr>
                  <td>103</td>
                  <td>日経225OP</td>
                </tr>
                <tr>
                  <td>107</td>
                  <td>TOPIX先物</td>
                </tr>
                <tr>
                  <td>121</td>
                  <td>JPX400先物</td>
                </tr>
                <tr>
                  <td>144</td>
                  <td>NYダウ</td>
                </tr>
                <tr>
                  <td>145</td>
                  <td>日経平均VI</td>
                </tr>
                <tr>
                  <td>154</td>
                  <td>グロース250先物</td>
                </tr>
                <tr>
                  <td>155</td>
                  <td>TOPIX_REIT</td>
                </tr>
                <tr>
                  <td>171</td>
                  <td>TOPIX CORE30</td>
                </tr>
                <tr>
                  <td>901</td>
                  <td>日経平均225ミニ先物</td>
                </tr>
                <tr>
                  <td>907</td>
                  <td>TOPIXミニ先物</td>
                </tr>
              </tbody>
            </table>
    """

    symbol: str | Unset = UNSET
    symbol_name: str | Unset = UNSET
    exchange: int | Unset = UNSET
    exchange_name: str | Unset = UNSET
    current_price: float | Unset = UNSET
    current_price_time: datetime.datetime | Unset = UNSET
    current_price_change_status: str | Unset = UNSET
    current_price_status: int | Unset = UNSET
    calc_price: float | Unset = UNSET
    previous_close: float | Unset = UNSET
    previous_close_time: datetime.datetime | Unset = UNSET
    change_previous_close: float | Unset = UNSET
    change_previous_close_per: float | Unset = UNSET
    opening_price: float | Unset = UNSET
    opening_price_time: datetime.datetime | Unset = UNSET
    high_price: float | Unset = UNSET
    high_price_time: datetime.datetime | Unset = UNSET
    low_price: float | Unset = UNSET
    low_price_time: datetime.datetime | Unset = UNSET
    trading_volume: float | Unset = UNSET
    trading_volume_time: datetime.datetime | Unset = UNSET
    vwap: float | Unset = UNSET
    trading_value: float | Unset = UNSET
    bid_qty: float | Unset = UNSET
    bid_price: float | Unset = UNSET
    bid_time: datetime.datetime | Unset = UNSET
    bid_sign: str | Unset = UNSET
    market_order_sell_qty: float | Unset = UNSET
    sell_1: BoardSuccessSell1 | Unset = UNSET
    sell_2: BoardSuccessSell2 | Unset = UNSET
    sell_3: BoardSuccessSell3 | Unset = UNSET
    sell_4: BoardSuccessSell4 | Unset = UNSET
    sell_5: BoardSuccessSell5 | Unset = UNSET
    sell_6: BoardSuccessSell6 | Unset = UNSET
    sell_7: BoardSuccessSell7 | Unset = UNSET
    sell_8: BoardSuccessSell8 | Unset = UNSET
    sell_9: BoardSuccessSell9 | Unset = UNSET
    sell_10: BoardSuccessSell10 | Unset = UNSET
    ask_qty: float | Unset = UNSET
    ask_price: float | Unset = UNSET
    ask_time: datetime.datetime | Unset = UNSET
    ask_sign: str | Unset = UNSET
    market_order_buy_qty: float | Unset = UNSET
    buy_1: BoardSuccessBuy1 | Unset = UNSET
    buy_2: BoardSuccessBuy2 | Unset = UNSET
    buy_3: BoardSuccessBuy3 | Unset = UNSET
    buy_4: BoardSuccessBuy4 | Unset = UNSET
    buy_5: BoardSuccessBuy5 | Unset = UNSET
    buy_6: BoardSuccessBuy6 | Unset = UNSET
    buy_7: BoardSuccessBuy7 | Unset = UNSET
    buy_8: BoardSuccessBuy8 | Unset = UNSET
    buy_9: BoardSuccessBuy9 | Unset = UNSET
    buy_10: BoardSuccessBuy10 | Unset = UNSET
    over_sell_qty: float | Unset = UNSET
    under_buy_qty: float | Unset = UNSET
    total_market_value: float | Unset = UNSET
    clearing_price: float | Unset = UNSET
    iv: float | Unset = UNSET
    gamma: float | Unset = UNSET
    theta: float | Unset = UNSET
    vega: float | Unset = UNSET
    delta: float | Unset = UNSET
    security_type: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        symbol = self.symbol

        symbol_name = self.symbol_name

        exchange = self.exchange

        exchange_name = self.exchange_name

        current_price = self.current_price

        current_price_time: str | Unset = UNSET
        if not isinstance(self.current_price_time, Unset):
            current_price_time = self.current_price_time.isoformat()

        current_price_change_status = self.current_price_change_status

        current_price_status = self.current_price_status

        calc_price = self.calc_price

        previous_close = self.previous_close

        previous_close_time: str | Unset = UNSET
        if not isinstance(self.previous_close_time, Unset):
            previous_close_time = self.previous_close_time.isoformat()

        change_previous_close = self.change_previous_close

        change_previous_close_per = self.change_previous_close_per

        opening_price = self.opening_price

        opening_price_time: str | Unset = UNSET
        if not isinstance(self.opening_price_time, Unset):
            opening_price_time = self.opening_price_time.isoformat()

        high_price = self.high_price

        high_price_time: str | Unset = UNSET
        if not isinstance(self.high_price_time, Unset):
            high_price_time = self.high_price_time.isoformat()

        low_price = self.low_price

        low_price_time: str | Unset = UNSET
        if not isinstance(self.low_price_time, Unset):
            low_price_time = self.low_price_time.isoformat()

        trading_volume = self.trading_volume

        trading_volume_time: str | Unset = UNSET
        if not isinstance(self.trading_volume_time, Unset):
            trading_volume_time = self.trading_volume_time.isoformat()

        vwap = self.vwap

        trading_value = self.trading_value

        bid_qty = self.bid_qty

        bid_price = self.bid_price

        bid_time: str | Unset = UNSET
        if not isinstance(self.bid_time, Unset):
            bid_time = self.bid_time.isoformat()

        bid_sign = self.bid_sign

        market_order_sell_qty = self.market_order_sell_qty

        sell_1: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sell_1, Unset):
            sell_1 = self.sell_1.to_dict()

        sell_2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sell_2, Unset):
            sell_2 = self.sell_2.to_dict()

        sell_3: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sell_3, Unset):
            sell_3 = self.sell_3.to_dict()

        sell_4: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sell_4, Unset):
            sell_4 = self.sell_4.to_dict()

        sell_5: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sell_5, Unset):
            sell_5 = self.sell_5.to_dict()

        sell_6: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sell_6, Unset):
            sell_6 = self.sell_6.to_dict()

        sell_7: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sell_7, Unset):
            sell_7 = self.sell_7.to_dict()

        sell_8: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sell_8, Unset):
            sell_8 = self.sell_8.to_dict()

        sell_9: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sell_9, Unset):
            sell_9 = self.sell_9.to_dict()

        sell_10: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sell_10, Unset):
            sell_10 = self.sell_10.to_dict()

        ask_qty = self.ask_qty

        ask_price = self.ask_price

        ask_time: str | Unset = UNSET
        if not isinstance(self.ask_time, Unset):
            ask_time = self.ask_time.isoformat()

        ask_sign = self.ask_sign

        market_order_buy_qty = self.market_order_buy_qty

        buy_1: dict[str, Any] | Unset = UNSET
        if not isinstance(self.buy_1, Unset):
            buy_1 = self.buy_1.to_dict()

        buy_2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.buy_2, Unset):
            buy_2 = self.buy_2.to_dict()

        buy_3: dict[str, Any] | Unset = UNSET
        if not isinstance(self.buy_3, Unset):
            buy_3 = self.buy_3.to_dict()

        buy_4: dict[str, Any] | Unset = UNSET
        if not isinstance(self.buy_4, Unset):
            buy_4 = self.buy_4.to_dict()

        buy_5: dict[str, Any] | Unset = UNSET
        if not isinstance(self.buy_5, Unset):
            buy_5 = self.buy_5.to_dict()

        buy_6: dict[str, Any] | Unset = UNSET
        if not isinstance(self.buy_6, Unset):
            buy_6 = self.buy_6.to_dict()

        buy_7: dict[str, Any] | Unset = UNSET
        if not isinstance(self.buy_7, Unset):
            buy_7 = self.buy_7.to_dict()

        buy_8: dict[str, Any] | Unset = UNSET
        if not isinstance(self.buy_8, Unset):
            buy_8 = self.buy_8.to_dict()

        buy_9: dict[str, Any] | Unset = UNSET
        if not isinstance(self.buy_9, Unset):
            buy_9 = self.buy_9.to_dict()

        buy_10: dict[str, Any] | Unset = UNSET
        if not isinstance(self.buy_10, Unset):
            buy_10 = self.buy_10.to_dict()

        over_sell_qty = self.over_sell_qty

        under_buy_qty = self.under_buy_qty

        total_market_value = self.total_market_value

        clearing_price = self.clearing_price

        iv = self.iv

        gamma = self.gamma

        theta = self.theta

        vega = self.vega

        delta = self.delta

        security_type = self.security_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if symbol is not UNSET:
            field_dict["Symbol"] = symbol
        if symbol_name is not UNSET:
            field_dict["SymbolName"] = symbol_name
        if exchange is not UNSET:
            field_dict["Exchange"] = exchange
        if exchange_name is not UNSET:
            field_dict["ExchangeName"] = exchange_name
        if current_price is not UNSET:
            field_dict["CurrentPrice"] = current_price
        if current_price_time is not UNSET:
            field_dict["CurrentPriceTime"] = current_price_time
        if current_price_change_status is not UNSET:
            field_dict["CurrentPriceChangeStatus"] = current_price_change_status
        if current_price_status is not UNSET:
            field_dict["CurrentPriceStatus"] = current_price_status
        if calc_price is not UNSET:
            field_dict["CalcPrice"] = calc_price
        if previous_close is not UNSET:
            field_dict["PreviousClose"] = previous_close
        if previous_close_time is not UNSET:
            field_dict["PreviousCloseTime"] = previous_close_time
        if change_previous_close is not UNSET:
            field_dict["ChangePreviousClose"] = change_previous_close
        if change_previous_close_per is not UNSET:
            field_dict["ChangePreviousClosePer"] = change_previous_close_per
        if opening_price is not UNSET:
            field_dict["OpeningPrice"] = opening_price
        if opening_price_time is not UNSET:
            field_dict["OpeningPriceTime"] = opening_price_time
        if high_price is not UNSET:
            field_dict["HighPrice"] = high_price
        if high_price_time is not UNSET:
            field_dict["HighPriceTime"] = high_price_time
        if low_price is not UNSET:
            field_dict["LowPrice"] = low_price
        if low_price_time is not UNSET:
            field_dict["LowPriceTime"] = low_price_time
        if trading_volume is not UNSET:
            field_dict["TradingVolume"] = trading_volume
        if trading_volume_time is not UNSET:
            field_dict["TradingVolumeTime"] = trading_volume_time
        if vwap is not UNSET:
            field_dict["VWAP"] = vwap
        if trading_value is not UNSET:
            field_dict["TradingValue"] = trading_value
        if bid_qty is not UNSET:
            field_dict["BidQty"] = bid_qty
        if bid_price is not UNSET:
            field_dict["BidPrice"] = bid_price
        if bid_time is not UNSET:
            field_dict["BidTime"] = bid_time
        if bid_sign is not UNSET:
            field_dict["BidSign"] = bid_sign
        if market_order_sell_qty is not UNSET:
            field_dict["MarketOrderSellQty"] = market_order_sell_qty
        if sell_1 is not UNSET:
            field_dict["Sell1"] = sell_1
        if sell_2 is not UNSET:
            field_dict["Sell2"] = sell_2
        if sell_3 is not UNSET:
            field_dict["Sell3"] = sell_3
        if sell_4 is not UNSET:
            field_dict["Sell4"] = sell_4
        if sell_5 is not UNSET:
            field_dict["Sell5"] = sell_5
        if sell_6 is not UNSET:
            field_dict["Sell6"] = sell_6
        if sell_7 is not UNSET:
            field_dict["Sell7"] = sell_7
        if sell_8 is not UNSET:
            field_dict["Sell8"] = sell_8
        if sell_9 is not UNSET:
            field_dict["Sell9"] = sell_9
        if sell_10 is not UNSET:
            field_dict["Sell10"] = sell_10
        if ask_qty is not UNSET:
            field_dict["AskQty"] = ask_qty
        if ask_price is not UNSET:
            field_dict["AskPrice"] = ask_price
        if ask_time is not UNSET:
            field_dict["AskTime"] = ask_time
        if ask_sign is not UNSET:
            field_dict["AskSign"] = ask_sign
        if market_order_buy_qty is not UNSET:
            field_dict["MarketOrderBuyQty"] = market_order_buy_qty
        if buy_1 is not UNSET:
            field_dict["Buy1"] = buy_1
        if buy_2 is not UNSET:
            field_dict["Buy2"] = buy_2
        if buy_3 is not UNSET:
            field_dict["Buy3"] = buy_3
        if buy_4 is not UNSET:
            field_dict["Buy4"] = buy_4
        if buy_5 is not UNSET:
            field_dict["Buy5"] = buy_5
        if buy_6 is not UNSET:
            field_dict["Buy6"] = buy_6
        if buy_7 is not UNSET:
            field_dict["Buy7"] = buy_7
        if buy_8 is not UNSET:
            field_dict["Buy8"] = buy_8
        if buy_9 is not UNSET:
            field_dict["Buy9"] = buy_9
        if buy_10 is not UNSET:
            field_dict["Buy10"] = buy_10
        if over_sell_qty is not UNSET:
            field_dict["OverSellQty"] = over_sell_qty
        if under_buy_qty is not UNSET:
            field_dict["UnderBuyQty"] = under_buy_qty
        if total_market_value is not UNSET:
            field_dict["TotalMarketValue"] = total_market_value
        if clearing_price is not UNSET:
            field_dict["ClearingPrice"] = clearing_price
        if iv is not UNSET:
            field_dict["IV"] = iv
        if gamma is not UNSET:
            field_dict["Gamma"] = gamma
        if theta is not UNSET:
            field_dict["Theta"] = theta
        if vega is not UNSET:
            field_dict["Vega"] = vega
        if delta is not UNSET:
            field_dict["Delta"] = delta
        if security_type is not UNSET:
            field_dict["SecurityType"] = security_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.board_success_buy_1 import BoardSuccessBuy1
        from ..models.board_success_buy_2 import BoardSuccessBuy2
        from ..models.board_success_buy_3 import BoardSuccessBuy3
        from ..models.board_success_buy_4 import BoardSuccessBuy4
        from ..models.board_success_buy_5 import BoardSuccessBuy5
        from ..models.board_success_buy_6 import BoardSuccessBuy6
        from ..models.board_success_buy_7 import BoardSuccessBuy7
        from ..models.board_success_buy_8 import BoardSuccessBuy8
        from ..models.board_success_buy_9 import BoardSuccessBuy9
        from ..models.board_success_buy_10 import BoardSuccessBuy10
        from ..models.board_success_sell_1 import BoardSuccessSell1
        from ..models.board_success_sell_2 import BoardSuccessSell2
        from ..models.board_success_sell_3 import BoardSuccessSell3
        from ..models.board_success_sell_4 import BoardSuccessSell4
        from ..models.board_success_sell_5 import BoardSuccessSell5
        from ..models.board_success_sell_6 import BoardSuccessSell6
        from ..models.board_success_sell_7 import BoardSuccessSell7
        from ..models.board_success_sell_8 import BoardSuccessSell8
        from ..models.board_success_sell_9 import BoardSuccessSell9
        from ..models.board_success_sell_10 import BoardSuccessSell10

        d = dict(src_dict)
        symbol = d.pop("Symbol", UNSET)

        symbol_name = d.pop("SymbolName", UNSET)

        exchange = d.pop("Exchange", UNSET)

        exchange_name = d.pop("ExchangeName", UNSET)

        current_price = d.pop("CurrentPrice", UNSET)

        _current_price_time = d.pop("CurrentPriceTime", UNSET)
        current_price_time: datetime.datetime | Unset
        if isinstance(_current_price_time, Unset):
            current_price_time = UNSET
        else:
            current_price_time = isoparse(_current_price_time)

        current_price_change_status = d.pop("CurrentPriceChangeStatus", UNSET)

        current_price_status = d.pop("CurrentPriceStatus", UNSET)

        calc_price = d.pop("CalcPrice", UNSET)

        previous_close = d.pop("PreviousClose", UNSET)

        _previous_close_time = d.pop("PreviousCloseTime", UNSET)
        previous_close_time: datetime.datetime | Unset
        if isinstance(_previous_close_time, Unset):
            previous_close_time = UNSET
        else:
            previous_close_time = isoparse(_previous_close_time)

        change_previous_close = d.pop("ChangePreviousClose", UNSET)

        change_previous_close_per = d.pop("ChangePreviousClosePer", UNSET)

        opening_price = d.pop("OpeningPrice", UNSET)

        _opening_price_time = d.pop("OpeningPriceTime", UNSET)
        opening_price_time: datetime.datetime | Unset
        if isinstance(_opening_price_time, Unset):
            opening_price_time = UNSET
        else:
            opening_price_time = isoparse(_opening_price_time)

        high_price = d.pop("HighPrice", UNSET)

        _high_price_time = d.pop("HighPriceTime", UNSET)
        high_price_time: datetime.datetime | Unset
        if isinstance(_high_price_time, Unset):
            high_price_time = UNSET
        else:
            high_price_time = isoparse(_high_price_time)

        low_price = d.pop("LowPrice", UNSET)

        _low_price_time = d.pop("LowPriceTime", UNSET)
        low_price_time: datetime.datetime | Unset
        if isinstance(_low_price_time, Unset):
            low_price_time = UNSET
        else:
            low_price_time = isoparse(_low_price_time)

        trading_volume = d.pop("TradingVolume", UNSET)

        _trading_volume_time = d.pop("TradingVolumeTime", UNSET)
        trading_volume_time: datetime.datetime | Unset
        if isinstance(_trading_volume_time, Unset):
            trading_volume_time = UNSET
        else:
            trading_volume_time = isoparse(_trading_volume_time)

        vwap = d.pop("VWAP", UNSET)

        trading_value = d.pop("TradingValue", UNSET)

        bid_qty = d.pop("BidQty", UNSET)

        bid_price = d.pop("BidPrice", UNSET)

        _bid_time = d.pop("BidTime", UNSET)
        bid_time: datetime.datetime | Unset
        if isinstance(_bid_time, Unset):
            bid_time = UNSET
        else:
            bid_time = isoparse(_bid_time)

        bid_sign = d.pop("BidSign", UNSET)

        market_order_sell_qty = d.pop("MarketOrderSellQty", UNSET)

        _sell_1 = d.pop("Sell1", UNSET)
        sell_1: BoardSuccessSell1 | Unset
        if isinstance(_sell_1, Unset):
            sell_1 = UNSET
        else:
            sell_1 = BoardSuccessSell1.from_dict(_sell_1)

        _sell_2 = d.pop("Sell2", UNSET)
        sell_2: BoardSuccessSell2 | Unset
        if isinstance(_sell_2, Unset):
            sell_2 = UNSET
        else:
            sell_2 = BoardSuccessSell2.from_dict(_sell_2)

        _sell_3 = d.pop("Sell3", UNSET)
        sell_3: BoardSuccessSell3 | Unset
        if isinstance(_sell_3, Unset):
            sell_3 = UNSET
        else:
            sell_3 = BoardSuccessSell3.from_dict(_sell_3)

        _sell_4 = d.pop("Sell4", UNSET)
        sell_4: BoardSuccessSell4 | Unset
        if isinstance(_sell_4, Unset):
            sell_4 = UNSET
        else:
            sell_4 = BoardSuccessSell4.from_dict(_sell_4)

        _sell_5 = d.pop("Sell5", UNSET)
        sell_5: BoardSuccessSell5 | Unset
        if isinstance(_sell_5, Unset):
            sell_5 = UNSET
        else:
            sell_5 = BoardSuccessSell5.from_dict(_sell_5)

        _sell_6 = d.pop("Sell6", UNSET)
        sell_6: BoardSuccessSell6 | Unset
        if isinstance(_sell_6, Unset):
            sell_6 = UNSET
        else:
            sell_6 = BoardSuccessSell6.from_dict(_sell_6)

        _sell_7 = d.pop("Sell7", UNSET)
        sell_7: BoardSuccessSell7 | Unset
        if isinstance(_sell_7, Unset):
            sell_7 = UNSET
        else:
            sell_7 = BoardSuccessSell7.from_dict(_sell_7)

        _sell_8 = d.pop("Sell8", UNSET)
        sell_8: BoardSuccessSell8 | Unset
        if isinstance(_sell_8, Unset):
            sell_8 = UNSET
        else:
            sell_8 = BoardSuccessSell8.from_dict(_sell_8)

        _sell_9 = d.pop("Sell9", UNSET)
        sell_9: BoardSuccessSell9 | Unset
        if isinstance(_sell_9, Unset):
            sell_9 = UNSET
        else:
            sell_9 = BoardSuccessSell9.from_dict(_sell_9)

        _sell_10 = d.pop("Sell10", UNSET)
        sell_10: BoardSuccessSell10 | Unset
        if isinstance(_sell_10, Unset):
            sell_10 = UNSET
        else:
            sell_10 = BoardSuccessSell10.from_dict(_sell_10)

        ask_qty = d.pop("AskQty", UNSET)

        ask_price = d.pop("AskPrice", UNSET)

        _ask_time = d.pop("AskTime", UNSET)
        ask_time: datetime.datetime | Unset
        if isinstance(_ask_time, Unset):
            ask_time = UNSET
        else:
            ask_time = isoparse(_ask_time)

        ask_sign = d.pop("AskSign", UNSET)

        market_order_buy_qty = d.pop("MarketOrderBuyQty", UNSET)

        _buy_1 = d.pop("Buy1", UNSET)
        buy_1: BoardSuccessBuy1 | Unset
        if isinstance(_buy_1, Unset):
            buy_1 = UNSET
        else:
            buy_1 = BoardSuccessBuy1.from_dict(_buy_1)

        _buy_2 = d.pop("Buy2", UNSET)
        buy_2: BoardSuccessBuy2 | Unset
        if isinstance(_buy_2, Unset):
            buy_2 = UNSET
        else:
            buy_2 = BoardSuccessBuy2.from_dict(_buy_2)

        _buy_3 = d.pop("Buy3", UNSET)
        buy_3: BoardSuccessBuy3 | Unset
        if isinstance(_buy_3, Unset):
            buy_3 = UNSET
        else:
            buy_3 = BoardSuccessBuy3.from_dict(_buy_3)

        _buy_4 = d.pop("Buy4", UNSET)
        buy_4: BoardSuccessBuy4 | Unset
        if isinstance(_buy_4, Unset):
            buy_4 = UNSET
        else:
            buy_4 = BoardSuccessBuy4.from_dict(_buy_4)

        _buy_5 = d.pop("Buy5", UNSET)
        buy_5: BoardSuccessBuy5 | Unset
        if isinstance(_buy_5, Unset):
            buy_5 = UNSET
        else:
            buy_5 = BoardSuccessBuy5.from_dict(_buy_5)

        _buy_6 = d.pop("Buy6", UNSET)
        buy_6: BoardSuccessBuy6 | Unset
        if isinstance(_buy_6, Unset):
            buy_6 = UNSET
        else:
            buy_6 = BoardSuccessBuy6.from_dict(_buy_6)

        _buy_7 = d.pop("Buy7", UNSET)
        buy_7: BoardSuccessBuy7 | Unset
        if isinstance(_buy_7, Unset):
            buy_7 = UNSET
        else:
            buy_7 = BoardSuccessBuy7.from_dict(_buy_7)

        _buy_8 = d.pop("Buy8", UNSET)
        buy_8: BoardSuccessBuy8 | Unset
        if isinstance(_buy_8, Unset):
            buy_8 = UNSET
        else:
            buy_8 = BoardSuccessBuy8.from_dict(_buy_8)

        _buy_9 = d.pop("Buy9", UNSET)
        buy_9: BoardSuccessBuy9 | Unset
        if isinstance(_buy_9, Unset):
            buy_9 = UNSET
        else:
            buy_9 = BoardSuccessBuy9.from_dict(_buy_9)

        _buy_10 = d.pop("Buy10", UNSET)
        buy_10: BoardSuccessBuy10 | Unset
        if isinstance(_buy_10, Unset):
            buy_10 = UNSET
        else:
            buy_10 = BoardSuccessBuy10.from_dict(_buy_10)

        over_sell_qty = d.pop("OverSellQty", UNSET)

        under_buy_qty = d.pop("UnderBuyQty", UNSET)

        total_market_value = d.pop("TotalMarketValue", UNSET)

        clearing_price = d.pop("ClearingPrice", UNSET)

        iv = d.pop("IV", UNSET)

        gamma = d.pop("Gamma", UNSET)

        theta = d.pop("Theta", UNSET)

        vega = d.pop("Vega", UNSET)

        delta = d.pop("Delta", UNSET)

        security_type = d.pop("SecurityType", UNSET)

        board_success = cls(
            symbol=symbol,
            symbol_name=symbol_name,
            exchange=exchange,
            exchange_name=exchange_name,
            current_price=current_price,
            current_price_time=current_price_time,
            current_price_change_status=current_price_change_status,
            current_price_status=current_price_status,
            calc_price=calc_price,
            previous_close=previous_close,
            previous_close_time=previous_close_time,
            change_previous_close=change_previous_close,
            change_previous_close_per=change_previous_close_per,
            opening_price=opening_price,
            opening_price_time=opening_price_time,
            high_price=high_price,
            high_price_time=high_price_time,
            low_price=low_price,
            low_price_time=low_price_time,
            trading_volume=trading_volume,
            trading_volume_time=trading_volume_time,
            vwap=vwap,
            trading_value=trading_value,
            bid_qty=bid_qty,
            bid_price=bid_price,
            bid_time=bid_time,
            bid_sign=bid_sign,
            market_order_sell_qty=market_order_sell_qty,
            sell_1=sell_1,
            sell_2=sell_2,
            sell_3=sell_3,
            sell_4=sell_4,
            sell_5=sell_5,
            sell_6=sell_6,
            sell_7=sell_7,
            sell_8=sell_8,
            sell_9=sell_9,
            sell_10=sell_10,
            ask_qty=ask_qty,
            ask_price=ask_price,
            ask_time=ask_time,
            ask_sign=ask_sign,
            market_order_buy_qty=market_order_buy_qty,
            buy_1=buy_1,
            buy_2=buy_2,
            buy_3=buy_3,
            buy_4=buy_4,
            buy_5=buy_5,
            buy_6=buy_6,
            buy_7=buy_7,
            buy_8=buy_8,
            buy_9=buy_9,
            buy_10=buy_10,
            over_sell_qty=over_sell_qty,
            under_buy_qty=under_buy_qty,
            total_market_value=total_market_value,
            clearing_price=clearing_price,
            iv=iv,
            gamma=gamma,
            theta=theta,
            vega=vega,
            delta=delta,
            security_type=security_type,
        )

        board_success.additional_properties = d
        return board_success

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
