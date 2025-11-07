# WalletMarginSuccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**MarginAccountWallet** | **number** | 信用新規可能額 | [optional] [default to undefined]
**DepositkeepRate** | **number** | 保証金維持率&lt;br&gt;※銘柄指定の場合のみ&lt;br&gt;※銘柄が指定されなかった場合、0.0を返す。 | [optional] [default to undefined]
**ConsignmentDepositRate** | **number** | 委託保証金率&lt;br&gt;※銘柄指定の場合のみ。&lt;br&gt;※銘柄が指定されなかった場合、Noneを返す。 | [optional] [default to undefined]
**CashOfConsignmentDepositRate** | **number** | 現金委託保証金率&lt;br&gt;※銘柄指定の場合のみ。&lt;br&gt;※銘柄が指定されなかった場合、Noneを返す。 | [optional] [default to undefined]

## Example

```typescript
import { WalletMarginSuccess } from 'kabusapi-client';

const instance: WalletMarginSuccess = {
    MarginAccountWallet,
    DepositkeepRate,
    ConsignmentDepositRate,
    CashOfConsignmentDepositRate,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
