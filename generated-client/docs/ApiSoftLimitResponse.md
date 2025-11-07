# ApiSoftLimitResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Stock** | **number** | 現物のワンショット上限&lt;br&gt;※単位は万円 | [optional] [default to undefined]
**Margin** | **number** | 信用のワンショット上限&lt;br&gt;※単位は万円 | [optional] [default to undefined]
**Future** | **number** | 先物のワンショット上限&lt;br&gt;※単位は枚 | [optional] [default to undefined]
**FutureMini** | **number** | ミニ先物のワンショット上限&lt;br&gt;※単位は枚 | [optional] [default to undefined]
**FutureMicro** | **number** | マイクロ先物のワンショット上限&lt;br&gt;※単位は枚 | [optional] [default to undefined]
**Option** | **number** | オプションのワンショット上限&lt;br&gt;※単位は枚 | [optional] [default to undefined]
**MiniOption** | **number** | ミニオプションのワンショット上限&lt;br&gt;※単位は枚 | [optional] [default to undefined]
**KabuSVersion** | **string** | kabuステーションのバージョン | [optional] [default to undefined]

## Example

```typescript
import { ApiSoftLimitResponse } from 'kabusapi-client';

const instance: ApiSoftLimitResponse = {
    Stock,
    Margin,
    Future,
    FutureMini,
    FutureMicro,
    Option,
    MiniOption,
    KabuSVersion,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
