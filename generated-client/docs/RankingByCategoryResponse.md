# RankingByCategoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** | 種別&lt;br&gt; ※業種別値上がり率、業種別値下がり率の場合、市場は「null」になります | [optional] [default to undefined]
**ExchangeDivision** | **string** | 市場 | [optional] [default to undefined]
**Ranking** | [**Array&lt;RankingByCategoryResponseRankingInner&gt;**](RankingByCategoryResponseRankingInner.md) | ランキング | [optional] [default to undefined]

## Example

```typescript
import { RankingByCategoryResponse } from 'kabusapi-client';

const instance: RankingByCategoryResponse = {
    Type,
    ExchangeDivision,
    Ranking,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
