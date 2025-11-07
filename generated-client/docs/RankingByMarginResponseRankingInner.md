# RankingByMarginResponseRankingInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_false** | **number** | 順位&lt;br&gt;※ランキング内で同じ順位が返却される場合があります（10位が2件など） | [optional] [default to undefined]
**Symbol** | **string** | 銘柄コード | [optional] [default to undefined]
**SymbolName** | **string** | 銘柄名称 | [optional] [default to undefined]
**SellRapidPaymentPercentage** | **number** | 売残（千株） | [optional] [default to undefined]
**SellLastWeekRatio** | **number** | 売残前週比 | [optional] [default to undefined]
**BuyRapidPaymentPercentage** | **number** | 買残（千株） | [optional] [default to undefined]
**BuyLastWeekRatio** | **number** | 買残前週比 | [optional] [default to undefined]
**Ratio** | **number** | 倍率 | [optional] [default to undefined]
**ExchangeName** | **string** | 市場名 | [optional] [default to undefined]
**CategoryName** | **string** | 業種名 | [optional] [default to undefined]

## Example

```typescript
import { RankingByMarginResponseRankingInner } from 'kabusapi-client';

const instance: RankingByMarginResponseRankingInner = {
    _false,
    Symbol,
    SymbolName,
    SellRapidPaymentPercentage,
    SellLastWeekRatio,
    BuyRapidPaymentPercentage,
    BuyLastWeekRatio,
    Ratio,
    ExchangeName,
    CategoryName,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
