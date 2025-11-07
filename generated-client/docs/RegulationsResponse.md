# RegulationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Symbol** | **string** | 銘柄コード&lt;br&gt; ※対象商品は、株式のみ | [optional] [default to undefined]
**RegulationsInfo** | [**Array&lt;RegulationsResponseRegulationsInfoInner&gt;**](RegulationsResponseRegulationsInfoInner.md) | 規制情報 | [optional] [default to undefined]

## Example

```typescript
import { RegulationsResponse } from 'kabusapi-client';

const instance: RegulationsResponse = {
    Symbol,
    RegulationsInfo,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
