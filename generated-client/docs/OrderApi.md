# OrderApi

All URIs are relative to *http://localhost:18080/kabusapi*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**cancelorderPut**](#cancelorderput) | **PUT** /cancelorder | 注文取消|
|[**sendoderFuturePost**](#sendoderfuturepost) | **POST** /sendorder/future | 注文発注（先物）|
|[**sendorderOptionPost**](#sendorderoptionpost) | **POST** /sendorder/option | 注文発注（オプション）|
|[**sendorderPost**](#sendorderpost) | **POST** /sendorder | 注文発注（現物・信用）|

# **cancelorderPut**
> OrderSuccess cancelorderPut(requestCancelOrder)

注文を取消します

### Example

```typescript
import {
    OrderApi,
    Configuration,
    RequestCancelOrder
} from 'kabusapi-client';

const configuration = new Configuration();
const apiInstance = new OrderApi(configuration);

let xAPIKEY: string; //トークン発行メソッドで取得した文字列 (default to undefined)
let requestCancelOrder: RequestCancelOrder; //

const { status, data } = await apiInstance.cancelorderPut(
    xAPIKEY,
    requestCancelOrder
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **requestCancelOrder** | **RequestCancelOrder**|  | |
| **xAPIKEY** | [**string**] | トークン発行メソッドで取得した文字列 | defaults to undefined|


### Return type

**OrderSuccess**

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

# **sendoderFuturePost**
> OrderSuccess sendoderFuturePost(requestSendOrderDerivFuture)

先物銘柄の注文を発注します。<br> 同一の銘柄に対しての注文は同時に5件ほどを上限としてご利用ください。

### Example

```typescript
import {
    OrderApi,
    Configuration,
    RequestSendOrderDerivFuture
} from 'kabusapi-client';

const configuration = new Configuration();
const apiInstance = new OrderApi(configuration);

let xAPIKEY: string; //トークン発行メソッドで取得した文字列 (default to undefined)
let requestSendOrderDerivFuture: RequestSendOrderDerivFuture; //

const { status, data } = await apiInstance.sendoderFuturePost(
    xAPIKEY,
    requestSendOrderDerivFuture
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **requestSendOrderDerivFuture** | **RequestSendOrderDerivFuture**|  | |
| **xAPIKEY** | [**string**] | トークン発行メソッドで取得した文字列 | defaults to undefined|


### Return type

**OrderSuccess**

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

# **sendorderOptionPost**
> OrderSuccess sendorderOptionPost(requestSendOrderDerivOption)

オプション銘柄の注文を発注します。<br> 同一の銘柄に対しての注文は同時に5件ほどを上限としてご利用ください。

### Example

```typescript
import {
    OrderApi,
    Configuration,
    RequestSendOrderDerivOption
} from 'kabusapi-client';

const configuration = new Configuration();
const apiInstance = new OrderApi(configuration);

let xAPIKEY: string; //トークン発行メソッドで取得した文字列 (default to undefined)
let requestSendOrderDerivOption: RequestSendOrderDerivOption; //

const { status, data } = await apiInstance.sendorderOptionPost(
    xAPIKEY,
    requestSendOrderDerivOption
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **requestSendOrderDerivOption** | **RequestSendOrderDerivOption**|  | |
| **xAPIKEY** | [**string**] | トークン発行メソッドで取得した文字列 | defaults to undefined|


### Return type

**OrderSuccess**

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

# **sendorderPost**
> OrderSuccess sendorderPost(requestSendOrder)

注文を発注します。<br> 同一の銘柄に対しての注文は同時に5件ほどを上限としてご利用ください。

### Example

```typescript
import {
    OrderApi,
    Configuration,
    RequestSendOrder
} from 'kabusapi-client';

const configuration = new Configuration();
const apiInstance = new OrderApi(configuration);

let xAPIKEY: string; //トークン発行メソッドで取得した文字列 (default to undefined)
let requestSendOrder: RequestSendOrder; //

const { status, data } = await apiInstance.sendorderPost(
    xAPIKEY,
    requestSendOrder
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **requestSendOrder** | **RequestSendOrder**|  | |
| **xAPIKEY** | [**string**] | トークン発行メソッドで取得した文字列 | defaults to undefined|


### Return type

**OrderSuccess**

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

