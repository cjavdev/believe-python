# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import biscuit_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncSkipLimitPage, AsyncSkipLimitPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.biscuit import Biscuit

__all__ = ["BiscuitsResource", "AsyncBiscuitsResource"]


class BiscuitsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BiscuitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/believe-python#accessing-raw-response-data-eg-headers
        """
        return BiscuitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BiscuitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/believe-python#with_streaming_response
        """
        return BiscuitsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        biscuit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Biscuit:
        """
        Get a specific type of biscuit by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not biscuit_id:
            raise ValueError(f"Expected a non-empty value for `biscuit_id` but received {biscuit_id!r}")
        return self._get(
            f"/biscuits/{biscuit_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Biscuit,
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
    ) -> SyncSkipLimitPage[Biscuit]:
        """
        Get a paginated list of Ted's famous homemade biscuits! Each comes with a
        heartwarming message.

        Args:
          limit: Maximum number of items to return (max: 100)

          skip: Number of items to skip (offset)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/biscuits",
            page=SyncSkipLimitPage[Biscuit],
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
                    biscuit_list_params.BiscuitListParams,
                ),
            ),
            model=Biscuit,
        )

    def get_fresh(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Biscuit:
        """Get a single fresh biscuit with a personalized message from Ted."""
        return self._get(
            "/biscuits/fresh",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Biscuit,
        )


class AsyncBiscuitsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBiscuitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/believe-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBiscuitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBiscuitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/believe-python#with_streaming_response
        """
        return AsyncBiscuitsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        biscuit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Biscuit:
        """
        Get a specific type of biscuit by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not biscuit_id:
            raise ValueError(f"Expected a non-empty value for `biscuit_id` but received {biscuit_id!r}")
        return await self._get(
            f"/biscuits/{biscuit_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Biscuit,
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
    ) -> AsyncPaginator[Biscuit, AsyncSkipLimitPage[Biscuit]]:
        """
        Get a paginated list of Ted's famous homemade biscuits! Each comes with a
        heartwarming message.

        Args:
          limit: Maximum number of items to return (max: 100)

          skip: Number of items to skip (offset)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/biscuits",
            page=AsyncSkipLimitPage[Biscuit],
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
                    biscuit_list_params.BiscuitListParams,
                ),
            ),
            model=Biscuit,
        )

    async def get_fresh(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Biscuit:
        """Get a single fresh biscuit with a personalized message from Ted."""
        return await self._get(
            "/biscuits/fresh",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Biscuit,
        )


class BiscuitsResourceWithRawResponse:
    def __init__(self, biscuits: BiscuitsResource) -> None:
        self._biscuits = biscuits

        self.retrieve = to_raw_response_wrapper(
            biscuits.retrieve,
        )
        self.list = to_raw_response_wrapper(
            biscuits.list,
        )
        self.get_fresh = to_raw_response_wrapper(
            biscuits.get_fresh,
        )


class AsyncBiscuitsResourceWithRawResponse:
    def __init__(self, biscuits: AsyncBiscuitsResource) -> None:
        self._biscuits = biscuits

        self.retrieve = async_to_raw_response_wrapper(
            biscuits.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            biscuits.list,
        )
        self.get_fresh = async_to_raw_response_wrapper(
            biscuits.get_fresh,
        )


class BiscuitsResourceWithStreamingResponse:
    def __init__(self, biscuits: BiscuitsResource) -> None:
        self._biscuits = biscuits

        self.retrieve = to_streamed_response_wrapper(
            biscuits.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            biscuits.list,
        )
        self.get_fresh = to_streamed_response_wrapper(
            biscuits.get_fresh,
        )


class AsyncBiscuitsResourceWithStreamingResponse:
    def __init__(self, biscuits: AsyncBiscuitsResource) -> None:
        self._biscuits = biscuits

        self.retrieve = async_to_streamed_response_wrapper(
            biscuits.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            biscuits.list,
        )
        self.get_fresh = async_to_streamed_response_wrapper(
            biscuits.get_fresh,
        )
