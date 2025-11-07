# AuthApi

All URIs are relative to *http://localhost:18080/kabusapi*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**tokenPost**](#tokenpost) | **POST** /token | トークン発行|

# **tokenPost**
> TokenSuccess tokenPost(requestToken)

APIトークンを発行します。<br> 発行したトークンは有効である限り使用することができ、リクエストごとに発行する必要はありません。<br> 発行されたAPIトークンは以下のタイミングで無効となります。<br> ・kabuステーションを終了した時<br> ・kabuステーションからログアウトした時<br> ・別のトークンが新たに発行された時<br> ※kabuステーションは早朝、強制的にログアウトいたしますのでご留意ください。<br>

### Example

```typescript
import {
    AuthApi,
    Configuration,
    RequestToken
} from 'kabusapi-client';

const configuration = new Configuration();
const apiInstance = new AuthApi(configuration);

let requestToken: RequestToken; //

const { status, data } = await apiInstance.tokenPost(
    requestToken
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **requestToken** | **RequestToken**|  | |


### Return type

**TokenSuccess**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |
|**400** | BadRequest |  -  |
|**401** | Unauthorized |  -  |
|**403** | Forbidden |  -  |
|**404** | NotFound |  -  |
|**405** | MethodNotAllowed |  -  |
|**413** | RequestEntityTooLarge |  -  |
|**415** | UnsupportedMediaType |  -  |
|**429** | TooManyRequests |  -  |
|**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

