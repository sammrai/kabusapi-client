# RequestUnregister


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Symbols** | [**Array&lt;RequestRegisterSymbolsInner&gt;**](RequestRegisterSymbolsInner.md) | ※為替銘柄を登録する場合、銘柄名は\&quot;通貨A\&quot; + \&quot;/\&quot; + \&quot;通貨B\&quot;、市場コードは\&quot;300\&quot;で指定してください。 例：\&#39;Symbol\&#39;: \&#39;EUR/USD\&#39;, \&quot;Exchange\&quot;: 300 | [optional] [default to undefined]

## Example

```typescript
import { RequestUnregister } from 'kabusapi-client';

const instance: RequestUnregister = {
    Symbols,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
