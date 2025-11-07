from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.board_success import BoardSuccess
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    symbol: str,
    *,
    x_api_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-API-KEY"] = x_api_key

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/board/{symbol}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BoardSuccess | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = BoardSuccess.from_dict(response.json())

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
) -> Response[BoardSuccess | ErrorResponse]:
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
    x_api_key: str,
) -> Response[BoardSuccess | ErrorResponse]:
    """時価情報・板情報

     指定した銘柄の時価情報・板情報を取得します<br>
    レスポンスの一部にnullが発生した場合、該当銘柄を銘柄登録をしてから、
    <br>再度時価情報・板情報APIを実行してください。

    Args:
        symbol (str):
        x_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BoardSuccess | ErrorResponse]
    """

    kwargs = _get_kwargs(
        symbol=symbol,
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
    x_api_key: str,
) -> BoardSuccess | ErrorResponse | None:
    """時価情報・板情報

     指定した銘柄の時価情報・板情報を取得します<br>
    レスポンスの一部にnullが発生した場合、該当銘柄を銘柄登録をしてから、
    <br>再度時価情報・板情報APIを実行してください。

    Args:
        symbol (str):
        x_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BoardSuccess | ErrorResponse
    """

    return sync_detailed(
        symbol=symbol,
        client=client,
        x_api_key=x_api_key,
    ).parsed


async def asyncio_detailed(
    symbol: str,
    *,
    client: AuthenticatedClient | Client,
    x_api_key: str,
) -> Response[BoardSuccess | ErrorResponse]:
    """時価情報・板情報

     指定した銘柄の時価情報・板情報を取得します<br>
    レスポンスの一部にnullが発生した場合、該当銘柄を銘柄登録をしてから、
    <br>再度時価情報・板情報APIを実行してください。

    Args:
        symbol (str):
        x_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BoardSuccess | ErrorResponse]
    """

    kwargs = _get_kwargs(
        symbol=symbol,
        x_api_key=x_api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    symbol: str,
    *,
    client: AuthenticatedClient | Client,
    x_api_key: str,
) -> BoardSuccess | ErrorResponse | None:
    """時価情報・板情報

     指定した銘柄の時価情報・板情報を取得します<br>
    レスポンスの一部にnullが発生した場合、該当銘柄を銘柄登録をしてから、
    <br>再度時価情報・板情報APIを実行してください。

    Args:
        symbol (str):
        x_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BoardSuccess | ErrorResponse
    """

    return (
        await asyncio_detailed(
            symbol=symbol,
            client=client,
            x_api_key=x_api_key,
        )
    ).parsed
