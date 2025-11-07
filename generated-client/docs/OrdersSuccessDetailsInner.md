# OrdersSuccessDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SeqNum** | **number** | ※注文明細レコードの生成順序です。&lt;br&gt;※通番であるとは限りませんが、大小による順序は保たれています。 | [optional] [default to undefined]
**ID** | **string** | 注文詳細番号 | [optional] [default to undefined]
**RecType** | **number** | 明細種別 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;受付&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;繰越&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;期限切れ&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;4&lt;/td&gt;           &lt;td&gt;発注&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;5&lt;/td&gt;           &lt;td&gt;訂正&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;6&lt;/td&gt;           &lt;td&gt;取消&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;7&lt;/td&gt;           &lt;td&gt;失効&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;8&lt;/td&gt;           &lt;td&gt;約定&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] [default to undefined]
**ExchangeID** | **string** | 取引所番号 | [optional] [default to undefined]
**State** | **number** | 状態 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;待機（発注待機）&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;処理中（発注送信中・訂正送信中・取消送信中）&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;処理済（発注済・訂正済・取消済・全約定・期限切れ）&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;4&lt;/td&gt;           &lt;td&gt;エラー&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;5&lt;/td&gt;           &lt;td&gt;削除済み&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] [default to undefined]
**TransactTime** | **string** | 処理時刻 | [optional] [default to undefined]
**OrdType** | **number** | 執行条件 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;null&lt;/td&gt;           &lt;td&gt;RecType&#x3D;[6] 取消 の場合&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0&lt;/td&gt;           &lt;td&gt;RecType&#x3D;[3] 期限切れ, [7] 失効, [8] 約定 の場合&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;ザラバ&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;寄り&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;引け&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;4&lt;/td&gt;           &lt;td&gt;不成&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;5&lt;/td&gt;           &lt;td&gt;対当指値&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;6&lt;/td&gt;           &lt;td&gt;IOC&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] [default to undefined]
**Price** | **number** | 値段 | [optional] [default to undefined]
**Qty** | **number** | 数量 | [optional] [default to undefined]
**ExecutionID** | **string** | 約定番号 | [optional] [default to undefined]
**ExecutionDay** | **string** | 約定日時 | [optional] [default to undefined]
**DelivDay** | **number** | 受渡日 | [optional] [default to undefined]
**Commission** | **number** | 手数料&lt;br&gt;※注文詳細の明細種別が約定（RecType&#x3D;8)の場合に設定。 | [optional] [default to undefined]
**CommissionTax** | **number** | 手数料消費税&lt;br&gt;※明細種別は約定（RecType&#x3D;8）の場合にのみ表示されます。 | [optional] [default to undefined]

## Example

```typescript
import { OrdersSuccessDetailsInner } from 'kabusapi-client';

const instance: OrdersSuccessDetailsInner = {
    SeqNum,
    ID,
    RecType,
    ExchangeID,
    State,
    TransactTime,
    OrdType,
    Price,
    Qty,
    ExecutionID,
    ExecutionDay,
    DelivDay,
    Commission,
    CommissionTax,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
