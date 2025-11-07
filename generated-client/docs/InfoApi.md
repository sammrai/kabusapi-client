# InfoApi

All URIs are relative to *http://localhost:18080/kabusapi*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**apisoftlimitGet**](#apisoftlimitget) | **GET** /apisoftlimit | ソフトリミット|
|[**boardGet**](#boardget) | **GET** /board/{symbol} | 時価情報・板情報|
|[**exchangeGet**](#exchangeget) | **GET** /exchange/{symbol} | 為替情報|
|[**marginpremiumGet**](#marginpremiumget) | **GET** /margin/marginpremium/{symbol} | プレミアム料取得|
|[**ordersGet**](#ordersget) | **GET** /orders | 注文約定照会|
|[**positionsGet**](#positionsget) | **GET** /positions | 残高照会|
|[**primaryExchangeGet**](#primaryexchangeget) | **GET** /primaryexchange/{symbol} | 優先市場|
|[**rankingGet**](#rankingget) | **GET** /ranking | 詳細ランキング|
|[**regulationsGet**](#regulationsget) | **GET** /regulations/{symbol} | 規制情報|
|[**symbolGet**](#symbolget) | **GET** /symbol/{symbol} | 銘柄情報|
|[**symbolnameFutureGet**](#symbolnamefutureget) | **GET** /symbolname/future | 先物銘柄コード取得|
|[**symbolnameOptionGet**](#symbolnameoptionget) | **GET** /symbolname/option | オプション銘柄コード取得|
|[**symbolnameOptionMiniGet**](#symbolnameoptionminiget) | **GET** /symbolname/minioptionweekly | ミニオプション（限週）銘柄コード取得|

# **apisoftlimitGet**
> ApiSoftLimitResponse apisoftlimitGet()

kabuステーションAPIのソフトリミット値を取得する

### Example

```typescript
import {
    InfoApi,
    Configuration
} from 'kabusapi-client';

const configuration = new Configuration();
const apiInstance = new InfoApi(configuration);

let xAPIKEY: string; //トークン発行メソッドで取得した文字列 (default to undefined)

const { status, data } = await apiInstance.apisoftlimitGet(
    xAPIKEY
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **xAPIKEY** | [**string**] | トークン発行メソッドで取得した文字列 | defaults to undefined|


### Return type

**ApiSoftLimitResponse**

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

# **boardGet**
> BoardSuccess boardGet()

指定した銘柄の時価情報・板情報を取得します<br> レスポンスの一部にnullが発生した場合、該当銘柄を銘柄登録をしてから、 <br>再度時価情報・板情報APIを実行してください。

### Example

```typescript
import {
    InfoApi,
    Configuration
} from 'kabusapi-client';

const configuration = new Configuration();
const apiInstance = new InfoApi(configuration);

let xAPIKEY: string; //トークン発行メソッドで取得した文字列 (default to undefined)
let symbol: string; //銘柄コード <br> ※次の形式で入力してください。<br> [銘柄コード]@[市場コード]<br> ※市場コードは下記の定義値から選択してください。<br> ※SOR市場は取扱っておりませんのでご注意ください。<b>市場コード</b><br> <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>1</td>           <td>東証</td>       </tr>       <tr>           <td>3</td>           <td>名証</td>       </tr>       <tr>           <td>5</td>           <td>福証</td>       </tr>       <tr>           <td>6</td>           <td>札証</td>       </tr>       <tr>           <td>2</td>           <td>日通し</td>       </tr>       <tr>           <td>23</td>           <td>日中</td>       </tr>       <tr>           <td>24</td>           <td>夜間</td>       </tr>   </tbody> </table> (default to undefined)

const { status, data } = await apiInstance.boardGet(
    xAPIKEY,
    symbol
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **xAPIKEY** | [**string**] | トークン発行メソッドで取得した文字列 | defaults to undefined|
| **symbol** | [**string**] | 銘柄コード &lt;br&gt; ※次の形式で入力してください。&lt;br&gt; [銘柄コード]@[市場コード]&lt;br&gt; ※市場コードは下記の定義値から選択してください。&lt;br&gt; ※SOR市場は取扱っておりませんのでご注意ください。&lt;b&gt;市場コード&lt;/b&gt;&lt;br&gt; &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;東証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;名証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;5&lt;/td&gt;           &lt;td&gt;福証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;6&lt;/td&gt;           &lt;td&gt;札証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;日通し&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;23&lt;/td&gt;           &lt;td&gt;日中&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;24&lt;/td&gt;           &lt;td&gt;夜間&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | defaults to undefined|


### Return type

**BoardSuccess**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | ※①：レスポンスにある「Bid」と「Ask」は、本来の意味である「買気配」と「売気配」と逆になっております。実際に返却される値は日本語の説明に準じたものになりますので、ご注意いただきますようお願い申し上げます。ご迷惑をおかけしまして、誠に申し訳ございません。&lt;br&gt;&lt;br&gt; 影響するキー名：&lt;br&gt; BidQty, BidPrice, BidTime, BidSign&lt;br&gt; AskQty, AskPrice, AskTime, AskSign |  -  |
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

# **exchangeGet**
> ExchangeResponse exchangeGet()

マネービューの情報を取得する

### Example

```typescript
import {
    InfoApi,
    Configuration
} from 'kabusapi-client';

const configuration = new Configuration();
const apiInstance = new InfoApi(configuration);

let xAPIKEY: string; //トークン発行メソッドで取得した文字列 (default to undefined)
let symbol: 'usdjpy' | 'eurjpy' | 'gbpjpy' | 'audjpy' | 'chfjpy' | 'cadjpy' | 'nzdjpy' | 'zarjpy' | 'eurusd' | 'gbpusd' | 'audusd'; //通貨 <table>   <thead>     <tr>       <th>定義値</th>       <th>内容</th>     </tr>   </thead>   <tbody>     <tr>       <td>usdjpy</td>       <td>USD/JPY</td>     </tr>     <tr>       <td>eurjpy</td>       <td>EUR/JPY</td>     </tr>     <tr>       <td>gbpjpy</td>       <td>GBP/JPY</td>     </tr>     <tr>       <td>audjpy</td>       <td>AUD/JPY</td>     </tr>     <tr>       <td>chfjpy</td>       <td>CHF/JPY</td>     </tr>     <tr>       <td>cadjpy</td>       <td>CAD/JPY</td>     </tr>     <tr>       <td>nzdjpy</td>       <td>NZD/JPY</td>     </tr>     <tr>       <td>zarjpy</td>       <td>ZAR/JPY</td>     </tr>     <tr>       <td>eurusd</td>       <td>EUR/USD</td>     </tr>     <tr>       <td>gbpusd</td>       <td>GBP/USD</td>     </tr>     <tr>       <td>audusd</td>       <td>AUD/USD</td>     </tr>   </tbody> </table> (default to undefined)

const { status, data } = await apiInstance.exchangeGet(
    xAPIKEY,
    symbol
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **xAPIKEY** | [**string**] | トークン発行メソッドで取得した文字列 | defaults to undefined|
| **symbol** | [**&#39;usdjpy&#39; | &#39;eurjpy&#39; | &#39;gbpjpy&#39; | &#39;audjpy&#39; | &#39;chfjpy&#39; | &#39;cadjpy&#39; | &#39;nzdjpy&#39; | &#39;zarjpy&#39; | &#39;eurusd&#39; | &#39;gbpusd&#39; | &#39;audusd&#39;**]**Array<&#39;usdjpy&#39; &#124; &#39;eurjpy&#39; &#124; &#39;gbpjpy&#39; &#124; &#39;audjpy&#39; &#124; &#39;chfjpy&#39; &#124; &#39;cadjpy&#39; &#124; &#39;nzdjpy&#39; &#124; &#39;zarjpy&#39; &#124; &#39;eurusd&#39; &#124; &#39;gbpusd&#39; &#124; &#39;audusd&#39;>** | 通貨 &lt;table&gt;   &lt;thead&gt;     &lt;tr&gt;       &lt;th&gt;定義値&lt;/th&gt;       &lt;th&gt;内容&lt;/th&gt;     &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;     &lt;tr&gt;       &lt;td&gt;usdjpy&lt;/td&gt;       &lt;td&gt;USD/JPY&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;eurjpy&lt;/td&gt;       &lt;td&gt;EUR/JPY&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;gbpjpy&lt;/td&gt;       &lt;td&gt;GBP/JPY&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;audjpy&lt;/td&gt;       &lt;td&gt;AUD/JPY&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;chfjpy&lt;/td&gt;       &lt;td&gt;CHF/JPY&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;cadjpy&lt;/td&gt;       &lt;td&gt;CAD/JPY&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;nzdjpy&lt;/td&gt;       &lt;td&gt;NZD/JPY&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;zarjpy&lt;/td&gt;       &lt;td&gt;ZAR/JPY&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;eurusd&lt;/td&gt;       &lt;td&gt;EUR/USD&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;gbpusd&lt;/td&gt;       &lt;td&gt;GBP/USD&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;audusd&lt;/td&gt;       &lt;td&gt;AUD/USD&lt;/td&gt;     &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | defaults to undefined|


### Return type

**ExchangeResponse**

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

# **marginpremiumGet**
> MarginPremiumResponse marginpremiumGet()

指定した銘柄のプレミアム料を取得するAPI

### Example

```typescript
import {
    InfoApi,
    Configuration
} from 'kabusapi-client';

const configuration = new Configuration();
const apiInstance = new InfoApi(configuration);

let xAPIKEY: string; //トークン発行メソッドで取得した文字列 (default to undefined)
let symbol: string; //銘柄コード (default to undefined)

const { status, data } = await apiInstance.marginpremiumGet(
    xAPIKEY,
    symbol
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **xAPIKEY** | [**string**] | トークン発行メソッドで取得した文字列 | defaults to undefined|
| **symbol** | [**string**] | 銘柄コード | defaults to undefined|


### Return type

**MarginPremiumResponse**

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

# **ordersGet**
> Array<OrdersSuccess> ordersGet()

注文一覧を取得します。<br> ※下記Queryパラメータは任意設定となります。

### Example

```typescript
import {
    InfoApi,
    Configuration
} from 'kabusapi-client';

const configuration = new Configuration();
const apiInstance = new InfoApi(configuration);

let xAPIKEY: string; //トークン発行メソッドで取得した文字列 (default to undefined)
let product: '0' | '1' | '2' | '3' | '4'; //取得する商品 <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>0</td>           <td>すべて </td>       </tr>       <tr>           <td>1</td>           <td>現物</td>       </tr>       <tr>           <td>2</td>           <td>信用</td>       </tr>       <tr>           <td>3</td>           <td>先物</td>       </tr>       <tr>           <td>4</td>           <td>OP</td>       </tr>   </tbody> </table> (optional) (default to undefined)
let id: string; //注文番号<br> ※指定された注文番号と一致する注文のみレスポンスします。<br> ※指定された注文番号との比較では大文字小文字を区別しません。<br> ※複数の注文番号を指定することはできません。 (optional) (default to undefined)
let updtime: string; //更新日時<br> ※形式：yyyyMMddHHmmss （例：20201201123456）<br> ※指定された更新日時以降（指定日時含む）に更新された注文のみレスポンスします。<br> ※複数の更新日時を指定することはできません。 (optional) (default to undefined)
let details: string; //注文詳細抑止 <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>true</td>           <td>注文詳細を出力する（デフォルト）</td>       </tr>       <tr>           <td>false</td>           <td>注文詳細の出力しない</td>       </tr>   </tbody> </table> (optional) (default to undefined)
let symbol: string; //銘柄コード<br>※指定された銘柄コードと一致する注文のみレスポンスします。<br>※複数の銘柄コードを指定することができません。 (optional) (default to undefined)
let state: '1' | '2' | '3' | '4' | '5'; //状態<br> ※指定された状態と一致する注文のみレスポンスします。<br> ※フィルタには数字の入力のみ受け付けます。<br> ※複数の状態を指定することはできません。 <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>1</td>           <td>待機（発注待機）</td>       </tr>       <tr>           <td>2</td>           <td>処理中（発注送信中）</td>       </tr>       <tr>           <td>3</td>           <td>処理済（発注済・訂正済）</td>       </tr>       <tr>           <td>4</td>           <td>訂正取消送信中</td>       </tr>       <tr>           <td>5</td>           <td>終了（発注エラー・取消済・全約定・失効・期限切れ）</td>       </tr>   </tbody> </table> (optional) (default to undefined)
let side: '1' | '2'; //売買区分<br> ※指定された売買区分と一致する注文のみレスポンスします。<br> ※フィルタには数字の入力のみ受け付けます。<br> ※複数の売買区分を指定することができません。 <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>1</td>           <td>売</td>       </tr>       <tr>           <td>2</td>           <td>買</td>       </tr>   </tbody> </table> (optional) (default to undefined)
let cashmargin: '2' | '3'; //取引区分<br> ※指定された取引区分と一致する注文のみレスポンスします。<br> ※フィルタには数字の入力のみ受け付けます。<br> ※複数の取引区分を指定することができません。 <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>2</td>           <td>新規</td>       </tr>       <tr>           <td>3</td>           <td>返済</td>       </tr>   </tbody> </table> (optional) (default to undefined)

const { status, data } = await apiInstance.ordersGet(
    xAPIKEY,
    product,
    id,
    updtime,
    details,
    symbol,
    state,
    side,
    cashmargin
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **xAPIKEY** | [**string**] | トークン発行メソッドで取得した文字列 | defaults to undefined|
| **product** | [**&#39;0&#39; | &#39;1&#39; | &#39;2&#39; | &#39;3&#39; | &#39;4&#39;**]**Array<&#39;0&#39; &#124; &#39;1&#39; &#124; &#39;2&#39; &#124; &#39;3&#39; &#124; &#39;4&#39;>** | 取得する商品 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;0&lt;/td&gt;           &lt;td&gt;すべて &lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;現物&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;信用&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;先物&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;4&lt;/td&gt;           &lt;td&gt;OP&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | (optional) defaults to undefined|
| **id** | [**string**] | 注文番号&lt;br&gt; ※指定された注文番号と一致する注文のみレスポンスします。&lt;br&gt; ※指定された注文番号との比較では大文字小文字を区別しません。&lt;br&gt; ※複数の注文番号を指定することはできません。 | (optional) defaults to undefined|
| **updtime** | [**string**] | 更新日時&lt;br&gt; ※形式：yyyyMMddHHmmss （例：20201201123456）&lt;br&gt; ※指定された更新日時以降（指定日時含む）に更新された注文のみレスポンスします。&lt;br&gt; ※複数の更新日時を指定することはできません。 | (optional) defaults to undefined|
| **details** | [**string**] | 注文詳細抑止 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;true&lt;/td&gt;           &lt;td&gt;注文詳細を出力する（デフォルト）&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;false&lt;/td&gt;           &lt;td&gt;注文詳細の出力しない&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | (optional) defaults to undefined|
| **symbol** | [**string**] | 銘柄コード&lt;br&gt;※指定された銘柄コードと一致する注文のみレスポンスします。&lt;br&gt;※複数の銘柄コードを指定することができません。 | (optional) defaults to undefined|
| **state** | [**&#39;1&#39; | &#39;2&#39; | &#39;3&#39; | &#39;4&#39; | &#39;5&#39;**]**Array<&#39;1&#39; &#124; &#39;2&#39; &#124; &#39;3&#39; &#124; &#39;4&#39; &#124; &#39;5&#39;>** | 状態&lt;br&gt; ※指定された状態と一致する注文のみレスポンスします。&lt;br&gt; ※フィルタには数字の入力のみ受け付けます。&lt;br&gt; ※複数の状態を指定することはできません。 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;待機（発注待機）&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;処理中（発注送信中）&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;処理済（発注済・訂正済）&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;4&lt;/td&gt;           &lt;td&gt;訂正取消送信中&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;5&lt;/td&gt;           &lt;td&gt;終了（発注エラー・取消済・全約定・失効・期限切れ）&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | (optional) defaults to undefined|
| **side** | [**&#39;1&#39; | &#39;2&#39;**]**Array<&#39;1&#39; &#124; &#39;2&#39;>** | 売買区分&lt;br&gt; ※指定された売買区分と一致する注文のみレスポンスします。&lt;br&gt; ※フィルタには数字の入力のみ受け付けます。&lt;br&gt; ※複数の売買区分を指定することができません。 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;売&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;買&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | (optional) defaults to undefined|
| **cashmargin** | [**&#39;2&#39; | &#39;3&#39;**]**Array<&#39;2&#39; &#124; &#39;3&#39;>** | 取引区分&lt;br&gt; ※指定された取引区分と一致する注文のみレスポンスします。&lt;br&gt; ※フィルタには数字の入力のみ受け付けます。&lt;br&gt; ※複数の取引区分を指定することができません。 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;新規&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;返済&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | (optional) defaults to undefined|


### Return type

**Array<OrdersSuccess>**

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

# **positionsGet**
> Array<PositionsSuccess> positionsGet()

残高一覧を取得します。<br>※下記Queryパラメータは任意設定となります。

### Example

```typescript
import {
    InfoApi,
    Configuration
} from 'kabusapi-client';

const configuration = new Configuration();
const apiInstance = new InfoApi(configuration);

let xAPIKEY: string; //トークン発行メソッドで取得した文字列 (default to undefined)
let product: '0' | '1' | '2' | '3' | '4'; //取得する商品 <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>0</td>           <td>すべて</td>       </tr>       <tr>           <td>1</td>           <td>現物</td>       </tr>       <tr>           <td>2</td>           <td>信用</td>       </tr>       <tr>           <td>3</td>           <td>先物</td>       </tr>       <tr>           <td>4</td>           <td>OP</td>       </tr>   </tbody> </table> (optional) (default to undefined)
let symbol: string; //銘柄コード<br>※指定された銘柄コードと一致するポジションのみレスポンスします。<br>※複数の銘柄コードを指定することはできません。 (optional) (default to undefined)
let side: '1' | '2'; //売買区分フィルタ<br> 指定された売買区分と一致する注文を返す <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>1</td>           <td>売</td>       </tr>       <tr>           <td>2</td>           <td>買</td>       </tr>   </tbody> </table> (optional) (default to undefined)
let addinfo: string; //追加情報出力フラグ（未指定時：true）<br> ※追加情報は、「現在値」、「評価金額」、「評価損益額」、「評価損益率」を意味します。 <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>true</td>           <td>追加情報を出力する</td>       </tr>       <tr>           <td>false</td>           <td>追加情報を出力しない</td>       </tr>   </tbody> </table> (optional) (default to undefined)

const { status, data } = await apiInstance.positionsGet(
    xAPIKEY,
    product,
    symbol,
    side,
    addinfo
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **xAPIKEY** | [**string**] | トークン発行メソッドで取得した文字列 | defaults to undefined|
| **product** | [**&#39;0&#39; | &#39;1&#39; | &#39;2&#39; | &#39;3&#39; | &#39;4&#39;**]**Array<&#39;0&#39; &#124; &#39;1&#39; &#124; &#39;2&#39; &#124; &#39;3&#39; &#124; &#39;4&#39;>** | 取得する商品 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;0&lt;/td&gt;           &lt;td&gt;すべて&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;現物&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;信用&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;先物&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;4&lt;/td&gt;           &lt;td&gt;OP&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | (optional) defaults to undefined|
| **symbol** | [**string**] | 銘柄コード&lt;br&gt;※指定された銘柄コードと一致するポジションのみレスポンスします。&lt;br&gt;※複数の銘柄コードを指定することはできません。 | (optional) defaults to undefined|
| **side** | [**&#39;1&#39; | &#39;2&#39;**]**Array<&#39;1&#39; &#124; &#39;2&#39;>** | 売買区分フィルタ&lt;br&gt; 指定された売買区分と一致する注文を返す &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;売&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;買&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | (optional) defaults to undefined|
| **addinfo** | [**string**] | 追加情報出力フラグ（未指定時：true）&lt;br&gt; ※追加情報は、「現在値」、「評価金額」、「評価損益額」、「評価損益率」を意味します。 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;true&lt;/td&gt;           &lt;td&gt;追加情報を出力する&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;false&lt;/td&gt;           &lt;td&gt;追加情報を出力しない&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | (optional) defaults to undefined|


### Return type

**Array<PositionsSuccess>**

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

# **primaryExchangeGet**
> PrimaryExchangeResponse primaryExchangeGet()

株式の優先市場を取得する

### Example

```typescript
import {
    InfoApi,
    Configuration
} from 'kabusapi-client';

const configuration = new Configuration();
const apiInstance = new InfoApi(configuration);

let xAPIKEY: string; //トークン発行メソッドで取得した文字列 (default to undefined)
let symbol: string; //銘柄コード (default to undefined)

const { status, data } = await apiInstance.primaryExchangeGet(
    xAPIKEY,
    symbol
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **xAPIKEY** | [**string**] | トークン発行メソッドで取得した文字列 | defaults to undefined|
| **symbol** | [**string**] | 銘柄コード | defaults to undefined|


### Return type

**PrimaryExchangeResponse**

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

# **rankingGet**
> RankingGet200Response rankingGet()

詳細ランキング画面と同様の各種ランキングを返します。 <br>ランキングの対象日はkabuステーションが保持している当日のデータとなります。 <br>※株価情報ランキング、業種別指数ランキングは、下記の時間帯でデータがクリアされるため、 <br>その間の詳細ランキングAPIは空レスポンスとなります。 <br>データクリア：平日7:53頃-9:00過ぎ頃 <br>※信用情報ランキングは毎週第３営業日の7:55頃にデータが更新されます。

### Example

```typescript
import {
    InfoApi,
    Configuration
} from 'kabusapi-client';

const configuration = new Configuration();
const apiInstance = new InfoApi(configuration);

let xAPIKEY: string; //トークン発行メソッドで取得した文字列 (default to undefined)
let type: '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | '10' | '11' | '12' | '13' | '14' | '15'; //種別<br> ※信用情報ランキングに「福証」「札証」を指定した場合は、空レスポンスになります <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>1</td>           <td>値上がり率（デフォルト）</td>       </tr>       <tr>           <td>2</td>           <td>値下がり率</td>       </tr>       <tr>           <td>3</td>           <td>売買高上位</td>       </tr>       <tr>           <td>4</td>           <td>売買代金</td>       </tr>       <tr>           <td>5</td>           <td>TICK回数</td>       </tr>       <tr>           <td>6</td>           <td>売買高急増</td>       </tr>       <tr>           <td>7</td>           <td>売買代金急増</td>       </tr>       <tr>           <td>8</td>           <td>信用売残増</td>       </tr>       <tr>           <td>9</td>           <td>信用売残減</td>       </tr>       <tr>           <td>10</td>           <td>信用買残増</td>       </tr>       <tr>           <td>11</td>           <td>信用買残減</td>       </tr>       <tr>           <td>12</td>           <td>信用高倍率</td>       </tr>       <tr>           <td>13</td>           <td>信用低倍率</td>       </tr>       <tr>           <td>14</td>           <td>業種別値上がり率</td>       </tr>       <tr>           <td>15</td>           <td>業種別値下がり率</td>       </tr>   </tbody> </table> (default to undefined)
let exchangeDivision: 'ALL' | 'T' | 'TP' | 'TS' | 'TG' | 'M' | 'FK' | 'S'; //市場<br> ※業種別値上がり率・値下がり率に市場を指定しても無視されます <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>ALL</td>           <td>全市場（デフォルト）</td>       </tr>       <tr>           <td>T</td>           <td>東証全体</td>       </tr>       <tr>           <td>TP</td>           <td>東証プライム</td>       </tr>       <tr>           <td>TS</td>           <td>東証スタンダード</td>       </tr>       <tr>           <td>TG</td>           <td>グロース250</td>       </tr>       <tr>           <td>M</td>           <td>名証</td>       </tr>       <tr>           <td>FK</td>           <td>福証</td>       </tr>       <tr>           <td>S</td>           <td>札証</td>       </tr>   </tbody> </table> (default to undefined)

const { status, data } = await apiInstance.rankingGet(
    xAPIKEY,
    type,
    exchangeDivision
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **xAPIKEY** | [**string**] | トークン発行メソッドで取得した文字列 | defaults to undefined|
| **type** | [**&#39;1&#39; | &#39;2&#39; | &#39;3&#39; | &#39;4&#39; | &#39;5&#39; | &#39;6&#39; | &#39;7&#39; | &#39;8&#39; | &#39;9&#39; | &#39;10&#39; | &#39;11&#39; | &#39;12&#39; | &#39;13&#39; | &#39;14&#39; | &#39;15&#39;**]**Array<&#39;1&#39; &#124; &#39;2&#39; &#124; &#39;3&#39; &#124; &#39;4&#39; &#124; &#39;5&#39; &#124; &#39;6&#39; &#124; &#39;7&#39; &#124; &#39;8&#39; &#124; &#39;9&#39; &#124; &#39;10&#39; &#124; &#39;11&#39; &#124; &#39;12&#39; &#124; &#39;13&#39; &#124; &#39;14&#39; &#124; &#39;15&#39;>** | 種別&lt;br&gt; ※信用情報ランキングに「福証」「札証」を指定した場合は、空レスポンスになります &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;値上がり率（デフォルト）&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;値下がり率&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;売買高上位&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;4&lt;/td&gt;           &lt;td&gt;売買代金&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;5&lt;/td&gt;           &lt;td&gt;TICK回数&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;6&lt;/td&gt;           &lt;td&gt;売買高急増&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;7&lt;/td&gt;           &lt;td&gt;売買代金急増&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;8&lt;/td&gt;           &lt;td&gt;信用売残増&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;9&lt;/td&gt;           &lt;td&gt;信用売残減&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;10&lt;/td&gt;           &lt;td&gt;信用買残増&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;11&lt;/td&gt;           &lt;td&gt;信用買残減&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;12&lt;/td&gt;           &lt;td&gt;信用高倍率&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;13&lt;/td&gt;           &lt;td&gt;信用低倍率&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;14&lt;/td&gt;           &lt;td&gt;業種別値上がり率&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;15&lt;/td&gt;           &lt;td&gt;業種別値下がり率&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | defaults to undefined|
| **exchangeDivision** | [**&#39;ALL&#39; | &#39;T&#39; | &#39;TP&#39; | &#39;TS&#39; | &#39;TG&#39; | &#39;M&#39; | &#39;FK&#39; | &#39;S&#39;**]**Array<&#39;ALL&#39; &#124; &#39;T&#39; &#124; &#39;TP&#39; &#124; &#39;TS&#39; &#124; &#39;TG&#39; &#124; &#39;M&#39; &#124; &#39;FK&#39; &#124; &#39;S&#39;>** | 市場&lt;br&gt; ※業種別値上がり率・値下がり率に市場を指定しても無視されます &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;ALL&lt;/td&gt;           &lt;td&gt;全市場（デフォルト）&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;T&lt;/td&gt;           &lt;td&gt;東証全体&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;TP&lt;/td&gt;           &lt;td&gt;東証プライム&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;TS&lt;/td&gt;           &lt;td&gt;東証スタンダード&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;TG&lt;/td&gt;           &lt;td&gt;グロース250&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;M&lt;/td&gt;           &lt;td&gt;名証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;FK&lt;/td&gt;           &lt;td&gt;福証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;S&lt;/td&gt;           &lt;td&gt;札証&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | defaults to undefined|


### Return type

**RankingGet200Response**

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

# **regulationsGet**
> RegulationsResponse regulationsGet()

規制情報＋空売り規制情報を取得する

### Example

```typescript
import {
    InfoApi,
    Configuration
} from 'kabusapi-client';

const configuration = new Configuration();
const apiInstance = new InfoApi(configuration);

let xAPIKEY: string; //トークン発行メソッドで取得した文字列 (default to undefined)
let symbol: string; //銘柄コード <br> ※次の形式で入力してください。<br> [銘柄コード]@[市場コード]<br> ※市場コードは下記の定義値から選択してください。 <b>市場コード</b> <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>1</td>           <td>東証</td>       </tr>       <tr>           <td>3</td>           <td>名証</td>       </tr>       <tr>           <td>5</td>           <td>福証</td>       </tr>       <tr>           <td>6</td>           <td>札証</td>       </tr>   </tbody> </table> (default to undefined)

const { status, data } = await apiInstance.regulationsGet(
    xAPIKEY,
    symbol
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **xAPIKEY** | [**string**] | トークン発行メソッドで取得した文字列 | defaults to undefined|
| **symbol** | [**string**] | 銘柄コード &lt;br&gt; ※次の形式で入力してください。&lt;br&gt; [銘柄コード]@[市場コード]&lt;br&gt; ※市場コードは下記の定義値から選択してください。 &lt;b&gt;市場コード&lt;/b&gt; &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;東証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;名証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;5&lt;/td&gt;           &lt;td&gt;福証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;6&lt;/td&gt;           &lt;td&gt;札証&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | defaults to undefined|


### Return type

**RegulationsResponse**

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

# **symbolGet**
> SymbolSuccess symbolGet()

指定した銘柄情報を取得します

### Example

```typescript
import {
    InfoApi,
    Configuration
} from 'kabusapi-client';

const configuration = new Configuration();
const apiInstance = new InfoApi(configuration);

let xAPIKEY: string; //トークン発行メソッドで取得した文字列 (default to undefined)
let symbol: string; //銘柄コード <br> ※次の形式で入力してください。<br> [銘柄コード]@[市場コード]<br> ※市場コードは下記の定義値から選択してください。<br> ※SOR市場は取扱っておりませんのでご注意ください。<b>市場コード</b><br> <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>1</td>           <td>東証</td>       </tr>       <tr>           <td>3</td>           <td>名証</td>       </tr>       <tr>           <td>5</td>           <td>福証</td>       </tr>       <tr>           <td>6</td>           <td>札証</td>       </tr>       <tr>           <td>2</td>           <td>日通し</td>       </tr>       <tr>           <td>23</td>           <td>日中</td>       </tr>       <tr>           <td>24</td>           <td>夜間</td>       </tr>   </tbody> </table> (default to undefined)
let addinfo: string; //追加情報出力フラグ（未指定時：true）<br> ※追加情報は、「時価総額」、「発行済み株式数」、「決算期日」、「清算値」を意味します。 <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>true</td>           <td>追加情報を出力する</td>       </tr>       <tr>           <td>false</td>           <td>追加情報を出力しない</td>       </tr>   </tbody> </table> (optional) (default to undefined)

const { status, data } = await apiInstance.symbolGet(
    xAPIKEY,
    symbol,
    addinfo
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **xAPIKEY** | [**string**] | トークン発行メソッドで取得した文字列 | defaults to undefined|
| **symbol** | [**string**] | 銘柄コード &lt;br&gt; ※次の形式で入力してください。&lt;br&gt; [銘柄コード]@[市場コード]&lt;br&gt; ※市場コードは下記の定義値から選択してください。&lt;br&gt; ※SOR市場は取扱っておりませんのでご注意ください。&lt;b&gt;市場コード&lt;/b&gt;&lt;br&gt; &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;1&lt;/td&gt;           &lt;td&gt;東証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;3&lt;/td&gt;           &lt;td&gt;名証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;5&lt;/td&gt;           &lt;td&gt;福証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;6&lt;/td&gt;           &lt;td&gt;札証&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;2&lt;/td&gt;           &lt;td&gt;日通し&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;23&lt;/td&gt;           &lt;td&gt;日中&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;24&lt;/td&gt;           &lt;td&gt;夜間&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | defaults to undefined|
| **addinfo** | [**string**] | 追加情報出力フラグ（未指定時：true）&lt;br&gt; ※追加情報は、「時価総額」、「発行済み株式数」、「決算期日」、「清算値」を意味します。 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;true&lt;/td&gt;           &lt;td&gt;追加情報を出力する&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;false&lt;/td&gt;           &lt;td&gt;追加情報を出力しない&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | (optional) defaults to undefined|


### Return type

**SymbolSuccess**

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

# **symbolnameFutureGet**
> SymbolNameSuccess symbolnameFutureGet()

先物銘柄コード取得

### Example

```typescript
import {
    InfoApi,
    Configuration
} from 'kabusapi-client';

const configuration = new Configuration();
const apiInstance = new InfoApi(configuration);

let xAPIKEY: string; //トークン発行メソッドで取得した文字列 (default to undefined)
let derivMonth: number; //限月<br> ※限月はyyyyMM形式で指定します。0を指定した場合、直近限月となります。<br> ※取引最終日に「0」（直近限月）を指定した場合、日中・夜間の時間帯に関わらず、 取引最終日を迎える限月の銘柄コードを返します。取引最終日を迎える銘柄の取引は日中取引をもって終了となりますので、ご注意ください。<br> (default to undefined)
let futureCode: string; //先物コード<br> ※大文字小文字は区別しません。 <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>NK225</td>           <td>日経平均先物</td>       </tr>       <tr>           <td>NK225mini</td>           <td>日経225mini先物</td>       </tr>       <tr>           <td>TOPIX</td>           <td>TOPIX先物</td>       </tr>       <tr>           <td>TOPIXmini</td>           <td>ミニTOPIX先物</td>       </tr>       <tr>           <td>GROWTH</td>           <td>グロース250先物</td>       </tr>       <tr>           <td>JPX400</td>           <td>JPX日経400先物</td>       </tr>       <tr>           <td>DOW</td>           <td>NYダウ先物</td>       </tr>       <tr>           <td>VI</td>           <td>日経平均VI先物</td>       </tr>       <tr>           <td>Core30</td>           <td>TOPIX Core30先物</td>       </tr>       <tr>           <td>REIT</td>           <td>東証REIT指数先物</td>       </tr>       <tr>           <td>NK225micro</td>           <td>日経225マイクロ先物</td>       </tr>   </tbody> </table> (optional) (default to undefined)

const { status, data } = await apiInstance.symbolnameFutureGet(
    xAPIKEY,
    derivMonth,
    futureCode
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **xAPIKEY** | [**string**] | トークン発行メソッドで取得した文字列 | defaults to undefined|
| **derivMonth** | [**number**] | 限月&lt;br&gt; ※限月はyyyyMM形式で指定します。0を指定した場合、直近限月となります。&lt;br&gt; ※取引最終日に「0」（直近限月）を指定した場合、日中・夜間の時間帯に関わらず、 取引最終日を迎える限月の銘柄コードを返します。取引最終日を迎える銘柄の取引は日中取引をもって終了となりますので、ご注意ください。&lt;br&gt; | defaults to undefined|
| **futureCode** | [**string**] | 先物コード&lt;br&gt; ※大文字小文字は区別しません。 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;NK225&lt;/td&gt;           &lt;td&gt;日経平均先物&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;NK225mini&lt;/td&gt;           &lt;td&gt;日経225mini先物&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;TOPIX&lt;/td&gt;           &lt;td&gt;TOPIX先物&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;TOPIXmini&lt;/td&gt;           &lt;td&gt;ミニTOPIX先物&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;GROWTH&lt;/td&gt;           &lt;td&gt;グロース250先物&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;JPX400&lt;/td&gt;           &lt;td&gt;JPX日経400先物&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;DOW&lt;/td&gt;           &lt;td&gt;NYダウ先物&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;VI&lt;/td&gt;           &lt;td&gt;日経平均VI先物&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;Core30&lt;/td&gt;           &lt;td&gt;TOPIX Core30先物&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;REIT&lt;/td&gt;           &lt;td&gt;東証REIT指数先物&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;NK225micro&lt;/td&gt;           &lt;td&gt;日経225マイクロ先物&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | (optional) defaults to undefined|


### Return type

**SymbolNameSuccess**

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

# **symbolnameOptionGet**
> SymbolNameSuccess symbolnameOptionGet()

オプション銘柄コード取得

### Example

```typescript
import {
    InfoApi,
    Configuration
} from 'kabusapi-client';

const configuration = new Configuration();
const apiInstance = new InfoApi(configuration);

let xAPIKEY: string; //トークン発行メソッドで取得した文字列 (default to undefined)
let derivMonth: number; //限月<br>※限月はyyyyMM形式で指定します。0を指定した場合、直近限月となります。<br>※取引最終日に「0」（直近限月）を指定した場合、日中・夜間の時間帯に関わらず、取引最終日を迎える限月の銘柄コードを返します。取引最終日を迎える銘柄の取引は日中取引をもって終了となりますので、ご注意ください。 (default to undefined)
let putOrCall: string; //コール or プット<br> ※大文字小文字は区別しません。 <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>P</td>           <td>PUT</td>       </tr>       <tr>           <td>C</td>           <td>CALL</td>       </tr>   </tbody> </table> (default to undefined)
let strikePrice: number; //権利行使価格<br>※0を指定した場合、APIを実行した時点でのATMとなります。 (default to undefined)
let optionCode: string; //オプションコード<br> ※指定なしの場合は、日経225オプションを対象とする。<br> <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>NK225op</td>           <td>日経225オプション</td>       </tr>       <tr>           <td>NK225miniop</td>           <td>日経225ミニオプション</td>       </tr>   </tbody> </table> (optional) (default to undefined)

const { status, data } = await apiInstance.symbolnameOptionGet(
    xAPIKEY,
    derivMonth,
    putOrCall,
    strikePrice,
    optionCode
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **xAPIKEY** | [**string**] | トークン発行メソッドで取得した文字列 | defaults to undefined|
| **derivMonth** | [**number**] | 限月&lt;br&gt;※限月はyyyyMM形式で指定します。0を指定した場合、直近限月となります。&lt;br&gt;※取引最終日に「0」（直近限月）を指定した場合、日中・夜間の時間帯に関わらず、取引最終日を迎える限月の銘柄コードを返します。取引最終日を迎える銘柄の取引は日中取引をもって終了となりますので、ご注意ください。 | defaults to undefined|
| **putOrCall** | [**string**] | コール or プット&lt;br&gt; ※大文字小文字は区別しません。 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;P&lt;/td&gt;           &lt;td&gt;PUT&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;C&lt;/td&gt;           &lt;td&gt;CALL&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | defaults to undefined|
| **strikePrice** | [**number**] | 権利行使価格&lt;br&gt;※0を指定した場合、APIを実行した時点でのATMとなります。 | defaults to undefined|
| **optionCode** | [**string**] | オプションコード&lt;br&gt; ※指定なしの場合は、日経225オプションを対象とする。&lt;br&gt; &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;NK225op&lt;/td&gt;           &lt;td&gt;日経225オプション&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;NK225miniop&lt;/td&gt;           &lt;td&gt;日経225ミニオプション&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | (optional) defaults to undefined|


### Return type

**SymbolNameSuccess**

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

# **symbolnameOptionMiniGet**
> SymbolNameSuccess symbolnameOptionMiniGet()

ミニオプション（限週）銘柄コード取得

### Example

```typescript
import {
    InfoApi,
    Configuration
} from 'kabusapi-client';

const configuration = new Configuration();
const apiInstance = new InfoApi(configuration);

let xAPIKEY: string; //トークン発行メソッドで取得した文字列 (default to undefined)
let derivMonth: number; //限月<br>※限月はyyyyMM形式で指定します。0を指定した場合、直近限月となります。<br>※取引最終日に「0」（直近限月）を指定した場合、日中・夜間の時間帯に関わらず、取引最終日を迎える限月の銘柄コードを返します。取引最終日を迎える銘柄の取引は日中取引をもって終了となりますので、ご注意ください。 (default to undefined)
let derivWeekly: number; //限週<br>※限週は0,1,3,4,5のいずれかを指定します。0を指定した場合、指定した限月の直近限週となります。<br>※取引最終日に「0」（直近限週）を指定した場合、日中・夜間の時間帯に関わらず、取引最終日を迎える限週の銘柄コードを返します。取引最終日を迎える銘柄の取引は日中取引をもって終了となりますので、ご注意ください。 (default to undefined)
let putOrCall: string; //コール or プット<br> ※大文字小文字は区別しません。 <table>   <thead>       <tr>           <th>定義値</th>           <th>説明</th>       </tr>   </thead>   <tbody>       <tr>           <td>P</td>           <td>PUT</td>       </tr>       <tr>           <td>C</td>           <td>CALL</td>       </tr>   </tbody> </table> (default to undefined)
let strikePrice: number; //権利行使価格<br>※0を指定した場合、APIを実行した時点でのATMとなります。 (default to undefined)

const { status, data } = await apiInstance.symbolnameOptionMiniGet(
    xAPIKEY,
    derivMonth,
    derivWeekly,
    putOrCall,
    strikePrice
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **xAPIKEY** | [**string**] | トークン発行メソッドで取得した文字列 | defaults to undefined|
| **derivMonth** | [**number**] | 限月&lt;br&gt;※限月はyyyyMM形式で指定します。0を指定した場合、直近限月となります。&lt;br&gt;※取引最終日に「0」（直近限月）を指定した場合、日中・夜間の時間帯に関わらず、取引最終日を迎える限月の銘柄コードを返します。取引最終日を迎える銘柄の取引は日中取引をもって終了となりますので、ご注意ください。 | defaults to undefined|
| **derivWeekly** | [**number**] | 限週&lt;br&gt;※限週は0,1,3,4,5のいずれかを指定します。0を指定した場合、指定した限月の直近限週となります。&lt;br&gt;※取引最終日に「0」（直近限週）を指定した場合、日中・夜間の時間帯に関わらず、取引最終日を迎える限週の銘柄コードを返します。取引最終日を迎える銘柄の取引は日中取引をもって終了となりますので、ご注意ください。 | defaults to undefined|
| **putOrCall** | [**string**] | コール or プット&lt;br&gt; ※大文字小文字は区別しません。 &lt;table&gt;   &lt;thead&gt;       &lt;tr&gt;           &lt;th&gt;定義値&lt;/th&gt;           &lt;th&gt;説明&lt;/th&gt;       &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;       &lt;tr&gt;           &lt;td&gt;P&lt;/td&gt;           &lt;td&gt;PUT&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;           &lt;td&gt;C&lt;/td&gt;           &lt;td&gt;CALL&lt;/td&gt;       &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt; | defaults to undefined|
| **strikePrice** | [**number**] | 権利行使価格&lt;br&gt;※0を指定した場合、APIを実行した時点でのATMとなります。 | defaults to undefined|


### Return type

**SymbolNameSuccess**

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

