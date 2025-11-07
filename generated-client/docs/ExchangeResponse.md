# ExchangeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Symbol** | **string** | 通貨 | [optional] [default to undefined]
**BidPrice** | **number** | BID | [optional] [default to undefined]
**Spread** | **number** | SP | [optional] [default to undefined]
**AskPrice** | **number** | ASK | [optional] [default to undefined]
**Change** | **number** | 前日比 | [optional] [default to undefined]
**Time** | **string** | 時刻 &lt;br&gt;※HH:mm:ss形式 | [optional] [default to undefined]

## Example

```typescript
import { ExchangeResponse } from 'kabusapi-client';

const instance: ExchangeResponse = {
    Symbol,
    BidPrice,
    Spread,
    AskPrice,
    Change,
    Time,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
