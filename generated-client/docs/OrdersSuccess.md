# OrdersSuccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ID** | **string** | 注文番号 | [optional] [default to undefined]
**State** | **number** | 状態&lt;br&gt; ※OrderStateと同一である &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;待機（発注待機）&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;処理中（発注送信中）&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;処理済（発注済・訂正済）&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;4&lt;/td&gt;           &lt;td&gt;訂正取消送信中&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;5&lt;/td&gt;           &lt;td&gt;終了（発注エラー・取消済・全約定・失効・期限切れ）&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] [default to undefined]
**OrderState** | **number** | 注文状態&lt;br&gt; ※Stateと同一である &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;待機（発注待機）&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;処理中（発注送信中）&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;処理済（発注済・訂正済）&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;4&lt;/td&gt;           &lt;td&gt;訂正取消送信中&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;5&lt;/td&gt;           &lt;td&gt;終了（発注エラー・取消済・全約定・失効・期限切れ）&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] [default to undefined]
**OrdType** | **number** | 執行条件 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;ザラバ&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;寄り&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;引け&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;4&lt;/td&gt;           &lt;td&gt;不成&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;5&lt;/td&gt;           &lt;td&gt;対当指値&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;6&lt;/td&gt;           &lt;td&gt;IOC&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] [default to undefined]
**RecvTime** | **string** | 受注日時 | [optional] [default to undefined]
**Symbol** | **string** | 銘柄コード | [optional] [default to undefined]
**SymbolName** | **string** | 銘柄名 | [optional] [default to undefined]
**Exchange** | **number** | 市場コード &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;東証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;名証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;5&lt;/td&gt;           &lt;td&gt;福証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;6&lt;/td&gt;           &lt;td&gt;札証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;9&lt;/td&gt;           &lt;td&gt;SOR&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;27&lt;/td&gt;           &lt;td&gt;東証+&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;日通し&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;23&lt;/td&gt;           &lt;td&gt;日中&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;24&lt;/td&gt;           &lt;td&gt;夜間&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] [default to undefined]
**ExchangeName** | **string** | 市場名 | [optional] [default to undefined]
**TimeInForce** | **number** | 有効期間条件&lt;br&gt;※先物・オプション銘柄の場合のみ &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;FAS&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;FAK&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;FOK&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] [default to undefined]
**Price** | **number** | 値段 | [optional] [default to undefined]
**OrderQty** | **number** | 発注数量&lt;br&gt; ※注文期限切れと失効の場合、OrderQtyはゼロになりません。&lt;br&gt; ※期限切れと失効の確認方法としては、DetailsのRecType（3: 期限切れ、7: 失効）にてご確認ください。 | [optional] [default to undefined]
**CumQty** | **number** | 約定数量 | [optional] [default to undefined]
**Side** | **string** | 売買区分 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;売&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;買&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] [default to undefined]
**CashMargin** | **number** | 取引区分 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;新規&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;返済&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] [default to undefined]
**AccountType** | **number** | 口座種別 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;一般&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;4&lt;/td&gt;           &lt;td&gt;特定&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;12&lt;/td&gt;           &lt;td&gt;法人&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] [default to undefined]
**DelivType** | **number** | 受渡区分 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;お預り金&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;auマネーコネクト&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] [default to undefined]
**ExpireDay** | **number** | 注文有効期限&lt;br&gt;yyyyMMdd形式 | [optional] [default to undefined]
**MarginTradeType** | **number** | 信用取引区分&lt;br&gt; ※信用を注文した際に表示されます。 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;制度信用&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;一般信用（長期）&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;一般信用（デイトレ）&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] [default to undefined]
**MarginPremium** | **number** | プレミアム料&lt;br&gt; ※（注文中数量＋約定済数量）×１株あたりプレミアム料として計算されます。&lt;br&gt; ※信用を注文した際に表示されます。&lt;br&gt; ※制度信用売/買、一般（長期）買、一般（デイトレ）買の場合は、Noneと返されます。&lt;br&gt; 一般（長期）売、一般（デイトレ）売の場合は、プレミアム料&#x3D;0の場合、0（ゼロ）と返されます。 | [optional] [default to undefined]
**Details** | [**Array&lt;OrdersSuccessDetailsInner&gt;**](OrdersSuccessDetailsInner.md) | 注文詳細 | [optional] [default to undefined]

## Example

```typescript
import { OrdersSuccess } from 'kabusapi-client';

const instance: OrdersSuccess = {
    ID,
    State,
    OrderState,
    OrdType,
    RecvTime,
    Symbol,
    SymbolName,
    Exchange,
    ExchangeName,
    TimeInForce,
    Price,
    OrderQty,
    CumQty,
    Side,
    CashMargin,
    AccountType,
    DelivType,
    ExpireDay,
    MarginTradeType,
    MarginPremium,
    Details,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
