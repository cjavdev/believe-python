# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .ws import WsResource, AsyncWsResource
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ClientResource", "AsyncClientResource"]


class ClientResource(SyncAPIResource):
    @cached_property
    def ws(self) -> WsResource:
        return WsResource(self._client)


class AsyncClientResource(AsyncAPIResource):
    @cached_property
    def ws(self) -> AsyncWsResource:
        return AsyncWsResource(self._client)
