# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["CommentaryResource", "AsyncCommentaryResource"]


class CommentaryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CommentaryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/believe-python#accessing-raw-response-data-eg-headers
        """
        return CommentaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CommentaryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/believe-python#with_streaming_response
        """
        return CommentaryResourceWithStreamingResponse(self)

    def stream(
        self,
        match_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Stream live match commentary for a specific match.

        Uses Server-Sent Events (SSE)
        to stream commentary events in real-time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not match_id:
            raise ValueError(f"Expected a non-empty value for `match_id` but received {match_id!r}")
        return self._post(
            f"/matches/{match_id}/commentary/stream",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncCommentaryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCommentaryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/believe-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCommentaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCommentaryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/believe-python#with_streaming_response
        """
        return AsyncCommentaryResourceWithStreamingResponse(self)

    async def stream(
        self,
        match_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Stream live match commentary for a specific match.

        Uses Server-Sent Events (SSE)
        to stream commentary events in real-time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not match_id:
            raise ValueError(f"Expected a non-empty value for `match_id` but received {match_id!r}")
        return await self._post(
            f"/matches/{match_id}/commentary/stream",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class CommentaryResourceWithRawResponse:
    def __init__(self, commentary: CommentaryResource) -> None:
        self._commentary = commentary

        self.stream = to_raw_response_wrapper(
            commentary.stream,
        )


class AsyncCommentaryResourceWithRawResponse:
    def __init__(self, commentary: AsyncCommentaryResource) -> None:
        self._commentary = commentary

        self.stream = async_to_raw_response_wrapper(
            commentary.stream,
        )


class CommentaryResourceWithStreamingResponse:
    def __init__(self, commentary: CommentaryResource) -> None:
        self._commentary = commentary

        self.stream = to_streamed_response_wrapper(
            commentary.stream,
        )


class AsyncCommentaryResourceWithStreamingResponse:
    def __init__(self, commentary: AsyncCommentaryResource) -> None:
        self._commentary = commentary

        self.stream = async_to_streamed_response_wrapper(
            commentary.stream,
        )
