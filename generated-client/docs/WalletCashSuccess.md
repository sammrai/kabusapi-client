# WalletCashSuccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**StockAccountWallet** | **number** | 現物買付可能額&lt;br&gt; ※auマネーコネクトが有効の場合、auじぶん銀行の残高を含めた合計可能額を表示する&lt;br&gt; ※auマネーコネクトが無効の場合、三菱UFJ eスマート証券の可能額のみを表示する | [optional] [default to undefined]
**AuKCStockAccountWallet** | **number** | うち、三菱UFJ eスマート証券可能額 | [optional] [default to undefined]
**AuJbnStockAccountWallet** | **number** | うち、auじぶん銀行残高&lt;br&gt;※auマネーコネクトが無効の場合、「0」を表示する | [optional] [default to undefined]

## Example

```typescript
import { WalletCashSuccess } from 'kabusapi-client';

const instance: WalletCashSuccess = {
    StockAccountWallet,
    AuKCStockAccountWallet,
    AuJbnStockAccountWallet,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
