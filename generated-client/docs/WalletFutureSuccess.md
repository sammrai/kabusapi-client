# WalletFutureSuccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**FutureTradeLimit** | **number** | 新規建玉可能額 | [optional] [default to undefined]
**MarginRequirement** | **number** | 買い必要証拠金額&lt;br&gt;※銘柄指定の場合のみ。&lt;br&gt;※銘柄が指定されなかった場合、空を返す。 | [optional] [default to undefined]
**MarginRequirementSell** | **number** | 売り必要証拠金額&lt;br&gt;※銘柄指定の場合のみ。&lt;br&gt;※銘柄が指定されなかった場合、空を返す。 | [optional] [default to undefined]

## Example

```typescript
import { WalletFutureSuccess } from 'kabusapi-client';

const instance: WalletFutureSuccess = {
    FutureTradeLimit,
    MarginRequirement,
    MarginRequirementSell,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
