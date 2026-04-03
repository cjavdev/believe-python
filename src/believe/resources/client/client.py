# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._resource import SyncAPIResource, AsyncAPIResource

from .ws import WsResource, AsyncWsResource, WsResourceWithRawResponse, AsyncWsResourceWithRawResponse, WsResourceWithStreamingResponse, AsyncWsResourceWithStreamingResponse

from ..._compat import cached_property

from typing_extensions import Literal, overload
from ..._types import Timeout, Headers, NotGiven, not_given, Omit, omit, NoneType, Query, Body

__all__ = ["ClientResource", "AsyncClientResource"]

class ClientResource(SyncAPIResource):
    @cached_property
    def ws(self) -> WsResource:
        """
        WebSocket endpoints for real-time bidirectional communication - Live match simulation
        """
        return WsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ClientResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cjavdev/believe-python#accessing-raw-response-data-eg-headers
        """
        return ClientResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClientResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cjavdev/believe-python#with_streaming_response
        """
        return ClientResourceWithStreamingResponse(self)

class AsyncClientResource(AsyncAPIResource):
    @cached_property
    def ws(self) -> AsyncWsResource:
        """
        WebSocket endpoints for real-time bidirectional communication - Live match simulation
        """
        return AsyncWsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncClientResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cjavdev/believe-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClientResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClientResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cjavdev/believe-python#with_streaming_response
        """
        return AsyncClientResourceWithStreamingResponse(self)

class ClientResourceWithRawResponse:
    def __init__(self, client: ClientResource) -> None:
        self._client = client

    @cached_property
    def ws(self) -> WsResourceWithRawResponse:
        """
        WebSocket endpoints for real-time bidirectional communication - Live match simulation
        """
        return WsResourceWithRawResponse(self._client.ws)

class AsyncClientResourceWithRawResponse:
    def __init__(self, client: AsyncClientResource) -> None:
        self._client = client

    @cached_property
    def ws(self) -> AsyncWsResourceWithRawResponse:
        """
        WebSocket endpoints for real-time bidirectional communication - Live match simulation
        """
        return AsyncWsResourceWithRawResponse(self._client.ws)

class ClientResourceWithStreamingResponse:
    def __init__(self, client: ClientResource) -> None:
        self._client = client

    @cached_property
    def ws(self) -> WsResourceWithStreamingResponse:
        """
        WebSocket endpoints for real-time bidirectional communication - Live match simulation
        """
        return WsResourceWithStreamingResponse(self._client.ws)

class AsyncClientResourceWithStreamingResponse:
    def __init__(self, client: AsyncClientResource) -> None:
        self._client = client

    @cached_property
    def ws(self) -> AsyncWsResourceWithStreamingResponse:
        """
        WebSocket endpoints for real-time bidirectional communication - Live match simulation
        """
        return AsyncWsResourceWithStreamingResponse(self._client.ws)