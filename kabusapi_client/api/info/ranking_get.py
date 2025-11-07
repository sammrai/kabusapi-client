from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.ranking_get_exchange_division import RankingGetExchangeDivision
from ...models.ranking_get_type import RankingGetType
from ...models.信用情報種別813 import 信用情報種別813
from ...models.株価情報種別5 import 株価情報種別5
from ...models.株価情報種別6 import 株価情報種別6
from ...models.株価情報種別7 import 株価情報種別7
from ...models.株価情報種別14 import 株価情報種別14
from ...models.業種別指数種別1415 import 業種別指数種別1415
from ...types import UNSET, Response


def _get_kwargs(
    *,
    type_: RankingGetType,
    exchange_division: RankingGetExchangeDivision,
    x_api_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-API-KEY"] = x_api_key

    params: dict[str, Any] = {}

    json_type_ = type_.value
    params["Type"] = json_type_

    json_exchange_division = exchange_division.value
    params["ExchangeDivision"] = json_exchange_division

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ranking",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ErrorResponse
    | 信用情報種別813
    | 株価情報種別14
    | 株価情報種別5
    | 株価情報種別6
    | 株価情報種別7
    | 業種別指数種別1415
    | None
):
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> 信用情報種別813 | 株価情報種別14 | 株価情報種別5 | 株価情報種別6 | 株価情報種別7 | 業種別指数種別1415:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = 株価情報種別14.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = 株価情報種別5.from_dict(data)

                return response_200_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_2 = 株価情報種別6.from_dict(data)

                return response_200_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_3 = 株価情報種別7.from_dict(data)

                return response_200_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_4 = 信用情報種別813.from_dict(data)

                return response_200_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_5 = 業種別指数種別1415.from_dict(data)

            return response_200_type_5

        response_200 = _parse_response_200(response.json())

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
) -> Response[
    ErrorResponse
    | 信用情報種別813
    | 株価情報種別14
    | 株価情報種別5
    | 株価情報種別6
    | 株価情報種別7
    | 業種別指数種別1415
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    type_: RankingGetType,
    exchange_division: RankingGetExchangeDivision,
    x_api_key: str,
) -> Response[
    ErrorResponse
    | 信用情報種別813
    | 株価情報種別14
    | 株価情報種別5
    | 株価情報種別6
    | 株価情報種別7
    | 業種別指数種別1415
]:
    """詳細ランキング

     詳細ランキング画面と同様の各種ランキングを返します。
    <br>ランキングの対象日はkabuステーションが保持している当日のデータとなります。
    <br>※株価情報ランキング、業種別指数ランキングは、下記の時間帯でデータがクリアされるため、
    <br>その間の詳細ランキングAPIは空レスポンスとなります。
    <br>データクリア：平日7:53頃-9:00過ぎ頃
    <br>※信用情報ランキングは毎週第３営業日の7:55頃にデータが更新されます。

    Args:
        type_ (RankingGetType):
        exchange_division (RankingGetExchangeDivision):
        x_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | 信用情報種別813 | 株価情報種別14 | 株価情報種別5 | 株価情報種別6 | 株価情報種別7 | 業種別指数種別1415]
    """

    kwargs = _get_kwargs(
        type_=type_,
        exchange_division=exchange_division,
        x_api_key=x_api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    type_: RankingGetType,
    exchange_division: RankingGetExchangeDivision,
    x_api_key: str,
) -> (
    ErrorResponse
    | 信用情報種別813
    | 株価情報種別14
    | 株価情報種別5
    | 株価情報種別6
    | 株価情報種別7
    | 業種別指数種別1415
    | None
):
    """詳細ランキング

     詳細ランキング画面と同様の各種ランキングを返します。
    <br>ランキングの対象日はkabuステーションが保持している当日のデータとなります。
    <br>※株価情報ランキング、業種別指数ランキングは、下記の時間帯でデータがクリアされるため、
    <br>その間の詳細ランキングAPIは空レスポンスとなります。
    <br>データクリア：平日7:53頃-9:00過ぎ頃
    <br>※信用情報ランキングは毎週第３営業日の7:55頃にデータが更新されます。

    Args:
        type_ (RankingGetType):
        exchange_division (RankingGetExchangeDivision):
        x_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | 信用情報種別813 | 株価情報種別14 | 株価情報種別5 | 株価情報種別6 | 株価情報種別7 | 業種別指数種別1415
    """

    return sync_detailed(
        client=client,
        type_=type_,
        exchange_division=exchange_division,
        x_api_key=x_api_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    type_: RankingGetType,
    exchange_division: RankingGetExchangeDivision,
    x_api_key: str,
) -> Response[
    ErrorResponse
    | 信用情報種別813
    | 株価情報種別14
    | 株価情報種別5
    | 株価情報種別6
    | 株価情報種別7
    | 業種別指数種別1415
]:
    """詳細ランキング

     詳細ランキング画面と同様の各種ランキングを返します。
    <br>ランキングの対象日はkabuステーションが保持している当日のデータとなります。
    <br>※株価情報ランキング、業種別指数ランキングは、下記の時間帯でデータがクリアされるため、
    <br>その間の詳細ランキングAPIは空レスポンスとなります。
    <br>データクリア：平日7:53頃-9:00過ぎ頃
    <br>※信用情報ランキングは毎週第３営業日の7:55頃にデータが更新されます。

    Args:
        type_ (RankingGetType):
        exchange_division (RankingGetExchangeDivision):
        x_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | 信用情報種別813 | 株価情報種別14 | 株価情報種別5 | 株価情報種別6 | 株価情報種別7 | 業種別指数種別1415]
    """

    kwargs = _get_kwargs(
        type_=type_,
        exchange_division=exchange_division,
        x_api_key=x_api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    type_: RankingGetType,
    exchange_division: RankingGetExchangeDivision,
    x_api_key: str,
) -> (
    ErrorResponse
    | 信用情報種別813
    | 株価情報種別14
    | 株価情報種別5
    | 株価情報種別6
    | 株価情報種別7
    | 業種別指数種別1415
    | None
):
    """詳細ランキング

     詳細ランキング画面と同様の各種ランキングを返します。
    <br>ランキングの対象日はkabuステーションが保持している当日のデータとなります。
    <br>※株価情報ランキング、業種別指数ランキングは、下記の時間帯でデータがクリアされるため、
    <br>その間の詳細ランキングAPIは空レスポンスとなります。
    <br>データクリア：平日7:53頃-9:00過ぎ頃
    <br>※信用情報ランキングは毎週第３営業日の7:55頃にデータが更新されます。

    Args:
        type_ (RankingGetType):
        exchange_division (RankingGetExchangeDivision):
        x_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | 信用情報種別813 | 株価情報種別14 | 株価情報種別5 | 株価情報種別6 | 株価情報種別7 | 業種別指数種別1415
    """

    return (
        await asyncio_detailed(
            client=client,
            type_=type_,
            exchange_division=exchange_division,
            x_api_key=x_api_key,
        )
    ).parsed
