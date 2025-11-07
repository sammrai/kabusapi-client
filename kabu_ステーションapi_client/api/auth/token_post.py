from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.request_token import RequestToken
from ...models.token_success import TokenSuccess
from ...types import Response


def _get_kwargs(
    *,
    body: RequestToken,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/token",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | TokenSuccess | None:
    if response.status_code == 200:
        response_200 = TokenSuccess.from_dict(response.json())

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
) -> Response[ErrorResponse | TokenSuccess]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RequestToken,
) -> Response[ErrorResponse | TokenSuccess]:
    """トークン発行

     APIトークンを発行します。<br>
    発行したトークンは有効である限り使用することができ、リクエストごとに発行する必要はありません。<br>
    発行されたAPIトークンは以下のタイミングで無効となります。<br>
    ・kabuステーションを終了した時<br>
    ・kabuステーションからログアウトした時<br>
    ・別のトークンが新たに発行された時<br>
    ※kabuステーションは早朝、強制的にログアウトいたしますのでご留意ください。<br>

    Args:
        body (RequestToken):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | TokenSuccess]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: RequestToken,
) -> ErrorResponse | TokenSuccess | None:
    """トークン発行

     APIトークンを発行します。<br>
    発行したトークンは有効である限り使用することができ、リクエストごとに発行する必要はありません。<br>
    発行されたAPIトークンは以下のタイミングで無効となります。<br>
    ・kabuステーションを終了した時<br>
    ・kabuステーションからログアウトした時<br>
    ・別のトークンが新たに発行された時<br>
    ※kabuステーションは早朝、強制的にログアウトいたしますのでご留意ください。<br>

    Args:
        body (RequestToken):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | TokenSuccess
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RequestToken,
) -> Response[ErrorResponse | TokenSuccess]:
    """トークン発行

     APIトークンを発行します。<br>
    発行したトークンは有効である限り使用することができ、リクエストごとに発行する必要はありません。<br>
    発行されたAPIトークンは以下のタイミングで無効となります。<br>
    ・kabuステーションを終了した時<br>
    ・kabuステーションからログアウトした時<br>
    ・別のトークンが新たに発行された時<br>
    ※kabuステーションは早朝、強制的にログアウトいたしますのでご留意ください。<br>

    Args:
        body (RequestToken):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | TokenSuccess]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RequestToken,
) -> ErrorResponse | TokenSuccess | None:
    """トークン発行

     APIトークンを発行します。<br>
    発行したトークンは有効である限り使用することができ、リクエストごとに発行する必要はありません。<br>
    発行されたAPIトークンは以下のタイミングで無効となります。<br>
    ・kabuステーションを終了した時<br>
    ・kabuステーションからログアウトした時<br>
    ・別のトークンが新たに発行された時<br>
    ※kabuステーションは早朝、強制的にログアウトいたしますのでご留意ください。<br>

    Args:
        body (RequestToken):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | TokenSuccess
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
