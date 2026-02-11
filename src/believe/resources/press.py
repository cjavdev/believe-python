# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import press_simulate_params
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
from ..types.press_simulate_response import PressSimulateResponse

__all__ = ["PressResource", "AsyncPressResource"]


class PressResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PressResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cjavdev/believe-python#accessing-raw-response-data-eg-headers
        """
        return PressResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PressResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cjavdev/believe-python#with_streaming_response
        """
        return PressResourceWithStreamingResponse(self)

    def simulate(
        self,
        *,
        question: str,
        hostile: bool | Omit = omit,
        topic: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PressSimulateResponse:
        """
        Get Ted's response to press conference questions.

        Args:
          question: The press question to answer

          hostile: Is this a hostile question from Trent Crimm?

          topic: Topic category

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/press",
            body=maybe_transform(
                {
                    "question": question,
                    "hostile": hostile,
                    "topic": topic,
                },
                press_simulate_params.PressSimulateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PressSimulateResponse,
        )


class AsyncPressResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPressResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cjavdev/believe-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPressResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPressResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cjavdev/believe-python#with_streaming_response
        """
        return AsyncPressResourceWithStreamingResponse(self)

    async def simulate(
        self,
        *,
        question: str,
        hostile: bool | Omit = omit,
        topic: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PressSimulateResponse:
        """
        Get Ted's response to press conference questions.

        Args:
          question: The press question to answer

          hostile: Is this a hostile question from Trent Crimm?

          topic: Topic category

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/press",
            body=await async_maybe_transform(
                {
                    "question": question,
                    "hostile": hostile,
                    "topic": topic,
                },
                press_simulate_params.PressSimulateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PressSimulateResponse,
        )


class PressResourceWithRawResponse:
    def __init__(self, press: PressResource) -> None:
        self._press = press

        self.simulate = to_raw_response_wrapper(
            press.simulate,
        )


class AsyncPressResourceWithRawResponse:
    def __init__(self, press: AsyncPressResource) -> None:
        self._press = press

        self.simulate = async_to_raw_response_wrapper(
            press.simulate,
        )


class PressResourceWithStreamingResponse:
    def __init__(self, press: PressResource) -> None:
        self._press = press

        self.simulate = to_streamed_response_wrapper(
            press.simulate,
        )


class AsyncPressResourceWithStreamingResponse:
    def __init__(self, press: AsyncPressResource) -> None:
        self._press = press

        self.simulate = async_to_streamed_response_wrapper(
            press.simulate,
        )
