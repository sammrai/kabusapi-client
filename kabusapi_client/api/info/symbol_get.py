from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.symbol_success import SymbolSuccess
from ...types import UNSET, Response, Unset


def _get_kwargs(
    symbol: str,
    *,
    addinfo: str | Unset = UNSET,
    x_api_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-API-KEY"] = x_api_key

    params: dict[str, Any] = {}

    params["addinfo"] = addinfo

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/symbol/{symbol}",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | SymbolSuccess | None:
    if response.status_code == 200:
        response_200 = SymbolSuccess.from_dict(response.json())

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
) -> Response[ErrorResponse | SymbolSuccess]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    symbol: str,
    *,
    client: AuthenticatedClient | Client,
    addinfo: str | Unset = UNSET,
    x_api_key: str,
) -> Response[ErrorResponse | SymbolSuccess]:
    """銘柄情報

     指定した銘柄情報を取得します

    Args:
        symbol (str):
        addinfo (str | Unset):
        x_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SymbolSuccess]
    """

    kwargs = _get_kwargs(
        symbol=symbol,
        addinfo=addinfo,
        x_api_key=x_api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    symbol: str,
    *,
    client: AuthenticatedClient | Client,
    addinfo: str | Unset = UNSET,
    x_api_key: str,
) -> ErrorResponse | SymbolSuccess | None:
    """銘柄情報

     指定した銘柄情報を取得します

    Args:
        symbol (str):
        addinfo (str | Unset):
        x_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SymbolSuccess
    """

    return sync_detailed(
        symbol=symbol,
        client=client,
        addinfo=addinfo,
        x_api_key=x_api_key,
    ).parsed


async def asyncio_detailed(
    symbol: str,
    *,
    client: AuthenticatedClient | Client,
    addinfo: str | Unset = UNSET,
    x_api_key: str,
) -> Response[ErrorResponse | SymbolSuccess]:
    """銘柄情報

     指定した銘柄情報を取得します

    Args:
        symbol (str):
        addinfo (str | Unset):
        x_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SymbolSuccess]
    """

    kwargs = _get_kwargs(
        symbol=symbol,
        addinfo=addinfo,
        x_api_key=x_api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    symbol: str,
    *,
    client: AuthenticatedClient | Client,
    addinfo: str | Unset = UNSET,
    x_api_key: str,
) -> ErrorResponse | SymbolSuccess | None:
    """銘柄情報

     指定した銘柄情報を取得します

    Args:
        symbol (str):
        addinfo (str | Unset):
        x_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SymbolSuccess
    """

    return (
        await asyncio_detailed(
            symbol=symbol,
            client=client,
            addinfo=addinfo,
            x_api_key=x_api_key,
        )
    ).parsed
