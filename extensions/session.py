"""Token issuing and token-authenticated clients for the kabu STATION API.

This module is hand-written (not generated). Its source of truth is ``extensions/session.py``;
the generate-client workflow copies it to ``kabusapi_client/session.py`` after every regeneration.

Usage::

    from kabusapi_client.session import issue_token, authenticated_client, from_env

    token = issue_token(base_url, api_password)          # issues a new token (the previous one becomes invalid)
    client = authenticated_client(base_url, token)       # reuse an existing token without issuing a new one
    client = from_env()                                  # KABU_API_BASE_URL / KABU_API_PASSWORD (+ optional CF_ACCESS_CLIENT_ID / CF_ACCESS_CLIENT_SECRET)

Note: the kabu STATION API invalidates the previous token whenever a new one is issued, and every token
becomes invalid when kabu STATION logs in again. Share one token between processes and issue a new one
only after a 401.
"""
from __future__ import annotations

import os

from .api.auth import token_post
from .client import AuthenticatedClient, Client
from .models import RequestToken


def _headers(cf_access_client_id: str | None, cf_access_client_secret: str | None, token: str | None = None) -> dict[str, str]:
    """Cloudflare Access headers (when the API is exposed through Cloudflare) and the X-API-KEY header."""
    h: dict[str, str] = {}
    if cf_access_client_id and cf_access_client_secret:
        h["CF-Access-Client-Id"] = cf_access_client_id
        h["CF-Access-Client-Secret"] = cf_access_client_secret
    if token:
        h["X-API-KEY"] = token
    return h


def issue_token(base_url: str, api_password: str, cf_access_client_id: str | None = None,
                cf_access_client_secret: str | None = None) -> str:
    """Issue a new API token with the API password (POST /token). Raises RuntimeError on failure."""
    r = token_post.sync_detailed(client=Client(base_url=base_url, headers=_headers(cf_access_client_id, cf_access_client_secret)),
                                 body=RequestToken(api_password=api_password))
    if r.status_code != 200 or r.parsed is None or not getattr(r.parsed, "token", None):
        raise RuntimeError(f"failed to issue a token: HTTP {r.status_code} {r.parsed}")
    return r.parsed.token


def authenticated_client(base_url: str, token: str, cf_access_client_id: str | None = None,
                         cf_access_client_secret: str | None = None) -> AuthenticatedClient:
    """A client that sends the given token (does not issue a new one)."""
    return AuthenticatedClient(base_url=base_url, token=token, headers=_headers(cf_access_client_id, cf_access_client_secret, token))


def from_env(token: str | None = None) -> AuthenticatedClient:
    """Build a client from environment variables; issues a new token when ``token`` is None."""
    base = os.environ["KABU_API_BASE_URL"]
    cid, sec = os.environ.get("CF_ACCESS_CLIENT_ID"), os.environ.get("CF_ACCESS_CLIENT_SECRET")
    token = token or issue_token(base, os.environ["KABU_API_PASSWORD"], cid, sec)
    return authenticated_client(base, token, cid, sec)
