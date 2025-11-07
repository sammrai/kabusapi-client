# PositionsSuccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ExecutionID** | **string** | 約定番号&lt;br&gt;※現物取引では、nullが返ります。 | [optional] [default to undefined]
**AccountType** | **number** | 口座種別 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;一般&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;4&lt;/td&gt;           &lt;td&gt;特定&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;12&lt;/td&gt;           &lt;td&gt;法人&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] [default to undefined]
**Symbol** | **string** | 銘柄コード | [optional] [default to undefined]
**SymbolName** | **string** | 銘柄名 | [optional] [default to undefined]
**Exchange** | **number** | 市場コード &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;東証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;名証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;5&lt;/td&gt;           &lt;td&gt;福証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;6&lt;/td&gt;           &lt;td&gt;札証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;9&lt;/td&gt;           &lt;td&gt;SOR&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;27&lt;/td&gt;           &lt;td&gt;東証+&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;日通し&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;23&lt;/td&gt;           &lt;td&gt;日中&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;24&lt;/td&gt;           &lt;td&gt;夜間&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] [default to undefined]
**ExchangeName** | **string** | 市場名 | [optional] [default to undefined]
**SecurityType** | **number** | 銘柄種別&lt;br&gt;※先物・オプション銘柄の場合のみ | [optional] [default to undefined]
**ExecutionDay** | **number** | 約定日（建玉日）&lt;br&gt;※信用・先物・オプションの場合のみ&lt;br&gt;※現物取引では、nullが返ります。 | [optional] [default to undefined]
**Price** | **number** | 値段 | [optional] [default to undefined]
**LeavesQty** | **number** | 残数量（保有数量） | [optional] [default to undefined]
**HoldQty** | **number** | 拘束数量（返済のために拘束されている数量） | [optional] [default to undefined]
**Side** | **string** | 売買区分 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;売&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;買&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] [default to undefined]
**Expenses** | **number** | 諸経費&lt;br&gt;※信用・先物・オプションの場合のみ | [optional] [default to undefined]
**Commission** | **number** | 手数料&lt;br&gt;※信用・先物・オプションの場合のみ | [optional] [default to undefined]
**CommissionTax** | **number** | 手数料消費税&lt;br&gt;※信用・先物・オプションの場合のみ | [optional] [default to undefined]
**ExpireDay** | **number** | 返済期日&lt;br&gt;※信用・先物・オプションの場合のみ | [optional] [default to undefined]
**MarginTradeType** | **number** | 信用取引区分&lt;br&gt;※信用の場合のみ &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;制度信用&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;一般信用（長期）&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;一般信用（デイトレ）&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] [default to undefined]
**CurrentPrice** | **number** | 現在値&lt;br&gt;追加情報出力フラグ：falseの場合、null | [optional] [default to undefined]
**Valuation** | **number** | 評価金額&lt;br&gt;追加情報出力フラグ：falseの場合、null | [optional] [default to undefined]
**ProfitLoss** | **number** | 評価損益額&lt;br&gt;追加情報出力フラグ：falseの場合、null | [optional] [default to undefined]
**ProfitLossRate** | **number** | 評価損益率&lt;br&gt;追加情報出力フラグ：falseの場合、null | [optional] [default to undefined]

## Example

```typescript
import { PositionsSuccess } from 'kabusapi-client';

const instance: PositionsSuccess = {
    ExecutionID,
    AccountType,
    Symbol,
    SymbolName,
    Exchange,
    ExchangeName,
    SecurityType,
    ExecutionDay,
    Price,
    LeavesQty,
    HoldQty,
    Side,
    Expenses,
    Commission,
    CommissionTax,
    ExpireDay,
    MarginTradeType,
    CurrentPrice,
    Valuation,
    ProfitLoss,
    ProfitLossRate,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
