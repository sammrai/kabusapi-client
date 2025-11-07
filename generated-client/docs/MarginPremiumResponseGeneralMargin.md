# MarginPremiumResponseGeneralMargin

一般信用（長期）

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**MarginPremiumType** | **number** | プレミアム料入力区分 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;null&lt;/td&gt;           &lt;td&gt;一般信用（長期）非対応銘柄&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;0&lt;/td&gt;           &lt;td&gt;プレミアム料がない銘柄&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;プレミアム料が固定の銘柄&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;プレミアム料が入札で決定する銘柄&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | [optional] [default to undefined]
**MarginPremium** | **number** | 確定プレミアム料&lt;br&gt; ※入札銘柄の場合、入札受付中は随時更新します。受付時間外は、確定したプレミアム料を返します。&lt;br&gt; ※非入札銘柄の場合、常に固定値を返します。&lt;br&gt; ※信用取引不可の場合、nullを返します。&lt;br&gt; ※19:30~翌営業日のプレミアム料になります。 | [optional] [default to undefined]
**UpperMarginPremium** | **number** | 上限プレミアム料&lt;br&gt; ※プレミアム料がない場合は、nullを返します。 | [optional] [default to undefined]
**LowerMarginPremium** | **number** | 下限プレミアム料&lt;br&gt; ※プレミアム料がない場合は、nullを返します。 | [optional] [default to undefined]
**TickMarginPremium** | **number** | プレミアム料刻値&lt;br&gt; ※入札可能銘柄以外は、nullを返します。 | [optional] [default to undefined]

## Example

```typescript
import { MarginPremiumResponseGeneralMargin } from 'kabusapi-client';

const instance: MarginPremiumResponseGeneralMargin = {
    MarginPremiumType,
    MarginPremium,
    UpperMarginPremium,
    LowerMarginPremium,
    TickMarginPremium,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
