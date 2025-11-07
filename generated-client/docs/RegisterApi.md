# RegisterApi

All URIs are relative to *http://localhost:18080/kabusapi*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**registerPut**](#registerput) | **PUT** /register | 銘柄登録|
|[**unregisterAllPut**](#unregisterallput) | **PUT** /unregister/all | 銘柄登録全解除|
|[**unregisterPut**](#unregisterput) | **PUT** /unregister | 銘柄登録解除|

# **registerPut**
> RegistSuccess registerPut(requestRegister)

PUSH配信する銘柄を登録します。<br> API登録銘柄リストを開くには、kabuステーションAPIインジケーターを右クリックし「API登録銘柄リスト」を選択してください。

### Example

```typescript
import {
    RegisterApi,
    Configuration,
    RequestRegister
} from 'kabusapi-client';

const configuration = new Configuration();
const apiInstance = new RegisterApi(configuration);

let xAPIKEY: string; //トークン発行メソッドで取得した文字列 (default to undefined)
let requestRegister: RequestRegister; //登録する銘柄のリスト

const { status, data } = await apiInstance.registerPut(
    xAPIKEY,
    requestRegister
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **requestRegister** | **RequestRegister**| 登録する銘柄のリスト | |
| **xAPIKEY** | [**string**] | トークン発行メソッドで取得した文字列 | defaults to undefined|


### Return type

**RegistSuccess**

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

# **unregisterAllPut**
> UnregisterAllSuccess unregisterAllPut()

API登録銘柄リストに登録されている銘柄をすべて解除します

### Example

```typescript
import {
    RegisterApi,
    Configuration
} from 'kabusapi-client';

const configuration = new Configuration();
const apiInstance = new RegisterApi(configuration);

let xAPIKEY: string; //トークン発行メソッドで取得した文字列 (default to undefined)

const { status, data } = await apiInstance.unregisterAllPut(
    xAPIKEY
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **xAPIKEY** | [**string**] | トークン発行メソッドで取得した文字列 | defaults to undefined|


### Return type

**UnregisterAllSuccess**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
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

# **unregisterPut**
> RegistSuccess unregisterPut(requestUnregister)

API登録銘柄リストに登録されている銘柄を解除します

### Example

```typescript
import {
    RegisterApi,
    Configuration,
    RequestUnregister
} from 'kabusapi-client';

const configuration = new Configuration();
const apiInstance = new RegisterApi(configuration);

let xAPIKEY: string; //トークン発行メソッドで取得した文字列 (default to undefined)
let requestUnregister: RequestUnregister; //登録解除する銘柄のリスト

const { status, data } = await apiInstance.unregisterPut(
    xAPIKEY,
    requestUnregister
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **requestUnregister** | **RequestUnregister**| 登録解除する銘柄のリスト | |
| **xAPIKEY** | [**string**] | トークン発行メソッドで取得した文字列 | defaults to undefined|


### Return type

**RegistSuccess**

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

