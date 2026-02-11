# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import believe_submit_params
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
from ..types.believe_submit_response import BelieveSubmitResponse

__all__ = ["BelieveResource", "AsyncBelieveResource"]


class BelieveResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BelieveResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cjavdev/believe-python#accessing-raw-response-data-eg-headers
        """
        return BelieveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BelieveResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cjavdev/believe-python#with_streaming_response
        """
        return BelieveResourceWithStreamingResponse(self)

    def submit(
        self,
        *,
        situation: str,
        situation_type: Literal[
            "work_challenge",
            "personal_setback",
            "team_conflict",
            "self_doubt",
            "big_decision",
            "failure",
            "new_beginning",
            "relationship",
        ],
        context: Optional[str] | Omit = omit,
        intensity: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BelieveSubmitResponse:
        """
        Submit your situation and receive Ted Lasso-style motivational guidance.

        Args:
          situation: Describe your situation

          situation_type: Type of situation

          context: Additional context

          intensity: How intense is the response needed (1=gentle, 10=full Ted)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/believe",
            body=maybe_transform(
                {
                    "situation": situation,
                    "situation_type": situation_type,
                    "context": context,
                    "intensity": intensity,
                },
                believe_submit_params.BelieveSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BelieveSubmitResponse,
        )


class AsyncBelieveResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBelieveResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cjavdev/believe-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBelieveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBelieveResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cjavdev/believe-python#with_streaming_response
        """
        return AsyncBelieveResourceWithStreamingResponse(self)

    async def submit(
        self,
        *,
        situation: str,
        situation_type: Literal[
            "work_challenge",
            "personal_setback",
            "team_conflict",
            "self_doubt",
            "big_decision",
            "failure",
            "new_beginning",
            "relationship",
        ],
        context: Optional[str] | Omit = omit,
        intensity: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BelieveSubmitResponse:
        """
        Submit your situation and receive Ted Lasso-style motivational guidance.

        Args:
          situation: Describe your situation

          situation_type: Type of situation

          context: Additional context

          intensity: How intense is the response needed (1=gentle, 10=full Ted)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/believe",
            body=await async_maybe_transform(
                {
                    "situation": situation,
                    "situation_type": situation_type,
                    "context": context,
                    "intensity": intensity,
                },
                believe_submit_params.BelieveSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BelieveSubmitResponse,
        )


class BelieveResourceWithRawResponse:
    def __init__(self, believe: BelieveResource) -> None:
        self._believe = believe

        self.submit = to_raw_response_wrapper(
            believe.submit,
        )


class AsyncBelieveResourceWithRawResponse:
    def __init__(self, believe: AsyncBelieveResource) -> None:
        self._believe = believe

        self.submit = async_to_raw_response_wrapper(
            believe.submit,
        )


class BelieveResourceWithStreamingResponse:
    def __init__(self, believe: BelieveResource) -> None:
        self._believe = believe

        self.submit = to_streamed_response_wrapper(
            believe.submit,
        )


class AsyncBelieveResourceWithStreamingResponse:
    def __init__(self, believe: AsyncBelieveResource) -> None:
        self._believe = believe

        self.submit = async_to_streamed_response_wrapper(
            believe.submit,
        )
