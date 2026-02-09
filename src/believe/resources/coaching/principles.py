# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncSkipLimitPage, AsyncSkipLimitPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.coaching import principle_list_params
from ...types.coaching.coaching_principle import CoachingPrinciple

__all__ = ["PrinciplesResource", "AsyncPrinciplesResource"]


class PrinciplesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PrinciplesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/believe-python#accessing-raw-response-data-eg-headers
        """
        return PrinciplesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrinciplesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/believe-python#with_streaming_response
        """
        return PrinciplesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        principle_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CoachingPrinciple:
        """
        Get details about a specific coaching principle.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not principle_id:
            raise ValueError(f"Expected a non-empty value for `principle_id` but received {principle_id!r}")
        return self._get(
            f"/coaching/principles/{principle_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CoachingPrinciple,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        skip: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSkipLimitPage[CoachingPrinciple]:
        """
        Get a paginated list of Ted Lasso's core coaching principles and philosophy.

        Args:
          limit: Maximum number of items to return (max: 100)

          skip: Number of items to skip (offset)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/coaching/principles",
            page=SyncSkipLimitPage[CoachingPrinciple],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                    },
                    principle_list_params.PrincipleListParams,
                ),
            ),
            model=CoachingPrinciple,
        )

    def get_random(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CoachingPrinciple:
        """Get a random coaching principle to inspire your day."""
        return self._get(
            "/coaching/principles/random",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CoachingPrinciple,
        )


class AsyncPrinciplesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPrinciplesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/believe-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPrinciplesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrinciplesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/believe-python#with_streaming_response
        """
        return AsyncPrinciplesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        principle_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CoachingPrinciple:
        """
        Get details about a specific coaching principle.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not principle_id:
            raise ValueError(f"Expected a non-empty value for `principle_id` but received {principle_id!r}")
        return await self._get(
            f"/coaching/principles/{principle_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CoachingPrinciple,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        skip: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CoachingPrinciple, AsyncSkipLimitPage[CoachingPrinciple]]:
        """
        Get a paginated list of Ted Lasso's core coaching principles and philosophy.

        Args:
          limit: Maximum number of items to return (max: 100)

          skip: Number of items to skip (offset)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/coaching/principles",
            page=AsyncSkipLimitPage[CoachingPrinciple],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                    },
                    principle_list_params.PrincipleListParams,
                ),
            ),
            model=CoachingPrinciple,
        )

    async def get_random(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CoachingPrinciple:
        """Get a random coaching principle to inspire your day."""
        return await self._get(
            "/coaching/principles/random",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CoachingPrinciple,
        )


class PrinciplesResourceWithRawResponse:
    def __init__(self, principles: PrinciplesResource) -> None:
        self._principles = principles

        self.retrieve = to_raw_response_wrapper(
            principles.retrieve,
        )
        self.list = to_raw_response_wrapper(
            principles.list,
        )
        self.get_random = to_raw_response_wrapper(
            principles.get_random,
        )


class AsyncPrinciplesResourceWithRawResponse:
    def __init__(self, principles: AsyncPrinciplesResource) -> None:
        self._principles = principles

        self.retrieve = async_to_raw_response_wrapper(
            principles.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            principles.list,
        )
        self.get_random = async_to_raw_response_wrapper(
            principles.get_random,
        )


class PrinciplesResourceWithStreamingResponse:
    def __init__(self, principles: PrinciplesResource) -> None:
        self._principles = principles

        self.retrieve = to_streamed_response_wrapper(
            principles.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            principles.list,
        )
        self.get_random = to_streamed_response_wrapper(
            principles.get_random,
        )


class AsyncPrinciplesResourceWithStreamingResponse:
    def __init__(self, principles: AsyncPrinciplesResource) -> None:
        self._principles = principles

        self.retrieve = async_to_streamed_response_wrapper(
            principles.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            principles.list,
        )
        self.get_random = async_to_streamed_response_wrapper(
            principles.get_random,
        )
