# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import pep_talk_retrieve_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.pep_talk_retrieve_response import PepTalkRetrieveResponse

__all__ = ["PepTalkResource", "AsyncPepTalkResource"]


class PepTalkResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PepTalkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/believe-python#accessing-raw-response-data-eg-headers
        """
        return PepTalkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PepTalkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/believe-python#with_streaming_response
        """
        return PepTalkResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        stream: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PepTalkRetrieveResponse:
        """Get a motivational pep talk from Ted Lasso himself.

        By default returns the
        complete pep talk. Add `?stream=true` to get Server-Sent Events (SSE) streaming
        the pep talk chunk by chunk.

        Args:
          stream: If true, returns SSE stream instead of full response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/pep-talk",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"stream": stream}, pep_talk_retrieve_params.PepTalkRetrieveParams),
            ),
            cast_to=PepTalkRetrieveResponse,
        )


class AsyncPepTalkResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPepTalkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/believe-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPepTalkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPepTalkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/believe-python#with_streaming_response
        """
        return AsyncPepTalkResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        stream: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PepTalkRetrieveResponse:
        """Get a motivational pep talk from Ted Lasso himself.

        By default returns the
        complete pep talk. Add `?stream=true` to get Server-Sent Events (SSE) streaming
        the pep talk chunk by chunk.

        Args:
          stream: If true, returns SSE stream instead of full response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/pep-talk",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"stream": stream}, pep_talk_retrieve_params.PepTalkRetrieveParams),
            ),
            cast_to=PepTalkRetrieveResponse,
        )


class PepTalkResourceWithRawResponse:
    def __init__(self, pep_talk: PepTalkResource) -> None:
        self._pep_talk = pep_talk

        self.retrieve = to_raw_response_wrapper(
            pep_talk.retrieve,
        )


class AsyncPepTalkResourceWithRawResponse:
    def __init__(self, pep_talk: AsyncPepTalkResource) -> None:
        self._pep_talk = pep_talk

        self.retrieve = async_to_raw_response_wrapper(
            pep_talk.retrieve,
        )


class PepTalkResourceWithStreamingResponse:
    def __init__(self, pep_talk: PepTalkResource) -> None:
        self._pep_talk = pep_talk

        self.retrieve = to_streamed_response_wrapper(
            pep_talk.retrieve,
        )


class AsyncPepTalkResourceWithStreamingResponse:
    def __init__(self, pep_talk: AsyncPepTalkResource) -> None:
        self._pep_talk = pep_talk

        self.retrieve = async_to_streamed_response_wrapper(
            pep_talk.retrieve,
        )
