from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.symbol_name_success import SymbolNameSuccess
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    future_code: str | Unset = UNSET,
    deriv_month: int,
    x_api_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-API-KEY"] = x_api_key

    params: dict[str, Any] = {}

    params["FutureCode"] = future_code

    params["DerivMonth"] = deriv_month

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/symbolname/future",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | SymbolNameSuccess | None:
    if response.status_code == 200:
        response_200 = SymbolNameSuccess.from_dict(response.json())

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
) -> Response[ErrorResponse | SymbolNameSuccess]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    future_code: str | Unset = UNSET,
    deriv_month: int,
    x_api_key: str,
) -> Response[ErrorResponse | SymbolNameSuccess]:
    """先物銘柄コード取得

     先物銘柄コード取得

    Args:
        future_code (str | Unset):
        deriv_month (int):
        x_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SymbolNameSuccess]
    """

    kwargs = _get_kwargs(
        future_code=future_code,
        deriv_month=deriv_month,
        x_api_key=x_api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    future_code: str | Unset = UNSET,
    deriv_month: int,
    x_api_key: str,
) -> ErrorResponse | SymbolNameSuccess | None:
    """先物銘柄コード取得

     先物銘柄コード取得

    Args:
        future_code (str | Unset):
        deriv_month (int):
        x_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SymbolNameSuccess
    """

    return sync_detailed(
        client=client,
        future_code=future_code,
        deriv_month=deriv_month,
        x_api_key=x_api_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    future_code: str | Unset = UNSET,
    deriv_month: int,
    x_api_key: str,
) -> Response[ErrorResponse | SymbolNameSuccess]:
    """先物銘柄コード取得

     先物銘柄コード取得

    Args:
        future_code (str | Unset):
        deriv_month (int):
        x_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SymbolNameSuccess]
    """

    kwargs = _get_kwargs(
        future_code=future_code,
        deriv_month=deriv_month,
        x_api_key=x_api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    future_code: str | Unset = UNSET,
    deriv_month: int,
    x_api_key: str,
) -> ErrorResponse | SymbolNameSuccess | None:
    """先物銘柄コード取得

     先物銘柄コード取得

    Args:
        future_code (str | Unset):
        deriv_month (int):
        x_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SymbolNameSuccess
    """

    return (
        await asyncio_detailed(
            client=client,
            future_code=future_code,
            deriv_month=deriv_month,
            x_api_key=x_api_key,
        )
    ).parsed
