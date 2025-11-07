from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.orders_get_cashmargin import OrdersGetCashmargin
from ...models.orders_get_product import OrdersGetProduct
from ...models.orders_get_side import OrdersGetSide
from ...models.orders_get_state import OrdersGetState
from ...models.orders_success import OrdersSuccess
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    product: OrdersGetProduct | Unset = UNSET,
    id: str | Unset = UNSET,
    updtime: str | Unset = UNSET,
    details: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    state: OrdersGetState | Unset = UNSET,
    side: OrdersGetSide | Unset = UNSET,
    cashmargin: OrdersGetCashmargin | Unset = UNSET,
    x_api_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-API-KEY"] = x_api_key

    params: dict[str, Any] = {}

    json_product: str | Unset = UNSET
    if not isinstance(product, Unset):
        json_product = product.value

    params["product"] = json_product

    params["id"] = id

    params["updtime"] = updtime

    params["details"] = details

    params["symbol"] = symbol

    json_state: str | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = state.value

    params["state"] = json_state

    json_side: str | Unset = UNSET
    if not isinstance(side, Unset):
        json_side = side.value

    params["side"] = json_side

    json_cashmargin: str | Unset = UNSET
    if not isinstance(cashmargin, Unset):
        json_cashmargin = cashmargin.value

    params["cashmargin"] = json_cashmargin

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/orders",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | list[OrdersSuccess] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = OrdersSuccess.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = ErrorResponse.from_dict(response.json())

        return response_405

    if response.status_code == 413:
        response_413 = ErrorResponse.from_dict(response.json())

        return response_413

    if response.status_code == 415:
        response_415 = ErrorResponse.from_dict(response.json())

        return response_415

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | list[OrdersSuccess]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    product: OrdersGetProduct | Unset = UNSET,
    id: str | Unset = UNSET,
    updtime: str | Unset = UNSET,
    details: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    state: OrdersGetState | Unset = UNSET,
    side: OrdersGetSide | Unset = UNSET,
    cashmargin: OrdersGetCashmargin | Unset = UNSET,
    x_api_key: str,
) -> Response[ErrorResponse | list[OrdersSuccess]]:
    """注文約定照会

     注文一覧を取得します。<br>
    ※下記Queryパラメータは任意設定となります。

    Args:
        product (OrdersGetProduct | Unset):
        id (str | Unset):
        updtime (str | Unset):
        details (str | Unset):
        symbol (str | Unset):
        state (OrdersGetState | Unset):
        side (OrdersGetSide | Unset):
        cashmargin (OrdersGetCashmargin | Unset):
        x_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | list[OrdersSuccess]]
    """

    kwargs = _get_kwargs(
        product=product,
        id=id,
        updtime=updtime,
        details=details,
        symbol=symbol,
        state=state,
        side=side,
        cashmargin=cashmargin,
        x_api_key=x_api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    product: OrdersGetProduct | Unset = UNSET,
    id: str | Unset = UNSET,
    updtime: str | Unset = UNSET,
    details: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    state: OrdersGetState | Unset = UNSET,
    side: OrdersGetSide | Unset = UNSET,
    cashmargin: OrdersGetCashmargin | Unset = UNSET,
    x_api_key: str,
) -> ErrorResponse | list[OrdersSuccess] | None:
    """注文約定照会

     注文一覧を取得します。<br>
    ※下記Queryパラメータは任意設定となります。

    Args:
        product (OrdersGetProduct | Unset):
        id (str | Unset):
        updtime (str | Unset):
        details (str | Unset):
        symbol (str | Unset):
        state (OrdersGetState | Unset):
        side (OrdersGetSide | Unset):
        cashmargin (OrdersGetCashmargin | Unset):
        x_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | list[OrdersSuccess]
    """

    return sync_detailed(
        client=client,
        product=product,
        id=id,
        updtime=updtime,
        details=details,
        symbol=symbol,
        state=state,
        side=side,
        cashmargin=cashmargin,
        x_api_key=x_api_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    product: OrdersGetProduct | Unset = UNSET,
    id: str | Unset = UNSET,
    updtime: str | Unset = UNSET,
    details: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    state: OrdersGetState | Unset = UNSET,
    side: OrdersGetSide | Unset = UNSET,
    cashmargin: OrdersGetCashmargin | Unset = UNSET,
    x_api_key: str,
) -> Response[ErrorResponse | list[OrdersSuccess]]:
    """注文約定照会

     注文一覧を取得します。<br>
    ※下記Queryパラメータは任意設定となります。

    Args:
        product (OrdersGetProduct | Unset):
        id (str | Unset):
        updtime (str | Unset):
        details (str | Unset):
        symbol (str | Unset):
        state (OrdersGetState | Unset):
        side (OrdersGetSide | Unset):
        cashmargin (OrdersGetCashmargin | Unset):
        x_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | list[OrdersSuccess]]
    """

    kwargs = _get_kwargs(
        product=product,
        id=id,
        updtime=updtime,
        details=details,
        symbol=symbol,
        state=state,
        side=side,
        cashmargin=cashmargin,
        x_api_key=x_api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    product: OrdersGetProduct | Unset = UNSET,
    id: str | Unset = UNSET,
    updtime: str | Unset = UNSET,
    details: str | Unset = UNSET,
    symbol: str | Unset = UNSET,
    state: OrdersGetState | Unset = UNSET,
    side: OrdersGetSide | Unset = UNSET,
    cashmargin: OrdersGetCashmargin | Unset = UNSET,
    x_api_key: str,
) -> ErrorResponse | list[OrdersSuccess] | None:
    """注文約定照会

     注文一覧を取得します。<br>
    ※下記Queryパラメータは任意設定となります。

    Args:
        product (OrdersGetProduct | Unset):
        id (str | Unset):
        updtime (str | Unset):
        details (str | Unset):
        symbol (str | Unset):
        state (OrdersGetState | Unset):
        side (OrdersGetSide | Unset):
        cashmargin (OrdersGetCashmargin | Unset):
        x_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | list[OrdersSuccess]
    """

    return (
        await asyncio_detailed(
            client=client,
            product=product,
            id=id,
            updtime=updtime,
            details=details,
            symbol=symbol,
            state=state,
            side=side,
            cashmargin=cashmargin,
            x_api_key=x_api_key,
        )
    ).parsed
