# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["WsResource", "AsyncWsResource"]


class WsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cjavdev/believe-python#accessing-raw-response-data-eg-headers
        """
        return WsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cjavdev/believe-python#with_streaming_response
        """
        return WsResourceWithStreamingResponse(self)

    def test(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Simple WebSocket test endpoint for connectivity testing.

        Connect to test WebSocket functionality. The server will:

        1. Send a welcome message on connection
        2. Echo back any message you send

        ## Example

        ```javascript
        const ws = new WebSocket("ws://localhost:8000/ws/test");
        ws.onmessage = (event) => console.log(event.data);
        ws.send("Hello!"); // Server responds with echo
        ```
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/ws/test",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncWsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cjavdev/believe-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cjavdev/believe-python#with_streaming_response
        """
        return AsyncWsResourceWithStreamingResponse(self)

    async def test(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Simple WebSocket test endpoint for connectivity testing.

        Connect to test WebSocket functionality. The server will:

        1. Send a welcome message on connection
        2. Echo back any message you send

        ## Example

        ```javascript
        const ws = new WebSocket("ws://localhost:8000/ws/test");
        ws.onmessage = (event) => console.log(event.data);
        ws.send("Hello!"); // Server responds with echo
        ```
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/ws/test",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class WsResourceWithRawResponse:
    def __init__(self, ws: WsResource) -> None:
        self._ws = ws

        self.test = to_raw_response_wrapper(
            ws.test,
        )


class AsyncWsResourceWithRawResponse:
    def __init__(self, ws: AsyncWsResource) -> None:
        self._ws = ws

        self.test = async_to_raw_response_wrapper(
            ws.test,
        )


class WsResourceWithStreamingResponse:
    def __init__(self, ws: WsResource) -> None:
        self._ws = ws

        self.test = to_streamed_response_wrapper(
            ws.test,
        )


class AsyncWsResourceWithStreamingResponse:
    def __init__(self, ws: AsyncWsResource) -> None:
        self._ws = ws

        self.test = async_to_streamed_response_wrapper(
            ws.test,
        )
