# WalletOptionSuccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**OptionBuyTradeLimit** | **number** | 買新規建玉可能額 | [optional] [default to undefined]
**OptionSellTradeLimit** | **number** | 売新規建玉可能額 | [optional] [default to undefined]
**MarginRequirement** | **number** | 必要証拠金額&lt;br&gt;※銘柄指定の場合のみ。&lt;br&gt;※銘柄が指定されなかった場合、空を返す。 | [optional] [default to undefined]

## Example

```typescript
import { WalletOptionSuccess } from 'kabusapi-client';

const instance: WalletOptionSuccess = {
    OptionBuyTradeLimit,
    OptionSellTradeLimit,
    MarginRequirement,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
