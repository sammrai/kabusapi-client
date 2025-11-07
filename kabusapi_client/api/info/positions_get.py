from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.positions_get_product import PositionsGetProduct
from ...models.positions_get_side import PositionsGetSide
from ...models.positions_success import PositionsSuccess
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    product: PositionsGetProduct | Unset = UNSET,
    symbol: str | Unset = UNSET,
    side: PositionsGetSide | Unset = UNSET,
    addinfo: str | Unset = UNSET,
    x_api_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-API-KEY"] = x_api_key

    params: dict[str, Any] = {}

    json_product: str | Unset = UNSET
    if not isinstance(product, Unset):
        json_product = product.value

    params["product"] = json_product

    params["symbol"] = symbol

    json_side: str | Unset = UNSET
    if not isinstance(side, Unset):
        json_side = side.value

    params["side"] = json_side

    params["addinfo"] = addinfo

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/positions",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | list[PositionsSuccess] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = PositionsSuccess.from_dict(response_200_item_data)

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
) -> Response[ErrorResponse | list[PositionsSuccess]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    product: PositionsGetProduct | Unset = UNSET,
    symbol: str | Unset = UNSET,
    side: PositionsGetSide | Unset = UNSET,
    addinfo: str | Unset = UNSET,
    x_api_key: str,
) -> Response[ErrorResponse | list[PositionsSuccess]]:
    """残高照会

     残高一覧を取得します。<br>※下記Queryパラメータは任意設定となります。

    Args:
        product (PositionsGetProduct | Unset):
        symbol (str | Unset):
        side (PositionsGetSide | Unset):
        addinfo (str | Unset):
        x_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | list[PositionsSuccess]]
    """

    kwargs = _get_kwargs(
        product=product,
        symbol=symbol,
        side=side,
        addinfo=addinfo,
        x_api_key=x_api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    product: PositionsGetProduct | Unset = UNSET,
    symbol: str | Unset = UNSET,
    side: PositionsGetSide | Unset = UNSET,
    addinfo: str | Unset = UNSET,
    x_api_key: str,
) -> ErrorResponse | list[PositionsSuccess] | None:
    """残高照会

     残高一覧を取得します。<br>※下記Queryパラメータは任意設定となります。

    Args:
        product (PositionsGetProduct | Unset):
        symbol (str | Unset):
        side (PositionsGetSide | Unset):
        addinfo (str | Unset):
        x_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | list[PositionsSuccess]
    """

    return sync_detailed(
        client=client,
        product=product,
        symbol=symbol,
        side=side,
        addinfo=addinfo,
        x_api_key=x_api_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    product: PositionsGetProduct | Unset = UNSET,
    symbol: str | Unset = UNSET,
    side: PositionsGetSide | Unset = UNSET,
    addinfo: str | Unset = UNSET,
    x_api_key: str,
) -> Response[ErrorResponse | list[PositionsSuccess]]:
    """残高照会

     残高一覧を取得します。<br>※下記Queryパラメータは任意設定となります。

    Args:
        product (PositionsGetProduct | Unset):
        symbol (str | Unset):
        side (PositionsGetSide | Unset):
        addinfo (str | Unset):
        x_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | list[PositionsSuccess]]
    """

    kwargs = _get_kwargs(
        product=product,
        symbol=symbol,
        side=side,
        addinfo=addinfo,
        x_api_key=x_api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    product: PositionsGetProduct | Unset = UNSET,
    symbol: str | Unset = UNSET,
    side: PositionsGetSide | Unset = UNSET,
    addinfo: str | Unset = UNSET,
    x_api_key: str,
) -> ErrorResponse | list[PositionsSuccess] | None:
    """残高照会

     残高一覧を取得します。<br>※下記Queryパラメータは任意設定となります。

    Args:
        product (PositionsGetProduct | Unset):
        symbol (str | Unset):
        side (PositionsGetSide | Unset):
        addinfo (str | Unset):
        x_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | list[PositionsSuccess]
    """

    return (
        await asyncio_detailed(
            client=client,
            product=product,
            symbol=symbol,
            side=side,
            addinfo=addinfo,
            x_api_key=x_api_key,
        )
    ).parsed
