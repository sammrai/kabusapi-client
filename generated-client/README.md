## kabusapi-client@1.0.0

This generator creates TypeScript/JavaScript client that utilizes [axios](https://github.com/axios/axios). The generated Node module can be used in the following environments:

Environment
* Node.js
* Webpack
* Browserify

Language level
* ES5 - you must have a Promises/A+ library installed
* ES6

Module system
* CommonJS
* ES6 module system

It can be used in both TypeScript and JavaScript. In TypeScript, the definition will be automatically resolved via `package.json`. ([Reference](https://www.typescriptlang.org/docs/handbook/declaration-files/consumption.html))

### Building

To build and compile the typescript sources to javascript use:
```
npm install
npm run build
```

### Publishing

First build the package then run `npm publish`

### Consuming

navigate to the folder of your consuming project and run one of the following commands.

_published:_

```
npm install kabusapi-client@1.0.0 --save
```

_unPublished (not recommended):_

```
npm install PATH_TO_GENERATED_PACKAGE --save
```

### Documentation for API Endpoints

All URIs are relative to *http://localhost:18080/kabusapi*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthApi* | [**tokenPost**](docs/AuthApi.md#tokenpost) | **POST** /token | トークン発行
*InfoApi* | [**apisoftlimitGet**](docs/InfoApi.md#apisoftlimitget) | **GET** /apisoftlimit | ソフトリミット
*InfoApi* | [**boardGet**](docs/InfoApi.md#boardget) | **GET** /board/{symbol} | 時価情報・板情報
*InfoApi* | [**exchangeGet**](docs/InfoApi.md#exchangeget) | **GET** /exchange/{symbol} | 為替情報
*InfoApi* | [**marginpremiumGet**](docs/InfoApi.md#marginpremiumget) | **GET** /margin/marginpremium/{symbol} | プレミアム料取得
*InfoApi* | [**ordersGet**](docs/InfoApi.md#ordersget) | **GET** /orders | 注文約定照会
*InfoApi* | [**positionsGet**](docs/InfoApi.md#positionsget) | **GET** /positions | 残高照会
*InfoApi* | [**primaryExchangeGet**](docs/InfoApi.md#primaryexchangeget) | **GET** /primaryexchange/{symbol} | 優先市場
*InfoApi* | [**rankingGet**](docs/InfoApi.md#rankingget) | **GET** /ranking | 詳細ランキング
*InfoApi* | [**regulationsGet**](docs/InfoApi.md#regulationsget) | **GET** /regulations/{symbol} | 規制情報
*InfoApi* | [**symbolGet**](docs/InfoApi.md#symbolget) | **GET** /symbol/{symbol} | 銘柄情報
*InfoApi* | [**symbolnameFutureGet**](docs/InfoApi.md#symbolnamefutureget) | **GET** /symbolname/future | 先物銘柄コード取得
*InfoApi* | [**symbolnameOptionGet**](docs/InfoApi.md#symbolnameoptionget) | **GET** /symbolname/option | オプション銘柄コード取得
*InfoApi* | [**symbolnameOptionMiniGet**](docs/InfoApi.md#symbolnameoptionminiget) | **GET** /symbolname/minioptionweekly | ミニオプション（限週）銘柄コード取得
*OrderApi* | [**cancelorderPut**](docs/OrderApi.md#cancelorderput) | **PUT** /cancelorder | 注文取消
*OrderApi* | [**sendoderFuturePost**](docs/OrderApi.md#sendoderfuturepost) | **POST** /sendorder/future | 注文発注（先物）
*OrderApi* | [**sendorderOptionPost**](docs/OrderApi.md#sendorderoptionpost) | **POST** /sendorder/option | 注文発注（オプション）
*OrderApi* | [**sendorderPost**](docs/OrderApi.md#sendorderpost) | **POST** /sendorder | 注文発注（現物・信用）
*RegisterApi* | [**registerPut**](docs/RegisterApi.md#registerput) | **PUT** /register | 銘柄登録
*RegisterApi* | [**unregisterAllPut**](docs/RegisterApi.md#unregisterallput) | **PUT** /unregister/all | 銘柄登録全解除
*RegisterApi* | [**unregisterPut**](docs/RegisterApi.md#unregisterput) | **PUT** /unregister | 銘柄登録解除
*WalletApi* | [**walletCashGet**](docs/WalletApi.md#walletcashget) | **GET** /wallet/cash | 取引余力（現物）
*WalletApi* | [**walletCashSymbolGet**](docs/WalletApi.md#walletcashsymbolget) | **GET** /wallet/cash/{symbol} | 取引余力（現物）（銘柄指定）
*WalletApi* | [**walletFutureGet**](docs/WalletApi.md#walletfutureget) | **GET** /wallet/future | 取引余力（先物）
*WalletApi* | [**walletFutureSymbolGet**](docs/WalletApi.md#walletfuturesymbolget) | **GET** /wallet/future/{symbol} | 取引余力（先物）（銘柄指定）
*WalletApi* | [**walletMarginGet**](docs/WalletApi.md#walletmarginget) | **GET** /wallet/margin | 取引余力（信用）
*WalletApi* | [**walletMarginSymbolGet**](docs/WalletApi.md#walletmarginsymbolget) | **GET** /wallet/margin/{symbol} | 取引余力（信用）（銘柄指定）
*WalletApi* | [**walletOptionGet**](docs/WalletApi.md#walletoptionget) | **GET** /wallet/option | 取引余力（オプション）
*WalletApi* | [**walletOptionSymbolGet**](docs/WalletApi.md#walletoptionsymbolget) | **GET** /wallet/option/{symbol} | 取引余力（オプション）（銘柄指定）


### Documentation For Models

 - [ApiSoftLimitResponse](docs/ApiSoftLimitResponse.md)
 - [BoardSuccess](docs/BoardSuccess.md)
 - [BoardSuccessBuy1](docs/BoardSuccessBuy1.md)
 - [BoardSuccessBuy10](docs/BoardSuccessBuy10.md)
 - [BoardSuccessBuy2](docs/BoardSuccessBuy2.md)
 - [BoardSuccessBuy3](docs/BoardSuccessBuy3.md)
 - [BoardSuccessBuy4](docs/BoardSuccessBuy4.md)
 - [BoardSuccessBuy5](docs/BoardSuccessBuy5.md)
 - [BoardSuccessBuy6](docs/BoardSuccessBuy6.md)
 - [BoardSuccessBuy7](docs/BoardSuccessBuy7.md)
 - [BoardSuccessBuy8](docs/BoardSuccessBuy8.md)
 - [BoardSuccessBuy9](docs/BoardSuccessBuy9.md)
 - [BoardSuccessSell1](docs/BoardSuccessSell1.md)
 - [BoardSuccessSell10](docs/BoardSuccessSell10.md)
 - [BoardSuccessSell2](docs/BoardSuccessSell2.md)
 - [BoardSuccessSell3](docs/BoardSuccessSell3.md)
 - [BoardSuccessSell4](docs/BoardSuccessSell4.md)
 - [BoardSuccessSell5](docs/BoardSuccessSell5.md)
 - [BoardSuccessSell6](docs/BoardSuccessSell6.md)
 - [BoardSuccessSell7](docs/BoardSuccessSell7.md)
 - [BoardSuccessSell8](docs/BoardSuccessSell8.md)
 - [BoardSuccessSell9](docs/BoardSuccessSell9.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [ExchangeResponse](docs/ExchangeResponse.md)
 - [MarginPremiumResponse](docs/MarginPremiumResponse.md)
 - [MarginPremiumResponseDayTrade](docs/MarginPremiumResponseDayTrade.md)
 - [MarginPremiumResponseGeneralMargin](docs/MarginPremiumResponseGeneralMargin.md)
 - [OrderSuccess](docs/OrderSuccess.md)
 - [OrdersSuccess](docs/OrdersSuccess.md)
 - [OrdersSuccessDetailsInner](docs/OrdersSuccessDetailsInner.md)
 - [Positions](docs/Positions.md)
 - [PositionsDeriv](docs/PositionsDeriv.md)
 - [PositionsSuccess](docs/PositionsSuccess.md)
 - [PrimaryExchangeResponse](docs/PrimaryExchangeResponse.md)
 - [RankingByCategoryResponse](docs/RankingByCategoryResponse.md)
 - [RankingByCategoryResponseRankingInner](docs/RankingByCategoryResponseRankingInner.md)
 - [RankingByMarginResponse](docs/RankingByMarginResponse.md)
 - [RankingByMarginResponseRankingInner](docs/RankingByMarginResponseRankingInner.md)
 - [RankingByTickCountResponse](docs/RankingByTickCountResponse.md)
 - [RankingByTickCountResponseRankingInner](docs/RankingByTickCountResponseRankingInner.md)
 - [RankingByTradeValueResponse](docs/RankingByTradeValueResponse.md)
 - [RankingByTradeValueResponseRankingInner](docs/RankingByTradeValueResponseRankingInner.md)
 - [RankingByTradeVolumeResponse](docs/RankingByTradeVolumeResponse.md)
 - [RankingByTradeVolumeResponseRankingInner](docs/RankingByTradeVolumeResponseRankingInner.md)
 - [RankingDefaultResponse](docs/RankingDefaultResponse.md)
 - [RankingDefaultResponseRankingInner](docs/RankingDefaultResponseRankingInner.md)
 - [RankingGet200Response](docs/RankingGet200Response.md)
 - [RegistSuccess](docs/RegistSuccess.md)
 - [RegulationsResponse](docs/RegulationsResponse.md)
 - [RegulationsResponseRegulationsInfoInner](docs/RegulationsResponseRegulationsInfoInner.md)
 - [RequestCancelOrder](docs/RequestCancelOrder.md)
 - [RequestRegister](docs/RequestRegister.md)
 - [RequestRegisterSymbolsInner](docs/RequestRegisterSymbolsInner.md)
 - [RequestSendOrder](docs/RequestSendOrder.md)
 - [RequestSendOrderDerivFuture](docs/RequestSendOrderDerivFuture.md)
 - [RequestSendOrderDerivFutureReverseLimitOrder](docs/RequestSendOrderDerivFutureReverseLimitOrder.md)
 - [RequestSendOrderDerivOption](docs/RequestSendOrderDerivOption.md)
 - [RequestSendOrderReverseLimitOrder](docs/RequestSendOrderReverseLimitOrder.md)
 - [RequestToken](docs/RequestToken.md)
 - [RequestUnregister](docs/RequestUnregister.md)
 - [SymbolNameSuccess](docs/SymbolNameSuccess.md)
 - [SymbolSuccess](docs/SymbolSuccess.md)
 - [TokenSuccess](docs/TokenSuccess.md)
 - [UnregisterAllSuccess](docs/UnregisterAllSuccess.md)
 - [WalletCashSuccess](docs/WalletCashSuccess.md)
 - [WalletFutureSuccess](docs/WalletFutureSuccess.md)
 - [WalletMarginSuccess](docs/WalletMarginSuccess.md)
 - [WalletOptionSuccess](docs/WalletOptionSuccess.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.

