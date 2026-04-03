# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._resource import SyncAPIResource, AsyncAPIResource

from .._compat import cached_property

from .._base_client import make_request_options

from .._types import NotGiven

from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

from typing_extensions import Literal, overload
from .._types import Timeout, Headers, NotGiven, not_given, Omit, omit, NoneType, Query, Body

__all__ = ["StreamResource", "AsyncStreamResource"]

class StreamResource(SyncAPIResource):
    """Server-Sent Events (SSE) streaming endpoints"""
    @cached_property
    def with_raw_response(self) -> StreamResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cjavdev/believe-python#accessing-raw-response-data-eg-headers
        """
        return StreamResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StreamResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cjavdev/believe-python#with_streaming_response
        """
        return StreamResourceWithStreamingResponse(self)

    def test_connection(self,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> object:
        """A simple SSE test endpoint that streams numbers 1-5."""
        return self._get(
            "/stream/test",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

class AsyncStreamResource(AsyncAPIResource):
    """Server-Sent Events (SSE) streaming endpoints"""
    @cached_property
    def with_raw_response(self) -> AsyncStreamResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cjavdev/believe-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStreamResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStreamResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cjavdev/believe-python#with_streaming_response
        """
        return AsyncStreamResourceWithStreamingResponse(self)

    async def test_connection(self,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,) -> object:
        """A simple SSE test endpoint that streams numbers 1-5."""
        return await self._get(
            "/stream/test",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

class StreamResourceWithRawResponse:
    def __init__(self, stream: StreamResource) -> None:
        self._stream = stream

        self.test_connection = to_raw_response_wrapper(
            stream.test_connection,
        )

class AsyncStreamResourceWithRawResponse:
    def __init__(self, stream: AsyncStreamResource) -> None:
        self._stream = stream

        self.test_connection = async_to_raw_response_wrapper(
            stream.test_connection,
        )

class StreamResourceWithStreamingResponse:
    def __init__(self, stream: StreamResource) -> None:
        self._stream = stream

        self.test_connection = to_streamed_response_wrapper(
            stream.test_connection,
        )

class AsyncStreamResourceWithStreamingResponse:
    def __init__(self, stream: AsyncStreamResource) -> None:
        self._stream = stream

        self.test_connection = async_to_streamed_response_wrapper(
            stream.test_connection,
        )