# RankingByTradeValueResponseRankingInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_false** | **number** | 順位&lt;br&gt;※ランキング内で同じ順位が返却される場合があります（10位が2件など） | [optional] [default to undefined]
**Trend** | **string** | トレンド &lt;table&gt;     &lt;thead&gt;         &lt;tr&gt;             &lt;th&gt;定義値&lt;/th&gt;             &lt;th&gt;内容&lt;/th&gt;         &lt;/tr&gt;     &lt;/thead&gt;     &lt;tbody&gt;         &lt;tr&gt;             &lt;td&gt;0&lt;/td&gt;             &lt;td&gt;対象データ無し&lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;1&lt;/td&gt;             &lt;td&gt;過去10営業日より20位以上上昇&lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;2&lt;/td&gt;             &lt;td&gt;過去10営業日より1～19位上昇&lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;3&lt;/td&gt;             &lt;td&gt;過去10営業日と変わらず&lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;4&lt;/td&gt;             &lt;td&gt;過去10営業日より1～19位下落&lt;/td&gt;         &lt;/tr&gt;         &lt;tr&gt;             &lt;td&gt;5&lt;/td&gt;             &lt;td&gt;過去10営業日より20位以上下落&lt;/td&gt;         &lt;/tr&gt;     &lt;/tbody&gt; &lt;/table&gt; | [optional] [default to undefined]
**AverageRanking** | **number** | 平均順位&lt;br&gt;※100位以下は「999」となります | [optional] [default to undefined]
**Symbol** | **string** | 銘柄コード | [optional] [default to undefined]
**SymbolName** | **string** | 銘柄名称 | [optional] [default to undefined]
**CurrentPrice** | **number** | 現在値 | [optional] [default to undefined]
**ChangeRatio** | **number** | 前日比 | [optional] [default to undefined]
**RapidPaymentPercentage** | **number** | 代金急増（％） | [optional] [default to undefined]
**Turnover** | **number** | 売買代金&lt;br&gt;売買代金を百万円単位で表示する&lt;br&gt;※十万円の位を四捨五入 | [optional] [default to undefined]
**CurrentPriceTime** | **string** | 時刻&lt;br&gt;HH:mm&lt;br&gt;※日付は返しません | [optional] [default to undefined]
**ChangePercentage** | **number** | 騰落率（%） | [optional] [default to undefined]
**ExchangeName** | **string** | 市場名 | [optional] [default to undefined]
**CategoryName** | **string** | 業種名 | [optional] [default to undefined]

## Example

```typescript
import { RankingByTradeValueResponseRankingInner } from 'kabusapi-client';

const instance: RankingByTradeValueResponseRankingInner = {
    _false,
    Trend,
    AverageRanking,
    Symbol,
    SymbolName,
    CurrentPrice,
    ChangeRatio,
    RapidPaymentPercentage,
    Turnover,
    CurrentPriceTime,
    ChangePercentage,
    ExchangeName,
    CategoryName,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
