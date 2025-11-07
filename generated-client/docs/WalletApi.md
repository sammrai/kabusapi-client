# WalletApi

All URIs are relative to *http://localhost:18080/kabusapi*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**walletCashGet**](#walletcashget) | **GET** /wallet/cash | 取引余力（現物）|
|[**walletCashSymbolGet**](#walletcashsymbolget) | **GET** /wallet/cash/{symbol} | 取引余力（現物）（銘柄指定）|
|[**walletFutureGet**](#walletfutureget) | **GET** /wallet/future | 取引余力（先物）|
|[**walletFutureSymbolGet**](#walletfuturesymbolget) | **GET** /wallet/future/{symbol} | 取引余力（先物）（銘柄指定）|
|[**walletMarginGet**](#walletmarginget) | **GET** /wallet/margin | 取引余力（信用）|
|[**walletMarginSymbolGet**](#walletmarginsymbolget) | **GET** /wallet/margin/{symbol} | 取引余力（信用）（銘柄指定）|
|[**walletOptionGet**](#walletoptionget) | **GET** /wallet/option | 取引余力（オプション）|
|[**walletOptionSymbolGet**](#walletoptionsymbolget) | **GET** /wallet/option/{symbol} | 取引余力（オプション）（銘柄指定）|

# **walletCashGet**
> WalletCashSuccess walletCashGet()

口座の取引余力（現物）を取得します

### Example

```typescript
import {
    WalletApi,
    Configuration
} from 'kabusapi-client';

const configuration = new Configuration();
const apiInstance = new WalletApi(configuration);

let xAPIKEY: string; //トークン発行メソッドで取得した文字列 (default to undefined)

const { status, data } = await apiInstance.walletCashGet(
    xAPIKEY
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **xAPIKEY** | [**string**] | トークン発行メソッドで取得した文字列 | defaults to undefined|


### Return type

**WalletCashSuccess**

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

# **walletCashSymbolGet**
> WalletCashSuccess walletCashSymbolGet()

指定した銘柄の取引余力（現物）を取得します

### Example

```typescript
import {
    WalletApi,
    Configuration
} from 'kabusapi-client';

const configuration = new Configuration();
const apiInstance = new WalletApi(configuration);

let xAPIKEY: string; //トークン発行メソッドで取得した文字列 (default to undefined)
let symbol: string; //銘柄コード <br> ※次の形式で入力してください。<br> [銘柄コード]@[市場コード]<br> ※市場コードは下記の定義値から選択してください。 <b>市場コード</b> <table>   <thead>     <tr>       <th>定義値</th>       <th>説明</th>     </tr>   </thead>   <tbody>     <tr>       <td>1</td>       <td>東証</td>     </tr>     <tr>       <td>3</td>       <td>名証</td>     </tr>     <tr>           <td>5</td>           <td>福証</td>       </tr>       <tr>           <td>6</td>           <td>札証</td>       </tr>       <tr>           <td>9</td>           <td>SOR</td>       </tr>       <tr>           <td>27</td>           <td>東証+</td>       </tr>   </tbody> </table> (default to undefined)

const { status, data } = await apiInstance.walletCashSymbolGet(
    xAPIKEY,
    symbol
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **xAPIKEY** | [**string**] | トークン発行メソッドで取得した文字列 | defaults to undefined|
| **symbol** | [**string**] | 銘柄コード &lt;br&gt; ※次の形式で入力してください。&lt;br&gt; [銘柄コード]@[市場コード]&lt;br&gt; ※市場コードは下記の定義値から選択してください。 &lt;b&gt;市場コード&lt;/b&gt; &lt;table&gt;   &lt;thead&gt;     &lt;tr&gt;       &lt;th&gt;定義値&lt;/th&gt;       &lt;th&gt;説明&lt;/th&gt;     &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;     &lt;tr&gt;       &lt;td&gt;1&lt;/td&gt;       &lt;td&gt;東証&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;3&lt;/td&gt;       &lt;td&gt;名証&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;           &lt;td&gt;5&lt;/td&gt;           &lt;td&gt;福証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;6&lt;/td&gt;           &lt;td&gt;札証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;9&lt;/td&gt;           &lt;td&gt;SOR&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;27&lt;/td&gt;           &lt;td&gt;東証+&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | defaults to undefined|


### Return type

**WalletCashSuccess**

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

# **walletFutureGet**
> WalletFutureSuccess walletFutureGet()

口座の取引余力（先物）を取得します

### Example

```typescript
import {
    WalletApi,
    Configuration
} from 'kabusapi-client';

const configuration = new Configuration();
const apiInstance = new WalletApi(configuration);

let xAPIKEY: string; //トークン発行メソッドで取得した文字列 (default to undefined)

const { status, data } = await apiInstance.walletFutureGet(
    xAPIKEY
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **xAPIKEY** | [**string**] | トークン発行メソッドで取得した文字列 | defaults to undefined|


### Return type

**WalletFutureSuccess**

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

# **walletFutureSymbolGet**
> WalletFutureSuccess walletFutureSymbolGet()

指定した銘柄の取引余力（先物）を取得します

### Example

```typescript
import {
    WalletApi,
    Configuration
} from 'kabusapi-client';

const configuration = new Configuration();
const apiInstance = new WalletApi(configuration);

let xAPIKEY: string; //トークン発行メソッドで取得した文字列 (default to undefined)
let symbol: string; //銘柄コード <br> ※次の形式で入力してください。<br> [銘柄コード]@[市場コード]<br> ※市場コードは下記の定義値から選択してください。     ※SOR市場は取扱っておりませんのでご注意ください。<b>市場コード</b><br> <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>2</td>           <td>日通し</td>       </tr>       <tr>           <td>23</td>           <td>日中</td>       </tr>       <tr>           <td>24</td>           <td>夜間</td>       </tr>   </tbody> </table> (default to undefined)

const { status, data } = await apiInstance.walletFutureSymbolGet(
    xAPIKEY,
    symbol
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **xAPIKEY** | [**string**] | トークン発行メソッドで取得した文字列 | defaults to undefined|
| **symbol** | [**string**] | 銘柄コード &lt;br&gt; ※次の形式で入力してください。&lt;br&gt; [銘柄コード]@[市場コード]&lt;br&gt; ※市場コードは下記の定義値から選択してください。     ※SOR市場は取扱っておりませんのでご注意ください。&lt;b&gt;市場コード&lt;/b&gt;&lt;br&gt; &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;日通し&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;23&lt;/td&gt;           &lt;td&gt;日中&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;24&lt;/td&gt;           &lt;td&gt;夜間&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | defaults to undefined|


### Return type

**WalletFutureSuccess**

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

# **walletMarginGet**
> WalletMarginSuccess walletMarginGet()

口座の取引余力（信用）を取得します

### Example

```typescript
import {
    WalletApi,
    Configuration
} from 'kabusapi-client';

const configuration = new Configuration();
const apiInstance = new WalletApi(configuration);

let xAPIKEY: string; //トークン発行メソッドで取得した文字列 (default to undefined)

const { status, data } = await apiInstance.walletMarginGet(
    xAPIKEY
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **xAPIKEY** | [**string**] | トークン発行メソッドで取得した文字列 | defaults to undefined|


### Return type

**WalletMarginSuccess**

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

# **walletMarginSymbolGet**
> WalletMarginSuccess walletMarginSymbolGet()

指定した銘柄の取引余力（信用）を取得します

### Example

```typescript
import {
    WalletApi,
    Configuration
} from 'kabusapi-client';

const configuration = new Configuration();
const apiInstance = new WalletApi(configuration);

let xAPIKEY: string; //トークン発行メソッドで取得した文字列 (default to undefined)
let symbol: string; //銘柄コード <br> ※次の形式で入力してください。<br> [銘柄コード]@[市場コード]<br> ※市場コードは下記の定義値から選択してください。 <b>市場コード</b> <table>   <thead>     <tr>       <th>定義値</th>       <th>説明</th>     </tr>   </thead>   <tbody>     <tr>       <td>1</td>       <td>東証</td>     </tr>     <tr>       <td>3</td>       <td>名証</td>     </tr>     <tr>       <td>9</td>       <td>SOR</td>     </tr>     <tr>       <td>27</td>       <td>東証+</td>     </tr>   </tbody> </table> (default to undefined)

const { status, data } = await apiInstance.walletMarginSymbolGet(
    xAPIKEY,
    symbol
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **xAPIKEY** | [**string**] | トークン発行メソッドで取得した文字列 | defaults to undefined|
| **symbol** | [**string**] | 銘柄コード &lt;br&gt; ※次の形式で入力してください。&lt;br&gt; [銘柄コード]@[市場コード]&lt;br&gt; ※市場コードは下記の定義値から選択してください。 &lt;b&gt;市場コード&lt;/b&gt; &lt;table&gt;   &lt;thead&gt;     &lt;tr&gt;       &lt;th&gt;定義値&lt;/th&gt;       &lt;th&gt;説明&lt;/th&gt;     &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;     &lt;tr&gt;       &lt;td&gt;1&lt;/td&gt;       &lt;td&gt;東証&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;3&lt;/td&gt;       &lt;td&gt;名証&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;9&lt;/td&gt;       &lt;td&gt;SOR&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;27&lt;/td&gt;       &lt;td&gt;東証+&lt;/td&gt;     &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | defaults to undefined|


### Return type

**WalletMarginSuccess**

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

# **walletOptionGet**
> WalletOptionSuccess walletOptionGet()

口座の取引余力（オプション）を取得します

### Example

```typescript
import {
    WalletApi,
    Configuration
} from 'kabusapi-client';

const configuration = new Configuration();
const apiInstance = new WalletApi(configuration);

let xAPIKEY: string; //トークン発行メソッドで取得した文字列 (default to undefined)

const { status, data } = await apiInstance.walletOptionGet(
    xAPIKEY
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **xAPIKEY** | [**string**] | トークン発行メソッドで取得した文字列 | defaults to undefined|


### Return type

**WalletOptionSuccess**

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

# **walletOptionSymbolGet**
> WalletOptionSuccess walletOptionSymbolGet()

指定した銘柄の取引余力（オプション）を取得します

### Example

```typescript
import {
    WalletApi,
    Configuration
} from 'kabusapi-client';

const configuration = new Configuration();
const apiInstance = new WalletApi(configuration);

let xAPIKEY: string; //トークン発行メソッドで取得した文字列 (default to undefined)
let symbol: string; //銘柄コード <br> ※次の形式で入力してください。<br> [銘柄コード]@[市場コード]<br> ※市場コードは下記の定義値から選択してください。 <b>市場コード</b> <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>2</td>           <td>日通し</td>       </tr>       <tr>           <td>23</td>           <td>日中</td>       </tr>       <tr>           <td>24</td>           <td>夜間</td>       </tr>   </tbody> </table> (default to undefined)

const { status, data } = await apiInstance.walletOptionSymbolGet(
    xAPIKEY,
    symbol
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **xAPIKEY** | [**string**] | トークン発行メソッドで取得した文字列 | defaults to undefined|
| **symbol** | [**string**] | 銘柄コード &lt;br&gt; ※次の形式で入力してください。&lt;br&gt; [銘柄コード]@[市場コード]&lt;br&gt; ※市場コードは下記の定義値から選択してください。 &lt;b&gt;市場コード&lt;/b&gt; &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;日通し&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;23&lt;/td&gt;           &lt;td&gt;日中&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;24&lt;/td&gt;           &lt;td&gt;夜間&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | defaults to undefined|


### Return type

**WalletOptionSuccess**

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

